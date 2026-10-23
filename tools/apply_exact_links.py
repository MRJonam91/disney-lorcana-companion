with open("collector-vault.html", "r", encoding="utf-8") as f:
    cv = f.read()

target_cv = """          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831" target="_blank" class="btn-pack" style="border-color:#93c5fd;color:#93c5fd;font-size:.82rem;">
              🍎 Scarica su App Store ➔
            </a>
            <a href="https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US" target="_blank" class="btn-pack" style="border-color:#4ade80;color:#4ade80;font-size:.82rem;">
              🤖 Scarica su Google Play Store ➔
            </a>
          </div>"""

replacement_cv = """          <div style="display:flex;gap:10px;flex-wrap:wrap;">
            <a href="https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831" target="_blank" class="btn-pack" style="border-color:#93c5fd;color:#93c5fd;font-size:.82rem;">
              🍎 Scarica su App Store ➔
            </a>
            <a href="https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US" target="_blank" class="btn-pack" style="border-color:#4ade80;color:#4ade80;font-size:.82rem;">
              🤖 Scarica su Google Play Store ➔
            </a>
            <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" class="btn-pack" style="border-color:var(--gold);color:var(--gold);font-size:.82rem;">
              🌐 Pagina Ufficiale Ravensburger App ➔
            </a>
          </div>"""

if target_cv in cv:
    cv = cv.replace(target_cv, replacement_cv)
    with open("collector-vault.html", "w", encoding="utf-8") as f:
        f.write(cv)
    print("collector-vault.html updated with official page link!")
else:
    print("target_cv not matched directly, checking normalized...")
    cv = cv.replace(
        '<a href="https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US" target="_blank" class="btn-pack" style="border-color:#4ade80;color:#4ade80;font-size:.82rem;">\n              🤖 Scarica su Google Play Store ➔\n            </a>',
        '<a href="https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US" target="_blank" class="btn-pack" style="border-color:#4ade80;color:#4ade80;font-size:.82rem;">\n              🤖 Scarica su Google Play Store ➔\n            </a>\n            <a href="https://www.disneylorcana.com/it-IT/app" target="_blank" class="btn-pack" style="border-color:var(--gold);color:var(--gold);font-size:.82rem;">\n              🌐 Pagina Ufficiale Ravensburger App ➔\n            </a>'
    )
    with open("collector-vault.html", "w", encoding="utf-8") as f:
        f.write(cv)
    print("collector-vault.html updated via fallback!")

with open("index.html", "r", encoding="utf-8") as f:
    idx = f.read()

idx = idx.replace(
    '<a href="https://www.disneylorcana.com/" target="_blank" class="btn-hero dark" style="font-size:.85rem;padding:10px 18px;">\n              🌐 Sito Ufficiale Disney Lorcana ➔\n            </a>',
    '<a href="https://www.disneylorcana.com/it-IT/app" target="_blank" class="btn-hero dark" style="font-size:.85rem;padding:10px 18px;border-color:var(--gold);color:var(--gold);">\n              🌐 Pagina Ufficiale Companion App ➔\n            </a>'
)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx)
print("index.html updated with direct official app page link!")
