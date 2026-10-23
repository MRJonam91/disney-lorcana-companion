import os
import json
import csv
import sqlite3
import re

def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

def normalize_rarity(r):
    if not r:
        return "Common"
    r_map = {
        "common": "Common",
        "uncommon": "Uncommon",
        "rare": "Rare",
        "super_rare": "Super Rare",
        "super rare": "Super Rare",
        "legendary": "Legendary",
        "epic": "Epic",
        "enchanted": "Enchanted",
        "iconic": "Iconic",
    }
    return r_map.get(r.lower(), r.replace("_", " ").title())

def sort_key_collector(c):
    cn = str(c.get("collector_number", "0"))
    m = re.match(r'^(\d+)', cn)
    num = int(m.group(1)) if m else 9999
    return (num, cn)

def main():
    os.makedirs("data/sets/json", exist_ok=True)
    os.makedirs("data/sets/csv", exist_ok=True)
    os.makedirs("data/sets/db", exist_ok=True)
    os.makedirs("docs/sets/cards", exist_ok=True)

    master_sets = []
    master_csv_rows = []
    js_sets = []

    # Prepare Master SQLite DB
    master_db_path = "data/lorcana-all-sets.db"
    if os.path.exists(master_db_path):
        os.remove(master_db_path)
    m_conn = sqlite3.connect(master_db_path)
    m_cur = m_conn.cursor()
    m_cur.execute("""
        CREATE TABLE sets (
            set_num INTEGER PRIMARY KEY,
            code TEXT,
            name TEXT,
            released_at TEXT,
            total_cards INTEGER,
            has_epic INTEGER,
            has_iconic INTEGER
        )
    """)
    m_cur.execute("""
        CREATE TABLE cards (
            id TEXT PRIMARY KEY,
            set_num INTEGER,
            set_code TEXT,
            set_name TEXT,
            collector_number TEXT,
            name TEXT,
            version TEXT,
            full_name TEXT,
            ink TEXT,
            inks TEXT,
            type TEXT,
            classifications TEXT,
            cost INTEGER,
            inkwell INTEGER,
            strength INTEGER,
            willpower INTEGER,
            lore INTEGER,
            move_cost INTEGER,
            rarity TEXT,
            keywords TEXT,
            text TEXT,
            price_usd REAL,
            price_usd_foil REAL,
            image_small TEXT,
            image_normal TEXT,
            tcgplayer_url TEXT
        )
    """)

    csv_headers = [
        "set_num", "set_code", "set_name", "collector_number", "name", "version", "full_name",
        "ink", "inks", "type", "classifications", "cost", "inkwell", "strength", "willpower",
        "lore", "move_cost", "rarity", "keywords", "price_usd", "price_usd_foil", "image_normal", "tcgplayer_url"
    ]

    md_index_lines = [
        "# 📚 Disney Lorcana — Complete 14-Set Card Database (JSON, SQLite DB, CSV & Markdown)",
        "",
        "> **Official Set & Card Data** synchronized with **LorcanaPlayer / Lorcast / TCGplayer** covering all **14 Main Sets (3,242 cards)**, including exact collector numbers, rarities (`Common`, `Uncommon`, `Rare`, `Super Rare`, `Legendary`, `Epic`, `Enchanted`, `Iconic`), stats, and market prices.",
        "",
        "## 📦 Master Multi-Set Files",
        "- **Master JSON Database**: [`data/lorcana-database.json`](../../../data/lorcana-database.json)",
        "- **Master SQLite Database (`.db`)**: [`data/lorcana-all-sets.db`](../../../data/lorcana-all-sets.db)",
        "- **Master CSV Spreadsheet**: [`data/lorcana-all-cards.csv`](../../../data/lorcana-all-cards.csv)",
        "- **Portable Web JS Bundle**: [`data/lorcana-cards.js`](../../../data/lorcana-cards.js)",
        "",
        "## 🗂️ Per-Set Databases & Card Lists (Sets 1 – 14)",
        "",
        "| Set | Name | Release Date | Total Cards | Iconics (👑) | Enchanteds (✨) | Epics (🟣) | Markdown | JSON | CSV | SQLite DB |",
        "| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |"
    ]

    for set_num in range(1, 15):
        raw_path = f"data/raw_sets/set_{set_num}.json"
        with open(raw_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        s_info = raw["set"]
        raw_cards = raw["cards"]
        raw_cards.sort(key=sort_key_collector)

        set_name = s_info["name"]
        released_at = s_info.get("released_at", "")
        slug = f"set-{set_num:02d}-{slugify(set_name)}"

        norm_cards = []
        js_cards = []
        set_csv_rows = []
        rarity_counts = {}
        iconic_list = []
        enchanted_list = []
        epic_list = []

        # Per-set SQLite DB
        set_db_path = f"data/sets/db/{slug}.db"
        if os.path.exists(set_db_path):
            os.remove(set_db_path)
        s_conn = sqlite3.connect(set_db_path)
        s_cur = s_conn.cursor()
        s_cur.execute("""
            CREATE TABLE cards (
                id TEXT PRIMARY KEY,
                collector_number TEXT,
                name TEXT,
                version TEXT,
                full_name TEXT,
                ink TEXT,
                inks TEXT,
                type TEXT,
                classifications TEXT,
                cost INTEGER,
                inkwell INTEGER,
                strength INTEGER,
                willpower INTEGER,
                lore INTEGER,
                move_cost INTEGER,
                rarity TEXT,
                keywords TEXT,
                text TEXT,
                price_usd REAL,
                price_usd_foil REAL,
                image_normal TEXT,
                tcgplayer_url TEXT
            )
        """)

        for c in raw_cards:
            cid = c.get("id") or f"s{set_num}_{c.get('collector_number')}"
            cn = str(c.get("collector_number", ""))
            name = c.get("name", "")
            version = c.get("version") or ""
            full_name = f"{name} - {version}" if version else name
            ink = (c.get("ink") or "Amber").lower()
            inks_list = c.get("inks") or ([c.get("ink")] if c.get("ink") else [])
            inks_str = "/".join([i for i in inks_list if i])
            type_list = c.get("type") or []
            type_str = " - ".join(type_list) if isinstance(type_list, list) else str(type_list)
            class_list = c.get("classifications") or []
            class_str = ", ".join(class_list) if isinstance(class_list, list) else ""
            cost = c.get("cost") if c.get("cost") is not None else 0
            inkwell = bool(c.get("inkwell", True))
            strength = c.get("strength")
            willpower = c.get("willpower")
            lore = c.get("lore")
            move_cost = c.get("move_cost")
            rarity = normalize_rarity(c.get("rarity"))
            kw_list = c.get("keywords") or []
            kw_str = ", ".join(kw_list) if isinstance(kw_list, list) else ""
            text_val = (c.get("text") or "").replace("\n", " ").strip()

            prices = c.get("prices") or {}
            p_usd = float(prices["usd"]) if prices.get("usd") else None
            p_foil = float(prices["usd_foil"]) if prices.get("usd_foil") else None

            imgs = (c.get("image_uris") or {}).get("digital") or {}
            img_small = imgs.get("small", "")
            img_normal = imgs.get("normal", "")
            tcg_url = (c.get("purchase_uris") or {}).get("tcgplayer") or ""

            rarity_counts[rarity] = rarity_counts.get(rarity, 0) + 1
            if rarity == "Iconic":
                iconic_list.append({
                    "num": cn,
                    "name": full_name,
                    "ink": inks_str or ink.title(),
                    "cost": cost,
                    "price_foil": p_foil,
                    "img": img_normal
                })
            elif rarity == "Enchanted":
                enchanted_list.append({
                    "num": cn,
                    "name": full_name,
                    "ink": inks_str or ink.title(),
                    "cost": cost,
                    "price_foil": p_foil
                })
            elif rarity == "Epic":
                epic_list.append({
                    "num": cn,
                    "name": full_name,
                    "ink": inks_str or ink.title(),
                    "cost": cost,
                    "price_foil": p_foil
                })

            card_obj = {
                "id": f"s{set_num}_{cn}",
                "lorcast_id": cid,
                "set_num": set_num,
                "set_code": str(set_num),
                "set_name": set_name,
                "collector_number": cn,
                "name": name,
                "version": version,
                "full_name": full_name,
                "ink": ink,
                "inks": inks_list,
                "type": type_str,
                "classifications": class_list,
                "cost": cost,
                "inkable": inkwell,
                "strength": strength,
                "willpower": willpower,
                "lore": lore,
                "move_cost": move_cost,
                "rarity": rarity,
                "keywords": kw_list,
                "text": text_val,
                "price_usd": p_usd,
                "price_usd_foil": p_foil,
                "image_small": img_small,
                "image_normal": img_normal,
                "tcgplayer_url": tcg_url
            }
            norm_cards.append(card_obj)

            # Compact card object for browser JS bundle
            js_card = {
                "id": f"s{set_num}_{cn}",
                "num": cn,
                "name": name,
                "sub": version,
                "ink": ink,
                "cost": cost,
                "inkable": inkwell,
                "type": type_str,
                "str": strength,
                "will": willpower,
                "lore": lore,
                "rarity": rarity
            }
            if kw_str:
                js_card["kw"] = kw_str
            if p_usd:
                js_card["usd"] = p_usd
            if p_foil:
                js_card["foil_usd"] = p_foil
            if img_small:
                js_card["img"] = img_small
            js_cards.append(js_card)

            csv_row = [
                set_num, str(set_num), set_name, cn, name, version, full_name,
                ink, inks_str, type_str, class_str, cost, int(inkwell),
                strength if strength is not None else "",
                willpower if willpower is not None else "",
                lore if lore is not None else "",
                move_cost if move_cost is not None else "",
                rarity, kw_str,
                p_usd if p_usd is not None else "",
                p_foil if p_foil is not None else "",
                img_normal, tcg_url
            ]
            set_csv_rows.append(csv_row)
            master_csv_rows.append(csv_row)

            s_cur.execute("""
                INSERT OR REPLACE INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                f"s{set_num}_{cn}", cn, name, version, full_name, ink, inks_str,
                type_str, class_str, cost, int(inkwell), strength, willpower, lore,
                move_cost, rarity, kw_str, text_val, p_usd, p_foil, img_normal, tcg_url
            ))

            m_cur.execute("""
                INSERT OR REPLACE INTO cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """, (
                f"s{set_num}_{cn}", set_num, str(set_num), set_name, cn, name, version,
                full_name, ink, inks_str, type_str, class_str, cost, int(inkwell),
                strength, willpower, lore, move_cost, rarity, kw_str, text_val,
                p_usd, p_foil, img_small, img_normal, tcg_url
            ))

        s_conn.commit()
        s_conn.close()

        has_epic = rarity_counts.get("Epic", 0) > 0
        has_iconic = rarity_counts.get("Iconic", 0) > 0

        m_cur.execute("""
            INSERT OR REPLACE INTO sets VALUES (?,?,?,?,?,?,?)
        """, (set_num, str(set_num), set_name, released_at, len(norm_cards), int(has_epic), int(has_iconic)))

        set_bundle = {
            "id": f"set{set_num}",
            "num": set_num,
            "code": str(set_num),
            "name": set_name,
            "released_at": released_at,
            "total_cards": len(norm_cards),
            "has_epic": has_epic,
            "has_iconic": has_iconic,
            "rarity_breakdown": rarity_counts,
            "iconic_cards": iconic_list,
            "cards": norm_cards
        }
        master_sets.append(set_bundle)

        js_sets.append({
            "id": f"set{set_num}",
            "num": set_num,
            "name": set_name,
            "date": released_at,
            "total": len(js_cards),
            "has_epic": has_epic,
            "has_iconic": has_iconic,
            "rarity_counts": rarity_counts,
            "iconic_cards": [f"#{ic['num']} {ic['name']}" for ic in iconic_list],
            "cards": js_cards
        })

        # Write Per-Set JSON
        with open(f"data/sets/json/{slug}.json", "w", encoding="utf-8") as f:
            json.dump(set_bundle, f, ensure_ascii=False, indent=2)

        # Write Per-Set CSV
        with open(f"data/sets/csv/{slug}.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(csv_headers)
            writer.writerows(set_csv_rows)

        # Write Per-Set Markdown
        md_lines = [
            f"# Set {set_num}: {set_name} — Complete Card List & Rarity Breakdown",
            "",
            f"- **Set Number**: {set_num} (`Set Code: {set_num}`)",
            f"- **Release Date**: `{released_at}`",
            f"- **Total Cards**: **{len(norm_cards)}**",
            f"- **Download Formats**: [JSON](../../../data/sets/json/{slug}.json) · [CSV](../../../data/sets/csv/{slug}.csv) · [SQLite DB](../../../data/sets/db/{slug}.db)",
            "",
            "## 📊 Rarity Breakdown",
            "| Rarity | Card Count |",
            "| :--- | :---: |"
        ]
        for r_key in ["Common", "Uncommon", "Rare", "Super Rare", "Legendary", "Epic", "Enchanted", "Iconic"]:
            if rarity_counts.get(r_key, 0) > 0:
                md_lines.append(f"| **{r_key}** | {rarity_counts[r_key]} |")

        if iconic_list:
            md_lines.extend([
                "",
                "## 👑 Iconic Chase Cards",
                "| # | Card Name | Ink | Cost | Foil Market Value (USD) |",
                "| :---: | :--- | :---: | :---: | :---: |"
            ])
            for ic in iconic_list:
                p_str = f"${ic['price_foil']:,.2f}" if ic['price_foil'] else "N/A"
                md_lines.append(f"| `#{ic['num']}` | **{ic['name']}** | {ic['ink']} | {ic['cost']} | **{p_str}** |")

        if enchanted_list:
            md_lines.extend([
                "",
                "## ✨ Enchanted Cards",
                "| # | Card Name | Ink | Cost | Foil Market Value (USD) |",
                "| :---: | :--- | :---: | :---: | :---: |"
            ])
            for en in enchanted_list:
                p_str = f"${en['price_foil']:,.2f}" if en['price_foil'] else "N/A"
                md_lines.append(f"| `#{en['num']}` | **{en['name']}** | {en['ink']} | {en['cost']} | {p_str} |")

        md_lines.extend([
            "",
            f"## 🃏 Complete Card Checklist ({len(norm_cards)} Cards)",
            "| # | Card Name | Ink | Rarity | Type | Cost | Inkable | Stats (⚔️/🛡️/◊) | USD | Foil USD |",
            "| :---: | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |"
        ])
        for c in norm_cards:
            stats_str = f"{c['strength']}/{c['willpower']}/{c['lore']}◊" if c['strength'] is not None else "—"
            ink_icon = "💧" if c['inkable'] else "🚫"
            u_str = f"${c['price_usd']:.2f}" if c['price_usd'] else "—"
            f_str = f"${c['price_usd_foil']:.2f}" if c['price_usd_foil'] else "—"
            md_lines.append(
                f"| `#{c['collector_number']}` | **{c['full_name']}** | {c['ink'].title()} | {c['rarity']} | {c['type']} | {c['cost']} | {ink_icon} | {stats_str} | {u_str} | {f_str} |"
            )

        with open(f"docs/sets/cards/{slug}.md", "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines) + "\n")

        ic_count = rarity_counts.get("Iconic", 0)
        en_count = rarity_counts.get("Enchanted", 0)
        ep_count = rarity_counts.get("Epic", 0)
        md_index_lines.append(
            f"| **Set {set_num}** | **{set_name}** | `{released_at}` | **{len(norm_cards)}** | {ic_count} | {en_count} | {ep_count} | [📖 MD]({slug}.md) | [📦 JSON](../../../data/sets/json/{slug}.json) | [📊 CSV](../../../data/sets/csv/{slug}.csv) | [🗄️ DB](../../../data/sets/db/{slug}.db) |"
        )

    m_conn.commit()
    m_conn.close()

    # Write Master JSON
    with open("data/lorcana-database.json", "w", encoding="utf-8") as f:
        json.dump({"total_sets": 14, "total_cards": len(master_csv_rows), "sets": master_sets}, f, ensure_ascii=False, indent=2)

    # Write Master CSV
    with open("data/lorcana-all-cards.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)
        writer.writerows(master_csv_rows)

    # Write Docs Sets Cards README
    with open("docs/sets/cards/README.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_index_lines) + "\n")

    # Write Portable Web JS Bundle (data/lorcana-cards.js)
    with open("data/lorcana-cards.js", "w", encoding="utf-8") as f:
        f.write("// Official Disney Lorcana Complete 14-Set Card Database (3,242 Cards)\n")
        f.write("window.LORCANA_SETS_DB = ")
        json.dump(js_sets, f, ensure_ascii=False, separators=(",", ":"))
        f.write(";\n")

    print(f"Successfully generated JSON, CSV, SQLite DB, Markdown, and JS bundle for all 14 sets ({len(master_csv_rows)} total cards)!")

if __name__ == "__main__":
    main()
