import os

# 1. DECK BUILDING AND TESTING (IT)
deck_guide_it = """# Guida Completa alla Creazione, Test e Simulazione dei Mazzi in Disney Lorcana

Tutto ciò che serve per passare dall'idea iniziale a un mazzo da 60 carte competitivo, pronto per i tornei e testato sul campo.

---

## 1. I Pilastri della Costruzione del Mazzo (Deckbuilding Rules)
- **Minimo 60 carte**: In ambiente competitivo si giocano **esattamente 60 carte** per massimizzare la consistenza e la probabilità di pescare le carte chiave.
- **Massimo 2 Inchiostri**: Scegli una combinazione complementare (es. Amber/Steel per canzoni e board control, Emerald/Sapphire per combo e ramp, Amethyst/Ruby per controllo e rimbalzo).
- **Regola delle 4 Copie**: Massimo 4 copie per carta con lo stesso nome completo e sottotitolo.

### La Regola d'Oro dei Non-Inchiostrabili (Non-Inkables)
- In un mazzo da 60 carte, mantieni **tra 6 e 12 carte non-inchiostrabili al massimo**.
- Superare le 14 carte non-inkable aumenta drasticamente la probabilità di **Ink-Screw** (trovarsi con la mano bloccata e impossibilitati a inchiostrare nei primi turni critici).

---

## 2. Simulazione e Goldfish Playtesting (Test in Solitario)

Il **Goldfish Testing** consiste nel giocare il proprio mazzo senza avversario per simulare la fluidità dei primi 5-6 turni:
1. **Verifica della Mano Iniziale**: Pescando 7 carte, hai almeno una giocata a costo 1 o 2 e una riserva inchiostrabile?
2. **Mulligan Test**: Applica la regola: rimetti sotto tutte le carte a costo 5+ se non hai già garantita la curva per i turni 1, 2 e 3.
3. **Turn to 20 Lore**: Quanti turni impiega il mazzo a raggiungere 20 Lore se lasciato indisturbato?
   - Mazzi **Aggro**: Devono chiudere entro il **Turno 5 o 6**.
   - Mazzi **Midrange / Combo**: Chiudono tra il **Turno 6 e 7**.
   - Mazzi **Control**: Stabilizzano il tavolo e accumulano Lore dal **Turno 8+**.

---

## 3. Piattaforme Esterne Consigliate per Giocare Online

Il nostro [Deck Lab (deck-lab.html)](../../deck-lab.html) permette di esportare le liste in formato standard compatibile con tutti i simulatori:

### ⚔️ Duels.ink (https://duels.ink)
- **Cosa fa**: Piattaforma web gratuita per partite PvP in tempo reale direttamente da browser, senza installare software.
- **Punti di Forza**: Sistema di matchmaking, replay delle partite, supporto completo per tutte le espansioni fino al Set 14.

### 🤖 Inktable.net (https://inktable.net)
- **Cosa fa**: Il miglior simulatore per giocare **contro bot dotati di intelligenza artificiale**.
- **Punti di Forza**: Velocissimo per testare un mazzo appena creato in 3 minuti, senza dover aspettare avversari reali.

### 📊 Dreamborn.ink (https://dreamborn.ink)
- **Cosa fa**: Il più grande database e deckbuilder mondiale per Lorcana.
- **Punti di Forza**: Tracciamento dei prezzi di mercato (Cardmarket, TCGplayer), statistiche di popolarità dei mazzi nei tornei.
"""

# 2. DECK BUILDING AND TESTING (EN)
deck_guide_en = """# Complete Guide to Deck Building, Testing & Online Simulators

Everything you need to transform an idea into a competitive, fine-tuned 60-card Disney Lorcana tournament list.

---

## 1. Deck Construction Fundamentals
- **Exactly 60 Cards**: Always play the minimum allowed to maximize draw consistency.
- **Maximum 2 Inks**: Combine colors that patch each other's weaknesses (e.g. Amber/Steel for Steelsongs, Emerald/Sapphire for Duo Shift tempo).
- **The Non-Inkable Rule**: Keep non-inkables between **6 and 12 maximum** per 60 cards to avoid resource choke.

---

## 2. Goldfish Testing Protocol
1. **Opening Hand Verification**: Do you have proactive 1-drop and 2-drop plays?
2. **Mulligan Optimization**: Send back high-cost bombs to ensure hitting 3 consecutive ink drops.
3. **Turn-to-20 Metric**:
   - Aggro: Reaches 20 Lore by Turn 5-6.
   - Midrange: Closes on Turn 6-7.
   - Control: Establishes board dominance and sweeps by Turn 7+.

---

## 3. Top Community Simulators & Online Platforms
Export your deck from our [Deck Lab](../../deck-lab.html) directly into:
- ⚔️ **Duels.ink** (https://duels.ink): Browser-based multiplayer PvP with full card pool and spectator modes.
- 🤖 **Inktable.net** (https://inktable.net): Instant single-player goldfish testing against AI opponents.
- 📊 **Dreamborn.ink** (https://dreamborn.ink): Decklist archive, meta tracker, and market price aggregator.
"""

