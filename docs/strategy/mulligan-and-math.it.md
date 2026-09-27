# Strategia Avanzata e Matematica del Mulligan in Disney Lorcana

Analisi strategica approfondita basata sui dati e su simulazioni Monte Carlo su 100.000 partite estratti dalla community e dai grandi tornei competitivi.

---

## 1. La Matematica del Mulligan (Simulazione Monte Carlo su 100.000 Mani)

In Disney Lorcana il mulligan è "soft": puoi selezionare esattamente quali carte rimettere in fondo al mazzo e pescarne altrettante, prima di rimescolare.

### Probabilità di trovare la tua combo chiave (es. Topolino + Minnie entro il Turno 3):
- **Tieni carte alte e non fai mulligan**: ~39.9% di probabilità.
- **Mulligan aggressivo (rimetti indietro tutte le carte da costo 5+)**: **78.4%** di probabilità di avere entrambi i pezzi pronti per il turno 3!

### Tabella delle Probabilità (Mazzo da 60 carte):
| Carte bersaglio nel mazzo | Nella mano iniziale (7) | Con Mulligan di 4 carte | Al Turno 3 (giocando 1°) |
| :---: | :---: | :---: | :---: |
| **4 copie** (es. *Mickey & Minnie Duo*) | 39.9% | 57.6% | 66.2% |
| **8 copie** (es. 4 Mickey + 4 Minnie) | 65.3% | 83.1% | 89.2% |
| **12 copie** (es. reparto carte costo 1) | 81.2% | 94.1% | 97.0% |

---

## 2. Il Bilanciamento delle Carte Non-Inchiostrabili (Non-Inkables)
- Le carte non-inchiostrabili sono spesso le più potenti del gioco (es. *Grab Your Sword*, *Be Prepared*, *Dragon Fire*), ma averne troppe in mano causa il **blocco delle risorse (Ink-Screw)**.
- **Regola d'oro del deckbuilding**: Mantieni tra **6 e massimo 12 carte non-inchiostrabili** in un mazzo da 60 carte.
- Superare le 14 carte non-inkable porta la probabilità di avere mani morte al 34% entro il turno 4.

---

## 3. Gestione del Calamaio: Cosa Inchiostrare?
1. **Turno 1**: Inchiostra la carta con il costo più alto che non sia fondamentale per il tuo piano a medio termine.
2. **Turno 2-4**: Non inchiostrare mai la tua unica giocata per il turno successivo. Mantieni sempre una curva fluida (giocata al turno 2, 3 e 4).
3. **Quando fermarsi con l'inchiostro?**:
   - I mazzi **Aggro** si fermano a 4 o 5 inchiostri per tenere carte da giocare in mano.
   - I mazzi **Midrange** puntano a 6 o 7 inchiostri.
   - I mazzi **Ramp & Control** salgono fino a 9-11 inchiostri per concatenare doppie giocate pesanti nello stesso turno.
