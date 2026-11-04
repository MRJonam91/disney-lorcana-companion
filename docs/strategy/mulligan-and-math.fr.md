# Stratégie et probabilités du mulligan

Le calculateur utilise des probabilités hypergéométriques, pas des simulations Monte Carlo. Les résultats indiquent au moins une carte utile parmi des cibles interchangeables, pas une combinaison complète.

Modèle : deck de 60 cartes, main initiale de 7. Gardez chaque cible ; sans cible, remplacez 4 cartes. Les cartes retournées sont remélangées avant les pioches des tours 2 et 3, en commençant. Aucun effet de pioche supplémentaire.

| Cibles | Main initiale | Après mulligan de 4 | Au tour 3 |
| --- | --- | --- | --- |
| 4 | 39.9% | 56.6% | 62.9% |
| 8 | 65.4% | 82.4% | 87.3% |
| 12 | 80.9% | 93.4% | 96.1% |

[Model, sources and limitations / Modello, fonti e limiti](../source-status.md).

## Décisions de jeu

Équilibrez les cartes non encrables avec la courbe des coûts et le plan du deck. Ces calculs ne fixent aucun seuil universel. Gardez vos prochaines actions et évaluez les cartes à encrer. Le calculateur ne mesure ni les mains mortes, ni les matchups, ni la qualité des décisions.
