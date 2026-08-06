NAVY, BLUE, TEAL, AMBER, STEEL = '#0B2545', '#3B87BE', '#009AA6', '#C9821E', '#8B9598'
MONO = 'font-family="IBM Plex Mono, monospace" letter-spacing="1.1"'
DISP = 'font-family="Archivo, sans-serif"'


def esc(t):
    return str(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def bil(x, y, size, fill, it, en, anchor='start', font=MONO, extra=''):
    return ['<text class="it" %s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (font, x, y, size, fill, anchor, extra, esc(it)),
            '<text class="en" %s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (font, x, y, size, fill, anchor, extra, esc(en))]


# ═══════════════════════════════════ FIG A — origin vs surfacing of problems
W, H = 1300, 540
PHASES = [
    ('Specifica',      'Specification'),
    ('Gara',           'Tender'),
    ('Mobilitazione',  'Mobilisation'),
    ('Acquisizione',   'Acquisition'),
    ('Processing',     'Processing'),
    ('Accettazione',   'Acceptance'),
]
# Non una distribuzione: casi nominati. Due istogrammi di numeri inventati
# dicono soltanto "questa serie pende a sinistra, quest'altra a destra", e
# non mostrano ne' il legame fra un problema e la sua scoperta, ne' il
# ritardo che li separa - che e' il punto dell'articolo. Qui ogni riga e' un
# problema solo: parte da dove nasce e finisce dove si scopre, e la
# lunghezza della freccia E' il ritardo.
LX = 270                         # le etichette finiscono qui
GX0, GX1 = 310, 1280             # la linea temporale occupa il resto
BW = (GX1 - GX0) / len(PHASES)
TOP, RH = 208, 62                # prima riga e passo verticale
BAND_TOP, BAND_BOT = 122, 474
OPEN_PHASES = 2                  # specifica e gara: qui i criteri sono ancora modificabili

# Costo della correzione per fase in cui il problema emerge, in pixel di
# spessore del cuneo. Non sono euro e non fingono di esserlo: e' una scala
# qualitativa, dichiarata nel sottotitolo. Serve perche' la didascalia
# affermava che il costo cresce mentre il disegno mostrava solo il ritardo -
# un'affermazione che il lettore non poteva verificare guardando la figura.
COST = [2, 5, 9, 14, 20, 27]

# origine e scoperta di ciascun caso, come indici di PHASES.
# Sono esempi tratti dal testo dell'articolo, non una casistica misurata:
# per questo la didascalia lo dichiara.
CASES = [
    ('Tolleranza non definita',          'Undefined tolerance',            0, 5),
    ('Criterio di accettazione ambiguo', 'Ambiguous acceptance criterion', 0, 4),
    ('Downtime meteo fuori programma',   'Weather downtime off schedule',  1, 3),
    ('Calibrazione non testimoniata',    'Calibration not witnessed',      2, 4),
    ('Posizionamento non pattuito',      'Positioning not agreed',         1, 2),
]

centre = lambda i: GX0 + i * BW + BW / 2

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Examples of offshore project problems, each shown from the phase where it '
     'originates to the phase where it is found">' % (W, H)]
o += bil(0, 52, 18, NAVY,
         'Quanto tardi si scopre, quanto costa rimediare',
         'How late it is found, how much it costs to put right', font=DISP)
# le due righe di sottotitolo spiegano le due dimensioni del disegno e
# dichiarano che sono esempi: viaggiano con l'immagine anche quando si apre
# a schermo intero, dove la didascalia non la segue
o += bil(0, 76, 14, STEEL,
         'OGNI CUNEO VA DA DOVE IL PROBLEMA NASCE A DOVE SI SCOPRE',
         'EACH WEDGE RUNS FROM WHERE A PROBLEM STARTS TO WHERE IT IS FOUND')
o += bil(0, 98, 14, STEEL,
         'LO SPESSORE CRESCE CON IL COSTO DI RIMEDIARE – SCALA QUALITATIVA, ESEMPI NON MISURATI',
         'THE WEDGE THICKENS WITH THE COST OF PUTTING IT RIGHT – QUALITATIVE SCALE, NOT MEASURED')

# La fascia sulle prime due fasi e' l'unica area colorata della figura: le
# strisce alternate di prima le farebbero concorrenza con un secondo grigio
# che non significa niente. Al loro posto, linee sottili ai bordi di colonna,
# che servono a mappare la punta della freccia sulla sua fase.
o.append('<rect x="%.1f" y="%d" width="%.1f" height="%d" fill="%s" fill-opacity=".055"/>'
         % (GX0, BAND_TOP, OPEN_PHASES * BW, BAND_BOT - BAND_TOP, TEAL))
for i in range(len(PHASES) + 1):
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".09"/>'
             % (GX0 + i * BW, BAND_TOP, GX0 + i * BW, BAND_BOT, NAVY))

