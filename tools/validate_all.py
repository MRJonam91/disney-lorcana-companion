for fname in ['deck-lab.html', 'collector-vault.html', 'index.html']:
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"{fname}: {len(text):,} chars | open divs: {text.count('<div')}, close divs: {text.count('</div>')}")
