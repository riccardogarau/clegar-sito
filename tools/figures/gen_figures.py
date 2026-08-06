import numpy as np

NAVY, BLUE, TEAL, AMBER, STEEL = '#0B2545', '#3B87BE', '#009AA6', '#C9821E', '#8B9598'
MONO = 'font-family="IBM Plex Mono, monospace" letter-spacing="1.1"'
DISP = 'font-family="Archivo, sans-serif"'


def esc(t):
    return str(t).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def head(w, h, label):
    return ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">' % (w, h, label)]


def bil(x, y, size, fill, it, en, anchor='start', font=MONO, extra=''):
    return ['<text class="it" %s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (font, x, y, size, fill, anchor, extra, esc(it)),
            '<text class="en" %s x="%.1f" y="%.1f" font-size="%s" fill="%s" text-anchor="%s"%s>%s</text>'
            % (font, x, y, size, fill, anchor, extra, esc(en))]


# ══════════════════════════════════════════ A. S-44 CROSSLINE CHECK
def tvu(d, a, b):
    return np.sqrt(a ** 2 + (b * d) ** 2)

rng = np.random.default_rng(11)
N = 430
depth = rng.uniform(9, 57, N)
o1a = tvu(depth, 0.50, 0.0130)
so = tvu(depth, 0.25, 0.0075)
dz = rng.normal(0, 0.30 * o1a)

# one survey block carries an uncorrected tide offset
blk = np.where((depth > 27) & (depth < 45))[0]
pick = rng.choice(blk, size=28, replace=False)
dz[pick] += rng.normal(0.62, 0.09, 28)

adz = np.abs(dz)
f1a, fso = adz > o1a, adz > so
print('S-44: N=%d | mean %.3f m | sd %.3f m | > Special Order %d (%.1f%%) | > Order 1a %d (%.1f%%)'
      % (N, dz.mean(), dz.std(), fso.sum(), 100*fso.mean(), f1a.sum(), 100*f1a.mean()))

W, H = 1400, 720
PL, PR, PT, PB = 130, 1010, 96, 556
HX0, HX1 = 1060, 1330
DMAX, ZMAX = 60.0, 1.25

def px(d): return PL + (PR - PL) * d / DMAX
def py(z): return (PT + PB) / 2 - (PB - PT) / 2 * z / ZMAX

o = head(W, H, 'Crossline difference check against IHO S-44 uncertainty limits')
o.append('<defs><marker id="ar2" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" '
         'orient="auto"><path d="M0,1 L7,4 L0,7 Z" fill="%s"/></marker></defs>' % AMBER)

o += bil(PL, 46, 15, NAVY, 'Verifica indipendente — differenze ai punti di incrocio',
         'Independent check — differences at line crossings', font=DISP)
o += bil(PL, 68, 10.5, STEEL, 'CONFRONTO CON I LIMITI DI INCERTEZZA IHO S-44',
         'AGAINST IHO S-44 UNCERTAINTY LIMITS')

# allowable envelope
ds = np.linspace(0.5, DMAX, 160)
def band(a, b):
    up = ' '.join('%.1f,%.1f' % (px(d), py(tvu(d, a, b))) for d in ds)
    dn = ' '.join('%.1f,%.1f' % (px(d), py(-tvu(d, a, b))) for d in ds[::-1])
    return up + ' ' + dn
o.append('<polygon points="%s" fill="%s" fill-opacity=".07"/>' % (band(0.50, 0.0130), BLUE))
for sgn in (1, -1):
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.8"/>'
             % (' '.join('%.1f,%.1f' % (px(d), py(sgn*tvu(d, .50, .0130))) for d in ds), BLUE))
    o.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="1.4" stroke-dasharray="6 4"/>'
             % (' '.join('%.1f,%.1f' % (px(d), py(sgn*tvu(d, .25, .0075))) for d in ds), TEAL))

# axes
o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".45"/>' % (PL, py(0), PR, py(0), NAVY))
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".35"/>' % (PL, PT, PL, PB, NAVY))
for z in (-1.0, -0.5, 0.5, 1.0):
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".09"/>' % (PL, py(z), PR, py(z), NAVY))
    o.append('<text %s x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%+.1f</text>' % (MONO, PL-9, py(z)+3.5, STEEL, z))
