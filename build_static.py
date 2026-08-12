import os, re, json, base64, shutil
from urllib.parse import quote
from lxml import html as LH, etree

SRC   = 'content/site2.html'
OUT   = 'docs'
DOMAIN = 'https://www.clegar.it'

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT + '/assets', exist_ok=True)

raw = open(SRC, encoding='utf-8').read()

# ══════════════════════════════════════════════ 1. externalise the assets
tok2file = {
    '__SEIS__':       ('assets/seismic.webp', 'assets/seismic.webp'),
    '__BATHY__':      ('assets/bathy.webp',   'assets/bathy.webp'),
    '__WORD_COLOR__': ('assets/logo-positive.png', 'assets/logo.png'),
    '__WORD_WHITE__': ('assets/logo-reversed.png', 'assets/logo-white.png'),
    '__MARK_B64__':   ('assets/mk_s.png',     'assets/mark.png'),
}
for tok, (src_path, dest) in tok2file.items():
    shutil.copy(src_path, f'{OUT}/{dest}')
    raw = raw.replace(tok, '{{ROOT}}' + dest)

MOBILE_CSS = r'''
/* ============================================================
   MOBILE
   Figures fit the screen. Dense charts would render their labels
   at 2-4px at that size, so tapping one opens it full-screen
   where it can be read and panned.
   ============================================================ */
figure{margin-inline:0}          /* browsers default to 40px each side */
.fig-hint{
  display:none;align-items:center;gap:.45rem;margin-top:.7rem;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--steel);
}
.fig-hint::before{content:"";width:14px;height:1px;background:var(--steel)}
@media(max-width:900px){
  .svc-fig{padding:.9rem;cursor:zoom-in}
  .profile .datafig{cursor:zoom-in}
  .fig-hint{display:flex}
}

/* full-screen figure viewer */
.figmodal{
  position:fixed;inset:0;z-index:1000;background:rgba(11,37,69,.97);
  display:none;flex-direction:column;
}
.figmodal.open{display:flex}
.figmodal-bar{
  display:flex;justify-content:space-between;align-items:center;gap:1rem;
  padding:.85rem 1.1rem;border-bottom:1px solid rgba(255,255,255,.16);flex:none;
}
.figmodal-bar span{
  font-family:var(--mono);font-size:.6rem;letter-spacing:.12em;
  text-transform:uppercase;color:rgba(220,231,241,.72);
}
.figmodal-close{
  background:none;border:1px solid rgba(220,231,241,.4);color:#DCE7F1;
  font-family:var(--mono);font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;
  padding:.6rem 1rem;cursor:pointer;min-height:44px;
}
.figmodal-body{
  flex:1;overflow:auto;-webkit-overflow-scrolling:touch;
  padding:1rem;background:var(--paper-2);
}
.figmodal-body > *{min-width:1180px;display:block}
.figmodal-body .datafig{min-width:1180px}
.figmodal-body .datafig img,.figmodal-body .datafig .ov{min-width:1180px}

@media(max-width:640px){
  :root{--pad:1.1rem}
  body{font-size:1rem;line-height:1.68}
  h1{font-size:clamp(2rem,8.5vw,2.6rem);letter-spacing:-.02em}
  h2{font-size:clamp(1.5rem,6.2vw,1.95rem)}
  .lede{font-size:1.05rem;line-height:1.58}
  .band-pad{padding-block:2.6rem}
  .band{padding:1.6rem 0 2.4rem}
  .hero-grid{padding-top:2.2rem}
  .hero-cta{gap:.6rem}
  .cta-solid,.cta-ghost,.btn-contact{
    padding:.95rem 1.15rem;min-height:46px;display:inline-flex;
    align-items:center;justify-content:center;
  }
  .hero-cta .cta-solid,.hero-cta .cta-ghost{flex:1 1 100%}
  .card{padding:1.4rem 1.15rem}
  .flist li{grid-template-columns:1fr;gap:.35rem;padding:.95rem 0}
  .flist .k{padding-top:0}
  .trio{gap:1.7rem}
  .callout{margin:1.5rem 0;padding-left:1.05rem}
  .form{max-width:none}
  .field input,.field textarea,.field select{font-size:16px;padding:.85rem .9rem}
  .foot-inner{padding-bottom:1.6rem}
  .foot-mark{width:230px;right:-50px;bottom:-70px}
  .profile-caption,.legend{font-size:.58rem;gap:.3rem .9rem}
}

/* comfortable touch targets (>=44px) */
@media(pointer:coarse){
  .tab{padding-block:1.15rem}
  .langsw a{padding:.8rem .85rem}
  .brand{padding-block:.4rem}
  .foot-nav{gap:0}
  .foot-nav a{display:block;padding-block:.65rem;min-height:44px}
  .foot h5 + .foot-nav{margin-top:-.3rem}
  .contact-cols a{display:inline-block;padding-block:.5rem}
  .foot-top > div > p > a{display:inline-block;padding-block:.4rem}
}

/* nothing may push the page sideways */
html,body{max-width:100%;overflow-x:hidden}
.wrap,.hero-grid,.masthead-row,.foot-inner{overflow-wrap:break-word}
'''

