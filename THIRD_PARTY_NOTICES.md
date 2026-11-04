# Third-party notices / Avvisi di terze parti

The shipped website uses HTML, CSS and browser JavaScript only. It has no
production package dependencies. The standalone guides and new tournament
  catalog do not download fonts. System fonts are
provided by the reader's operating system and are not redistributed.

Il sito distribuito usa solo HTML, CSS e JavaScript del browser. Non include
dipendenze di produzione né font scaricati. I font di sistema appartengono
all'installazione del lettore e non vengono ridistribuiti.

- **Disney Lorcana, Disney and Ravensburger**: third-party names and card
  references used for identification and discussion; no trademark license
  or endorsement is implied. See the [official resources](https://disneylorcana.com/en/resources/).
- **Historical tournament and collecting notes** mention inkDecks, lorcana.gg,
  TCGplayer and grading services. Those mentions do not establish a verified
  dataset, permission to reproduce material, or current pricing. No raw
  tournament dataset is included. See [source status](docs/source-status.md).
- **MIT license**: retained from the existing repository. It permits reuse of
  the original contributions, including proprietary forks; it does not grant
  rights to third-party characters, card text, art or marks. This maintenance
  change does not relicense prior contributions.
- **Development checks**: Python and Node.js standard libraries; CI invokes
  GitHub's checkout, setup-python and setup-node actions. Playwright may be
  used separately for browser QA and is not shipped with the website.

## Upstream database and assets / Database e asset preesistenti

`data/lorcana-database.json`, portable JSON/CSV/SQLite variants, and
`data/lorcana-cards.js` were added by upstream commits, sourced through
Lorcast. Their “official” description is an upstream label, not proof of an
officially licensed dataset. Card-image links point to Lorcast; card text,
art and marks retain their owners' rights. See [ASSETS.md](ASSETS.md).
New tournament metadata is derived from that snapshot, with list quantities
independently compared to the cited original deck pages. It is not a live
price feed. / I metadati usano quella fotografia; quantità e fonti delle
liste sono state confrontate separatamente. Non è un listino in tempo reale.
