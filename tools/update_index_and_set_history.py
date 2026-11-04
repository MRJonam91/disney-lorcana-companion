import re

def update_index():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Add Database Card in .features-grid
    target_end = '            <a href="docs/decks/deck-building-and-testing.es.md" class="feat-tag">ES Builder</a>\n          </div>\n        </div>\n      </div>'
    db_card = """            <a href="docs/decks/deck-building-and-testing.es.md" class="feat-tag">ES Builder</a>
          </div>
        </div>

        <div class="feat-card foil-card-fx" style="border-color:var(--gold);">
          <div class="feat-icon">🗄️</div>
          <h3>14-Set Card Databases (3,242 Cards)</h3>
          <p>Complete portable datasets for all 14 sets (Set 1 to Set 14 Hyperia City) in JSON, SQLite (.db), CSV, and Markdown with collector numbers, rarities, Iconic/Enchanted chase lists, and market prices.</p>
          <div class="feat-links">
            <a href="docs/sets/cards/README.md" class="feat-tag">📚 All 14 Sets Index</a>
            <a href="data/lorcana-database.json" class="feat-tag">📦 Master JSON</a>
            <a href="data/lorcana-all-cards.csv" class="feat-tag">📊 Master CSV</a>
            <a href="data/lorcana-all-sets.db" class="feat-tag">🗄️ Master SQLite DB</a>
          </div>
        </div>
      </div>"""
    if target_end in html and "14-Set Card Databases (3,242 Cards)" not in html:
        html = html.replace(target_end, db_card)

    # Replace .sets-scroller with official names, card counts, and direct links to each set's Markdown catalog
    old_scroller = re.search(r'<div class="sets-scroller">.*?</div>\s*</section>', html, re.S)
    new_scroller = """<div class="sets-scroller">
        <a href="docs/sets/cards/set-01-the-first-chapter.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 1 · 216 Cards</div>
          <div class="set-name">The First Chapter</div>
          <div class="set-date">2023-08-18 · ✨ 12 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-02-rise-of-the-floodborn.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 2 · 216 Cards</div>
          <div class="set-name">Rise of the Floodborn</div>
          <div class="set-date">2023-11-17 · ✨ 12 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-03-into-the-inklands.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 3 · 227 Cards</div>
          <div class="set-name">Into the Inklands</div>
          <div class="set-date">2024-02-23 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-04-ursula-s-return.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 4 · 225 Cards</div>
          <div class="set-name">Ursula's Return</div>
          <div class="set-date">2024-05-17 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-05-shimmering-skies.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 5 · 223 Cards</div>
          <div class="set-name">Shimmering Skies</div>
          <div class="set-date">2024-08-09 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-06-azurite-sea.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 6 · 222 Cards</div>
          <div class="set-name">Azurite Sea</div>
          <div class="set-date">2024-11-15 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-07-archazia-s-island.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 7 · 224 Cards</div>
          <div class="set-name">Archazia's Island</div>
          <div class="set-date">2025-03-07 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-08-reign-of-jafar.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 8 · 229 Cards</div>
          <div class="set-name">Reign of Jafar</div>
          <div class="set-date">2025-05-30 · ✨ 18 Enchanted</div>
        </a>
        <a href="docs/sets/cards/set-09-fabled.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 9 · 243 Cards</div>
          <div class="set-name">Fabled</div>
          <div class="set-date">2025-08-29 · 🟣 18 Epic · 👑 2 Iconic</div>
        </a>
        <a href="docs/sets/cards/set-10-whispers-in-the-well.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 10 · 242 Cards</div>
          <div class="set-name">Whispers in the Well</div>
          <div class="set-date">2025-11-07 · 🟣 18 Epic · 👑 2 Iconic</div>
        </a>
        <a href="docs/sets/cards/set-11-winterspell.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 11 · 243 Cards</div>
          <div class="set-name">Winterspell</div>
          <div class="set-date">2026-02-13 · 🟣 18 Epic · 👑 2 Iconic</div>
        </a>
        <a href="docs/sets/cards/set-12-wilds-unknown.md" class="set-pill foil-card-fx">
          <div class="set-num">Set 12 · 243 Cards</div>
          <div class="set-name">Wilds Unknown</div>
          <div class="set-date">2026-05-08 · 🟣 18 Epic · 👑 2 Iconic</div>
        </a>
        <a href="docs/sets/cards/set-13-attack-of-the-vine.md" class="set-pill foil-card-fx" style="border-color:var(--emerald);background:rgba(63,163,100,0.12);">
          <div class="set-num" style="color:#4ade80;">Set 13 · 247 Cards</div>
          <div class="set-name">Attack of the Vine!</div>
          <div class="set-date">2026-07-17 · 👑 Lilo &amp; Stitch / Belle &amp; Beast</div>
        </a>
        <a href="docs/sets/cards/set-14-hyperia-city.md" class="set-pill foil-card-fx" style="border-color:var(--gold);background:rgba(229,185,92,0.14);">
          <div class="set-num" style="color:var(--gold);">Set 14 · 242 Cards</div>
          <div class="set-name">Hyperia City</div>
          <div class="set-date">2026-10-16 · 👑 Mickey / Cinderella</div>
        </a>
      </div>
    </section>"""
    if old_scroller:
        html = html[:old_scroller.start()] + new_scroller + html[old_scroller.end():]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html timeline and database links!")


