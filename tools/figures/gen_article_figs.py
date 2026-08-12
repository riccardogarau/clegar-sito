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
    ('Requisiti',      'Requirements'),
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


# ═══════════════════════════════════ FIG C — inviluppo di tolleranza IHO S-44
# Le curve non sono sintetiche: escono dalla formula dello standard per
# l'Order 1a. Sintetici sono solo i 45 scarti, che l'articolo dichiara tali.
# La figura mostra cio' che la tabella non puo' mostrare: quanto la scelta
# della soglia sposti l'esito, e che gli scarti si addensano a una profondita'
# precisa invece di distribuirsi.
import math, random

W, H = 1300, 560
# PX1 sta 30 px dentro il bordo: l'ultima etichetta dell'asse e' centrata sul
# suo punto, e con il disegno fino a 1290 sarebbe uscita dalla tela per meta'
PX0, PX1 = 170, 1260              # area di disegno
PY0, PY1 = 470, 130               # y di 0 m e di 1,6 m
D0, D1 = 20, 60                   # profondita' rappresentate
VMAX = 1.6
A_CONST, B_CONST = 0.50, 0.013    # Order 1a

tvu = lambda d: math.sqrt(A_CONST ** 2 + (B_CONST * d) ** 2)
sx = lambda d: PX0 + (d - D0) / (D1 - D0) * (PX1 - PX0)
sy = lambda v: PY0 - v / VMAX * (PY0 - PY1)

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Crossing differences plotted against the IHO S-44 Order 1a tolerance '
     'envelope, showing the failures clustered at one depth range">' % (W, H)]

o += bil(0, 52, 18, NAVY,
         'L’inviluppo di tolleranza, e dove gli scarti si addensano',
         'The tolerance envelope, and where the failures cluster', font=DISP)
o += bil(0, 76, 14, STEEL,
         'CURVE CALCOLATE DALLO STANDARD – I 45 SCARTI SONO DELL’ESEMPIO SINTETICO',
         'CURVES COMPUTED FROM THE STANDARD – THE 45 FAILURES ARE FROM THE SYNTHETIC EXAMPLE')

# legenda dei tre gruppi
for x, col, it, en in ((0, STEEL, 'A – RUMORE', 'A – NOISE'),
                       (300, BLUE, 'B – SISTEMATICO', 'B – SYSTEMATIC'),
                       (600, AMBER, 'C – VARIAZIONE REALE', 'C – REAL CHANGE')):
    o.append('<circle cx="%d" cy="100" r="5" fill="%s"/>' % (x + 6, col))
    o += bil(x + 20, 105, 14, NAVY, it, en, extra=' fill-opacity=".8"')

# griglia e assi
for v in (0.4, 0.8, 1.2, 1.6):
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".09"/>'
             % (PX0, sy(v), PX1, sy(v), NAVY))
    o += bil(PX0 - 16, sy(v) + 5, 14, STEEL, ('%.1f' % v).replace('.', ','), '%.1f' % v,
             anchor='end')
o += bil(PX0 - 16, PY0 + 5, 14, STEEL, '0', '0', anchor='end')
o += bil(0, PY1 - 14, 14, STEEL, 'DIFFERENZA ALL’INCROCIO (m)', 'CROSSING DIFFERENCE (m)')
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".28"/>'
         % (PX0, PY0, PX1, PY0, NAVY))
for d in range(D0, D1 + 1, 10):
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".28"/>'
             % (sx(d), PY0, sx(d), PY0 + 7, NAVY))
    o += bil(sx(d), PY0 + 28, 14, NAVY, '%d m' % d, '%d m' % d, anchor='middle',
             extra=' fill-opacity=".72"')
o += bil(PX1, PY0 + 56, 14, STEEL, 'PROFONDITÀ', 'WATER DEPTH', anchor='end')

# la fascia fra le due soglie: e' la differenza fra il test giusto e quello sbagliato
step = [D0 + i for i in range(D1 - D0 + 1)]
up = ' '.join('%.1f,%.1f' % (sx(d), sy(math.sqrt(2) * tvu(d))) for d in step)
dn = ' '.join('%.1f,%.1f' % (sx(d), sy(tvu(d))) for d in reversed(step))
o.append('<polygon points="%s %s" fill="%s" fill-opacity=".07"/>' % (up, dn, NAVY))
for f, dash in ((lambda d: math.sqrt(2) * tvu(d), ''), (tvu, ' stroke-dasharray="6 5"')):
    pts = ' '.join('%.1f,%.1f' % (sx(d), sy(f(d))) for d in step)
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2"%s/>' % (pts, NAVY, dash))
o += bil(PX1 - 6, sy(math.sqrt(2) * tvu(58)) - 14, 14, NAVY, '√2 × TVU', '√2 × TVU', anchor='end')
o += bil(PX1 - 6, sy(tvu(58)) + 26, 14, NAVY, 'TVU', 'TVU', anchor='end',
         extra=' fill-opacity=".7"')