for d in range(0, 61, 10):
    o.append('<text %s x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%d</text>' % (MONO, px(d), PB+22, STEEL, d))
o += bil((PL+PR)/2, PB+44, 10.5, STEEL, 'PROFONDITÀ (m)', 'DEPTH (m)', anchor='middle')
o += bil(PL-9, PT-14, 10.5, STEEL, 'Δz (m)', 'Δz (m)', anchor='end')

# points
for i in range(N):
    x, y = px(depth[i]), py(np.clip(dz[i], -ZMAX, ZMAX))
    if f1a[i]:
        o.append('<circle cx="%.1f" cy="%.1f" r="4.2" fill="none" stroke="%s" stroke-width="1.7"/>' % (x, y, AMBER))
    elif fso[i]:
        o.append('<circle cx="%.1f" cy="%.1f" r="2.6" fill="%s" fill-opacity=".75"/>' % (x, y, BLUE))
    else:
        o.append('<circle cx="%.1f" cy="%.1f" r="2.2" fill="%s" fill-opacity=".55"/>' % (x, y, NAVY))

# callout on the failing block
cx, cy = px(36), py(0.72)
o.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4" marker-end="url(#ar2)"/>' % (cx+120, cy-56, cx+26, cy-12, AMBER))
o += bil(cx+128, cy-60, 10.5, AMBER, 'BLOCCO CON MAREA NON CORRETTA', 'BLOCK WITH UNCORRECTED TIDE')

# marginal histogram
cnt, edges = np.histogram(dz, bins=26, range=(-ZMAX, ZMAX))
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".35"/>' % (HX0, PT, HX0, PB, NAVY))
for k in range(len(cnt)):
    y0, y1 = py(edges[k+1]), py(edges[k])
    o.append('<rect x="%d" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity=".45"/>'
             % (HX0, y0, (HX1-HX0)*cnt[k]/cnt.max(), y1-y0-1, NAVY))
o += bil(HX0, PT-14, 10.5, STEEL, 'DISTRIBUZIONE', 'DISTRIBUTION')

# stats
sy = PB + 74
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".18"/>' % (PL, sy-30, HX1, sy-30, NAVY))
stats = [('INCROCI ANALIZZATI', 'CROSSINGS ANALYSED', '%d' % N, NAVY),
         ('MEDIA', 'MEAN', '%+.3f m' % dz.mean(), NAVY),
         ('DEV. STANDARD', 'STANDARD DEVIATION', '%.3f m' % dz.std(), NAVY),
         ('OLTRE SPECIAL ORDER', 'ABOVE SPECIAL ORDER', '%d (%.1f%%)' % (fso.sum(), 100*fso.mean()), BLUE),
         ('OLTRE ORDER 1a', 'ABOVE ORDER 1a', '%d (%.1f%%)' % (f1a.sum(), 100*f1a.mean()), AMBER)]
for i, (a, b, val, col) in enumerate(stats):
    x = PL + i * 246
    o += bil(x, sy, 9.5, STEEL, a, b)
    o.append('<text %s x="%.1f" y="%.1f" font-size="19" fill="%s">%s</text>' % (DISP, x, sy+28, col, val))

# legend — swatch (circle or 17px line) then an 7px gap before the label,
# matching the layout already verified working in render_gantt.py
ly = H - 16
LEG = [
    (0,   'circle', dict(r=2.6, fill=NAVY),                                  'ENTRO SPECIAL ORDER', 'WITHIN SPECIAL ORDER'),
    (232, 'circle', dict(r=2.6, fill=BLUE),                                  'ENTRO ORDER 1a', 'WITHIN ORDER 1a'),
    (446, 'circle', dict(r=4.2, fill='none', stroke=AMBER, sw=1.7),          'FUORI TOLLERANZA', 'OUT OF TOLERANCE'),
    (672, 'line',   dict(stroke=TEAL, sw=1.4, dash='5 3'),                   'LIMITE SPECIAL ORDER', 'SPECIAL ORDER LIMIT'),
    (924, 'line',   dict(stroke=BLUE, sw=1.8, dash=None),                    'LIMITE ORDER 1a', 'ORDER 1a LIMIT'),
]
SW = 17    # swatch footprint in px, kept equal for every item
GAP = 7    # clear space between swatch and label — never overlaps
for dx, kind, st, it, en in LEG:
    xx = PL + dx
    if kind == 'circle':
        extra = (' stroke="%s" stroke-width="%s"' % (st['stroke'], st['sw'])) if 'stroke' in st else ''
        o.append('<circle cx="%.1f" cy="%d" r="%.1f" fill="%s"%s/>' % (xx + SW/2, ly-4, st['r'], st['fill'], extra))
    else:
        dash = ' stroke-dasharray="%s"' % st['dash'] if st['dash'] else ''
        o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-width="%s"%s/>'
                  % (xx, ly-4, xx+SW, ly-4, st['stroke'], st['sw'], dash))
    o += bil(xx + SW + GAP, ly, 9.5, STEEL, it, en)
