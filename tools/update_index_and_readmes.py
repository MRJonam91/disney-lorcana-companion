import re

def update_index():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Update collector's vault description
    old_desc = "Simula l'apertura realistica di 1 bustina, 10 bustine, 1 Trove (8 pack), 1 Booster Box (24 pack) o un intero Case (96 pack). Calcola con precisione binomiale le probabilità di trovare carte Incantate per ogni set, consulta il catalogo prodotti e genera sfide casuali con moneta 3D."
    new_desc = "Simula l'apertura realistica con qualsiasi quantità di bustine a scelta (1, 8, 10, Box da 24, Case da 96 o numero personalizzato). Include le rarità Epiche e Iconiche, la guida ai simboli ufficiali e all'evoluzione delle 3 Ere, calcolatore binomiale e collegamento a r/Lorcana Educational."

    if old_desc in html:
        html = html.replace(old_desc, new_desc)

    # Update tags
    old_tags = """              <span class="feat-tag">🎴 Pack Simulator</span>
              <span class="feat-tag">✨ Incantate (1:80)</span>
              <span class="feat-tag">📦 Catalogo Prodotti</span>
              <span class="feat-tag">🪙 Coin Flip Decider</span>"""

    new_tags = """              <span class="feat-tag">🎴 Pack Simulator</span>
              <span class="feat-tag">🔢 Input Libero Quantità</span>
              <span class="feat-tag">🟣 Epiche &amp; 👑 Iconiche</span>
              <span class="feat-tag">⏳ Confronto 3 Ere</span>
              <span class="feat-tag">🤖 Reddit Educational</span>"""

    if old_tags in html:
        html = html.replace(old_tags, new_tags)

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("index.html updated successfully!")

def update_readmes():
    # Update README.md
    with open("README.md", "r", encoding="utf-8") as f:
        rm = f.read()

    old_row = "| **💎 Collector's Vault** | Realistic booster pack simulator (1 pack, 10, Trove, 24-box, 96-case), binomial pull rate calculator per set, sealed product catalog, random quest generator & coin flip | [Open Collector's Vault](collector-vault.html) |"
    new_row = "| **💎 Collector's Vault** | Realistic booster pack simulator with custom pack input (1 to 10,000 packs), Epic (🟣) & Iconic (👑) chase support, 3-Eras historical evolution (Classic, Expansion, Modern), factory balancing vs blister analysis, and Reddit r/Lorcana Educational hub | [Open Collector's Vault](collector-vault.html) |"
    if old_row in rm:
        rm = rm.replace(old_row, new_row)
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(rm)
        print("README.md updated!")

    # Update README.it.md
    with open("README.it.md", "r", encoding="utf-8") as f:
        rm_it = f.read()

    old_row_it = "| **💎 Collector's Vault** | Simulatore realistico spacchettamento (1, 10, Trove, box 24, case 96), calcolatore pull rate binomiale per set, catalogo prodotti sigillati, generatore sfide e lancio moneta | [Apri Collector's Vault](collector-vault.html) |"
    new_row_it = "| **💎 Collector's Vault** | Simulatore spacchettamento realistico con input personalizzato di bustine, supporto rarità Epiche (🟣) e Iconiche (👑), evoluzione storica delle 3 Ere, analisi bilanciamento box vs blister e risorsa Reddit r/Lorcana Educational | [Apri Collector's Vault](collector-vault.html) |"
    if old_row_it in rm_it:
        rm_it = rm_it.replace(old_row_it, new_row_it)
        with open("README.it.md", "w", encoding="utf-8") as f:
            f.write(rm_it)
        print("README.it.md updated!")

if __name__ == "__main__":
    update_index()
    update_readmes()
