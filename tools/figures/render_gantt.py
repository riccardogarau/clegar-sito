import json

d = json.load(open('sched.json'))
T, ES, EF, LF, FLOAT, CRIT = d['T'], d['ES'], d['EF'], d['LF'], d['FLOAT'], d['CRIT']
END, DD = d['END'], d['DATA_DATE']
planned, actual = d['planned'], d['actual']

VW, VH = 1400, 780
L, R = 296, 1352                      # timeline left / right
TOP, RH = 118, 32                     # first row y, row height
GB = TOP + len(T) * RH + 6            # gantt bottom
SC_T, SC_B = GB + 92, VH - 46         # s-curve panel

def X(w):  return L + (R - L) * w / END
def Y(i):  return TOP + i * RH

NAVY, BLUE, TEAL, AMBER, STEEL = '#0B2545', '#3B87BE', '#009AA6', '#C9821E', '#8B9598'
o = []
A = o.append

A(f'<svg viewBox="0 0 {VW} {VH}" xmlns="http://www.w3.org/2000/svg" role="img" '
  f'aria-label="Project schedule with critical path, float and progress S-curve">')
A('<defs>'
  '<pattern id="wxh" width="7" height="7" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">'
  f'<line x1="0" y1="0" x2="0" y2="7" stroke="{AMBER}" stroke-width="3" stroke-opacity=".45"/></pattern>'
  f'<marker id="arw" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="6" markerHeight="6" orient="auto">'
  f'<path d="M0,1 L7,4 L0,7 Z" fill="{STEEL}"/></marker>'
  '</defs>')
MONO = 'font-family="IBM Plex Mono, monospace" letter-spacing="1.1"'
DISP = 'font-family="Archivo, sans-serif"'

# ---------------------------------------------------------------- time axis
A(f'<line x1="{L}" y1="{TOP-16}" x2="{R}" y2="{TOP-16}" stroke="{NAVY}" stroke-opacity=".3"/>')
for w in range(0, END + 1, 2):
    A(f'<line x1="{X(w):.1f}" y1="{TOP-16}" x2="{X(w):.1f}" y2="{GB}" '
      f'stroke="{NAVY}" stroke-opacity="{0.11 if w % 4 else 0.18}"/>')
    A(f'<text class="m" x="{X(w):.1f}" y="{TOP-24}" font-size="10.5" fill="{STEEL}" '
      f'text-anchor="middle">W{w:02d}</text>')

# month bands
A(f'<text class="m it" x="{L}" y="{TOP-46}" font-size="10.5" fill="{NAVY}" fill-opacity=".55">MESE 1</text>')
for i, mx in enumerate([0, 4.35, 8.7, 13.0, 17.4, 21.7], start=1):
    if i == 1: continue
    A(f'<line x1="{X(mx):.1f}" y1="{TOP-56}" x2="{X(mx):.1f}" y2="{TOP-16}" stroke="{NAVY}" stroke-opacity=".22"/>')
    A(f'<text class="m it" x="{X(mx)+7:.1f}" y="{TOP-46}" font-size="10.5" fill="{NAVY}" fill-opacity=".55">MESE {i}</text>')
    A(f'<text class="m en" x="{X(mx)+7:.1f}" y="{TOP-46}" font-size="10.5" fill="{NAVY}" fill-opacity=".55">MONTH {i}</text>')
A(f'<text class="m en" x="{L}" y="{TOP-46}" font-size="10.5" fill="{NAVY}" fill-opacity=".55">MONTH 1</text>')

