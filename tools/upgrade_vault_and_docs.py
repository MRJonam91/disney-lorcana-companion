import os
import shutil
import re

def copy_assets():
    os.makedirs("assets/img", exist_ok=True)
    src_dir = r"C:\Users\conta\.gemini\antigravity\brain\bb5de452-853d-4410-aecd-be64676dc373\.user_uploaded"
    mapping = {
        "media_1792746278046_c4854421.jpg": "assets/img/lorcana-rarities-symbols.jpg",
        "media_1792746246172_7b50e2f3.png": "assets/img/community-pull-rates.png",
        "media_1792746253806_6139574c.png": "assets/img/pack-structure.png",
        "media_1792746299546_cd4b0ebf.png": "assets/img/card-rarities-text.png",
        "media_1792746364883_cbcc1f23.png": "assets/img/rarity-tiers-table.png",
    }
    for src_name, dst_path in mapping.items():
        src_path = os.path.join(src_dir, src_name)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"Copied {src_name} -> {dst_path}")
        else:
            print(f"Warning: {src_path} not found")

def upgrade_collector_vault():
    path = "collector-vault.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add extra CSS styles for disclaimer, custom input, guide & reddit
    extra_css = """
    /* Disclaimer Banner */
    .disclaimer-banner {
      background: linear-gradient(135deg, rgba(234, 179, 8, 0.12), rgba(20, 15, 30, 0.85));
      border: 1px solid rgba(234, 179, 8, 0.4);
      border-radius: 12px;
      padding: 14px 18px;
      margin-bottom: 22px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
      font-size: .84rem;
      color: var(--parch-muted);
      line-height: 1.5;
    }
    .disclaimer-icon {
      font-size: 1.5rem;
      line-height: 1;
    }
    .custom-pack-row {
      display: flex;
      align-items: center;
      gap: 12px;
      margin-top: 14px;
      padding: 12px 16px;
      background: rgba(0, 0, 0, 0.35);
      border: 1px dashed var(--line);
      border-radius: 10px;
      flex-wrap: wrap;
    }
    .custom-pack-input {
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 8px;
      color: var(--parch);
      padding: 8px 14px;
      width: 120px;
      font-size: .95rem;
      outline: none;
      font-weight: 700;
      text-align: center;
    }
    .custom-pack-input:focus {
      border-color: var(--gold);
    }
    
    /* Guide Styles */
    .era-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 18px;
      margin-top: 16px;
    }
    .era-card {
      background: var(--surface-2);
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 20px;
      transition: all .2s;
    }
    .era-card:hover {
      border-color: var(--gold);
      transform: translateY(-2px);
    }
    .era-badge {
      display: inline-block;
      font-size: .72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: .08em;
      padding: 3px 10px;
      border-radius: 99px;
      margin-bottom: 10px;
    }
    .era-classic { background: rgba(59, 126, 194, .2); color: #93c5fd; border: 1px solid #3b82f6; }
    .era-expansion { background: rgba(63, 163, 100, .2); color: #86efac; border: 1px solid #22c55e; }
    .era-modern { background: linear-gradient(135deg, rgba(217, 70, 239, .3), rgba(234, 179, 8, .3)); color: #fef08a; border: 1px solid #eab308; }
    
    .godpack-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 16px;
      margin: 16px 0;
    }
    .godpack-card {
      background: linear-gradient(145deg, rgba(23, 18, 36, 0.9), rgba(13, 10, 20, 0.9));
      border: 1px solid var(--line);
      border-radius: 12px;
      padding: 18px;
      position: relative;
    }
    .reddit-banner {
      background: linear-gradient(135deg, rgba(255, 69, 0, 0.15), var(--surface));
      border: 1.5px solid #ff4500;
      border-radius: 14px;
      padding: 20px 24px;
      margin-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      flex-wrap: wrap;
    }
    .btn-reddit {
      background: #ff4500;
      color: #fff;
      font-weight: 700;
      padding: 10px 20px;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: .88rem;
      border: none;
      cursor: pointer;
      transition: all .2s;
    }
    .btn-reddit:hover {
      background: #e03d00;
      transform: translateY(-2px);
      box-shadow: 0 4px 14px rgba(255, 69, 0, 0.4);
    }
    .symbol-table-wrap {
      overflow-x: auto;
      margin: 18px 0;
    }
    .symbol-table {
      width: 100%;
      border-collapse: collapse;
      font-size: .88rem;
    }
    .symbol-table th {
      background: rgba(0,0,0,0.4);
      padding: 10px 14px;
      text-align: left;
      color: var(--gold);
      border-bottom: 2px solid var(--line);
    }
    .symbol-table td {
      padding: 10px 14px;
      border-bottom: 1px solid rgba(229, 185, 92, 0.1);
    }
    .symbol-table tr:hover td {
      background: rgba(229, 185, 92, 0.05);
    }
"""
    if '.disclaimer-banner' not in html:
        html = html.replace('  </style>', extra_css + '\n  </style>')

    # 2. Add Tab button in .vault-tabs
    old_tabs = """    <div class="vault-tabs">
      <button class="tab-btn active" onclick="switchVaultTab('simulator')">🎴 Simulatore Spacchettamento</button>
      <button class="tab-btn" onclick="switchVaultTab('probability')">📊 Calcolatore Probabilità &amp; Pull Rate</button>
      <button class="tab-btn" onclick="switchVaultTab('products')">📦 Catalogo Completo Prodotti</button>
      <button class="tab-btn" onclick="switchVaultTab('challenges')">🏆 Sfide &amp; Chi Inizia?</button>
    </div>"""

    new_tabs = """    <!-- Disclaimer Banner Globale -->
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

    if old_tabs in html:
        html = html.replace(old_tabs, new_tabs)

    # 3. Add Custom Pack Input inside #view-simulator controls
    old_sim_controls_end = """          <button class="btn-pack primary" onclick="openPacks(24)">🏆 Apri 1 Booster Box (24 Bustine)</button>
          <button class="btn-pack" onclick="openPacks(96)">🚢 Apri 1 Case (96 Bustine)</button>
        </div>"""

    new_sim_controls_end = """          <button class="btn-pack primary" onclick="openPacks(24)">🏆 Apri 1 Booster Box (24 Bustine)</button>
          <button class="btn-pack" onclick="openPacks(96)">🚢 Apri 1 Case (96 Bustine)</button>
        </div>

        <!-- Custom Pack Input Bar -->
        <div class="custom-pack-row">
          <label for="customPackCount" style="font-size:.88rem;color:var(--gold-soft);font-weight:700;">🔢 Oppure inserisci quante bustine vuoi aprire:</label>
          <input type="number" id="customPackCount" min="1" max="10000" value="36" class="custom-pack-input" placeholder="Es. 36">
          <button class="btn-pack primary" onclick="openCustomPacks()">🚀 Apri Bustine Personalizzate</button>
          <span style="font-size:.78rem;color:var(--muted);">(Puoi inserire qualsiasi quantità, da 1 a 10.000 bustine per testare grandi campioni!)</span>
        </div>"""

    if old_sim_controls_end in html:
        html = html.replace(old_sim_controls_end, new_sim_controls_end)

    # 4. Insert view-guide section before view-products
    view_guide_html = """    <!-- 2.5 GUIDE VIEW (Rarities, Eras & God Packs) -->
    <div id="view-guide" style="display:none;">
      <div class="panel">
        <div class="panel-head">
          <div class="panel-title">📖 Guida ai Simboli, Rarità, Evoluzione delle Ere &amp; God Packs</div>
        </div>

        <p style="font-size:.9rem;color:var(--parch-muted);margin-bottom:20px;line-height:1.6;">
          Guida analitica basata sulle osservazioni empiriche della community globale, sui report di apertura di massa (es. 44 booster box aperti per set da <em>The Gamers Lodge</em>) 
          e sui thread di discussione e ricerca didattica su <strong>Reddit r/Lorcana</strong>.
        </p>

        <!-- Reddit Recommendation Banner -->
        <div class="reddit-banner">
          <div>
            <div style="font-weight:800;font-size:1.15rem;color:#ff4500;margin-bottom:6px;display:flex;align-items:center;gap:8px;">
              <span>🤖 Risorsa Consigliata: Reddit r/Lorcana (Flair "Educational")</span>
            </div>
            <p style="font-size:.86rem;color:var(--parch);max-width:700px;line-height:1.5;">
              Per guide approfondite sulle regole, analisi statistiche dei tornei ufficiali, studi empirici sui tassi di estrazione e discussioni sui ruling più complessi, 
              il canale didattico ufficiale della community su Reddit è la migliore risorsa vivente per ogni Illumineer.
            </p>
          </div>
          <a href="https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22" target="_blank" class="btn-reddit">
            <span>Visita r/Lorcana Educational</span> ➔
          </a>
        </div>

        <!-- Visual Symbol Overview -->
        <h3 style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.25rem;margin:30px 0 12px;">🔍 I Simboli Ufficiali delle Rarità Disney Lorcana</h3>
        <p style="font-size:.86rem;color:var(--muted);margin-bottom:14px;">
          Ogni carta reca in basso al centro un simbolo geometrico che ne identifica inconfondibilmente il livello di rarità e collocazione nel pacchetto:
        </p>

        <div style="text-align:center;margin:18px 0;background:rgba(0,0,0,0.3);border-radius:12px;padding:16px;border:1px solid var(--line);">
          <img src="assets/img/lorcana-rarities-symbols.jpg" alt="Lorcana Card Rarities and Symbols" style="max-width:100%;height:auto;border-radius:8px;box-shadow:0 6px 20px rgba(0,0,0,0.5);">
          <div style="font-size:.76rem;color:var(--muted);margin-top:8px;">
            Simboli ufficiali: Cerchio Grigio (Comune), Libro Bianco (Non Comune), Triangolo Bronzo (Rara), Diamante Argento (Super Rara), Ventaglio Arcobaleno (Epica), Pentagono Dorato (Leggendaria), Esagono Arcobaleno (Incantata), Sigillo D23 &amp; 1st League.
          </div>
        </div>

        <!-- Table of Rarities & Frequencies -->
        <div class="symbol-table-wrap">
          <table class="symbol-table">
            <thead>
              <tr>
                <th>Simbolo</th>
                <th>Rarità</th>
                <th>Posizione nel Pack (12 carte)</th>
                <th>Frequenza Stimata (Media Esperita)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>⚪ Cerchio Grigio</strong></td>
                <td>Comune (Common)</td>
                <td>Slot 1 – 6</td>
                <td>Esattamente 6 per bustina (100%)</td>
              </tr>
              <tr>
                <td><strong>📖 Libro Bianco</strong></td>
                <td>Non Comune (Uncommon)</td>
                <td>Slot 7 – 9</td>
                <td>Esattamente 3 per bustina (100%)</td>
              </tr>
              <tr>
                <td><strong>🔺 Triangolo Bronzo</strong></td>
                <td>Rara (Rare)</td>
                <td>Slot 10 – 11</td>
                <td>~1.5 per bustina</td>
              </tr>
              <tr>
                <td><strong>🔷 Diamante Argento</strong></td>
                <td>Super Rara (Super Rare)</td>
                <td>Slot 10 – 11</td>
                <td>1 ogni 2 o 3 bustine (~12-14 per box)</td>
              </tr>
              <tr>
                <td><strong>🪭 Ventaglio Arcobaleno</strong></td>
                <td>Epica (Epic) <i>(Set 9+)</i></td>
                <td>Slot 10 – 11 o Foil (12)</td>
                <td><strong>1 ogni 16 bustine</strong> (~1.5 - 2.5 per box da 24)</td>
              </tr>
              <tr>
                <td><strong>🟡 Pentagono Dorato</strong></td>
                <td>Leggendaria (Legendary)</td>
                <td>Slot 10 – 11</td>
                <td>1 ogni 5 o 6 bustine (~4 - 6 per box)</td>
              </tr>
              <tr>
                <td><strong>✨ Esagono Arcobaleno</strong></td>
                <td>Incantata (Enchanted)</td>
                <td>Slot 12 (Foil)</td>
                <td><strong>1 ogni 96 bustine</strong> (~1 per Sealed Case da 4 Box)</td>
              </tr>
              <tr>
                <td><strong>👑 Sigillo Iconico</strong></td>
                <td>Iconica (Iconic Chase) <i>(Set 13+)</i></td>
                <td>Slot 12 (Foil)</td>
                <td><strong>1 ogni ~384 a 1.500 bustine</strong> (Richiede fino a 15+ case!)</td>
              </tr>
              <tr>
                <td><strong>🌟 Foil Generale</strong></td>
                <td>Qualsiasi Carta Foil</td>
                <td>Slot 12 (Garantito)</td>
                <td>1 carta foil garantita al 100% in ogni bustina</td>
              </tr>
            </tbody>
          </table>
        </div>

        <!-- The 3 Eras Comparison -->
        <h3 style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.25rem;margin:32px 0 12px;">⏳ Come si sono Evolute le Probabilità: Il Confronto Set-by-Set</h3>
        
        <div class="era-grid">
          
          <!-- Classic Era -->
          <div class="era-card">
            <span class="era-badge era-classic">Set 1 – 4 · L'Era Classica</span>
            <h4 style="color:var(--parch);font-size:1.05rem;margin-bottom:8px;">The First Chapter, Rise of the Floodborn, Into the Inklands, Ursula's Return</h4>
            <p style="font-size:.84rem;color:var(--muted);line-height:1.5;">
              <strong>La Matematica:</strong> Ha fissato il gold standard storico: 4-5 Leggendarie per booster box. Le Incantate (Enchanted) erano stimate rigidamente a 1 ogni 96 bustine (1 per Master Case sigillato da 4 box).
            </p>
            <p style="font-size:.84rem;color:var(--parch-muted);margin-top:8px;">
              <strong>Il Vibe:</strong> Estrema linearità e pulizia. Chi apriva un box sapeva esattamente cosa aspettarsi: trovare meno di 4 leggendarie era considerata una giornata sfortunata.
            </p>
          </div>

          <!-- Expansion Era -->
          <div class="era-card">
            <span class="era-badge era-expansion">Set 5 – 8 · L'Era dell'Espansione</span>
            <h4 style="color:var(--parch);font-size:1.05rem;margin-bottom:8px;">Shimmering Skies, Azurite Sea, Archazia's Island, Reign of Chaos</h4>
            <p style="font-size:.84rem;color:var(--muted);line-height:1.5;">
              <strong>La Matematica:</strong> Introduzione dei Luoghi (Locations), che condividono gli slot Rara/Super Rara/Leggendaria con personaggi e oggetti. Il tasso di Leggendarie è rimasto stabile attorno a 5 per box.
            </p>
            <p style="font-size:.84rem;color:var(--parch-muted);margin-top:8px;">
              <strong>Il Fenomeno "Clumping":</strong> La community ha notato una concentrazione maggiore di copie duplicate della medesima Leggendaria nello stesso box rispetto al passato.
            </p>
          </div>

          <!-- Modern Era -->
          <div class="era-card">
            <span class="era-badge era-modern">Set 9+ · L'Era Moderna (Epic &amp; Iconic)</span>
            <h4 style="color:var(--parch);font-size:1.05rem;margin-bottom:8px;">Fables of Light, Wilds Unknown, Attack of the Vine, Hyperia City</h4>
            <p style="font-size:.84rem;color:var(--muted);line-height:1.5;">
              <strong>La Rivoluzione Epica &amp; Iconica:</strong>
              <ul style="padding-left:18px;margin-top:6px;font-size:.84rem;color:var(--parch);">
                <li><strong>Epiche:</strong> compaiono circa 1 volta ogni 16 bustine (~2.5 per box, 100 epiche registrate su 44 box di <em>Attack of the Vine</em>).</li>
                <li><strong>Iconiche:</strong> il nuovo Sacro Graal. Molto più rare delle Incantate, stimate tra 1:384 e 1:1.500 bustine (circa 1 ogni 15+ case).</li>
                <li><strong>Leggendarie Aumentate:</strong> salite fino a 5-6 per box (269 leggendarie su 44 box in <em>Hyperia City</em>) per favorire la reperibilità dei mazzi competitivi nel Gioco Organizzato.</li>
              </ul>
            </p>
          </div>

        </div>

        <!-- God Pack Hierarchy -->
        <h3 style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.25rem;margin:32px 0 12px;">⚡ La Gerarchia dei "God Pack": I Pull dei Tuoi Sogni</h3>
        <p style="font-size:.86rem;color:var(--muted);margin-bottom:14px;">
          Grazie alla struttura a 12 slot di Lorcana, una singola bustina può regalare combinazioni straordinarie:
        </p>

        <div class="godpack-grid">
          
          <div class="godpack-card" style="border-color:#38bdf8;">
            <div style="font-size:.8rem;color:#38bdf8;font-weight:700;text-transform:uppercase;">Livello 1</div>
            <div style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.1rem;margin:4px 0 8px;">The Double Hit</div>
            <p style="font-size:.82rem;color:var(--parch-muted);">
              Sbustare <strong>2 Carte Leggendarie contemporaneamente</strong> negli slot 10 e 11. Accade approssimativamente 1 volta ogni 35 bustine aperte.
            </p>
          </div>

          <div class="godpack-card" style="border-color:#c084fc;">
            <div style="font-size:.8rem;color:#c084fc;font-weight:700;text-transform:uppercase;">Livello 2</div>
            <div style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.1rem;margin:4px 0 8px;">The Triple Hit</div>
            <p style="font-size:.82rem;color:var(--parch-muted);">
              Sbustare <strong>2 Leggendarie regolari</strong> (slot 10-11) <strong>PIÙ una Leggendaria Foil</strong> nello slot 12. Un evento memorabile che ripaga l'intero costo della bustina.
            </p>
          </div>

          <div class="godpack-card" style="border-color:#facc15;background:linear-gradient(145deg, rgba(234, 179, 8, .15), rgba(13, 10, 20, 0.9));">
            <div style="font-size:.8rem;color:#facc15;font-weight:700;text-transform:uppercase;">Livello 3 · Apex</div>
            <div style="font-family:'Cinzel',serif;color:#fef08a;font-size:1.1rem;margin:4px 0 8px;">The Ultimate Pull</div>
            <p style="font-size:.82rem;color:var(--parch);">
              Sbustare <strong>2 Leggendarie</strong> negli slot 10-11 e una carta <strong>Iconica o Incantata</strong> nello slot 12 Foil. Dal Set 9+ è l'evento di unboxing più raro in assoluto!
            </p>
          </div>

        </div>

        <!-- Factory Balancing vs Loose Packs -->
        <h3 style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.25rem;margin:32px 0 12px;">⚖️ Booster Box Sigillati vs Bustine Sfuse: Come Funziona il Confezionamento</h3>
        <div style="background:var(--surface-2);border:1px solid var(--line);border-radius:12px;padding:20px;font-size:.86rem;color:var(--parch-muted);line-height:1.6;">
          <ul style="padding-left:20px;display:flex;flex-direction:column;gap:10px;">
            <li>
              <strong style="color:var(--gold);">1. Booster Box Sigillato (24 Bustine):</strong>
              È il metodo d'acquisto più sicuro e controllato. I box sono bilanciati in fase di imbustamento industriale: troverai quasi certamente <strong>almeno 12 Super Rare</strong>, <strong>tra 4 e 6 Leggendarie</strong> e <strong>1-2 Epiche</strong> nei set moderni. La probabilità di trovare una carta Incantata in un singolo box è di circa il <strong>25%</strong> (1 su 4 box).
            </li>
            <li>
              <strong style="color:var(--gold);">2. Illumineer's Trove (8 Bustine):</strong>
              Rappresenta il test supremo della sorte. Con sole 8 bustine, il bilanciamento di fabbrica non interviene: puoi imbatterti in un <em>"God Trove"</em> con 2 Leggendarie e un'Incantata, oppure aprire 8 bustine con solo Rare.
            </li>
            <li>
              <strong style="color:var(--gold);">3. Blister Sleeved (Bustine Singole):</strong>
              Sono bustine con involucro esterno protettivo, distribuite in modo indipendente. Non sono legate alla sequenza di un singolo box: per questo il rischio è alto, ma è anche l'unico modo con cui un acquirente casuale può sbustare 2 Incantate con soli 3 o 4 pacchetti.
            </li>
          </ul>
        </div>

      </div>
    </div>"""

    if 'id="view-products"' in html and 'id="view-guide"' not in html:
        html = html.replace('    <!-- 3. PRODUCTS CATALOG VIEW -->', view_guide_html + '\n\n    <!-- 3. PRODUCTS CATALOG VIEW -->')

    # 5. Add openCustomPacks in Javascript
    custom_pack_js = """    function openCustomPacks() {
      const inp = document.getElementById('customPackCount');
      let count = parseInt(inp.value, 10);
      if (isNaN(count) || count < 1) count = 1;
      if (count > 10000) count = 10000;
      inp.value = count;
      openPacks(count);
    }
