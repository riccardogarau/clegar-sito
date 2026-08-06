import numpy as np
from scipy.ndimage import gaussian_filter, rotate
from PIL import Image

# ============================================================ helpers
def fractal(shape, beta=2.3, seed=0):
    """1/f^beta noise via FFT filtering — natural-looking terrain roughness"""
    g = np.random.default_rng(seed)
    ny, nx = shape
    w = g.normal(0, 1, shape)
    F = np.fft.fftshift(np.fft.fft2(w))
    fy = np.fft.fftshift(np.fft.fftfreq(ny))[:, None]
    fx = np.fft.fftshift(np.fft.fftfreq(nx))[None, :]
    r = np.sqrt(fy ** 2 + fx ** 2)
    r[r == 0] = 1e-6
    F /= r ** beta
    out = np.real(np.fft.ifft2(np.fft.ifftshift(F)))
    return (out - out.mean()) / (out.std() + 1e-9)

def detrend(a, sigma=150):
    """strip the very-long-wavelength component so the mosaic reads evenly"""
    d = a - gaussian_filter(a, sigma)
    return d / (d.std() + 1e-9)

def ramp(stops, n=1024):
    out = np.zeros((n, 3))
    pos = np.array([s[0] for s in stops], dtype=float)
    cols = np.array([s[1] for s in stops], dtype=float)
    t = np.linspace(0, 1, n)
    for c in range(3):
        out[:, c] = np.interp(t, pos, cols[:, c])
    return out

def hillshade(z, az=315.0, alt=45.0, ve=1.0):
    dy, dx = np.gradient(z * ve)
    slope = np.pi / 2 - np.arctan(np.hypot(dx, dy))
    aspect = np.arctan2(-dx, dy)
    a, z0 = np.radians(az), np.radians(alt)
    hs = (np.sin(z0) * np.sin(slope) +
          np.cos(z0) * np.cos(slope) * np.cos(a - aspect))
    return np.clip(hs, 0, 1)

# ============================================================ BATHYMETRY
NY, NX = 1080, 1720
yy, xx = np.mgrid[0:NY, 0:NX]

# regional depth trend: deepening to the SW
z = 24.0 + 0.0082 * (NX - xx) + 0.0045 * yy

# broad seabed relief
z += fractal((NY, NX), 2.55, 1) * 3.1
z += fractal((NY, NX), 1.85, 2) * 0.55

# --- sand-wave field over the shallower NE half -------------------------
th = np.radians(24.0)
s = xx * np.cos(th) + yy * np.sin(th)
lam = 46 + 14 * gaussian_filter(np.random.default_rng(5).normal(0, 1, (NY, NX)), 80)
sw = np.sin(2 * np.pi * s / lam)
sw = np.sign(sw) * np.abs(sw) ** 0.65                # asymmetric crests
field = np.clip((xx - 620) / 520.0, 0, 1) * np.clip((yy - 120) / 260.0, 0, 1)
field *= np.clip((980 - yy) / 260.0, 0, 1)
z -= sw * 0.85 * gaussian_filter(field, 30)

# --- meandering palaeo-channel ------------------------------------------
cy = 620 + 130 * np.sin(xx[0] / 260.0) + 55 * np.sin(xx[0] / 95.0 + 1.2)
dist = np.abs(yy - cy[None, :])
half = 88 + 26 * np.sin(xx[0] / 180.0)[None, :]
prof = np.clip(1 - (dist / half) ** 2, 0, 1)
z += prof ** 0.75 * 7.4                               # channel is deeper

# --- pockmarks -----------------------------------------------------------
g = np.random.default_rng(9)
for _ in range(26):
    px, py = g.integers(120, NX - 120), g.integers(90, NY - 90)
    if prof[py, px] > 0.25:      # pockmarks cluster off-channel
        continue
    r = g.uniform(11, 27)
    d = np.hypot(xx - px, yy - py)
    z += np.exp(-(d / r) ** 2) * g.uniform(0.7, 1.9)

# --- boulder field near the outcrop -------------------------------------
for _ in range(90):
    px, py = g.integers(1180, NX - 60), g.integers(700, NY - 60)
    r = g.uniform(2.4, 5.5)
    d = np.hypot(xx - px, yy - py)
    z -= np.exp(-(d / r) ** 2) * g.uniform(0.5, 1.4)

z = gaussian_filter(z, 0.7)
np.save('bathy.npy', z.astype(np.float32))

