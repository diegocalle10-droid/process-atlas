"""Elimina las marcas de trabajo de los documentos de un macroproceso (Metodologia_de_redaccion.md §12).

Suprime las marcas en línea `[VERIFICADO…]` y `[INFERENCIA…]` y las líneas de fuente
(`Fuente: …`, `Filas …`). No toca *(Pendiente de desarrollo)* ni *No aplica*: el primero
se resuelve en el cierre F6 y el segundo es contenido del documento. Sin el argumento
--aplicar solo informa de lo que eliminaría.

Uso: python .claude/scripts/quitar_marcas_trabajo.py MPR_001 [--aplicar]
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
LINEA_FUENTE = r'(?m)^`(?:Fuente|Filas)[^`\n]*`[ \t]*\n(?:[ \t]*\n)?'
MARCA_EN_LINEA = r'[ \t]*`\[(?:VERIFICADO|INFERENCIA)[^`\n]*\]`'


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    if len(sys.argv) < 2 or not re.fullmatch(r'MPR_\d{3}', sys.argv[1]):
        print('Uso: python .claude/scripts/quitar_marcas_trabajo.py MPR_NNN [--aplicar]')
        return
    aplicar = '--aplicar' in sys.argv[2:]
    carpeta = os.path.join(RAIZ, sys.argv[1])
    for ruta in sorted(glob.glob(os.path.join(carpeta, '**', '*.md'), recursive=True)):
        if ruta.endswith('_mapa_relaciones.md'):
            continue
        with open(ruta, encoding='utf8') as f:
            texto = f.read()
        nuevo, n1 = re.subn(LINEA_FUENTE, '', texto)
        nuevo, n2 = re.subn(MARCA_EN_LINEA, '', nuevo)
        nuevo = re.sub(r'\n{3,}', '\n\n', nuevo)
        print(f'{os.path.relpath(ruta, RAIZ)}: {n1} líneas de fuente, {n2} marcas en línea')
        if aplicar and nuevo != texto:
            with open(ruta, 'w', encoding='utf8') as f:
                f.write(nuevo)
    if not aplicar:
        print('Modo informe: no se ha modificado ningún archivo. Añade --aplicar para eliminar.')



if __name__ == '__main__':
    main()
