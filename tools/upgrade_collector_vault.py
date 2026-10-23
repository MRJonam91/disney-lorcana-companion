import re

with open('collector-vault.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Include data/lorcana-cards.js before the main script
if '<script src="data/lorcana-cards.js"></script>' not in text:
    text = text.replace('  <script>', '  <script src="data/lorcana-cards.js"></script>\n  <script>')

# 2. Add Epic and Iconic CSS rules
epic_iconic_css = """
    :root {
      --epic: #a855f7;
      --iconic: #38bdf8;
    }
    .pulled-card.rarity-Epic {
      border-color: var(--epic);
      background: linear-gradient(145deg, rgba(168, 85, 247, 0.22), var(--surface-2));
      box-shadow: 0 0 24px rgba(168, 85, 247, 0.5);
    }
    .pulled-card.rarity-Iconic {
      border: 2px solid #ffd700;
      background: radial-gradient(circle at 50% 0%, rgba(56, 189, 248, 0.35) 0%, rgba(244, 114, 182, 0.25) 50%, var(--surface-2) 100%);
      box-shadow: 0 0 35px rgba(255, 215, 0, 0.8), 0 0 15px rgba(56, 189, 248, 0.6);
      animation: iconicPulse 1.8s infinite alternate;
    }
    @keyframes iconicPulse {
      from { transform: scale(1); box-shadow: 0 0 25px rgba(255, 215, 0, 0.7); }
      to { transform: scale(1.04); box-shadow: 0 0 45px rgba(56, 189, 248, 0.9), 0 0 20px #ffd700; }
    }
    .pulled-iconic-badge {
      position: absolute;
      top: 6px;
      left: 6px;
      font-size: .65rem;
      background: linear-gradient(90deg, #ffd700, #38bdf8);
      color: #0b0913;
      font-weight: 900;
      padding: 2px 7px;
      border-radius: 99px;
      letter-spacing: .05em;
    }
"""

if '.pulled-card.rarity-Epic' not in text:
    text = text.replace('    /* Probability Calculator Section */', epic_iconic_css + '\n    /* Probability Calculator Section */')

# 3. Update the selectSet options to include all 14 sets
all_sets_options = """          <select class="select-set" id="selectSimSet" onchange="changeSet()">
            <option value="set14">Set 14: Hyperia City (New Release · Epic &amp; Iconic)</option>
            <option value="set13" selected>Set 13: Attack of the Vine! (Current · Epic &amp; Iconic)</option>
            <option value="set12">Set 12: Wilds Unknown (Epic &amp; Iconic)</option>
            <option value="set11">Set 11: Sunken Realms (Epic &amp; Iconic)</option>
            <option value="set10">Set 10: Whispers of the Deep (Epic &amp; Iconic)</option>
            <option value="set9">Set 9: Fables of Light (Epic &amp; Iconic Debut)</option>
            <option value="set8">Set 8: Reign of Chaos</option>
            <option value="set7">Set 7: Archazia's Island</option>
            <option value="set6">Set 6: Azurite Sea</option>
            <option value="set5">Set 5: Shimmering Skies</option>
            <option value="set4">Set 4: Ursula's Return</option>
            <option value="set3">Set 3: Into the Inklands</option>
            <option value="set2">Set 2: Rise of the Floodborn</option>
            <option value="set1">Set 1: The First Chapter</option>
          </select>"""

text = re.sub(r'<select class="select-set" id="selectSimSet"[^>]*>.*?</select>', lambda m: all_sets_options, text, flags=re.DOTALL)

# 4. Update the summary counters bar to include Epic & Iconic
counters_bar = """        <!-- Pull Summary Bar -->
        <div class="pull-stats-grid">
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntPacks" style="color:var(--parch);">0</div>
            <div class="pull-stat-lbl">Bustine</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntCommon" style="color:var(--common);">0</div>
            <div class="pull-stat-lbl">Comuni</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntUncommon" style="color:var(--uncommon);">0</div>
            <div class="pull-stat-lbl">Non Comuni</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntRare" style="color:var(--rare);">0</div>
            <div class="pull-stat-lbl">Rare</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntSuperRare" style="color:var(--super-rare);">0</div>
            <div class="pull-stat-lbl">Super Rare</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntLegendary" style="color:var(--legendary);">0</div>
            <div class="pull-stat-lbl">Leggendarie</div>
          </div>
          <div class="pull-stat-box" style="border-color:var(--epic);background:rgba(168,85,247,0.12);">
            <div class="pull-stat-val" id="cntEpic" style="color:var(--epic);">0</div>
            <div class="pull-stat-lbl">Epiche 🟣</div>
          </div>
          <div class="pull-stat-box" style="border-color:var(--enchanted);background:rgba(244,114,182,0.12);">
            <div class="pull-stat-val" id="cntEnchanted" style="color:var(--enchanted);">0</div>
            <div class="pull-stat-lbl">Incantate ✨</div>
          </div>
          <div class="pull-stat-box" style="border-color:#38bdf8;background:rgba(56,189,248,0.14);">
            <div class="pull-stat-val" id="cntIconic" style="color:#38bdf8;">0</div>
            <div class="pull-stat-lbl">Iconiche 👑</div>
          </div>
          <div class="pull-stat-box">
            <div class="pull-stat-val" id="cntFoils" style="color:var(--gold-soft);">0</div>
            <div class="pull-stat-lbl">Foil Totali</div>
          </div>
        </div>"""

text = re.sub(r'<!-- Pull Summary Bar -->.*?<!-- Cards Container -->', lambda m: counters_bar + '\n\n        <!-- Cards Container -->', text, flags=re.DOTALL)

# 5. Add Official App Banner in Products View
app_card_products = """
      <!-- Official App Banner in Products Tab -->
      <div style="margin-top:24px;background:linear-gradient(145deg, rgba(59,126,194,0.15), var(--surface));border:1.5px solid var(--sapphire);border-radius:14px;padding:24px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:20px;">
        <div style="max-width:720px;">
          <h3 style="font-family:'Cinzel',serif;color:var(--gold);font-size:1.3rem;margin-bottom:8px;">📱 App Ufficiale per Collezionisti: Disney Lorcana TCG Companion</h3>
          <p style="font-size:.88rem;color:var(--parch-muted);margin-bottom:14px;">
            Sviluppata direttamente da Ravensburger per iOS e Android. Permette di tenere traccia dell'intera collezione, catalogare le varianti foil, visualizzare le carte in 3D con effetto olografico sensibile al movimento, creare la tua wishlist e consultare il ruling ufficiale.
          </p>
          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="https://apps.apple.com/app/disney-lorcana-tcg-companion/id6448270106" target="_blank" class="btn-pack" style="border-color:#93c5fd;color:#93c5fd;font-size:.82rem;">
              🍎 Scarica su App Store ➔
            </a>
            <a href="https://play.google.com/store/apps/details?id=com.ravensburger.disneylorcana" target="_blank" class="btn-pack" style="border-color:#4ade80;color:#4ade80;font-size:.82rem;">
              🤖 Scarica su Google Play Store ➔
            </a>
          </div>
        </div>
        <div style="font-size:3.5rem;">📲✨</div>
      </div>
"""

if '<!-- Official App Banner in Products Tab -->' not in text:
    text = text.replace('        </div>\n      </div>\n    </div>\n\n    <!-- 4. CHALLENGES & DECIDER VIEW -->', '        </div>\n' + app_card_products + '      </div>\n    </div>\n\n    <!-- 4. CHALLENGES & DECIDER VIEW -->')

# 6. Update the JavaScript simulator logic for Epic and Iconic
js_sim_updated = """
    let simStats = {
      packs: 0,
      Common: 0,
      Uncommon: 0,
      Rare: 0,
      'Super Rare': 0,
      Legendary: 0,
      Epic: 0,
      Enchanted: 0,
      Iconic: 0,
      foils: 0
    };

    function openPacks(n) {
      const grid = document.getElementById('pulledCardsGrid');
      grid.innerHTML = '';
      const pulled = [];

      const currentSetId = document.getElementById('selectSimSet').value;
      const setMeta = (window.LORCANA_SETS_DB || []).find(s => s.id === currentSetId) || { has_epic: true, has_iconic: true, cards: [] };

      for (let p = 0; p < n; p++) {
        simStats.packs++;

        // 6 Commons
        for (let i = 0; i < 6; i++) {
          simStats.Common++;
          pulled.push(getSampleCard('Common', setMeta, false));
        }

        // 3 Uncommons
        for (let i = 0; i < 3; i++) {
          simStats.Uncommon++;
          pulled.push(getSampleCard('Uncommon', setMeta, false));
        }

        // 2 Rare+ Slots
        for (let i = 0; i < 2; i++) {
          const roll = Math.random();
          let r = 'Rare';
          if (setMeta.has_epic && roll < 0.04) {
            r = 'Epic';
            simStats.Epic++;
          } else if (roll < 0.16) {
            r = 'Legendary';
            simStats.Legendary++;
          } else if (roll < 0.46) {
            r = 'Super Rare';
            simStats['Super Rare']++;
          } else {
            simStats.Rare++;
          }
          pulled.push(getSampleCard(r, setMeta, false));
        }

        // 1 Foil Slot (100% Guaranteed Foil)
        simStats.foils++;
        const foilRoll = Math.random();
        let foilRarity = 'Common';

        // Iconic (1:240 packs in sets that feature them)
        if (setMeta.has_iconic && foilRoll < 0.0042) {
          foilRarity = 'Iconic';
          simStats.Iconic++;
        }
        // Enchanted (1:80 packs)
        else if (foilRoll < 0.0125) {
          foilRarity = 'Enchanted';
          simStats.Enchanted++;
        }
        // Epic (1:48 packs in modern sets)
        else if (setMeta.has_epic && foilRoll < 0.033) {
          foilRarity = 'Epic';
          simStats.Epic++;
        }
        else if (foilRoll < 0.08) {
          foilRarity = 'Legendary';
          simStats.Legendary++;
        }
        else if (foilRoll < 0.22) {
          foilRarity = 'Super Rare';
          simStats['Super Rare']++;
        }
        else if (foilRoll < 0.52) {
          foilRarity = 'Rare';
          simStats.Rare++;
        }
        else if (foilRoll < 0.78) {
          foilRarity = 'Uncommon';
          simStats.Uncommon++;
        }
        else {
          simStats.Common++;
        }

        pulled.push(getSampleCard(foilRarity, setMeta, true));
      }

      updateStatsUI();

      // Display up to 48 cards to keep DOM snappy
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
      });
    }

    function getSampleCard(rarity, setMeta, isFoil) {
      const inSet = (setMeta.cards || []).filter(c => c.rarity === rarity);
      if (inSet.length > 0) {
        const picked = inSet[Math.floor(Math.random() * inSet.length)];
        return { name: `${picked.name} - ${picked.sub}`, rarity: rarity, foil: isFoil };
      }
      const generic = (CARD_SAMPLES[rarity] || CARD_SAMPLES.Common);
      return { name: generic[Math.floor(Math.random() * generic.length)], rarity: rarity, foil: isFoil };
    }

    function getRarityIcon(rarity) {
      switch(rarity) {
        case 'Common': return '⚪';
        case 'Uncommon': return '📖';
        case 'Rare': return '🔺';
        case 'Super Rare': return '🔷';
        case 'Legendary': return '⬟';
        case 'Epic': return '🟣';
        case 'Enchanted': return '✨';
        case 'Iconic': return '👑';
        default: return '✦';
      }
    }

    function updateStatsUI() {
      document.getElementById('cntPacks').innerText = simStats.packs;
      document.getElementById('cntCommon').innerText = simStats.Common;
      document.getElementById('cntUncommon').innerText = simStats.Uncommon;
      document.getElementById('cntRare').innerText = simStats.Rare;
      document.getElementById('cntSuperRare').innerText = simStats['Super Rare'];
      document.getElementById('cntLegendary').innerText = simStats.Legendary;
      if (document.getElementById('cntEpic')) document.getElementById('cntEpic').innerText = simStats.Epic;
      if (document.getElementById('cntEnchanted')) document.getElementById('cntEnchanted').innerText = simStats.Enchanted;
      if (document.getElementById('cntIconic')) document.getElementById('cntIconic').innerText = simStats.Iconic;
      document.getElementById('cntFoils').innerText = simStats.foils;
    }

    function resetPullStats() {
      simStats = { packs: 0, Common: 0, Uncommon: 0, Rare: 0, 'Super Rare': 0, Legendary: 0, Epic: 0, Enchanted: 0, Iconic: 0, foils: 0 };
      updateStatsUI();
      document.getElementById('pulledCardsGrid').innerHTML = `
        <div style="grid-column: 1 / -1; text-align:center; padding: 40px; color:var(--muted);">
          Contatore azzerato. Apri nuove bustine!
        </div>
      `;
    }
"""

text = re.sub(r'let simStats = \{.*?\n    function resetPullStats\(\) \{.*?\n    \}', lambda m: js_sim_updated.strip(), text, flags=re.DOTALL)

with open('collector-vault.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Upgraded collector-vault.html successfully!")
