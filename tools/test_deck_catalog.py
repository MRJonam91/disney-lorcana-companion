import copy
import unittest

from deck_catalog import validate_catalog, deck_text, opening_metrics


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.deck = {
            'id': 'example', 'name': 'Example', 'source': 'https://example.com/deck',
            'cards': [
                {'quantity': 4, 'name': f'Card {i}', 'cost': 1 if i < 3 else 2,
                 'inkable': True, 'type': 'character'} for i in range(15)
            ],
        }

    def test_accepts_sixty_cards_and_exports_each_line(self):
        validate_catalog([self.deck])
        lines = deck_text(self.deck).splitlines()
        self.assertEqual(len(lines), 15)
        self.assertEqual(lines[0], '4 Card 0')

    def test_rejects_wrong_total(self):
        self.deck['cards'][0]['quantity'] = 3
        with self.assertRaisesRegex(ValueError, '60'):
            validate_catalog([self.deck])

    def test_rejects_duplicate_full_names(self):
        self.deck['cards'][1]['name'] = self.deck['cards'][0]['name']
        with self.assertRaisesRegex(ValueError, 'duplicate'):
            validate_catalog([self.deck])

    def test_rejects_over_four_copies(self):
        self.deck['cards'][0]['quantity'] = 5
        self.deck['cards'][1]['quantity'] = 3
        with self.assertRaisesRegex(ValueError, 'copies'):
            validate_catalog([self.deck])

    def test_rejects_html_and_non_https_sources(self):
        self.deck['source'] = 'javascript:alert(1)'
        with self.assertRaisesRegex(ValueError, 'https'):
            validate_catalog([self.deck])

    def test_simulation_is_seeded_and_does_not_mutate_catalog(self):
        before = copy.deepcopy(self.deck)
        first = opening_metrics(self.deck, trials=100, seed=42)
        self.assertEqual(first, opening_metrics(self.deck, trials=100, seed=42))
        self.assertEqual(self.deck, before)
        self.assertEqual(first['trials'], 100)
        self.assertEqual(first['opening']['three_inkable'], 1)
        self.assertEqual(first['mulligan']['three_inkable'], 1)

    def test_missing_card_metadata_is_not_silently_simulated(self):
        self.deck['cards'][0].pop('cost')
        with self.assertRaisesRegex(ValueError, 'metadata'):
            opening_metrics(self.deck, trials=100)


if __name__ == '__main__':
    unittest.main()
