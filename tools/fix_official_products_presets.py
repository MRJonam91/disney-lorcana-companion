with open("collector-vault.html", "r", encoding="utf-8") as f:
    cv = f.read()

old_presets = """        <!-- Row 2: 5-Column Product Preset Action Cards -->
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
        </div>"""

new_presets = """        <!-- Row 2: 5-Column Official Sealed Products Preset Cards -->
        <div class="pack-presets-grid">
          <button type="button" class="pack-action-card" onclick="openPacks(1)">
            <span class="pack-action-icon">✨</span>
            <span class="pack-action-title" data-i18n="act_1_title">1 Booster Pack</span>
            <span class="pack-action-sub" data-i18n="act_1_sub">1 Bustina · 12 Carte (o Starter)</span>
          </button>

          <button type="button" class="pack-action-card" onclick="openPacks(4)">
            <span class="pack-action-icon">🌟</span>
            <span class="pack-action-title" data-i18n="act_4_title">Gift Set</span>
            <span class="pack-action-sub" data-i18n="act_4_sub">4 Bustine · 48 Carte</span>
          </button>

          <button type="button" class="pack-action-card" onclick="openPacks(8)">
            <span class="pack-action-icon">🎁</span>
            <span class="pack-action-title" data-i18n="act_8_title">Illumineer's Trove</span>
            <span class="pack-action-sub" data-i18n="act_8_sub">8 Bustine · 96 Carte</span>
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
        </div>"""

if old_presets in cv:
    cv = cv.replace(old_presets, new_presets)

# Also set default custom pack input to 10 so opening 10 loose packs is 1 click
cv = cv.replace('value="36" class="custom-pack-input"', 'value="10" class="custom-pack-input"')

with open("collector-vault.html", "w", encoding="utf-8") as f:
    f.write(cv)

# Update data/lorcana-i18n.js
with open("data/lorcana-i18n.js", "r", encoding="utf-8") as f:
    i18n = f.read()

replacements = [
    # IT
    ('act_1_title: "1 Bustina",\n      act_1_sub: "12 Carte · 1 Foil Garantita",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Bustine · 96 Carte",\n      act_10_title: "Bundle 10 Pack",\n      act_10_sub: "10 Bustine · 120 Carte",',
     'act_1_title: "1 Booster Pack",\n      act_1_sub: "1 Bustina · 12 Carte (o Starter)",\n      act_4_title: "Gift Set",\n      act_4_sub: "4 Bustine · 48 Carte",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Bustine · 96 Carte",'),
    # EN
    ('act_1_title: "1 Booster Pack",\n      act_1_sub: "12 Cards · 1 Guaranteed Foil",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Packs · 96 Cards",\n      act_10_title: "10-Pack Bundle",\n      act_10_sub: "10 Packs · 120 Cards",',
     'act_1_title: "1 Booster Pack",\n      act_1_sub: "1 Pack · 12 Cards (or Starter)",\n      act_4_title: "Gift Set",\n      act_4_sub: "4 Packs · 48 Cards",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Packs · 96 Cards",'),
    # FR
    ('act_1_title: "1 Booster",\n      act_1_sub: "12 Cartes · 1 Foil Garantie",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Boosters · 96 Cartes",\n      act_10_title: "Lot de 10 Boosters",\n      act_10_sub: "10 Boosters · 120 Cartes",',
     'act_1_title: "1 Booster",\n      act_1_sub: "1 Booster · 12 Cartes (ou Starter)",\n      act_4_title: "Coffret Cadeau (Gift Set)",\n      act_4_sub: "4 Boosters · 48 Cartes",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Boosters · 96 Cartes",'),
    # DE
    ('act_1_title: "1 Booster Pack",\n      act_1_sub: "12 Karten · 1 Garantierte Foil",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Booster · 96 Karten",\n      act_10_title: "10er Booster-Bundle",\n      act_10_sub: "10 Booster · 120 Karten",',
     'act_1_title: "1 Booster Pack",\n      act_1_sub: "1 Booster · 12 Karten (oder Starter)",\n      act_4_title: "Geschenkset (Gift Set)",\n      act_4_sub: "4 Booster · 48 Karten",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Booster · 96 Karten",'),
    # ES
    ('act_1_title: "1 Sobre",\n      act_1_sub: "12 Cartas · 1 Foil Garantizada",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Sobres · 96 Cartas",\n      act_10_title: "Lote 10 Sobres",\n      act_10_sub: "10 Sobres · 120 Cartas",',
     'act_1_title: "1 Sobre (Booster)",\n      act_1_sub: "1 Sobre · 12 Cartas (o Starter)",\n      act_4_title: "Gift Set (Caja Regalo)",\n      act_4_sub: "4 Sobres · 48 Cartas",\n      act_8_title: "Illumineer\'s Trove",\n      act_8_sub: "8 Sobres · 96 Cartas",')
]

for old_s, new_s in replacements:
    assert old_s in i18n, f"Missing: {old_s[:30]}"
    i18n = i18n.replace(old_s, new_s)

with open("data/lorcana-i18n.js", "w", encoding="utf-8") as f:
    f.write(i18n)

print("Replaced non-existent 10-Pack Bundle with official Gift Set (4 Boosters) across all 5 languages!")
