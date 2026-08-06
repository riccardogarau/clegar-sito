import json

# ============================================================ schedule data
# (id, name_it, name_en, duration weeks, [(pred, lag)], weight)
T = [
 ('tender',  'Preparazione gara',            'Tender preparation',        3, [],               4),
 ('bid',     'Valutazione offerte',          'Bid evaluation',            2, [('tender', 0)],  3),
 ('permit',  'Permessi e autorizzazioni',    'Permits and consents',      5, [('tender', 0)],  3),
 ('mobplan', 'Pianificazione mobilitazione', 'Mobilisation planning',     2, [('bid', 0)],     3),
 ('equip',   'Mobilitazione strumentazione', 'Equipment mobilisation',    2, [('mobplan', 0)], 5),
 ('acq',     'Acquisizione geofisica',       'Geophysical acquisition',   6, [('equip', 0), ('permit', 0)],  20),
 ('wx',      'Contingenza meteo',            'Weather contingency',       2, [('acq', 0)],     4),
 ('demob',   'Demobilitazione',              'Demobilisation',            1, [('wx', 0)],      3),
 ('proc',    'Data processing',              'Data processing',           5, [('acq', -3)],   12),
 ('interp',  'Interpretazione',              'Interpretation',            5, [('proc', 0)],   12),
 ('report',  'Reporting e chart',            'Reporting and charts',      4, [('interp', -1)],10),
 ('review',  'Revisione cliente',            'Client review',             2, [('report', 0)],  4),
]
IDX = {t[0]: i for i, t in enumerate(T)}
DUR = {t[0]: t[3] for t in T}
PRE = {t[0]: t[4] for t in T}

# ------------------------------------------------------------ forward pass
ES, EF = {}, {}
for tid in [t[0] for t in T]:
    es = 0
    for p, lag in PRE[tid]:
        es = max(es, EF[p] + lag)
    ES[tid], EF[tid] = es, es + DUR[tid]
END = max(EF.values())

# ----------------------------------------------------------- backward pass
succ = {t[0]: [] for t in T}
for tid in [t[0] for t in T]:
    for p, lag in PRE[tid]:
        succ[p].append((tid, lag))

LS, LF = {}, {}
for tid in [t[0] for t in T][::-1]:
    lf = END if not succ[tid] else min(LS[s] - lag for s, lag in succ[tid])
    LF[tid], LS[tid] = lf, lf - DUR[tid]

FLOAT = {t[0]: LS[t[0]] - ES[t[0]] for t in T}
CRIT = {k: v == 0 for k, v in FLOAT.items()}

print('project duration: %d weeks' % END)
print('%-9s %4s %4s %4s %4s %6s %s' % ('task','ES','EF','LS','LF','float','critical'))
for t in T:
    k = t[0]
    print('%-9s %4d %4d %4d %4d %6d %s' % (k, ES[k], EF[k], LS[k], LF[k], FLOAT[k], CRIT[k]))
print('\ncritical path:', ' -> '.join(k for k in [t[0] for t in T] if CRIT[k]))

# ------------------------------------------------------------- S-curve
DATA_DATE = 16
weekly = [0.0] * (END + 1)
for t in T:
    k, w = t[0], t[5]
    for wk in range(ES[k], EF[k]):
        weekly[wk] += w / DUR[k]
total = sum(weekly)
planned, c = [], 0.0
for wk in range(END + 1):
    planned.append(100 * c / total)
    c += weekly[wk]
planned.append(100.0)

# actual: tracks planned then slips slightly, reported only to the data date
actual = []
for wk in range(DATA_DATE + 1):
    slip = 0.0 if wk < 8 else min(0.16, 0.020 * (wk - 8))
    actual.append(planned[wk] * (1 - slip))

print('\nplanned at data date W%d: %.1f%%  |  actual: %.1f%%  |  variance %.1f pts'
      % (DATA_DATE, planned[DATA_DATE], actual[-1], actual[-1] - planned[DATA_DATE]))

json.dump({'T': T, 'ES': ES, 'EF': EF, 'LS': LS, 'LF': LF, 'FLOAT': FLOAT,
           'CRIT': CRIT, 'END': END, 'planned': planned, 'actual': actual,
           'DATA_DATE': DATA_DATE}, open('sched.json', 'w'))
