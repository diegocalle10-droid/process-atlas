"""Comprueba el formato y el destino de las referencias en los documentos de MPR_NNN/.

Aplica Metodologia_de_relaciones.md §4.3 a §4.5:
1. Enlaces intercalados: ningún enlace [[...]] puede ir dentro de una frase ni de una celda
   del cuerpo; solo en una línea propia que empiece por «*Referencia:*» o «*Referencias:*».
   Quedan exentos los mapas de relaciones y el Anexo 3 de los macroprocesos, cuya función
   es referenciar.
2. Destino: desde un procedimiento no se remite a la descripción de una actividad de un
   macroproceso (encabezado 3.1.N), salvo a las actividades que no tienen procedimiento
   propio (las que su 4.1 marca como «No aplica»), a los apartados que el índice del mapa
   global registra como origen de una definición compartida y desde el 2.1, donde el
   procedimiento declara la actividad que desarrolla.

Uso: python .claude/scripts/comprobar_referencias_en_prosa.py [--resumen]
"""
import glob
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ENLACE = re.compile(r'\[\[(.*?)\]\]')
LINEA_REFERENCIA = re.compile(r'^\s*\*Referencias?:\*')


def documentos():
    rutas = [r for r in glob.glob(os.path.join(RAIZ, 'MPR_[0-9][0-9][0-9]', '**', '*.md'), recursive=True)]
    return sorted(r for r in rutas if not r.endswith('_mapa_relaciones.md'))


def actividades_sin_procedimiento():
    """Encabezados 3.1.N de cada MPR cuya actividad no tiene procedimiento (4.1 «No aplica»)."""
    permitidas = set()
    for ruta in glob.glob(os.path.join(RAIZ, 'MPR_[0-9][0-9][0-9]', 'MPR_[0-9][0-9][0-9].md')):
        nombre = os.path.splitext(os.path.basename(ruta))[0]
        with open(ruta, encoding='utf8') as f:
            lineas = f.read().split('\n')
        en_41, sin_prc = False, []
        for l in lineas:
            if l.startswith('### 4.1.'):
                en_41 = True
                continue
            if en_41 and l.startswith('#'):
                en_41 = False
            if en_41 and l.startswith('|') and 'No aplica' in l:
                celdas = [c.strip() for c in l.strip().strip('|').split('|')]
                if len(celdas) >= 2 and 'No aplica' in celdas[1]:
                    sin_prc.append(celdas[0])
        for l in lineas:
            m = re.match(r'^#{3,4}\s+(3\.1\.\d+\.\s+(.*))$', l)
            if m and any(m.group(2).startswith(a) for a in sin_prc):
                permitidas.add((nombre, m.group(1).strip()))
    return permitidas


def definiciones_registradas():
    """Destinos (archivo, encabezado) de la columna «Definido en» del índice del mapa global."""
    registradas = set()
    ruta = os.path.join(RAIZ, '00_Mapa_global_relaciones.md')
    if not os.path.exists(ruta):
        return registradas
    with open(ruta, encoding='utf8') as f:
        en_indice = False
        for l in f:
            if l.startswith('## '):
                en_indice = 'Índice de definiciones' in l
            if en_indice and l.startswith('|'):
                celdas = l.strip().strip('|').split(' | ')
                if len(celdas) >= 2:
                    for e in ENLACE.findall(celdas[1]):
                        archivo, _, encabezado = e.replace('\\|', '|').split('|')[0].partition('#')
                        registradas.add((archivo, encabezado.strip()))
    return registradas


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    resumen = '--resumen' in sys.argv
    permitidas = actividades_sin_procedimiento() | definiciones_registradas()
    total_intercalados, total_destino = 0, 0
    for ruta in documentos():
        rel = os.path.relpath(ruta, RAIZ)
        es_prc = os.path.basename(ruta).startswith('PRC_')
        with open(ruta, encoding='utf8') as f:
            lineas = f.read().split('\n')
        en_codigo, en_anexo3, en_21 = False, False, False
        intercalados, destino = [], []
        for n, linea in enumerate(lineas, 1):
            if linea.strip().startswith('```'):
                en_codigo = not en_codigo
                continue
            if en_codigo:
                continue
            if linea.startswith('#'):
                en_anexo3 = linea.startswith('### Anexo 3.') or linea.startswith('### 4.1.')
                en_21 = linea.startswith('### 2.1.')
            enlaces = ENLACE.findall(linea)
            if not enlaces:
                continue
            if not LINEA_REFERENCIA.match(linea) and not en_anexo3:
                tipo = 'celda' if linea.lstrip().startswith('|') else 'prosa'
                intercalados.append(f'{rel}:{n} ({tipo})')
            if es_prc and not en_21:
                for e in enlaces:
                    archivo, _, encabezado = e.replace('\\|', '|').split('|')[0].partition('#')
                    if re.match(r'MPR_\d{3}$', archivo) and re.match(r'3\.1\.\d+\.', encabezado.strip()):
                        if (archivo, encabezado.strip()) not in permitidas:
                            destino.append(f'{rel}:{n} -> {archivo} # {encabezado.strip()}')
        total_intercalados += len(intercalados)
        total_destino += len(destino)
        if intercalados or destino:
            print(f'{rel}: {len(intercalados)} intercalados, {len(destino)} con destino a revisar')
            if not resumen:
                for x in intercalados:
                    print(f'  intercalado  {x}')
                for x in destino:
                    print(f'  destino      {x}')
    print(f'Enlaces intercalados en prosa o celda: {total_intercalados}')
    print(f'Referencias de un procedimiento a una actividad de macroproceso: {total_destino}')



if __name__ == '__main__':
    main()
