# Sources and calculator model / Fonti e modello del calcolatore

Review date / Data della revisione: **2026-11-04**.

## Verified primary sources / Fonti primarie consultate

- [Official resources](https://disneylorcana.com/en/resources/): rulebook and
  set-note entry points. The linked PDFs are authoritative; the site's update
  date and a document's effective date may differ.
- [Official product archive](https://disneylorcana.com/en/product-archive/):
  corrected names including **Reign of Jafar**. The resources page confirms
  **Fabled**, **Whispers in the Well** and **Winterspell**. Release months in
  the hub refer to initial game-store availability, not necessarily wide retail.
- [Hyperia City announcement, 2026-09-22](https://disneylorcana.com/en/news/2026/09/disney-lorcana-trading-card-game-heads-to-hyperia-city/):
  game-store prerelease **2026-10-16**, wide release **2026-10-23**, new
  **ink drops** mechanic. It must no longer be labelled upcoming on 2026-11-04.

## Historical material / Materiale storico

Legacy guide and Markdown sections contain unverified tournament counts,
win rates, prices, rarity/pull-rate claims, deck lists and card abilities.
The legacy claims do not include their underlying tournament dataset or
a program reproducing the claimed historical Monte Carlo results. These claims are **not validated by this UI
maintenance work**. Some non-Italian pages still contain Italian paragraphs.
The hub, guide notices and READMEs now disclose these limitations.

Le sezioni preesistenti su meta, prezzi, rarità, mazzi e abilità delle carte
richiedono una revisione delle fonti. Le vecchie affermazioni non forniscono il dataset dei tornei né un programma
che riproduca le dichiarate 100.000 simulazioni.
Le traduzioni sono parziali. Questi limiti restano espliciti: i controlli del
software non certificano i contenuti di gioco né le traduzioni.

Before treating a historical claim as current, record a dated primary
source, scope, sample and reproducible derivation where relevant. Do not
infer a verified data sample from a bare reference to a website.

## Calculator / Calcolatore

The tool calculates deterministic probabilities, **not Monte Carlo samples**.
Its result is the chance of finding **at least one** card from a group of
interchangeable targets. Eight copies does not mean finding both halves of
a two-card combo. It is not a recommendation to run eight copies of one card.

Let `N` be deck size, `K` target count and `m` the number of cards replaced
when the opening hand contains no target. Keep every target if found. Draw
7 cards, replace `m` from the remaining `N−7` before shuffling returned cards
back, then take the two ordinary draws by turn 3 on the play. No extra draw,
tutor, ink or gameplay effects are modelled. A found target is retained or
counts as already found; this is not the probability of still holding it.

With `C(a,b)` the binomial coefficient, miss probabilities are:

```text
openingMiss     = C(N−K, 7) / C(N, 7)
replacementMiss = C(N−7−K, m) / C(N−7, m)   [conditional on opening miss]
turnDrawMiss    = C(N−7−K, 2) / C(N−7, 2)   [after reshuffling]

opening  = 1 − openingMiss
mulligan = 1 − openingMiss × replacementMiss
turn3    = 1 − openingMiss × replacementMiss × turnDrawMiss
```

For `m=0`, the last result equals the ordinary probability of finding a
target in 9 draws. With one target and a full mulligan in 60 cards,
the post-mulligan probability is `14/60`; by turn 3 it is
`1 − (53/60) × (46/53) × (51/53)`, approximately **26.2%**.

Il modello conserva le carte utili e, se non ne hai, cambia il numero
selezionato di carte. Tiene conto del rimescolamento prima dei turni 2 e 3.
Non calcola combo o effetti di pescata aggiuntiva. Accetta 40–100 carte per
scenari personalizzati: questo intervallo non certifica la legalità di un
mazzo. In costruito servono almeno 60 carte. Valori vuoti, decimali o fuori
intervallo mostrano un errore e nessuna percentuale.

Run `node --test tools/odds.test.cjs` to check the actual embedded runtime
in all five guides. The tests include independently derived cases for no
mulligan, full mulligan and invalid inputs. `python tools/check_site.py`
checks the six pages, links, anchors, labels, offline dependencies and
runtime consistency. Neither check substitutes for content fact-checking.

## Shared analysis integration / Integrazione analisi condivisa

The new [IT](../tournament-decks.html) and [EN](../tournament-decks.en.html)
catalog separates four reported tournament lists from the officially
published Coco themed proposal. Each source was opened and compared on
2026-11-04. Card metadata and base-printing IDs use the upstream Lorcast
snapshot; the original list sources own the quantity/placement claims.
See [Hyperia verification](research/hyperia-card-verification.md) and
[Torino context](research/torino-tournament-context.md).

New simulations are reproducible in `tools/deck_catalog.py`, unlike the
unprovided legacy 100,000-trial claims. Results and seed are stored in
`data/tournament-simulations.json`; the catalog digest prevents silently
mixing results with a changed list. These are opening-hand experiments,
not simulated match wins. / I nuovi esperimenti sulle mani iniziali hanno
codice, seed e risultati salvati; non simulano vittorie o partite complete.