"""

    if 'function openCustomPacks()' not in html:
        html = html.replace('    function openPacks(n) {', custom_pack_js + '\n    function openPacks(n) {')

    # 6. Update switchVaultTab in Javascript
    old_switch = "const views = ['simulator', 'probability', 'products', 'challenges'];"
    new_switch = "const views = ['simulator', 'probability', 'guide', 'products', 'challenges'];"
    if old_switch in html:
        html = html.replace(old_switch, new_switch)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("collector-vault.html successfully upgraded!")

def update_docs():
    # Update Italian doc
    doc_it_path = "docs/cards-and-rarities/pull-rates-and-products.it.md"
    new_doc_it = """# Guida Completa ai Pull Rate, Rarità, Evoluzione delle Ere e Catalogo Prodotti

> ⚠️ **AVVERTENZA STATISTICA & PULL RATE SPERIMENTALI:**
> Disney Lorcana™ e i relativi marchi e personaggi sono copyright di Disney e Ravensburger.
> **Ravensburger non pubblica quote o percentuali ufficiali di estrazione delle carte.**
> Tutte le probabilità, i tassi e i calcoli riportati in questo documento sono stime sperimentali elaborate dalla community globale (studi empirici su oltre 44 booster box documentati da *The Gamers Lodge* e discussioni su *Reddit r/Lorcana*) e modelli matematici di distribuzione binomiale. Le aperture reali in negozio o blister possono variare per la naturale varianza casuale.