# i 45 scarti. Seme fisso: la build deve restare riproducibile.
rnd = random.Random(11)
for lo, hi, n, over, col in ((24, 31, 6, 0.16, STEEL),
                             (44, 58, 8, 0.26, BLUE),
                             (26, 34, 31, 0.46, AMBER)):
    for _ in range(n):
        d = rnd.uniform(lo, hi)
        v = math.sqrt(2) * tvu(d) + rnd.uniform(0.03, over)
        o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" fill-opacity=".85"/>'
                 % (sx(d), sy(min(v, VMAX - 0.02)), col))
o.append('</svg>')
open('fig_art_tvu.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_tvu.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG D — la percentuale contro la mappa
# La tesi dell'articolo in un'immagine: a sinistra la sintesi scalare, a
# destra il fenomeno spaziale che quella sintesi comprime. I 45 scarti sono
# gli stessi nelle due meta'.
W, H = 1300, 560
BX0, BX1, BY0, BY1 = 500, 1290, 150, 470       # il blocco di rilievo
SWX0, SWX1, SWY0, SWY1 = 600, 830, 200, 340    # il campo di sand wave

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="The same crossline result shown as a single pass rate and as a map, '
     'where the failures cluster in a mobile sand wave field">' % (W, H)]

o += bil(0, 52, 18, NAVY,
         'Lo stesso risultato, letto in due modi',
         'The same result, read two ways', font=DISP)
o += bil(0, 76, 14, STEEL,
         'GLI STESSI 45 SCARTI SU 1.240 INCROCI – ESEMPIO SINTETICO',
         'THE SAME 45 FAILURES OUT OF 1,240 CROSSINGS – SYNTHETIC EXAMPLE')

# meta' sinistra: la sintesi
o += bil(0, 246, 14, STEEL, '1.240 INCROCI', '1,240 CROSSINGS')
o += bil(0, 322, 64, NAVY, '96,4%', '96.4%', font=DISP)
o += bil(0, 356, 14, STEEL, 'ENTRO TOLLERANZA', 'WITHIN TOLERANCE')
o += bil(0, 404, 14, STEEL, 'IL RILIEVO PASSA', 'THE SURVEY PASSES')
o.append('<line x1="430" y1="150" x2="430" y2="470" stroke="%s" stroke-opacity=".18"/>' % NAVY)

# meta' destra: il blocco, il campo di sand wave, il tracciato in progetto
o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="none" stroke="%s" stroke-opacity=".3"/>'
         % (BX0, BY0, BX1 - BX0, BY1 - BY0, NAVY))
o.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" fill-opacity=".09"/>'
         % (SWX0, SWY0, SWX1 - SWX0, SWY1 - SWY0, TEAL))
o += bil(SWX0, SWY0 - 10, 14, TEAL, 'CAMPO DI SAND WAVE', 'SAND WAVE FIELD')
o.append('<polyline points="%d,430 700,320 900,282 %d,250" fill="none" stroke="%s" '
         'stroke-width="2" stroke-opacity=".45" stroke-dasharray="8 6"/>' % (BX0, BX1, NAVY))
o += bil(BX1 - 6, 236, 14, NAVY, 'TRACCIATO CAVO IN PROGETTO', 'PROPOSED CABLE ROUTE',
         anchor='end', extra=' fill-opacity=".65"')

# gli scarti. Seme fisso: la build deve restare riproducibile.
rnd = random.Random(23)
for _ in range(31):                                   # gruppo C, dentro le sand wave
    o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" fill-opacity=".9"/>'
             % (rnd.uniform(SWX0 + 12, SWX1 - 12), rnd.uniform(SWY0 + 12, SWY1 - 12), AMBER))
for i in range(8):                                    # gruppo B, tutti sulla stessa linea
    t = i / 7
    o.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s" fill-opacity=".9"/>'
             % (900 + t * 340, 442 - t * 72, BLUE))
for cx, cy in ((548, 214), (566, 402), (992, 186), (1210, 320), (742, 452), (1104, 428)):
    o.append('<circle cx="%d" cy="%d" r="4.5" fill="%s" fill-opacity=".9"/>' % (cx, cy, STEEL))

o.append('<line x1="%d" y1="270" x2="852" y2="270" stroke="%s" stroke-opacity=".5"/>'
         % (SWX1, AMBER))
o += bil(860, 265, 14, AMBER,
         '31 SCARTI – IL FONDALE SI È MOSSO', '31 FAILURES – THE SEABED MOVED')

for x, col, it, en in ((BX0, STEEL, 'A – RUMORE', 'A – NOISE'),
                       (720, BLUE, 'B – SISTEMATICO', 'B – SYSTEMATIC'),
                       (960, AMBER, 'C – VARIAZIONE REALE', 'C – REAL CHANGE')):
    o.append('<circle cx="%d" cy="516" r="5" fill="%s"/>' % (x + 6, col))
    o += bil(x + 20, 521, 14, NAVY, it, en, extra=' fill-opacity=".8"')
o.append('</svg>')
open('fig_art_map.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_map.svg', len('\n'.join(o)), 'chars')
