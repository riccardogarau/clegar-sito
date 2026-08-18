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
# L'etichetta dice dove cadono, non perche'. Il testo dell'articolo spiega
# che una parte della differenza puo' venire dalla pendenza e non dalla
# mobilita' del fondale: la figura non puo' anticipare una conclusione che
# il testo raggiunge solo dopo aver separato le due componenti.
o += bil(860, 265, 14, AMBER,
         '31 SCARTI, TUTTI QUI', '31 FAILURES, ALL HERE')

for x, col, it, en in ((BX0, STEEL, 'A – RUMORE', 'A – NOISE'),
                       (720, BLUE, 'B – SISTEMATICO', 'B – SYSTEMATIC'),
                       (960, AMBER, 'C – VARIAZIONE REALE', 'C – REAL CHANGE')):
    o.append('<circle cx="%d" cy="516" r="5" fill="%s"/>' % (x + 6, col))
    o += bil(x + 20, 521, 14, NAVY, it, en, extra=' fill-opacity=".8"')
o.append('</svg>')
open('fig_art_map.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_map.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG E — finestra operativa per attivita'
# La curva non e' inventata: e' una Weibull a due parametri, la distribuzione
# standard per l'altezza d'onda significativa, con forma e scala ricavate
# imponendo che passi esattamente per i due punti che l'articolo dichiara
# (62% a 1,5 m e 84% a 2,5 m). Cosi' il disegno non aggiunge assunzioni al
# testo: le mostra soltanto.
W, H = 1300, 520
QX0, QX1, QY0, QY1 = 170, 760, 420, 130
HS_MAX = 4.0
K_W = math.log(math.log(1 - .84) / math.log(1 - .62)) / math.log(2.5 / 1.5)
LAM_W = 1.5 / (-math.log(1 - .62)) ** (1 / K_W)
cdf = lambda x: 1 - math.exp(-(x / LAM_W) ** K_W)
qx = lambda h: QX0 + h / HS_MAX * (QX1 - QX0)
qy = lambda p: QY0 - p * (QY0 - QY1)

BX, DAY = 840, 16                 # pannello destro: 16 px per giorno

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Why the same weather window costs the two activities a different '
     'number of calendar days">' % (W, H)]
o += bil(0, 52, 18, NAVY,
         'La stessa finestra meteo, due costi diversi',
         'The same weather window, two different costs', font=DISP)
o += bil(0, 76, 14, STEEL,
         'CURVA RICAVATA DAI DUE VALORI DICHIARATI NELL’ARTICOLO – ESEMPIO SINTETICO',
         'CURVE DERIVED FROM THE TWO VALUES STATED IN THE ARTICLE – SYNTHETIC EXAMPLE')
o += bil(0, 112, 14, STEEL, 'FINESTRA OPERATIVA', 'WORKABLE SHARE OF WINDOW')

for p in (0, .25, .50, .75, 1.0):
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".09"/>'
             % (QX0, qy(p), QX1, qy(p), NAVY))
    o += bil(QX0 - 16, qy(p) + 5, 14, STEEL, '%d%%' % (p * 100), '%d%%' % (p * 100), anchor='end')
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".28"/>'
         % (QX0, QY0, QX1, QY0, NAVY))
for h in (0, 4):
    o += bil(qx(h), QY0 + 26, 14, STEEL, '%d m' % h, '%d m' % h, anchor='middle')
o += bil((QX0 + QX1) / 2, QY0 + 56, 14, STEEL,
         'ALTEZZA D’ONDA SIGNIFICATIVA', 'SIGNIFICANT WAVE HEIGHT', anchor='middle')

pts = ' '.join('%.1f,%.1f' % (qx(i * HS_MAX / 120), qy(cdf(i * HS_MAX / 120))) for i in range(121))
o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="2.4"/>' % (pts, NAVY))

