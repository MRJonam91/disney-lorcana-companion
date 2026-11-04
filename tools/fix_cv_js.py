with open("collector-vault.html", "r", encoding="utf-8") as f:
    s = f.read()

bad = """    } - ${picked.sub}`, rarity: rarity, foil: isFoil };
      }
      const generic = (CARD_SAMPLES[rarity] || CARD_SAMPLES.Common);
      return { name: generic[Math.floor(Math.random() * generic.length)], rarity: rarity, foil: isFoil };
    }"""

assert bad in s, "bad string not found"
s = s.replace(bad, "    }")

with open("collector-vault.html", "w", encoding="utf-8") as f:
    f.write(s)
print("Fixed collector-vault.html JS!")
