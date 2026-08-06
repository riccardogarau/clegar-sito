# CLEGAR — sito web

Sorgenti del sito www.clegar.it. Il sito finito sta in `docs/`.

## Primo avvio

```bash
pip install -r requirements.txt
python build.py
python check.py
```

## Uso quotidiano

| Cosa | Comando |
|---|---|
| Ricostruire tutto | `python build.py` |
| Verificare prima di pubblicare | `python check.py` |
| Rigenerare le figure degli articoli | `python build.py --figures` |
| Guardare il risultato | aprire `ANTEPRIMA-locale.html` |

## Pubblicare

```bash
git add -A && git commit -m "descrizione" && git push
```

GitHub Pages pubblica la cartella `docs/` del branch `main`.

Le convenzioni del progetto e le regole da non violare sono in `CLAUDE.md`.
