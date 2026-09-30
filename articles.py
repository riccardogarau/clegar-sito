# -*- coding: utf-8 -*-
"""Contenuto degli articoli Insights.

Ogni articolo esiste in entrambe le lingue. Per aggiungerne uno nuovo,
copiare la struttura e aggiungerlo in testa alla lista ARTICLES
(l'ordine della lista è l'ordine di pubblicazione, dal più recente).
"""

FIG_ORIGIN = '__FIG_ORIGIN__'
FIG_LINES = '__FIG_LINES__'
FIG_TVU = '__FIG_TVU__'
FIG_MAP = '__FIG_MAP__'
FIG_WORK = '__FIG_WORK__'
FIG_SWAP = '__FIG_SWAP__'

ARTICLES = [
    {
        'id': 'datum-etrs89-wgs84',
        'topic': 'geoscience',
        'date': '2026-08-31',
        'slug': {'it': 'etrs89-e-wgs84-il-problema-del-datum',
                 'en': 'etrs89-and-wgs84-the-datum-problem'},
        'title': {
            'it': 'Il problema del datum: ETRS89 e WGS84 non sono la stessa coordinata',
            'en': 'The datum problem: ETRS89 and WGS84 are not the same coordinate',
        },
        'meta_title': {
            'it': 'Il problema del datum: ETRS89 e WGS84 | Insights',
            'en': 'The datum problem: ETRS89 and WGS84 | Insights',
        },
        'desc': {
            'it': ('Perché un deliverable in ETRS89 caricato in un progetto WGS84 sbaglia di quasi '
                   'un metro, perché nessun software lo segnala, e come si verifica con un punto noto.'),
            'en': ('Why a deliverable in ETRS89 loaded into a WGS84 project is nearly a metre out, '
                   'why no software flags it, and how one known point detects it.'),
        },
        'abstract': {
            'it': ('Due sistemi che sembrano dire la stessa cosa, e che dal 1989 si separano di '
                   '2,5 cm all’anno. La differenza è sistematica, prevedibile e verificabile con '
                   'una sottrazione – eppure resta uno degli errori più ricorrenti nei deliverable '
                   'di rilievo.'),
            'en': ('Two systems that look like the same answer, drifting apart by 2.5 cm a year '
                   'since 1989. The difference is systematic, predictable and detectable with a '
                   'subtraction – and still one of the most routine errors in survey deliverables.'),
        },
        'body': {
            'it': """
<p class="lede">Non lo sono. Differiscono di quasi un metro, e la differenza è sistematica – stessa entità e stessa direzione in ogni punto del blocco. È uno dei pochi errori del lavoro di rilievo offshore che sia interamente prevedibile, interamente evitabile e ciononostante ancora ricorrente.</p>

<h2>Perché i due sistemi si allontanano</h2>

<p>ETRS89 è stato adottato da EUREF nella riunione di Firenze del 1990, con la Risoluzione 1, che lo definisce coincidente con l'International Terrestrial Reference System (ITRS) all'epoca 1989.0 e ancorato alla parte stabile della placca eurasiatica. È quest'ultima clausola a contenere tutta la questione. ETRS89 si muove con l'Europa. Un punto sul fondale al largo della costa olandese mantiene indefinitamente la stessa coordinata ETRS89, che è esattamente ciò che serve per il catasto, la cartografia nazionale e qualunque dataset debba restare confrontabile nell'arco di decenni. È il sistema di riferimento richiesto per i dati territoriali europei conformi alla direttiva INSPIRE.</p>

<p>WGS84 non funziona così. È il sistema di riferimento implicito nel GPS, mantenuto da NGA e allineato alle successive realizzazioni dell'ITRF – che è ancorato al centro di massa terrestre e non tiene ferma alcuna placca. La realizzazione attuale, WGS84 (G2296), è entrata in vigore a gennaio 2024, allineata a ITRF2020 e a IGS20, con un accordo con ITRF2020 entro circa 2 cm. È il settimo aggiornamento di questo tipo in trent'anni.</p>

<p>Quindi ETRS89 tiene ferma l'Europa mentre WGS84 la lascia muovere. La placca eurasiatica deriva verso nord-est a circa 2,5 cm all'anno, e i due sistemi si separano a quella velocità dal 1989.0:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th class="num">Epoca</th><th class="num">Anni dal 1989.0</th><th class="num">Separazione approssimativa</th></tr>
</thead>
<tbody>
<tr><td class="num">2000</td><td class="num">11 anni</td><td class="num">~25 cm</td></tr>
<tr><td class="num">2010</td><td class="num">21 anni</td><td class="num">~52 cm</td></tr>
<tr><td class="num">2020</td><td class="num">31 anni</td><td class="num">~78 cm</td></tr>
<tr><td class="num">2026</td><td class="num">37 anni</td><td class="num">~93 cm</td></tr>
</tbody>
</table>
</div>

<p>Il valore relativo al 2000 è documentato; i successivi discendono dal tasso di deriva. Entità e direzione esatte variano in qualche misura con la posizione in Europa, quindi la tabella va letta come ordine di grandezza, non come trasformazione.</p>

<h2>Perché nulla lo segnala</h2>

<p>Tre fattori concorrono a rendere silenzioso questo errore.</p>

<p><strong>Gli ellissoidi sono quasi identici.</strong> ETRS89 usa GRS80: semiasse maggiore 6378137 m, schiacciamento inverso 298,257222101. WGS84 usa un ellissoide con lo stesso semiasse maggiore, 6378137 m, e schiacciamento inverso 298,257223563. La differenza compare alla nona cifra significativa e si traduce in circa un decimo di millimetro sul semiasse minore. Qualunque controllo che confronti i parametri dell'ellissoide passerà. Il problema non è l'ellissoide: sono la realizzazione del datum e l'epoca.</p>

<p><strong>Non esistono parametri di trasformazione ufficiali.</strong> Le realizzazioni recenti di WGS84 sono allineate all'ITRF in modo sufficientemente stretto da essere trattate come coincidenti, quindi tra le due non è pubblicata alcuna trasformazione. Il software non ha dunque nulla da applicare, e spesso non applica nulla – in silenzio.</p>

<p><strong>"ETRS89" non è un singolo frame, è un ensemble.</strong> Nel registro EPSG, ETRS89 (EPSG:4258) è definito come un ensemble i cui membri vanno da ETRF89 a ETRF2020, con un'accuratezza dichiarata dell'ensemble pari a 0,1 m. Un deliverable etichettato semplicemente "ETRS89" è quindi specificato solo a circa 10 cm, prima ancora che si ponga qualsiasi questione riguardo a WGS84. Il Technical Working Group di EUREF raccomanda ETRF2000 come frame convenzionale; se la specifica non nomina una realizzazione, si sta accettando l'ensemble.</p>

<p>I sistemi proiettati ereditano tutto questo. EPSG:25831 è ETRS89 / UTM zona 31N. EPSG:32631 è WGS 84 / UTM zona 31N. Stessa proiezione, stesso meridiano centrale, stesso fattore di scala, stesso falso est. Datum diverso. Un'intestazione di file che riporti soltanto "UTM31N" non distingue né l'uno né l'altro.</p>

<h2>Un esempio pratico</h2>

<p>I valori riportati di seguito sono sintetici – costruiti per illustrare il meccanismo di errore, non tratti da progetti reali – ma il meccanismo è esatto.</p>

<p>Un rilievo UXO su un corridoio di cavo di esportazione di un parco eolico consegna una lista di target: 214 anomalie magnetiche, ciascuna con posizione, massa stimata e classe di confidenza. L'intestazione del deliverable riporta ETRS89 / UTM zona 31N. Il GIS di asset del cliente e lo spread ROV incaricato di rilocalizzare e identificare i target lavorano entrambi in WGS 84 / UTM zona 31N.</p>

<p>Nessuno trasforma nulla, perché entrambi sono "UTM31N".</p>

<p>Ogni posizione di target risulta ora spostata di circa 0,93 m verso sud-ovest rispetto a dove il ROV andrà a cercarla. Si consideri l'effetto sulla campagna di relocation:</p>

<ul>
  <li>Un'anomalia magnetica porta già con sé la propria incertezza posizionale – comunemente da uno a pochi metri, a seconda di quota di volo, spaziatura delle linee e inversione utilizzata. Lo scostamento di datum non si media con questa incertezza. Vi si somma, nella stessa direzione, su ogni target.</li>
  <li>Gli schemi di ricerca per la relocation sono dimensionati sull'incertezza attesa. Uno scostamento sistematico di 0,93 m consuma una quota rilevante di un raggio di ricerca previsto per il solo errore casuale.</li>
  <li>I target che non vengono rilocalizzati vengono riclassificati, riacquisiti o portati in escalation. Ognuna di queste risposte costa tempo ROV, e nessuna affronta la causa reale.</li>
</ul>

<p>La campagna non fallisce apertamente. Procede lenta, produce una percentuale di target non rilocalizzati superiore alle attese e genera una spiegazione plausibile ma sbagliata: che il rilievo magnetometrico originale fosse di scarsa qualità.</p>

<h2>La firma che lo identifica</h2>

<p>Un disallineamento di datum ha una firma che nessun altro errore del lavoro di rilievo riproduce: i residui sono <strong>costanti in entità e costanti in direzione</strong> su tutto il dataset.</p>

<p>Il rumore di posizionamento è casuale e tende a mediarsi a zero. Gli errori di marea o di riferimento verticale si manifestano in profondità, non in pianta. Gli errori di layback o di offset variano con la rotta, e cambiano quindi segno tra linee reciproche. Un disallineamento di giroscopio scala con la distanza dal punto di riferimento. Un disallineamento di datum non fa nulla di tutto ciò: sposta ogni cosa, ovunque, dello stesso vettore.</p>

<p>Questo lo rende banalmente verificabile, a condizione che qualcuno esegua la verifica. Si prenda un punto qualsiasi la cui posizione sia nota in modo indipendente – una struttura installata, un met mast, un target precedentemente verificato, un dataset sovrapposto di un altro contractor – e si calcoli il residuo. Se un pugno di punti di questo tipo mostra tutto lo stesso spostamento, nella stessa direzione, con entità prossima al metro, la risposta è un datum, non un difetto di rilievo.</p>

<h2>Cosa richiedere nella specifica</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Identificazione completa del CRS, tramite codice EPSG, per ogni deliverable.</strong><span class="t"> Non "WGS84", non "UTM31N". EPSG:25831 e EPSG:32631 sono due risposte diverse alla stessa descrizione informale.</span></span></li>
  <li><span class="k">02</span><span><strong>Realizzazione ed epoca, indicate esplicitamente.</strong><span class="t"> ETRF2000 all'epoca 2026.5 è una specifica. "ETRS89" è un ensemble con accuratezza di 0,1 m, e su un progetto che posiziona a livello centimetrico non è sufficiente.</span></span></li>
  <li><span class="k">03</span><span><strong>La trasformazione effettivamente applicata, con i suoi parametri, documentata nel report</strong><span class="t"> – incluso il caso in cui non ne sia stata applicata alcuna, con la relativa giustificazione.</span></span></li>
  <li><span class="k">04</span><span><strong>Un unico CRS di progetto, definito nel contratto prima della mobilitazione,</strong><span class="t"> con qualsiasi conversione da o verso di esso eseguita una sola volta, da un soggetto individuato, e registrata.</span></span></li>
  <li><span class="k">05</span><span><strong>Una verifica di datum in fase di mobilitazione,</strong><span class="t"> rispetto ad almeno una posizione nota in modo indipendente, con il residuo riportato come vettore e non come distanza. Uno scalare nasconde la direzione, e la direzione è ciò che identifica la causa.</span></span></li>
  <li><span class="k">06</span><span><strong>Definizioni di CRS contenute nelle intestazioni dei file,</strong><span class="t"> non in una email di accompagnamento. Le intestazioni dei formati P IOGP esistono proprio per questo; sono utili solo se vengono compilate correttamente e lette.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Quasi ogni altra fonte di errore in un deliverable di rilievo richiede un giudizio per essere valutata. Questa no. Il tasso di deriva è pubblicato, i sistemi di riferimento sono documentati, i codici EPSG non sono ambigui, e il test che lo rileva richiede un punto noto e una sottrazione.</p>

<p>Persiste perché "ETRS89" e "WGS84" sembrano entrambi la risposta alla domanda "quale datum?", e perché un metro è abbastanza piccolo da risultare invisibile in un plot d'insieme e abbastanza grande da contare ovunque il lavoro venga effettivamente svolto.</p>

<h3>Riferimenti</h3>

<ul>
  <li>EUREF, Risoluzione 1, Firenze 1990 – definizione di ETRS89.</li>
  <li>EUREF Technical Working Group – raccomandazione di adottare ETRF2000 come frame convenzionale di ETRS89.</li>
  <li>NGA, WGS 84 (G2296) – realizzazione in vigore da gennaio 2024, allineata a ITRF2020 e IGS20.</li>
  <li>Registro dei parametri geodetici IOGP/EPSG – EPSG:4258, EPSG:4326, EPSG:25831, EPSG:32631.</li>
  <li>Direttiva INSPIRE (2007/2/CE) – ETRS89 come sistema di riferimento per i dati territoriali europei.</li>
</ul>

<div class="callout">
  <p>CLEGAR fornisce QC indipendente e technical assurance su dataset geofisici per sviluppatori, contractor e asset owner dell'offshore. Se state redigendo la specifica di un rilievo, o state valutando un deliverable che avete ricevuto, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">They are not right. They differ by very nearly a metre, and the difference is systematic – the same magnitude and the same direction at every point in the block. This is one of the few errors in offshore survey work that is entirely predictable, entirely avoidable, and still routine.</p>

<h2>Why the two systems drift apart</h2>

<p>ETRS89 was adopted by EUREF at its 1990 meeting in Florence, following Resolution 1, which defined it as coincident with the International Terrestrial Reference System (ITRS) at epoch 1989.0 and fixed to the stable part of the Eurasian Plate. That last clause is the whole story. ETRS89 moves with Europe. A point on the seabed off the Dutch coast keeps the same ETRS89 coordinate indefinitely, which is exactly what you want for cadastral work, national mapping, and any dataset that has to remain comparable across decades. It is the reference frame mandated for INSPIRE-compliant European spatial data.</p>

<p>WGS84 does not work that way. It is the reference frame implicit in GPS, maintained by NGA, and aligned to successive realizations of the ITRF – which is anchored to the Earth's centre of mass and does not hold any single plate fixed. The current realization, WGS84 (G2296), became effective in January 2024, aligned to ITRF2020 and to IGS20, agreeing with ITRF2020 to within about 2 cm. It is the seventh such update in thirty years.</p>

<p>So ETRS89 holds Europe still while WGS84 lets it move. The Eurasian Plate drifts north-east at roughly 2.5 cm per year, and the two systems have been separating at that rate since 1989.0:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th class="num">Epoch</th><th class="num">Elapsed since 1989.0</th><th class="num">Approximate separation</th></tr>
</thead>
<tbody>
<tr><td class="num">2000</td><td class="num">11 years</td><td class="num">~25 cm</td></tr>
<tr><td class="num">2010</td><td class="num">21 years</td><td class="num">~52 cm</td></tr>
<tr><td class="num">2020</td><td class="num">31 years</td><td class="num">~78 cm</td></tr>
<tr><td class="num">2026</td><td class="num">37 years</td><td class="num">~93 cm</td></tr>
</tbody>
</table>
</div>

<p>The 2000 figure is documented; the later ones follow from the rate. The exact magnitude and bearing vary somewhat with position in Europe, so treat the table as the order of magnitude, not as a transformation.</p>

<h2>Why nothing warns you</h2>

<p>Three things conspire to make this error silent.</p>

<p><strong>The ellipsoids are nearly identical.</strong> ETRS89 uses GRS80: semi-major axis 6378137 m, inverse flattening 298.257222101. WGS84 uses an ellipsoid with the same semi-major axis, 6378137 m, and inverse flattening 298.257223563. The difference appears in the ninth significant figure and works out to roughly a tenth of a millimetre on the semi-minor axis. Any check that compares ellipsoid parameters will pass. The ellipsoid is not the problem; the datum realization and the epoch are.</p>

<p><strong>There are no official transformation parameters.</strong> Recent WGS84 realizations are aligned to ITRF closely enough that the two are treated as coincident, so no transformation is published between them. Software therefore has nothing to apply, and often applies nothing – silently.</p>

<p><strong>"ETRS89" is not one frame, it is an ensemble.</strong> In the EPSG registry, ETRS89 (EPSG:4258) is defined as an ensemble whose members run from ETRF89 through ETRF2020, with a stated ensemble accuracy of 0.1 m. A deliverable labelled simply "ETRS89" is therefore only specified to about 10 cm, before any question of WGS84 arises. EUREF's Technical Working Group recommends ETRF2000 as the conventional frame; if your specification does not name a realization, you have accepted the ensemble.</p>

<p>The projected systems inherit all of this. EPSG:25831 is ETRS89 / UTM zone 31N. EPSG:32631 is WGS 84 / UTM zone 31N. Same projection, same central meridian, same scale factor, same false easting. Different datum. A file header that says only "UTM31N" distinguishes neither.</p>

<h2>A worked example</h2>

<p>The figures below are synthetic – built to illustrate the failure mode, not taken from real projects – but the mechanism is exact.</p>

<p>A UXO survey over a wind farm export cable corridor delivers a target list: 214 magnetic anomalies, each with a position, an estimated mass, and a confidence class. The deliverable header states ETRS89 / UTM zone 31N. The client's asset GIS, and the ROV survey spread contracted to relocate and identify the targets, both work in WGS 84 / UTM zone 31N.</p>

<p>Nobody transforms anything, because both are "UTM31N".</p>

<p>Every target position is now displaced approximately 0.93 m to the south-west of where the ROV will look for it. Consider what that does to the relocation campaign:</p>

<ul>
  <li>A magnetic anomaly already carries its own positional uncertainty – commonly one to a few metres, depending on altitude, line spacing, and the inversion used. The datum offset does not average out against this. It adds to it, in the same direction, on every target.</li>
  <li>Relocation search patterns are sized against the expected uncertainty. A systematic 0.93 m consumes a substantial share of a search radius that was budgeted for random error alone.</li>
  <li>Targets that fail to relocate get reclassified, re-surveyed, or escalated. Each of those responses costs ROV time, and none of them addresses the actual cause.</li>
</ul>

<p>The campaign does not fail outright. It runs slow, produces a higher-than-expected proportion of unrelocated targets, and generates a plausible but wrong explanation: that the original magnetometer survey was of poor quality.</p>

<h2>The signature that identifies it</h2>

<p>A datum mismatch has a signature that no other error in survey work reproduces: the residuals are <strong>constant in magnitude and constant in bearing</strong> across the entire dataset.</p>

<p>Positioning noise is random and averages toward zero. Tidal or vertical reference errors show up in depth, not in plan. Layback or offset errors vary with heading, and therefore change sign between reciprocal lines. A gyro misalignment scales with distance from the reference point. A datum mismatch does none of these things – it shifts everything, everywhere, by the same vector.</p>

<p>That makes it trivially testable, provided anyone runs the test. Take any point whose position is known independently – an installed structure, a met mast, a previously verified target, an overlapping dataset from another contractor – and compute the residual. If a handful of such points all show the same displacement, in the same direction, with a magnitude near a metre, the answer is a datum, not a survey defect.</p>

<h2>What to require in the specification</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Full CRS identification, by EPSG code, for every deliverable.</strong><span class="t"> Not "WGS84", not "UTM31N". EPSG:25831 and EPSG:32631 are different answers to the same informal description.</span></span></li>
  <li><span class="k">02</span><span><strong>The realization and the epoch, stated explicitly.</strong><span class="t"> ETRF2000 at epoch 2026.5 is a specification. "ETRS89" is an ensemble with 0.1 m accuracy, and on a project positioning to centimetre level that is not good enough.</span></span></li>
  <li><span class="k">03</span><span><strong>The transformation actually applied, with its parameters, documented in the report</strong><span class="t"> – including the case where none was applied, and the justification for that.</span></span></li>
  <li><span class="k">04</span><span><strong>A single project CRS, defined in the contract before mobilisation,</strong><span class="t"> with any conversion to or from it performed once, by a named party, and recorded.</span></span></li>
  <li><span class="k">05</span><span><strong>A datum verification check at mobilisation,</strong><span class="t"> against at least one independently known position, with the residual reported as a vector rather than a distance. A scalar hides the direction, and the direction is what identifies the cause.</span></span></li>
  <li><span class="k">06</span><span><strong>CRS definitions carried in the file headers,</strong><span class="t"> not in a covering email. The IOGP P-format headers exist for this; they are only useful if they are populated correctly and read.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>Almost every other source of error in a survey deliverable requires judgement to assess. This one does not. The rate is published, the reference frames are documented, the EPSG codes are unambiguous, and the test that detects it takes one known point and a subtraction.</p>

<p>It persists because "ETRS89" and "WGS84" both look like the answer to the question "which datum?", and because a metre is small enough to be invisible in an overview plot and large enough to matter everywhere the work actually happens.</p>

<h3>References</h3>

<ul>
  <li>EUREF, Resolution 1, Florence 1990 – definition of ETRS89.</li>
  <li>EUREF Technical Working Group – recommendation to adopt ETRF2000 as the conventional frame of ETRS89.</li>
  <li>NGA, WGS 84 (G2296) – realization effective January 2024, aligned to ITRF2020 and IGS20.</li>
  <li>IOGP/EPSG Geodetic Parameter Registry – EPSG:4258, EPSG:4326, EPSG:25831, EPSG:32631.</li>
  <li>INSPIRE Directive (2007/2/EC) – ETRS89 as the reference system for European spatial data.</li>
</ul>

<div class="callout">
  <p>CLEGAR provides independent QC and technical assurance on geophysical datasets for offshore developers, contractors and asset owners. If you are specifying a survey, or reviewing a deliverable you have received, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'critical-path',
        'topic': 'pm',
        'date': '2026-08-12',
        'slug': {'it': 'quando-il-percorso-critico-si-sposta', 'en': 'when-the-critical-path-moves'},
        'title': {
            'it': 'Quando il critical path si sposta',
            'en': 'When the critical path moves',
        },
        'meta_title': {
            'it': 'Quando il critical path si sposta | Insights',
            'en': 'When the critical path moves | Insights',
        },
        'desc': {
            'it': ('Perché un weather allowance unico per tutte le attività offshore sposta il '
                   'critical path senza che nessuno se ne accorga, e come si ricalcola sulla '
                   'finestra operativa.'),
            'en': ('Why a single weather allowance across all offshore activities moves the critical '
                   'path without anyone noticing, and how to recompute it on workability.'),
        },
        'abstract': {
            'it': ('Il critical path non è una proprietà del progetto: è una proprietà delle '
                   'assunzioni su cui il programma è stato costruito. Su una campagna offshore, '
                   'quella che lavora di più è l’assunzione sul meteo.'),
            'en': ('A critical path is not a property of the project. It is a property of the '
                   'assumptions the schedule was built on – and offshore, the assumption doing the '
                   'most work is the one about weather.'),
        },
        'body': {
            'it': """
<p class="lede">Il critical path della maggior parte delle campagne offshore viene calcolato una volta, presentato al kick-off, e poi richiamato solo quando qualcosa è già andato storto. A quel punto, di solito, è il critical path sbagliato – non perché il planner abbia commesso un errore di calcolo, ma perché il programma è stato costruito su un'assunzione meteo che tratta ogni attività offshore come ugualmente esposta.</p>

<p>Non sono ugualmente esposte. Ed è quella differenza a decidere quale path sia effettivamente vincolante.</p>

<h2>Il problema del weather allowance unico</h2>

<p>La maggior parte dei programmi di campagna applica un unico weather allowance a tutto il lavoro offshore – 15%, 20%, qualunque valore abbia usato l'ultimo progetto. È un numero che sembra ragionevole, e viene applicato in modo uniforme perché applicarlo in qualunque altro modo richiede un'analisi della finestra operativa per cui, in fase di gara, nessuno ha previsto il tempo necessario.</p>

<p>Ma il meteo non ritarda le attività in proporzione alla loro durata. Le ritarda in proporzione a quanto spesso lo stato del mare supera <em>il proprio</em> limite operativo. Una linea di acquisizione multibeam e una prova CPT non si fermano alla stessa altezza d'onda significativa, e in una stagione marginale è nello scarto fra queste due soglie che il programma finisce davvero per fallire.</p>

<h2>Un esempio pratico</h2>

<p>I valori riportati di seguito sono sintetici – costruiti per illustrare il metodo, non tratti da progetti reali – ma la struttura è ricorrente.</p>

<p>Una campagna di site investigation combinata: uno spread geofisico e uno spread geotecnico, che procedono in parallelo su navi separate, entrambi confluenti in un unico obiettivo – un ground model integrato consegnato al progettista.</p>

<p><strong>Come pianificato al kick-off</strong>, con un weather allowance fisso del 15% applicato a entrambe le attività offshore:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Path A – Geofisico</th><th class="num">Giorni</th></tr>
</thead>
<tbody>
<tr><td>Mobilitazione</td><td class="num">4</td></tr>
<tr><td>Calibrazione e patch test</td><td class="num">2</td></tr>
<tr><td>Transito</td><td class="num">1</td></tr>
<tr><td>Acquisizione (22 + 15%)</td><td class="num">25</td></tr>
<tr><td>Processing</td><td class="num">10</td></tr>
<tr><td>Interpretazione e integrazione</td><td class="num">3</td></tr>
<tr><td><strong>Totale</strong></td><td class="num"><strong>45</strong></td></tr>
</tbody>
</table>
</div>

<div class="tablewrap">
<table>
<thead>
<tr><th>Path B – Geotecnico</th><th class="num">Giorni</th></tr>
</thead>
<tbody>
<tr><td>Mobilitazione</td><td class="num">5</td></tr>
<tr><td>Transito</td><td class="num">1</td></tr>
<tr><td>Campionamento e CPT (14 + 15%)</td><td class="num">16</td></tr>
<tr><td>Prove di laboratorio</td><td class="num">14</td></tr>
<tr><td>Factual Report</td><td class="num">5</td></tr>
<tr><td><strong>Totale</strong></td><td class="num"><strong>41</strong></td></tr>
</tbody>
</table>
</div>

<p>Path A è critico a 45 giorni. Path B ha 4 giorni di float. La milestone di consegna cade quindi al giorno 45.</p>

<p>Tutto il piano di mitigazione nasce da questa lettura: una clausola di standby nel contratto della nave usata per il rilievo, che fissa in anticipo quanto si paga nei giorni di fermo, un trasduttore MBES di ricambio spedito al porto di mobilitazione, un tecnico di processing in più nel team per comprimere il blocco di 10 giorni di processing se l'acquisizione sfora. Tutto questo protegge Path A.</p>

<h2>Lo stesso programma, con la finestra operativa applicata</h2>

<p>Ora si sostituisca il weather allowance unico con il limite operativo proprio di ciascuna attività, valutato rispetto alle statistiche hindcast meteo-marine per la finestra di acquisizione su quel sito:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Attività</th><th class="num">Limite operativo</th><th class="num">Finestra operativa</th><th class="num">Giorni produttivi richiesti</th><th class="num">Giorni di calendario necessari</th></tr>
</thead>
<tbody>
<tr><td>Acquisizione geofisica</td><td class="num">Hs ≤ 2,5 m</td><td class="num">84%</td><td class="num">22</td><td class="num">26</td></tr>
<tr><td>Campionamento geotecnico e CPT</td><td class="num">Hs ≤ 1,5 m</td><td class="num">62%</td><td class="num">14</td><td class="num">23</td></tr>
</tbody>
</table>
</div>

__FIG_WORK__

<p>Per l'acquisizione geofisica il weather allowance unico prevedeva 25 giorni di calendario, e ne servono 26: l'assunzione era quasi giusta. Per il campionamento geotecnico ne prevedeva 16, e ne servono 23. Sette giorni in meno del necessario.</p>

<p>Ricalcolato:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th></th><th class="num">Pianificato</th><th class="num">Ricalcolato</th><th class="num">Variazione</th></tr>
</thead>
<tbody>
<tr><td>Path A – Geofisico</td><td class="num">45</td><td class="num">46</td><td class="num">+1</td></tr>
<tr><td>Path B – Geotecnico</td><td class="num">41</td><td class="num">48</td><td class="num">+7</td></tr>
</tbody>
</table>
</div>

<p><strong>Path B è ora critico a 48 giorni. Path A ha 2 giorni di float.</strong></p>

__FIG_SWAP__

<h2>Che cosa è cambiato davvero</h2>

<p>La milestone è slittata di tre giorni. Questa è la conseguenza visibile, ed è la minore delle due.</p>

<p>La conseguenza maggiore è che tutte le mitigazioni del piano proteggono ormai il path sbagliato. La clausola di standby, il trasduttore di ricambio, il tecnico di processing in più: difendono un path che non vincola più e che ora ha persino del float. Il path che vincola davvero, invece, non ha alcuna protezione: al kick-off aveva quattro giorni di float, quindi nessuno gliene ha assegnata.</p>

<p>È questo il failure mode che vale la pena nominare: non che il programma sia in ritardo, ma che le misure protettive del progetto siano state allocate su un critical path che ha smesso di essere critico nel momento stesso in cui è stato applicato un modello meteo realistico – e nessuno lo ha ricalcolato.</p>

<h2>Dove si può davvero recuperare tempo</h2>

<p>Quando a vincolare è Path B, l'istinto è proteggere l'operazione di campionamento: estendere il noleggio della nave, aggiungere un giorno di standby meteo, spostare più avanti la finestra. Sono tutte soluzioni costose, e nessuna è affidabile, perché il vincolo è lo stato del mare e lo stato del mare non è negoziabile.</p>

<p>Su Path B l'unico blocco su cui si può davvero intervenire è quello delle prove di laboratorio: quattordici giorni a terra, che il meteo non tocca e che si possono comprimere. Accelerare i tempi di laboratorio da 14 a 9 giorni riporta Path B a 43 giorni, a una frazione del costo di un giorno di standby nave e senza alcun rischio meteo.</p>

<p>Questo, però, non ripristina la milestone originale. Con Path B a 43 giorni, torna a vincolare Path A, a 46 giorni, e lo slittamento si riduce da tre giorni a uno. Recuperare quell'ultimo giorno significa tornare al path geofisico e comprimere il blocco di 10 giorni di processing – esattamente ciò per cui era previsto il tecnico di processing in più nel piano di mitigazione originale. Quella mitigazione non era sbagliata. Era prematura: proteggeva un path che aveva smesso di essere vincolante, ed è tornata utile solo una volta che l'altro path è stato riportato sotto controllo.</p>

<p>È la stessa lezione applicata due volte all'interno di un solo esempio. Si comprime il path vincolante, e il critical path si sposta di nuovo.</p>

<p>Quell’opzione è sempre stata disponibile. È rimasta invisibile finché il piano mostrava il path geotecnico con un float comodo.</p>

<h2>Che cosa richiedere nella pianificazione della campagna</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Un weather allowance per attività, derivato dai limiti operativi.</strong><span class="t"> Un unico numero applicato a tutto lo scope offshore non è un weather allowance, è un segnaposto. Il limite di ciascuna attività va valutato rispetto alle statistiche meteo-marine del sito per la finestra reale.</span></span></li>
  <li><span class="k">02</span><span><strong>La base della finestra operativa dichiarata esplicitamente</strong><span class="t"> – quale dataset hindcast, quali anni, quale percentile. Queste ipotesi guidano il programma più di qualsiasi stima di durata, e sono di solito la parte meno documentata del piano.</span></span></li>
  <li><span class="k">03</span><span><strong>Il critical path ricalcolato ogni settimana, sui dati reali.</strong><span class="t"> Non la baseline ripresentata – ricalcolato, con il downtime reale a oggi e una stima aggiornata della finestra operativa futura. Il path vincolante alla quarta settimana spesso non è quello che vincolava al kick-off.</span></span></li>
  <li><span class="k">04</span><span><strong>La mitigazione mappata sul critical path corrente, non su quello di baseline.</strong><span class="t"> Se il critical path si sposta e il registro delle mitigazioni non lo segue, il progetto sta pagando una protezione di cui non ha più bisogno.</span></span></li>
  <li><span class="k">05</span><span><strong>Una soglia di near-critical definita.</strong><span class="t"> Qualsiasi path che disti meno di cinque giorni dal critical path va monitorato con la stessa disciplina. Nel lavoro offshore l’ordine dei path cambia troppo facilmente per monitorare soltanto quello in testa.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Un critical path non è una proprietà del progetto. È una proprietà delle assunzioni su cui è stato costruito il programma – e in una campagna offshore, l'assunzione che lavora di più è quella sul meteo.</p>

<p>Se al posto della percentuale fissa si usano i limiti operativi reali, non cambia soltanto la durata delle attività: cambia quale path vincola. Il programma che ne risulta non è più pessimistico. È puntato sul problema giusto.</p>

<div class="callout">
  <p>CLEGAR fornisce project management e technical assurance per campagne offshore. Se state pianificando un rilievo, o state rivedendo un programma che vi è stato consegnato, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">The critical path on most offshore campaigns is computed once, presented at kick-off, and then referred to only when something has already gone wrong. By that point it is usually the wrong critical path – not because the planner made an arithmetic error, but because the schedule was built on a weather assumption that treats every offshore activity as equally exposed.</p>

<p>They are not equally exposed. And the difference decides which path actually binds.</p>

<h2>The flat allowance problem</h2>

<p>Most campaign schedules apply a single weather allowance across all offshore work – 15%, 20%, whatever the last project used. It is a reasonable-looking number, and it is applied uniformly because applying it any other way requires a workability analysis that takes time nobody has budgeted at tender stage.</p>

<p>But weather does not delay activities in proportion to their duration. It delays them in proportion to how often the sea state exceeds <em>their own</em> operating limit. A multibeam acquisition line and a CPT deployment do not stop at the same significant wave height, and in a marginal season the gap between those two thresholds is where the schedule actually fails.</p>

<h2>A worked example</h2>

<p>The figures below are synthetic – built to illustrate the method, not taken from real projects – but the structure is one that recurs.</p>

<p>A combined site investigation campaign: a geophysical spread and a geotechnical spread, running in parallel on separate vessels, both feeding a single milestone – an integrated ground model handed to the foundation designer.</p>

<p><strong>As planned at kick-off</strong>, with a flat 15% weather allowance applied to both offshore activities:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Path A – Geophysical</th><th class="num">Days</th></tr>
</thead>
<tbody>
<tr><td>Mobilisation</td><td class="num">4</td></tr>
<tr><td>Calibration &amp; patch test</td><td class="num">2</td></tr>
<tr><td>Transit</td><td class="num">1</td></tr>
<tr><td>Acquisition (22 + 15%)</td><td class="num">25</td></tr>
<tr><td>Processing</td><td class="num">10</td></tr>
<tr><td>Interpretation &amp; integration</td><td class="num">3</td></tr>
<tr><td><strong>Total</strong></td><td class="num"><strong>45</strong></td></tr>
</tbody>
</table>
</div>

<div class="tablewrap">
<table>
<thead>
<tr><th>Path B – Geotechnical</th><th class="num">Days</th></tr>
</thead>
<tbody>
<tr><td>Mobilisation</td><td class="num">5</td></tr>
<tr><td>Transit</td><td class="num">1</td></tr>
<tr><td>Sampling &amp; CPT (14 + 15%)</td><td class="num">16</td></tr>
<tr><td>Laboratory testing</td><td class="num">14</td></tr>
<tr><td>Factual reporting</td><td class="num">5</td></tr>
<tr><td><strong>Total</strong></td><td class="num"><strong>41</strong></td></tr>
</tbody>
</table>
</div>

<p>Path A is critical at 45 days. Path B carries 4 days of float. The handover milestone sits at day 45.</p>

<p>Everything in the mitigation plan follows from that reading: a standby clause in the survey vessel contract, fixing in advance what an idle day costs, a spare MBES transducer head shipped to the mobilisation port, an extra processor on the team to compress the 10-day processing block if acquisition overruns. All of it protects Path A.</p>

<h2>The same schedule, with workability applied</h2>

<p>Now replace the flat allowance with each activity's own operating limit, assessed against metocean hindcast statistics for the acquisition window at that site:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Activity</th><th class="num">Operating limit</th><th class="num">Workable proportion of window</th><th class="num">Productive days required</th><th class="num">Calendar days needed</th></tr>
</thead>
<tbody>
<tr><td>Geophysical acquisition</td><td class="num">Hs ≤ 2.5 m</td><td class="num">84%</td><td class="num">22</td><td class="num">26</td></tr>
<tr><td>Geotechnical sampling &amp; CPT</td><td class="num">Hs ≤ 1.5 m</td><td class="num">62%</td><td class="num">14</td><td class="num">23</td></tr>
</tbody>
</table>
</div>

__FIG_WORK__

<p>The geophysical acquisition needed 25 calendar days under the flat allowance and needs 26 – the assumption was close to right. The geotechnical sampling needed 16 and needs 23. The flat allowance under-provisioned it by seven days.</p>

<p>Recomputed:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th></th><th class="num">Planned</th><th class="num">Recomputed</th><th class="num">Change</th></tr>
</thead>
<tbody>
<tr><td>Path A – Geophysical</td><td class="num">45</td><td class="num">46</td><td class="num">+1</td></tr>
<tr><td>Path B – Geotechnical</td><td class="num">41</td><td class="num">48</td><td class="num">+7</td></tr>
</tbody>
</table>
</div>

<p><strong>Path B is now critical at 48 days. Path A has 2 days of float.</strong></p>

__FIG_SWAP__

<h2>What actually changed</h2>

<p>The milestone slipped three days. That is the visible consequence, and it is the smaller one.</p>

<p>The larger consequence is that every mitigation in the plan is now pointed at the wrong path. The standby clause, the spare transducer, the extra processor – all of it protects a path that is no longer binding and now carries float of its own. The path that actually binds, by contrast, has no protection at all: at kick-off it carried four days of float, so nobody assigned it any.</p>

<p>This is the failure mode worth naming: not that the schedule was late, but that the project's protective measures were allocated against a critical path that stopped being critical the moment a realistic weather model was applied – and nobody recomputed.</p>

<h2>Where the recovery lever actually is</h2>

<p>Once Path B is critical, the instinct is to protect the sampling operation: extend the vessel charter, add a weather standby day, push the window later. All of these are expensive, and none of them are reliable, because the constraint is the sea state and the sea state is not negotiable.</p>

<p>The recovery lever on Path B is the 14-day laboratory testing block – onshore, weather-independent, and compressible. Expediting lab turnaround from 14 days to 9 pulls Path B back to 43 days, at a fraction of the cost of a vessel standby day and with none of the weather risk.</p>

<p>It does not, however, restore the original milestone. With Path B at 43 days, Path A binds again at 46, and the slip narrows from three days to one. Recovering that last day means going back to the geophysical path and compressing the 10-day processing block – which is precisely what the extra processor in the original mitigation plan was for. That mitigation was not wrong. It was premature: it protected a path that had stopped binding, and became useful again only once the other path had been brought back under control.</p>

<p>This is the same lesson applied twice inside a single example. Compress the binding path, and the ranking changes again.</p>

<p>That option was always available. It was invisible for as long as the plan showed the geotechnical path carrying comfortable float.</p>

<h2>What to require in campaign planning</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>A per-activity weather allowance, derived from operating limits.</strong><span class="t"> One number applied across the whole offshore scope is not a weather allowance, it is a placeholder. Each activity's limit assessed against site metocean statistics for the actual window.</span></span></li>
  <li><span class="k">02</span><span><strong>The workability basis stated explicitly</strong><span class="t"> – which hindcast dataset, which years, which percentile. These assumptions drive the schedule more than any duration estimate, and they are usually the least documented part of the plan.</span></span></li>
  <li><span class="k">03</span><span><strong>The critical path recomputed weekly, on actuals.</strong><span class="t"> Not the baseline re-presented – recomputed, with real downtime to date and an updated forward workability estimate. The path that binds in week four is often not the one that bound at kick-off.</span></span></li>
  <li><span class="k">04</span><span><strong>Mitigation mapped to the current critical path, not the baseline one.</strong><span class="t"> If the critical path moves and the mitigation register does not follow it, the project is paying for protection it no longer needs.</span></span></li>
  <li><span class="k">05</span><span><strong>A near-critical threshold defined.</strong><span class="t"> Any path within, say, five days of critical gets tracked with the same discipline as the critical path itself. On offshore work the ranking changes too easily to monitor only the top item.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>A critical path is not a property of the project. It is a property of the assumptions the schedule was built on – and on an offshore campaign, the assumption doing the most work is the one about weather.</p>

<p>Change the weather model from a flat percentage to actual operating limits, and the ranking of the paths changes with it. The schedule that results is not more pessimistic. It is pointed at the right problem.</p>

<div class="callout">
  <p>CLEGAR provides project management and technical assurance for offshore campaigns. If you are planning a survey, or reviewing a schedule you have been given, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'crossline-check',
        'topic': 'geoscience',
        'date': '2026-08-12',
        'slug': {'it': 'crossline-check-come-mappa', 'en': 'crossline-check-as-a-map'},
        'title': {
            'it': 'Leggere un crossline check come una mappa, non come una percentuale',
            'en': 'Reading a crossline check as a map, not a pass rate',
        },
        'meta_title': {
            'it': 'Leggere un crossline check come una mappa | Insights',
            'en': 'Reading a crossline check as a map | Insights',
        },
        'desc': {
            'it': ('Perché la percentuale di incroci entro tolleranza nasconde il risultato di '
                   'un’analisi crossline, e che cosa chiedere nella specifica prima dell’acquisizione.'),
            'en': ('Why the percentage of crossings within tolerance hides the finding of a '
                   'crossline analysis, and what to ask for in the specification before acquisition.'),
        },
        'abstract': {
            'it': ('L’analisi delle crossline confronta il dataset con se stesso. Ridotta a una '
                   'percentuale nel report finale, perde proprio l’informazione che serve: dove le '
                   'due misure sono in disaccordo, e perché.'),
            'en': ('A crossline analysis compares the dataset against itself. Reduced to a percentage '
                   'in the final report, it loses the very information that matters: where the two '
                   'measurements disagree, and why.'),
        },
        'body': {
            'it': """
<p class="lede">L'analisi delle crossline è uno dei pochi prodotti di QC di un rilievo batimetrico che confronta il dataset con se stesso. Due linee di acquisizione attraversano lo stesso punto del fondale, acquisite in momenti diversi, su rotte diverse, in condizioni di marea e di velocità del suono diverse. La profondità che riportano nel punto di incrocio dovrebbe coincidere. Quanto strettamente coincide è un'affermazione diretta e misurabile su quanto il dataset sia affidabile.</p>

<p>Nella pratica, questo controllo viene spesso ridotto a un singolo numero nel report finale – una percentuale di incroci entro tolleranza – e letto come si legge un voto di promozione. È in quella riduzione che l'informazione utile va perduta.</p>

<h2>L'inviluppo di tolleranza</h2>

<p>Lo standard IHO S-44 non prescrive una procedura di crossline analysis. Quello che definisce è la Total Vertical Uncertainty (TVU) ammessa a una data profondità, al livello di confidenza del 95%:</p>

<p><strong>TVU = √( a² + (b × d)² )</strong></p>

<p>dove <em>d</em> è la profondità e <em>a</em> e <em>b</em> sono le costanti fissate dall'ordine di rilievo. Per l'<strong>Order 1a</strong>, l'ordine più comunemente specificato per le site investigation nell'eolico offshore:</p>

<ul>
  <li>a = 0,50 m (componente indipendente dalla profondità)</li>
  <li>b = 0,013 (componente dipendente dalla profondità)</li>
</ul>

<p>Che dà, su un sito tipico del Mare del Nord meridionale:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th class="num">Profondità</th><th class="num">TVU ammessa (Order 1a)</th><th class="num">Soglia sugli incroci (√2 × TVU)</th></tr>
</thead>
<tbody>
<tr><td class="num">20 m</td><td class="num">0,56 m</td><td class="num">0,80 m</td></tr>
<tr><td class="num">30 m</td><td class="num">0,63 m</td><td class="num">0,90 m</td></tr>
<tr><td class="num">40 m</td><td class="num">0,72 m</td><td class="num">1,02 m</td></tr>
<tr><td class="num">50 m</td><td class="num">0,82 m</td><td class="num">1,16 m</td></tr>
<tr><td class="num">60 m</td><td class="num">0,93 m</td><td class="num">1,31 m</td></tr>
</tbody>
</table>
</div>

__FIG_TVU__

<p>La seconda colonna è quella che viene saltata. La differenza in un punto di incrocio è il disaccordo tra <em>due</em> misure indipendenti, ciascuna con la propria incertezza. Confrontare quella differenza con un singolo valore di TVU è il test sbagliato: le due incertezze si compongono in quadratura, quindi l'inviluppo per la differenza è √2 × TVU. Specificare quale delle due soglie si applica è una decisione contrattuale, non un dettaglio tecnico, e va scritta nella specifica prima dell'acquisizione anziché discussa dopo la consegna.</p>

<h2>Un esempio pratico</h2>

<p>I valori riportati di seguito sono sintetici – costruiti per illustrare il metodo, non tratti da lavori per clienti – ma la struttura è ricorrente.</p>

<p>Un rilievo di site investigation su un'area di sviluppo eolico, profondità tra 22 m e 58 m, acquisito in Order 1a. L'analisi delle crossline produce 1.240 punti di incrocio. La riga di sintesi nel report recita:</p>

<div class="pull"><strong>96,4%</strong><span>degli incroci entro tolleranza</span></div>

<p>Con quasi qualsiasi criterio di accettazione di progetto, il rilievo passa. È un buon numero. Il dataset viene approvato.</p>

<p>Ora lo stesso risultato, risolto spazialmente. I 45 incroci fuori tolleranza non sono distribuiti casualmente sul blocco. Ricadono in tre gruppi:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Gruppo</th><th class="num">Incroci fuori tolleranza</th><th class="num">Intervallo di profondità</th><th>Caratteristiche del fondale</th></tr>
</thead>
<tbody>
<tr><td>A</td><td class="num">6</td><td class="num">24–31 m</td><td>piatto, sabbioso – isolati, nessuno schema</td></tr>
<tr><td>B</td><td class="num">8</td><td class="num">44–58 m</td><td>piatto – tutti dalla stessa linea, stessa giornata</td></tr>
<tr><td>C</td><td class="num">31</td><td class="num">26–34 m</td><td>campo di sand wave mobili</td></tr>
</tbody>
</table>
</div>

__FIG_MAP__

<p>Tre risultati diversi, tre conseguenze diverse.</p>

<p><strong>Il gruppo A</strong> è rumore. Sei incroci isolati su 1.240, senza schema spaziale o temporale. È l'aspetto che ha un dataset sano sulle code della distribuzione.</p>

<p><strong>Il gruppo B</strong> è un errore sistematico. Tutti e otto gli scarti provengono da una singola linea acquisita in una singola giornata. Quella firma – raggruppata nel tempo, non nello spazio – punta al riferimento verticale: una correzione di marea applicata dalla stazione sbagliata, una variazione di pescaggio non registrata dopo il bunkeraggio, un profilo di velocità del suono ormai fuori dalla propria finestra di validità. È un difetto reale, ed è anche il più semplice dei tre da risolvere, perché uno scostamento sistematico su una linea nota può essere quantificato e corretto anziché riacquisito.</p>

<p><strong>Il gruppo C</strong> è quello che conta. Trentuno scarti concentrati in un campo di sand wave mobili, su un intervallo di profondità tra 26 e 34 m. Qui le due linee sono realmente in disaccordo, ed entrambe possono essere corrette: il fondale si è spostato tra un passaggio e l'altro. Nessun riprocessing le riconcilierà, perché non c'è nulla da riconciliare – le misure descrivono due stati diversi di una superficie che cambia.</p>

<p>Prima di attribuire tutto alla mobilità, però, va sottratta una componente che si presenta esattamente negli stessi punti. Su una superficie inclinata, uno scarto orizzontale fra le due linee si traduce in una differenza verticale anche se il fondale è fermo: con una pendenza di 15°, un metro di scarto orizzontale produce da solo 27 cm di differenza in quota. Sui fianchi di una sand wave è proprio dove le pendenze sono maggiori che gli incroci cadono. È il motivo per cui diverse specifiche escludono le aree ad alto gradiente dalle statistiche crossline, o chiedono che la differenza venga normalizzata sulla pendenza locale prima di essere confrontata con la soglia.</p>

<p>Separare le due componenti è ciò che rende l'attribuzione difendibile. Se, tolto il contributo della pendenza, il disaccordo resta, allora il fondale si è mosso davvero – e a quel punto l'affermazione regge anche davanti a un contractor che abbia interesse a smontarla.</p>

<h2>Perché la percentuale nasconde il risultato</h2>

<p>Il 96,4% di sintesi tratta tutti e 45 gli scarti come equivalenti. Risolti spazialmente, sono tre risultati distinti che richiedono tre risposte distinte: accettare, correggere e – per il gruppo C – escalare.</p>

<p>Il gruppo C conta per dove si trova, non per quanto è grande. Trentuno incroci sono il 2,5% del dataset. Ma se una posizione di fondazione proposta o un tracciato cavo attraversa quel campo di sand wave, il rilievo ha appena prodotto evidenza quantitativa di mobilità del fondale esattamente nell'area in cui verranno progettate la profondità di interro e la protezione allo scalzamento. Non è una non conformità di QC da registrare e chiudere. È un dato di geohazard, e appartiene alla discussione ingegneristica, non a un allegato.</p>

<p>La percentuale non può dirti questo. È una sintesi scalare di un fenomeno spaziale, e la struttura spaziale è l'intero risultato.</p>

<h2>Cosa chiedere nella specifica</h2>

<p>Gran parte di ciò che rende utile un crossline check si decide prima che la nave salpi:</p>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Indicare quale soglia si applica</strong><span class="t"> – TVU o √2 × TVU – e a quale livello di confidenza. Non lasciarlo dedurre dallo standard.</span></span></li>
  <li><span class="k">02</span><span><strong>Richiedere il risultato delle crossline come superficie rappresentata graficamente</strong><span class="t">, non solo come statistica di sintesi. Una mappa delle differenze con l'inviluppo di tolleranza applicato mostra una struttura che una percentuale non può mostrare.</span></span></li>
  <li><span class="k">03</span><span><strong>Richiedere che gli scarti siano raggruppati e attribuiti</strong><span class="t"> – rumore, sistematico o variazione reale – anziché elencati. L'attribuzione è l'analisi; l'elenco ne è soltanto il dato di ingresso.</span></span></li>
  <li><span class="k">04</span><span><strong>Definire cosa succede dopo per ciascuna attribuzione.</strong><span class="t"> Uno scostamento sistematico si corregge. Una variazione reale del fondale si porta al team di ingegneria. Senza questo definito in anticipo, entrambi gli esiti tendono a ricevere lo stesso trattamento: una nota nel report.</span></span></li>
  <li><span class="k">05</span><span><strong>Fissare la densità delle crossline</strong><span class="t"> – un riferimento diffuso è una lunghezza complessiva pari a circa il 5% delle mainline, ma il valore corretto dipende dal sito e dalle decisioni che i dati dovranno supportare.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Un crossline check risponde a una domanda più stretta di quanto sembri. Non dice se i dati sono buoni. Dice dove due misure indipendenti dello stesso fondale sono in disaccordo, e di quanto – e il valore sta nel leggerlo come una mappa di dove la confidenza è più bassa, non come un voto.</p>

<p>Un dataset che passa al 96,4% non è uniformemente affidabile al 96,4%. È altamente affidabile sulla maggior parte del blocco e meno affidabile in un'area specifica – e in questo esempio, quell'area è dove si fa l'ingegneria.</p>

<div class="callout">
  <p>CLEGAR fornisce QC indipendente e technical assurance su dataset geofisici per sviluppatori, contractor e asset owner dell'offshore. Se state redigendo la specifica di un rilievo, o state valutando un dataset che avete ricevuto, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">A crossline analysis is one of the few QC products on a bathymetric survey that compares the dataset against itself. Two survey lines cross the same patch of seabed, acquired at different times, on different headings, under different tide and sound-velocity conditions. The depth they report at the crossing point should agree. How closely they agree is a direct, measurable statement about how much the dataset can be trusted.</p>

<p>In practice, this check is often reduced to a single number in the final report – a percentage of crossings within tolerance – and read the way one reads a passing grade. That reduction is where the useful information gets lost.</p>

<h2>The tolerance envelope</h2>

<p>IHO S-44 does not prescribe a crossline procedure. What it defines is the Total Vertical Uncertainty (TVU) permitted at a given depth, at the 95% confidence level:</p>

<p><strong>TVU = √( a² + (b × d)² )</strong></p>

<p>where <em>d</em> is the depth and <em>a</em> and <em>b</em> are the constants set by the survey order. For <strong>Order 1a</strong>, the order most commonly specified for offshore wind site investigation:</p>

<ul>
  <li>a = 0.50 m (depth-independent component)</li>
  <li>b = 0.013 (depth-dependent component)</li>
</ul>

<p>Which gives, across a typical Southern North Sea site:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th class="num">Depth</th><th class="num">Permitted TVU (Order 1a)</th><th class="num">Crossing threshold (√2 × TVU)</th></tr>
</thead>
<tbody>
<tr><td class="num">20 m</td><td class="num">0.56 m</td><td class="num">0.80 m</td></tr>
<tr><td class="num">30 m</td><td class="num">0.63 m</td><td class="num">0.90 m</td></tr>
<tr><td class="num">40 m</td><td class="num">0.72 m</td><td class="num">1.02 m</td></tr>
<tr><td class="num">50 m</td><td class="num">0.82 m</td><td class="num">1.16 m</td></tr>
<tr><td class="num">60 m</td><td class="num">0.93 m</td><td class="num">1.31 m</td></tr>
</tbody>
</table>
</div>

__FIG_TVU__

<p>The second column is the point that gets skipped. A crossing difference is the disagreement between <em>two</em> independent measurements, each carrying its own uncertainty. Comparing that difference against a single TVU value is the wrong test – the two uncertainties combine in quadrature, so the envelope for the difference is √2 × TVU. Specifying which of these two thresholds applies is a contractual decision, not a technical detail, and it should be written into the specification before acquisition rather than argued about after delivery.</p>

<h2>A worked example</h2>

<p>The figures below are synthetic – built to illustrate the method, not taken from client work – but the shape is one we see repeatedly.</p>

<p>A site investigation survey over a wind farm development area, water depths from 22 m to 58 m, acquired to Order 1a. The crossline analysis produces 1,240 crossing points. The summary line in the report reads:</p>

<div class="pull"><strong>96.4%</strong><span>of crossings within tolerance</span></div>

<p>By almost any project's acceptance criterion, that passes. It is a good number. The dataset gets signed off.</p>

<p>Now the same result, resolved spatially. The 45 failing crossings are not distributed randomly across the block. They fall into three groups:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Group</th><th class="num">Crossings failing</th><th class="num">Depth range</th><th>Seabed character</th></tr>
</thead>
<tbody>
<tr><td>A</td><td class="num">6</td><td class="num">24–31 m</td><td>flat, sandy – isolated, no pattern</td></tr>
<tr><td>B</td><td class="num">8</td><td class="num">44–58 m</td><td>flat – all from one line, one day</td></tr>
<tr><td>C</td><td class="num">31</td><td class="num">26–34 m</td><td>mobile sand wave field</td></tr>
</tbody>
</table>
</div>

__FIG_MAP__

<p>Three different findings, three different consequences.</p>

<p><strong>Group A</strong> is noise. Six isolated crossings out of 1,240, no spatial or temporal pattern. This is what a healthy dataset looks like at the tails.</p>

<p><strong>Group B</strong> is a systematic error. All eight failures come from a single line acquired on a single day. That signature – clustered in time, not in space – points at the vertical reference: a tide correction applied from the wrong station, a draft change not logged after bunkering, a sound velocity profile that had aged past its useful window. It is a real defect, and it is also the easiest of the three to fix, because a systematic offset on a known line can be quantified and corrected rather than reacquired.</p>

<p><strong>Group C</strong> is the one that matters. Thirty-one failures concentrated in a mobile sand wave field, over a depth range of 26–34 m. Here the two survey lines genuinely disagree, and both may be correct: the seabed moved between the two passes. No reprocessing will reconcile them, because there is nothing to reconcile – the measurements describe two different states of a surface that changes.</p>

<p>Before attributing all of it to mobility, though, one component has to be subtracted, and it appears in exactly the same places. On a sloping surface, a horizontal offset between the two lines turns into a vertical difference even if the seabed has not moved at all: on a 15° slope, one metre of horizontal offset produces 27 cm of height difference on its own. On the flanks of a sand wave, the steepest gradients are precisely where the crossings fall. This is why several specifications exclude high-gradient areas from crossline statistics, or require the difference to be normalised against the local slope before it is compared with the threshold.</p>

<p>Separating the two components is what makes the attribution defensible. If the disagreement survives once the slope contribution has been removed, then the seabed really did move – and at that point the statement holds up even in front of a contractor with an interest in dismantling it.</p>

<h2>Why the pass rate hides the finding</h2>

<p>The 96.4% headline treats all 45 failures as equivalent. Resolved spatially, they are three separate findings requiring three separate responses: accept, correct, and – for Group C – escalate.</p>

<p>Group C matters because of where it sits, not how large it is. Thirty-one crossings is 2.5% of the dataset. But if a proposed foundation location or a cable route crosses that sand wave field, the survey has just produced quantitative evidence of seabed mobility in the exact area where burial depth and scour protection will be designed. That is not a QC failure to be dispositioned and closed. It is a geohazard finding, and it belongs in the engineering discussion, not in an appendix.</p>

<p>The pass rate cannot tell you this. It is a scalar summary of a spatial phenomenon, and the spatial structure is the entire finding.</p>

<h2>What to ask for in the specification</h2>

<p>Most of what makes a crossline check useful is decided before the vessel sails:</p>

<ul class="flist">
  <li><span class="k">01</span><span><strong>State which threshold applies</strong><span class="t"> – TVU or √2 × TVU – and at what confidence level. Do not leave it to be inferred from the standard.</span></span></li>
  <li><span class="k">02</span><span><strong>Require the crossline result as a plotted surface</strong><span class="t">, not only as a summary statistic. A difference map with the tolerance envelope applied shows structure that a percentage cannot.</span></span></li>
  <li><span class="k">03</span><span><strong>Require failures to be grouped and attributed</strong><span class="t"> – noise, systematic, or real change – rather than listed. The attribution is the analysis; the list is only the input to it.</span></span></li>
  <li><span class="k">04</span><span><strong>Define what happens next for each attribution.</strong><span class="t"> A systematic offset gets corrected. Genuine seabed change gets escalated to the engineering team. Without this defined in advance, both outcomes tend to receive the same treatment: a note in the report.</span></span></li>
  <li><span class="k">05</span><span><strong>Set the crossline density</strong><span class="t"> – a common baseline is crosslines totalling around 5% of mainline length, but the right figure depends on the site and the decisions the data will support.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>A crossline check answers a narrower question than it appears to. It does not tell you whether the data is good. It tells you where two independent measurements of the same seabed disagree, and by how much – and the value is in reading that as a map of where confidence is lowest, not as a grade.</p>

<p>A dataset that passes at 96.4% is not uniformly 96.4% reliable. It is highly reliable across most of the block and least reliable in one specific area – and in this example, that area is where the engineering happens.</p>

<div class="callout">
  <p>CLEGAR provides independent QC and technical assurance on geophysical datasets for offshore developers, contractors and asset owners. If you are specifying a survey, or reviewing one you have received, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'introducing-clegar',
        'topic': None,
        'date': '2026-08-05',
        'slug': {'it': 'presentazione-clegar', 'en': 'introducing-clegar'},
        'title': {
            'it': 'Presentazione di CLEGAR',
            'en': 'Introducing CLEGAR',
        },
        'meta_title': {
            'it': 'Presentazione di CLEGAR | Insights',
            'en': 'Introducing CLEGAR | Insights',
        },
        'desc': {
            'it': ('CLEGAR è una società di consulenza indipendente per progetti marini e offshore. '
                   'Perché nasce, che cosa significa indipendenza in questo settore e le cinque linee di servizio.'),
            'en': ('CLEGAR is an independent consultancy for marine and offshore projects. '
                   'Why it exists, what independence means here, and the five service lines.'),
        },
        'abstract': {
            'it': ('Perché nasce CLEGAR, che cosa significa indipendenza quando si valuta un dataset '
                   'geofisico, e come si articolano le cinque linee di servizio.'),
            'en': ('Why CLEGAR exists, what independence means when assessing a geophysical dataset, '
                   'and how the five service lines fit together.'),
        },
        'body': {
            'en': """
<p class="lede">CLEGAR is an independent consultancy for marine and offshore projects. We plan geophysical surveys, verify the data they produce, and represent the client where the decisions that matter are actually made – on board, on the quayside, and across the contract table.</p>

<h2>Why CLEGAR exists</h2>

<p>Most problems on an offshore project don't start offshore. They start weeks earlier, when the requirements are written – with a tolerance nobody defined precisely, or an acceptance criterion the client and the contractor each read differently.</p>

<p>By the time the data comes back and someone has to decide whether it's good enough, the argument has no fixed reference point. It gets settled by whoever is more persuasive in the room, not by what the deliverable actually shows against what was agreed.</p>

""" + FIG_ORIGIN + """

<p>CLEGAR was set up to sit on the other side of that problem: involved early enough that the criteria are clear before acquisition starts, and independent enough that when we say a deliverable does or doesn't meet the standard it was bought against, there is no second interest behind that opinion.</p>

<h2>What independence means here</h2>

<p>We don't sell survey equipment. We don't acquire data ourselves. We hold no stake in the supply chain we're asked to assess.</p>

<p>This is a narrow, specific kind of independence – not a marketing claim, but a structural one: nothing in how CLEGAR is paid depends on which contractor, which vessel, or which technology a client ends up choosing.</p>

<h2>Five service lines</h2>

""" + FIG_LINES + """

<ul class="flist">
  <li><span class="k">01</span><span><strong>Marine Geoscience</strong><span class="t">Survey planning, technical specifications, QC against recognised standards such as IHO S-44, processing and interpretation of geophysical datasets.</span></span></li>
  <li><span class="k">02</span><span><strong>Project Management</strong><span class="t">Schedule and critical path management, interface management between contractors, cost control, and a risk register that gets updated, not filed.</span></span></li>
  <li><span class="k">03</span><span><strong>Technical Advisory &amp; Assurance</strong><span class="t">Independent technical reviews, due diligence on geophysical datasets and contractor deliverables, second-opinion verification before a client signs off.</span></span></li>
  <li><span class="k">04</span><span><strong>Owner's Engineering</strong><span class="t">Mobilisation planning and acceptance, witnessing of instrument calibrations, offshore supervision, production and downtime control on behalf of the client.</span></span></li>
  <li><span class="k">05</span><span><strong>Operational Excellence</strong><span class="t">Operational KPIs, procedures and SOPs, readiness reviews before campaigns, and turning lessons learned into something the next project actually uses.</span></span></li>
</ul>

<h2>Who we work with</h2>

<p>Offshore wind developers, marine contractors, and asset owners who need a technical partner that reduces risk and improves decision-making at each stage of a project – from the first requirements to the final acceptance.</p>

<h2>What comes next</h2>

<p>This is the first of a series of technical articles CLEGAR will publish covering real cases from marine geoscience, project management, and offshore operations – the kind of worked examples that show how a tolerance, a schedule, or a mobilisation record actually gets checked in practice, not just described in general terms.</p>

<div class="callout">
  <p>If you're planning a survey, reviewing a dataset you're not sure you should accept, or setting the requirements for an upcoming campaign, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'it': """
<p class="lede">CLEGAR è una società di consulenza indipendente per progetti marini e offshore. Pianifichiamo indagini geofisiche, verifichiamo i dati che ne escono e rappresentiamo il committente dove le decisioni che contano si prendono davvero: a bordo, in banchina e al tavolo del contratto.</p>

<h2>Perché nasce CLEGAR</h2>

<p>La maggior parte dei problemi di un progetto offshore non nasce offshore. Nasce settimane prima, quando si scrivono i requisiti: una tolleranza che nessuno ha definito con precisione, o un criterio di accettazione che il committente e il contractor leggono in due modi diversi.</p>

<p>Quando i dati tornano a terra e qualcuno deve decidere se sono sufficienti, la discussione non ha più un riferimento fisso. Si risolve in favore di chi è più persuasivo nella stanza, non in base a quello che il deliverable mostra davvero rispetto a quanto era stato pattuito.</p>

""" + FIG_ORIGIN + """

<p>CLEGAR nasce per stare dall'altra parte di quel problema: coinvolta abbastanza presto perché i criteri siano chiari prima che l'acquisizione cominci, e abbastanza indipendente perché, quando diciamo che un deliverable rispetta o non rispetta lo standard per cui è stato acquistato, dietro quel giudizio non ci sia un secondo interesse.</p>

<h2>Che cosa significa indipendenza in questo settore</h2>

<p>Non vendiamo strumentazione da survey. Non acquisiamo dati in proprio. Non abbiamo interessi nella catena di fornitura che ci viene chiesto di valutare.</p>

<p>È un tipo di indipendenza stretto e preciso: non una dichiarazione di marketing, ma una condizione strutturale. Nulla di come CLEGAR viene remunerata dipende da quale contractor, quale nave o quale tecnologia il committente sceglierà.</p>

<h2>Le cinque linee di servizio</h2>

""" + FIG_LINES + """

<ul class="flist">
  <li><span class="k">01</span><span><strong>Marine Geoscience</strong><span class="t">Pianificazione delle indagini, specifiche tecniche, QC secondo standard riconosciuti come IHO S-44, processing e interpretazione di dataset geofisici.</span></span></li>
  <li><span class="k">02</span><span><strong>Project Management</strong><span class="t">Gestione del programma e del percorso critico, gestione delle interfacce tra contractor, controllo dei costi e un registro dei rischi che viene aggiornato, non archiviato.</span></span></li>
  <li><span class="k">03</span><span><strong>Technical Advisory &amp; Assurance</strong><span class="t">Revisioni tecniche indipendenti, due diligence su dataset geofisici e deliverable del contractor, verifica in seconda opinione prima che il committente firmi l'accettazione.</span></span></li>
  <li><span class="k">04</span><span><strong>Owner's Engineering</strong><span class="t">Pianificazione e accettazione della mobilitazione, witnessing delle calibrazioni strumentali, supervisione offshore, controllo di produzione e downtime per conto del committente.</span></span></li>
  <li><span class="k">05</span><span><strong>Operational Excellence</strong><span class="t">KPI operativi, procedure e SOP, readiness review prima delle campagne, e trasformazione delle lessons learned in qualcosa che il progetto successivo usa davvero.</span></span></li>
</ul>

<h2>Con chi lavoriamo</h2>

<p>Sviluppatori eolici offshore, contractor marini e proprietari di asset che hanno bisogno di un partner tecnico capace di ridurre il rischio e migliorare le decisioni in ogni fase del progetto, dai primi requisiti all'accettazione finale.</p>

<h2>Che cosa arriva dopo</h2>

<p>Questo è il primo di una serie di articoli tecnici che CLEGAR pubblicherà su casi reali di geoscienze marine, project management e operazioni offshore: esempi lavorati che mostrano come una tolleranza, un programma o un verbale di mobilitazione vengano verificati nella pratica, e non soltanto descritti in termini generali.</p>

<div class="callout">
  <p>Se state pianificando un'indagine, valutando un dataset che non siete sicuri di dover accettare, o impostando i requisiti di una campagna in arrivo, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
]