# --------------------------------------------------------------- task rows
for i, t in enumerate(T):
    k, nit, nen, dur = t[0], t[1], t[2], t[3]
    y = Y(i)
    if i % 2 == 0:
        A(f'<rect x="{L}" y="{y-2}" width="{R-L}" height="{RH-4}" fill="{NAVY}" fill-opacity=".025"/>')
    A(f'<text class="d it" x="{L-16}" y="{y+16}" font-size="13.5" fill="{NAVY}" '
      f'fill-opacity="{0.92 if CRIT[k] else 0.62}" text-anchor="end">{nit}</text>')
    A(f'<text class="d en" x="{L-16}" y="{y+16}" font-size="13.5" fill="{NAVY}" '
      f'fill-opacity="{0.92 if CRIT[k] else 0.62}" text-anchor="end">{nen}</text>')

    x0, x1 = X(ES[k]), X(EF[k])
    bh = 15
    by = y + 4
    if k == 'wx':
        A(f'<rect x="{x0:.1f}" y="{by}" width="{x1-x0:.1f}" height="{bh}" fill="url(#wxh)"/>')
        A(f'<rect x="{x0:.1f}" y="{by}" width="{x1-x0:.1f}" height="{bh}" fill="none" '
          f'stroke="{AMBER}" stroke-width="1.2"/>')
    else:
        col = NAVY if CRIT[k] else BLUE
        op = 1 if CRIT[k] else .55
        A(f'<rect x="{x0:.1f}" y="{by}" width="{x1-x0:.1f}" height="{bh}" fill="{col}" fill-opacity="{op}" rx="1.5"/>')
        # % complete against the data date
        pc = 0 if ES[k] >= DD else (1 if EF[k] <= DD else (DD - ES[k]) / dur)
        if pc > 0:
            A(f'<rect x="{x0:.1f}" y="{by+5}" width="{(x1-x0)*pc:.1f}" height="{bh-10}" '
              f'fill="#fff" fill-opacity=".72"/>')
    # float
    if FLOAT[k] > 0:
        A(f'<line x1="{x1:.1f}" y1="{by+bh/2}" x2="{X(LF[k]):.1f}" y2="{by+bh/2}" '
          f'stroke="{STEEL}" stroke-width="1" stroke-dasharray="3 3"/>')
        A(f'<line x1="{X(LF[k]):.1f}" y1="{by+2}" x2="{X(LF[k]):.1f}" y2="{by+bh-2}" '
          f'stroke="{STEEL}" stroke-width="1"/>')
        A(f'<text class="m" x="{X(LF[k])+7:.1f}" y="{by+bh-3}" font-size="9.5" fill="{STEEL}">'
          f'+{FLOAT[k]}w</text>')

# ------------------------------------------------------ dependency arrows
for i, t in enumerate(T):
    k = t[0]
    for p, lag in t[4]:
        pi = [j for j, q in enumerate(T) if q[0] == p][0]
        x_from, y_from = X(EF[p]), Y(pi) + 11.5
        x_to,   y_to   = X(ES[k]), Y(i) + 11.5
        mid = x_from + 9 if x_to >= x_from else x_to - 12
        A(f'<path d="M{x_from:.1f},{y_from:.1f} H{mid:.1f} V{y_to:.1f} H{x_to-4:.1f}" '
          f'fill="none" stroke="{STEEL}" stroke-width="1" stroke-opacity=".65" marker-end="url(#arw)"/>')

# ------------------------------------------------------------- milestones
MS = [('bid', 'AGGIUDICAZIONE', 'AWARD'), ('equip', 'PARTENZA', 'SAIL'),
      ('demob', 'DEMOB', 'DEMOB'), ('review', 'CONSEGNA FINALE', 'FINAL DELIVERY')]
for k, mit, men in MS:
    i = [j for j, q in enumerate(T) if q[0] == k][0]
    x, y = X(EF[k]), Y(i) + 11.5
    A(f'<path d="M{x:.1f},{y-7} l7,7 l-7,7 l-7,-7 Z" fill="{TEAL}"/>')
    anchor = 'end' if k == 'review' else 'start'
    dx = -12 if k == 'review' else 12
    A(f'<text class="m it" x="{x+dx:.1f}" y="{y-10}" font-size="9.5" fill="{TEAL}" text-anchor="{anchor}">{mit}</text>')
    A(f'<text class="m en" x="{x+dx:.1f}" y="{y-10}" font-size="9.5" fill="{TEAL}" text-anchor="{anchor}">{men}</text>')

# -------------------------------------------------------------- data date
A(f'<line x1="{X(DD):.1f}" y1="{TOP-58}" x2="{X(DD):.1f}" y2="{SC_B}" stroke="{AMBER}" '
  f'stroke-width="1.4" stroke-dasharray="5 4"/>')
A(f'<text class="m it" x="{X(DD)+8:.1f}" y="{TOP-62}" font-size="10" fill="{AMBER}">DATA DATE · W{DD}</text>')
A(f'<text class="m en" x="{X(DD)+8:.1f}" y="{TOP-62}" font-size="10" fill="{AMBER}">DATA DATE · W{DD}</text>')

# ============================================================== S-CURVE
A(f'<line x1="{L}" y1="{SC_B}" x2="{R}" y2="{SC_B}" stroke="{NAVY}" stroke-opacity=".35"/>')
A(f'<line x1="{L}" y1="{SC_T}" x2="{L}" y2="{SC_B}" stroke="{NAVY}" stroke-opacity=".35"/>')
for pct in (0, 25, 50, 75, 100):
    yy = SC_B - (SC_B - SC_T) * pct / 100
    A(f'<line x1="{L}" y1="{yy:.1f}" x2="{R}" y2="{yy:.1f}" stroke="{NAVY}" stroke-opacity=".09"/>')
    A(f'<text class="m" x="{L-10}" y="{yy+3.5:.1f}" font-size="10" fill="{STEEL}" text-anchor="end">{pct}%</text>')

