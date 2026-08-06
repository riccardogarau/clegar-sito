# CLEGAR — sito

Sito bilingue (IT/EN) di CLEGAR S.r.l., consulenza indipendente per progetti
marini e offshore. Generato da script Python, pubblicato su GitHub Pages
all'indirizzo **www.clegar.it**.

Repo: `riccardogarau/clegar-sito`, branch `main`.
Questa cartella contiene **sorgenti e sito insieme**: i sorgenti alla radice,
il sito compilato in `docs/`, che è la cartella pubblicata da Pages.

---

## Comandi

```bash
python build.py             # costruisce docs/ + ANTEPRIMA-locale.html
python build.py --check     # costruisce e lancia la verifica strutturale
python build.py --figures   # rigenera anche le figure degli articoli
python check.py             # verifica strutturale — SEMPRE prima di pubblicare
```

`docs/` è **output**: viene cancellata e ricostruita a ogni build. Non
modificarla mai a mano — qualsiasi correzione fatta lì sparisce alla build
successiva. Si modifica il sorgente e si ricostruisce.

---

## Ciclo di lavoro obbligatorio

Ogni modifica al sito segue questi passi, senza saltarne nessuno:

1. Modificare il **sorgente** (`content/site2.html`, `articles.py`,
   `build_static.py`, `assets/`), mai `docs/`.
2. `python build.py --check` — deve finire con "Nessun problema strutturale".
3. Rileggere il diff di `docs/` per verificare che l'effetto sia quello
   voluto e nient'altro sia cambiato.
4. Commit e push su `main`.
5. GitHub Pages ripubblica in un paio di minuti.

**Commit e push a ogni modifica completata**, senza aspettare che vengano
chiesti: il sito online deve restare allineato con il repo. Un commit per
modifica logica, messaggio in italiano che dice *cosa cambia per chi legge il
sito*, non quale file è stato toccato.

Se `check.py` fallisce, si corregge e si ricostruisce: **non si pubblica mai
una build che non passa la verifica**.

---

## Struttura

```
build.py            punto di ingresso (build + anteprima + check)
build_static.py     generatore del sito (18 pagine)
build_preview.py    assembla docs/ in un file unico di anteprima
articles.py         contenuto degli articoli Insights (IT + EN)
check.py            verifica strutturale
content/
  site2.html        SORGENTE dei contenuti delle pagine fisse
  fig_art_*.svg     figure degli articoli
assets/             sorgenti: immagini, site.js, og.png
tools/figures/      script che generano le figure (dati sintetici)
docs/               OUTPUT — pubblicato da GitHub Pages
```

**`content/site2.html` è il sorgente dei contenuti**, non una pagina servita.
`build_static.py` ne estrae le `<section id="page-*">` e le impagina.
Per cambiare il testo di una pagina fissa si modifica lì.

In `assets/` convivono i nomi sorgente e i nomi pubblicati: `logo-positive.png`
→ `logo.png`, `logo-reversed.png` → `logo-white.png`, `mk_s.png` → `mark.png`.
La corrispondenza è nella tabella in testa a `build_static.py`.

---

## Regole da non violare

Ognuna di queste nasce da un difetto realmente verificatosi. Rompendole si
riapre un problema già risolto.

### Bilinguismo
- Ogni testo esiste due volte, in elementi gemelli con `class="it"` e
  `class="en"`, **stesso tag e stesso genitore**. Il generatore rimuove
  l'altra lingua; se manca il gemello, quel testo compare in entrambe.
- Vale anche dentro gli SVG: i `<text>` delle figure sono duplicati allo
  stesso modo.
- Un articolo si pubblica **solo quando esistono entrambe le lingue**,
  altrimenti `hreflang` punta a una pagina inesistente.

### Navigazione e URL
- Slug italiani per le pagine IT, inglesi per le EN
  (`/geoscienze-marine/` ↔ `/en/marine-geoscience/`).
- Il menu ha 8 voci: sotto i 1001 px scorre orizzontalmente, sopra viene
  compattato da due media query. Aggiungendo una nona voce **rimisurare**:
  a 1024 px l'ultima voce spariva.

### Rilevamento lingua
- Redirect automatico **solo sulla home italiana** (`docs/index.html`),
  mai sulle pagine interne. Se lo si mettesse ovunque, Googlebot — che
  scansiona dagli Stati Uniti — non indicizzerebbe più le pagine italiane.
- Usa il fuso orario (`Europe/Rome`) e la lingua del browser: nessuna
  chiamata di rete, nessun dato inviato a terzi.
- La scelta manuale (localStorage `clegar_lang`) vince sempre.

### Figure
- Le figure raster hanno un overlay SVG allineato al pixel: se si cambia
  la dimensione dell'immagine va cambiato anche il `viewBox`.
- **Mai** un attributo `transform` su un elemento con classe animata
  (`ship`, `sweep`, `draw`): il CSS lo sovrascrive e l'elemento finisce
  fuori dall'inquadratura. `check.py` lo verifica.
- Su mobile le figure entrano nello schermo e si aprono a schermo intero
  al tocco. Non reintrodurre lo scorrimento orizzontale: era stato
  provato e produceva figure larghe il triplo dello schermo.
