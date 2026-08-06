# -*- coding: utf-8 -*-
"""Costruisce l'anteprima locale a partire dal sito reale già generato.

L'anteprima è un file unico: tutte le pagine di entrambe le lingue sono
incluse come sezioni e la navigazione avviene in JavaScript. Serve solo
per guardare il sito; la versione da pubblicare resta l'archivio.
"""
import os, re, base64
from lxml import html as LH, etree

SITE = 'docs'
OUT = 'ANTEPRIMA-locale.html'


def tostr(node):
    return etree.tostring(node, encoding='unicode', method='html')


def inner(node):
    out = node.text or ''
    for ch in node:
        out += tostr(ch)
    return out


# ------------------------------------------------ raccolta di tutte le pagine
pages = []
for dp, _, fs in os.walk(SITE):
    if 'index.html' not in fs:
        continue
    path = os.path.join(dp, 'index.html')
    slug = os.path.relpath(path, SITE).replace('\\', '/')[:-10]   # '' oppure 'en/...'
    doc = LH.parse(path).getroot()
    lang = doc.get('lang')
    main = doc.find('.//main')
    if main is None:
        continue
    pages.append({
        'slug': slug,
        'lang': lang,
        'title': doc.findtext('.//title'),
        'body': inner(main),
        'doc': doc,
    })
pages.sort(key=lambda p: (p['lang'], p['slug']))
print('pagine raccolte:', len(pages))

# masthead / nav / footer presi dalla home di ciascuna lingua
shell = {}
for lang, home in (('it', ''), ('en', 'en/')):
    doc = [p for p in pages if p['slug'] == home][0]['doc']
    shell[lang] = {
        'masthead': tostr(doc.find('.//header')),
        'nav': tostr(doc.find('.//nav')),
        'footer': tostr(doc.find('.//footer')),
    }

# ------------------------------------------------ risorse da incorporare
css = open(f'{SITE}/assets/style.css', encoding='utf-8').read()

ASSETS = {}
for name in os.listdir(f'{SITE}/assets'):
    if name.rsplit('.', 1)[-1].lower() in ('png', 'webp', 'jpg', 'jpeg', 'svg'):
        mime = {'png': 'image/png', 'webp': 'image/webp', 'jpg': 'image/jpeg',
                'jpeg': 'image/jpeg', 'svg': 'image/svg+xml'}[name.rsplit('.', 1)[-1].lower()]
        data = base64.b64encode(open(f'{SITE}/assets/{name}', 'rb').read()).decode()
        ASSETS[name] = f'data:{mime};base64,{data}'


def inline_assets(html):
    """sostituisce ogni riferimento a assets/<file> con il dato incorporato"""
    def rep(m):
        name = m.group(2)
        return m.group(1) + ASSETS.get(name, m.group(0)) if name in ASSETS else m.group(0)
    return re.sub(r'((?:src|href)=")(?:\.\./)*assets/([A-Za-z0-9_.-]+)"',
                  lambda m: (m.group(1) + ASSETS[m.group(2)] + '"') if m.group(2) in ASSETS
                  else m.group(0), html)


# ------------------------------------------------ riscrittura dei collegamenti
SLUGS = {p['slug'] for p in pages}


def to_slug(href, from_slug):
    """converte un href relativo nello slug di destinazione, se è interno"""
    if not href or href.startswith(('http', 'mailto:', 'tel:', '#', 'data:')):
        return None
    base = os.path.dirname('/' + from_slug + 'index.html')
    target = os.path.normpath(os.path.join(base, href)).lstrip('/')
    if target == '.':
        target = ''
    if target and not target.endswith('/'):
        target += '/'
    return target if target in SLUGS else None


def rewrite(html, from_slug):
    frag = LH.fragment_fromstring(html, create_parent='div')
    for a in frag.findall('.//a[@href]'):
        s = to_slug(a.get('href'), from_slug)
        if s is not None:
            a.set('data-goto', s)
            a.set('href', '#' + (s or 'home'))
    return inner(frag)


sections = []
for p in pages:
    body = rewrite(p['body'], p['slug'])
    sections.append(
        f'<section class="ppage" data-lang="{p["lang"]}" data-slug="{p["slug"]}" '
        f'data-title="{p["title"]}">{body}</section>')