---

## 1. Risorsa Didattica Consigliata: Reddit r/Lorcana (Educational)
Per approfondire ruling complessi, analisi statistiche aggiornate sui tornei e discussioni aperte della community, consigliamo caldamente:
👉 [**Reddit r/Lorcana — Flair Educational**](https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22)

---

## 2. Anatomia del Pacchetto e Simboli Ufficiali delle Rarità

Ogni bustina standard contiene **12 carte** divise in slot precisi:
- **Slot 1 – 6 (6 Carte):** Comuni garantite.
- **Slot 7 – 9 (3 Carte):** Non Comuni garantite.
- **Slot 10 – 11 (2 Carte):** Rara, Super Rara, Epica (dal Set 9+) o Leggendaria.
- **Slot 12 (1 Carta Foil Garantita):** Qualsiasi carta del set in versione laminata foil, con possibilità di estrarre **Incantate (Enchanted)** o **Iconiche (Iconic)**.

| Simbolo Geometrico | Rarità | Slot nel Pack | Frequenza Media Stimata |
| :--- | :--- | :--- | :--- |
| **⚪ Cerchio Grigio** | Comune (Common) | 1 – 6 | 6 per bustina (100%) |
| **📖 Libro Bianco** | Non Comune (Uncommon) | 7 – 9 | 3 per bustina (100%) |
| **🔺 Triangolo Bronzo** | Rara (Rare) | 10 – 11 | ~1.5 per bustina |
| **🔷 Diamante Argento** | Super Rara (Super Rare) | 10 – 11 | 1 ogni 2 o 3 bustine (~12-14 per box) |
| **🪭 Ventaglio Arcobaleno** | Epica (Epic) *(Set 9+)* | 10 – 11 o Foil (12) | **1 ogni 16 bustine** (~1.5 - 2.5 per box) |
| **🟡 Pentagono Dorato** | Leggendaria (Legendary) | 10 – 11 | 1 ogni 5 o 6 bustine (~4 - 6 per box) |
| **✨ Esagono Arcobaleno** | Incantata (Enchanted) | 12 (Foil) | **1 ogni 96 bustine** (~1 per Master Case da 4 box) |
| **👑 Sigillo Iconico** | Iconica (Iconic Chase) *(Set 13+)* | 12 (Foil) | **1 ogni ~384 a 1.500 bustine** (Spesso richiede 15+ case) |

