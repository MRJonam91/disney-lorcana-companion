# Strategie und Mulligan-Wahrscheinlichkeiten

Der Rechner verwendet hypergeometrische Wahrscheinlichkeiten, keine Monte-Carlo-Simulationen. Ergebnisse bedeuten mindestens eine passende Karte aus austauschbaren Zielen, keine vollständige Kombination.

Modell: 60 Karten, Starthand mit 7 Karten. Behalte jede Zielkarte; ohne Zielkarte tausche 4 Karten aus. Zurückgelegte Karten werden vor den Ziehschritten in Zug 2 und 3 eingemischt; du beginnst. Keine zusätzlichen Zieheffekte.

| Ziele | Starthand | Nach 4-Karten-Mulligan | Bis Zug 3 |
| --- | --- | --- | --- |
| 4 | 39.9% | 56.6% | 62.9% |
| 8 | 65.4% | 82.4% | 87.3% |
| 12 | 80.9% | 93.4% | 96.1% |

[Model, sources and limitations / Modello, fonti e limiti](../source-status.md).

## Entscheidungen am Tisch

Stimme nicht einfärbbare Karten auf Kostenkurve und Deckplan ab. Diese Berechnung liefert keinen universellen Grenzwert. Behalte kommende Spielzüge und prüfe, welche Karten Tinte werden können. Der Rechner bewertet keine unspielbaren Hände, Matchups oder Entscheidungsqualität.
