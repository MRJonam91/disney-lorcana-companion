import os
import re

def upgrade_collector_vault():
    path = "collector-vault.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Link lorcana-foil-ui.css in <head>
    if "assets/css/lorcana-foil-ui.css" not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="assets/css/lorcana-foil-ui.css">\n</head>'
        )

    # 2. Include data/lorcana-i18n.js before closing </body>
    if "data/lorcana-i18n.js" not in html:
        html = html.replace(
            '<script src="data/lorcana-cards.js"></script>',
            '<script src="data/lorcana-cards.js"></script>\n  <script src="data/lorcana-i18n.js"></script>'
        )

    # 3. Upgrade Top Bar with data-i18n attributes
    old_topbar = """    <div class="top-links">
      <a href="index.html">🌐 Portale</a>
      <a href="guide/guida-lorcana-it.html">📖 Guida IT</a>
      <a href="deck-lab.html">🃏 Deck Lab</a>
      <a href="collector-vault.html" class="active">💎 Collezionismo &amp; Pulls</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank">💬 Discussions</a>
    </div>"""

    new_topbar = """    <div class="top-links">
      <a href="index.html" data-i18n="nav_hub">🌐 Hub</a>
      <a href="deck-lab.html" data-i18n="nav_decklab">🃏 Deck Lab</a>
      <a href="collector-vault.html" class="active" data-i18n="nav_vault">💎 Collezionismo &amp; Pulls</a>
      <a href="guide/guida-lorcana-it.html" data-i18n="nav_guide" data-i18n-guide-link="1">📖 Guida</a>
      <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" data-i18n="nav_app">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank" data-i18n="nav_forum">💬 Discussions</a>
    </div>"""
    if old_topbar in html:
        html = html.replace(old_topbar, new_topbar)

    # 4. Upgrade Header, Disclaimer & Tabs with data-i18n
    old_header_tabs = """    <div class="vault-header">
      <div class="vault-badge">Collector Hub, Pack Simulator &amp; Probability</div>
      <h1>Disney Lorcana · Collector's Vault</h1>
      <p class="vault-desc">Simula l'apertura realistica di bustine e box, calcola le probabilità matematiche di trovare carte Incantate e Leggendarie per ogni set, esplora il catalogo prodotti e metti alla prova le tue abilità con le sfide Illumineer.</p>
    </div>

    <!-- Navigation Tabs -->
    <!-- Disclaimer Banner Globale -->
    <div class="disclaimer-banner">
      <div class="disclaimer-icon">⚠️</div>
      <div class="disclaimer-text">
        <strong>NOTA INFORMATIVA &amp; STATISTICHE SPERIMENTALI:</strong><br>
        Disney Lorcana™ e tutti i marchi collegati sono proprietà di Disney e Ravensburger. 
        <strong>Ravensburger non pubblica probabilità o percentuali ufficiali di estrazione delle carte nei booster pack.</strong>
        Tutti i tassi, le probabilità e le simulazioni presenti in questa piattaforma sono stime sperimentali calcolate dalla community internazionale 
        (tramite tracking empirico su migliaia di box, casi studio su oltre 44 booster box documentati da <em>The Gamers Lodge</em> e discussioni didattiche su <em>Reddit r/Lorcana</em>) 
        e modelli matematici di distribuzione binomiale. Le aperture reali in negozio o blister singoli sono soggette alla naturale varianza statistica del caso.
      </div>
    </div>

    <div class="vault-tabs">
      <button class="tab-btn active" onclick="switchVaultTab('simulator')">🎴 Simulatore Spacchettamento</button>
      <button class="tab-btn" onclick="switchVaultTab('probability')">📊 Calcolatore Probabilità &amp; Pull Rate</button>
      <button class="tab-btn" onclick="switchVaultTab('guide')">📖 Guida Ritratti, Ere &amp; God Packs</button>
      <button class="tab-btn" onclick="switchVaultTab('products')">📦 Catalogo Completo Prodotti</button>
      <button class="tab-btn" onclick="switchVaultTab('challenges')">🏆 Sfide &amp; Chi Inizia?</button>
    </div>"""

    new_header_tabs = """    <div class="vault-header">
      <div class="vault-badge" data-i18n="vault_badge">Simulatore Collezionismo, Effetti Foil &amp; Pull Rate</div>
      <h1 data-i18n="vault_title">Disney Lorcana · Collector's Vault</h1>
      <p class="vault-desc" data-i18n="vault_desc">Simula l'apertura di bustine, Trove, Booster Box e Case con effetti Foil olografici. Calcola le probabilità matematiche per tutti i 14 Set (incluse Epiche e Iconiche) ed esplora il catalogo prodotti.</p>
    </div>

    <!-- Compact Glassmorphic Disclaimer Banner -->
    <div class="disclaimer-banner">
      <div class="disclaimer-icon">⚠️</div>
      <div class="disclaimer-text" data-i18n-html="disclaimer_html">
        <strong>NOTA INFORMATIVA &amp; STATISTICHE SPERIMENTALI:</strong> Disney Lorcana™ è un marchio registrato di Disney e Ravensburger. <strong>Ravensburger non pubblica percentuali ufficiali di estrazione.</strong> Tutti i tassi e i simulatori qui presenti sono stime sperimentali della community internazionale (casi studio su 44+ box di <em>The Gamers Lodge</em> e <em>Reddit r/Lorcana</em>) e modelli di distribuzione binomiale.
      </div>
    </div>

    <!-- Segmented Glassmorphic Tab Dock -->
    <div class="vault-tabs">
      <button class="tab-btn active" onclick="switchVaultTab('simulator')" data-i18n="tab_sim">🎴 Simulatore Pull</button>
      <button class="tab-btn" onclick="switchVaultTab('probability')" data-i18n="tab_prob">📊 Calcolatore Probabilità</button>
      <button class="tab-btn" onclick="switchVaultTab('guide')" data-i18n="tab_guide">📖 Ere, Simboli &amp; God Packs</button>
      <button class="tab-btn" onclick="switchVaultTab('products')" data-i18n="tab_prod">📦 Catalogo Prodotti</button>
      <button class="tab-btn" onclick="switchVaultTab('challenges')" data-i18n="tab_chal">🏆 Sfide &amp; Moneta 3D</button>
    </div>"""

    if old_header_tabs in html:
        html = html.replace(old_header_tabs, new_header_tabs)

    # 5. Reorganize Simulator Command Center & 10-Item Telemetry Grid
    sim_start_marker = '    <!-- 1. SIMULATOR VIEW -->'
    sim_end_marker = '    <!-- 2. PROBABILITY VIEW -->'
    if sim_start_marker in html and sim_end_marker in html:
        s_idx = html.index(sim_start_marker)
        e_idx = html.index(sim_end_marker)
        new_sim_block = """    <!-- 1. SIMULATOR VIEW -->
    <div id="view-simulator">
      <div class="panel">
        <div class="panel-head">
          <div class="panel-title" data-i18n="sim_panel_title">🎴 Simulatore Spacchettamento Olografico</div>
          <button class="btn-pack" onclick="resetPullStats()" data-i18n="btn_reset_col">🔄 Azzera Collezione</button>
        </div>

        <!-- Row 1: Command Bar (Set Selector + Custom Pack Opener) -->
        <div class="sim-command-bar">
          <div class="sim-set-group">
            <label for="selectSimSet" style="font-size:.86rem;color:var(--gold-soft);font-weight:700;white-space:nowrap;" data-i18n="lbl_set_select">Set Espansione:</label>
            <select class="select-set" id="selectSimSet" onchange="changeSet()">
              <option value="set14">Set 14: Hyperia City (New · 🟣 Epic &amp; 👑 Iconic)</option>
              <option value="set13" selected>Set 13: Attack of the Vine! (🟣 Epic &amp; 👑 Iconic)</option>
              <option value="set12">Set 12: Wilds Unknown (🟣 Epic &amp; 👑 Iconic)</option>
              <option value="set11">Set 11: Winterspell / Celestial Twilight (🟣 Epic)</option>
              <option value="set10">Set 10: Whispers in the Well (🟣 Epic)</option>
              <option value="set9">Set 9: Fables of Light / Fabled (🟣 Epic &amp; 👑 Iconic Debut)</option>
              <option value="set8">Set 8: Reign of Jafar / Reign of Chaos</option>
              <option value="set7">Set 7: Archazia's Island</option>
              <option value="set6">Set 6: Azurite Sea</option>
              <option value="set5">Set 5: Shimmering Skies</option>
              <option value="set4">Set 4: Ursula's Return</option>
              <option value="set3">Set 3: Into the Inklands</option>
              <option value="set2">Set 2: Rise of the Floodborn</option>
              <option value="set1">Set 1: The First Chapter</option>
            </select>
          </div>

          <div class="sim-custom-group">
            <label for="customPackCount" style="font-size:.82rem;color:var(--gold-soft);font-weight:700;" data-i18n="lbl_custom_packs">🔢 Quantità libera:</label>
            <button type="button" class="pack-step-btn" onclick="stepCustomPacks(-10)">-10</button>
            <input type="number" id="customPackCount" min="1" max="10000" value="36" class="custom-pack-input" style="width:92px;padding:6px 8px;" placeholder="36">
            <button type="button" class="pack-step-btn" onclick="stepCustomPacks(10)">+10</button>
            <button type="button" class="btn-pack primary" onclick="openCustomPacks()" data-i18n="btn_open_custom" style="padding:8px 14px;font-size:.83rem;">🚀 Apri Bustine</button>
          </div>
        </div>

        <!-- Row 2: 5-Column Product Preset Action Cards -->
        <div class="pack-presets-grid">
          <button type="button" class="pack-action-card" onclick="openPacks(1)">
            <span class="pack-action-icon">✨</span>
            <span class="pack-action-title" data-i18n="act_1_title">1 Bustina</span>
            <span class="pack-action-sub" data-i18n="act_1_sub">12 Carte · 1 Foil Garantita</span>
          </button>

          <button type="button" class="pack-action-card" onclick="openPacks(8)">
            <span class="pack-action-icon">🎁</span>
            <span class="pack-action-title" data-i18n="act_8_title">Illumineer's Trove</span>
            <span class="pack-action-sub" data-i18n="act_8_sub">8 Bustine · 96 Carte</span>
          </button>

          <button type="button" class="pack-action-card" onclick="openPacks(10)">
            <span class="pack-action-icon">📦</span>
            <span class="pack-action-title" data-i18n="act_10_title">Bundle 10 Pack</span>
            <span class="pack-action-sub" data-i18n="act_10_sub">10 Bustine · 120 Carte</span>
          </button>

          <button type="button" class="pack-action-card featured-box foil-shimmer" onclick="openPacks(24)">
            <span class="pack-action-icon">🏆</span>
            <span class="pack-action-title" data-i18n="act_24_title">1 Booster Box</span>
            <span class="pack-action-sub" data-i18n="act_24_sub">24 Bustine · 288 Carte</span>
          </button>

          <button type="button" class="pack-action-card featured-case foil-shimmer" onclick="openPacks(96)">
            <span class="pack-action-icon">🚢</span>
            <span class="pack-action-title" data-i18n="act_96_title">1 Master Case</span>
            <span class="pack-action-sub" data-i18n="act_96_sub">96 Bustine · 4 Box Sigillati</span>
          </button>
        </div>

        <!-- Row 3: 10-Item Balanced Telemetry Stats Grid (5x2 or 10x1) -->
        <div class="pull-stats-grid">
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntPacks" style="color:var(--parch);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_packs">Bustine</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntCommon" style="color:var(--common);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_common">Comuni ⚪</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntUncommon" style="color:var(--uncommon);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_uncommon">Non Comuni 📖</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntRare" style="color:var(--rare);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_rare">Rare 🔺</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntSuperRare" style="color:var(--super-rare);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_super">Super Rare 🔷</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntLegendary" style="color:var(--legendary);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_legendary">Leggendarie 🟡</div>
          </div>
          <div class="pull-stat-box" style="border-color:rgba(168,85,247,0.45)!important;background:rgba(168,85,247,0.12)!important;">
            <div class="pull-stat-val" id="cntEpic" style="color:var(--epic);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_epic">Epiche 🟣</div>
          </div>
          <div class="pull-stat-box" style="border-color:rgba(244,114,182,0.45)!important;background:rgba(244,114,182,0.12)!important;">
            <div class="pull-stat-val" id="cntEnchanted" style="color:var(--enchanted);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_enchanted">Incantate ✨</div>
          </div>
          <div class="pull-stat-box" style="border-color:rgba(250,204,21,0.55)!important;background:rgba(250,204,21,0.12)!important;">
            <div class="pull-stat-val" id="cntIconic" style="color:#fde047;">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_iconic">Iconiche 👑</div>
          </div>
          <div class="pull-stat-box" style="border-color:rgba(56,189,248,0.4)!important;background:rgba(56,189,248,0.1)!important;">
            <div class="pull-stat-val" id="cntFoils" style="color:var(--gold-soft);">0</div>
            <div class="pull-stat-lbl" data-i18n="stat_foils">Foil Totali 🌟</div>
          </div>
        </div>

        <!-- Pulled Cards Showcase -->
        <div style="font-family:'Cinzel',serif;font-size:1.05rem;color:var(--gold);margin-bottom:10px;" data-i18n="lbl_last_pulled">✨ Ultime Carte Sbustate (Passa il mouse per l'effetto Foil 3D):</div>
        <div class="cards-grid" id="pulledCardsGrid">
          <div style="grid-column: 1 / -1; text-align:center; padding: 40px; color:var(--muted);" data-i18n="empty_pull_msg">
            Seleziona un prodotto qui sopra o inserisci un numero di bustine per iniziare lo spacchettamento con effetti Foil!
          </div>
        </div>
      </div>
    </div>

"""
        html = html[:s_idx] + new_sim_block + html[e_idx:]

    # 6. Add i18n attributes to remaining panel headers
    html = html.replace(
        '<div class="panel-title">📊 Calcolatore Probabilità Matematiche &amp; Pull Rate</div>',
        '<div class="panel-title" data-i18n="prob_title">📊 Calcolatore Probabilità Matematiche &amp; Pull Rate</div>'
    )
    html = html.replace(
        '<div class="panel-title">📖 Guida ai Simboli, Rarità, Evoluzione delle Ere &amp; God Packs</div>',
        '<div class="panel-title" data-i18n="guide_title">📖 Guida ai Simboli, Rarità, Evoluzione delle Ere &amp; God Packs</div>'
    )
    html = html.replace(
        '<div class="panel-title">📦 Catalogo Completo dei Prodotti Disney Lorcana</div>',
        '<div class="panel-title" data-i18n="prod_title">📦 Catalogo Completo dei Prodotti Disney Lorcana</div>'
    )
    html = html.replace(
        '<div class="quest-title">🎲 Sfida della Serata (Community Quest Generator)</div>',
        '<div class="quest-title" data-i18n="chal_quest_title">🎲 Sfida della Serata (Community Quest Generator)</div>'
    )
    html = html.replace(
        '<button class="btn-pack primary" onclick="generateNewQuest()">✨ Genera Nuova Sfida per la Partita</button>',
        '<button class="btn-pack primary" onclick="generateNewQuest()" data-i18n="chal_quest_btn">✨ Genera Nuova Sfida per la Partita</button>'
    )
    html = html.replace(
        '<div class="panel-title">🪙 Chi Inizia il Turno 1? (Illumineer Coin Flip)</div>',
        '<div class="panel-title" data-i18n="chal_coin_title">🪙 Chi Inizia il Turno 1? (Illumineer Coin Flip)</div>'
    )

    # 7. Upgrade JS openPacks card rendering (Sort hits first + add .is-foil & .pulled-card-inner + stepCustomPacks)
    old_display_js = """      // Display up to 48 cards to keep DOM snappy
      const displayCards = pulled.slice(-48);
      displayCards.forEach(c => {
        const div = document.createElement('div');
        const rarityClass = `rarity-${c.rarity.replace(/\\s+/g, '-')}`;
        div.className = `pulled-card ${rarityClass}`;
        div.innerHTML = `
          ${c.rarity === 'Iconic' ? '<span class="pulled-iconic-badge">👑 ICONIC CHASE</span>' : ''}
          ${c.foil ? '<span class="pulled-foil-badge">FOIL</span>' : ''}
          <div style="font-size:1.4rem;margin:8px 0;">${getRarityIcon(c.rarity)}</div>
          <div style="font-weight:700;font-size:.85rem;color:var(--parch);line-height:1.2;">${c.name}</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:6px;">${c.rarity}</div>
        `;
        grid.appendChild(div);
      });"""

    new_display_js = """      // Sort hits to the front when opening multiple packs so Iconic/Enchanted/Epic/Legendary/Foil are showcased first!
      const rarityRank = { 'Iconic': 8, 'Enchanted': 7, 'Epic': 6, 'Legendary': 5, 'Super Rare': 4, 'Rare': 3, 'Uncommon': 2, 'Common': 1 };
      const sortedPulled = (n > 2)
        ? [...pulled].sort((a, b) => ((rarityRank[b.rarity] || 0) + (b.foil ? 0.5 : 0)) - ((rarityRank[a.rarity] || 0) + (a.foil ? 0.5 : 0)))
        : pulled;
      const displayCards = sortedPulled.slice(0, 48);
      displayCards.forEach(c => {
        const div = document.createElement('div');
        const rarityClass = `rarity-${c.rarity.replace(/\\s+/g, '-')}`;
        const foilClass = (c.foil || ['Epic', 'Enchanted', 'Iconic'].includes(c.rarity)) ? 'is-foil' : '';
        div.className = `pulled-card ${rarityClass} ${foilClass}`;
        div.innerHTML = `
          <div class="pulled-card-inner">
            ${c.rarity === 'Iconic' ? '<span class="pulled-iconic-badge">👑 ICONIC CHASE</span>' : ''}
            ${c.foil ? '<span class="pulled-foil-badge">✨ HOLO FOIL</span>' : ''}
            <div style="font-size:1.55rem;margin:6px 0;filter:drop-shadow(0 2px 6px rgba(0,0,0,0.45));">${getRarityIcon(c.rarity)}</div>
            <div style="font-weight:700;font-size:.86rem;color:var(--parch);line-height:1.25;">${c.name}</div>
            <div style="font-size:.71rem;color:var(--gold-soft);margin-top:4px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;">${c.rarity}</div>
          </div>
        `;
        grid.appendChild(div);
      });"""

    if old_display_js in html:
        html = html.replace(old_display_js, new_display_js)

    # Add stepCustomPacks helper and localized generateNewQuest
    if "function stepCustomPacks" not in html:
        html = html.replace(
            "function openCustomPacks() {",
            """function stepCustomPacks(delta) {
      const inp = document.getElementById('customPackCount');
      let v = parseInt(inp.value, 10) || 1;
      v = Math.max(1, Math.min(10000, v + delta));
      inp.value = v;
    }

    function openCustomPacks() {"""
        )

    old_quest_fn = """    function generateNewQuest() {
      const q = QUESTS[Math.floor(Math.random() * QUESTS.length)];
      document.getElementById('questText').innerText = `"${q}"`;
    }"""
    new_quest_fn = """    function generateNewQuest() {
      const lang = window.currentLorcanaLang || 'it';
      const pool = (window.LORCANA_QUESTS_I18N && window.LORCANA_QUESTS_I18N[lang]) ? window.LORCANA_QUESTS_I18N[lang] : QUESTS;
      const q = pool[Math.floor(Math.random() * pool.length)];
      document.getElementById('questText').innerText = `"${q}"`;
    }"""
    if old_quest_fn in html:
        html = html.replace(old_quest_fn, new_quest_fn)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("collector-vault.html upgraded with UI, Foil FX & 5-language i18n!")