o.append('</svg>')
open('fig_advisory.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_advisory.svg', len('\n'.join(o)), 'chars')


# ══════════════════════════════════════ B. MOBILISATION ACCEPTANCE RECORD
P = [  # name_it, name_en, unit, measured, tolerance, rerun
    ('Bias di rollio MBES',          'MBES roll bias',              '°', -0.06, 0.20, None),
    ('Bias di beccheggio MBES',      'MBES pitch bias',             '°',  0.09, 0.20, None),
    ('Bias di imbardata MBES',       'MBES yaw bias',               '°', -0.11, 0.25, None),
    ('Latenza posizionamento',       'Positioning latency',         's',  0.012, 0.030, None),
    ('Verifica su punto noto',       'Check against known point',   'm',  0.14, 0.35, None),
    ('Allineamento giroscopico',     'Gyro alignment',              '°',  0.21, 0.50, None),
    ('Residuo calibrazione USBL',    'USBL calibration residual',   'm',  0.42, 0.60, None),
    ('Bar check contro SVP',         'Bar check against SVP',       'm',  0.05, 0.10, None),
    ('Accuratezza heave',            'Heave accuracy',              'm',  0.031, 0.050, None),
    ('Confronto mareografo',         'Tide gauge comparison',       'm',  0.38, 0.15, 0.07),
]
W, H = 1400, 720
LX, BX0, BX1 = 40, 470, 1090
RT, RH0 = 150, 46

o = head(W, H, 'Mobilisation acceptance record: measured values against tolerance')
o += bil(LX, 46, 15, NAVY, 'Verbale di accettazione della mobilitazione',
         'Mobilisation acceptance record', font=DISP)
o += bil(LX, 68, 10.5, STEEL, 'VERIFICHE TESTIMONIATE IN BANCHINA PRIMA DELLA PARTENZA',
         'CHECKS WITNESSED ALONGSIDE BEFORE SAILING')
o += bil(BX1 + 70, 46, 10.5, STEEL, 'ESITO', 'RESULT')
o.append('<line x1="%d" y1="102" x2="%d" y2="102" stroke="%s" stroke-opacity=".3"/>' % (LX, 1360, NAVY))

# scale header: tolerance normalised so every row shares one axis
mid = (BX0 + BX1) / 2
def tx(f): return mid + (BX1 - mid) * f / 1.6
for f, lab in [(-1.6, ''), (-1, '−tol'), (0, '0'), (1, '+tol'), (1.6, '')]:
    if lab:
        o.append('<text %s x="%.1f" y="%d" font-size="10" fill="%s" text-anchor="middle">%s</text>' % (MONO, tx(f), 122, STEEL, lab))
o += bil(BX0 - 12, 122, 10.5, STEEL, 'MISURATO / TOLLERANZA', 'MEASURED / TOLERANCE', anchor='end')