---

## 3. Confronto Set-by-Set: L'Evoluzione delle Probabilità nelle 3 Ere

### 🏛️ 1. L'Era Classica (Set 1–4)
*Set: The First Chapter, Rise of the Floodborn, Into the Inklands, Ursula's Return.*
- **La Matematica:** Gold standard: 4-5 Leggendarie per box. Incantate rigorosamente a 1 ogni 96 bustine (1 per sealed case da 4 box).
- **Il Vibe:** Semplice e lineare. Meno di 4 leggendarie in un box era un'anomalia statistica negativa.

### 🌿 2. L'Era dell'Espansione (Set 5–8)
*Set: Shimmering Skies, Azurite Sea, Archazia's Island, Reign of Chaos.*
- **La Matematica:** Ha introdotto i Luoghi (Locations), che condividono gli slot Rara/Super Rara/Leggendaria con personaggi e oggetti. Il tasso è rimasto costante a ~5 Leggendarie per box.
- **Nota di Clumping:** I collezionisti hanno riscontrato frequenti duplicati della stessa Leggendaria nel medesimo box rispetto ai primi set.

### 👑 3. L'Era Moderna (Set 9+)
*Set: Fables of Light, Wilds Unknown, Attack of the Vine, Hyperia City e successivi.*
- **Carte Epiche (🟣):** Compaiono circa 1 volta ogni 16 bustine (~2.5 per box, ben 100 epiche registrate su 44 box di *Attack of the Vine*).
- **Carte Iconiche (👑):** Il nuovo "sacro graal". Molto più rare delle Incantate, stimate tra 1:384 e 1:1.500 bustine (spesso richiedono 15+ case per essere trovate).
- **Leggendarie Aumentate:** Per incentivare il gioco competitivo e rendere i playset più accessibili, le Leggendarie non-foil sono aumentate fino a 5.5 - 6 per box (269 Leggendarie aperte su 44 box in *Hyperia City*).
- **Incantate Stabili:** Mantenute su ~1 ogni 96 bustine (aperte tra 11 e 15 Incantate nei test su 44 box).

