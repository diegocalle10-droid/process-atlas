"""Detecta dependencias circulares entre apartados (Metodologia_de_relaciones.md §8.3).

Lee los enlaces [[archivo#encabezado|texto]] de los documentos de las carpetas MPR_NNN/
(sin los mapas de relaciones) y construye las aristas «apartado de origen -> apartado
de destino». Informa de todo par de apartados que se citan mutuamente, contando
también las citas entre un apartado y sus subapartados.

Uso: python .claude/scripts/comprobar_ciclos.py
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def aristas():
    resultado = set()
    rutas = [r for r in glob.glob(os.path.join(RAIZ, 'MPR_[0-9][0-9][0-9]', '**', '*.md'), recursive=True)]
    for ruta in rutas:
        if ruta.endswith('_mapa_relaciones.md'):
            continue
        origen = os.path.splitext(os.path.basename(ruta))[0]
        apartado = ''
        with open(ruta, encoding='utf8') as f:
            for linea in f:
                m = re.match(r'^#{2,5}\s+(\d[\d.]*\.)\s', linea)
                if m:
                    apartado = m.group(1).rstrip('.')
                for r in re.finditer(r'\[\[(.*?)\]\]', linea):
                    destino = r.group(1).replace('\\|', '|').split('|')[0]
                    archivo, _, encabezado = destino.partition('#')
                    n = re.match(r'(\d[\d.]*\.)', encabezado)
                    if n:
                        resultado.add((origen, apartado, archivo, n.group(1).rstrip('.')))
    return resultado


def solapan(a, b):
    return a == b or a.startswith(b + '.') or b.startswith(a + '.')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    red = aristas()
    ciclos = []
    for (a, x, b, y) in red:
        for (c, z, d, w) in red:
            if c == b and d == a and solapan(z, y) and solapan(w, x) and (a, x) < (b, y):
                ciclos.append((a, x, b, y))
    print(f'Aristas apartado -> apartado: {len(red)}')
    print(f'Ciclos de dependencia: {len(ciclos)}')
    for a, x, b, y in sorted(set(ciclos)):
        print(f'  {a} §{x} <-> {b} §{y}')



if __name__ == '__main__':
    main()