shell_html = []
for lang in ('it', 'en'):
    sh = {k: rewrite(v, '' if lang == 'it' else 'en/') for k, v in shell[lang].items()}
    shell_html.append(
        f'<div class="pshell" data-lang="{lang}">{sh["masthead"]}{sh["nav"]}</div>')
    shell_html.append(
        f'<div class="pfoot" data-lang="{lang}">{sh["footer"]}</div>')

EXTRA_CSS = '''
/* --- solo anteprima --- */
.ppage,.pshell,.pfoot{display:none}
.ppage.on,.pshell.on,.pfoot.on{display:block}
.pbanner{
  position:fixed;left:0;right:0;bottom:0;z-index:1200;background:#C9821E;color:#fff;
  font-family:"IBM Plex Mono",monospace;font-size:.62rem;letter-spacing:.1em;
  text-transform:uppercase;text-align:center;padding:.5rem .8rem;
}
body{padding-bottom:2.2rem}
'''

JS = r'''
(function () {
  var pages  = [].slice.call(document.querySelectorAll('.ppage'));
  var shells = [].slice.call(document.querySelectorAll('.pshell'));
  var foots  = [].slice.call(document.querySelectorAll('.pfoot'));
  var lang = 'it', slug = '';

  function langOf(s) { return s.indexOf('en/') === 0 || s === 'en/' ? 'en' : 'it'; }

  function show(s) {
    var target = pages.filter(function (p) { return p.dataset.slug === s; })[0];
    if (!target) { target = pages[0]; s = target.dataset.slug; }
    slug = s; lang = target.dataset.lang;
    pages.forEach(function (p) { p.classList.toggle('on', p === target); });
    shells.forEach(function (x) { x.classList.toggle('on', x.dataset.lang === lang); });
    foots.forEach(function (x) { x.classList.toggle('on', x.dataset.lang === lang); });
    document.documentElement.lang = lang;
    document.title = target.dataset.title;
    // stato attivo nel menu della lingua corrente
    shells.forEach(function (sh) {
      sh.querySelectorAll('.tab').forEach(function (t) {
        var g = t.getAttribute('data-goto');
        if (g === slug) t.setAttribute('aria-current', 'page');
        else t.removeAttribute('aria-current');
      });
    });
    window.scrollTo(0, 0);
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[data-goto]');
    if (!a) return;
    e.preventDefault();
    show(a.getAttribute('data-goto'));
  });

  show('');

  /* visualizzatore figure a schermo intero, come sul sito */
  if (window.matchMedia && window.matchMedia('(max-width: 900px)').matches) {
    var modal = document.createElement('div');
    modal.className = 'figmodal';
    modal.innerHTML = '<div class="figmodal-bar"><span>Scorri per esplorare</span>'
      + '<button class="figmodal-close" type="button">Chiudi</button></div>'
      + '<div class="figmodal-body"></div>';
    document.body.appendChild(modal);
    var mb = modal.querySelector('.figmodal-body');
    document.addEventListener('click', function (e) {
      var fig = e.target.closest('figure[data-zoomable]');
      if (!fig) return;
      var chart = fig.querySelector('svg, .datafig');
      if (!chart) return;
      mb.innerHTML = ''; mb.appendChild(chart.cloneNode(true));
      modal.classList.add('open'); document.body.style.overflow = 'hidden';
    });
    modal.querySelector('.figmodal-close').addEventListener('click', function () {
      modal.classList.remove('open'); document.body.style.overflow = ''; mb.innerHTML = '';
    });
  }
})();
'''

html = f'''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>CLEGAR — anteprima locale</title>
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
{css}
{EXTRA_CSS}
</style>
</head>
<body>
{''.join(shell_html[0::2])}
<main id="main">
{''.join(sections)}
</main>
{''.join(shell_html[1::2])}
<div class="pbanner">Anteprima locale — per pubblicare usare clegar-sito-github.zip</div>
<script>{JS}</script>
</body>
</html>
'''

html = inline_assets(html)
html = html.replace('\u2014', '\u2013') if False else html
open(OUT, 'w', encoding='utf-8').write(html)
print('anteprima: %.0f KB' % (os.path.getsize(OUT) / 1024))
print('sezioni:', html.count('class="ppage"'))
print('riferimenti assets rimasti:', len(re.findall(r'(?:src|href)="(?:\.\./)*assets/', html)))