npass = 0
for i, (nit, nen, unit, val, tol, rerun) in enumerate(P):
    y = RT + i * RH0
    fail = abs(val) > tol
    final = rerun if rerun is not None else val
    if not (abs(final) > tol):
        npass += 1
    if i % 2 == 0:
        o.append('<rect x="%d" y="%.1f" width="%d" height="%d" fill="%s" fill-opacity=".025"/>' % (LX, y-16, 1320, RH0-6, NAVY))
    o += bil(LX, y, 13.5, NAVY, nit, nen, font=DISP, extra=' fill-opacity=".9"')
    # tolerance band
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" fill="%s" fill-opacity=".13" rx="2"/>'
             % (tx(-1), y-12, tx(1)-tx(-1), TEAL))
    o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-opacity=".35" stroke-dasharray="2 3"/>' % (mid, y-14, mid, y+6, NAVY))
    for f in (-1, 1):
        o.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="1.4"/>' % (tx(f), y-13, tx(f), y+5, STEEL))
    # measured marker
    mx = tx(np.clip(val/tol, -1.55, 1.55))
    col = AMBER if fail else NAVY
    o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (mx, y-4, col))
    if rerun is not None:
        rx = tx(np.clip(rerun/tol, -1.55, 1.55))
        o.append('<path d="M%.1f,%.1f L%.1f,%.1f" stroke="%s" stroke-width="1.4" stroke-dasharray="3 3"/>' % (mx-6, y-4, rx+7, y-4, STEEL))
        o.append('<circle cx="%.1f" cy="%.1f" r="5" fill="%s"/>' % (rx, y-4, TEAL))
    o.append('<text %s x="%d" y="%.1f" font-size="12" fill="%s" text-anchor="end">%+.3f %s</text>'
             % (MONO, BX1+56, y, NAVY, final, unit))
    if rerun is None:
        o += bil(BX1+80, y, 10, TEAL, 'ACCETTATO', 'ACCEPTED')
    else:
        o += bil(BX1+80, y, 10, AMBER, 'RIPETUTO → ACCETTATO', 'RE-RUN → ACCEPTED')

fy = RT + len(P)*RH0 + 26
o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".3"/>' % (LX, fy, 1360, fy, NAVY))
o += bil(LX, fy+30, 9.5, STEEL, 'VOCI VERIFICATE', 'ITEMS VERIFIED')
o.append('<text %s x="%d" y="%.1f" font-size="19" fill="%s">%d</text>' % (DISP, LX, fy+58, NAVY, len(P)))
o += bil(LX+250, fy+30, 9.5, STEEL, 'ACCETTATE ALLA PRIMA', 'ACCEPTED FIRST TIME')
o.append('<text %s x="%d" y="%.1f" font-size="19" fill="%s">%d</text>' % (DISP, LX+250, fy+58, NAVY, len(P)-1))
o += bil(LX+520, fy+30, 9.5, STEEL, 'RESPINTE E RIPETUTE', 'REJECTED AND RE-RUN')
o.append('<text %s x="%d" y="%.1f" font-size="19" fill="%s">1</text>' % (DISP, LX+520, fy+58, AMBER))
o += bil(LX+790, fy+30, 9.5, STEEL, 'ESITO MOBILITAZIONE', 'MOBILISATION OUTCOME')
o += bil(LX+790, fy+58, 19, TEAL, 'FIRMATA', 'SIGNED OFF', font=DISP)
o.append('</svg>')
open('fig_owners.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_owners.svg  accepted first time: %d/%d' % (len(P)-1, len(P)))


# ══════════════════════════════════════════ C. VESSEL TIME ACCOUNTING
CATS = [('Produzione in linea', 'Line production',    NAVY),
        ('Cambio linea',        'Line turns',         BLUE),
        ('Transito',            'Transit',            STEEL),
        ('Calibrazioni e SVP',  'Calibrations & SVP', TEAL),
        ('Standby meteo',       'Weather standby',    AMBER),
        ('Fermo strumentazione','Equipment downtime', '#8C4A3B')]
rng = np.random.default_rng(5)
D = 18
hours = np.zeros((D, 6))
for d in range(D):
    if d in (6, 7):        base = [4.0, 1.0, 0.5, 0.5, 17.0, 1.0]
    elif d == 11:          base = [9.0, 1.5, 0.5, 0.5, 0.5, 12.0]
    elif d in (0, 1):      base = [13.0, 2.0, 4.0, 3.0, 1.5, 0.5]
    else:                  base = [17.5, 2.4, 0.9, 1.0, 1.6, 0.6]
    v = np.maximum(np.array(base) + rng.normal(0, 0.55, 6), 0)
    hours[d] = v / v.sum() * 24