# ══════════════════════════════════════════════ 2. lift CSS and JS out
css = re.search(r'<style>(.*?)</style>', raw, re.S).group(1)
raw = raw.replace(re.search(r'<style>.*?</style>', raw, re.S).group(0),
                  '<link rel="stylesheet" href="{{ROOT}}assets/style.css">')

# page-switching CSS is no longer needed: every page is a real document
css = css.replace('.page{display:none;animation:rise .5s cubic-bezier(.16,.84,.44,1) both}\n.page.is-active{display:block}',
                  '.page{animation:rise .5s cubic-bezier(.16,.84,.44,1) both}')
css = css.replace('html[data-lang="it"] .en,\nhtml[data-lang="en"] .it{display:none!important}', '')
css += """
/* --- crawlable navigation --- */
.tab{text-decoration:none;display:inline-block}
.tab[aria-current="page"]{color:var(--ink)}
.tab[aria-current="page"]::after{content:"";position:absolute;left:.95rem;right:.95rem;bottom:-1px;height:2px;background:var(--teal)}
.tab:first-child[aria-current="page"]::after{left:0}
.card,.foot-nav a{text-decoration:none;color:inherit}
.card{display:block}
.langsw a{
  font-family:var(--mono);font-size:.68rem;letter-spacing:.12em;
  background:none;border:0;color:var(--steel);padding:.5rem .62rem;text-decoration:none;transition:all .2s;
}
.langsw a:hover{color:var(--ink)}
.langsw a[aria-current="true"]{background:var(--ink);color:#fff}
.brand{text-decoration:none}

/* otto voci di menu: su desktop vanno compattate per stare nella riga */
@media(min-width:1001px){
  .tab{padding-left:.6rem;padding-right:.6rem;font-size:.72rem;letter-spacing:.07em}
  .tab[aria-current="page"]::after{left:.6rem;right:.6rem}
  .tab:first-child[aria-current="page"]::after{left:0}
}
@media(min-width:1001px) and (max-width:1120px){
  .tab{padding-left:.42rem;padding-right:.42rem;font-size:.665rem;letter-spacing:.045em}
  .tab[aria-current="page"]::after{left:.42rem;right:.42rem}
  .tab:first-child[aria-current="page"]::after{left:0}
}

/* ---------- Insights: indice e articoli ---------- */
.artlist{list-style:none;margin:2.2rem 0 0;padding:0}
.artlist li{border-top:1px solid var(--line);padding:1.6rem 0}
.artlist li:last-child{border-bottom:1px solid var(--line)}
.artlist time{
  font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;
  text-transform:uppercase;color:var(--teal);display:block;margin-bottom:.5rem;
}
.artlist h2{font-size:clamp(1.2rem,2.2vw,1.6rem);margin-bottom:.5rem}
.artlist a{text-decoration:none;color:inherit;display:block}
.artlist a:hover h2{color:var(--teal)}
.artlist p{font-size:.98rem;line-height:1.6;color:rgba(11,37,69,.72);margin:0;max-width:44rem}
.artlist .go{
  font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--steel);margin-top:.9rem;display:inline-block;
}
.artlist a:hover .go{color:var(--teal)}

.article{max-width:none}
.article > p,.article > h2,.article > h3,.article > ul,.article > .callout{max-width:44rem}
.article > figure{max-width:none;width:100%}
.article h2{font-size:clamp(1.3rem,2.4vw,1.75rem);margin:2.4rem 0 .9rem}
.article p{margin:0 0 1.15rem}
.article .flist{margin-top:1.2rem}
.article figure{margin:2.2rem 0}
.art-meta{
  font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--teal);margin-bottom:1rem;display:flex;gap:1rem;flex-wrap:wrap;align-items:center;
}
.art-back{
  font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--steel);text-decoration:none;display:inline-block;margin-top:2.4rem;
}
.art-back:hover{color:var(--teal)}
.article-wide{max-width:none}
.article-wide .svc-fig{max-width:none}

/* ---------- tabelle negli articoli ----------
   Le cifre sono in mono e allineate a destra: incolonnate si confrontano,
   in proporzionale no. Il contenitore scorre in orizzontale, perche' una
   tabella larga e' l'unico modo in cui questo sito puo' spingere la pagina
   di lato, e la regola e' che non succeda mai. */
.tablewrap{overflow-x:auto;margin:2rem 0;max-width:44rem;-webkit-overflow-scrolling:touch}
.article table{border-collapse:collapse;width:100%;min-width:32rem;font-size:.94rem}
.article th,.article td{
  text-align:left;padding:.7rem .9rem;border-bottom:1px solid var(--line);
  vertical-align:top;
}
.article thead th{
  font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--steel);font-weight:400;border-bottom:1px solid var(--ink);white-space:nowrap;
}
.article tbody tr:last-child td{border-bottom:1px solid var(--line)}
.article td.num,.article th.num{font-family:var(--mono);text-align:right;white-space:nowrap}
.article table caption{
  caption-side:bottom;text-align:left;padding-top:.8rem;
  font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--steel);line-height:1.7;
}

/* ---------- il numero che l'articolo mette in discussione ---------- */
.pull{
  margin:2.4rem 0;padding:1.6rem 0 1.6rem 1.6rem;border-left:2px solid var(--teal);
  max-width:44rem;
}
.pull strong{
  display:block;font-size:clamp(1.6rem,4vw,2.3rem);line-height:1.15;letter-spacing:-.01em;
}
.pull span{
  display:block;margin-top:.6rem;font-family:var(--mono);font-size:.64rem;
  letter-spacing:.12em;text-transform:uppercase;color:var(--steel);
}

/* ---------- condivisione in fondo all'articolo ---------- */
.share{
  display:flex;flex-wrap:wrap;align-items:center;gap:.6rem;max-width:44rem;
  margin-top:3rem;padding-top:1.5rem;border-top:1px solid var(--line);
}
.share-label{
  font-family:var(--mono);font-size:.64rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--steel);margin-right:.35rem;
}
.share-btn{
  font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--ink);text-decoration:none;background:none;cursor:pointer;
  border:1px solid var(--line);padding:0 .95rem;min-height:44px;
  display:inline-flex;align-items:center;transition:border-color .2s,color .2s;
}
.share-btn:hover,.share-btn:focus-visible{border-color:var(--teal);color:var(--teal)}
.share-btn[data-copied]{border-color:var(--teal);color:var(--teal)}
.share .art-back{margin-top:0}
""" + MOBILE_CSS
open(f'{OUT}/assets/style.css', 'w', encoding='utf-8').write(css)

