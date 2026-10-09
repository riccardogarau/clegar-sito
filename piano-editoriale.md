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

Pubblicato un articolo, si segna `[x]` e si aggiunge la data.

## Arretrato

### Operational Excellence — 2 articoli pubblicati
- [x] La classificazione del tempo nave: chi paga la giornata in cui non si è lavorato — 2026-10-05
- [x] Readiness review: che cosa si verifica prima che la nave parta — 2026-10-05
  *(tratta persone, documenti, permessi, interfacce e contingenze. La verifica
  della strumentazione in banchina resta all'articolo sull'accettazione della
  mobilitazione, che quindi non si sovrappone.)*
- [ ] Le lessons learned che nessuno rilegge, e come si scrive una nota che verrà usata

### Owner's Engineering — 1 articolo pubblicato
- [x] Il witnessing di una calibrazione: che cosa si firma e che cosa si guarda — 2026-10-08
  *(tratta il patch test di roll e il residuo della passata di conferma: la
  verifica a tappeto della mobilitazione resta alla voce successiva, che
  quindi non si sovrappone.)*
- [ ] L'accettazione della mobilitazione, voce per voce
- [ ] Che cosa decide in giornata un rappresentante a bordo

### Technical Advisory & Assurance — 1 articolo pubblicato
- [x] La seconda opinione prima di firmare un'accettazione — 2026-10-09
  *(tratta la velocità di conversione di una mappa di spessori, tarata sui CPT.
  La due diligence su un dataset ereditato resta alla voce successiva, che
  quindi non si sovrappone, purché non riprenda la taratura sui dati geotecnici.)*
- [ ] Due diligence su un dataset che arriva insieme all'asset
- [ ] Il parere tecnico in una controversia: che cosa lo rende utilizzabile

### Marine Geoscience — 2 articoli pubblicati
- [ ] Spaziatura delle linee: che cosa non si vede fra una linea e l'altra
- [ ] Un profilo di velocità del suono scaduto, e come si riconosce dai dati

### Project Management — 1 articolo pubblicato
- [ ] Le interfacce fra contractor: dove si rompono e chi le tiene

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