---

## 4. La Gerarchia dei "God Pack"

Grazie al sistema di slot separati di Lorcana, una bustina può regalare combinazioni straordinarie:
1. **The Double Hit:** 2 Leggendarie negli slot 10 e 11 (accade circa 1 volta ogni 35 bustine).
2. **The Triple Hit:** 2 Leggendarie regolari + 1 Leggendaria Foil nello slot 12.
3. **The Ultimate Pull:** 2 Leggendarie (slot 10-11) + 1 Iconica o Incantata nello slot 12 Foil!

---

## 5. Box Sigillati vs Troves vs Bustine Sfuse

- **Booster Box Sigillato (24 Bustine):** Confezionamento bilanciato in fabbrica. Troverai con certezza quasi assoluta almeno 12 Super Rare, 4-6 Leggendarie, 1-2 Epiche e ~25% di probabilità di contenere un'Incantata.
- **Illumineer's Trove (8 Bustine):** Nessun bilanciamento industriale su 8 pacchetti. Può essere un *God Trove* o non contenere alcuna Leggendaria.
- **Blister Sleeves (Bustine Singole):** Estrazioni puramente indipendenti. Rischio più elevato di bustine "a vuoto", ma unico modo per sbustare più Incantate su una manciata di pacchetti casuali.

---

