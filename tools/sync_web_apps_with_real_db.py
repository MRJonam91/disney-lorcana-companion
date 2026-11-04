import re

def update_foil_css():
    path = "assets/css/lorcana-foil-ui.css"
    with open(path, "r", encoding="utf-8") as f:
        css = f.read()

    badge_fix_css = """
/* Fix Badge Overlap & Horizontal Panel Overflow */
.panel {
  overflow-x: hidden;
}

.pulled-badge-row {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  gap: 4px;
  width: 100%;
  margin-bottom: 4px;
}

.pulled-foil-badge,
.pulled-iconic-badge {
  position: static !important;
  display: inline-block !important;
  font-size: 0.6rem !important;
  font-weight: 900 !important;
  padding: 2px 6px !important;
  border-radius: 99px !important;
  line-height: 1.2 !important;
  white-space: nowrap !important;
}

.set-meta-banner {
  background: rgba(15, 11, 26, 0.78);
  border: 1px solid rgba(229, 185, 92, 0.28);
  border-radius: 11px;
  padding: 10px 14px;
  margin-bottom: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
  font-size: 0.81rem;
}

.set-meta-downloads {
  display: flex;
  gap: 6px;
  flex-wrap: wrap;
}

.set-dl-pill {
  background: rgba(229, 185, 92, 0.12);
  border: 1px solid rgba(229, 185, 92, 0.35);
  color: var(--gold-bright);
  padding: 3px 9px;
  border-radius: 6px;
  font-size: 0.74rem;
  font-weight: 700;
  transition: all 0.15s;
}

.set-dl-pill:hover {
  background: rgba(229, 185, 92, 0.28);
  transform: translateY(-1px);
}
"""
    if ".pulled-badge-row" not in css:
        css += badge_fix_css
        with open(path, "w", encoding="utf-8") as f:
            f.write(css)
        print("Updated assets/css/lorcana-foil-ui.css with badge & layout fixes!")