# --- render: colour ramp + hillshade ------------------------------------
BATH = ramp([(0.00, (10, 26, 52)), (0.18, (18, 52, 100)), (0.38, (38, 104, 164)),
             (0.58, (62, 150, 190)), (0.76, (108, 196, 202)), (0.90, (186, 226, 214)),
             (1.00, (238, 244, 236))])

zn = (z.max() - z) / (z.max() - z.min())              # shallow = high value
idx = (np.clip(zn, 0, 1) * (len(BATH) - 1)).astype(int)
rgb = BATH[idx] / 255.0

hs = hillshade(-z, az=315, alt=40, ve=10.0)[..., None]
rgb = np.clip(rgb * (0.42 + 0.78 * hs), 0, 1)

# subtle depth contours every 2 m
cont = np.abs((z / 2.0) - np.round(z / 2.0))
cmask = np.clip(1 - cont / 0.055, 0, 1) ** 2
rgb = np.clip(rgb * (1 - 0.30 * cmask[..., None]) + 0.30 * cmask[..., None] * 0.92, 0, 1)

Image.fromarray((rgb * 255).astype(np.uint8)).save('bathy.png')
print('bathymetry', z.shape, 'depth range %.1f–%.1f m' % (z.min(), z.max()))

# ============================================================ SIDESCAN
SY, SX = 900, 1720
sy, sx = np.mgrid[0:SY, 0:SX]
cxm = SX / 2.0
across = np.abs(sx - cxm) / cxm                      # 0 at nadir, 1 at outer range

b = 0.50 + 0.20 * detrend(fractal((SY, SX), 2.15, 21), 120)        # sediment backscatter

# --- facies: coarse/rocky patch, muddy basin ----------------------------
patch = detrend(gaussian_filter(fractal((SY, SX), 2.35, 22), 11), 130)
rocky = np.clip((patch - 0.85) * 1.15, 0, 1)
b += rocky * 0.24 + fractal((SY, SX), 1.3, 23) * rocky * 0.16
muddy = np.clip((-patch - 0.85) * 1.10, 0, 1)
b -= muddy * 0.13

# --- ripple field --------------------------------------------------------
thr = np.radians(-16.0)
sr = sx * np.cos(thr) + sy * np.sin(thr)
rip = np.sin(2 * np.pi * sr / 21.0)
rmask = gaussian_filter(np.clip(detrend(fractal((SY, SX), 2.6, 24), 140), 0, 1), 18)
b += rip * 0.17 * rmask * (1 - rocky)

# --- buried cable: linear feature with a thin bright/dark pair ----------
cl = 300 + 46 * np.sin(sx[0] / 300.0)
dl = sy - cl[None, :]
b += np.exp(-((dl - 2) / 3.0) ** 2) * 0.30
b -= np.exp(-((dl + 3) / 3.5) ** 2) * 0.22

# --- targets: bright return + acoustic shadow away from nadir -----------
gt = np.random.default_rng(33)
targets = [(430, 250, 9), (1190, 615, 12), (860, 720, 7),
           (1450, 380, 8), (640, 560, 6), (1330, 200, 6)]
for tx, ty, r in targets:
    d = np.hypot(sx - tx, sy - ty)
    b += np.exp(-(d / r) ** 2) * 0.75
    sh_len = r * (2.6 + 5.0 * abs(tx - cxm) / cxm)
    direc = 1 if tx > cxm else -1
    dd = (sx - tx) * direc
    shadow = (dd > r * 0.7) & (dd < sh_len) & (np.abs(sy - ty) < r * 1.25)
    b[shadow] -= 0.55

# --- nadir gap + across-track gain residual ------------------------------
b *= (0.60 + 0.55 * np.exp(-((across - 0.42) ** 2) / 0.16))
nad = np.exp(-((sx - cxm) / 16.0) ** 2)
b = b * (1 - nad) + nad * 0.94                        # bright water-column line
b -= np.exp(-((np.abs(sx - cxm) - 30) / 12.0) ** 2) * 0.35

b += np.random.default_rng(44).normal(0, 0.035, (SY, SX))
b = gaussian_filter(b, 0.6)
b = np.clip((b - np.percentile(b, 1)) / (np.percentile(b, 99) - np.percentile(b, 1)), 0, 1)

SS = ramp([(0.0, (12, 16, 22)), (0.30, (62, 70, 78)), (0.62, (150, 158, 162)),
           (0.85, (214, 219, 221)), (1.0, (250, 251, 252))])
idx = (b * (len(SS) - 1)).astype(int)
Image.fromarray(SS[idx].astype(np.uint8)).save('sss.png')
print('sidescan', b.shape)