- Dentro una figura tutto il contenuto parte dallo stesso bordo interno
  (x = 0 nel sistema del viewBox).
- I dataset delle figure sono **sintetici**. Ogni didascalia lo dichiara
  ("dataset dimostrativo" / "illustrative dataset"). Non rimuovere quella
  nota finché non ci sono dati reali: il sito vende verifica indipendente.

### Privacy e analytics
- Google Analytics (`G-XL4B4Y4DY1`) è in `assets/site.js`, riga `GA_ID`.
  **Un solo punto di configurazione.**
- Il tracciamento parte **solo dopo il consenso esplicito**: il Garante
  Privacy italiano lo richiede. Non sostituire con lo snippet standard di
  Google, che traccia da subito.

### Testo
- I trattini fra parole sono en dash (–), non em dash (—). I trattini
  interni alle parole composte (`close-out`, `meteo-marini`) restano
  trattini semplici.
- Registro impersonale, "voi" professionale, mai il "tu".

---

## Divisione del lavoro fra modelli

Il lavoro su questo sito è organizzato come **un orchestratore Opus 5 con una
squadra di agenti Sonnet 5** (tipicamente da 4 a 6, secondo la mole del
lavoro). La regola generale: Sonnet 5 produce, Opus 5 decide e verifica.

### Opus 5 — orchestratore

Non delega e svolge di persona:

- La **scomposizione del lavoro**: capire cosa ha chiesto l'utente,
  dividerlo in incarichi indipendenti, assegnarli, ricomporre i risultati.
- Le **modifiche architetturali**: `build_static.py`, `build_preview.py`,
  `check.py`, la struttura di navigazione, gli URL, il rilevamento lingua,
  la pipeline delle figure, lo schema dei dati strutturati e SEO.
- Il **debug** di qualsiasi problema che attraversi più file o che un agente
  non abbia risolto al primo tentativo.
- Le **decisioni di contenuto**: tono, posizionamento, cosa il sito afferma
  sull'azienda. Non si delegano a un agente.
- Il **controllo finale prima di pubblicare**, che non è mai delegabile:
  1. `python build.py --check` eseguito da lui;
  2. lettura del diff completo di `docs/`;
  3. verifica che i gemelli `.it`/`.en` esistano per ogni testo nuovo;
  4. solo allora commit e push.

Opus 5 risponde di tutto ciò che finisce online. Un agente che dichiara
"fatto" non è una verifica: la verifica è il punto 4 qui sopra.

### Sonnet 5 — agenti esecutori

Ricevono incarichi circoscritti, meccanici, verificabili:

- Traduzioni IT↔EN e creazione dei gemelli linguistici mancanti.
- Stesura e revisione del corpo degli articoli in `articles.py`.
- Ritocchi CSS, spaziature, responsive, correzioni di refusi.
- Aggiornamento di testi ripetitivi su più pagine (contatti, footer, meta
  description, titoli SEO).
- Controlli a tappeto: link rotti, `alt` mancanti, en dash usate male,
  didascalie senza la nota "dataset dimostrativo".
- Ricerche nel codice e nei contenuti quando serve capire dov'è una cosa.

### Come si assegna un incarico a un agente

Ogni incarico deve essere autoconsistente, perché l'agente parte senza il
contesto della conversazione. Va sempre indicato:

- il percorso esatto dei file da toccare;
- che **non deve mai modificare `docs/`**;
- la regola specifica di questo file che l'incarico deve rispettare
  (es. "ogni testo nuovo ha il gemello `.it`/`.en` nello stesso genitore");
- che **non deve committare né pushare**: al git ci pensa l'orchestratore
  dopo la verifica.

Agenti che lavorano su file diversi girano in parallelo. Agenti che
toccherebbero lo stesso file vanno messi in sequenza, altrimenti si
sovrascrivono a vicenda.

---

## Pubblicare un articolo

1. Aggiungere un blocco in testa a `ARTICLES` in `articles.py`
   (copiare quello esistente): `id`, `date`, `slug` IT/EN, `title`,
   `meta_title`, `desc`, `abstract`, `body` IT/EN.
2. `python build.py --check`
3. Aprire `ANTEPRIMA-locale.html` e controllare a occhio.
4. Commit e push: GitHub Pages ripubblica in un paio di minuti.
5. Reinviare la sitemap in Google Search Console.

Il `body` è HTML. Classi utili già disponibili: `.lede` (paragrafo di
apertura), `.callout` (riquadro con barra teal), `.flist` (elenco
numerato con descrizioni). I segnaposto `FIG_ORIGIN` e `FIG_LINES`
inseriscono le due figure esistenti.

---

## Da completare

- **Form contatti**: `FORM_ENDPOINT` in `assets/site.js` è vuoto, quindi il
  pulsante apre il client di posta. Su GitHub Pages serve Formspree o
  Web3Forms — il PHP non gira.
- **Informativa privacy**: manca la pagina richiesta dal GDPR (titolare,
  finalità, base giuridica, diritti). Il banner cookie da solo non basta.
- **LinkedIn**: il link nel footer e nei contatti è ancora `#`.
