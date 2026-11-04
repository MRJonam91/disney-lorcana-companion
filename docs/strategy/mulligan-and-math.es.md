# Estrategia y probabilidades del mulligan

El calculador usa probabilidades hipergeométricas, no simulaciones Monte Carlo. Los resultados significan al menos una carta útil de objetivos intercambiables, no un combo completo.

Modelo: mazo de 60 cartas, mano inicial de 7. Conserva cada objetivo; sin objetivos, cambia 4 cartas. Las cartas devueltas se barajan antes de robar en los turnos 2 y 3, empezando primero. Sin efectos de robo adicionales.

| Objetivos | Mano inicial | Tras mulligan de 4 | Hasta turno 3 |
| --- | --- | --- | --- |
| 4 | 39.9% | 56.6% | 62.9% |
| 8 | 65.4% | 82.4% | 87.3% |
| 12 | 80.9% | 93.4% | 96.1% |

[Model, sources and limitations / Modello, fonti e limiti](../source-status.md).

## Decisiones en la mesa

Equilibra las cartas no entintables con la curva de costes y el plan del mazo. Estos cálculos no establecen un umbral universal. Conserva tus próximas jugadas y considera qué cartas convertir en tinta. El calculador no mide manos muertas, enfrentamientos ni calidad de decisiones.
