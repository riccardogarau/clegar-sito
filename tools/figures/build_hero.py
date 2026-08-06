import numpy as np, json, os, base64
from PIL import Image

S = np.load('seis.npy'); H = np.load('seis_h.npy')
SURF, NZ, NX = [int(v) for v in np.load('seis_meta.npy')]

VW = 1800.0
VH = round(VW * NZ / NX)                     # keep the true aspect
sx, sy = VW / NX, VH / NZ
print('viewBox %d x %d  (surface y=%.1f)' % (VW, VH, SURF * sy))

# ------------------------------------------------------------- raster
def ramp(stops, n=1024):
    out = np.zeros((n, 3)); pos = np.array([s[0] for s in stops], float)
    cols = np.array([s[1] for s in stops], float); t = np.linspace(0, 1, n)
    for c in range(3):
        out[:, c] = np.interp(t, pos, cols[:, c])
    return out

VD = ramp([(0.00, (255, 255, 255)), (0.30, (236, 242, 247)), (0.55, (120, 170, 205)),
           (0.78, (36, 96, 150)), (1.00, (6, 22, 44))])
v = np.clip(np.abs(S) ** 0.82, 0, 1)
im = Image.fromarray(VD[(v * (len(VD) - 1)).astype(int)].astype(np.uint8))
im = im.resize((int(VW), int(VH)), Image.LANCZOS)
im.convert('RGB').save('assets/seismic.webp', quality=70, method=6)
print('seismic.webp', os.path.getsize('assets/seismic.webp') // 1024, 'KB')

# ------------------------------------------------------- geometry helpers
STEP = 12
xs = np.arange(0, NX, STEP)

def poly(row):
    return [(x * sx, H[row, x] * sy) for x in xs]

def d_of(pts):
    return 'M' + ' L'.join(f'{a:.1f},{b:.1f}' for a, b in pts)

picks = {k: d_of(poly(i)) for i, k in enumerate(['seabed', 'h1', 'h2', 'h3', 'h4'])}

# sea surface: gentle swell
SY = SURF * sy
surf_pts = [(x, SY + 1.6 * np.sin(x / 46.0) + 0.9 * np.sin(x / 17.0 + 1.1))
            for x in np.arange(0, VW + 1, 9)]
surf_d = d_of(surf_pts)

# water body = surface line, then back along the seabed
seabed_pts = poly(0)
water_d = (surf_d + ' L' +
           ' L'.join(f'{a:.1f},{b:.1f}' for a, b in reversed(seabed_pts)) + ' Z')

# ------------------------------------------------------ feature anchors
fault_x = 640 * sx
fault_y = H[3, 640] * sy
ch_lo, ch_hi = (1230 - 256) * sx, (1230 + 256) * sx
ch_top = (H[2, 1230] - 78) * sy
mult_x = 380 * sx
mult_y = (2 * H[0, 380] - 8) * sy
print('fault (%.0f,%.0f) | channel %.0f-%.0f top %.0f | multiple (%.0f,%.0f)'
      % (fault_x, fault_y, ch_lo, ch_hi, ch_top, mult_x, mult_y))

# ---------------------------------------------------------------- vessel
# drawn with the waterline at local y=0, bow to starboard (+x), ~104 long
VESSEL = '''
        <g class="hull">
          <!-- A-frame over the stern -->
          <path d="M-56,-13 L-48,-42 L-34,-42 L-41,-13" fill="none" stroke="#0B2545" stroke-width="3"/>
          <!-- deck crane -->
          <path d="M-21,-14 L-21,-33 L-3,-29" fill="none" stroke="#0B2545" stroke-width="2.6"/>
          <!-- hull: raked bow, transom stern -->
          <path d="M-58,-13 L58,-14 L64,-2 L56,8 L-46,8 L-58,-1 Z" fill="#0B2545"/>
          <!-- superstructure -->
          <path d="M6,-14 L40,-14 L40,-30 L10,-30 Z" fill="#F5F9FC" stroke="#0B2545" stroke-width="2.2"/>
          <path d="M16,-30 L34,-30 L34,-39 L18,-39 Z" fill="#F5F9FC" stroke="#0B2545" stroke-width="2.2"/>
          <!-- funnel -->
          <path d="M-14,-14 L-5,-14 L-6,-28 L-13,-28 Z" fill="#0B2545"/>
          <!-- mast -->
          <path d="M26,-39 L26,-54 M19,-49 L33,-49" stroke="#0B2545" stroke-width="2.3"/>
        </g>
        <!-- tow cable to the source, streaming aft -->
        <path d="M-57,-6 C-84,3 -106,11 -128,24" fill="none" stroke="#0B2545"
              stroke-width="1.6" stroke-opacity=".8"/>
        <ellipse cx="-132" cy="26" rx="10" ry="4.8" fill="#0B2545"/>'''

hero = f'''<figure class="profile">
        <div class="datafig">
          <img src="__SEIS__" alt="Ultra-high resolution seismic section" width="{int(VW)}" height="{int(VH)}">
          <svg class="ov" viewBox="0 0 {int(VW)} {int(VH)}" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <defs>
              <linearGradient id="wcol" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#3B87BE" stop-opacity=".20"/>
                <stop offset="100%" stop-color="#3B87BE" stop-opacity=".07"/>
              </linearGradient>
              <linearGradient id="trail" x1="0" y1="0" x2="1" y2="0">
                <stop offset="0%" stop-color="#31D6E2" stop-opacity="0"/>
                <stop offset="100%" stop-color="#31D6E2" stop-opacity=".26"/>
              </linearGradient>
            </defs>

            <!-- water body: sea surface down to the seabed -->
            <path d="{water_d}" fill="url(#wcol)"/>
            <path d="{surf_d}" fill="none" stroke="#2E7BB0" stroke-width="2" stroke-opacity=".85"/>

            <!-- interpreted horizons -->
            <path class="pick" d="{picks['seabed']}" stroke="#FFFFFF" stroke-width="2.8" stroke-opacity=".95"/>
            <path class="pick" d="{picks['h1']}" stroke="#31D6E2" stroke-width="2.0" stroke-opacity=".92"/>
            <path class="pick" d="{picks['h2']}" stroke="#F2A93B" stroke-width="2.0" stroke-opacity=".92"/>
            <path class="pick" d="{picks['h3']}" stroke="#B9CBDD" stroke-width="1.8" stroke-opacity=".92"/>
            <path class="pick" d="{picks['h4']}" stroke="#8FA6BC" stroke-width="1.6" stroke-opacity=".92"/>

            <!-- normal fault -->
            <path d="M{fault_x:.0f},{fault_y:.0f} L{fault_x+16:.0f},{VH}" stroke="#FF6F61"
                  stroke-width="1.8" stroke-dasharray="8 6" stroke-opacity=".9"/>
            <text class="olab it" x="{fault_x+26:.0f}" y="{fault_y+42:.0f}" fill="#FF6F61">FAGLIA · RIGETTO 0,9 m</text>
            <text class="olab en" x="{fault_x+26:.0f}" y="{fault_y+42:.0f}" fill="#FF6F61">FAULT · 0.9 m THROW</text>

            <!-- palaeo-channel -->
            <path d="M{ch_lo:.0f},{ch_top-6:.0f} L{ch_lo:.0f},{ch_top-22:.0f} L{ch_hi:.0f},{ch_top-22:.0f} L{ch_hi:.0f},{ch_top-6:.0f}"
                  fill="none" stroke="#F2A93B" stroke-width="1.8" stroke-opacity=".9"/>
            <text class="olab" x="{(ch_lo+ch_hi)/2:.0f}" y="{ch_top-32:.0f}" fill="#F2A93B" text-anchor="middle">PALAEO-CHANNEL</text>

            <!-- water-bottom multiple -->
            <path d="M{mult_x:.0f},{mult_y:.0f} L{mult_x+44:.0f},{mult_y-30:.0f}" stroke="#B9CBDD" stroke-width="1.5"/>
            <text class="olab it" x="{mult_x+51:.0f}" y="{mult_y-34:.0f}" fill="#B9CBDD">MULTIPLO DEL FONDALE</text>
            <text class="olab en" x="{mult_x+51:.0f}" y="{mult_y-34:.0f}" fill="#B9CBDD">SEABED MULTIPLE</text>

            <!-- live acquisition: vessel on the surface, source towed astern -->
            <g class="sweep">
              <rect x="-312" y="{SY:.0f}" width="180" height="{VH-SY:.0f}" fill="url(#trail)"/>
              <line x1="-132" y1="{SY+26:.0f}" x2="-132" y2="{VH}" stroke="#31D6E2" stroke-width="1.6" stroke-opacity=".8"/>
              <g transform="translate(0,{SY:.1f})"><g class="ship">{VESSEL}
              </g></g>
            </g>
          </svg>
        </div>
        <div class="legend">
          <span><i style="border-color:#0B2545"></i><span class="it">Fig. 01 — Sezione UHRS interpretata</span><span class="en">Fig. 01 — Interpreted UHRS section</span></span>
          <span><i style="border-color:#2E7BB0"></i><span class="it">Superficie del mare</span><span class="en">Sea surface</span></span>
          <span><i style="border-color:#9AA7B4"></i>Seabed</span>
          <span><i style="border-color:#31D6E2"></i>H1</span>
          <span><i style="border-color:#F2A93B"></i>H2</span>
          <span><i style="border-color:#B9CBDD"></i>H3 / H4</span>
          <span class="it">Dataset dimostrativo</span><span class="en">Illustrative dataset</span>
        </div>
      </figure>'''

open('hero_block.html', 'w', encoding='utf-8').write(hero)
json.dump({'VW': VW, 'VH': VH, 'SY': SY}, open('hero_meta.json', 'w'))
print('hero block written, %d chars' % len(hero))