for i, (it, en) in enumerate(PHASES):
    o += bil(centre(i), 150, 14, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".72"')

# una riga per caso: pallino dove nasce, cuneo fino a dove si scopre.
# Due dimensioni in un solo segno: la lunghezza e' il ritardo, lo spessore
# finale e' il costo. Due problemi trovati nella stessa fase costano uguale
# anche se sono nati in momenti diversi - ed e' giusto che sia cosi'.
for j, (it, en, a, b) in enumerate(CASES):
    y = TOP + j * RH
    o += bil(LX, y + 5, 15, NAVY, it, en, anchor='end', font=DISP, extra=' fill-opacity=".9"')
    x0, x1 = centre(a), centre(b)
    xs, t = x0 + 11, COST[b]
    o.append('<circle cx="%.1f" cy="%d" r="6.5" fill="%s"/>' % (x0, y, NAVY))
    o.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s" fill-opacity=".78"/>'
             % (xs, y - 1.5, x1, y - t / 2, x1, y + t / 2, xs, y + 1.5, AMBER))

# la parentesi sotto la fascia: dice dove i criteri si possono ancora fissare,
# cioe' dove entra CLEGAR. L'etichetta sta sotto e non dentro, altrimenti la
# versione italiana sarebbe piu' larga della fascia stessa.
o.append('<line x1="%.1f" y1="486" x2="%.1f" y2="486" stroke="%s" stroke-width="2" stroke-opacity=".55"/>'
         % (GX0, GX0 + OPEN_PHASES * BW, TEAL))
o += bil(GX0, 508, 14, TEAL,
         'QUI I CRITERI SI POSSONO ANCORA FISSARE',
         'THE CRITERIA CAN STILL BE SET HERE')
o.append('</svg>')
open('fig_art_origin.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_origin.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG B — service lines across lifecycle
# Stessa griglia della prima figura: nello stesso articolo le sei fasi devono
# cadere negli stessi punti, altrimenti il lettore non riconosce di star
# guardando due volte la stessa linea temporale. Prima erano due griglie
# diverse (LX 330 contro 270, GX0 360 contro 310).
W, H = 1300, 480
LINES = [
    ('Marine Geoscience',            'Marine Geoscience',            0, 6),
    ('Project Management',           'Project Management',           0, 6),
    ('Technical Advisory & Assurance','Technical Advisory & Assurance',0, 6),
    ("Owner's Engineering",          "Owner's Engineering",          2, 5),
    ('Operational Excellence',       'Operational Excellence',       4, 6),
]
TOP, RH = 190, 62
GRID_TOP, GRID_BOT = 104, 456

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Coverage of the five CLEGAR service lines across the project lifecycle">' % (W, H)]
o += bil(0, 52, 18, NAVY,
         'Le cinque linee di servizio lungo il ciclo di progetto',
         'The five service lines across the project lifecycle', font=DISP)
# il sottotitolo dice il raggruppamento. Prima stava in una frase in fondo
# alla figura, che ripeteva a parole quello che le barre gia' mostravano.
o += bil(0, 76, 14, STEEL,
         'TRE LINEE COPRONO L\u2019INTERO CICLO, DUE INTERVENGONO IN FASI PRECISE',
         'THREE LINES SPAN THE WHOLE CYCLE, TWO APPLY AT SPECIFIC STAGES')

for i in range(len(PHASES) + 1):
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".09"/>'
             % (GX0 + i * BW, GRID_TOP, GX0 + i * BW, GRID_BOT, NAVY))
for i, (it, en) in enumerate(PHASES):
    o += bil(centre(i), 132, 14, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".72"')

# Due tinte, non cinque: il colore distingue chi copre l'intero ciclo da chi
# entra in fasi precise. Cinque tinte su cinque righe gia' etichettate erano
# decorazione, e lasciavano credere che il colore significasse qualcosa.
for j, (it, en, a, b) in enumerate(LINES):
    y = TOP + j * RH
    full = (a == 0 and b == len(PHASES))
    o += bil(LX, y + 5, 15, NAVY, it, en, anchor='end', font=DISP, extra=' fill-opacity=".9"')
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" rx="2" fill="%s" fill-opacity=".82"/>'
             % (GX0 + a * BW + 4, y - 8, (b - a) * BW - 8, NAVY if full else TEAL))
o.append('</svg>')
open('fig_art_lines.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_lines.svg', len('\n'.join(o)), 'chars')
