import re

def main():
    path = "deck-lab.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add script data/lorcana-cards.js before the main script
    if 'data/lorcana-cards.js' not in content:
        content = content.replace(
            '<script>',
            '<script src="data/lorcana-cards.js"></script>\n  <script>',
            1
        )

    # 2. Add Top Bar App link if not present
    if 'disneylorcana.com/en-US/app' not in content:
        content = content.replace(
            '<a href="deck-lab.html" class="active">🃏 Deck Lab</a>',
            '<a href="deck-lab.html" class="active">🃏 Deck Lab</a>\n      <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" style="color:var(--gold);">📱 App Ufficiale</a>'
        )

    # 3. Add CSS for rarity tags and set filter
    rarity_css = """
    /* Rarity badges */
    .rarity-tag {
      display: inline-block;
      font-size: .68rem;
      padding: 1px 7px;
      border-radius: 4px;
      font-weight: 700;
      letter-spacing: .04em;
      margin-left: 6px;
      vertical-align: middle;
    }
    .rarity-Common { background: rgba(148, 163, 184, 0.2); color: #cbd5e1; border: 1px solid rgba(148, 163, 184, 0.4); }
    .rarity-Uncommon { background: rgba(125, 211, 252, 0.2); color: #7dd3fc; border: 1px solid rgba(125, 211, 252, 0.4); }
    .rarity-Rare { background: rgba(253, 224, 71, 0.2); color: #fde047; border: 1px solid rgba(253, 224, 71, 0.4); }
    .rarity-SuperRare { background: rgba(192, 132, 252, 0.2); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.4); }
    .rarity-Legendary { background: rgba(251, 146, 60, 0.25); color: #fb923c; border: 1px solid rgba(251, 146, 60, 0.6); }
    .rarity-Epic { background: linear-gradient(135deg, rgba(217, 70, 239, 0.35), rgba(168, 85, 247, 0.4)); color: #f0abfc; border: 1px solid #d946ef; box-shadow: 0 0 6px rgba(217, 70, 239, 0.4); }
    .rarity-Iconic { background: linear-gradient(135deg, rgba(234, 179, 8, 0.4), rgba(244, 63, 94, 0.4)); color: #fef08a; border: 1px solid #facc15; box-shadow: 0 0 10px rgba(250, 204, 21, 0.5); }
    .rarity-Enchanted { background: linear-gradient(135deg, rgba(56, 189, 248, 0.3), rgba(192, 132, 252, 0.4)); color: #e0e7ff; border: 1px solid #a855f7; box-shadow: 0 0 8px rgba(168, 85, 247, 0.4); }
    
    .cat-filter-row {
      display: flex;
      gap: 10px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }
    .catalog-set-select {
      flex: 1;
      min-width: 200px;
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--parch);
      padding: 8px 12px;
      font-size: .85rem;
      outline: none;
      cursor: pointer;
    }
    .catalog-set-select:focus {
      border-color: var(--gold);
    }
"""
    if '.rarity-Epic' not in content:
        content = content.replace('  </style>', rarity_css + '\n  </style>')

    # 4. Add Set selector in HTML above or alongside search input
    search_target = '<input type="text" class="catalog-search" id="catSearch" placeholder="🔍 Cerca per nome, costo o abilità (es. Mickey, Rush, Ward, Song)..." oninput="renderCatalog()">'
    new_search_html = """<div class="cat-filter-row">
          <select id="catSetSelect" class="catalog-set-select" onchange="renderCatalog()">
            <option value="all">🌐 Tutti i Set (Set 1 - 14)</option>
            <option value="set1">Set 1: The First Chapter</option>
            <option value="set2">Set 2: Rise of the Floodborn</option>
            <option value="set3">Set 3: Into the Inklands</option>
            <option value="set4">Set 4: Ursula's Return</option>
            <option value="set5">Set 5: Shimmering Skies</option>
            <option value="set6">Set 6: Azurite Sea</option>
            <option value="set7">Set 7: Whispers in the Well</option>
            <option value="set8">Set 8: Reign of Beasts</option>
            <option value="set9">Set 9: Fables of Light (🟣 Epic)</option>
            <option value="set10">Set 10: Glacial Crown (🟣 Epic)</option>
            <option value="set11">Set 11: Celestial Twilight (🟣 Epic)</option>
            <option value="set12">Set 12: Chronicles of the Deep (🟣 Epic)</option>
            <option value="set13">Set 13: Tales of the Inklands (👑 Iconic)</option>
            <option value="set14">Set 14: Hyperia City (👑 Iconic)</option>
          </select>
          <input type="text" class="catalog-search" id="catSearch" style="margin-bottom:0;flex:2;min-width:220px;" placeholder="🔍 Cerca per nome, rarità o testo (es. Mickey, Epic, Shift)..." oninput="renderCatalog()">
        </div>"""

    if search_target in content:
        content = content.replace(search_target, new_search_html)

    # 5. Update CARDS_DB initialization to load from window.LORCANA_SETS_DB
    old_init = "let activeInkFilters = new Set(['amber', 'amethyst', 'emerald', 'ruby', 'sapphire', 'steel']);"
    new_init = """let activeInkFilters = new Set(['amber', 'amethyst', 'emerald', 'ruby', 'sapphire', 'steel']);

    // Merge full database from window.LORCANA_SETS_DB
    function initDatabase() {
      const seenIds = new Set(CARDS_DB.map(c => c.id));
      if (window.LORCANA_SETS_DB && Array.isArray(window.LORCANA_SETS_DB)) {
        window.LORCANA_SETS_DB.forEach(s => {
          (s.cards || []).forEach(c => {
            if (!seenIds.has(c.id)) {
              seenIds.add(c.id);
              CARDS_DB.push({
                ...c,
                setId: s.id,
                setNum: s.num,
                setName: s.name,
                rarity: c.rarity || 'Common'
              });
            }
          });
        });
      }
    }
    initDatabase();"""

    if old_init in content and 'function initDatabase()' not in content:
        content = content.replace(old_init, new_init)

    # 6. Update renderCatalog to support set filter and display rarities
    old_filter_code = """      const filtered = CARDS_DB.filter(c => {
        if (!activeInkFilters.has(c.ink)) return false;
        if (!q) return true;
        const text = `${c.name} ${c.sub} ${c.type} ${c.kw || ''} ${c.text || ''}`.toLowerCase();
        return text.includes(q);
      });"""

    new_filter_code = """      const selSet = document.getElementById('catSetSelect') ? document.getElementById('catSetSelect').value : 'all';
      const filtered = CARDS_DB.filter(c => {
        if (!activeInkFilters.has(c.ink)) return false;
        if (selSet !== 'all' && c.setId && c.setId !== selSet) return false;
        if (!q) return true;
        const text = `${c.name} ${c.sub || ''} ${c.type || ''} ${c.kw || ''} ${c.text || ''} ${c.rarity || ''} ${c.setName || ''}`.toLowerCase();
        return text.includes(q);
      });"""

    if old_filter_code in content:
        content = content.replace(old_filter_code, new_filter_code)

    # 7. Update card item template to show rarity badge
    old_card_template = """              <div class="card-name-title">${c.name}</div>
              <div class="card-name-sub">${c.sub} · <span style="text-transform:capitalize;color:var(--${c.ink});">${c.ink}</span> ${c.kw ? '· <i>' + c.kw + '</i>' : ''}</div>"""

    new_card_template = """              <div class="card-name-title">
                ${c.name}
                ${c.rarity ? `<span class="rarity-tag rarity-${c.rarity.replace(/\\s+/g, '')}">${c.rarity === 'Iconic' ? '👑 Iconic' : (c.rarity === 'Epic' ? '🟣 Epic' : (c.rarity === 'Enchanted' ? '✨ Ench' : c.rarity))}</span>` : ''}
              </div>
              <div class="card-name-sub">${c.sub || ''} · <span style="text-transform:capitalize;color:var(--${c.ink});">${c.ink}</span> ${c.kw ? '· <i>' + c.kw + '</i>' : ''} ${c.setName ? '<span style="color:var(--gold);opacity:.8;">[' + c.setName + ']</span>' : ''}</div>"""

    if old_card_template in content:
        content = content.replace(old_card_template, new_card_template)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("deck-lab.html successfully updated!")

if __name__ == "__main__":
    main()
