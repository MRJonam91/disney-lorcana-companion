with open('README.md', 'r', encoding='utf-8') as f:
    text = f.read()

apps_spotlight_en = """
---

## 🚀 Interactive Community Web Apps

| Application | Features | Direct Link |
| :--- | :--- | :--- |
| **🃏 Deck Lab & Playtester** | 60-card builder, live mana curve, goldfish turn-by-turn playtesting, export/import compatible with **duels.ink**, **inktable.net** and **dreamborn.ink** | [Launch Deck Lab](deck-lab.html) |
| **💎 Collector's Vault** | Realistic booster pack simulator (1 pack, 10, Trove, 24-box, 96-case), binomial pull rate calculator per set, sealed product catalog, random quest generator & coin flip | [Open Collector's Vault](collector-vault.html) |
| **🌐 Multilingual Hub** | Unified international portal with quick language switch, lore tracker & set timeline | [Open Hub Portal](index.html) |
"""

target = "--- \n\n## ⚡ What Makes This Repository Special?"
if "## ⚡ What Makes This Repository Special?" in text:
    text = text.replace("## ⚡ What Makes This Repository Special?", apps_spotlight_en.strip() + "\n\n---\n\n## ⚡ What Makes This Repository Special?")
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(text)
    with open('README.en.md', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated README.md and README.en.md")
else:
    print("Target not found in README.md")

# Update README.it.md
with open('README.it.md', 'r', encoding='utf-8') as f:
    it_text = f.read()

apps_spotlight_it = """
---

## 🚀 Applicazioni Web Interattive & Simulatori

- **[🃏 Deck Lab & Goldfish Playtester (deck-lab.html)](deck-lab.html)**: Costruzione mazzi da 60 carte, analisi della curva d'inchiostro, test della mano iniziale con mulligan, simulatore primi turni e compatibilità export con **duels.ink**, **inktable.net** e **dreamborn.ink**.
- **[💎 Collector's Vault & Pulls Simulator (collector-vault.html)](collector-vault.html)**: Simulatore realistico di spacchettamento (1 bustina, 10, Trove, Box da 24, Case da 96), calcolo esatto delle probabilità di trovare carte Incantate per ogni set, catalogo prodotti e generatore di sfide con moneta 3D.
"""

if "## 🚀 Accesso Rapido alle Guide" in it_text:
    it_text = it_text.replace("## 🚀 Accesso Rapido alle Guide", apps_spotlight_it.strip() + "\n\n---\n\n## 🚀 Accesso Rapido alle Guide")
    with open('README.it.md', 'w', encoding='utf-8') as f:
        f.write(it_text)
    print("Updated README.it.md")