js_block = re.search(r'<script>(.*?)</script>\s*</body>', raw, re.S).group(1)
raw = raw.replace(re.search(r'<script>.*?</script>\s*</body>', raw, re.S).group(0),
                  '<script src="{{ROOT}}assets/site.js" defer></script>\n</body>')



# ══════════════════════════════════════════════ 3. page definitions
PAGES = [
    # key,        it slug,                    en slug
    ('home',       '',                          'en/'),
    ('geoscience', 'geoscienze-marine/',        'en/marine-geoscience/'),
    ('pm',         'project-management/',       'en/project-management/'),
    ('advisory',   'technical-advisory/',       'en/technical-advisory/'),
    ('owners',     'owners-engineering/',       'en/owners-engineering/'),
    ('excellence', 'operational-excellence/',   'en/operational-excellence/'),
    ('insights',   'insights/',                 'en/insights/'),
    ('contatti',   'contatti/',                 'en/contact/'),
    # fuori dal menu: raggiungibile dal footer, il menu resta a 8 voci
    ('privacy',    'privacy/',                  'en/privacy/'),
]
SLUG = {k: {'it': i, 'en': e} for k, i, e in PAGES}

NAV = [('home', 'Home', 'Home'),
       ('geoscience', 'Marine Geoscience', 'Marine Geoscience'),
       ('pm', 'Project Management', 'Project Management'),
       ('advisory', 'Technical Advisory', 'Technical Advisory'),
       ('owners', "Owner's Engineering", "Owner's Engineering"),
       ('excellence', 'Operational Excellence', 'Operational Excellence'),
       ('insights', 'Insights', 'Insights'),
       ('contatti', 'Contatti', 'Contact')]

