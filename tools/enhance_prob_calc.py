with open("collector-vault.html", "r", encoding="utf-8") as f:
    html = f.read()

old_prob_grid = """        <!-- Expected Values Grid -->
        <div class="expectancy-grid">
          <div class="exp-card">
            <div class="exp-title">Probabilità Incantata (Enchanted)</div>
            <div class="exp-value" id="expEnchantedProb" style="color:var(--enchanted);">26.1%</div>
            <div class="exp-sub">Chance di trovare <b>almeno 1</b> carta Incantata su <span class="exp-pack-n">24</span> bustine (tasso 1:80).</div>
          </div>

          <div class="exp-card">
            <div class="exp-title">Leggendarie Attese (Media)</div>
            <div class="exp-value" id="expLegendary" style="color:var(--legendary);">3.6 - 4.2</div>
            <div class="exp-sub">Circa 1 Leggendaria ogni 6-7 bustine aperte.</div>
          </div>

          <div class="exp-card">
            <div class="exp-title">Super Rare Attese (Media)</div>
            <div class="exp-value" id="expSuperRare" style="color:var(--super-rare);">12.0 - 14.5</div>
            <div class="exp-sub">Circa 1 Super Rara ogni 3-4 bustine.</div>
          </div>

          <div class="exp-card">
            <div class="exp-title">Carte Foil Garantite</div>
            <div class="exp-value" id="expFoils" style="color:var(--gold-soft);">24</div>
            <div class="exp-sub">1 carta foil garantita al 100% in ogni bustina.</div>
          </div>
        </div>"""

new_prob_grid = """        <!-- Expected Values Grid (6-Card Telemetry incl. Epic & Iconic) -->
        <div class="expectancy-grid" style="grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));">
          <div class="exp-card foil-card-fx" style="border-color:rgba(244,114,182,0.5);">
            <div class="exp-title">✨ Probabilità Incantata (Enchanted)</div>
            <div class="exp-value" id="expEnchantedProb" style="color:var(--enchanted);">22.2%</div>
            <div class="exp-sub">Chance di trovare <b>almeno 1</b> Incantata su <span class="exp-pack-n">24</span> bustine (tasso 1:96).</div>
          </div>

          <div class="exp-card foil-card-fx" style="border-color:rgba(250,204,21,0.55);">
            <div class="exp-title">👑 Probabilità Iconica (Iconic Set 9+)</div>
            <div class="exp-value" id="expIconicProb" style="color:#fde047;">6.1%</div>
            <div class="exp-sub">Chance di trovare <b>almeno 1</b> Iconica su <span class="exp-pack-n">24</span> bustine (tasso ~1:384).</div>
          </div>

          <div class="exp-card foil-card-fx" style="border-color:rgba(168,85,247,0.5);">
            <div class="exp-title">🟣 Epiche Attese (Set 9+)</div>
            <div class="exp-value" id="expEpic" style="color:var(--epic);">1.2 - 1.8</div>
            <div class="exp-sub">Circa 1 carta Epica ogni 16 bustine (~1.5 - 2.5 per box).</div>
          </div>

          <div class="exp-card foil-card-fx">
            <div class="exp-title">🟡 Leggendarie Attese (Media)</div>
            <div class="exp-value" id="expLegendary" style="color:var(--legendary);">4.0 - 5.2</div>
            <div class="exp-sub">Circa 1 Leggendaria ogni 5-6 bustine aperte.</div>
          </div>

          <div class="exp-card foil-card-fx">
            <div class="exp-title">🔷 Super Rare Attese (Media)</div>
            <div class="exp-value" id="expSuperRare" style="color:var(--super-rare);">11.5 - 14.0</div>
            <div class="exp-sub">Circa 1 Super Rara ogni 2-3 bustine.</div>
          </div>

          <div class="exp-card foil-card-fx">
            <div class="exp-title">🌟 Carte Foil Garantite</div>
            <div class="exp-value" id="expFoils" style="color:var(--gold-soft);">24</div>
            <div class="exp-sub">1 carta foil garantita al 100% in ogni bustina (Slot 12).</div>
          </div>
        </div>"""

if old_prob_grid in html:
    html = html.replace(old_prob_grid, new_prob_grid)

# Increase slider max to 240 packs (2.5 Cases)
html = html.replace('min="1" max="100" value="24"', 'min="1" max="240" value="24"')
html = html.replace('100 (Più di un Case)', '240 (10 Booster Box)')

old_prob_js = """    // PROBABILITY CALCULATOR
    function updateProbabilityCalc(n) {
      n = parseInt(n);
      document.getElementById('sliderVal').innerText = n;
      document.querySelectorAll('.exp-pack-n').forEach(el => el.innerText = n);

      // Prob of at least 1 enchanted: 1 - (1 - 1/80)^n
      const pEnchanted = (1 - Math.pow(1 - 1/80, n)) * 100;
      document.getElementById('expEnchantedProb').innerText = pEnchanted.toFixed(1) + '%';

      // Legendary expectancy: ~0.16 per pack in rare slot * 2 = 0.32 + foil chance 0.03 = ~0.17 per pack
      const legMin = (n * 0.15).toFixed(1);
      const legMax = (n * 0.18).toFixed(1);
      document.getElementById('expLegendary').innerText = `${legMin} - ${legMax}`;

      // Super rare expectancy: ~0.55 per pack
      const srMin = (n * 0.5).toFixed(1);
      const srMax = (n * 0.6).toFixed(1);
      document.getElementById('expSuperRare').innerText = `${srMin} - ${srMax}`;

      document.getElementById('expFoils').innerText = n;
    }"""

new_prob_js = """    // PROBABILITY CALCULATOR
    function updateProbabilityCalc(n) {
      n = parseInt(n);
      document.getElementById('sliderVal').innerText = n;
      document.querySelectorAll('.exp-pack-n').forEach(el => el.innerText = n);

      // Prob of at least 1 enchanted: 1 - (1 - 1/96)^n
      const pEnchanted = (1 - Math.pow(1 - 1/96, n)) * 100;
      document.getElementById('expEnchantedProb').innerText = pEnchanted.toFixed(1) + '%';

      // Prob of at least 1 iconic: 1 - (1 - 1/384)^n
      const pIconic = (1 - Math.pow(1 - 1/384, n)) * 100;
      if (document.getElementById('expIconicProb')) {
        document.getElementById('expIconicProb').innerText = pIconic.toFixed(1) + '%';
      }

      // Epic expectancy: ~1 in 16 packs (0.0625 per pack)
      if (document.getElementById('expEpic')) {
        const epMin = (n * 0.055).toFixed(1);
        const epMax = (n * 0.085).toFixed(1);
        document.getElementById('expEpic').innerText = `${epMin} - ${epMax}`;
      }

      // Legendary expectancy: ~1 in 5-6 packs
      const legMin = (n * 0.17).toFixed(1);
      const legMax = (n * 0.22).toFixed(1);
      document.getElementById('expLegendary').innerText = `${legMin} - ${legMax}`;

      // Super rare expectancy: ~0.52 per pack
      const srMin = (n * 0.48).toFixed(1);
      const srMax = (n * 0.58).toFixed(1);
      document.getElementById('expSuperRare').innerText = `${srMin} - ${srMax}`;

      document.getElementById('expFoils').innerText = n;
    }"""

if old_prob_js in html:
    html = html.replace(old_prob_js, new_prob_js)

with open("collector-vault.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Enhanced probability calculator in collector-vault.html!")
