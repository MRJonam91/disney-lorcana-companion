"""Validated deck exports and reproducible opening-hand experiments.

These experiments draw cards; they do not simulate complete Lorcana games.
"""
from collections import Counter
from math import comb
import random
import re


def validate_catalog(decks):
    ids = set()
    for deck in decks:
        if not re.fullmatch(r'[a-z0-9-]+', deck['id']) or deck['id'] in ids:
            raise ValueError('Invalid or duplicate deck id')
        ids.add(deck['id'])
        if not deck['source'].startswith('https://'):
            raise ValueError('Source must use https')
        names = set()
        for card in deck['cards']:
            if not isinstance(card['quantity'], int) or not 1 <= card['quantity'] <= 4:
                raise ValueError('Each full card name needs 1–4 copies')
            name = card['name'].casefold()
            if name in names:
                raise ValueError('Invalid duplicate full card name')
            names.add(name)
        if sum(card['quantity'] for card in deck['cards']) != 60:
            raise ValueError('Each published deck must contain exactly 60 cards')
        if all('ink' in card for card in deck['cards']):
            if len({card['ink'] for card in deck['cards']}) > 2:
                raise ValueError('More than two inks')
        if any(card.get('set', 9) < 9 for card in deck['cards']):
            raise ValueError('Missing a Core-legal printing in this snapshot')
        if any(card.get('rarity') in ('Enchanted', 'Iconic', 'Epic') for card in deck['cards']):
            raise ValueError('Use base printings for published deck exports')


def deck_text(deck):
    return ''.join(f"{card['quantity']} {card['name']}\n" for card in deck['cards'])


def opening_metrics(deck, trials=200_000, seed=20261104):
    if trials < 1:
        raise ValueError('Positive trial count required')
    if any(not {'cost', 'inkable', 'type'} <= card.keys() for card in deck['cards']):
        raise ValueError('Missing card metadata; cannot simulate')
    cards = [card for card in deck['cards'] for _ in range(card['quantity'])]
    rng = random.Random(seed)
    counters = {'opening': Counter(), 'mulligan': Counter()}

    def measure(hand, counter):
        one = any(c['cost'] == 1 and c['type'] == 'character' for c in hand)
        two = any(c['cost'] == 2 and c['type'] == 'character' for c in hand)
        counter['one_drop'] += one
        counter['two_drop'] += two
        counter['one_and_two'] += one and two
        counter['three_inkable'] += sum(c['inkable'] for c in hand) >= 3

    for _ in range(trials):
        initial = rng.sample(range(len(cards)), 7)
        hand = [cards[i] for i in initial]
        measure(hand, counters['opening'])
        keep = set()
        # Fixed heuristic: first character at each cost 1, 2 and 3,
        # then earliest inkable cards until three are retained. Replace rest.
        for cost in (1, 2, 3):
            for index, card in enumerate(hand):
                if card['cost'] == cost and card['type'] == 'character':
                    keep.add(index)
                    break
        for index, card in enumerate(hand):
            if sum(hand[i]['inkable'] for i in keep) >= 3:
                break
            if card['inkable']:
                keep.add(index)
        excluded = set(initial)
        remaining = [i for i in range(len(cards)) if i not in excluded]
        replacements = rng.sample(remaining, 7 - len(keep))
        final = [hand[i] for i in sorted(keep)] + [cards[i] for i in replacements]
        measure(final, counters['mulligan'])
    result = {stage: {key: value / trials for key, value in values.items()}
              for stage, values in counters.items()}
    result.update(trials=trials, seed=seed)
    return result


def swiss_probability(match_win, rounds=6, required_wins=5):
    """Independent constant match-win probability; no draws or tiebreakers."""
    return sum(comb(rounds, k) * match_win ** k * (1 - match_win) ** (rounds - k)
               for k in range(required_wins, rounds + 1))