META = {
 'home': {
   'it': ("Consulenza geofisica marina e offshore | CLEGAR",
          "Consulenza indipendente per progetti marini e offshore: indagini geofisiche, verifica dei dati, project management e rappresentanza del committente."),
   'en': ("Marine Geoscience & Offshore Advisory | CLEGAR",
          "Independent consultancy for marine and offshore projects: geophysical survey planning, data verification, project management and owner representation across Europe.")},
 'geoscience': {
   'it': ("Indagini geofisiche marine: pianificazione e QC | CLEGAR",
          "Pianificazione di indagini geofisiche marine, specifiche tecniche, controllo qualità secondo IHO S-44, processing e interpretazione di batimetria, sub-bottom e UHRS."),
   'en': ("Marine geophysical survey planning and QC | CLEGAR",
          "Marine geophysical survey planning, technical specifications, data QC against IHO S-44, processing and interpretation of bathymetry, side scan, sub-bottom and UHRS data.")},
 'pm': {
   'it': ("Project management per campagne offshore | CLEGAR",
          "Direzione di progetto e project controls per campagne geofisiche offshore: programma lavori, percorso critico, gestione interfacce, controllo costi e registro dei rischi."),
   'en': ("Project management for offshore campaigns | CLEGAR",
          "Project direction and project controls for offshore geophysical campaigns: schedule, critical path, interface management, cost control and a live risk register.")},
 'advisory': {
   'it': ("Due diligence e verifica indipendente dati | CLEGAR",
          "Revisioni tecniche, due diligence su dataset geofisici, oversight del contractor e verifica indipendente dei risultati per accettazioni, finanziamenti e gestione dei claim."),
   'en': ("Technical due diligence and independent verification | CLEGAR",
          "Technical reviews, due diligence on geophysical datasets, contractor oversight and independent verification of results for acceptance, financing and claim management.")},
 'owners': {
   'it': ("Owner's engineering e rappresentanza offshore | CLEGAR",
          "Rappresentanza del committente a bordo e in banchina: mobilitazione, witnessing di calibrazioni, supervisione delle operazioni e controllo di produzione e downtime."),
   'en': ("Owner's engineering and offshore client representation | CLEGAR",
          "Client representation on board and alongside: mobilisation, witnessing of calibrations, supervision of operations and control of production and downtime.")},
 'excellence': {
   'it': ("KPI e ottimizzazione delle operazioni marine | CLEGAR",
          "Definizione di KPI operativi, procedure e SOP, readiness review, analisi del tempo nave e lessons learned per ridurre downtime e costi nelle campagne marine."),
   'en': ("Operational KPIs and marine operations optimisation | CLEGAR",
          "Operational KPIs, procedures and SOPs, readiness reviews, vessel time analysis and lessons learned to reduce downtime and cost on marine campaigns.")},
 'insights': {
   'it': ("Insights: articoli tecnici su survey e offshore | CLEGAR",
          "Articoli tecnici su geoscienze marine, gestione di campagne offshore, verifica dei dati e rappresentanza del committente. Casi concreti, non teoria."),
   'en': ("Insights: technical articles on survey and offshore | CLEGAR",
          "Technical articles on marine geoscience, offshore campaign management, data verification and owner representation. Worked examples, not theory.")},
 'contatti': {
   'it': ("Contatti | CLEGAR",
          "Contattate CLEGAR per una campagna geofisica da impostare o un dataset da verificare. Rispondiamo entro due giorni lavorativi, in italiano o in inglese."),
   'en': ("Contact | CLEGAR",
          "Get in touch with CLEGAR about a geophysical campaign to set up or a dataset to verify. We reply within two working days, in English or Italian.")},
 'privacy': {
   'it': ("Informativa sulla privacy | CLEGAR",
          "Quali dati personali raccoglie www.clegar.it, con quale base giuridica, per quanto tempo li conserva e come esercitare i diritti previsti dal GDPR."),
   'en': ("Privacy notice | CLEGAR",
          "What personal data www.clegar.it collects, on what legal basis, how long they are kept and how to exercise the rights granted by the GDPR.")},
}

SERVICE_KEYS = ['geoscience', 'pm', 'advisory', 'owners', 'excellence']

# ══════════════════════════════════════════════ 4. parse and split
doc = LH.document_fromstring(raw)


def strip_lang(node, drop):
    for e in node.xpath(f'.//*[contains(concat(" ",normalize-space(@class)," ")," {drop} ")]'):
        par = e.getparent()
        if par is not None:
            if e.tail:
                prev = e.getprevious()
                if prev is not None:
                    prev.tail = (prev.tail or '') + e.tail
                else:
                    par.text = (par.text or '') + e.tail
            par.remove(e)


def tostr(node):
    return etree.tostring(node, encoding='unicode', method='html')


sections = {s.get('id')[5:]: s for s in doc.findall('.//section') if (s.get('id') or '').startswith('page-')}
head_tpl = doc.find('.//head')
foot_tpl = doc.find('.//footer')
mast_tpl = doc.find('.//header')


def rel_root(slug):
    depth = slug.count('/')
    return '../' * depth if depth else ''





GEO_REDIRECT = r'''<script>
/* Rilevamento lingua alla prima visita della home italiana.
   Nessuna richiesta di rete: usa il fuso orario e le lingue del browser,
   quindi nessun dato del visitatore lascia il dispositivo.
   Agisce solo su "/", una sola volta, e mai se l'utente ha gia scelto. */
(function () {
  try {
    var KEY = 'clegar_lang';
    var saved = localStorage.getItem(KEY);
    if (saved === 'it') return;                         // ha scelto italiano
    if (saved === 'en') { location.replace('en/'); return; }   // ha scelto inglese
    if (location.host && document.referrer &&
        document.referrer.indexOf(location.host) !== -1) return;  // navigazione interna
    if (location.search.indexOf('lang=') !== -1) return;          // forzatura esplicita

    var inItaly = false;
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || '';
      inItaly = (tz === 'Europe/Rome');
    } catch (e) {}

    if (!inItaly) {
      var langs = navigator.languages || [navigator.language || ''];
      for (var i = 0; i < langs.length; i++) {
        if (String(langs[i]).toLowerCase().indexOf('it') === 0) { inItaly = true; break; }
      }
    }
    if (!inItaly) location.replace('en/');
  } catch (e) {}
})();
</script>
'''



FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&'
         'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&'
         'family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')


def render_page(lang, slug, title, desc, alt_it, alt_en, ldjson, geo_redirect,
                masthead, nav, footer, body, og_type='website', og_image='assets/og.png'):
    root = rel_root(slug)
    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{DOMAIN}/{slug}">
