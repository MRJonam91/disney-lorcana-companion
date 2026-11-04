# Disney Lorcana · Guida della community

[![Licenza: MIT](https://img.shields.io/badge/Licenza-MIT-yellow.svg)](LICENSE)
[English](README.en.md) · [Portale multilingua](index.html)

Companion statico non ufficiale per imparare a giocare a Disney Lorcana.
Apri **[il portale web](index.html)** oppure la
**[guida italiana](guide/guida-lorcana-it.html)**: trovi regole, glossario
ricercabile, segnapunti per due giocatori e calcolatore del mulligan.

**Stato:** sito utilizzabile offline; traduzioni parziali e contenuti storici
da verificare. Le vecchie statistiche sui tornei, i prezzi, le rarità e le
liste dei mazzi non costituiscono un dataset corrente validato. Consulta
[fonti e limiti del modello](docs/source-status.md) e le
[risorse ufficiali](https://disneylorcana.com/en/resources/) per regole e carte.

## Avvio e uso

Non serve installare o compilare nulla: apri `index.html` in un browser
moderno, anche su telefono. Ogni guida è un singolo file HTML scaricabile.
Nessun account, backend, font remoto o libreria CDN. Lettura e indice sono
disponibili senza JavaScript; glossario interattivo, punteggi e calcolatore
richiedono JavaScript. I punteggi si azzerano ricaricando la pagina.
I link alle fonti esterne e alla documentazione su GitHub richiedono rete.

Il calcolatore usa il modello ipergeometrico: probabilità di trovare almeno
una carta utile, conservando i bersagli trovati e considerando il
rimescolamento dopo il mulligan. Non esegue simulazioni e non calcola combo.
Gli input non validi mostrano un messaggio e nessuna percentuale.

## Sviluppo e verifiche

Server locale facoltativo, con Python 3:

```sh
python -m http.server 8765 --bind 127.0.0.1
```

Apri `http://127.0.0.1:8765`. Per i controlli servono Python 3.10+ e Node.js 22+:

```sh
python tools/check_site.py
node --test tools/odds.test.cjs
python tools/run_git_workflow.py
```

L'ultimo comando legge soltanto lo stato del checkout attuale: non cambia
identità Git, branch, commit o merge. La CI verifica pagine, link, ancore,
label, dipendenze offline e probabilità nelle cinque guide. Verifica anche
nel browser schermi stretti, tastiera, ricerca senza risultati, vittoria e
reset, input non validi e lettura offline senza JavaScript.

CSS e JavaScript sono incorporati nelle cinque guide per mantenerle
scaricabili come singoli file. Mantieni sincronizzate le correzioni: il
controllo automatico rileva divergenze tra gli script. Non ci sono
dipendenze di produzione da installare.

## Documentazione e community

- [Regole](docs/rules/complete-rules.it.md), [strategia](docs/strategy/mulligan-and-math.it.md), [glossario](docs/glossary/glossary.it.md)
- [Contribuire](CONTRIBUTING.md), [condotta](CODE_OF_CONDUCT.md), [supporto](SUPPORT.md)
- [Sicurezza](SECURITY.md), [changelog](CHANGELOG.md)
- [Discussioni GitHub](https://github.com/MRJonam91/disney-lorcana-companion/discussions), se abilitate

## Licenza e attribuzioni

I contributi originali mantengono la [licenza MIT](LICENSE) preesistente.
Consulta [NOTICE](NOTICE), [avvisi di terze parti](THIRD_PARTY_NOTICES.md) e
[provenienza degli asset](ASSETS.md). Marchi, personaggi, nomi e testi delle
carte restano dei rispettivi titolari. La licenza software non concede
questi diritti. Il progetto non è affiliato, approvato o sponsorizzato da
Disney o Ravensburger.

## Sostieni il progetto

Se il progetto ti è utile, puoi sostenerne la manutenzione tramite
[GitHub Sponsors](https://github.com/sponsors/MRJonam91),
[Ko-fi](https://ko-fi.com/mrjonam),
[Buy Me a Coffee](https://buymeacoffee.com/mrjonam) o
[PayPal](https://paypal.me/manorollo).
Il supporto è volontario e non attribuisce licenze o diritti aggiuntivi.
