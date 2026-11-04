import subprocess
import json
import os

os.makedirs("data/raw_sets", exist_ok=True)

ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

sets_resp = subprocess.check_output(["curl.exe", "-s", "-L", "-A", ua, "https://api.lorcast.com/v0/sets"]).decode("utf-8")
sets_data = json.loads(sets_resp)["results"]

main_sets = [s for s in sets_data if s["code"] in [str(i) for i in range(1, 15)]]
main_sets.sort(key=lambda s: int(s["code"]))

for s in main_sets:
    code = s["code"]
    url = f"https://api.lorcast.com/v0/sets/{code}/cards"
    raw = subprocess.check_output(["curl.exe", "-s", "-L", "-A", ua, url]).decode("utf-8")
    cards = json.loads(raw)
    with open(f"data/raw_sets/set_{code}.json", "w", encoding="utf-8") as f:
        json.dump({"set": s, "cards": cards}, f, ensure_ascii=False, indent=2)

    rarities = {}
    iconics = []
    for c in cards:
        r = c.get("rarity", "Unknown")
        rarities[r] = rarities.get(r, 0) + 1
        if r.lower() == "iconic":
            iconics.append(f"#{c.get('collector_number')} {c.get('name')} - {c.get('version')}")
    print(f"Set {code:>2}: {s['name']:<24} | Released: {s['released_at']} | Total Cards: {len(cards):>3} | Rarities: {rarities}")
    if iconics:
        print(f"   -> Iconics: {iconics}")