<link rel="alternate" hreflang="it" href="{DOMAIN}/{alt_it}">
<link rel="alternate" hreflang="en" href="{DOMAIN}/{alt_en}">
<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{alt_it}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="CLEGAR">
<meta property="og:locale" content="{'it_IT' if lang == 'it' else 'en_GB'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{DOMAIN}/{slug}">
<meta property="og:image" content="{DOMAIN}/{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{DOMAIN}/{og_image}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0B2545">
<!-- Google Search Console: sostituire con il proprio codice di verifica -->
<!-- <meta name="google-site-verification" content="INCOLLA_QUI_IL_CODICE"> -->
<link rel="icon" href="{root}assets/mark.png">
<link rel="apple-touch-icon" href="{root}assets/mark.png">
{FONTS}
<link rel="stylesheet" href="{root}assets/style.css">
{ldjson}
{geo_redirect}
</head>
<body>
{masthead}
{nav}
<main id="main">
{body}
</main>
{footer}
<script src="{root}assets/site.js" defer></script>
</body>
</html>
"""
    return html.replace('{{ROOT}}', root).replace('{ga_block}', '')



def shell(lang, key, slug):
    """testata, navigazione e footer per una qualsiasi pagina del sito"""
    root = rel_root(slug)
    other = 'en' if lang == 'it' else 'it'

    mast = LH.fromstring(tostr(mast_tpl))
    strip_lang(mast, other)
    br = mast.find('.//button[@class="brand"]')
    br.tag = 'a'; br.set('href', root); br.attrib.pop('data-go', None)
    sw = mast.find('.//div[@class="langsw"]')
    for b in list(sw):
        sw.remove(b)
    for L in ('it', 'en'):
        a = etree.SubElement(sw, 'a')
        a.set('href', root + SLUG[key][L])
        if L == lang:
            a.set('aria-current', 'true')
        else:
            a.set('hreflang', L)
        a.text = L.upper()
    cb = mast.find('.//button[@class="btn-contact"]')
    cb.tag = 'a'; cb.set('href', root + SLUG['contatti'][lang]); cb.attrib.pop('data-go', None)

    items = []
    for k, it_l, en_l in NAV:
        lab = it_l if lang == 'it' else en_l
        cur = ' aria-current="page"' if k == key else ''
        items.append(f'<a class="tab" href="{root}{SLUG[k][lang]}"{cur}>{lab}</a>')
    nav = ('<nav class="tabbar" aria-label="'
           + ('Navigazione principale' if lang == 'it' else 'Main navigation')
           + '">\n  <div class="tabbar-inner">\n    ' + '\n    '.join(items) + '\n  </div>\n</nav>')

    ft = LH.fromstring(tostr(foot_tpl))
    strip_lang(ft, other)
    for b in ft.xpath('.//*[@data-go]'):
        t = b.get('data-go'); b.tag = 'a'
        b.set('href', root + SLUG[t][lang]); b.attrib.pop('data-go', None)

    return {'masthead': tostr(mast), 'nav': nav, 'footer': tostr(ft)}


def build(key, lang):
    slug = SLUG[key][lang]
    root = rel_root(slug)
    other = 'en' if lang == 'it' else 'it'
    title, desc = META[key][lang]

    # ---- content
    sec = LH.fromstring(tostr(sections[key]))
    strip_lang(sec, other)
    sec.attrib.pop('id', None)
    sec.attrib.pop('role', None)
    sec.set('class', 'page')
    # internal links: data-go buttons -> real anchors
    for b in sec.xpath('.//*[@data-go]'):
        tgt = b.get('data-go')
        b.tag = 'a'
        b.set('href', root + SLUG[tgt][lang])
        for a in ('data-go', 'type'):
            b.attrib.pop(a, None)
    # figures fit the screen; on small screens a tap opens them full-screen
    for fig in sec.findall('.//figure'):
        chart = None
        for ch in fig:
            if ch.tag == 'svg' or (ch.tag == 'div' and 'datafig' in (ch.get('class') or '')):
                chart = ch
                break
        if chart is None:
            continue
        fig.set('data-zoomable', '1')
        hint = etree.Element('p'); hint.set('class', 'fig-hint')
        hint.text = ('Tocca il grafico per ingrandirlo' if lang == 'it'
                     else 'Tap the chart to enlarge it')
        chart.addnext(hint)
    body = tostr(sec)

    _sh = shell(lang, key, slug)
    masthead, nav, footer = _sh['masthead'], _sh['nav'], _sh['footer']

    # ---- structured data
    org = {
        "@context": "https://schema.org", "@type": "ProfessionalService",
        "@id": DOMAIN + "/#organization", "name": "CLEGAR",
        "legalName": "CLEGAR S.r.l.", "vatID": "IT07422540828",
        "url": DOMAIN + "/", "email": "info@clegar.it",
        "logo": DOMAIN + "/assets/logo.png",
        "image": DOMAIN + "/assets/og.png",
        "description": META['home'][lang][1],
        "address": {"@type": "PostalAddress", "addressCountry": "IT"},
        "areaServed": [{"@type": "Place", "name": n} for n in
                       ["Italy", "Europe", "North Sea", "Mediterranean Sea"]],
        "knowsAbout": ["Marine geophysics", "Offshore wind site investigation",
                       "Submarine cable route survey", "Multibeam bathymetry",
                       "Sub-bottom profiling", "UHRS", "IHO S-44",
                       "Owner's engineering", "Technical due diligence"],
        "availableLanguage": ["it", "en"],
    }
    ld = [org]
    if key in SERVICE_KEYS:
        h1 = sec.find('.//h1')
        ld.append({
            "@context": "https://schema.org", "@type": "Service",
            "name": ' '.join((h1.text_content() or '').split()),
            "serviceType": ' '.join((h1.text_content() or '').split()),
            "description": desc,
            "provider": {"@id": DOMAIN + "/#organization"},
            "areaServed": {"@type": "Place", "name": "Europe"},
            "url": f"{DOMAIN}/{slug}",
        })
        ld.append({
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1,
                 "name": "Home" if lang == 'it' else "Home",
                 "item": f"{DOMAIN}/" + (SLUG['home'][lang])},
                {"@type": "ListItem", "position": 2,
                 "name": ' '.join((h1.text_content() or '').split()),
                 "item": f"{DOMAIN}/{slug}"}]})
    ldjson = '\n'.join(
        f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, separators=(",", ":"))}</script>'
        for x in ld)

    geo_redirect = GEO_REDIRECT if (key == 'home' and lang == 'it') else ''

    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&'
             'family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&'
             'family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">')

    html = render_page(lang=lang, slug=slug, title=title, desc=desc,
                       alt_it=SLUG[key]['it'], alt_en=SLUG[key]['en'],
                       ldjson=ldjson, geo_redirect=geo_redirect,
                       masthead=masthead, nav=nav, footer=footer, body=body,
                       og_type='website')
    path = f'{OUT}/{slug}index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)
    return slug



# ══════════════════════════════════════════ Insights: indice e articoli
from articles import ARTICLES, FIG_ORIGIN, FIG_LINES, FIG_TVU, FIG_MAP

FIG_SVG = {
    FIG_ORIGIN: ('content/fig_art_origin.svg',
                 ('Il cuneo si allunga con il ritardo e si ingrossa con il costo: '
                  'lo stesso errore, scoperto due fasi dopo, si paga il doppio. Esempi dimostrativi.',
                  'The wedge lengthens with the delay and thickens with the cost: '
                  'the same mistake, found two stages later, costs twice as much. Illustrative examples.')),
    FIG_LINES:  ('content/fig_art_lines.svg',
                 ('Chi fissa i criteri all’inizio è lo stesso che ne verifica il rispetto alla fine: '
                  'è lì che l’indipendenza conta.',
                  'The people who set the criteria at the start are the ones who verify them at the end: '
                  'that is where independence counts.')),
    FIG_TVU:    ('content/fig_art_tvu.svg',
                 ('√2 × TVU è il 41% più largo di TVU: la fascia grigia è la distanza fra il test '
                  'giusto e quello sbagliato. Scarti dell’esempio sintetico.',
                  '√2 × TVU is 41% wider than TVU: the grey band is the distance between the right '
                  'test and the wrong one. Failures from the synthetic example.')),
    FIG_MAP:    ('content/fig_art_map.svg',
                 ('Trentuno scarti sono il 2,5% del dataset, ma cadono dove passerà il cavo: '
                  'è lì che il numero di sintesi smette di bastare. Esempio sintetico.',
                  'Thirty-one failures are 2.5% of the dataset, but they fall where the cable will '
                  'run: that is where the headline number stops being enough. Synthetic example.')),
}


def article_slug(art, lang):
    base = SLUG['insights'][lang]
    return base + art['slug'][lang] + '/'


def month_name(iso, lang):
    y, m, d = iso.split('-')
    IT = ['gennaio','febbraio','marzo','aprile','maggio','giugno','luglio',
          'agosto','settembre','ottobre','novembre','dicembre']
    EN = ['January','February','March','April','May','June','July',
          'August','September','October','November','December']
    names = IT if lang == 'it' else EN
    return '%d %s %s' % (int(d), names[int(m) - 1], y)


def render_figures(html, lang):
    """sostituisce i segnaposto con le figure, avvolte come le altre del sito"""
    for token, (path, caps) in FIG_SVG.items():
        if token not in html:
            continue
        svg = open(path, encoding='utf-8').read().strip()
        cap = caps[0] if lang == 'it' else caps[1]
        hint = ('Tocca il grafico per ingrandirlo' if lang == 'it'
                else 'Tap the chart to enlarge it')
        fig = ('<figure class="svc-fig" data-zoomable="1">\n' + svg
               + '\n<p class="fig-hint">' + hint + '</p>'
               + '\n<figcaption class="fig-cap">' + cap + '</figcaption>\n</figure>')
        html = html.replace(token, fig)
    return html


def strip_other_lang_svg(html, lang):
    """le figure sono bilingui: rimuove i <text> dell'altra lingua"""
    drop = 'en' if lang == 'it' else 'it'
    return re.sub(r'<text class="' + drop + r'"[^>]*>.*?</text>', '', html, flags=re.S)


