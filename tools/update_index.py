import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

target = '    <!-- Core Features & Documentation -->'
replacement = '''    <!-- NEW: Interactive Apps Showcase (Deck Lab & Collector's Vault) -->
    <section style="margin-bottom:70px;">
      <h2 class="section-title">✨ Community Web Apps &amp; Tabletop Simulators</h2>
      <p class="section-desc">Interactive tools built for deck building, goldfish playtesting, booster pack opening, and collecting.</p>

      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(360px, 1fr));gap:24px;">
        <!-- Deck Lab Card -->
        <div style="background:linear-gradient(145deg, rgba(229,185,92,0.12), var(--bg-card));border:1.5px solid var(--gold);border-radius:18px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 10px 30px rgba(0,0,0,0.4);">
          <div>
            <div style="font-size:2.6rem;margin-bottom:12px;">🃏</div>
            <h3 style="font-family:'Cinzel',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;">Deck Lab &amp; Playtester</h3>
            <p style="color:var(--parch-muted);font-size:0.95rem;margin-bottom:18px;">
              Costruisci e perfeziona il tuo mazzo da 60 carte con catalogo carte integrato, visualizzatore della curva d'inchiostro, test della mano iniziale con mulligan realistico e simulatore goldfish dei primi turni. Esporta con 1 click per <strong>duels.ink</strong>, <strong>inktable.net</strong> e <strong>dreamborn.ink</strong>!
            </p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px;">
              <span class="feat-tag">🛠️ 60-Card Builder</span>
              <span class="feat-tag">📊 Curva d'Inchiostro Live</span>
              <span class="feat-tag">🎲 Goldfish Playtester</span>
              <span class="feat-tag">📤 Export Duels.ink</span>
            </div>
          </div>
          <a href="deck-lab.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;">Lancia Deck Lab &amp; Playtester ➔</a>
        </div>

        <!-- Collector's Vault Card -->
        <div style="background:linear-gradient(145deg, rgba(244,114,182,0.12), var(--bg-card));border:1.5px solid #f472b6;border-radius:18px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 10px 30px rgba(0,0,0,0.4);">
          <div>
            <div style="font-size:2.6rem;margin-bottom:12px;">💎</div>
            <h3 style="font-family:'Cinzel',serif;font-size:1.6rem;color:var(--gold);margin-bottom:10px;">Collector's Vault &amp; Pulls</h3>
            <p style="color:var(--parch-muted);font-size:0.95rem;margin-bottom:18px;">
              Simula l'apertura realistica di 1 bustina, 10 bustine, 1 Trove (8 pack), 1 Booster Box (24 pack) o un intero Case (96 pack). Calcola con precisione binomiale le probabilità di trovare carte Incantate per ogni set, consulta il catalogo prodotti e genera sfide casuali con moneta 3D.
            </p>
            <div style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:24px;">
              <span class="feat-tag">🎴 Pack Simulator</span>
              <span class="feat-tag">✨ Incantate (1:80)</span>
              <span class="feat-tag">📦 Catalogo Prodotti</span>
              <span class="feat-tag">🪙 Coin Flip Decider</span>
            </div>
          </div>
          <a href="collector-vault.html" class="btn-open" style="text-align:center;font-size:1.05rem;padding:12px 20px;border-color:#f472b6;color:#ff80bf;">Apri Collector's Vault ➔</a>
        </div>
      </div>
    </section>

    <!-- Core Features & Documentation -->'''

if target in text:
    text = text.replace(target, replacement, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Updated index.html successfully!")
else:
    print("Target not found!")
