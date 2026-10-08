"""PostToolUse (Bash|PowerShell|Write|Edit|MultiEdit). Regenera las dos vistas derivadas:

1. El bloque <!-- ARBOL:INICIO --> … <!-- ARBOL:FIN --> de Arbol_del_proyecto.md, a partir del
   árbol real, con la glosa de cada rama leída de Orquestador.md §1. Una rama sin fila queda
   sin glosa y el triaje de arranque la reporta (F7).
2. El bloque <!-- FICHAS:INICIO --> … <!-- FICHAS:FIN --> de Tabla_de_fichas.md, leyendo el
   anexo de ficha técnica de cada MPR, PRC y MAN de las carpetas MPR_NNN/.
Solo escribe si el contenido cambia. No falla el turno.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_sistema as L  # noqa: E402

CAMPOS = ['codigo', 'nombre', 'tipo', 'macroproceso', 'version', 'propietario', 'fecha de aprobacion', 'ubicacion']
ORDEN = {'MPR': 1, 'PRC': 2, 'MAN': 3}


def lineas_arbol(ruta, prefijo, relativo, glosas):
    elementos = [e for e in os.listdir(ruta) if e not in L.EXCLUIDOS]
    elementos.sort(key=lambda e: (not os.path.isdir(os.path.join(ruta, e)), e.lower()))
    salida = []
    for i, nombre in enumerate(elementos):
        completo = os.path.join(ruta, nombre)
        ultimo = i == len(elementos) - 1
        conector = '└── ' if ultimo else '├── '
        if os.path.isdir(completo):
            rel = relativo + nombre + '/'
            vacia = not [e for e in os.listdir(completo) if e not in L.EXCLUIDOS]
            glosa = L.glosa_de(rel, glosas)
            salida.append(prefijo + conector + nombre + '/' + (' (vacía)' if vacia else '')
                          + (' — ' + glosa if glosa else ''))
            salida += lineas_arbol(completo, prefijo + ('    ' if ultimo else '│   '), rel, glosas)
        else:
            glosa = L.glosa_de(relativo + nombre, glosas)
            salida.append(prefijo + conector + nombre + (' — ' + glosa if glosa else ''))
    return salida


def reemplazar_bloque(ruta, inicio, fin, contenido):
    if not os.path.exists(ruta):
        return
    texto = L.leer(ruta)
    m = re.search(r'(?s)(%s[ \t]*\r?\n).*?(\r?\n[ \t]*%s)' % (re.escape(inicio), re.escape(fin)), texto)
    if not m:
        return
    nuevo = texto[:m.end(1)] + contenido + texto[m.start(2):]
    if nuevo != texto:
        L.escribir(ruta, nuevo)


def actualizar_arbol():
    arbol = ['./'] + lineas_arbol(L.RAIZ, '', '', L.glosas_orquestador())
    reemplazar_bloque(L.RUTA_ARBOL, '<!-- ARBOL:INICIO -->', '<!-- ARBOL:FIN -->',
                      '```\n' + '\n'.join(arbol) + '\n```')


def datos_ficha(ruta):
    lineas = L.leer(ruta).splitlines()
    inicio = next((i for i, l in enumerate(lineas)
                   if re.match(r'^#{2,4}\s*anexo \d+\.\s*ficha tecnica del', L.sin_tildes(l))), None)
    datos = {}
    if inicio is None:
        return datos
    for l in lineas[inicio + 1:]:
        l = l.strip()
        if not l:
            if datos:
                break
            continue
        if not l.startswith('|'):
            break
        c = L.celdas(l)
        clave = L.sin_tildes(c[0]) if c else ''
        if len(c) >= 2 and clave != 'campo' and not re.fullmatch(r'-+', clave):
            datos[clave] = c[1]
    return datos


def actualizar_fichas():
    filas = []
    for _, carpeta in L.carpetas_mpr():
        for dirpath, _, filenames in os.walk(carpeta):
            for nombre in filenames:
                codigo = L.codigo_desde_nombre(nombre)
                if not codigo or not nombre.endswith('.md'):
                    continue
                ruta = os.path.join(dirpath, nombre)
                datos = datos_ficha(ruta)
                valores = [datos.get(c, '') for c in CAMPOS]
                valores[0] = valores[0] or L.guion(*codigo)
                valores[7] = valores[7] or L.ruta_relativa(ruta)
                filas.append((ORDEN[codigo[0]], codigo[1], '| ' + ' | '.join(valores) + ' |'))
    cabecera = ('| Código | Nombre | Tipo | Macroproceso | Versión | Propietario | Fecha de aprobación | Ubicación |\n'
                '|---|---|---|---|---|---|---|---|')
    cuerpo = '\n'.join(f[2] for f in sorted(filas)) if filas else '\nSin documentos oficiales registrados.'
    reemplazar_bloque(L.RUTA_FICHAS, '<!-- FICHAS:INICIO -->', '<!-- FICHAS:FIN -->', cabecera + '\n' + cuerpo)


def main():
    for tarea in (actualizar_arbol, actualizar_fichas):
        try:
            tarea()
        except Exception:
            pass


if __name__ == '__main__':
    main()
