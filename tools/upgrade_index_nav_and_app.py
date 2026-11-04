import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add top-bar styles if not present
topbar_css = """
    /* Sticky Top Bar */
    .top-bar {
      background: rgba(14, 11, 20, 0.96);
      border-bottom: 1px solid var(--line);
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(10px);
    }
    .top-brand {
      font-family: 'Cinzel', serif;
      font-weight: 900;
      letter-spacing: .08em;
      color: var(--gold);
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 1.1rem;
    }
    .top-links {
      display: flex;
      gap: 14px;
      align-items: center;
      font-size: .86rem;
      flex-wrap: wrap;
    }
    .top-links a {
      color: var(--parch-muted);
      padding: 6px 14px;
      border-radius: 8px;
      transition: all .2s;
      font-weight: 600;
    }
    .top-links a:hover, .top-links a.active {
      color: var(--gold);
      background: rgba(229, 185, 92, .14);
    }
    .top-links a.highlight {
      background: linear-gradient(135deg, rgba(229, 185, 92, .25), rgba(229, 185, 92, .08));
      border: 1px solid var(--gold);
      color: var(--gold);
    }
    .hero-actions {
      display: flex;
      gap: 14px;
      justify-content: center;
      flex-wrap: wrap;
      margin: 24px 0 36px;
    }
    .btn-hero {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 24px;
      border-radius: 12px;
      font-family: 'Cinzel', serif;
      font-weight: 700;
      font-size: .95rem;
      transition: all .25s;
      box-shadow: 0 4px 20px rgba(0,0,0,0.4);
    }
    .btn-hero:hover {
      transform: translateY(-3px);
      box-shadow: 0 8px 30px rgba(229, 185, 92, 0.3);
    }
    .btn-hero.gold {
      background: linear-gradient(135deg, #ffd700, #b2862d);
      color: #0c0a12;
      border: 1px solid #ffd700;
    }
    .btn-hero.pink {
      background: linear-gradient(135deg, rgba(244,114,182,0.3), rgba(168,85,247,0.2));
      border: 1.5px solid #f472b6;
      color: #ffd9f0;
    }
    .btn-hero.dark {
      background: var(--bg-card);
      border: 1px solid var(--line);
      color: var(--parch);
    }
"""

if '.top-bar {' not in text:
    text = text.replace('/* Container */', topbar_css + '\n    /* Container */')

# 2. Add top bar right after <body>
top_nav_html = """  <!-- Top Sticky Navigation -->
  <div class="top-bar">
    <a href="index.html" class="top-brand">
      <span>✦ DISNEY LORCANA</span>
      <span style="color:var(--parch-muted);font-weight:400;font-size:.85rem;">| Community Portal</span>
    </a>
    <div class="top-links">
      <a href="index.html" class="active">🌐 Hub Home</a>
      <a href="deck-lab.html" class="highlight">🃏 Deck Lab &amp; Test</a>
      <a href="collector-vault.html" class="highlight" style="border-color:#f472b6;color:#ff80bf;">💎 Collezionismo &amp; Pulls</a>
      <a href="guide/guida-lorcana-it.html">📖 Guida IT</a>
      <a href="guide/lorcana-guide-en.html">🇬🇧 Guide EN</a>
      <a href="#official-app">📱 App Ufficiale</a>
      <a href="https://github.com/MRJonam91/disney-lorcana-companion/discussions" target="_blank">💬 Forum</a>
    </div>
  </div>
"""

if '<!-- Top Sticky Navigation -->' not in text:
    text = text.replace('<body>', '<body>\n\n' + top_nav_html, 1)

# 3. Add Hero CTA Buttons right after <p class="subtitle">...</p>
hero_btns_html = """      <!-- Hero Quick Launch Buttons -->
      <div class="hero-actions">
        <a href="deck-lab.html" class="btn-hero gold">🃏 Apri Deck Lab &amp; Playtester</a>
        <a href="collector-vault.html" class="btn-hero pink">💎 Apri Collector's Vault &amp; Pulls</a>
        <a href="guide/guida-lorcana-it.html" class="btn-hero dark">📖 Leggi Guida Ufficiale (IT)</a>
        <a href="#official-app" class="btn-hero dark">📱 App Ufficiale Ravensburger</a>
      </div>
"""

if '<!-- Hero Quick Launch Buttons -->' not in text:
    subtitle_end = text.find('</p>', text.find('class="subtitle"'))
    if subtitle_end != -1:
        text = text[:subtitle_end + 4] + '\n' + hero_btns_html + text[subtitle_end + 4:]

# 4. Add Official Companion App Section before footer
app_section_html = """
    <!-- Official Disney Lorcana Companion App Banner -->
    <section id="official-app" style="margin-bottom:70px;background:linear-gradient(145deg, rgba(59,126,194,0.15), var(--bg-card));border:1.5px solid var(--sapphire);border-radius:18px;padding:36px;box-shadow:0 12px 40px rgba(0,0,0,0.5);">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:24px;">
        <div style="max-width:700px;">
          <div style="font-size:0.8rem;letter-spacing:0.12em;text-transform:uppercase;color:#93c5fd;font-weight:700;margin-bottom:8px;">App Ufficiale Ravensburger per il Collezionismo</div>
          <h2 style="font-family:'Cinzel',serif;font-size:1.8rem;color:var(--gold);margin-bottom:12px;">Disney Lorcana TCG Companion App</h2>
          <p style="color:var(--parch-muted);font-size:0.95rem;line-height:1.6;margin-bottom:18px;">
            L'applicazione ufficiale gratuita per iOS e Android sviluppata da Ravensburger: catalogo completo di tutte le carte da sfogliare in 3D con effetto foil reattivo al giroscopio dello smartphone, gestione del raccoglitore personale (carte possedute e wishlist), segnapunti Lore ufficiale e avvisi sulle nuove espansioni.
          </p>
          <div style="display:flex;gap:12px;flex-wrap:wrap;">
            <a href="https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831" target="_blank" class="btn-hero dark" style="border-color:#93c5fd;color:#93c5fd;font-size:.85rem;padding:10px 18px;">
              🍎 Scarica su Apple App Store ➔
            </a>
            <a href="https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US" target="_blank" class="btn-hero dark" style="border-color:#4ade80;color:#4ade80;font-size:.85rem;padding:10px 18px;">
              🤖 Scarica su Google Play Store ➔
            </a>
            <a href="https://www.disneylorcana.com/" target="_blank" class="btn-hero dark" style="font-size:.85rem;padding:10px 18px;">
              🌐 Sito Ufficiale Disney Lorcana ➔
            </a>
          </div>
        </div>
        <div style="font-size:5rem;text-align:center;padding:10px 20px;">
          📱✨
        </div>
      </div>
    </section>
"""

if 'id="official-app"' not in text:
    text = text.replace('  </main>', app_section_html + '\n  </main>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated index.html with top navigation, hero CTAs, and official companion app section!")
