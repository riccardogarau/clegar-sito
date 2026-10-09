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
        'id': 'seconda-opinione',
        'topic': 'advisory',
        'date': '2026-10-09',
        'slug': {'it': 'seconda-opinione-prima-dell-accettazione',
                 'en': 'second-opinion-before-acceptance'},
        'title': {
            'it': 'La seconda opinione prima di firmare un’accettazione: che cosa il QC del contractor non controlla',
            'en': 'A second opinion before signing an acceptance: what the contractor’s QC does not check',
        },
        'meta_title': {
            'it': 'La seconda opinione prima dell’accettazione | Insights',
            'en': 'A second opinion before acceptance | Insights',
        },
        'desc': {
            'it': ('Perché una seconda opinione che rilegge il QC del contractor arriva alle sue stesse '
                   'conclusioni, e che cosa va controllato prima di firmare un’accettazione: le '
                   'assunzioni del deliverable, confrontate con dati indipendenti.'),
            'en': ('Why a second opinion that re-reads the contractor’s QC reaches the same conclusions, '
                   'and what to check before signing an acceptance: the assumptions behind the '
                   'deliverable, set against independent data.'),
        },
        'abstract': {
            'it': ('Una mappa di spessori consegnata in metri, convertita da tempi con una velocità che '
                   'sulla mappa non compare. Cinque CPT già pagati dicevano che quella velocità era '
                   'troppo alta, e l’errore spostava 7,5 km di tracciato – un quarto di quello adatto '
                   'al jetting – nella classe sbagliata.'),
            'en': ('A thickness map delivered in metres, converted from time with a velocity that does '
                   'not appear on the map. Five CPTs already paid for showed that velocity was too '
                   'high, and the error moved 7.5 km of route – a quarter of the length suited to '
                   'jetting – into the wrong class.'),
        },
        'body': {
            'it': """
<p class="lede">Prima di firmare l'accettazione di un deliverable di interpretazione, il committente riceve il rapporto di QC del contractor: le verifiche previste dalla specifica, tutte superate. Una seconda opinione che rilegge quel rapporto arriva quasi sempre alla stessa conclusione, perché controlla le stesse cose.</p>

<p>Il QC del contractor verifica che il lavoro sia coerente con sé stesso: che gli orizzonti siano tracciati con continuità, che agli incroci delle linee lo stesso riflettore cada alla stessa profondità, che i file siano nel formato richiesto. Non verifica, perché non è il suo compito, le scelte su cui l'interpretazione si regge. Una seconda opinione utile comincia da lì: dalle assunzioni che il deliverable dà per scontate, messe a confronto con dati che il contractor non ha usato per produrlo.</p>

<h2>Il numero che non compare sulla mappa</h2>

<p>Un profilatore sub-bottom non misura profondità sotto il fondale: misura tempi. Il riflettore che segna la base dei sedimenti soffici arriva qualche millesimo di secondo dopo l'eco del fondale, e per trasformare quel ritardo in metri serve la velocità di propagazione nei sedimenti. Lo spessore è quella velocità moltiplicata per il tempo di andata e ritorno, diviso due.</p>

<p>Lungo un tracciato quella velocità raramente si misura. Si assume: un valore unico per tutta l'unità, scritto in un'appendice del rapporto. La mappa consegnata al committente riporta metri, e la velocità che li ha prodotti non vi compare. Non è la velocità del suono in acqua, che si misura con un profilo a ogni campagna: è quella nei sedimenti, che nessun profilo misura.</p>

<p>I sedimenti fini superficiali, ricchi d'acqua, propagano il suono a velocità vicine a quella dell'acqua di mare. Un valore assunto più alto produce spessori più grandi in proporzione: una velocità più alta del 10% dà spessori più grandi del 10%, su tutta la mappa.</p>

<h2>Un esempio pratico</h2>

<p>I valori che seguono sono sintetici – costruiti per illustrare il meccanismo, non tratti da progetti reali – ma le proporzioni sono quelle di un tracciato vero.</p>

<p>Un tracciato di cavo lungo 42 km. Il deliverable è la mappa dello spessore dei sedimenti soffici sopra uno strato di argilla consistente, convertita da tempi a metri con una velocità di 1650 m/s. Chi progetta l'interramento ha fissato un criterio: dove i sedimenti soffici superano 1,8 m il cavo si interra con un mezzo a getti d'acqua, il jetting; dove sono meno, serve un mezzo diverso. La mappa diventa così una classificazione del tracciato, tratto per tratto.</p>

<p>Lungo il tracciato ci sono cinque CPT della campagna geotecnica, ciascuno entro 10 m dalla linea sismica più vicina. In ogni CPT il passaggio all'argilla consistente si legge come un aumento netto della resistenza di punta: è una profondità misurata, indipendente dalla velocità assunta, e il contractor geofisico non l'ha usata per la conversione.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Punto</th><th class="num">Ritardo del riflettore (ms)</th><th class="num">Spessore dalla mappa (m)</th><th class="num">Profondità al CPT (m)</th><th class="num">Differenza (m)</th><th class="num">Velocità implicita (m/s)</th></tr>
</thead>
<tbody>
<tr><td>CPT-01</td><td class="num">3,20</td><td class="num">2,64</td><td class="num">2,43</td><td class="num">0,21</td><td class="num">1519</td></tr>
<tr><td>CPT-02</td><td class="num">2,30</td><td class="num">1,90</td><td class="num">1,74</td><td class="num">0,16</td><td class="num">1513</td></tr>
<tr><td>CPT-03</td><td class="num">4,00</td><td class="num">3,30</td><td class="num">3,05</td><td class="num">0,25</td><td class="num">1525</td></tr>
<tr><td>CPT-04</td><td class="num">1,90</td><td class="num">1,57</td><td class="num">1,44</td><td class="num">0,13</td><td class="num">1516</td></tr>
<tr><td>CPT-05</td><td class="num">2,80</td><td class="num">2,31</td><td class="num">2,14</td><td class="num">0,17</td><td class="num">1529</td></tr>
</tbody>
</table>
</div>

<p>In tutti e cinque i punti la mappa dà uno spessore maggiore di quello trovato dal CPT. La velocità che riconcilia tempi e profondità – il doppio della profondità al CPT diviso il ritardo – sta fra 1513 e 1529 m/s, con una media di 1520 m/s. Con la velocità assunta, ogni spessore della mappa risulta più grande dell'8,6% di quello che si ottiene con la velocità dei CPT.</p>

<h2>Perché l'8,6% diventa un quarto del tracciato</h2>

<p>Un errore dell'8,6% sullo spessore, preso da solo, sembra tollerabile. Ma la mappa non viene letta per i suoi spessori: viene usata per classificare il tracciato rispetto a una soglia. E vicino alla soglia un errore proporzionale non sposta un numero, sposta interi tratti da una classe all'altra.</p>

<p>La soglia di 1,8 m corrisponde, a 1650 m/s, a un ritardo di 2,18 ms; a 1520 m/s, a un ritardo di 2,37 ms. Ogni tratto in cui il riflettore arriva fra 2,18 e 2,37 ms dopo il fondale è adatto al jetting secondo la mappa consegnata, e non lo è secondo i CPT.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Ritardo del riflettore</th><th class="num">Tracciato (km)</th><th>Secondo la mappa (1650 m/s)</th><th>Secondo i CPT (1520 m/s)</th></tr>
</thead>
<tbody>
<tr><td>meno di 2,18 ms</td><td class="num">11,0</td><td>meno di 1,8 m</td><td>meno di 1,8 m</td></tr>
<tr><td>da 2,18 a 2,37 ms</td><td class="num">7,5</td><td>jetting</td><td>meno di 1,8 m</td></tr>
<tr><td>2,37 ms e oltre</td><td class="num">23,5</td><td>jetting</td><td>jetting</td></tr>
<tr><td><strong>Totale</strong></td><td class="num"><strong>42,0</strong></td><td></td><td></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>7,5 km</strong><span>di tracciato adatto al jetting sulla mappa, e non nei CPT</span></div>

<p>La mappa consegnata dà 31,0 km adatti al jetting, il 74% del tracciato. Con la velocità dei CPT sono 23,5 km, il 56%. I 7,5 km che cambiano classe sono il 24% della lunghezza che il progettista considerava risolta: quasi un quarto. Il CPT-02 cade proprio in quella fascia: la mappa vi indica 1,90 m, il CPT trova l'argilla consistente a 1,74 m.</p>

<p>Finché la mappa resta una mappa, un errore di spessore resta un errore di spessore, e nessuno lo nota. Diventa un costo quando la mappa diventa la base su cui un altro contractor sceglie i mezzi e quota l'interramento.</p>

<h2>Le obiezioni che arriveranno</h2>

<p>La prima: la velocità di conversione è un'assunzione dichiarata, e il rapporto attribuisce agli spessori un'incertezza del 10%. È vero, ed è il motivo per cui la seconda opinione deve guardarci. Un'assunzione che si può confrontare con dati già in mano al committente non è un'incertezza: è una verifica non fatta. E un'incertezza scritta nel testo non cambia la mappa, perché la classificazione è disegnata sul valore centrale, ed è quella che arriva al progettista.</p>

<p>La seconda è più seria: il riflettore sismico e il passaggio di resistenza nel CPT non sono la stessa superficie. Il contrasto acustico può cadere un po' sopra o un po' sotto il punto in cui la resistenza di punta aumenta, e il CPT non sta esattamente sulla linea. Anche questo è vero, ma produce un errore di forma diversa. Uno scarto fra le due superfici sposterebbe tutte le profondità della stessa quantità in metri; un errore di velocità le sposta in proporzione allo spessore. Nell'esempio le differenze crescono con lo spessore – 0,13 m dove la mappa dà 1,57 m, 0,25 m dove ne dà 3,30 – e restano tutte fra il 7% e il 9% dello spessore della mappa. È la firma di una velocità, non di uno scarto.</p>

<p>Resta il caso. Se gli errori fossero casuali, con la stessa probabilità di cadere da una parte o dall'altra, cinque differenze dello stesso segno capiterebbero una volta su trentadue. Non basta a escluderlo, ma basta a non firmare senza una spiegazione.</p>

<h2>Che cosa non fa una seconda opinione</h2>

<p>Non rifà l'interpretazione. Nell'esempio non serve ritracciare un solo orizzonte: serve una tabella di cinque righe, costruita con dati che il committente ha già pagato. Il lavoro della seconda opinione è sapere dove guardare – le assunzioni che il deliverable non mostra, e l'uso che ne verrà fatto – e farlo prima della firma.</p>

<p>Il momento conta. Prima dell'accettazione, una nuova conversione con una velocità tarata sui CPT è una correzione dentro il contratto di survey. Dopo, il dato è passato a chi progetta e a chi installa, e la stessa correzione diventa un lavoro nuovo, oppure una contestazione.</p>

<h2>Cosa richiedere nella specifica</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>La velocità di conversione scritta sulla mappa, non solo nel rapporto.</strong><span class="t"> Per ogni unità, con la sua origine: misurata, tarata su dati geotecnici, oppure assunta dalla letteratura.</span></span></li>
  <li><span class="k">02</span><span><strong>Una tabella di taratura su ogni CPT o carotaggio disponibile.</strong><span class="t"> Ritardo, spessore convertito, profondità geotecnica, differenza e velocità implicita: la tabella dell'esempio, che costa poche ore a chi ha già i dati.</span></span></li>
  <li><span class="k">03</span><span><strong>La taratura prima dell'accettazione, non dopo.</strong><span class="t"> Se i dati geotecnici arrivano più tardi, la specifica prevede che la conversione venga rivista al loro arrivo, e l'accettazione la aspetta.</span></span></li>
  <li><span class="k">04</span><span><strong>Le soglie d'uso dichiarate al contractor.</strong><span class="t"> Se la mappa servirà a classificare il tracciato rispetto a uno spessore, il contractor deve saperlo, e indicare la fascia di ritardi in cui la classe dipende dalla velocità scelta.</span></span></li>
  <li><span class="k">05</span><span><strong>I ritardi consegnati insieme agli spessori.</strong><span class="t"> Con i tempi in mano, una conversione diversa si rifà in un giorno; senza, si rifà l'interpretazione.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Un rapporto di QC dice se il lavoro è stato fatto come la specifica chiedeva. Non dice se le scelte che la specifica lasciava al contractor reggono il confronto con il resto dei dati del progetto. È lì che una seconda opinione serve, ed è lì che di solito nessuno guarda, perché ogni verifica prevista risulta superata.</p>

<p>Nell'esempio la mappa era corretta per la velocità con cui era stata costruita; era la velocità a non essere controllata. Il controllo esisteva già, in cinque CPT, e mancava soltanto qualcuno che li mettesse accanto alla mappa prima della firma.</p>

<h3>Riferimenti</h3>

<ul>
  <li>ISO 19901-10:2021, <em>Petroleum and natural gas industries – Specific requirements for offshore structures – Part 10: Marine geophysical investigations</em> – requisiti per le indagini geofisiche marine, compresi la mappatura del sottofondo e il reporting.</li>
  <li>E. L. Hamilton, «Geoacoustic modeling of the sea floor», <em>Journal of the Acoustical Society of America</em>, 68(5), 1980, pp. 1313–1340 – proprietà acustiche dei sedimenti marini, velocità di propagazione comprese.</li>
</ul>

<div class="callout">
  <p>CLEGAR fornisce pareri tecnici indipendenti su deliverable geofisici e ground model, prima di un'accettazione o nel corso di una due diligence. Se state per firmare un'accettazione, o volete sapere su quali assunzioni si regge un dataset che vi è stato consegnato, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">Before signing the acceptance of an interpretation deliverable, the client receives the contractor's QC report: the checks the specification called for, all passed. A second opinion that re-reads that report almost always reaches the same conclusion, because it checks the same things.</p>

<p>The contractor's QC verifies that the work is consistent with itself: that horizons are picked continuously, that at line crossings the same reflector falls at the same depth, that the files are in the required format. It does not verify, because that is not its job, the choices the interpretation rests on. A useful second opinion starts there: with the assumptions the deliverable takes for granted, set against data the contractor did not use to produce it.</p>

<h2>The number that is not on the map</h2>

<p>A sub-bottom profiler does not measure depth below the seabed: it measures time. The reflector marking the base of the soft sediments arrives a few milliseconds after the seabed echo, and turning that delay into metres takes the propagation velocity in the sediments. The thickness is that velocity multiplied by the two-way time, divided by two.</p>

<p>Along a route that velocity is rarely measured. It is assumed: a single value for the whole unit, written in an appendix of the report. The map delivered to the client shows metres, and the velocity that produced them does not appear on it. This is not the sound velocity in water, which is measured with a profile on every campaign: it is the velocity in the sediments, which no profile measures.</p>

<p>Fine-grained surface sediments, rich in water, carry sound at velocities close to that of seawater. An assumed value that is too high produces thicknesses that are too large in proportion: a velocity 10% higher gives thicknesses 10% larger, across the whole map.</p>

<h2>A worked example</h2>

<p>The figures below are illustrative – built to show the mechanism, not taken from real projects – but the proportions are those of a real route.</p>

<p>A cable route 42 km long. The deliverable is a map of the thickness of soft sediments above a layer of stiff clay, converted from time to metres with a velocity of 1650 m/s. The burial designer has set a criterion: where the soft sediments exceed 1.8 m the cable is buried with a water-jetting tool; where they are thinner, a different tool is needed. The map thus becomes a classification of the route, section by section.</p>

<p>Along the route there are five CPTs from the geotechnical campaign, each within 10 m of the nearest seismic line. In each CPT the transition to stiff clay shows as a sharp increase in cone resistance: a measured depth, independent of the assumed velocity, and the geophysical contractor did not use it for the conversion.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Location</th><th class="num">Reflector delay (ms)</th><th class="num">Thickness from map (m)</th><th class="num">Depth at CPT (m)</th><th class="num">Difference (m)</th><th class="num">Implied velocity (m/s)</th></tr>
</thead>
<tbody>
<tr><td>CPT-01</td><td class="num">3.20</td><td class="num">2.64</td><td class="num">2.43</td><td class="num">0.21</td><td class="num">1519</td></tr>
<tr><td>CPT-02</td><td class="num">2.30</td><td class="num">1.90</td><td class="num">1.74</td><td class="num">0.16</td><td class="num">1513</td></tr>
<tr><td>CPT-03</td><td class="num">4.00</td><td class="num">3.30</td><td class="num">3.05</td><td class="num">0.25</td><td class="num">1525</td></tr>
<tr><td>CPT-04</td><td class="num">1.90</td><td class="num">1.57</td><td class="num">1.44</td><td class="num">0.13</td><td class="num">1516</td></tr>
<tr><td>CPT-05</td><td class="num">2.80</td><td class="num">2.31</td><td class="num">2.14</td><td class="num">0.17</td><td class="num">1529</td></tr>
</tbody>
</table>
</div>

<p>At all five locations the map gives a greater thickness than the CPT found. The velocity that reconciles times and depths – twice the depth at the CPT divided by the delay – lies between 1513 and 1529 m/s, with a mean of 1520 m/s. With the assumed velocity, every thickness on the map is 8.6% larger than the one obtained with the CPT velocity.</p>

<h2>Why 8.6% becomes a quarter of the route</h2>

<p>An 8.6% error in thickness, taken on its own, looks tolerable. But the map is not read for its thicknesses: it is used to classify the route against a threshold. And near the threshold a proportional error does not shift a number, it shifts whole sections from one class to the other.</p>

<p>The 1.8 m threshold corresponds, at 1650 m/s, to a delay of 2.18 ms; at 1520 m/s, to a delay of 2.37 ms. Every section where the reflector arrives between 2.18 and 2.37 ms after the seabed is suited to jetting according to the delivered map, and is not according to the CPTs.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Reflector delay</th><th class="num">Route (km)</th><th>According to the map (1650 m/s)</th><th>According to the CPTs (1520 m/s)</th></tr>
</thead>
<tbody>
<tr><td>under 2.18 ms</td><td class="num">11.0</td><td>under 1.8 m</td><td>under 1.8 m</td></tr>
<tr><td>2.18 to 2.37 ms</td><td class="num">7.5</td><td>jetting</td><td>under 1.8 m</td></tr>
<tr><td>2.37 ms and over</td><td class="num">23.5</td><td>jetting</td><td>jetting</td></tr>
<tr><td><strong>Total</strong></td><td class="num"><strong>42.0</strong></td><td></td><td></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>7.5 km</strong><span>of route suited to jetting on the map, and not in the CPTs</span></div>

<p>The delivered map gives 31.0 km suited to jetting, 74% of the route. With the CPT velocity it is 23.5 km, 56%. The 7.5 km that change class are 24% of the length the designer considered settled: nearly a quarter. CPT-02 falls right in that band: the map shows 1.90 m there, and the CPT finds the stiff clay at 1.74 m.</p>

<p>As long as the map stays a map, a thickness error stays a thickness error, and nobody notices it. It becomes a cost when the map becomes the basis on which another contractor chooses its tools and prices the burial.</p>

<h2>The objections that will come</h2>

<p>The first: the conversion velocity is a declared assumption, and the report gives the thicknesses an uncertainty of 10%. True, and that is why the second opinion has to look at it. An assumption that can be checked against data the client already holds is not an uncertainty: it is a check not made. And an uncertainty written in the text does not change the map, because the classification is drawn on the central value, and that is what reaches the designer.</p>

<p>The second is more serious: the seismic reflector and the resistance transition in the CPT are not the same surface. The acoustic contrast may fall slightly above or below the point where cone resistance rises, and the CPT is not exactly on the line. That is also true, but it produces an error of a different shape. An offset between the two surfaces would shift every depth by the same amount in metres; a velocity error shifts them in proportion to the thickness. In the example the differences grow with the thickness – 0.13 m where the map shows 1.57 m, 0.25 m where it shows 3.30 – and all stay between 7% and 9% of the map thickness. That is the signature of a velocity, not of an offset.</p>

<p>That leaves chance. If the errors were random, equally likely to fall either way, five differences of the same sign would occur once in thirty-two. That is not enough to rule it out, but it is enough not to sign without an explanation.</p>

<h2>What a second opinion does not do</h2>

<p>It does not redo the interpretation. In the example not a single horizon needs re-picking: what is needed is a five-row table, built from data the client has already paid for. The work of a second opinion is knowing where to look – the assumptions the deliverable does not show, and the use it will be put to – and doing so before the signature.</p>

<p>Timing matters. Before acceptance, a new conversion with a velocity calibrated on the CPTs is a correction within the survey contract. Afterwards, the data has passed to those who design and those who install, and the same correction becomes new work, or a claim.</p>

<h2>What to require in the specification</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>The conversion velocity written on the map, not only in the report.</strong><span class="t"> For each unit, with its origin: measured, calibrated on geotechnical data, or assumed from the literature.</span></span></li>
  <li><span class="k">02</span><span><strong>A calibration table on every available CPT or core.</strong><span class="t"> Delay, converted thickness, geotechnical depth, difference and implied velocity: the table in the example, which costs a few hours to whoever already has the data.</span></span></li>
  <li><span class="k">03</span><span><strong>Calibration before acceptance, not after.</strong><span class="t"> If the geotechnical data arrives later, the specification provides for the conversion to be revised when it arrives, and acceptance waits for it.</span></span></li>
  <li><span class="k">04</span><span><strong>The thresholds of use declared to the contractor.</strong><span class="t"> If the map will be used to classify the route against a thickness, the contractor must know it, and show the band of delays in which the class depends on the chosen velocity.</span></span></li>
  <li><span class="k">05</span><span><strong>The delays delivered together with the thicknesses.</strong><span class="t"> With the times in hand, a different conversion is redone in a day; without them, the interpretation is redone.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>A QC report says whether the work was done as the specification asked. It does not say whether the choices the specification left to the contractor stand up against the rest of the project's data. That is where a second opinion is useful, and that is where nobody usually looks, because every check called for has been passed.</p>

<p>In the example the map was correct for the velocity it was built with; it was the velocity that went unchecked. The check already existed, in five CPTs, and all that was missing was someone to set them beside the map before the signature.</p>

<h3>References</h3>

<ul>
  <li>ISO 19901-10:2021, <em>Petroleum and natural gas industries – Specific requirements for offshore structures – Part 10: Marine geophysical investigations</em> – requirements for marine geophysical investigations, including sub-seafloor mapping and reporting.</li>
  <li>E. L. Hamilton, "Geoacoustic modeling of the sea floor", <em>Journal of the Acoustical Society of America</em>, 68(5), 1980, pp. 1313–1340 – acoustic properties of marine sediments, including propagation velocity.</li>
</ul>

<div class="callout">
  <p>CLEGAR provides independent technical opinions on geophysical deliverables and ground models, before an acceptance or in the course of a due diligence. If you are about to sign an acceptance, or want to know which assumptions a dataset you have been given rests on, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'witnessing-calibrazione',
        'topic': 'owners',
        'date': '2026-10-08',
        'slug': {'it': 'witnessing-di-una-calibrazione',
                 'en': 'witnessing-a-calibration'},
        'title': {
            'it': 'Il witnessing di una calibrazione: che cosa si firma e che cosa si guarda',
            'en': 'Witnessing a calibration: what you sign and what you look at',
        },
        'meta_title': {
            'it': 'Il witnessing di una calibrazione | Insights',
            'en': 'Witnessing a calibration | Insights',
        },
        'desc': {
            'it': ('Perché il valore sul certificato di un patch test non dice se la calibrazione '
                   'ha funzionato, e qual è l’unico dato che lo direbbe: il residuo di una passata '
                   'di conferma sui fasci esterni.'),
            'en': ('Why the value on a patch test certificate does not say whether the calibration '
                   'worked, and what the one figure that would is: the residual of a confirmation '
                   'pass on the outer beams.'),
        },
        'abstract': {
            'it': ('Correzione giusta o segno rovesciato, il certificato scrive la stessa riga. '
                   'In mezzo ci sono 0,02 m di residuo contro 0,40 m, cioè il 63% del TVU ammesso '
                   'dall’Ordine 1a consumato da un errore di segno – e a distinguerli serve una passata '
                   'che quasi nessuna specifica richiede.'),
            'en': ('Right correction or reversed sign, the certificate records the same line. '
                   'Between them lie 0.02 m of residual and 0.40 m, or 63% of the TVU allowed by '
                   'Order 1a spent on a sign error – and telling them apart takes a pass that '
                   'almost no specification asks for.'),
        },
        'body': {
            'it': """
<p class="lede">Al termine di una calibrazione il rappresentante del committente firma un certificato. La firma attesta che la prova è stata eseguita in sua presenza. Non attesta che la calibrazione abbia funzionato, e quasi mai il certificato contiene il dato che lo direbbe.</p>

<p>Il certificato riporta il valore determinato: un disallineamento di roll di tot gradi, applicato. Quel numero da solo non distingue una calibrazione che ha corretto l'errore da una che lo ha raddoppiato. Sono esiti opposti, e sul foglio si scrivono nello stesso modo.</p>

<h2>Che cosa determina un patch test</h2>

<p>Per il roll la prova è una linea percorsa due volte in direzioni opposte sopra un fondale piano, e si guardano i fasci esterni. Un disallineamento di roll inclina lo swath: a una distanza trasversale dal nadir produce un errore di profondità proporzionale a quella distanza, positivo da un lato e negativo dall'altro. Invertendo la rotta, lo stesso punto del fondo viene misurato dal lato opposto, e l'errore cambia segno.</p>

<p>Da qui il metodo: la differenza fra le due passate a una data distanza dal nadir vale il doppio dell'errore, e il disallineamento si ricava dividendo per due volte quella distanza. È una grandezza che non si misura, si deduce da una differenza – ed è per questo che il modo in cui la differenza viene letta conta quanto lo strumento.</p>

<h2>Un esempio pratico</h2>

<p>I valori che seguono sono sintetici – costruiti per illustrare il meccanismo, non tratti da progetti reali – ma le proporzioni sono quelle di una campagna vera.</p>

<p>Fondale piano a 30 m, swath utile fino a 100 m per lato: a quella distanza il fascio esterno guarda a 73 gradi dal nadir. Le due passate reciproche differiscono di 0,20 m sui fasci esterni, che corrisponde a un disallineamento di roll di 0,057 gradi. Il valore viene determinato e applicato, e il certificato viene firmato.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Esito della correzione</th><th class="num">Differenza fra le passate</th><th class="num">Quota del TVU Ordine 1a a 30 m</th></tr>
</thead>
<tbody>
<tr><td>Nessuna correzione</td><td class="num">0,20 m</td><td class="num">32%</td></tr>
<tr><td>Correzione applicata col segno giusto</td><td class="num">0,02 m</td><td class="num">3%</td></tr>
<tr><td>Correzione applicata col segno sbagliato</td><td class="num">0,40 m</td><td class="num">63%</td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>63%</strong><span>del TVU consumato da un errore di segno</span></div>

<p>Il TVU ammesso dall'Ordine 1a della IHO S-44 a 30 m di profondità è 0,634 m. Applicare la correzione col segno rovesciato non lascia l'errore dov'era: lo raddoppia, perché al disallineamento reale si somma una correzione che punta nella stessa direzione. E il certificato, in tutti e tre i casi della tabella, riporta la stessa riga: disallineamento di roll 0,057 gradi, applicato.</p>

<h2>Che cosa si guarda, allora</h2>

<p>Una sola cosa, e non è il valore: la <strong>passata di conferma</strong> eseguita dopo aver applicato la correzione, con il residuo misurato sugli stessi fasci esterni. Se il residuo è sceso, la calibrazione ha funzionato. Se è salito, il segno è rovesciato. Senza quella passata non esiste alcuna prova che la correzione abbia migliorato qualcosa, e la firma attesta soltanto che qualcuno era presente.</p>

<p>Conta anche dove si guarda. L'errore da roll è nullo al nadir e massimo ai bordi dello swath: un controllo sulla profondità media, o sui fasci centrali, non vede né il caso corretto né quello rovesciato. È il motivo per cui il patch test si legge sui fasci esterni, e per cui un residuo dichiarato senza dire a quale distanza dal nadir è stato misurato non è un residuo.</p>

<h2>L'obiezione che arriverà</h2>

<p>Il contractor risponderà che del segno si occupa il software, e che un segno rovesciato sarebbe evidente. La prima parte è vera e la seconda no: è evidente solo a chi guarda una passata di conferma sui fasci esterni, che è esattamente la cosa che manca.</p>

<p>E il punto non è il software, sono i due software. La convenzione di segno del roll – positivo con il lato sinistro in alto, oppure con il destro – non è universale, e il valore viaggia dal programma che lo determina al progetto di processing attraverso un foglio firmato, dove compare come numero senza la convenzione che lo definisce. Ogni passaggio in cui un numero cambia programma è un passaggio in cui può cambiare segno.</p>

<h2>Quello che una sola passata non distingue</h2>

<p>C'è una seconda ragione per cui le due passate devono essere reciproche e non una ripetizione nella stessa direzione, e riguarda una grandezza diversa. Anche un errore di velocità del suono inclina i bordi dello swath, incurvandoli verso l'alto o verso il basso. Su una sola passata l'effetto somiglia a quello del roll.</p>

<p>Le due si separano dal comportamento al cambio di rotta. L'errore da roll è antisimmetrico: cresce da un lato e cala dall'altro, quindi invertendo la rotta si rovescia. L'errore da velocità del suono dipende dall'inclinazione del fascio e non dal lato: è simmetrico, e invertendo la rotta resta com'era.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Grandezza</th><th>Al cambio di rotta</th><th>Si isola con</th></tr>
</thead>
<tbody>
<tr><td>Disallineamento di roll</td><td>si rovescia</td><td>la differenza fra le due passate</td></tr>
<tr><td>Errore di velocità del suono</td><td>resta com'è</td><td>la somma delle due passate</td></tr>
</tbody>
</table>
</div>

<p>Due passate reciproche danno quindi due informazioni, non una: la differenza misura il roll, la somma misura quanto profilo di velocità del suono sbagliato c'è ancora dentro il dato. Chiedere entrambe costa la stessa nave e la stessa ora.</p>

<h2>Cosa richiedere nella specifica</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>La passata di conferma come parte della prova, non come extra.</strong><span class="t"> La calibrazione non è conclusa quando il valore è determinato, ma quando una passata successiva mostra il residuo con la correzione attiva.</span></span></li>
  <li><span class="k">02</span><span><strong>Il residuo dichiarato con la distanza dal nadir a cui è misurato.</strong><span class="t"> Un residuo senza quella distanza non è confrontabile con niente, perché l'errore che deve rilevare vale zero al centro dello swath.</span></span></li>
  <li><span class="k">03</span><span><strong>La convenzione di segno scritta accanto al valore.</strong><span class="t"> Nel certificato e nel progetto di processing, non nella memoria di chi ha fatto la prova. È l'unico modo di rendere verificabile il passaggio del numero da un programma all'altro.</span></span></li>
  <li><span class="k">04</span><span><strong>Due passate reciproche, e la somma oltre alla differenza.</strong><span class="t"> La differenza dà il roll, la somma dà il residuo di velocità del suono. Una ripetizione nella stessa direzione non separa le due cause.</span></span></li>
  <li><span class="k">05</span><span><strong>Il profilo di velocità del suono della prova, allegato con ora e posizione.</strong><span class="t"> Un patch test su un profilo scaduto attribuisce al montaggio un errore che è di propagazione, e lo congela in una costante.</span></span></li>
  <li><span class="k">06</span><span><strong>I valori applicati verificati nel progetto, non nel certificato.</strong><span class="t"> Il certificato dice che cosa è stato determinato; solo il progetto di processing dice che cosa agisce davvero sul dato consegnato.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Il witnessing costa una giornata di un tecnico e produce, nella forma consueta, una firma su un numero. Nella forma utile produce un residuo: una misura di quanto l'errore sia diminuito dopo la correzione, letta dove quell'errore è grande.</p>

<p>La differenza fra le due forme non sta nella diligenza di chi assiste, ma in che cosa la specifica gli ha chiesto di guardare. Se la prova prevede una sola passata, il rappresentante più scrupoloso del mondo può firmare in buona fede una calibrazione che ha peggiorato il dato del doppio.</p>

<h3>Riferimenti</h3>

<ul>
  <li>IHO C-13, <em>Manual on Hydrography</em> (1ª edizione, 2005) – verifica e calibrazione dei sistemi di rilievo, patch test per gli angoli di assetto.</li>
  <li>IHO S-44, <em>Standards for Hydrographic Surveys</em> – Ordine 1a: TVU con a = 0,50 m e b = 0,013, da cui 0,634 m a 30 m di profondità.</li>
</ul>

<div class="callout">
  <p>CLEGAR rappresenta il committente a bordo e in banchina, e verifica in modo indipendente le prove di sistema e i dati che ne derivano. Se state scrivendo la specifica di una calibrazione, o state valutando un certificato che vi è stato consegnato, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">At the end of a calibration the client representative signs a certificate. The signature attests that the test was carried out in their presence. It does not attest that the calibration worked, and the certificate almost never carries the figure that would say so.</p>

<p>The certificate records the value determined: a roll misalignment of so many degrees, applied. That number on its own does not distinguish a calibration that removed the error from one that doubled it. Those are opposite outcomes, and on the sheet they are written the same way.</p>

<h2>What a patch test determines</h2>

<p>For roll, the test is one line run twice in opposite directions over a flat seabed, read on the outer beams. A roll misalignment tilts the swath: at a given across-track distance from nadir it produces a depth error proportional to that distance, positive on one side and negative on the other. Reverse the heading, and the same patch of seabed is measured from the opposite side, so the error changes sign.</p>

<p>Hence the method: the difference between the two passes at a given distance from nadir is twice the error, and the misalignment follows from dividing by twice that distance. It is a quantity that is not measured but inferred from a difference – which is why how the difference is read matters as much as the instrument.</p>

<h2>A worked example</h2>

<p>The figures below are illustrative – built to show the mechanism, not taken from real projects – but the proportions are those of a real campaign.</p>

<p>A flat seabed at 30 m, with usable swath out to 100 m each side: at that distance the outer beam looks 73 degrees off nadir. The two reciprocal passes differ by 0.20 m on the outer beams, which corresponds to a roll misalignment of 0.057 degrees. The value is determined and applied, and the certificate is signed.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Outcome of the correction</th><th class="num">Difference between passes</th><th class="num">Share of Order 1a TVU at 30 m</th></tr>
</thead>
<tbody>
<tr><td>No correction</td><td class="num">0.20 m</td><td class="num">32%</td></tr>
<tr><td>Correction applied with the right sign</td><td class="num">0.02 m</td><td class="num">3%</td></tr>
<tr><td>Correction applied with the wrong sign</td><td class="num">0.40 m</td><td class="num">63%</td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>63%</strong><span>of the TVU spent on a sign error</span></div>

<p>The TVU allowed by IHO S-44 Order 1a at 30 m depth is 0.634 m. Applying the correction with the sign reversed does not leave the error where it was: it doubles it, because a correction pointing the same way as the real misalignment adds to it. And in all three rows of the table the certificate records the same line: roll misalignment 0.057 degrees, applied.</p>

<h2>What to look at instead</h2>

<p>One thing, and it is not the value: the <strong>confirmation pass</strong> run after the correction has been applied, with the residual measured on the same outer beams. If the residual has fallen, the calibration worked. If it has risen, the sign is reversed. Without that pass there is no evidence at all that the correction improved anything, and the signature attests only that somebody was present.</p>

<p>Where you look matters too. Roll error is zero at nadir and largest at the edges of the swath: a check on mean depth, or on the central beams, sees neither the corrected case nor the reversed one. That is why a patch test is read on the outer beams, and why a residual quoted without saying at what distance from nadir it was measured is not a residual.</p>

<h2>The objection that will come</h2>

<p>The contractor will reply that the software handles the sign, and that a reversed sign would be obvious. The first part is true and the second is not: it is obvious only to someone looking at a confirmation pass on the outer beams, which is exactly what is missing.</p>

<p>And the issue is not the software, it is the two pieces of software. The roll sign convention – positive with the port side up, or with the starboard side up – is not universal, and the value travels from the program that determines it to the processing project by way of a signed sheet, where it appears as a number without the convention that defines it. Every step in which a number changes program is a step in which it can change sign.</p>

<h2>What a single pass cannot separate</h2>

<p>There is a second reason the two passes must be reciprocal rather than a repeat in the same direction, and it concerns a different quantity. A sound velocity error also tilts the edges of the swath, curving them up or down. On a single pass the effect resembles roll.</p>

<p>The two separate by how they behave when the heading reverses. Roll error is antisymmetric: it grows on one side and falls on the other, so reversing the heading flips it. Sound velocity error depends on the beam angle and not on the side: it is symmetric, and reversing the heading leaves it as it was.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Quantity</th><th>On reversing the heading</th><th>Isolated by</th></tr>
</thead>
<tbody>
<tr><td>Roll misalignment</td><td>flips</td><td>the difference between the two passes</td></tr>
<tr><td>Sound velocity error</td><td>stays as it is</td><td>the sum of the two passes</td></tr>
</tbody>
</table>
</div>

<p>Two reciprocal passes therefore give two pieces of information, not one: the difference measures roll, and the sum measures how much wrong sound velocity profile is still inside the data. Asking for both costs the same vessel and the same hour.</p>

<h2>What to require in the specification</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>The confirmation pass as part of the test, not as an extra.</strong><span class="t"> A calibration is not finished when the value has been determined, but when a subsequent pass shows the residual with the correction active.</span></span></li>
  <li><span class="k">02</span><span><strong>The residual quoted with the distance from nadir at which it was measured.</strong><span class="t"> A residual without that distance is comparable to nothing, because the error it has to detect is zero at the centre of the swath.</span></span></li>
  <li><span class="k">03</span><span><strong>The sign convention written next to the value.</strong><span class="t"> On the certificate and in the processing project, not in the memory of whoever ran the test. It is the only way to make the number's passage between programs verifiable.</span></span></li>
  <li><span class="k">04</span><span><strong>Two reciprocal passes, and the sum as well as the difference.</strong><span class="t"> The difference gives roll, the sum gives the residual sound velocity error. A repeat in the same direction does not separate the two causes.</span></span></li>
  <li><span class="k">05</span><span><strong>The sound velocity profile used for the test, attached with its time and position.</strong><span class="t"> A patch test run on an expired profile attributes a propagation error to the mounting, and freezes it into a constant.</span></span></li>
  <li><span class="k">06</span><span><strong>The applied values verified in the project, not on the certificate.</strong><span class="t"> The certificate says what was determined; only the processing project says what is actually acting on the delivered data.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>Witnessing costs one technician one day and produces, in its customary form, a signature on a number. In its useful form it produces a residual: a measure of how much the error fell after the correction, read where that error is large.</p>

<p>The difference between the two forms lies not in the diligence of whoever attends, but in what the specification asked them to look at. If the test calls for a single pass, the most scrupulous representative in the world can sign in good faith a calibration that made the data twice as bad.</p>

<h3>References</h3>

<ul>
  <li>IHO C-13, <em>Manual on Hydrography</em> (1st edition, 2005) – survey system verification and calibration, patch test for the attitude angles.</li>
  <li>IHO S-44, <em>Standards for Hydrographic Surveys</em> – Order 1a: TVU with a = 0.50 m and b = 0.013, giving 0.634 m at 30 m depth.</li>
</ul>

<div class="callout">
  <p>CLEGAR represents the client on board and on the quayside, and independently verifies system trials and the data that comes from them. If you are writing the specification for a calibration, or assessing a certificate you have been given, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'readiness-review',
        'topic': 'excellence',
        'date': '2026-10-05',
        'slug': {'it': 'readiness-review-prima-che-la-nave-parta',
                 'en': 'readiness-review-before-the-vessel-sails'},
        'title': {
            'it': 'Readiness review: che cosa si verifica prima che la nave parta',
            'en': 'Readiness review: what to check before the vessel sails',
        },
        'meta_title': {
            'it': 'Readiness review prima della partenza | Insights',
            'en': 'Readiness review before sailing | Insights',
        },
        'desc': {
            'it': ('Perché una checklist al 94% non dice se la nave può partire, e come si conduce '
                   'una readiness review sul margine delle voci aperte invece che sul numero di '
                   'voci chiuse.'),
            'en': ('Why a checklist at 94% does not tell you whether the vessel can sail, and how to '
                   'run a readiness review on the margin of the open items rather than on the count '
                   'of closed ones.'),
        },
        'abstract': {
            'it': ('Quarantotto voci, quarantacinque chiuse: il 94%. Fra le chiuse ce n’era una '
                   'verificata su una revisione superata del piano linee, con dieci giorni di '
                   'margine negativo. La percentuale scendeva di due punti, e la decisione di '
                   'partenza cambiava del tutto.'),
            'en': ('Forty-eight items, forty-five closed: 94%. Among the closed ones was an item '
                   'checked against a superseded revision of the line plan, ten days short of '
                   'being closable. The percentage dropped by two points, and the sailing decision '
                   'changed entirely.'),
        },
        'body': {
            'it': """
<p class="lede">Prima che una nave lasci la banchina per una campagna offshore, qualcuno presenta una tabella: quarantotto voci, quarantacinque chiuse, tre aperte e tutte in via di chiusura. Il 94%. La riunione dura un'ora e si chiude con la decisione di partire.</p>

<p>Quella tabella risponde a una domanda – quante voci sono chiuse – che non è quella per cui la riunione è stata convocata. La domanda di una readiness review è un'altra: c'è qualcosa che non si chiuderà prima del momento in cui servirà? A questa domanda la percentuale non risponde, nemmeno per approssimazione.</p>

<p>Qui si parla della readiness review in senso stretto: persone, documenti, permessi, interfacce, contingenze. La verifica della strumentazione in banchina – calibrazioni, offset, prove di sistema – è un controllo diverso, con regole proprie, e merita un articolo a sé.</p>

<h2>Perché la percentuale non misura la prontezza</h2>

<p>Una checklist tratta tutte le voci allo stesso modo: ciascuna vale una casella. Ma le voci non richiedono lo stesso tempo per essere chiuse. Un corso di aggiornamento si fa in un giorno; la modifica di un'autorizzazione dell'autorità marittima può richiedere settimane, e quel tempo non dipende da chi la chiede.</p>

<p>La prontezza di una campagna non è quindi la media delle voci. La decide la voce peggiore, e «peggiore» non vuol dire la più importante in astratto: vuol dire quella che richiede più tempo di quanto ne resti. Per ogni voce aperta conta una sola differenza, il margine: i giorni che mancano al momento in cui la voce servirà, meno i giorni che servono a chiuderla. Se il margine è positivo, la voce è un'attività da seguire. Se è negativo, è una decisione da prendere subito.</p>

<p>Una percentuale non contiene nessuno dei due numeri.</p>

<h2>Un esempio pratico</h2>

<p>I valori che seguono sono sintetici – costruiti per illustrare il meccanismo, non tratti da progetti reali – ma la struttura è ricorrente.</p>

<p>Una campagna geofisica con 20 giorni di acquisizione, in un'area a poche ore dal porto. La readiness review si tiene cinque giorni prima della partenza, per consuetudine. Lo stato presentato è questo:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Area</th><th class="num">Voci</th><th class="num">Chiuse</th><th class="num">Aperte</th></tr>
</thead>
<tbody>
<tr><td>Persone</td><td class="num">10</td><td class="num">9</td><td class="num">1</td></tr>
<tr><td>Nave</td><td class="num">8</td><td class="num">8</td><td class="num">0</td></tr>
<tr><td>Documenti e procedure</td><td class="num">12</td><td class="num">11</td><td class="num">1</td></tr>
<tr><td>Permessi</td><td class="num">6</td><td class="num">6</td><td class="num">0</td></tr>
<tr><td>Interfacce</td><td class="num">7</td><td class="num">6</td><td class="num">1</td></tr>
<tr><td>Contingenze</td><td class="num">5</td><td class="num">5</td><td class="num">0</td></tr>
<tr><td><strong>Totale</strong></td><td class="num"><strong>48</strong></td><td class="num"><strong>45</strong></td><td class="num"><strong>3</strong></td></tr>
</tbody>
</table>
</div>

<p>Le tre voci aperte, con il tempo necessario a chiuderle e il margine rispetto alla partenza:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Voce aperta</th><th class="num">Giorni per chiuderla</th><th class="num">Margine</th></tr>
</thead>
<tbody>
<tr><td>Formazione di base alla sicurezza offshore (BOSIET) di un tecnico, in scadenza a campagna in corso: aggiornamento FOET da prenotare e frequentare</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td>Procedura di recupero dello strumento trainato, in approvazione presso il committente</td><td class="num">3</td><td class="num">+2</td></tr>
<tr><td>Bridging document fra i sistemi di gestione HSE di committente e contractor, da firmare</td><td class="num">2</td><td class="num">+3</td></tr>
</tbody>
</table>
</div>

<p>Tutti i margini sono positivi, e la decisione di partire è coerente con i numeri presentati.</p>

<p>Il problema sta fra le voci chiuse. La voce «autorizzazione dell'area di lavoro» è spuntata: l'autorizzazione esiste, è valida, è archiviata. È stata però rilasciata sul poligono del piano linee in revisione B. Sette giorni prima della review – dodici prima della partenza – è stata emessa la revisione D, che aggiunge sei linee lungo una variante di tracciato di un cavo. Quattro di queste escono in parte dal poligono autorizzato.</p>

<p>Nessuno ha nascosto niente: la voce era stata chiusa prima che il piano linee cambiasse, e nessuna regola la riapriva. In questo esempio la modifica dell'autorizzazione richiede quindici giorni.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Voce aperta</th><th class="num">Giorni per chiuderla</th><th class="num">Margine</th></tr>
</thead>
<tbody>
<tr><td>Formazione di base alla sicurezza offshore</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td>Procedura di recupero</td><td class="num">3</td><td class="num">+2</td></tr>
<tr><td>Bridging document</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td><strong>Autorizzazione dell'area di lavoro, riaperta</strong></td><td class="num"><strong>15</strong></td><td class="num"><strong>−10</strong></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>−10</strong><span>giorni di margine, dentro una checklist al 94%</span></div>

<p>Con la voce riaperta, le voci chiuse passano da 45 su 48 a 44: dal 94% al 92%. Due punti percentuali, che in una presentazione nessuno noterebbe. Il margine della voce peggiore passa invece da +2 a −10 giorni, ed è questo numero che cambia la decisione.</p>

<h2>Che cosa si decide con un margine negativo</h2>

<p>Un margine negativo non vuol dire automaticamente che la nave resta in porto. Vuol dire che la decisione di partenza deve stabilire che cosa succede alle linee che non si possono ancora acquisire.</p>

<p>Nell'esempio le quattro linee fuori poligono richiedono in tutto due giorni di acquisizione. Se la nave parte alla data prevista, la modifica dell'autorizzazione arriva dieci giorni dopo la partenza: quindici giorni per ottenerla, meno i cinque che mancavano alla partenza. Con 20 giorni di acquisizione e due da riservare alle quattro linee, queste devono cominciare entro 18 giorni dalla partenza per non allungare la campagna. Fra l'arrivo atteso dell'autorizzazione e l'ultimo giorno utile restano otto giorni.</p>

<p>La decisione corretta è quindi: si parte, con una condizione scritta. Le quattro linee vanno in coda al programma; la modifica dell'autorizzazione ha un responsabile e una data attesa; se a 18 giorni dalla partenza non è arrivata, si sceglie fra prolungare il noleggio e rinunciare alle linee – e quella scelta la fissa oggi chi ne ha l'autorità, non la improvvisa quel giorno chi è a bordo.</p>

<p>È una decisione diversa da «si parte», e nessuno la prende se la tabella dice 94%.</p>

<h2>Il difetto non era nella voce, ma nel modo di chiuderla</h2>

<p>La voce sull'autorizzazione non era stata chiusa male. Era stata chiusa su un documento che poi è cambiato, e una checklist che registra solo lo stato – aperta o chiusa – non ha modo di accorgersene.</p>

<p>Il rimedio è registrare, per ogni voce chiusa, su quale revisione di quale documento è stata verificata: «autorizzazione verificata sul piano linee rev. B», non «autorizzazione presente». Quando esce la rev. D, ogni voce che dipende dal piano linee si riapre. Nell'esempio la voce si sarebbe riaperta dodici giorni prima della partenza, con un margine di −3 giorni invece di −10: ancora negativo, ma scoperto sette giorni prima, quando c'era tempo per sollecitare l'autorità o riordinare il programma a terra, invece che in mare.</p>

<h2>L'obiezione che arriverà</h2>

<p>Chi organizza la campagna risponderà che anticipare la review non risolve il problema: a quindici giorni dalla partenza metà delle voci non può essere chiusa. L'equipaggio non è ancora assegnato, la nave sta finendo un altro lavoro, le procedure aspettano la versione definitiva del piano linee. Una review anticipata produrrebbe soltanto un lungo elenco di voci aperte.</p>

<p>L'obiezione è corretta sui fatti, e indica come va fatta la review, non che vada rimandata. A quindici giorni dalla partenza non si verifica che le voci siano chiuse: si verifica che ognuna abbia un responsabile, un tempo di chiusura stimato e un margine positivo. Una voce aperta con dieci giorni di margine è in ordine. Una voce aperta di cui nessuno sa dire quanto tempo richieda è il risultato più utile che la review possa produrre.</p>

<p>Le passate sono quindi due, con scopi diversi. La prima, tenuta prima che il tempo residuo scenda sotto il tempo di chiusura più lungo della lista, verifica i margini. La seconda, a ridosso della partenza, verifica le chiusure. Tenerne una sola, cinque giorni prima per consuetudine, vuol dire fare la seconda credendo di aver fatto anche la prima.</p>

<h2>Cosa richiedere nella specifica</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Il tempo di chiusura accanto a ogni voce.</strong><span class="t"> Non soltanto aperta o chiusa: quanti giorni servono a chiuderla e chi la chiude. Senza quel numero il margine non si calcola, e senza margine la review conta caselle.</span></span></li>
  <li><span class="k">02</span><span><strong>Il margine della voce peggiore in testa al rapporto.</strong><span class="t"> Prima della percentuale, o al suo posto. È il numero su cui si decide la partenza, e deve essere il primo che legge chi non era alla riunione.</span></span></li>
  <li><span class="k">03</span><span><strong>Ogni chiusura legata alla revisione del documento verificato.</strong><span class="t"> Una nuova revisione di un documento riapre tutte le voci che dipendono da esso. Il piano linee, il programma e l'elenco del personale sono i documenti che cambiano più spesso nelle ultime settimane.</span></span></li>
  <li><span class="k">04</span><span><strong>Due passate, con le date fissate dal tempo di chiusura più lungo.</strong><span class="t"> La prima sui margini, la seconda sulle chiusure. Non una sola riunione in una data scelta per consuetudine.</span></span></li>
  <li><span class="k">05</span><span><strong>Le partenze condizionate scritte come tali.</strong><span class="t"> Se si parte con una voce a margine negativo, la decisione indica che cosa resta escluso, chi chiude la voce, entro quando, e che cosa si fa se non si chiude. Una condizione che vive solo nel verbale della riunione non arriva a bordo.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Una readiness review non serve a dimostrare che si è pronti. Serve a trovare, finché c'è tempo per agire, la voce che non si chiuderà in tempo. Una checklist al 94% dice che il lavoro è quasi finito; non dice se ciò che manca si può finire prima della partenza.</p>

<p>Fra le due cose c'è un numero per voce, il margine, che quasi nessuna checklist riporta e che costa pochissimo aggiungere. Va previsto nella specifica: il giorno della review la forma della tabella è già decisa.</p>

<h3>Riferimenti</h3>

<ul>
  <li>IOGP Report 423, <em>HSE management – guidelines for working together in a contract environment</em>, e il supplemento 423-02, <em>Guide to preparing HSE plans and Bridging documents</em>: il bridging document serve quando il lavoro, in tutto o in parte, si svolge con il sistema di gestione del contractor, ritenuto conforme ai requisiti di quello del committente.</li>
  <li>OPITO, standard BOSIET e FOET: il certificato BOSIET ha validità di quattro anni; l'aggiornamento è il corso FOET di un giorno, da frequentare mentre il certificato è ancora valido.</li>
</ul>

<div class="callout">
  <p>CLEGAR fornisce project management e technical assurance per campagne offshore, readiness review comprese. Se state preparando una campagna, o volete una verifica indipendente della prontezza prima della partenza, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">Before a vessel leaves the quay for an offshore campaign, somebody presents a table: forty-eight items, forty-five closed, three open and all on their way to closure. 94%. The meeting lasts an hour and ends with the decision to sail.</p>

<p>That table answers a question – how many items are closed – which is not the one the meeting was called for. The question of a readiness review is a different one: is there anything that will not be closed before the moment it is needed? The percentage does not answer it, not even approximately.</p>

<p>This article is about the readiness review in the strict sense: people, documents, permits, interfaces, contingencies. Verifying equipment on the quay – calibrations, offsets, system trials – is a different check, with rules of its own, and deserves an article of its own.</p>

<h2>Why the percentage does not measure readiness</h2>

<p>A checklist treats every item the same way: each one is worth one box. But items do not take the same time to close. A refresher course takes a day; amending a permit from the maritime authority can take weeks, and that time does not depend on whoever is asking.</p>

<p>The readiness of a campaign is therefore not the average of its items. It is set by the worst item, and "worst" does not mean the most important in the abstract: it means the one that needs more time than is left. For every open item a single difference matters, the margin: the days remaining until the item is needed, minus the days needed to close it. If the margin is positive, the item is an activity to follow up. If it is negative, it is a decision to be taken now.</p>

<p>A percentage contains neither number.</p>

<h2>A worked example</h2>

<p>The figures below are illustrative – built to show the mechanism, not taken from real projects – but the structure recurs.</p>

<p>A geophysical campaign with 20 days of acquisition, in an area a few hours from port. The readiness review is held five days before sailing, by custom. The status presented is this:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Area</th><th class="num">Items</th><th class="num">Closed</th><th class="num">Open</th></tr>
</thead>
<tbody>
<tr><td>People</td><td class="num">10</td><td class="num">9</td><td class="num">1</td></tr>
<tr><td>Vessel</td><td class="num">8</td><td class="num">8</td><td class="num">0</td></tr>
<tr><td>Documents and procedures</td><td class="num">12</td><td class="num">11</td><td class="num">1</td></tr>
<tr><td>Permits</td><td class="num">6</td><td class="num">6</td><td class="num">0</td></tr>
<tr><td>Interfaces</td><td class="num">7</td><td class="num">6</td><td class="num">1</td></tr>
<tr><td>Contingencies</td><td class="num">5</td><td class="num">5</td><td class="num">0</td></tr>
<tr><td><strong>Total</strong></td><td class="num"><strong>48</strong></td><td class="num"><strong>45</strong></td><td class="num"><strong>3</strong></td></tr>
</tbody>
</table>
</div>

<p>The three open items, with the time needed to close them and the margin against sailing:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Open item</th><th class="num">Days to close</th><th class="num">Margin</th></tr>
</thead>
<tbody>
<tr><td>Basic offshore safety training certificate (BOSIET) for one technician, expiring mid-campaign: FOET refresher to be booked and attended</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td>Recovery procedure for the towed instrument, awaiting client approval</td><td class="num">3</td><td class="num">+2</td></tr>
<tr><td>Bridging document between the client's and the contractor's HSE management systems, to be signed</td><td class="num">2</td><td class="num">+3</td></tr>
</tbody>
</table>
</div>

<p>All margins are positive, and the decision to sail is consistent with the figures presented.</p>

<p>The problem lies among the closed items. The item "work area permit" is ticked: the permit exists, is valid, is on file. It was issued, however, on the polygon of revision B of the line plan. Seven days before the review – twelve before sailing – revision D was issued, adding six lines along a cable route variation. Four of them run partly outside the permitted polygon.</p>

<p>Nobody hid anything: the item had been closed before the line plan changed, and no rule reopened it. In this example, amending the permit takes fifteen days.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Open item</th><th class="num">Days to close</th><th class="num">Margin</th></tr>
</thead>
<tbody>
<tr><td>Basic offshore safety training</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td>Recovery procedure</td><td class="num">3</td><td class="num">+2</td></tr>
<tr><td>Bridging document</td><td class="num">2</td><td class="num">+3</td></tr>
<tr><td><strong>Work area permit, reopened</strong></td><td class="num"><strong>15</strong></td><td class="num"><strong>−10</strong></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>−10</strong><span>days of margin, inside a checklist at 94%</span></div>

<p>With the item reopened, closed items go from 45 out of 48 to 44: from 94% to 92%. Two percentage points, which nobody would notice in a presentation. The margin of the worst item, on the other hand, goes from +2 to −10 days, and that is the number that changes the decision.</p>

<h2>What a negative margin decides</h2>

<p>A negative margin does not automatically mean the vessel stays in port. It means the sailing decision has to state what happens to the lines that cannot yet be acquired.</p>

<p>In the example the four lines outside the polygon need two days of acquisition in total. If the vessel sails on the planned date, the permit amendment arrives ten days after sailing: fifteen days to obtain it, minus the five that were left before sailing. With 20 days of acquisition and two to be reserved for the four lines, these must start within 18 days of sailing so as not to lengthen the campaign. Between the expected arrival of the permit and the last useful day there are eight days.</p>

<p>The correct decision is therefore: sail, with a written condition. The four lines go to the end of the programme; the permit amendment has an owner and an expected date; if it has not arrived 18 days after sailing, the choice is between extending the charter and giving up the lines – and that choice is set today by whoever has the authority, not improvised on the day by whoever is on board.</p>

<p>It is a different decision from "sail", and nobody takes it if the table says 94%.</p>

<h2>The fault was not in the item, but in how it was closed</h2>

<p>The permit item had not been closed badly. It had been closed against a document that later changed, and a checklist that records only the status – open or closed – has no way of noticing.</p>

<p>The remedy is to record, for every closed item, against which revision of which document it was verified: "permit verified against line plan rev. B", not "permit in place". When rev. D is issued, every item that depends on the line plan reopens. In the example the item would have reopened twelve days before sailing, with a margin of −3 days instead of −10: still negative, but found seven days earlier, when there was time to chase the authority or reorder the programme on shore rather than at sea.</p>

<h2>The objection that will come</h2>

<p>Whoever organises the campaign will reply that bringing the review forward does not solve the problem: fifteen days before sailing, half the items cannot be closed. The crew is not yet assigned, the vessel is finishing another job, the procedures are waiting for the final version of the line plan. An early review would produce nothing but a long list of open items.</p>

<p>The objection is right on the facts, and it shows how the review should be run, not that it should be postponed. Fifteen days before sailing, the check is not that items are closed: it is that each one has an owner, an estimated closure time and a positive margin. An open item with ten days of margin is in order. An open item for which nobody can say how long it will take is the most useful finding a review can produce.</p>

<p>There are therefore two passes, with different purposes. The first, held before the remaining time drops below the longest closure time on the list, checks margins. The second, close to sailing, checks closures. Holding only one, five days before by custom, means running the second while believing the first has been run too.</p>

<h2>What to require in the specification</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>The closure time next to every item.</strong><span class="t"> Not just open or closed: how many days it takes to close and who closes it. Without that number the margin cannot be computed, and without the margin the review is counting boxes.</span></span></li>
  <li><span class="k">02</span><span><strong>The margin of the worst item at the top of the report.</strong><span class="t"> Before the percentage, or instead of it. It is the number the sailing decision rests on, and it must be the first one read by whoever was not at the meeting.</span></span></li>
  <li><span class="k">03</span><span><strong>Every closure tied to the revision of the document checked.</strong><span class="t"> A new revision of a document reopens every item that depends on it. The line plan, the programme and the personnel list are the documents that change most often in the final weeks.</span></span></li>
  <li><span class="k">04</span><span><strong>Two passes, with dates set by the longest closure time.</strong><span class="t"> The first on margins, the second on closures. Not a single meeting on a date chosen by custom.</span></span></li>
  <li><span class="k">05</span><span><strong>Conditional sailings written down as such.</strong><span class="t"> If the vessel sails with an item at negative margin, the decision states what is excluded, who closes the item, by when, and what happens if it is not closed. A condition that lives only in the meeting minutes does not reach the vessel.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>A readiness review is not there to prove that everyone is ready. It is there to find, while there is still time to act, the item that will not close in time. A checklist at 94% says the work is almost done; it does not say whether what is missing can be finished before sailing.</p>

<p>Between the two there is one number per item, the margin, which almost no checklist reports and which costs very little to add. It has to be specified in advance: by the day of the review, the shape of the table has already been decided.</p>

<h3>References</h3>

<ul>
  <li>IOGP Report 423, <em>HSE management – guidelines for working together in a contract environment</em>, and supplement 423-02, <em>Guide to preparing HSE plans and Bridging documents</em>: a bridging document is needed when all or part of the scope of work is carried out under the contractor's management system, on the basis that it meets the requirements of the client's.</li>
  <li>OPITO, BOSIET and FOET standards: the BOSIET certificate is valid for four years; the refresher is the one-day FOET course, to be attended while the certificate is still in date.</li>
</ul>

<div class="callout">
  <p>CLEGAR provides project management and technical assurance for offshore campaigns, readiness reviews included. If you are preparing a campaign, or want an independent check of readiness before sailing, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
    {
        'id': 'tempo-nave',
        'topic': 'excellence',
        'date': '2026-10-05',
        'slug': {'it': 'la-classificazione-del-tempo-nave',
                 'en': 'classifying-vessel-time'},
        'title': {
            'it': 'La classificazione del tempo nave: chi paga la giornata in cui non si è lavorato',
            'en': 'Classifying vessel time: who pays for the day nothing was done',
        },
        'meta_title': {
            'it': 'La classificazione del tempo nave | Insights',
            'en': 'Classifying vessel time | Insights',
        },
        'desc': {
            'it': ('Perché l’etichetta scritta nel rapporto giornaliero decide chi paga una '
                   'giornata di fermo, e come si verifica incrociando ogni voce di standby con '
                   'lo stato del mare registrato.'),
            'en': ('Why the label written in the daily report decides who pays for an idle day, '
                   'and how to check it by cross-referencing every standby entry against the '
                   'recorded sea state.'),
        },
        'abstract': {
            'it': ('Weather standby o guasto: la stessa giornata di fermo cade sul committente o '
                   'sul contractor secondo una parola scritta a bordo da chi ha interesse a '
                   'scriverne una piuttosto che un’altra. Su una campagna di 28 giorni sono due '
                   'giornate, cioè l’8% del tempo nave fatturato.'),
            'en': ('Weather standby or breakdown: the same idle day falls on the client or on the '
                   'contractor according to a word written on board by the party with an interest '
                   'in writing one rather than another. On a 28-day campaign that is two days, or '
                   '8% of invoiced vessel time.'),
        },
        'body': {
            'it': """
<p class="lede">Una campagna offshore si fattura a giornate, e ogni giornata porta un'etichetta: acquisizione, transito, weather standby, guasto. L'etichetta non descrive soltanto che cosa è successo. Decide chi paga.</p>

<p>Viene assegnata a bordo, di solito la sera, da chi compila il rapporto giornaliero (il daily progress report): spesso alla fine di un turno, quasi sempre dal contractor. È una delle poche decisioni di una campagna che valgono decine di migliaia di euro e che nessuno tratta come una decisione.</p>

<h2>Perché la parola conta più del fatto</h2>

<p>Nei contratti di noleggio offshore della famiglia SUPPLYTIME, la clausola di <em>off-hire</em> elenca le cause che sospendono il nolo: carenza di equipaggio, sciopero, guasto di macchinari o strumentazione, danni allo scafo o altri incidenti alla nave. Per il tempo perso il nolo non è dovuto, e il costo resta al contractor.</p>

<p>Il meteo non è in quell'elenco. Una nave ferma perché il mare supera i limiti operativi resta <em>on hire</em>: il committente paga la giornata per intero.</p>

<p>L'elenco ha però un confine che conta: la stessa clausola esclude dal caso del guasto la strumentazione installata a bordo dal noleggiatore. Se lo strumento che si ferma è stato portato dal committente, il suo guasto non sospende il nolo. Chi fornisce lo spread decide quindi anche chi paga quando lo spread non funziona, e questa è una verifica da fare sul contratto prima che sul rapporto giornaliero.</p>

<p>Da qui l'asimmetria che governa tutto il resto. La stessa nave, lo stesso mare, le stesse ventiquattro ore in cui non si è acquisito un metro di dato: costano al contractor se la causa è un guasto, al committente se la causa è il meteo. Fra le due possibilità non c'è una misura. C'è una parola scritta in un rapporto.</p>

<h2>Un esempio pratico</h2>

<p>I valori che seguono sono sintetici – costruiti per illustrare il meccanismo, non tratti da progetti reali – ma la struttura è ricorrente.</p>

<p>Una campagna geofisica di 28 giorni. A fine lavori il riepilogo dei rapporti giornalieri si presenta così:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Categoria di tempo</th><th class="num">Giorni</th><th>A carico di</th></tr>
</thead>
<tbody>
<tr><td>Acquisizione</td><td class="num">16</td><td>committente</td></tr>
<tr><td>Transito</td><td class="num">2</td><td>committente</td></tr>
<tr><td>Weather standby</td><td class="num">7</td><td>committente</td></tr>
<tr><td>Off-hire per guasto</td><td class="num">3</td><td>contractor</td></tr>
<tr><td><strong>Totale</strong></td><td class="num"><strong>28</strong></td><td><strong>25 al committente</strong></td></tr>
</tbody>
</table>
</div>

<p>Venticinque giornate fatturabili su ventotto. Il totale torna, e nessuno contesta i tre giorni di guasto: li ha dichiarati il contractor stesso.</p>

<p>Chi rivede i rapporti giornalieri, però, incrocia ogni voce di weather standby con lo stato del mare registrato. Due delle sette giornate riportano altezze d'onda significative di 1,4 m e 1,6 m, contro un limite operativo contrattuale di Hs ≤ 2,5 m per l'acquisizione. In quelle due giornate la nave non ha lavorato perché il sensore di moto (MRU), parte dello spread fornito dal contractor, dava un'uscita degradata: con quel mare – dentro i limiti, ma non calmo – il dato risultava fuori specifica.</p>

<p>Non è weather standby. È strumentazione che non funziona, e un mare che si limita a mettere in luce il difetto.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Categoria di tempo</th><th class="num">Come riportato</th><th class="num">Dopo la revisione</th></tr>
</thead>
<tbody>
<tr><td>Weather standby</td><td class="num">7</td><td class="num">5</td></tr>
<tr><td>Off-hire per guasto</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td><strong>Giornate a carico del committente</strong></td><td class="num"><strong>25</strong></td><td class="num"><strong>23</strong></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>8%</strong><span>del tempo nave fatturato</span></div>

<p>Due giornate: l'8% delle venticinque che erano state fatturate al committente. La durata della campagna non cambia di un'ora: cambia da quale parte del contratto cade.</p>

<h2>La verifica che lo rileva</h2>

<p>È un controllo che si fa con un confronto, a condizione che qualcuno lo faccia: si prende ogni voce di weather standby e si confronta lo stato del mare registrato in quell'intervallo con il limite operativo scritto nel contratto.</p>

<p>Una giornata di standby dichiarata con il mare ben dentro i limiti operativi non dimostra nulla da sola, ma è una domanda che merita una risposta scritta. Se le risposte non arrivano, o arrivano identiche per giornate diverse, la classificazione non regge.</p>

<p>Il controllo funziona solo se lo stato del mare è registrato accanto alla voce di standby, dalla fonte che il contratto ha nominato. Se il dato meteo e il rapporto giornaliero vivono in due documenti che nessuno incrocia, la verifica è impossibile – ed è esattamente così che quasi tutte le campagne sono organizzate.</p>

<h2>L'obiezione che arriverà</h2>

<p>Un contractor risponderà, correttamente, che l'altezza d'onda significativa da sola non definisce l'operabilità. Un mare di 1,4 m al traverso con periodo corto può essere peggiore, per un trasduttore multibeam montato sullo scafo, di 2,2 m con mare di prua. Direzione relativa e periodo contano quanto l'altezza, e un limite scritto come numero singolo non li contiene.</p>

<p>L'obiezione è fondata, e non smonta la verifica: la sposta. Il criterio non è «Hs sotto il limite, quindi la classificazione è sbagliata». Il criterio è che il limite operativo vada scritto come inviluppo – altezza, periodo, direzione relativa – e che ogni voce di standby dichiari <em>quale</em> condizione sia stata superata.</p>

<p>Un limite espresso con un numero solo non previene la controversia: la prepara, perché lascia a ciascuna parte la possibilità di avere ragione.</p>

<h2>Cosa richiedere nella specifica</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Categorie di tempo esaustive, senza voce residua.</strong><span class="t"> Ogni ora della campagna deve ricadere in una categoria definita nel contratto. Una voce «altro» è il posto dove finiscono le giornate che nessuno vuole discutere.</span></span></li>
  <li><span class="k">02</span><span><strong>Lo stato del mare accanto a ogni voce di standby.</strong><span class="t"> Altezza d'onda significativa, periodo e direzione relativa, dalla fonte nominata nel contratto – sensore di bordo o hindcast – e non da due documenti diversi a seconda di chi scrive.</span></span></li>
  <li><span class="k">03</span><span><strong>Il limite operativo come inviluppo, non come numero.</strong><span class="t"> Con l'indicazione dell'attività a cui si applica: acquisizione, messa a mare, recupero e transito non si fermano allo stesso mare.</span></span></li>
  <li><span class="k">04</span><span><strong>La zona grigia definita in anticipo.</strong><span class="t"> Strumentazione degradata ma non guasta: è off-hire, è standby, o è lavoro pagato a tariffa ridotta? È lì che finisce la maggior parte delle controversie, ed è il punto che quasi nessun contratto affronta.</span></span></li>
  <li><span class="k">05</span><span><strong>Il rapporto giornaliero controfirmato ogni giorno.</strong><span class="t"> Dal rappresentante del committente a bordo, entro ventiquattro ore. Un rapporto approvato a fine campagna non è una verifica: è una ricostruzione fatta quando nessuno ricorda più il mare di quel martedì.</span></span></li>
  <li><span class="k">06</span><span><strong>Le categorie del rapporto riconciliate con quelle della fattura.</strong><span class="t"> Sono quasi sempre due tassonomie diverse, compilate da uffici diversi. Finché nessuno le mette in colonna, la classificazione può cambiare fra il mare e l'amministrazione senza che si veda.</span></span></li>
</ul>

<h2>Il punto di fondo</h2>

<p>Il tempo nave è la voce di costo più grande di una campagna offshore, e si assegna con una parola scritta a bordo da chi ha interesse a scriverne una piuttosto che un'altra. Non è malafede: è un conflitto di interessi strutturale, lasciato senza un controllo.</p>

<p>Il controllo costa poco – incrociare due colonne che il contratto può obbligare a esistere – e va previsto prima che la nave parta. Dopo la consegna si può ancora fare, ma a quel punto non è più una verifica: è una contestazione, e si discute con chi ha già emesso la fattura.</p>

<h3>Riferimenti</h3>

<ul>
  <li>BIMCO SUPPLYTIME 2017, clausola 13(a) – off-hire: carenza di equipaggio o di dotazioni dell'armatore, sciopero dell'equipaggio, guasto di macchinari e/o strumentazione, danni allo scafo o altri incidenti alla nave. La stessa clausola esclude la strumentazione installata a bordo dal noleggiatore ai sensi della clausola 4.</li>
  <li>The Shipowners' Club, confronto fra WINDTIME e SUPPLYTIME – nei noleggi per l'eolico offshore il rischio meteo è spesso diviso rispetto alla capacità garantita della nave: un'allocazione diversa, utile come termine di paragone.</li>
</ul>

<div class="callout">
  <p>CLEGAR fornisce project management e technical assurance per campagne offshore. Se state impostando la specifica di una campagna, o state rivedendo un consuntivo di tempo nave che vi è stato consegnato, ne parliamo volentieri.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
            'en': """
<p class="lede">An offshore campaign is invoiced by the day, and every day carries a label: acquisition, transit, weather standby, breakdown. The label does not merely describe what happened. It decides who pays.</p>

<p>It is assigned on board, usually in the evening, by whoever fills in the daily progress report – often at the end of a shift, and almost always by the contractor. It is one of the few decisions on a campaign that are worth tens of thousands of euros and that nobody treats as a decision.</p>

<h2>Why the word matters more than the fact</h2>

<p>In offshore charters of the SUPPLYTIME family, the <em>off-hire</em> clause lists the causes that suspend hire: deficiency of crew, strike, breakdown of machinery or equipment, damage to the hull or other accidents to the vessel. No hire is payable for the time lost, and the cost stays with the contractor.</p>

<p>Weather is not on that list. A vessel on standby because the sea exceeds its operating limits remains <em>on hire</em>: the client pays the day in full.</p>

<p>The list has a boundary that matters, though: the same clause excludes from breakdown any equipment installed on board by the charterers. If the instrument that stops was brought by the client, its failure does not suspend hire. Who supplies the spread therefore also decides who pays when the spread does not work, and that is a check to run against the contract before running it against the daily report.</p>

<p>Hence the asymmetry that governs everything else. The same vessel, the same sea, the same twenty-four hours in which not a metre of data was acquired: they cost the contractor if the cause was a breakdown, and the client if the cause was weather. Between those two outcomes there is no measurement. There is a word written in a report.</p>

<h2>A worked example</h2>

<p>The figures below are illustrative – built to show the mechanism, not taken from real projects – but the structure recurs.</p>

<p>A 28-day geophysical campaign. At the end of the works, the summary of the daily progress reports looks like this:</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Time category</th><th class="num">Days</th><th>Borne by</th></tr>
</thead>
<tbody>
<tr><td>Acquisition</td><td class="num">16</td><td>client</td></tr>
<tr><td>Transit</td><td class="num">2</td><td>client</td></tr>
<tr><td>Weather standby</td><td class="num">7</td><td>client</td></tr>
<tr><td>Off-hire for breakdown</td><td class="num">3</td><td>contractor</td></tr>
<tr><td><strong>Total</strong></td><td class="num"><strong>28</strong></td><td><strong>25 to the client</strong></td></tr>
</tbody>
</table>
</div>

<p>Twenty-five billable days out of twenty-eight. The total adds up, and nobody disputes the three days of breakdown: the contractor declared them itself.</p>

<p>Reviewing the daily reports, however, means cross-checking every weather standby entry against the recorded sea state. Two of the seven days report significant wave heights of 1.4 m and 1.6 m, against a contractual operating limit of Hs ≤ 2.5 m for acquisition. On those two days the vessel did not work because the motion reference unit (MRU), part of the contractor-supplied spread, was producing a degraded output: in that sea – inside the limit, but not calm – the data fell out of specification.</p>

<p>That is not weather standby. It is equipment that does not work, and a sea that merely exposes the fault.</p>

<div class="tablewrap">
<table>
<thead>
<tr><th>Time category</th><th class="num">As reported</th><th class="num">After review</th></tr>
</thead>
<tbody>
<tr><td>Weather standby</td><td class="num">7</td><td class="num">5</td></tr>
<tr><td>Off-hire for breakdown</td><td class="num">3</td><td class="num">5</td></tr>
<tr><td><strong>Days borne by the client</strong></td><td class="num"><strong>25</strong></td><td class="num"><strong>23</strong></td></tr>
</tbody>
</table>
</div>

<div class="pull"><strong>8%</strong><span>of invoiced vessel time</span></div>

<p>Two days: 8% of the twenty-five that had been invoiced to the client. The duration of the campaign does not change by an hour: what changes is which side of the contract it falls on.</p>

<h2>The check that finds it</h2>

<p>The check itself is one comparison, provided somebody makes it: take every weather standby entry and compare the sea state recorded over that interval with the operating limit written into the contract.</p>

<p>A standby day declared with the sea well inside the operating limits proves nothing on its own, but it is a question that deserves an answer in writing. If the answers do not come, or come back identical for different days, the classification does not hold.</p>

<p>The check only works if the sea state is recorded alongside the standby entry, from the source the contract named. If the weather data and the daily report live in two documents that nobody cross-checks, the verification is impossible – and that is exactly how almost every campaign is organised.</p>

<h2>The objection that will come</h2>

<p>A contractor will reply, correctly, that significant wave height alone does not define workability. A 1.4 m sea on the beam with a short period can be worse, for a hull-mounted multibeam transducer, than 2.2 m in a head sea. Relative heading and period matter as much as height, and a limit written as a single number contains neither.</p>

<p>The objection is sound, and it does not dismantle the check: it relocates it. The criterion is not "Hs below the limit, therefore the classification is wrong". The criterion is that the operating limit should be written as an envelope – height, period, relative heading – and that every standby entry should state <em>which</em> condition was exceeded.</p>

<p>A limit expressed as one number does not prevent the dispute: it prepares it, because it leaves each party room to be right.</p>

<h2>What to require in the specification</h2>

<ul class="flist">
  <li><span class="k">01</span><span><strong>Exhaustive time categories, with no residual entry.</strong><span class="t"> Every hour of the campaign must fall into a category defined in the contract. An "other" line is where the days nobody wants to discuss end up.</span></span></li>
  <li><span class="k">02</span><span><strong>The sea state alongside every standby entry.</strong><span class="t"> Significant wave height, period and relative heading, from the source named in the contract – onboard sensor or hindcast – and not from two different documents depending on who is writing.</span></span></li>
  <li><span class="k">03</span><span><strong>The operating limit as an envelope, not as a number.</strong><span class="t"> Stating which activity it applies to: acquisition, deployment, recovery and transit do not stop in the same sea.</span></span></li>
  <li><span class="k">04</span><span><strong>The grey area defined in advance.</strong><span class="t"> Equipment degraded but not broken: is that off-hire, standby, or work paid at a reduced rate? That is where most disputes end up, and it is the point almost no contract addresses.</span></span></li>
  <li><span class="k">05</span><span><strong>The daily report countersigned every day.</strong><span class="t"> By the client representative on board, within twenty-four hours. A report approved at the end of the campaign is not a verification: it is a reconstruction made when nobody remembers the sea on that particular Tuesday.</span></span></li>
  <li><span class="k">06</span><span><strong>The report categories reconciled with the invoice categories.</strong><span class="t"> They are almost always two different taxonomies, filled in by different offices. Until somebody lines them up, the classification can change between the sea and the accounts department without anyone seeing it.</span></span></li>
</ul>

<h2>The underlying point</h2>

<p>Vessel time is the largest single cost item on an offshore campaign, and it is assigned by a word written on board by the party with an interest in writing one rather than another. This is not bad faith: it is a structural conflict of interest, left without a check.</p>

<p>The check costs little – cross-referencing two columns the contract can oblige to exist – and it has to be specified before the vessel sails. After delivery it can still be done, but by then it is no longer a verification: it is a claim, argued with a party that has already issued the invoice.</p>

<h3>References</h3>

<ul>
  <li>BIMCO SUPPLYTIME 2017, clause 13(a) – off-hire: deficiency of crew or of the owners' stores, strike of crew, breakdown of machinery and/or equipment, damage to hull or other accidents to the vessel. The same clause excludes equipment installed on board by the charterers under clause 4.</li>
  <li>The Shipowners' Club, comparative review of WINDTIME and SUPPLYTIME – in offshore wind charters the weather risk is often split against the vessel's warranted capability: a different allocation, useful as a point of comparison.</li>
</ul>

<div class="callout">
  <p>CLEGAR provides project management and technical assurance for offshore campaigns. If you are setting up a campaign specification, or reviewing a vessel-time account that has been handed to you, we are glad to talk it through.</p>
</div>

<p><a href="mailto:info@clegar.it">info@clegar.it</a></p>
""",
        },
    },
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