def update_set_histories():
    summary_table = """
---

## 🗄️ Database Completo Carte per Ogni Set (3.242 Carte Ufficiali — JSON, CSV, SQLite DB & Markdown)

Tutti i dati ufficiali delle carte (inclusi numeri di collezione, rarità esatte, carte **Iconiche 👑**, **Incantate ✨**, **Epiche 🟣** e prezzi di mercato) sono disponibili per ogni singolo set:

| Set | Nome Ufficiale | Data Uscita | Carte Totali | Carte Iconiche (👑) | Lista MD | JSON | CSV | SQLite DB |
| :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :---: |
| **1** | **The First Chapter** | `2023-08-18` | 216 | — | [MD](cards/set-01-the-first-chapter.md) | [JSON](../../data/sets/json/set-01-the-first-chapter.json) | [CSV](../../data/sets/csv/set-01-the-first-chapter.csv) | [DB](../../data/sets/db/set-01-the-first-chapter.db) |
| **2** | **Rise of the Floodborn** | `2023-11-17` | 216 | — | [MD](cards/set-02-rise-of-the-floodborn.md) | [JSON](../../data/sets/json/set-02-rise-of-the-floodborn.json) | [CSV](../../data/sets/csv/set-02-rise-of-the-floodborn.csv) | [DB](../../data/sets/db/set-02-rise-of-the-floodborn.db) |
| **3** | **Into the Inklands** | `2024-02-23` | 227 | — | [MD](cards/set-03-into-the-inklands.md) | [JSON](../../data/sets/json/set-03-into-the-inklands.json) | [CSV](../../data/sets/csv/set-03-into-the-inklands.csv) | [DB](../../data/sets/db/set-03-into-the-inklands.db) |
| **4** | **Ursula's Return** | `2024-05-17` | 225 | — | [MD](cards/set-04-ursula-s-return.md) | [JSON](../../data/sets/json/set-04-ursula-s-return.json) | [CSV](../../data/sets/csv/set-04-ursula-s-return.csv) | [DB](../../data/sets/db/set-04-ursula-s-return.db) |
| **5** | **Shimmering Skies** | `2024-08-09` | 223 | — | [MD](cards/set-05-shimmering-skies.md) | [JSON](../../data/sets/json/set-05-shimmering-skies.json) | [CSV](../../data/sets/csv/set-05-shimmering-skies.csv) | [DB](../../data/sets/db/set-05-shimmering-skies.db) |
| **6** | **Azurite Sea** | `2024-11-15` | 222 | — | [MD](cards/set-06-azurite-sea.md) | [JSON](../../data/sets/json/set-06-azurite-sea.json) | [CSV](../../data/sets/csv/set-06-azurite-sea.csv) | [DB](../../data/sets/db/set-06-azurite-sea.db) |
| **7** | **Archazia's Island** | `2025-03-07` | 224 | — | [MD](cards/set-07-archazia-s-island.md) | [JSON](../../data/sets/json/set-07-archazia-s-island.json) | [CSV](../../data/sets/csv/set-07-archazia-s-island.csv) | [DB](../../data/sets/db/set-07-archazia-s-island.db) |
| **8** | **Reign of Jafar** | `2025-05-30` | 229 | — | [MD](cards/set-08-reign-of-jafar.md) | [JSON](../../data/sets/json/set-08-reign-of-jafar.json) | [CSV](../../data/sets/csv/set-08-reign-of-jafar.csv) | [DB](../../data/sets/db/set-08-reign-of-jafar.db) |
| **9** | **Fabled** | `2025-08-29` | 243 | `#241` Minnie Mouse, `#242` Mickey Mouse | [MD](cards/set-09-fabled.md) | [JSON](../../data/sets/json/set-09-fabled.json) | [CSV](../../data/sets/csv/set-09-fabled.csv) | [DB](../../data/sets/db/set-09-fabled.db) |
| **10** | **Whispers in the Well** | `2025-11-07` | 242 | `#241` Ariel, `#242` Hades | [MD](cards/set-10-whispers-in-the-well.md) | [JSON](../../data/sets/json/set-10-whispers-in-the-well.json) | [CSV](../../data/sets/csv/set-10-whispers-in-the-well.csv) | [DB](../../data/sets/db/set-10-whispers-in-the-well.db) |
| **11** | **Winterspell** | `2026-02-13` | 243 | `#241` Pocahontas, `#242` Moana | [MD](cards/set-11-winterspell.md) | [JSON](../../data/sets/json/set-11-winterspell.json) | [CSV](../../data/sets/csv/set-11-winterspell.csv) | [DB](../../data/sets/db/set-11-winterspell.db) |
| **12** | **Wilds Unknown** | `2026-05-08` | 243 | `#241` Buzz Lightyear, `#242` Merida | [MD](cards/set-12-wilds-unknown.md) | [JSON](../../data/sets/json/set-12-wilds-unknown.json) | [CSV](../../data/sets/csv/set-12-wilds-unknown.csv) | [DB](../../data/sets/db/set-12-wilds-unknown.db) |
| **13** | **Attack of the Vine!** | `2026-07-17` | 247 | `#244` Lilo & Stitch, `#245` Belle & Beast | [MD](cards/set-13-attack-of-the-vine.md) | [JSON](../../data/sets/json/set-13-attack-of-the-vine.json) | [CSV](../../data/sets/csv/set-13-attack-of-the-vine.csv) | [DB](../../data/sets/db/set-13-attack-of-the-vine.db) |
| **14** | **Hyperia City** | `2026-10-16` | 242 | `#241` Mickey Mouse, `#242` Cinderella | [MD](cards/set-14-hyperia-city.md) | [JSON](../../data/sets/json/set-14-hyperia-city.json) | [CSV](../../data/sets/csv/set-14-hyperia-city.csv) | [DB](../../data/sets/db/set-14-hyperia-city.db) |
"""
    for lang in ["it", "en", "fr", "de", "es"]:
        p = f"docs/sets/set-history.{lang}.md"
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        if "cards/set-13-attack-of-the-vine.md" not in txt:
            txt = txt.rstrip() + "\n" + summary_table
            with open(p, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"Updated {p} with 14-set database index table!")

if __name__ == "__main__":
    update_index()
    update_set_histories()