A(f'<text class="d it" x="{L-16}" y="{SC_T-14}" font-size="13.5" fill="{NAVY}" text-anchor="end">Avanzamento cumulato</text>')
A(f'<text class="d en" x="{L-16}" y="{SC_T-14}" font-size="13.5" fill="{NAVY}" text-anchor="end">Cumulative progress</text>')

def curve(vals):
    return ' '.join(f'{X(w):.1f},{SC_B-(SC_B-SC_T)*v/100:.1f}' for w, v in enumerate(vals))

A(f'<polyline points="{curve(planned)}" fill="none" stroke="{BLUE}" stroke-width="2" stroke-dasharray="6 4"/>')
A(f'<polygon points="{X(0):.1f},{SC_B} {curve(actual)} {X(len(actual)-1):.1f},{SC_B}" '
  f'fill="{NAVY}" fill-opacity=".10"/>')
A(f'<polyline points="{curve(actual)}" fill="none" stroke="{NAVY}" stroke-width="2.4"/>')

pv = SC_B - (SC_B - SC_T) * planned[DD] / 100
av = SC_B - (SC_B - SC_T) * actual[-1] / 100
A(f'<circle cx="{X(DD):.1f}" cy="{pv:.1f}" r="3.4" fill="{BLUE}"/>')
A(f'<circle cx="{X(DD):.1f}" cy="{av:.1f}" r="3.8" fill="{NAVY}"/>')
A(f'<line x1="{X(DD):.1f}" y1="{pv:.1f}" x2="{X(DD):.1f}" y2="{av:.1f}" stroke="{AMBER}" stroke-width="3"/>')
A(f'<text class="m it" x="{X(DD)+12:.1f}" y="{(pv+av)/2+4:.1f}" font-size="10.5" fill="{AMBER}">'
  f'SCOSTAMENTO −{planned[DD]-actual[-1]:.1f} pt</text>')
A(f'<text class="m en" x="{X(DD)+12:.1f}" y="{(pv+av)/2+4:.1f}" font-size="10.5" fill="{AMBER}">'
  f'VARIANCE −{planned[DD]-actual[-1]:.1f} pts</text>')

# ---------------------------------------------------------------- legend
lx, ly = L, VH - 14
def leg(dx, swatch, it, en):
    A(swatch.replace('@X', f'{lx+dx:.0f}').replace('@Y', f'{ly-8:.0f}'))
    A(f'<text class="m it" x="{lx+dx+24}" y="{ly-1}" font-size="9.5" fill="{STEEL}">{it}</text>')
    A(f'<text class="m en" x="{lx+dx+24}" y="{ly-1}" font-size="9.5" fill="{STEEL}">{en}</text>')

leg(0,   f'<rect x="@X" y="@Y" width="17" height="8" fill="{NAVY}"/>',                       'PERCORSO CRITICO', 'CRITICAL PATH')
leg(180, f'<rect x="@X" y="@Y" width="17" height="8" fill="{BLUE}" fill-opacity=".55"/>',    'CON MARGINE', 'WITH FLOAT')
leg(330, f'<rect x="@X" y="@Y" width="17" height="8" fill="url(#wxh)" stroke="{AMBER}"/>',   'CONTINGENZA METEO', 'WEATHER CONTINGENCY')
leg(540, f'<path d="M@X,@Y l7,4 l-7,4 l-7,-4 Z" transform="translate(7,0)" fill="{TEAL}"/>', 'MILESTONE', 'MILESTONE')
leg(680, f'<line x1="@X" y1="@Y" x2="{lx+697}" y2="@Y" stroke="{STEEL}" stroke-dasharray="3 3"/>', 'MARGINE LIBERO', 'FREE FLOAT')
leg(850, f'<line x1="@X" y1="@Y" x2="{lx+867}" y2="@Y" stroke="{BLUE}" stroke-width="2" stroke-dasharray="5 3"/>', 'PIANIFICATO', 'PLANNED')
leg(990, f'<line x1="@X" y1="@Y" x2="{lx+1007}" y2="@Y" stroke="{NAVY}" stroke-width="2.4"/>', 'EFFETTIVO', 'ACTUAL')

A('</svg>')
svg = '\n'.join(o)
open('gantt.svg', 'w', encoding='utf-8').write(svg)
print('gantt.svg written: %d chars, %d elements' % (len(svg), len(o)))