def upgrade_deck_lab():
    path = "deck-lab.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "assets/css/lorcana-foil-ui.css" not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="assets/css/lorcana-foil-ui.css">\n</head>'
        )

    if "data/lorcana-i18n.js" not in html:
        html = html.replace(
            '<script src="data/lorcana-cards.js"></script>',
            '<script src="data/lorcana-cards.js"></script>\n  <script src="data/lorcana-i18n.js"></script>'
        )

    # Top bar i18n
    old_top = """    <div class="top-links">
      <a href="index.html">🌐 Portale</a>
      <a href="guide/guida-lorcana-it.html">📖 Guida IT</a>
      <a href="collector-vault.html">💎 Collezionismo &amp; Pulls</a>
      <a href="deck-lab.html" class="active">🃏 Deck Lab</a>
      <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" style="color:var(--gold);">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank">💬 Discussions</a>
    </div>"""
    new_top = """    <div class="top-links">
      <a href="index.html" data-i18n="nav_hub">🌐 Hub</a>
      <a href="deck-lab.html" class="active" data-i18n="nav_decklab">🃏 Deck Lab</a>
      <a href="collector-vault.html" data-i18n="nav_vault">💎 Collezionismo &amp; Pulls</a>
      <a href="guide/guida-lorcana-it.html" data-i18n="nav_guide" data-i18n-guide-link="1">📖 Guida</a>
      <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" style="color:var(--gold);" data-i18n="nav_app">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank" data-i18n="nav_forum">💬 Discussions</a>
    </div>"""
    if old_top in html:
        html = html.replace(old_top, new_top)

    # Header & Tabs i18n
    html = html.replace(
        '<div class="lab-badge">Tournament Deck Builder &amp; Playtester</div>',
        '<div class="lab-badge" data-i18n="dl_badge">Tournament Deck Builder &amp; Playtester</div>'
    )
    html = html.replace(
        '<h1>Disney Lorcana · Deck Lab</h1>',
        '<h1 data-i18n="dl_title">Disney Lorcana · Deck Lab</h1>'
    )
    html = html.replace(
        '<p class="lab-desc">Costruisci il tuo mazzo da 60 carte, analizza la curva d\'inchiostro, testa la mano iniziale con mulligan realistico e simula i primi turni. Esporta per <strong>duels.ink</strong>, <strong>inktable</strong> o <strong>dreamborn</strong>.</p>',
        '<p class="lab-desc" data-i18n="dl_desc">Costruisci il tuo mazzo da 60 carte, analizza la curva d\'inchiostro, testa la mano iniziale con mulligan realistico e simula i primi turni. Esporta per duels.ink, inktable o dreamborn.</p>'
    )
    html = html.replace(
        '<button class="tab-btn active" onclick="switchLabTab(\'builder\')">🛠️ Deck Builder &amp; Curva</button>',
        '<button class="tab-btn active" onclick="switchLabTab(\'builder\')" data-i18n="dl_tab_builder">🛠️ Deck Builder &amp; Curva</button>'
    )
    html = html.replace(
        '<button class="tab-btn" onclick="switchLabTab(\'goldfish\')">🎲 Simulatore Mano &amp; Goldfish Playtester</button>',
        '<button class="tab-btn" onclick="switchLabTab(\'goldfish\')" data-i18n="dl_tab_goldfish">🎲 Simulatore Mano &amp; Goldfish</button>'
    )
    html = html.replace(
        '<button class="tab-btn" onclick="openSimulatorLinks()">⚡ Gioca Online (Duels.ink &amp; Inktable)</button>',
        '<button class="tab-btn" onclick="openSimulatorLinks()" data-i18n="dl_tab_online">⚡ Gioca Online (Duels.ink &amp; Inktable)</button>'
    )
    html = html.replace(
        '<div class="panel-title">📚 Catalogo Carte &amp; Sinergie</div>',
        '<div class="panel-title" data-i18n="dl_cat_title">📚 Catalogo Carte (Set 1 – 14)</div>'
    )
    html = html.replace(
        'id="catSearch"',
        'id="catSearch" data-i18n-placeholder="dl_search_ph"'
    )
    html = html.replace(
        '<div class="stat-lbl">Carte Totali</div>',
        '<div class="stat-lbl" data-i18n="dl_stat_total">Carte Totali</div>'
    )
    html = html.replace(
        '<div class="stat-lbl">Inchiostrabili</div>',
        '<div class="stat-lbl" data-i18n="dl_stat_ink">Inchiostrabili</div>'
    )
    html = html.replace(
        '<div class="stat-lbl">Non-Inkable</div>',
        '<div class="stat-lbl" data-i18n="dl_stat_noink">Non-Inkable</div>'
    )
    html = html.replace(
        '<div class="stat-lbl">Costo Medio</div>',
        '<div class="stat-lbl" data-i18n="dl_stat_avg">Costo Medio</div>'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("deck-lab.html upgraded with UI, Foil FX & 5-language i18n!")


def upgrade_index():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    if "assets/css/lorcana-foil-ui.css" not in html:
        html = html.replace(
            "</head>",
            '  <link rel="stylesheet" href="assets/css/lorcana-foil-ui.css">\n</head>'
        )

    if "data/lorcana-i18n.js" not in html:
        html = html.replace(
            "</body>",
            '  <script src="data/lorcana-i18n.js"></script>\n</body>'
        )

    old_top = """    <div class="top-links">
      <a href="index.html" class="active">🌐 Hub Home</a>
      <a href="deck-lab.html" class="highlight">🃏 Deck Lab &amp; Test</a>
      <a href="collector-vault.html" class="highlight" style="border-color:#f472b6;color:#ff80bf;">💎 Collezionismo &amp; Pulls</a>
      <a href="guide/guida-lorcana-it.html">📖 Guida IT</a>
      <a href="guide/lorcana-guide-en.html">🇬🇧 Guide EN</a>
      <a href="#official-app">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank">💬 Forum</a>
    </div>"""
    new_top = """    <div class="top-links">
      <a href="index.html" class="active" data-i18n="nav_hub">🌐 Hub</a>
      <a href="deck-lab.html" class="highlight" data-i18n="nav_decklab">🃏 Deck Lab</a>
      <a href="collector-vault.html" class="highlight" style="border-color:#f472b6;color:#ff80bf;" data-i18n="nav_vault">💎 Collezionismo &amp; Pulls</a>
      <a href="guide/guida-lorcana-it.html" data-i18n="nav_guide" data-i18n-guide-link="1">📖 Guida</a>
      <a href="#official-app" data-i18n="nav_app">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank" data-i18n="nav_forum">💬 Forum</a>
    </div>"""
    if old_top in html:
        html = html.replace(old_top, new_top)

    html = html.replace(
        '<div class="badge">✦ The Ultimate Illumineer Portal ✦</div>',
        '<div class="badge" data-i18n="idx_badge">✦ Il Portale Definitivo per gli Illumineer ✦</div>'
    )
    html = html.replace(
        '<p class="subtitle">Complete community repository, interactive strategy guides in 5 languages, full set history from Chapter 1 to Set 14, card rarities &amp; collecting, tournament meta analytics, and tabletop tools.</p>',
        '<p class="subtitle" data-i18n="idx_subtitle">Repository completo della community, guide strategiche interattive in 5 lingue, storico dei 14 Set, rarità e collezionismo, simulatore spacchettamento foil e laboratorio mazzi da torneo.</p>'
    )
    html = html.replace(
        '<a href="deck-lab.html" class="btn-hero gold">🃏 Apri Deck Lab &amp; Playtester</a>',
        '<a href="deck-lab.html" class="btn-hero gold foil-shimmer" data-i18n="idx_cta_deck">🃏 Apri Deck Lab &amp; Playtester</a>'
    )
    html = html.replace(
        '<a href="collector-vault.html" class="btn-hero pink">💎 Apri Collector\'s Vault &amp; Pulls</a>',
        '<a href="collector-vault.html" class="btn-hero pink foil-shimmer" data-i18n="idx_cta_vault">💎 Apri Collector\'s Vault &amp; Pulls</a>'
    )
    html = html.replace(
        '<a href="guide/guida-lorcana-it.html" class="btn-hero dark">📖 Leggi Guida Ufficiale (IT)</a>',
        '<a href="guide/guida-lorcana-it.html" class="btn-hero dark" data-i18n="idx_cta_guide" data-i18n-guide-link="1">📖 Leggi Guida Interattiva</a>'
    )
    html = html.replace(
        '<a href="#official-app" class="btn-hero dark">📱 App Ufficiale Ravensburger</a>',
        '<a href="#official-app" class="btn-hero dark" data-i18n="idx_cta_app">📱 App Ufficiale Ravensburger</a>'
    )
    html = html.replace(
        '<h2 class="section-title">Select Your Language / Scegli la tua Lingua</h2>',
        '<h2 class="section-title" data-i18n="idx_lang_title">Scegli la Tua Lingua · 5 Edizioni Ufficiali</h2>'
    )
    html = html.replace(
        '<p class="section-desc">Experience the complete standalone interactive web guide with lore tracker, card breakdown, and mulligan simulator.</p>',
        '<p class="section-desc" data-i18n="idx_lang_desc">Guide interattive standalone, regole complete, segnapunti Lore e simulatore matematico del mulligan.</p>'
    )
    html = html.replace(
        '<h2 class="section-title">✨ Community Web Apps &amp; Tabletop Simulators</h2>',
        '<h2 class="section-title" data-i18n="idx_apps_title">✨ Web App Interattive &amp; Simulatori da Tavolo</h2>'
    )
    html = html.replace(
        '<p class="section-desc">Interactive tools built for deck building, goldfish playtesting, booster pack opening, and collecting.</p>',
        '<p class="section-desc" data-i18n="idx_apps_desc">Strumenti avanzati con effetti Foil olografici CSS per creazione mazzi, goldfish playtesting e calcolo pull rate.</p>'
    )
    html = html.replace(
        '<h3 style="font-family:\'Cinzel\',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;">Deck Lab &amp; Playtester</h3>',
        '<h3 style="font-family:\'Cinzel\',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;" data-i18n="idx_deck_title">Deck Lab &amp; Playtester</h3>'
    )
    html = html.replace(
        '<a href="deck-lab.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;">Lancia Deck Lab &amp; Playtester ➔</a>',
        '<a href="deck-lab.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;" data-i18n="idx_deck_btn">Lancia Deck Lab &amp; Playtester ➔</a>'
    )
    html = html.replace(
        '<h3 style="font-family:\'Cinzel\',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;">Collector\'s Vault &amp; Pulls</h3>',
        '<h3 style="font-family:\'Cinzel\',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;" data-i18n="idx_vault_title">Collector\'s Vault &amp; Pulls</h3>'
    )
    html = html.replace(
        '<a href="collector-vault.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;border-color:#f472b6;color:#ff80bf;">Apri Collector\'s Vault ➔</a>',
        '<a href="collector-vault.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;border-color:#f472b6;color:#ff80bf;" data-i18n="idx_vault_btn">Apri Collector\'s Vault ➔</a>'
    )
    html = html.replace(
        '<h2 class="section-title">Repository Knowledge Base</h2>',
        '<h2 class="section-title" data-i18n="idx_kb_title">Knowledge Base &amp; Documentazione</h2>'
    )
    html = html.replace(
        '<div style="font-size:0.8rem;letter-spacing:0.12em;text-transform:uppercase;color:#93c5fd;font-weight:700;margin-bottom:8px;">App Ufficiale Ravensburger per il Collezionismo</div>',
        '<div style="font-size:0.8rem;letter-spacing:0.12em;text-transform:uppercase;color:#93c5fd;font-weight:700;margin-bottom:8px;" data-i18n="idx_app_badge">App Ufficiale Ravensburger per il Collezionismo</div>'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html upgraded with UI, Foil FX & 5-language i18n!")


def upgrade_guides():
    guide_files = [
        ("guide/guida-lorcana-it.html", "it"),
        ("guide/lorcana-guide-en.html", "en"),
        ("guide/lorcana-guide-fr.html", "fr"),
        ("guide/lorcana-guide-de.html", "de"),
        ("guide/lorcana-guide-es.html", "es"),
    ]
    for path, lang in guide_files:
        if not os.path.exists(path):
            continue
        with open(path, "r", encoding="utf-8") as f:
            html = f.read()

        if "lorcana-foil-ui.css" not in html:
            html = html.replace(
                "</head>",
                '  <link rel="stylesheet" href="../assets/css/lorcana-foil-ui.css">\n</head>'
            )

        if "class=\"top-bar\"" not in html:
            top_nav = f"""  <!-- Global Top Navigation Bar -->
  <div class="top-bar">
    <a href="../index.html" class="top-brand">
      <span>✦ DISNEY LORCANA</span>
    </a>
    <div class="top-links">
      <a href="../index.html" data-i18n="nav_hub">🌐 Hub</a>
      <a href="../deck-lab.html" data-i18n="nav_decklab">🃏 Deck Lab</a>
      <a href="../collector-vault.html" data-i18n="nav_vault">💎 Collector Vault</a>
      <a href="#" class="active" data-i18n="nav_guide">📖 Guide</a>
      <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" data-i18n="nav_app">📱 App</a>
    </div>
  </div>
"""
            html = html.replace("<body>", "<body>\n" + top_nav, 1)

        if "lorcana-i18n.js" not in html:
            html = html.replace(
                "</body>",
                f'  <script>localStorage.setItem("lorcana_lang", "{lang}");</script>\n  <script src="../data/lorcana-i18n.js"></script>\n</body>'
            )

        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Upgraded {path} with Global Top Bar & Language Switcher!")

if __name__ == "__main__":
    upgrade_collector_vault()
    upgrade_deck_lab()
    upgrade_index()
    upgrade_guides()
