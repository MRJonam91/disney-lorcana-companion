# Strategia e matematica del mulligan

Questo calcolatore usa probabilità ipergeometriche, non simulazioni Monte Carlo. Le percentuali indicano almeno una carta utile da un gruppo di bersagli equivalenti: non la probabilità di completare una combo.

Modello: mazzo da 60 carte, mano iniziale di 7. Conservi ogni bersaglio; se non ne hai, cambi 4 carte. Le carte cambiate vengono rimescolate nel mazzo prima delle pescate dei turni 2 e 3, giocando per primo. Nessun effetto di pescata aggiuntivo.

| Bersagli | Mano iniziale | Dopo mulligan di 4 | Entro turno 3 |
| --- | --- | --- | --- |
| 4 | 39.9% | 56.6% | 62.9% |
| 8 | 65.4% | 82.4% | 87.3% |
| 12 | 80.9% | 93.4% | 96.1% |

[Model, sources and limitations / Modello, fonti e limiti](../source-status.md).

## Scelte al tavolo

Bilancia le carte non inchiostrabili con la curva dei costi e il piano del mazzo. Non esiste una soglia universale certificata da questi calcoli. Conserva le giocate dei prossimi turni e valuta quali carte puoi usare come inchiostro. Il calcolatore non misura mani morte, matchup o qualità delle decisioni.