## 6. Catalogo Prodotti Ufficiali Disney Lorcana

- **Booster Display Box (24 Bustine):** 288 carte totali, perfetto per draft e collezionismo.
- **Illumineer's Trove:** 8 bustine, 6 dadi contadanni in resina metallizzata, 1 rotella lore e 6 divisori tematici.
- **Starter Decks:** Mazzi completi da 60 carte con 1 bustina aggiuntiva e segnalini.
- **Illumineer's Quest (Deep Trouble):** Modalità cooperativa/solitaria con mazzo boss Ursula automatico.
- **App Ufficiale Companion:** Disponibile su iOS e Android con tracciamento della collezione e scansione.
"""
    with open(doc_it_path, "w", encoding="utf-8") as f:
        f.write(new_doc_it)
    print("docs IT updated!")

    # Update English doc
    doc_en_path = "docs/cards-and-rarities/pull-rates-and-products.en.md"
    new_doc_en = """# Complete Guide to Pull Rates, Rarities, Eras Evolution & Sealed Products

> ⚠️ **STATISTICAL NOTICE & EXPERIMENTAL PULL RATES:**
> Disney Lorcana™ and all associated marks and images are copyright of Disney and Ravensburger.
> **Ravensburger does not publish official pull rates or drop probabilities.**
> All odds, frequencies, and pull rates in this guide are experimental community estimates (aggregated from mass unboxings of 44+ booster boxes by *The Gamers Lodge* and community research on *Reddit r/Lorcana*) combined with binomial distribution modeling. Actual unboxings may vary due to random variance.

