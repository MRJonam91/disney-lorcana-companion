"""Dependency-free checks for shipped standalone pages and local links."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path
        self.ids = set()
        self.links = []
        self.errors = []
        self.labels = set()
        self.fields = []
        self.mains = 0
        self.balance = {'div': 0, 'a': 0, 'main': 0}

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag in self.balance:
            self.balance[tag] += 1
        if id_ := attrs.get('id'):
            if id_ in self.ids:
                self.errors.append(f'duplicate id: {id_}')
            self.ids.add(id_)
        if tag == 'main':
            self.mains += 1
        if tag == 'label':
            self.labels.add(attrs.get('for'))
        if tag in ('input', 'select'):
            self.fields.append(attrs)
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])
        if tag in ('script', 'link'):
            url = attrs.get('src', attrs.get('href', ''))
            if url.startswith(('http:', 'https:', '//')):
                self.errors.append(f'external runtime dependency: {url}')

    def handle_endtag(self, tag):
        if tag in self.balance:
            self.balance[tag] -= 1
            if self.balance[tag] < 0:
                self.errors.append(f'unexpected closing tag: {tag}')


def main():
    paths = [ROOT / 'index.html', ROOT / 'tournament-decks.html', ROOT / 'tournament-decks.en.html', *sorted((ROOT / 'guide').glob('*.html'))]
    pages = {}
    errors = []
    scripts = []
    for path in paths:
        page = Page(path)
        source = path.read_text(encoding='utf-8')
        page.feed(source)
        for tag, count in page.balance.items():
            if count:
                page.errors.append(f'unbalanced {tag} tags: {count}')
        pages[path] = page
        if page.mains != 1:
            page.errors.append('expected exactly one main landmark')
        for attrs in page.fields:
            if attrs.get('id') not in page.labels and not attrs.get('aria-label'):
                page.errors.append(f'unlabelled form control: {attrs.get("id")}')
        if 'name="description"' not in source:
            page.errors.append('missing meta description')
        if path.parent.name == 'guide':
            scripts.append(re.search(r'<script>([\s\S]*?)</script>', source)[1])
        errors.extend(f'{path.relative_to(ROOT)}: {e}' for e in page.errors)
    if any(script != scripts[0] for script in scripts):
        errors.append('guide runtimes have drifted between languages')
    for path, page in pages.items():
        for href in page.links:
            url = urlsplit(href)
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path
            if not target.is_file():
                errors.append(f'{path.relative_to(ROOT)}: missing link {href}')
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(ROOT)}: missing anchor {href}')
    markdown = [*ROOT.glob('*.md'), *(ROOT / 'docs').rglob('*.md')]
    for path in markdown:
        source = path.read_text(encoding='utf-8')
        for href in re.findall(r'(?<!!)\[[^\]]+\]\(([^\s)]+)\)', source):
            url = urlsplit(href)
            if url.scheme or url.netloc or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.exists():
                errors.append(f'{path.relative_to(ROOT)}: missing Markdown link {href}')
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        return 1
    print(f'PASS: {len(pages)} pages, {len(markdown)} Markdown files, local links, anchors, labels, metadata, offline dependencies and synchronized runtimes')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
