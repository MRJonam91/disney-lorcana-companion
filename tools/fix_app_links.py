import os

def update_file(path):
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    orig = content

    # 1. Replace Apple App Store URL
    old_apple = [
        "https://apps.apple.com/app/disney-lorcana-tcg-companion/id6448270106",
        "https://apps.apple.com/app/disney-lorcana-tcg-companion/id6448270106",
    ]
    for oa in old_apple:
        content = content.replace(oa, "https://apps.apple.com/us/app/disney-lorcana-tcg-companion/id6444333831")

    # 2. Replace Google Play Store URL
    old_google = [
        "https://play.google.com/store/apps/details?id=com.ravensburger.disneylorcana",
    ]
    for og in old_google:
        content = content.replace(og, "https://play.google.com/store/apps/details?id=com.ravensburger.disney.lorcana&hl=en_US")

    # 3. Replace Official site link where appropriate
    content = content.replace("https://www.disneylorcana.com/en-US/app/", "https://www.disneylorcana.com/it-IT/app")
    content = content.replace("https://www.disneylorcana.com/en-US/app", "https://www.disneylorcana.com/it-IT/app")

    if content != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {path}")
    else:
        print(f"No changes needed: {path}")

def main():
    files = [
        "index.html",
        "collector-vault.html",
        "deck-lab.html",
        "docs/cards-and-rarities/pull-rates-and-products.it.md",
        "docs/cards-and-rarities/pull-rates-and-products.en.md",
        "README.md",
        "README.it.md",
        "tools/upgrade_collector_vault.py",
        "tools/upgrade_index_nav_and_app.py",
        "tools/upgrade_deck_lab.py",
        "tools/upgrade_vault_and_docs.py"
    ]
    for f in files:
        update_file(f)

if __name__ == "__main__":
    main()