---

## 1. Recommended Educational Resource: Reddit r/Lorcana (Educational)
For in-depth rulings, tournament breakdown stats, and mass unboxing studies, visit:
👉 [**Reddit r/Lorcana — Educational Flair**](https://www.reddit.com/r/Lorcana/?f=flair_name%3A%22Educational%22)

---

## 2. Pack Anatomy & Official Rarity Symbols

Each booster pack contains **12 cards**:
- **Slots 1 – 6 (6 Cards):** Guaranteed Commons.
- **Slots 7 – 9 (3 Cards):** Guaranteed Uncommons.
- **Slots 10 – 11 (2 Cards):** Rare, Super Rare, Epic (Set 9+) or Legendary.
- **Slot 12 (1 Guaranteed Foil Card):** Any card from the set in foil, with chances for **Enchanted** or **Iconic** chase cards.

| Geometric Symbol | Rarity | Pack Slot | Estimated Frequency |
| :--- | :--- | :--- | :--- |
| **⚪ Gray Circle** | Common | Slots 1 – 6 | 6 in every pack (100%) |
| **📖 White Book** | Uncommon | Slots 7 – 9 | 3 in every pack (100%) |
| **🔺 Bronze Triangle** | Rare | Slots 10 – 11 | ~1.5 per pack |
| **🔷 Silver Diamond** | Super Rare | Slots 10 – 11 | 1 in every 2 to 3 packs (~12-14 per box) |
| **🪭 Rainbow Fan** | Epic *(Set 9+)* | Slots 10 – 11 or Foil (12) | **1 in every 16 packs** (~1.5 - 2.5 per box) |
| **🟡 Gold Pentagon** | Legendary | Slots 10 – 11 | 1 in every 5 to 6 packs (~4 - 6 per box) |
| **✨ Rainbow Hex** | Enchanted | Slot 12 (Foil) | **1 in every 96 packs** (~1 per 4-box Case) |
| **👑 Iconic Seal** | Iconic Chase *(Set 13+)* | Slot 12 (Foil) | **1 in ~384 to 1,500 packs** (Requires up to 15+ cases) |

---

## 3. Set-by-Set Evolution: How Odds Evolved Across 3 Eras

### 🏛️ 1. The Classic Era (Sets 1–4)
*Sets: The First Chapter, Rise of the Floodborn, Into the Inklands, Ursula's Return.*
- **The Math:** 4 to 5 Legendaries per box. Enchanteds strictly 1 per 96 packs (1 per sealed case of 4 boxes).
- **The Vibe:** Clean and predictable. Less than 4 Legendaries in a box was an outlier.

### 🌿 2. The Expansion Era (Sets 5–8)
*Sets: Shimmering Skies, Azurite Sea, Archazia's Island, Reign of Chaos.*
- **The Math:** Introduced Locations sharing Rare+ slots. Rates remained steady at ~5 Legendaries per box.
- **Clumping Note:** Players noticed frequent duplicate copies of the same Legendary within the same box.

### 👑 3. The Modern Era (Set 9+)
*Sets: Fables of Light, Wilds Unknown, Attack of the Vine, Hyperia City.*
- **Epic Cards (🟣):** Show up roughly 1 in every 16 packs (~2.5 per box, ~100 epics in 44 boxes of *Attack of the Vine*).
- **Iconic Cards (👑):** The ultimate chase tier. Far rarer than Enchanteds, estimated between 1:384 and 1:1,500 packs.
- **Increased Legendaries:** Increased to 5.5 - 6 per box (269 Legendaries in 44 boxes of *Hyperia City*) to improve player accessibility.
- **Enchanted Stability:** Consistent at ~1 per 96 packs (11 to 15 pulled across 44 boxes).

---

## 4. The Hierarchy of "God Packs"

1. **The Double Hit:** Pulling two Legendaries in slots 10 and 11 (~1 in 35 packs).
2. **The Triple Hit:** Pulling two Legendaries AND a foil Legendary in slot 12.
3. **The Ultimate Pull:** Pulling two Legendaries (slots 10-11) AND an Iconic or Enchanted in slot 12!

---

## 5. Factory Sealed Boxes vs Loose Packs & Troves

- **Booster Box (24 Packs):** Factory balanced (guaranteed ~12+ Super Rares, 4-6 Legendaries, 1-2 Epics, ~25% Enchanted chance).
- **Illumineer's Trove (8 Packs):** Pure luck test; no box balancing applies.
- **Blister Sleeves (Loose Packs):** Independent random rolls from master shipments.
"""
    with open(doc_en_path, "w", encoding="utf-8") as f:
        f.write(new_doc_en)
    print("docs EN updated!")

if __name__ == "__main__":
    copy_assets()
    upgrade_collector_vault()
    update_docs()