def update_collector_vault():
    path = "collector-vault.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update #selectSimSet options with exact official names and counts
    old_select_block = re.search(r'<select class="select-set" id="selectSimSet" onchange="changeSet\(\)">.*?</select>', html, re.S)
    new_select_html = """<select class="select-set" id="selectSimSet" onchange="changeSet()">
              <option value="set14">Set 14: Hyperia City (242 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set13" selected>Set 13: Attack of the Vine! (247 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set12">Set 12: Wilds Unknown (243 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set11">Set 11: Winterspell (243 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set10">Set 10: Whispers in the Well (242 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set9">Set 9: Fabled (243 Cards · 🟣 18 Epic &amp; 👑 2 Iconic)</option>
              <option value="set8">Set 8: Reign of Jafar (229 Cards · ✨ 18 Enchanted)</option>
              <option value="set7">Set 7: Archazia's Island (224 Cards · ✨ 18 Enchanted)</option>
              <option value="set6">Set 6: Azurite Sea (222 Cards · ✨ 18 Enchanted)</option>
              <option value="set5">Set 5: Shimmering Skies (223 Cards · ✨ 18 Enchanted)</option>
              <option value="set4">Set 4: Ursula's Return (225 Cards · ✨ 18 Enchanted)</option>
              <option value="set3">Set 3: Into the Inklands (227 Cards · ✨ 18 Enchanted)</option>
              <option value="set2">Set 2: Rise of the Floodborn (216 Cards · ✨ 12 Enchanted)</option>
              <option value="set1">Set 1: The First Chapter (216 Cards · ✨ 12 Enchanted)</option>
            </select>"""
    if old_select_block:
        html = html[:old_select_block.start()] + new_select_html + html[old_select_block.end():]

    # 2. Insert Live Set Info & Download Bar right below .sim-command-bar
    if 'id="setMetaBanner"' not in html:
        target_marker = '<!-- Row 2: 5-Column Official Sealed Products Preset Cards -->'
        meta_banner_html = """<!-- Active Set Info & Chase Summary Bar -->
        <div class="set-meta-banner" id="setMetaBanner">
          <div id="setMetaDetails">
            <strong style="color:var(--gold-bright);">Set 13: Attack of the Vine!</strong> · 247 Carte Ufficiali · 👑 <strong>Iconiche:</strong> #244 Lilo &amp; Stitch, #245 Belle &amp; Beast
          </div>
          <div class="set-meta-downloads" id="setMetaDownloads">
            <a href="docs/sets/cards/set-13-attack-of-the-vine.md" target="_blank" class="set-dl-pill">📖 Card List MD</a>
            <a href="data/sets/json/set-13-attack-of-the-vine.json" target="_blank" class="set-dl-pill">📦 JSON</a>
            <a href="data/sets/csv/set-13-attack-of-the-vine.csv" target="_blank" class="set-dl-pill">📊 CSV</a>
            <a href="data/sets/db/set-13-attack-of-the-vine.db" target="_blank" class="set-dl-pill">🗄️ SQLite DB</a>
          </div>
        </div>

        """
        html = html.replace(target_marker, meta_banner_html + target_marker)

    # 3. Update JS getSampleCard, openPacks card template, and changeSet()
    old_sample_fn = re.search(r'function getSampleCard\(rarity, setMeta, isFoil\)\s*\{.*?\}', html, re.S)
    new_sample_fn = """function getSampleCard(rarity, setMeta, isFoil) {
      const inSet = (setMeta.cards || []).filter(c => c.rarity === rarity);
      if (inSet.length > 0) {
        const picked = inSet[Math.floor(Math.random() * inSet.length)];
        const fullName = picked.sub ? `${picked.name} - ${picked.sub}` : picked.name;
        const price = isFoil ? (picked.foil_usd || picked.usd || null) : (picked.usd || picked.foil_usd || null);
        return {
          num: picked.num || '',
          name: fullName,
          rarity: rarity,
          foil: isFoil,
          ink: picked.ink || '',
          cost: picked.cost || 0,
          price: price
        };
      }
      const generic = (CARD_SAMPLES[rarity] || CARD_SAMPLES.Common);
      return { num: '', name: generic[Math.floor(Math.random() * generic.length)], rarity: rarity, foil: isFoil, price: null };
    }"""
    if old_sample_fn:
        html = html[:old_sample_fn.start()] + new_sample_fn + html[old_sample_fn.end():]

    # Update card HTML rendering inside openPacks
    old_card_render = re.search(r'div\.innerHTML = `\s*<div class="pulled-card-inner">.*?</div>\s*`;', html, re.S)
    new_card_render = """div.innerHTML = `
          <div class="pulled-card-inner">
            <div class="pulled-badge-row">
              ${c.num ? `<span style="font-size:.64rem;color:var(--muted);font-weight:700;">#${c.num}</span>` : ''}
              ${c.rarity === 'Iconic' ? '<span class="pulled-iconic-badge">👑 ICONIC</span>' : ''}
              ${c.foil ? '<span class="pulled-foil-badge">✨ FOIL</span>' : ''}
            </div>
            <div style="font-size:1.5rem;margin:4px 0;filter:drop-shadow(0 2px 6px rgba(0,0,0,0.45));">${getRarityIcon(c.rarity)}</div>
            <div style="font-weight:700;font-size:.84rem;color:var(--parch);line-height:1.25;">${c.name}</div>
            <div style="display:flex;justify-content:center;align-items:center;gap:6px;margin-top:4px;flex-wrap:wrap;">
              <span style="font-size:.69rem;color:var(--gold-soft);font-weight:700;letter-spacing:.04em;text-transform:uppercase;">${c.rarity}</span>
              ${c.price ? `<span style="font-size:.68rem;background:rgba(34,197,94,0.18);color:#86efac;border:1px solid rgba(34,197,94,0.4);padding:1px 5px;border-radius:4px;font-weight:700;">$${Number(c.price).toFixed(2)}</span>` : ''}
            </div>
          </div>
        `;"""
    if old_card_render:
        html = html[:old_card_render.start()] + new_card_render + html[old_card_render.end():]

    # Update changeSet() so it updates #setMetaDetails and #setMetaDownloads dynamically
    old_change_set = """    function changeSet() {
      resetPullStats();
    }"""
    new_change_set = """    const SET_SLUGS = {
      set1: 'set-01-the-first-chapter',
      set2: 'set-02-rise-of-the-floodborn',
      set3: 'set-03-into-the-inklands',
      set4: 'set-04-ursula-s-return',
      set5: 'set-05-shimmering-skies',
      set6: 'set-06-azurite-sea',
      set7: 'set-07-archazia-s-island',
      set8: 'set-08-reign-of-jafar',
      set9: 'set-09-fabled',
      set10: 'set-10-whispers-in-the-well',
      set11: 'set-11-winterspell',
      set12: 'set-12-wilds-unknown',
      set13: 'set-13-attack-of-the-vine',
      set14: 'set-14-hyperia-city'
    };

    function updateSetMetaBanner() {
      const currentSetId = document.getElementById('selectSimSet').value;
      const setMeta = (window.LORCANA_SETS_DB || []).find(s => s.id === currentSetId);
      if (!setMeta) return;
      const slug = SET_SLUGS[currentSetId] || 'set-13-attack-of-the-vine';
      const detailsEl = document.getElementById('setMetaDetails');
      const dlEl = document.getElementById('setMetaDownloads');
      if (detailsEl) {
        const iconicInfo = (setMeta.iconic_cards && setMeta.iconic_cards.length > 0)
          ? ` · 👑 <strong>Iconiche (2):</strong> ${setMeta.iconic_cards.join(' &amp; ')}`
          : ` · ✨ <strong>Enchanted:</strong> ${(setMeta.rarity_counts && setMeta.rarity_counts.Enchanted) || 18} Carte`;
        detailsEl.innerHTML = `<strong style="color:var(--gold-bright);">Set ${setMeta.num}: ${setMeta.name}</strong> (${setMeta.date}) · <strong>${setMeta.total} Carte Ufficiali</strong>${iconicInfo}`;
      }
      if (dlEl) {
        dlEl.innerHTML = `
          <a href="docs/sets/cards/${slug}.md" target="_blank" class="set-dl-pill">📖 Card List MD</a>
          <a href="data/sets/json/${slug}.json" target="_blank" class="set-dl-pill">📦 JSON</a>
          <a href="data/sets/csv/${slug}.csv" target="_blank" class="set-dl-pill">📊 CSV</a>
          <a href="data/sets/db/${slug}.db" target="_blank" class="set-dl-pill">🗄️ SQLite DB</a>
        `;
      }
    }

    function changeSet() {
      updateSetMetaBanner();
      resetPullStats();
    }
    window.addEventListener('DOMContentLoaded', updateSetMetaBanner);"""

    if old_change_set in html:
        html = html.replace(old_change_set, new_change_set)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated collector-vault.html with real 3,242-card DB, Iconic names, prices, and per-set download links!")


