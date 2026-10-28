# Piano editoriale Insights

Tre articoli a settimana: lunedì, mercoledì e venerdì. Il compito pianificato
`articolo-insights` parte alle **10:00** (ora di Roma) di quei giorni, prepara
l'articolo nelle due lingue e lo sottopone in chat. **Non si pubblica senza il
via libera**, e si pubblica appena il via libera arriva.

## Come si sceglie il prossimo

Si prende il primo argomento non pubblicato della linea di servizio che ha
**meno articoli**, non la prima voce dell'elenco. Il motivo è che una pagina di
servizio senza articoli resta fuori dalla rete di collegamenti interni e non
riceve niente dagli Insights: finché una linea è a zero, un secondo articolo
su una linea già coperta rende meno.

A parità di articoli pubblicati vince l'ordine in cui le linee sono elencate
qui sotto. L'8 ottobre 2026 la regola scritta prima diceva "il primo
argomento in ordine" e avrebbe dato un terzo articolo a Operational
Excellence mentre due linee erano ancora a zero: la lettera contraddiceva il
motivo, e ha vinto il motivo.

**Ogni articolo è nuovo.** Prima di scrivere si rileggono i titoli e i corpi
di quelli già in `articles.py`: non basta un titolo diverso, perché un
argomento è già coperto anche quando coincidono il meccanismo tecnico,
l'esempio lavorato o la tesi. In quel caso si salta alla voce successiva e si
annota qui perché. Citare e linkare un articolo pubblicato va bene; rifarlo no.

Già online, da non riprendere:

| Articolo | Linea | Di che cosa parla già |
|---|---|---|
| Che cosa facciamo | — | presentazione, indipendenza |
| Il controllo agli incroci | Marine Geoscience | differenze agli incroci, TVU S-44, mobilità del fondale |
| Quando il critical path si sposta | Project Management | float, near-critical, weather allowance, recupero di schedule |
| Il problema del datum | Marine Geoscience | ETRS89 / WGS84, realizzazioni, epoche, codici EPSG |
| La classificazione del tempo nave | Operational Excellence | off-hire e on hire, weather standby contro guasto, categorie del rapporto giornaliero |
| Readiness review prima della partenza | Operational Excellence | margine delle voci aperte contro percentuale di chiusura, riapertura su revisione del documento, partenza condizionata |
| Il witnessing di una calibrazione | Owner's Engineering | patch test di roll, passata di conferma e residuo, convenzione di segno, roll contro velocità del suono |
| La seconda opinione prima dell'accettazione | Technical Advisory | QC del contractor contro assunzioni, velocità di conversione tempo-profondità nei sedimenti, taratura sui CPT, classificazione del tracciato rispetto a una soglia |
| L'accettazione della mobilitazione, voce per voce | Owner's Engineering | riferimento indipendente e più preciso della tolleranza, errore costante invisibile agli incroci, bordo libero comune a multibeam e single-beam, volume di dragaggio, rimisurare finché passa |
| Due diligence su un dataset ereditato | Technical Advisory | copertura del cavo come differenza fra quota del cavo e fondale mobile, sand wave, quote assolute nel data room, costante verticale fra due rilievi, incertezza in pianta sui fianchi |
| Le interfacce fra contractor | Project Management | contratti separati, Rev A contro dati definitivi, ciclo di revisione come durata, date contrattuali contro date dei programmi, registro delle interfacce tenuto dal committente |
| Le lessons learned che si usano | Operational Excellence | lezione come percentuale contro parametro, tempo in linea più line turn, run-in del towfish, production rate scomposta in gara, posto della nota nel modello di stima |
| Che cosa decide in giornata il rappresentante a bordo | Owner's Engineering | perdita delle correzioni di posizionamento, rifare subito contro attendere il post-processing, costo del ritorno che cresce con la distanza, osservazioni grezze come condizione del recupero, scadenza legata alla posizione della nave, confine fra decisioni di bordo e di terra |
| Il parere tecnico in una controversia | Technical Advisory | measured mile, perdita di produttività di un aratro, scelta del tratto di riferimento, differenza di terreno contro evento contestato, controllo incrociato sulle ore di fermo, incertezze con il loro verso, IBA Rules art. 5.2, confine fra fatto tecnico e responsabilità |
| La spaziatura delle linee | Marine Geoscience | ombra del side scan e distanza dalla linea, striscia sotto la linea con copertura al 100%, spaziatura sopra e sotto la portata, multibeam come copertura della striscia, criterio di riconoscimento in gara, feature detection contro feature search in S-44 |
| Dove i path paralleli si incontrano | Project Management | merge bias, probabilità della milestone come prodotto delle probabilità dei path, float che non misura la coda della durata, dipendenza fra path per il meteo, predecessori ridotti al blocco che serve, GAO-16-89G |

Pubblicato un articolo, si segna `[x]` e si aggiunge la data.

## Arretrato