# i due limiti operativi, ciascuno con il colore della propria attivita'
for lim, col, share in ((2.5, NAVY, .84), (1.5, AMBER, .62)):
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="5 4" stroke-opacity=".75"/>' % (qx(lim), QY0, qx(lim), qy(share), col))
    o.append('<line x1="%d" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.6" '
             'stroke-dasharray="5 4" stroke-opacity=".75"/>' % (QX0, qy(share), qx(lim), qy(share), col))
    o.append('<circle cx="%.1f" cy="%.1f" r="5.5" fill="%s"/>' % (qx(lim), qy(share), col))
    o += bil(qx(lim) - 12, qy(share) - 12, 14, col, '%d%%' % (share * 100), '%d%%' % (share * 100),
             anchor='end')
    t = ('%.1f m' % lim).replace('.', ',')
    o += bil(qx(lim), QY0 + 26, 14, col, 'Hs ≤ ' + t, 'Hs ≤ %.1f m' % lim, anchor='middle')

# pannello destro: quanti giorni di calendario costa ciascuna attivita'
o.append('<line x1="800" y1="130" x2="800" y2="460" stroke="%s" stroke-opacity=".18"/>' % NAVY)
o += bil(BX, 112, 14, STEEL, 'GIORNI NECESSARI', 'CALENDAR DAYS NEEDED')
for y, col, lab_it, lab_en, prod, wait in (
        (190, NAVY,  'GEOFISICO – Hs ≤ 2,5 m',  'GEOPHYSICAL – Hs ≤ 2.5 m',  22, 4),
        (310, AMBER, 'GEOTECNICO – Hs ≤ 1,5 m', 'GEOTECHNICAL – Hs ≤ 1.5 m', 14, 9)):
    o += bil(BX, y, 14, col, lab_it, lab_en)
    o.append('<rect x="%d" y="%d" width="%d" height="30" fill="%s" fill-opacity=".85"/>'
             % (BX, y + 16, prod * DAY, col))
    o.append('<rect x="%d" y="%d" width="%d" height="30" fill="%s" fill-opacity=".22"/>'
             % (BX + prod * DAY, y + 16, wait * DAY, col))
    o += bil(BX, y + 72, 14, STEEL,
             '%d PRODUTTIVI + %d DI ATTESA = %d DI CALENDARIO' % (prod, wait, prod + wait),
             '%d PRODUCTIVE + %d WAITING = %d CALENDAR' % (prod, wait, prod + wait))
o.append('</svg>')
open('fig_art_work.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_work.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG F — lo scambio del percorso critico
# Quattro barre: i due percorsi come pianificati e come ricalcolati. Il colore
# non distingue i percorsi ma l'esposizione al meteo, perche' e' quella la
# variabile dell'articolo: cosi' si vede che il segmento che si gonfia e'
# offshore, e che il blocco piu' lungo del percorso vincolante e' invece a
# terra - cioe' dov'e' la leva di recupero. Le mitigazioni restano alla
# didascalia: in figura sarebbero il quarto messaggio e la sovraccaricherebbero.
W, H = 1300, 540
PX, DAYW = 290, 700 / 48.0        # 48 giorni e' il percorso piu' lungo
LXP = 230

PATHS = {
    'A_plan': [('Mobilitazione','Mobilisation',4,0), ('Calibrazione','Calibration',2,1),
               ('Transito','Transit',1,1), ('Acquisizione','Acquisition',25,1),
               ('Processing','Processing',10,0), ('Interpretazione','Interpretation',3,0)],
    'B_plan': [('Mobilitazione','Mobilisation',5,0), ('Transito','Transit',1,1),
               ('Campionamento','Sampling & CPT',16,1), ('Laboratorio','Laboratory',14,0),
               ('Reporting','Reporting',5,0)],
}
PATHS['A_rec'] = [(a,b,26 if a=='Acquisizione' else c,d) for a,b,c,d in PATHS['A_plan']]
PATHS['B_rec'] = [(a,b,23 if a=='Campionamento' else c,d) for a,b,c,d in PATHS['B_plan']]
tot = lambda k: sum(s[2] for s in PATHS[k])

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="The two paths as planned and recomputed: the critical path swaps from '
     'the geophysical to the geotechnical one">' % (W, H)]