def build_article(art, lang):
    slug = article_slug(art, lang)
    root = rel_root(slug)
    title = art['meta_title'][lang]
    desc = art['desc'][lang]

    body_html = render_figures(art['body'][lang], lang)
    body_html = strip_other_lang_svg(body_html, lang)

    back = ('Tutti gli articoli' if lang == 'it' else 'All articles')
    head_block = (
        '<div class="art-meta"><time datetime="' + art['date'] + '">'
        + month_name(art['date'], lang) + '</time><span>Insights</span></div>')

    # Condivisione: link normali, nessuno script di terze parti. Il widget
    # ufficiale di LinkedIn carica un SDK che traccia il visitatore prima del
    # consenso, che l'informativa esclude. Un link non traccia nessuno finche'
    # non viene cliccato.
    url = DOMAIN + '/' + slug
    attr = lambda s: s.replace('&', '&amp;').replace('"', '&quot;')
    lab = {'it': ('Condividi', 'Copia link'), 'en': ('Share', 'Copy link')}[lang]
    share = (
        '<div class="share">'
        '<span class="share-label">' + lab[0] + '</span>'
        '<a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url='
        + quote(url, safe='') + '" target="_blank" rel="noopener">LinkedIn</a>'
        '<a class="share-btn" href="mailto:?subject=' + quote(art['title'][lang], safe='')
        + '&amp;body=' + quote(art['title'][lang] + '\n' + url, safe='') + '">Email</a>'
        '<button class="share-btn" type="button" data-share-url="' + attr(url)
        + '" data-share-title="' + attr(art['title'][lang]) + '">' + lab[1] + '</button>'
        '</div>')

    body = ('<section class="page">\n'
            '  <div class="svc-hero"><div class="wrap">\n'
            + head_block
            + '<h1>' + art['title'][lang] + '</h1>\n'
            '  </div></div>\n'
            '  <div class="band band-white band-pad"><div class="wrap">\n'
            '    <div class="article">' + body_html + '</div>\n'
            '    ' + share + '\n'
            '    <a class="art-back" href="' + root + SLUG['insights'][lang] + '">&larr; ' + back + '</a>\n'
            '  </div></div>\n'
            '</section>')

    ld = {
        "@context": "https://schema.org", "@type": "Article",
        "headline": art['title'][lang],
        "description": desc,
        "datePublished": art['date'],
        "dateModified": art['date'],
        "inLanguage": lang,
        "author": {"@type": "Organization", "name": "CLEGAR", "url": DOMAIN + "/"},
        "publisher": {"@id": DOMAIN + "/#organization"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": DOMAIN + "/" + slug},
        "image": DOMAIN + "/assets/og.png",
    }
    crumbs = {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home",
             "item": DOMAIN + "/" + SLUG['home'][lang]},
            {"@type": "ListItem", "position": 2, "name": "Insights",
             "item": DOMAIN + "/" + SLUG['insights'][lang]},
            {"@type": "ListItem", "position": 3, "name": art['title'][lang],
             "item": DOMAIN + "/" + slug}]}
    ldjson = '\n'.join(
        '<script type="application/ld+json">%s</script>'
        % json.dumps(x, ensure_ascii=False, separators=(",", ":")) for x in (ld, crumbs))

    html = render_page(lang=lang, slug=slug, title=title, desc=desc,
                       alt_it=article_slug(art, 'it'), alt_en=article_slug(art, 'en'),
                       ldjson=ldjson, geo_redirect='',
                       masthead=shell(lang, 'insights', slug)['masthead'],
                       nav=shell(lang, 'insights', slug)['nav'],
                       footer=shell(lang, 'insights', slug)['footer'],
                       body=body, og_type='article')
    path = f'{OUT}/{slug}index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)
    return slug


