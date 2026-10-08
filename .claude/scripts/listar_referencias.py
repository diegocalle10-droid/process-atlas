"""Lista todas las referencias vivas de un macroproceso con su apartado de origen.

Recorre el documento del macroproceso, sus procedimientos y sus manuales (sin el mapa
de relaciones) y escribe una línea por referencia: origen §apartado -> destino §apartado.
Es la base para construir o revisar el mapa local de relaciones
(Metodologia_de_relaciones.md §5 y §7).

Uso: python .claude/scripts/listar_referencias.py MPR_001
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) != 2 or not re.fullmatch(r'MPR_\d{3}', sys.argv[1]):
        print('Uso: python .claude/scripts/listar_referencias.py MPR_NNN')
        return
    carpeta = os.path.join(RAIZ, sys.argv[1])
    rutas = sorted(r for r in glob.glob(os.path.join(carpeta, '**', '*.md'), recursive=True)
                   if not r.endswith('_mapa_relaciones.md'))
    vistas = set()
    for ruta in rutas:
        origen = os.path.splitext(os.path.basename(ruta))[0]
        apartado = ''
        with open(ruta, encoding='utf8') as f:
            for linea in f:
                m = re.match(r'^(#{2,5})\s+(\d[\d.]*\.)\s', linea)
                if m:
                    apartado = m.group(2).rstrip('.')
                elif linea.startswith('### Anexo'):
                    apartado = linea[4:].strip()
                for r in re.finditer(r'\[\[(.*?)\]\]', linea):
                    destino = r.group(1).replace('\\|', '|').split('|')[0]
                    archivo, _, encabezado = destino.partition('#')
                    clave = (origen, apartado, archivo, encabezado)
                    if clave in vistas:
                        continue
                    vistas.add(clave)
                    print(f'{origen} §{apartado} -> {archivo}{" # " + encabezado if encabezado else ""}')



if __name__ == '__main__':
    main()