def update_deck_lab():
    path = "deck-lab.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Set selector options in deck-lab.html
    old_set_select = re.search(r'<select id="catSetSelect" class="catalog-set-select" onchange="renderCatalog\(\)">.*?</select>', html, re.S)
    new_set_select = """<select id="catSetSelect" class="catalog-set-select" onchange="renderCatalog()">
            <option value="all">🌐 Tutti i 14 Set (3.242 Carte Ufficiali)</option>
            <option value="set14">Set 14: Hyperia City (242 Carte)</option>
            <option value="set13">Set 13: Attack of the Vine! (247 Carte)</option>
            <option value="set12">Set 12: Wilds Unknown (243 Carte)</option>
            <option value="set11">Set 11: Winterspell (243 Carte)</option>
            <option value="set10">Set 10: Whispers in the Well (242 Carte)</option>
            <option value="set9">Set 9: Fabled (243 Carte)</option>
            <option value="set8">Set 8: Reign of Jafar (229 Carte)</option>
            <option value="set7">Set 7: Archazia's Island (224 Carte)</option>
            <option value="set6">Set 6: Azurite Sea (222 Carte)</option>
            <option value="set5">Set 5: Shimmering Skies (223 Carte)</option>
            <option value="set4">Set 4: Ursula's Return (225 Carte)</option>
            <option value="set3">Set 3: Into the Inklands (227 Carte)</option>
            <option value="set2">Set 2: Rise of the Floodborn (216 Carte)</option>
            <option value="set1">Set 1: The First Chapter (216 Carte)</option>
          </select>"""
    if old_set_select:
        html = html[:old_set_select.start()] + new_set_select + html[old_set_select.end():]

    # 2. Cap renderCatalog DOM rendering at 100 items so 3,242 cards remain ultra-fast
    old_for_each = "filtered.forEach(c => {"
    new_for_each = """const shown = filtered.slice(0, 100);
      if (filtered.length > 100) {
        const infoDiv = document.createElement('div');
        infoDiv.style.cssText = 'font-size:.76rem;color:var(--gold-soft);padding:6px 10px;background:rgba(229,185,92,0.08);border:1px dashed var(--line);border-radius:8px;margin-bottom:8px;text-align:center;';
        infoDiv.innerText = `Mostrando le prime 100 di ${filtered.length} carte corrispondenti. Filtra per Set, Inchiostro o nome per affinare.`;
        cont.appendChild(infoDiv);
      }
      shown.forEach(c => {"""
    if old_for_each in html:
        html = html.replace(old_for_each, new_for_each, 1)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated deck-lab.html to handle all 3,242 real cards smoothly!")

if __name__ == "__main__":
    update_foil_css()
    update_collector_vault()
    update_deck_lab()
