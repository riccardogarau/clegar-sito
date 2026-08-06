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
W, H = 1400, 620
PHASES = [
    ('Specifica',      'Specification'),
    ('Gara',           'Tender'),
    ('Mobilitazione',  'Mobilisation'),
    ('Acquisizione',   'Acquisition'),
    ('Processing',     'Processing'),
    ('Accettazione',   'Acceptance'),
]
X0, X1 = 150, 1300
ROW_A, ROW_B = 190, 430          # origin row, surfacing row
BW = (X1 - X0) / len(PHASES)

# qualitative weight of where issues originate / where they become visible
ORIGIN  = [0.42, 0.20, 0.14, 0.10, 0.08, 0.06]
SURFACE = [0.02, 0.04, 0.08, 0.16, 0.28, 0.42]

o = ['<svg viewBox="0 0 %d %d" xmlns="http://www.w3.org/2000/svg" role="img" '
     'aria-label="Where offshore project problems originate compared with where they surface">' % (W, H)]
o.append('<defs><marker id="fa" viewBox="0 0 9 9" refX="8" refY="4.5" markerWidth="7" markerHeight="7" '
         'orient="auto"><path d="M0,1 L8,4.5 L0,8 Z" fill="%s" fill-opacity=".55"/></marker></defs>' % AMBER)

o += bil(0, 52, 16, NAVY,
         'Dove nascono i problemi, dove si manifestano',
         'Where problems originate, where they surface', font=DISP)
o += bil(0, 76, 10.5, STEEL,
         'SCHEMA QUALITATIVO — NON SONO DATI MISURATI',
         'QUALITATIVE SCHEMATIC — NOT MEASURED DATA')

# phase columns
for i, (it, en) in enumerate(PHASES):
    x = X0 + i * BW
    if i % 2 == 0:
        o.append('<rect x="%.1f" y="110" width="%.1f" height="%d" fill="%s" fill-opacity=".025"/>'
                 % (x, BW, ROW_B + 130 - 110, NAVY))
    o += bil(x + BW / 2, 132, 11, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".72"')

# row A — origin
o += bil(0, ROW_A + 4, 11, NAVY, 'ORIGINE DEL PROBLEMA', 'WHERE IT ORIGINATES')
for i, v in enumerate(ORIGIN):
    x = X0 + i * BW + BW / 2
    r = 16 + v * 120
    o.append('<circle cx="%.1f" cy="%d" r="%.1f" fill="%s" fill-opacity="%.2f"/>'
             % (x, ROW_A, r, NAVY, 0.18 + v * 1.1))

# row B — surfacing
o += bil(0, ROW_B + 4, 11, NAVY, 'DOVE DIVENTA VISIBILE', 'WHERE IT BECOMES VISIBLE')
for i, v in enumerate(SURFACE):
    x = X0 + i * BW + BW / 2
    r = 16 + v * 120
    o.append('<circle cx="%.1f" cy="%d" r="%.1f" fill="%s" fill-opacity="%.2f"/>'
             % (x, ROW_B, r, AMBER, 0.18 + v * 1.1))

# the lag: specification -> acceptance
sx = X0 + 0 * BW + BW / 2
ex = X0 + 5 * BW + BW / 2
o.append('<path d="M%.1f,%d C%.1f,%d %.1f,%d %.1f,%d" fill="none" stroke="%s" stroke-width="1.6" '
         'stroke-dasharray="7 5" marker-end="url(#fa)"/>'
         % (sx, ROW_A + 62, sx + 260, ROW_A + 190, ex - 300, ROW_B - 110, ex - 4, ROW_B - 60, AMBER))
o += bil((sx + ex) / 2, ROW_A + 96, 11.5, AMBER,
         'IL COSTO DELLA CORREZIONE CRESCE LUNGO QUESTO PERCORSO',
         'THE COST OF FIXING IT GROWS ALONG THIS PATH', anchor='middle')

# closing note
o.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".18"/>'
         % (0, ROW_B + 96, X1, ROW_B + 96, NAVY))
o += bil(0, ROW_B + 128, 13.5, NAVY,
         'Una tolleranza non definita in specifica diventa una discussione contrattuale in accettazione.',
         'A tolerance left undefined in the specification becomes a contractual argument at acceptance.',
         font=DISP, extra=' fill-opacity=".85"')
o.append('</svg>')
open('fig_art_origin.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_origin.svg', len('\n'.join(o)), 'chars')


# ═══════════════════════════════════ FIG B — service lines across lifecycle
W, H = 1400, 560
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
o += bil(0, 52, 16, NAVY,
         'Le cinque linee di servizio lungo il ciclo di progetto',
         'The five service lines across the project lifecycle', font=DISP)
o += bil(0, 76, 10.5, STEEL,
         'DOVE INTERVIENE CIASCUNA LINEA', 'WHERE EACH LINE APPLIES')

for i, (it, en) in enumerate(PHASES):
    x = GX0 + i * BW2
    o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".1"/>'
             % (x, 120, x, TOP + len(LINES) * RH - 10, NAVY))
    o += bil(x + BW2 / 2, 142, 10.5, NAVY, it.upper(), en.upper(), anchor='middle', extra=' fill-opacity=".7"')
o.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="%s" stroke-opacity=".1"/>'
         % (GX1, 120, GX1, TOP + len(LINES) * RH - 10, NAVY))

for j, (it, en, a, b, col) in enumerate(LINES):
    y = TOP + j * RH
    o += bil(LX, y + 5, 13.5, NAVY, it, en, anchor='end', font=DISP, extra=' fill-opacity=".9"')
    x = GX0 + a * BW2
    w = (b - a) * BW2
    o.append('<rect x="%.1f" y="%.1f" width="%.1f" height="16" rx="2" fill="%s" fill-opacity=".82"/>'
             % (x + 4, y - 8, w - 8, col))

o.append('<line x1="0" y1="%d" x2="%d" y2="%d" stroke="%s" stroke-opacity=".18"/>'
         % (TOP + len(LINES) * RH + 18, GX1, TOP + len(LINES) * RH + 18, NAVY))
o += bil(0, TOP + len(LINES) * RH + 50, 13.5, NAVY,
         'Le prime tre linee coprono l\u2019intero ciclo: i criteri si definiscono prima, si verificano dopo.',
         'The first three lines span the whole cycle: criteria are set early and verified later.',
         font=DISP, extra=' fill-opacity=".85"')
o.append('</svg>')
open('fig_art_lines.svg', 'w', encoding='utf-8').write('\n'.join(o))
print('fig_art_lines.svg', len('\n'.join(o)), 'chars')