def build_insights_index(lang):
    slug = SLUG['insights'][lang]
    root = rel_root(slug)
    title, desc = META['insights'][lang]

    intro = ({'it': ('Articoli tecnici su geoscienze marine, gestione di campagne offshore e '
                     'verifica dei dati. Casi concreti e esempi lavorati, non teoria generale.'),
              'en': ('Technical articles on marine geoscience, offshore campaign management and '
                     'data verification. Worked examples, not general theory.')})[lang]
    read = 'Leggi' if lang == 'it' else 'Read'

    items = []
    for art in ARTICLES:
        items.append(
            '<li><a href="' + root + article_slug(art, lang) + '">'
            '<time datetime="' + art['date'] + '">' + month_name(art['date'], lang) + '</time>'
            '<h2>' + art['title'][lang] + '</h2>'
            '<p>' + art['abstract'][lang] + '</p>'
            '<span class="go">' + read + ' &rarr;</span></a></li>')

    body = ('<section class="page">\n'
            '  <div class="svc-hero"><div class="wrap">\n'
            '    <p class="eyebrow">Insights</p>\n'
            '    <h1>' + ('Note tecniche e casi di progetto' if lang == 'it'
                          else 'Technical notes and project cases') + '</h1>\n'
            '    <p class="lede">' + intro + '</p>\n'
            '  </div></div>\n'
            '  <div class="band band-white band-pad"><div class="wrap">\n'
            '    <ul class="artlist">' + '\n'.join(items) + '</ul>\n'
            '  </div></div>\n'
            '</section>')

    ld = {"@context": "https://schema.org", "@type": "CollectionPage",
          "name": "Insights", "description": desc,
          "url": DOMAIN + "/" + slug, "inLanguage": lang,
          "isPartOf": {"@id": DOMAIN + "/#organization"}}
    ldjson = ('<script type="application/ld+json">%s</script>'
              % json.dumps(ld, ensure_ascii=False, separators=(",", ":")))

    sh = shell(lang, 'insights', slug)
    html = render_page(lang=lang, slug=slug, title=title, desc=desc,
                       alt_it=SLUG['insights']['it'], alt_en=SLUG['insights']['en'],
                       ldjson=ldjson, geo_redirect='',
                       masthead=sh['masthead'], nav=sh['nav'], footer=sh['footer'],
                       body=body, og_type='website')
    path = f'{OUT}/{slug}index.html'
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write(html)
    return slug


