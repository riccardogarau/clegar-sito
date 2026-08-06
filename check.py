#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verifica strutturale del sito generato.

Esegue i controlli che sono serviti a trovare difetti reali durante lo
sviluppo. Va lanciato dopo ogni modifica, PRIMA di pubblicare:

    python check.py

Esce con codice 1 se trova problemi, così può essere usato in automatico.
"""
import os, re, json, sys
from lxml import html as LH

SITE = 'docs'
DOMAIN = 'https://www.clegar.it'

problems = []


def fail(page, what):
    problems.append('%-42s %s' % (page, what))


pages = sorted(os.path.join(dp, f)
               for dp, _, fs in os.walk(SITE) for f in fs if f == 'index.html')
if not pages:
    sys.exit('Nessuna pagina in %s/ — lanciare prima: python build.py' % SITE)

alt = {}
for p in pages:
    url = '/' + os.path.relpath(p, SITE).replace('\\', '/')[:-10]
    doc = LH.parse(p).getroot()
    src = open(p, encoding='utf-8').read()
    base = os.path.dirname(p)

    # 1. link e risorse interne devono esistere
    refs = [e.get('href') for e in doc.findall('.//a[@href]') + doc.findall('.//link[@href]')]
    refs += [e.get('src') for e in doc.findall('.//img[@src]') + doc.findall('.//script[@src]')]
    for h in refs:
        if not h or h.startswith(('http', 'mailto:', 'tel:', '#', 'data:')):
            continue
        t = os.path.normpath(os.path.join(base, h))
        if os.path.isdir(t):
            t = os.path.join(t, 'index.html')
        elif not os.path.splitext(t)[1]:
            t += '/index.html'
        if not os.path.exists(t):
            fail(url, 'link rotto: ' + h)

    # 2. una sola lingua per pagina
    if 'class="it"' in src and 'class="en"' in src:
        fail(url, 'entrambe le lingue presenti nella stessa pagina')

    # 3. esattamente un H1
    n = len(doc.findall('.//h1'))
    if n != 1:
        fail(url, 'H1 presenti: %d (deve essere 1)' % n)

    # 4. canonical coerente con il percorso
    can = doc.find('.//link[@rel="canonical"]')
    if can is None or can.get('href') != DOMAIN + url:
        fail(url, 'canonical assente o errato')

    # 5. dati strutturati validi
    for sj in doc.findall('.//script[@type="application/ld+json"]'):
        try:
            json.loads(sj.text)
        except Exception as e:
            fail(url, 'JSON-LD non valido: %s' % e)

    # 6. nessun segnaposto rimasto
    for tok in ('{{ROOT}}', '{ga_block}', '__FIG_', '__SEIS__', '__BATHY__', '__WORD_'):
        if tok in src:
            fail(url, 'segnaposto non risolto: ' + tok)

    # 7. errore che si e' gia' verificato: un attributo transform su un
    #    elemento con classe animata viene sovrascritto dal CSS e sposta
    #    l'elemento fuori dall'inquadratura
    for e in doc.iter():
        cls = set((e.get('class') or '').split())
        if e.get('transform') and (cls & {'ship', 'sweep', 'draw'}):
            fail(url, 'transform + classe animata su <%s> (la nave finisce fuori campo)' % e.tag)

    alt[DOMAIN + url] = {a.get('hreflang'): a.get('href')
                         for a in doc.findall('.//link[@rel="alternate"]')}

# 8. hreflang reciproci fra le due lingue
for u, a in alt.items():
    for lg, t in a.items():
        if lg == 'x-default':
            continue
        if t not in alt:
            fail(u.replace(DOMAIN, ''), 'hreflang punta a pagina inesistente: ' + t)
        elif u not in alt[t].values():
            fail(u.replace(DOMAIN, ''), 'hreflang non reciproco con ' + t)

# 9. sitemap allineata alle pagine reali
sm = os.path.join(SITE, 'sitemap.xml')
if os.path.exists(sm):
    locs = re.findall(r'<loc>([^<]+)</loc>', open(sm, encoding='utf-8').read())
    have = {('/' + os.path.relpath(p, SITE).replace('\\', '/'))[:-10] for p in pages}
    for l in locs:
        if l.replace(DOMAIN, '') not in have:
            fail('sitemap.xml', 'URL inesistente: ' + l)
    if len(locs) != len(pages):
        fail('sitemap.xml', 'contiene %d URL ma le pagine sono %d' % (len(locs), len(pages)))
else:
    fail('sitemap.xml', 'mancante')

# 10. file indispensabili per la pubblicazione
for f in ('CNAME', '.nojekyll', 'robots.txt', '404.html', 'assets/style.css', 'assets/site.js'):
    if not os.path.exists(os.path.join(SITE, f)):
        fail(f, 'file mancante in %s/' % SITE)

print('Pagine controllate: %d' % len(pages))
if problems:
    print('\nPROBLEMI (%d):' % len(problems))
    for p in problems:
        print('  ' + p)
    sys.exit(1)
print('Nessun problema strutturale.')
