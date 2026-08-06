import numpy as np
from scipy.ndimage import gaussian_filter, gaussian_filter1d
from PIL import Image

rng = np.random.default_rng(7)

NX, NZ = 2000, 915          # traces, samples (TWT)
SURF   = 95                 # sea-surface sample (air above it)

x = np.arange(NX)

# ---------------------------------------------------------------- horizons
def wob(scale, amp, seed):
    """smooth band-limited lateral wobble"""
    r = np.random.default_rng(seed).normal(0, 1, NX)
    return gaussian_filter1d(r, scale) * amp / (gaussian_filter1d(r, scale).std() + 1e-9)

seabed = SURF + 132 + wob(160, 26, 1) + wob(45, 7, 2) + wob(12, 1.6, 3)

# unit thicknesses vary laterally
h1 = seabed + 46 + wob(200, 14, 11) + wob(50, 4, 12)
h2 = h1     + 78 + wob(240, 22, 21) + wob(60, 6, 22)
h3 = h2     + 96 + wob(300, 26, 31)
h4 = h3     + 88 + wob(280, 20, 41)

# ---- palaeo-channel incised into h2 (fills the unit above it) -------------
cx, cw, cdep = 1230, 190, 78
u = (x - cx) / cw
chan = np.exp(-(u ** 2) * 2.2) * cdep
chan[np.abs(u) > 1.35] = 0.0
chan = gaussian_filter1d(chan, 5)
h2c = h2 + chan                       # channel base cuts down

# ---- normal fault offsetting the deeper section --------------------------
fx, throw = 640, 26
fmask = 1.0 / (1.0 + np.exp(-(x - fx) / 3.0))       # smooth step
h3f = h3 + throw * fmask
h4f = h4 + throw * 1.25 * fmask

R = np.zeros((NZ, NX), dtype=np.float32)

def emboss(hz, amp, rough=0.18, seed=0):
    """place a reflector, with lateral amplitude variation"""
    g = np.random.default_rng(seed)
    a = amp * (1.0 + rough * gaussian_filter1d(g.normal(0, 1, NX), 22) /
               (gaussian_filter1d(g.normal(0, 1, NX), 22).std() + 1e-9))
    iz = np.clip(np.round(hz).astype(int), 0, NZ - 1)
    R[iz, x] += a

emboss(seabed, 1.00, 0.10, 101)      # water bottom: strongest
emboss(h1,    -0.42, 0.30, 102)
emboss(h2c,    0.55, 0.28, 103)
emboss(h3f,   -0.34, 0.35, 104)
emboss(h4f,    0.40, 0.30, 105)

# ---- intra-unit thin bedding --------------------------------------------
zz = np.arange(NZ)[:, None]
def unit_fill(top, bot, amp, nbeds, seed, chaotic=False):
    g = np.random.default_rng(seed)
    for k in range(nbeds):
        f = (k + 0.5) / nbeds
        if chaotic:
            lay = top + (bot - top) * f + wob(14, 9, seed + k) + g.normal(0, 2.0, NX)
        else:
            lay = top + (bot - top) * f + wob(180, 5, seed + k)
        iz = np.clip(np.round(lay).astype(int), 0, NZ - 1)
        R[iz, x] += g.normal(0, 1, NX) * amp * (0.5 + 0.5 * g.random())

unit_fill(seabed, h1,  0.10, 11, 201)                     # soft recent muds
unit_fill(h1,     h2c, 0.16, 15, 202)                     # bedded sands
unit_fill(h2c,    h3f, 0.13, 17, 203)
unit_fill(h3f,    h4f, 0.11, 14, 204)
unit_fill(h4f,    h4f + 150, 0.09, 16, 205)

# chaotic channel fill sitting on top of the incision
mask_ch = chan > 1.0
if mask_ch.any():
    g = np.random.default_rng(303)
    for k in range(9):
        f = (k + 0.5) / 9
        lay = h2 + chan * f + g.normal(0, 2.2, NX)
        iz = np.clip(np.round(lay).astype(int), 0, NZ - 1)
        amp = g.normal(0, 1, NX) * 0.20 * mask_ch
        R[iz, x] += amp

# ---- point diffractors (boulders / channel shoulders) --------------------
def diffraction(x0, z0, amp, v=3.0):
    dx = (x - x0).astype(np.float32)
    t = np.sqrt(z0 ** 2 + (dx / v) ** 2)
    keep = (t < NZ - 1) & (np.abs(dx) < 260)
    iz = np.round(t[keep]).astype(int)
    fall = amp * np.exp(-np.abs(dx[keep]) / 130.0)
    R[iz, x[keep]] += fall

for x0, dz, a in [(1140, 6, .34), (1325, 6, .34), (455, 34, .26),
                  (1690, 22, .22), (905, 12, .20)]:
    diffraction(x0, seabed[x0] + dz, a)

# ---- water-bottom multiple ----------------------------------------------
mult = np.clip(np.round(2 * seabed - 8).astype(int), 0, NZ - 1)
R[mult, x] += -0.30
mult2 = np.clip(np.round(3 * seabed - 16).astype(int), 0, NZ - 1)
R[mult2, x] += 0.13

# water column: quiet
for i in range(NX):
    R[: int(seabed[i]) - 3, i] *= 0.02
R[SURF:SURF+2, :] += 0.16     # sea-surface reflection (faint)
R[:SURF - 2, :] = 0.0         # air: no data above the surface

# ---------------------------------------------------------------- wavelet
def ricker(n, f):
    t = np.arange(-n // 2, n // 2 + 1)
    a = (np.pi * f * t) ** 2
    return (1 - 2 * a) * np.exp(-a)

w = ricker(61, 0.085)
w /= np.abs(w).max()

S = np.apply_along_axis(lambda tr: np.convolve(tr, w, mode='same'), 0, R)

# ---- attenuation, then AGC (as a real display would be gained) ----------
S *= np.exp(-zz / 900.0)
noise = gaussian_filter(rng.normal(0, 1, (NZ, NX)), (1.1, 0.7))
S += noise * (0.012 + 0.055 * (zz / NZ) ** 1.7)

win = 90
env = np.sqrt(gaussian_filter1d(S ** 2, win, axis=0) + 1e-8)
S = S / (env + 0.35 * env.mean())
S = gaussian_filter(S, (0.5, 0.6))

clip = np.percentile(np.abs(S), 99.0)
S = np.clip(S / clip, -1, 1)

S[:SURF - 3, :] = 0.0                       # air is empty
S[SURF + 3:, :] *= 1.0
np.save('seis.npy', S.astype(np.float32))
np.save('seis_h.npy', np.vstack([seabed, h1, h2c, h3f, h4f]).astype(np.float32))
np.save('seis_meta.npy', np.array([SURF, NZ, NX]))
print('seismic model ready', S.shape, 'rms', float(S.std()))
