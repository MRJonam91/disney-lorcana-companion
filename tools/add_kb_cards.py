with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

target = '            <a href="docs/glossary/glossary.es.md" class="feat-tag">ES Dictionary</a>\n          </div>\n        </div>\n      </div>'
replacement = """            <a href="docs/glossary/glossary.es.md" class="feat-tag">ES Dictionary</a>
          </div>
        </div>

        <div class="feat-card foil-card-fx">
          <div class="feat-icon">📊</div>
          <h3>Pull Rates, 3 Eras &amp; Products</h3>
          <p>Experimental community pull rates (Classic, Expansion &amp; Modern Eras), Epic &amp; Iconic odds, God Pack hierarchy, and sealed product guide across all 5 languages.</p>
          <div class="feat-links">
            <a href="docs/cards-and-rarities/pull-rates-and-products.it.md" class="feat-tag">IT Pulls</a>
            <a href="docs/cards-and-rarities/pull-rates-and-products.en.md" class="feat-tag">EN Pulls</a>
            <a href="docs/cards-and-rarities/pull-rates-and-products.fr.md" class="feat-tag">FR Pulls</a>
            <a href="docs/cards-and-rarities/pull-rates-and-products.de.md" class="feat-tag">DE Pulls</a>
            <a href="docs/cards-and-rarities/pull-rates-and-products.es.md" class="feat-tag">ES Pulls</a>
          </div>
        </div>

        <div class="feat-card foil-card-fx">
          <div class="feat-icon">🛠️</div>
          <h3>Deck Building &amp; Simulators</h3>
          <p>60-card construction rules, uninkable count thresholds, ink curve geometry, goldfish playtesting methodology, and export guides for duels.ink &amp; inktable.</p>
          <div class="feat-links">
            <a href="docs/decks/deck-building-and-testing.it.md" class="feat-tag">IT Builder</a>
            <a href="docs/decks/deck-building-and-testing.en.md" class="feat-tag">EN Builder</a>
            <a href="docs/decks/deck-building-and-testing.fr.md" class="feat-tag">FR Builder</a>
            <a href="docs/decks/deck-building-and-testing.de.md" class="feat-tag">DE Builder</a>
            <a href="docs/decks/deck-building-and-testing.es.md" class="feat-tag">ES Builder</a>
          </div>
        </div>
      </div>"""

if target in html:
    html = html.replace(target, replacement)

# Also add foil-card-fx to existing .feat-card elements
html = html.replace('<div class="feat-card">', '<div class="feat-card foil-card-fx">')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("index.html updated with 8 5-language knowledge base cards & foil effects!")