made = []
for key, _, _ in PAGES:
    for lang in ('it', 'en'):
        if key == 'insights':
            made.append(build_insights_index(lang))
        else:
            made.append(build(key, lang))

for art in ARTICLES:
    for lang in ('it', 'en'):
        made.append(build_article(art, lang))
print('pages written:', len(made))
for m in made:
    print('   /' + m)


# ══════════════════════════════════════════════ 5. JS, sitemap, robots, CNAME
shutil.copy('assets/site.js', f'{OUT}/assets/site.js')
shutil.copy('assets/og.png',  f'{OUT}/assets/og.png')

import datetime
today = datetime.date.today().isoformat()
x = ['<?xml version="1.0" encoding="UTF-8"?>',
     '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
     '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
SITEMAP_ENTRIES = [(k, i, e) for k, i, e in PAGES]
for art in ARTICLES:
    SITEMAP_ENTRIES.append(('article', article_slug(art, 'it'), article_slug(art, 'en')))

for key, it_s, en_s in SITEMAP_ENTRIES:
    pr = ('1.0' if key == 'home'
          else '0.7' if key == 'contatti'
          else '0.8' if key == 'article'
          else '0.3' if key == 'privacy'
          else '0.9')
    for cur in (it_s, en_s):
        x += ['  <url>', f'    <loc>{DOMAIN}/{cur}</loc>',
              f'    <xhtml:link rel="alternate" hreflang="it" href="{DOMAIN}/{it_s}"/>',
              f'    <xhtml:link rel="alternate" hreflang="en" href="{DOMAIN}/{en_s}"/>',
              f'    <xhtml:link rel="alternate" hreflang="x-default" href="{DOMAIN}/{it_s}"/>',
              f'    <lastmod>{today}</lastmod>', '    <changefreq>monthly</changefreq>',
              f'    <priority>{pr}</priority>', '  </url>']
x.append('</urlset>')
open(f'{OUT}/sitemap.xml', 'w', encoding='utf-8').write('\n'.join(x))
open(f'{OUT}/robots.txt', 'w', encoding='utf-8').write(
    f'User-agent: *\nAllow: /\n\nSitemap: {DOMAIN}/sitemap.xml\n')
open(f'{OUT}/CNAME', 'w', encoding='utf-8').write('www.clegar.it\n')
open(f'{OUT}/.nojekyll', 'w', encoding='utf-8').write('')

# 404 page keeps visitors (and crawlers) inside the site
open(f'{OUT}/404.html', 'w', encoding='utf-8').write("""<!DOCTYPE html>
<html lang="it"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pagina non trovata | CLEGAR</title><meta name="robots" content="noindex,follow">
<link rel="stylesheet" href="/assets/style.css"><link rel="icon" href="/assets/mark.png">
</head><body>
<header class="masthead"><div class="masthead-row">
<a class="brand" href="/"><img src="/assets/logo.png" alt="CLEGAR" width="224"></a>
</div></header>
<div class="band band-white band-pad"><div class="wrap">
<p class="eyebrow">404</p>
<h1 style="max-width:22rem">Questa pagina non esiste.</h1>
<p class="lede" style="margin-top:1.2rem;max-width:34rem">Il collegamento potrebbe essere obsoleto.
Ripartite dalla <a href="/">home</a> o scriveteci a
<a href="mailto:info@clegar.it">info@clegar.it</a>.</p>
<p class="lede" style="max-width:34rem">This page doesn't exist &mdash; start from the
<a href="/en/">English home page</a>.</p>
</div></div></body></html>""")
print('\nextras: sitemap.xml, robots.txt, CNAME, .nojekyll, 404.html, site.js, og.png')
