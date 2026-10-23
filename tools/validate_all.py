files = [
    'index.html',
    'collector-vault.html',
    'deck-lab.html',
    'guide/guida-lorcana-it.html',
    'guide/lorcana-guide-en.html',
    'guide/lorcana-guide-fr.html',
    'guide/lorcana-guide-de.html',
    'guide/lorcana-guide-es.html'
]
for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    o_div = text.count('<div')
    c_div = text.count('</div>')
    status = "OK" if o_div == c_div else "MISMATCH!"
    print(f"[{status}] {fname}: {len(text):,} chars | open divs: {o_div}, close divs: {c_div}")
