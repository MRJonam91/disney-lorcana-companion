# Disney Lorcana · Community Companion

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[Italiano](README.it.md) · [English](README.en.md) · [Français](README.fr.md) · [Deutsch](README.de.md) · [Español](README.es.md)

An unofficial static companion for learning and playing Disney Lorcana.
Open **[the web portal](index.html)** for guides, a searchable glossary,
a two-player lore tracker and a mulligan probability calculator.

**Stato / Status:** sito utilizzabile offline; traduzioni e dati storici ancora
da verificare. / The website works offline; translations are partial and
historical game data still requires source verification. See
[source status and calculator assumptions](docs/source-status.md).

## Open and use

No installation or build is needed. Open `index.html` in a current desktop
or mobile browser, or open a guide directly:

| Language | Interactive guide | Written rules notes |
| --- | --- | --- |
| Italiano | [Guida](guide/guida-lorcana-it.html) | [Regole](docs/rules/complete-rules.it.md) |
| English | [Guide](guide/lorcana-guide-en.html) | [Rules](docs/rules/complete-rules.en.md) |
| Français | [Guide](guide/lorcana-guide-fr.html) | [Règles](docs/rules/complete-rules.fr.md) |
| Deutsch | [Leitfaden](guide/lorcana-guide-de.html) | [Regeln](docs/rules/complete-rules.de.md) |
| Español | [Guía](guide/lorcana-guide-es.html) | [Reglas](docs/rules/complete-rules.es.md) |

Each guide is a single downloadable HTML file. No web fonts, CDN libraries,
accounts or backend are required. Reading and the native contents menu work
without JavaScript; search, scores and calculations require JavaScript.
Scores reset when you reload. External sources and GitHub documentation
links require a connection.

The calculator computes the chance of finding **at least one target**,
keeping targets and accounting for the post-mulligan shuffle. It uses exact
hypergeometric calculations rounded for display, not simulations and not
multi-card combo probabilities. Invalid inputs show an error instead of odds.

## Content boundaries

The site is a community learning aid, not the official rulebook or a live
meta database. Some legacy paragraphs remain in Italian on other language
pages. Tournament counts, win rates, collecting claims, prices and deck
examples in older sections are not a verified current dataset. Verify card
text and format legality before playing or purchasing cards. Official
rules and updates are on [Disney Lorcana resources](https://disneylorcana.com/en/resources/).

## Local development and checks

For an optional local web server (Python 3):

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765`. For checks, use Python 3.10+ and Node.js 22+:

```sh
python tools/check_site.py
node --test tools/odds.test.cjs
python tools/run_git_workflow.py
```

The last command only inspects the current checkout; it does not initialize
Git, change identity, create branches, merge or commit. CI runs the static
and calculator checks. Browser QA should also cover narrow screens,
keyboard navigation, glossary empty/reset states, score win/reset states,
invalid inputs, reduced motion and offline/no-JavaScript reading.

The five guides intentionally embed the same CSS and runtime to preserve
single-file distribution. Keep runtime fixes synchronized; the checker
detects script drift. There are no production package dependencies.

## Community and maintenance

- [Contribute](CONTRIBUTING.md), [conduct](CODE_OF_CONDUCT.md), [support](SUPPORT.md)
- [Report a security issue](SECURITY.md), [changelog](CHANGELOG.md)
- [GitHub Discussions](https://github.com/MRJonam91/disney-lorcana-companion/discussions), when enabled

## License and attribution

Original contributions retain the existing [MIT license](LICENSE). See
[NOTICE](NOTICE), [third-party notices](THIRD_PARTY_NOTICES.md) and
[asset provenance](ASSETS.md). Disney Lorcana, characters, card names and
trademarks belong to their respective owners. The software license grants
no rights to third-party art, card text or trademarks. This project is not
affiliated with, endorsed by or sponsored by Disney or Ravensburger.

## Support the project / Sostieni il progetto

Support is voluntary and grants no additional license or rights. / Il
supporto è volontario e non attribuisce licenze o diritti aggiuntivi:
[GitHub Sponsors](https://github.com/sponsors/MRJonam91),
[Ko-fi](https://ko-fi.com/mrjonam),
[Buy Me a Coffee](https://buymeacoffee.com/mrjonam),
[PayPal](https://paypal.me/manorollo).