o += bil(0, 52, 18, NAVY,
         'Il percorso critico si scambia', 'The critical path swaps over', font=DISP)
o += bil(0, 76, 14, STEEL,
         'IL COLORE DISTINGUE CIO’ CHE IL METEO PUO’ FERMARE DA CIO’ CHE E’ A TERRA',
         'COLOUR SEPARATES WHAT THE WEATHER CAN STOP FROM WHAT SITS ONSHORE')

for gy, keys, hdr_it, hdr_en in ((150, ('A_plan','B_plan'), 'COME PIANIFICATO, FRANCHIGIA METEO PIATTA DEL 15%',
                                  'AS PLANNED, FLAT 15% WEATHER ALLOWANCE'),
                                 (340, ('A_rec','B_rec'), 'RICALCOLATO SULLA FINESTRA OPERATIVA',
                                  'RECOMPUTED ON WORKABILITY')):
    o += bil(0, gy, 14, NAVY, hdr_it, hdr_en, extra=' fill-opacity=".8"')
    crit = max(tot(k) for k in keys)
    for i, k in enumerate(keys):
        y = gy + 40 + i * 60
        it_lab = 'Path A – Geofisico' if k[0] == 'A' else 'Path B – Geotecnico'
        en_lab = 'Path A – Geophysical' if k[0] == 'A' else 'Path B – Geotechnical'
        o += bil(LXP, y + 5, 15, NAVY, it_lab, en_lab, anchor='end', font=DISP,
                 extra=' fill-opacity=".9"')
        x = PX
        for _, _, days, exposed in PATHS[k]:
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="%s" fill-opacity="%s"/>'
                     % (x + .6, y - 13, days * DAYW - 1.2, NAVY, '.85' if exposed else '.22'))
            x += days * DAYW
        if tot(k) < crit:
            o.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="none" stroke="%s" '
                     'stroke-opacity=".45" stroke-dasharray="4 3"/>'
                     % (x + .6, y - 13, (crit - tot(k)) * DAYW - 1.2, NAVY))
        end = PX + crit * DAYW + 14
        if tot(k) == crit:
            o += bil(end, y + 5, 14, AMBER, '%d GIORNI – CRITICO' % tot(k),
                     '%d DAYS – CRITICAL' % tot(k))
        else:
            o += bil(end, y + 5, 14, STEEL, '%d GIORNI – FLOAT %d' % (tot(k), crit - tot(k)),
                     '%d DAYS – FLOAT %d' % (tot(k), crit - tot(k)))

# dove sono finiti i giorni in piu'
for k, key, delta in (('A_rec', 'Acquisizione', 1), ('B_rec', 'Campionamento', 7)):
    y = 340 + 40 + (0 if k[0] == 'A' else 60)
    x = PX
    for name, _, days, _ in PATHS[k]:
        if name == key:
            o += bil(x + days * DAYW / 2, y - 20, 14, AMBER, '+%d' % delta, '+%d' % delta,
                     anchor='middle')
            break
        x += days * DAYW

for x, op, it, en in ((290, '.85', 'ESPOSTO AL METEO', 'WEATHER-EXPOSED'),
                      (620, '.22', 'A TERRA', 'ONSHORE')):
    o.append('<rect x="%d" y="505" width="16" height="16" fill="%s" fill-opacity="%s"/>' % (x, NAVY, op))
    o += bil(x + 26, 518, 14, NAVY, it, en, extra=' fill-opacity=".8"')
o.append('<rect x="900" y="505" width="16" height="16" fill="none" stroke="%s" '
         'stroke-opacity=".45" stroke-dasharray="4 3"/>' % NAVY)
o += bil(926, 518, 14, NAVY, 'FLOAT', 'FLOAT', extra=' fill-opacity=".8"')
o.append('</svg>')
open('fig_art_swap.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_swap.svg', len('\n'.join(o)), 'chars')
