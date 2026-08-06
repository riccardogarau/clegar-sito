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
W, H = 1300, 520
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
TOP, RH = 190, 62                # prima riga e passo verticale
BAND_TOP, BAND_BOT = 104, 456
OPEN_PHASES = 2                  # specifica e gara: qui i criteri sono ancora modificabili

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
o.append('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" '
         'orient="auto"><path d="M0,1 L9,5 L0,9 Z" fill="%s"/></marker></defs>' % AMBER)

o += bil(0, 52, 18, NAVY,
         'Dove nascono i problemi, dove si scoprono',
         'Where problems start, where they are found', font=DISP)
# il sottotitolo spiega come si legge la figura e dichiara che sono esempi:
# viaggia con l'immagine anche quando si apre a schermo intero
o += bil(0, 76, 14, STEEL,
         'OGNI FRECCIA VA DA DOVE IL PROBLEMA NASCE A DOVE SI SCOPRE – ESEMPI, NON CASISTICA MISURATA',
         'EACH ARROW RUNS FROM WHERE A PROBLEM STARTS TO WHERE IT IS FOUND – EXAMPLES, NOT MEASURED CASES')

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
    o += bil(centre(i), 132, 14, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".72"')

# una riga per caso: pallino dove nasce, freccia fino a dove si scopre
for j, (it, en, a, b) in enumerate(CASES):
    y = TOP + j * RH
    o += bil(LX, y + 5, 15, NAVY, it, en, anchor='end', font=DISP, extra=' fill-opacity=".9"')
    x0, x1 = centre(a), centre(b)
    o.append('<circle cx="%.1f" cy="%d" r="6.5" fill="%s"/>' % (x0, y, NAVY))
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-width="2" '
             'stroke-opacity=".55" marker-end="url(#ar)"/>' % (x0 + 11, y, x1 - 6, y, AMBER))

# la parentesi sotto la fascia: dice dove i criteri si possono ancora fissare,
# cioe' dove entra CLEGAR. L'etichetta sta sotto e non dentro, altrimenti la
# versione italiana sarebbe piu' larga della fascia stessa.
o.append('<line x1="%.1f" y1="468" x2="%.1f" y2="468" stroke="%s" stroke-width="2" stroke-opacity=".55"/>'
         % (GX0, GX0 + OPEN_PHASES * BW, TEAL))
o += bil(GX0, 490, 14, TEAL,
         'QUI I CRITERI SI POSSONO ANCORA FISSARE',
         'THE CRITERIA CAN STILL BE SET HERE')
o.append('</svg>')
open('fig_art_origin.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_origin.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG B — service lines across lifecycle
# +2 px oltre l'ultima linea della griglia (GX1=1330): sul bordo esatto
# meta' del tratto cadrebbe fuori dal viewBox e quella linea si vedrebbe
# piu' chiara delle altre
W, H = 1332, 560
LINES = [
    ('Marine Geoscience',            'Marine Geoscience',            0, 6, NAVY),
    ('Project Management',           'Project Management',           0, 6, BLUE),
    ('Technical Advisory & Assurance','Technical Advisory & Assurance',0, 6, TEAL),
    ("Owner's Engineering",          "Owner's Engineering",          2, 5, AMBER),
    ('Operational Excellence',       'Operational Excellence',       4, 6, STEEL),
]
LX = 330
GX0, GX1 = LX + 30, 1330
TOP, RH = 168, 62
BW2 = (GX1 - GX0) / 6

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Coverage of the five CLEGAR service lines across the project lifecycle">' % (W, H)]
o += bil(0, 52, 18, NAVY,
         'Le cinque linee di servizio lungo il ciclo di progetto',
         'The five service lines across the project lifecycle', font=DISP)
o += bil(0, 76, 14, STEEL,
         'DOVE INTERVIENE CIASCUNA LINEA', 'WHERE EACH LINE APPLIES')

for i, (it, en) in enumerate(PHASES):
    x = GX0 + i * BW2
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".1"/>'
             % (x, 120, x, TOP + len(LINES) * RH - 10, NAVY))
    o += bil(x + BW2 / 2, 142, 14, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".7"')
o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".1"/>'
         % (GX1, 120, GX1, TOP + len(LINES) * RH - 10, NAVY))

for j, (it, en, a, b, col) in enumerate(LINES):
    y = TOP + j * RH
    o += bil(LX, y + 5, 15, NAVY, it, en, anchor='end', font=DISP, extra=' fill-opacity=".9"')
    x = GX0 + a * BW2
    w = (b - a) * BW2
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" rx="2" fill="%s" fill-opacity=".82"/>'
             % (x + 4, y - 8, w - 8, col))

o.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".18"/>'
         % (TOP + len(LINES) * RH + 18, GX1, TOP + len(LINES) * RH + 18, NAVY))
o += bil(0, TOP + len(LINES) * RH + 50, 15, NAVY,
         'Le prime tre linee coprono l\u2019intero ciclo: i criteri si definiscono prima, si verificano dopo.',
         'The first three lines span the whole cycle: criteria are set early and verified later.',
         font=DISP, extra=' fill-opacity=".85"')
o.append('</svg>')
open('fig_art_lines.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_lines.svg', len('\n'.join(o)), 'chars')