### Operational Excellence — 3 articoli pubblicati
- [x] La classificazione del tempo nave: chi paga la giornata in cui non si è lavorato — 2026-10-05
- [x] Readiness review: che cosa si verifica prima che la nave parta — 2026-10-05
  *(tratta persone, documenti, permessi, interfacce e contingenze. La verifica
  della strumentazione in banchina resta all'articolo sull'accettazione della
  mobilitazione, che quindi non si sovrappone.)*
- [x] Le lessons learned che nessuno rilegge, e come si scrive una nota che verrà usata — 2026-10-19
  *(l'esempio sono le durate di acquisizione e i line turn di un sistema
  trainato: non riprende la classificazione del tempo nave, che riguarda chi
  paga una giornata, né la readiness review.)*

### Owner's Engineering — 3 articoli pubblicati
- [x] Il witnessing di una calibrazione: che cosa si firma e che cosa si guarda — 2026-10-08
  *(tratta il patch test di roll e il residuo della passata di conferma: la
  verifica a tappeto della mobilitazione resta alla voce successiva, che
  quindi non si sovrappone.)*
- [x] L'accettazione della mobilitazione, voce per voce — 2026-10-12
  *(l'esempio è verticale – immersione dei trasduttori – perché la verifica di
  posizione su un punto noto in mobilitazione era già nell'articolo sul datum.)*
- [x] Che cosa decide in giornata un rappresentante a bordo — 2026-10-21
  *(l'esempio è un tratto di linea senza correzioni di posizionamento e la
  scelta fra rifarlo e attendere il post-processing. Non riprende la
  classificazione del tempo nave, che riguarda chi paga le ore, né il
  witnessing o l'accettazione della mobilitazione, che si fanno in banchina.)*

### Technical Advisory & Assurance — 3 articoli pubblicati
- [x] La seconda opinione prima di firmare un'accettazione — 2026-10-09
  *(tratta la velocità di conversione di una mappa di spessori, tarata sui CPT.
  La due diligence su un dataset ereditato resta alla voce successiva, che
  quindi non si sovrappone, purché non riprenda la taratura sui dati geotecnici.)*
- [x] Due diligence su un dataset che arriva insieme all'asset — 2026-10-14
- [x] Il parere tecnico in una controversia: che cosa lo rende utilizzabile — 2026-10-23
  *(l'esempio è una richiesta per perdita di produttività di un aratro, con il
  measured mile e la scelta del tratto di riferimento. Non riprende la seconda
  opinione, che riguarda le assunzioni di un'interpretazione, né la
  classificazione del tempo nave, che riguarda chi paga una giornata.)*

### Marine Geoscience — 3 articoli pubblicati
- [x] Spaziatura delle linee: che cosa non si vede fra una linea e l'altra — 2026-10-26
  *(pubblicato come "la striscia in cui un masso non si vede": l'esempio è
  l'ombra del side scan che si accorcia vicino alla linea. Non riprende il
  crossline check, che riguarda l'accordo verticale agli incroci, né il
  witnessing, che riguarda il roll sui fasci esterni.)*
- [ ] Un profilo di velocità del suono scaduto, e come si riconosce dai dati
  *(attenzione: il witnessing spiega già che un errore di velocità del suono
  incurva i bordi dello swath e si distingue dal roll con passate reciproche.
  Va impostato su un altro meccanismo o un altro esempio, non rifatto.)*

### Project Management — 3 articoli pubblicati
- [x] Le interfacce fra contractor: dove si rompono e chi le tiene — 2026-10-16
  *(tratta la stessa parola con due significati in due contratti separati. Non
  si sovrappone alla readiness review, che riapre una voce chiusa su una
  revisione di documento, né al critical path, che riguarda il meteo.)*
- [x] Dove i path paralleli si incontrano: la probabilità di una milestone — 2026-10-28
  *(aggiunto il 2026-10-28: Project Management era la linea con meno articoli
  e non aveva voci in arretrato. L'esempio è il merge bias – tre path
  all'80% che danno una milestone al 56% – e il float che non misura la coda
  della durata. Non riprende il critical path, che è deterministico e
  riguarda quale path vincola quando cambia l'assunzione sul meteo.)*

## Che cosa si consegna per ogni articolo

Tre cose, non una: il testo italiano, il testo inglese, e il **post LinkedIn
nelle due lingue** in `post-linkedin.md`. Un articolo senza post resta senza
lettori, perche' il profilo LinkedIn e' l'unico canale di distribuzione del
sito. Su LinkedIn pubblica l'utente, non il generatore: il post va solo
preparato e lasciato pronto da copiare.

## Regole di contenuto

Valgono quelle di `CLAUDE.md`, in particolare: ogni numero va **ricalcolato**,
non riletto; i dataset degli esempi sono sintetici e la didascalia lo dichiara;
ogni affermazione tecnica va difesa dall'obiezione più ovvia; e ogni articolo
dichiara il proprio `topic`, altrimenti resta isolato dalla rete di link.
