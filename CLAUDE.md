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
build_static.py     generatore del sito (22 pagine)
build_preview.py    assembla docs/ in un file unico di anteprima
articles.py         contenuto degli articoli Insights (IT + EN)
check.py            verifica strutturale
content/
  site2.html        SORGENTE dei contenuti delle pagine fisse
  fig_art_*.svg     figure degli articoli
assets/             sorgenti: immagini, site.js, og.png
tools/figures/      script che generano le figure
.github/workflows/  pages.yml: pubblica docs/ su GitHub Pages
docs/               OUTPUT — pubblicato da GitHub Pages
```

Le pagine sono 22: otto voci di menu in due lingue, `/privacy/` fuori dal
menu in due lingue, e due articoli in due lingue. `check.py` le conta e
confronta il totale con gli URL della sitemap: se non coincidono, fallisce.

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
  trattini semplici. Fa eccezione il trattino che separa marchio e
  descrizione — titolo delle pagine, `alt` del logo, oggetto delle email
  — che resta em dash: lì non separa parole di una frase.
- Registro impersonale, "voi" professionale, mai il "tu".
- Le sei fasi di progetto si chiamano **Requisiti**, Gara, Mobilitazione,
  Acquisizione, Processing, Accettazione. La prima non è "Specifica":
  quello è un documento, mentre le altre cinque sono attività, e il
  criterio di accettazione — metà dell'argomento — spesso nella specifica
  tecnica non c'è. "Specifiche tecniche" resta corretto dove nomina un
  deliverable prodotto da CLEGAR.
- Attenzione ai calchi dall'inglese: `dispositare` non è italiano.

### Contenuto tecnico
- **Ogni numero pubblicato va ricalcolato**, non riletto. Nella tabella
  delle soglie del secondo articolo un valore era troncato invece che
  arrotondato: 0,79 al posto di 0,80. Su un sito che vende verifica
  indipendente, un errore aritmetico costa più di dieci refusi.
- **Ogni affermazione tecnica va difesa dall'obiezione più ovvia.** Le
  differenze agli incroci in aree ad alta pendenza sono gonfiate
  dall'incertezza orizzontale: attribuirle alla mobilità del fondale senza
  dirlo lasciava all'articolo una presa che un contractor avrebbe usato.
- **Le figure non anticipano conclusioni che il testo raggiunge dopo.**
  L'etichetta "il fondale si è mosso" è stata tolta proprio per questo.

### Pubblicazione
Pubblica `.github/workflows/pages.yml`, un workflow nostro: la
pubblicazione automatica di GitHub non è un file del repo e quindi non si
può configurare. Tre modi diversi di fallire, tutti verificatisi, tutti
diagnosticati male al primo colpo:

- **Un solo `CNAME` nel repo**, quello che `build_static.py` scrive in
  `docs/`. Quando ce n'era anche uno nella radice, la build falliva senza
  dire perché.
- **Un trigger alla volta.** Push, cambi di impostazione e ricostruzioni
  forzate avviano ciascuno un deploy. Con `cancel-in-progress: false` non
  si annullano più a vicenda, ma restano in coda: si pusha una volta sola
  e si aspetta.
- **Il timeout del passo di pubblicazione.** Il valore predefinito di
  `actions/deploy-pages` è dieci minuti; quando la coda di GitHub è lenta
  non bastano, e l'azione si arrende scrivendo "Timeout reached, aborting"
  e "Canceling Pages deployment". Sembra un guasto del sito e non lo è: la
  build è già riuscita e l'artefatto è pronto. Nel workflow il timeout sta
  a trenta minuti.

Distinguere i tre casi conta, perché la cura è diversa: il primo si
corregge nel repo, il secondo aspettando, il terzo rilanciando lo stesso
workflow senza toccare niente. **Non mettere mano al codice per un guasto
che nel codice non c'è.**

La diagnosi non sta mai nell'API di Pages, che risponde solo "Page build
failed", ma nei log: `gh run list` e `gh run view <id> --log-failed`.

E soprattutto: **lo stato del workflow non è la verità**. Un run può
chiudersi in rosso mentre il sito è aggiornato, e viceversa. Si verifica
scaricando la pagina vera e cercandoci dentro la modifica.

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

Se il corpo arriva in Markdown, la conversione è un incarico da agente:
è meccanica e verificabile. Ma va verificata contando gli elementi nelle
due lingue, che devono corrispondere uno a uno.

Il `body` è HTML. Classi disponibili:

| Classe | A cosa serve |
|---|---|
| `.lede` | paragrafo di apertura |
| `.callout` | riquadro con barra teal |
| `.flist` | elenco numerato con descrizioni, `<span class="k">01</span>` |
| `.tablewrap` | **obbligatorio** attorno a ogni `<table>` |
| `.pull` | il numero che l'articolo mette in discussione |
| `.num` | celle numeriche: mono, allineate a destra |

**Ogni tabella va avvolta in `.tablewrap`.** Senza, su uno schermo stretto
spinge di lato l'intera pagina — è l'unico elemento del sito capace di
farlo, e la regola è che non succeda mai. Le celle numeriche prendono
`class="num"` anche nell'intestazione: incolonnate in monospaziato si
confrontano, in proporzionale no.

I segnaposto delle figure sono `FIG_ORIGIN`, `FIG_LINES`, `FIG_TVU` e
`FIG_MAP`, definiti in testa a `articles.py` e mappati su file e didascalie
in `FIG_SVG` dentro `build_static.py`. Per aggiungerne uno: costante in
`articles.py`, generatore in `tools/figures/gen_article_figs.py`, il nome
del file in `build.py` fra quelli spostati in `content/`, e la voce in
`FIG_SVG` con le due didascalie.

In fondo a ogni articolo il generatore aggiunge da solo il blocco di
condivisione: LinkedIn ed Email sono link normali e il terzo pulsante usa
le API del browser. **Nessun widget di terze parti**, che caricherebbe un
SDK di tracciamento prima del consenso.

---

## assets/site.js

Un solo file, una sola funzione avvolgente, blocchi indipendenti dentro.
**Ogni blocco che può non trovare il proprio elemento in pagina deve stare
in una funzione propria.** Il modulo contatti esiste su una pagina sola e
comincia con `if (!send) return;`: finché quel `return` usciva dalla
funzione esterna, su ogni altra pagina zittiva tutto il codice scritto
dopo. Il primo tentativo di aggiungere la condivisione non funzionava per
questo, e la sintassi era valida — si scopre solo provando in pagina.

Il modulo contatti passa da **Web3Forms**. `FORM_ENDPOINT` e
`WEB3FORMS_KEY` sono le uniche due costanti da toccare per cambiare
fornitore. La chiave sta nel sorgente ed è visibile: per Web3Forms è un
alias dell'indirizzo email, non una credenziale. Sul piano gratuito non è
legata al dominio, quindi chi la copia può scrivere alla casella: contro
questo restano il loro firewall e la trappola `#f-hp` del modulo.

---

## Da completare

- **Sede legale nell'informativa**: c'è la sola città. L'articolo 13 del
  GDPR chiede gli estremi del titolare, e la prassi è via, civico e CAP.
- **DPA con Web3Forms**: non ne risulta uno pubblicato. Per un modulo
  contatti B2B senza categorie particolari di dati è un rischio accettato
  consapevolmente, non una svista.
- **Repo pubblico**: su GitHub Pages con account gratuito è obbligatorio.
  Con repo privato servono GitHub Pro, oppure Cloudflare Pages o Netlify,
  che sono gratuiti e pubblicano in secondi invece che in minuti.
- **Pagina strumenti**: prevista in `/strumenti/`, fuori dal menu, per il
  tool di ascolto dei dati SEG-Y. Se diventerà un prodotto in vendita
  servirà una nona voce di menu, e a quel punto **rimisurare** le due
  media query fra 1001 e 1120 px.