tot = hours.sum(0); pct = 100 * tot / tot.sum()
print('vessel time: ' + ' | '.join('%s %.1f%%' % (c[1], p) for c, p in zip(CATS, pct)))

W, H = 1400, 720
GX0, GX1, GY0, GY1 = 96, 1010, 118, 520
BW = (GX1 - GX0) / D * 0.66
o = head(W, H, 'Vessel time accounting by day and category')
o += bil(GX0-56, 46, 15, NAVY, 'Impiego del tempo nave — campagna di 18 giorni',
         'Vessel time accounting — 18-day campaign', font=DISP)
o += bil(GX0-56, 68, 10.5, STEEL, 'RIPARTIZIONE DELLE 24 ORE PER CAUSALE',
         'ALL 24 HOURS ALLOCATED BY CAUSE')

for h in range(0, 25, 6):
    y = GY1 - (GY1-GY0)*h/24
    o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-opacity=".1"/>' % (GX0, y, GX1, y, NAVY))
    o.append('<text %s x="%d" y="%.1f" font-size="10" fill="%s" text-anchor="end">%dh</text>' % (MONO, GX0-10, y+3.5, STEEL, h))
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".4"/>' % (GX0, GY1, GX1, GY1, NAVY))

for d in range(D):
    x = GX0 + (GX1-GX0)*(d+0.5)/D - BW/2
    acc = 0.0
    for c in range(6):
        hgt = (GY1-GY0)*hours[d, c]/24
        o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                 % (x, GY1-acc-hgt, BW, hgt, CATS[c][2]))
        acc += hgt
    o.append('<text %s x="%.1f" y="%d" font-size="9.5" fill="%s" text-anchor="middle">D%02d</text>'
             % (MONO, x+BW/2, GY1+20, STEEL, d+1))

ty = GY1 - (GY1-GY0)*17.0/24
o.append('<line x1="%d" y1="%.1f" x2="%d" y2="%.1f" stroke="%s" stroke-width="1.6" stroke-dasharray="6 4"/>' % (GX0, ty, GX1, ty, TEAL))
o += bil(GX1-6, ty-8, 10, TEAL, 'OBIETTIVO PRODUZIONE 17 h', 'PRODUCTION TARGET 17 h', anchor='end')

for d0, d1, it, en, col in [(6, 7, 'FINESTRA METEO', 'WEATHER WINDOW', AMBER),
                            (11, 11, 'GUASTO VERRICELLO', 'WINCH FAILURE', '#8C4A3B')]:
    xa = GX0 + (GX1-GX0)*(d0+0.5)/D - BW/2 - 4
    xb = GX0 + (GX1-GX0)*(d1+0.5)/D + BW/2 + 4
    o.append('<path d="M%.1f,%d L%.1f,%d L%.1f,%d L%.1f,%d" fill="none" stroke="%s" stroke-width="1.3"/>'
             % (xa, GY0-8, xa, GY0-16, xb, GY0-16, xb, GY0-8, col))
    o += bil((xa+xb)/2, GY0-24, 10, col, it, en, anchor='middle')

# campaign totals
BY = 596
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".18"/>' % (GX0-56, BY-40, 1360, BY-40, NAVY))
o += bil(GX0-56, BY-16, 10.5, STEEL, 'TOTALE CAMPAGNA', 'CAMPAIGN TOTAL')
acc = 0.0
FW = 1360 - (GX0-56)
for c in range(6):
    w = FW * pct[c] / 100
    o.append('<rect x="%.1f" y="%d" width="%.1f" height="26" fill="%s"/>' % (GX0-56+acc, BY, w, CATS[c][2]))
    if w > 46:
        o.append('<text %s x="%.1f" y="%d" font-size="11" fill="#fff" text-anchor="middle">%.0f%%</text>'
                 % (MONO, GX0-56+acc+w/2, BY+18, pct[c]))
    acc += w

ly = H - 16
for c in range(6):
    x = GX0 - 56 + c * 222
    o.append('<rect x="%d" y="%d" width="16" height="9" fill="%s"/>' % (x, ly-8, CATS[c][2]))
    o += bil(x+22, ly, 9.5, STEEL, CATS[c][0].upper(), CATS[c][1].upper())
o.append('</svg>')
open('fig_opex.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_opex.svg written')
