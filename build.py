#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Punto di ingresso unico: costruisce il sito e l'anteprima.

    python build.py            costruisce sito + anteprima
    python build.py --figures  rigenera anche le figure degli articoli
    python build.py --check    costruisce e lancia la verifica strutturale

Il sito finito va in docs/ (è la cartella che GitHub Pages pubblica).
L'anteprima è ANTEPRIMA-locale.html: file unico, solo per guardare.
"""
import subprocess, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)


def run(cmd, cwd=None):
    print('\n$ ' + ' '.join(cmd))
    r = subprocess.run([sys.executable] + cmd, cwd=cwd)
    if r.returncode != 0:
        sys.exit('FALLITO: ' + ' '.join(cmd))


if '--figures' in sys.argv:
    # le figure degli articoli vivono in content/; lo script le scrive lì
    run(['tools/figures/gen_article_figs.py'])
    for f in ('fig_art_origin.svg', 'fig_art_lines.svg'):
        if os.path.exists(f):
            os.replace(f, os.path.join('content', f))
    print('figure articoli rigenerate in content/')

run(['build_static.py'])
run(['build_preview.py'])

if '--check' in sys.argv:
    run(['check.py'])

print('\nFatto.')
print('  sito     -> docs/            (da pubblicare)')
print('  anteprima-> ANTEPRIMA-locale.html')
