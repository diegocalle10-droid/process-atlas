"""Comprueba los enlaces resolubles [[archivo#encabezado|texto]] del sistema de procesos.

Revisa todos los documentos de las carpetas MPR_NNN/ y el mapa global de relaciones.
Para cada enlace verifica que el archivo destino existe y que el encabezado citado
coincide literalmente con un encabezado del destino (Metodologia_de_relaciones.md §4.2).
Los enlaces a documentos que todavía no existen se listan aparte para revisarlos:
solo son admisibles como excepción autorizada por el usuario (§8.1).

Uso: python .claude/scripts/comprobar_enlaces.py
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def documentos_revisados():
    rutas = [r for r in glob.glob(os.path.join(RAIZ, 'MPR_[0-9][0-9][0-9]', '**', '*.md'), recursive=True)]
    rutas.append(os.path.join(RAIZ, '00_Mapa_global_relaciones.md'))
    return [r for r in rutas if os.path.exists(r)]


def indice_encabezados():
    archivos = {}
    for ruta in glob.glob(os.path.join(RAIZ, '**', '*.md'), recursive=True):
        if os.sep + '.claude' + os.sep in ruta:
            continue
        nombre = os.path.splitext(os.path.basename(ruta))[0]
        with open(ruta, encoding='utf8') as f:
            archivos[nombre] = {re.sub(r'^#+\s*', '', l).strip() for l in f if l.startswith('#')}
    return archivos


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    archivos = indice_encabezados()
    total, rotos, inexistentes = 0, [], {}
    for ruta in documentos_revisados():
        rel = os.path.relpath(ruta, RAIZ)
        with open(ruta, encoding='utf8') as f:
            for n, linea in enumerate(f, 1):
                for m in re.finditer(r'\[\[(.*?)\]\]', linea):
                    total += 1
                    destino = m.group(1).replace('\\|', '|').split('|')[0]
                    archivo, _, encabezado = destino.partition('#')
                    if archivo not in archivos:
                        inexistentes.setdefault(archivo, []).append(f'{rel}:{n}')
                    elif encabezado and encabezado.strip() not in archivos[archivo]:
                        rotos.append(f'{rel}:{n} -> {archivo} # {encabezado}')
    print(f'Enlaces revisados: {total}')
    print(f'Encabezados que no existen en su destino: {len(rotos)}')
    for r in rotos:
        print(f'  {r}')
    print(f'Destinos que todavía no existen: {len(inexistentes)}')
    for archivo, usos in sorted(inexistentes.items()):
        print(f'  {archivo} ({len(usos)} usos): {", ".join(usos[:6])}{" …" if len(usos) > 6 else ""}')



if __name__ == '__main__':
    main()