# 3. PULL RATES AND PRODUCTS (IT)
pull_guide_it = """# Guida ai Pull Rate, Probabilità per Set e Catalogo Prodotti Ufficiali

Analisi statistica delle probabilità di sbustamento e panoramica di tutti i prodotti sigillati di Disney Lorcana.

---

## 1. Probabilità Matematiche di Sbustamento (Pull Rates)

Ogni bustina (Booster Pack) standard da 12 carte segue questa composizione esatta:
- **6 Carte Comuni**
- **3 Carte Non Comuni**
- **2 Slot Rari o Superiori**:
  - ~68% Rara
  - ~20% Super Rara
  - ~12% Leggendaria
- **1 Slot Foil Garantito**:
  - Può contenere qualsiasi carta del set in versione foil.
  - Tasso stimato per una carta **Incantata (Enchanted)**: **1 su 72 - 96 bustine** (media standard: **1 ogni 80 bustine**, pari a ~1.25% per bustina).

### Tabella Probabilità per Quantità di Bustine:
| Prodotto | Bustine | Leggendarie Attese | Probabilità Almeno 1 Incantata |
| :--- | :---: | :---: | :---: |
| **Bustina Singola** | 1 | 0.17 | 1.25% |
| **Starter Deck (+ Booster)** | 1 | 0.17 | 1.25% |
| **Gift Set** | 4 | 0.68 | 4.9% |
| **Illumineer's Trove** | 8 | 1.36 | 9.6% |
| **Booster Display Box** | 24 | ~4.1 | **26.1%** |
| **2 Booster Box** | 48 | ~8.2 | **45.4%** |
| **Master Case (4 Box)** | 96 | ~16.4 | **70.2%** |

*Formula applicata: P(almeno 1) = 1 - (1 - 1/80)^N*

---

## 2. Catalogo Prodotti Ufficiali Disney Lorcana

### 🎴 Booster Display Box (24 Bustine)
- 288 carte totali per confezione.
- Il prodotto più conveniente per iniziare una collezione seria o organizzare tornei Draft e Sealed.

### 🎁 Illumineer's Trove
- Scatola rinforzata porta-collezione con illustrazioni del set.
- 8 Bustine booster.
- 6 Dadi metallizzati segna-danno.
- 1 Contatore Lore rotante.
- 6 Divisori in cartoncino rigido per catalogare le carte per inchiostro.

### ⚔️ Starter Decks
- Mazzo completo a 60 carte bilanciato e pronto all'uso con 2 inchiostri.
- 1 Bustina booster inclusa per iniziare a personalizzare la lista.
- Segnalini danno in cartoncino e regolamento rapido.

### 🐙 Illumineer's Quest (Deep Trouble)
- Espansione cooperativa e solitaria: 1-4 giocatori affrontano Ursula e il suo mazzo con regole automatiche.
- Include 2 mazzi giocatore precon e carte speciali con retro personalizzato.
"""

# 4. PULL RATES AND PRODUCTS (EN)
pull_guide_en = """# Disney Lorcana Pull Rates, Probability Math & Sealed Product Guide

Comprehensive mathematical analysis of booster pack distribution and complete catalog of sealed retail products.

---

## 1. Mathematical Pull Rates (12-Card Booster Pack)
- 6 Commons
- 3 Uncommons
- 2 Rare or higher slots (Rare, Super Rare, Legendary)
- 1 Guaranteed 100% Foil slot (Any rarity, with a ~1:80 chance of being an Enchanted card).

### Cumulative Enchanted Odds by Product:
- 1 Booster Pack: 1.25%
- Illumineer's Trove (8 packs): 9.6%
- Booster Display Box (24 packs): **26.1%**
- Sealed Case (96 packs / 4 boxes): **70.2%**

---

## 2. Official Product Breakdown
- **Booster Packs (12 Cards)**: Ideal for limited play (Draft & Sealed).
- **Booster Box (24 Packs)**: 288 cards, ~4-5 Legendaries, ~12-14 Super Rares.
- **Illumineer's Trove**: Storage box, 8 booster packs, 6 metal damage counters, spin-down lore counter, card dividers.
- **Starter Decks**: 60-card ready-to-play deck + 1 booster pack.
- **Illumineer's Quest**: Cooperative challenge box against automated boss encounter.
"""

with open('docs/decks/deck-building-and-testing.it.md', 'w', encoding='utf-8') as f:
    f.write(deck_guide_it)

with open('docs/decks/deck-building-and-testing.en.md', 'w', encoding='utf-8') as f:
    f.write(deck_guide_en)

with open('docs/cards-and-rarities/pull-rates-and-products.it.md', 'w', encoding='utf-8') as f:
    f.write(pull_guide_it)

with open('docs/cards-and-rarities/pull-rates-and-products.en.md', 'w', encoding='utf-8') as f:
    f.write(pull_guide_en)

print("Generated markdown documentation successfully.")
