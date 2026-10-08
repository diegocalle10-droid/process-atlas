"""SessionStart (startup|resume|clear|compact). Triaje determinista del estado del sistema.

Se inyecta en el contexto de la sesión (hookSpecificOutput.additionalContext) para que el
agente orquestador proponga en su primera respuesta las funciones pendientes
(Orquestador.md §3). Solo lee; lo único que borra son marcas de pre-escritura caducadas.

Comprueba:
  F0  arranque: perfil sin responder, marcadores {{…}} sin sustituir, mapa de procesos vacío
      o inválido, macroprocesos del mapa sin desplegar
  F1  material pendiente en En_proceso/ (sin contar En_proceso/Procesado/)
  F2  rutas citadas en CLAUDE.md, Orquestador.md e Instrucciones_de_actuacion.md que no
      existen; carpetas MPR_NNN/ que no figuran en el mapa
  F3  documentos de MPR_NNN/ con código inválido o sin inscribir en el registro
  F7  ramas del árbol sin fila (glosa) en Orquestador.md §1
  Autocomprobación de los parsers: tablas y marcadores que leen los hooks
"""
import os
import re
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def salida(texto):
    import json
    sys.stdout.write(json.dumps({'hookSpecificOutput': {
        'hookEventName': 'SessionStart', 'additionalContext': texto}}, ensure_ascii=True))


def limpiar_marcas(L):
    if not os.path.isdir(L.RUTA_ESTADO):
        return
    limite = time.time() - 3600
    for nombre in os.listdir(L.RUTA_ESTADO):
        ruta = os.path.join(L.RUTA_ESTADO, nombre)
        if nombre.endswith('.marker') and os.path.getmtime(ruta) < limite:
            try:
                os.remove(ruta)
            except OSError:
                pass


def rutas_citadas_inexistentes(L, sin_desplegar):
    documentos = [os.path.join(L.RAIZ, '.claude', 'CLAUDE.md'), L.RUTA_ORQUESTADOR,
                  os.path.join(L.RAIZ, L.RECURSOS, 'Instrucciones_de_actuacion.md')]
    nombres = set()
    for dirpath, dirnames, filenames in os.walk(L.RAIZ):
        dirnames[:] = [d for d in dirnames if d not in ('.git', '.state', 'node_modules')]
        nombres.update(n.lower() for n in dirnames + filenames)
    creados_por_despliegue = ('En_proceso', '00_Mapa_global_relaciones.md', '00_Mapa_contenidos_pendientes.md')
    inexistentes = []
    for doc in documentos:
        if not os.path.exists(doc):
            inexistentes.append('(falta el propio documento %s)' % os.path.basename(doc))
            continue
        for t in re.findall(r'`([^`\r\n]+)`', L.leer(doc)):
            t = t.strip()
            if re.search(r'[*?\[\]%<>|{}]', t) or re.search(r'\s', t):
                continue  # patrones, marcadores o texto
            if re.search(r'00[NXYMP]|NNN', t):
                continue  # nombres genéricos de plantilla
            if '/' not in t and not re.search(r'\.(md|py|json)$', t):
                continue  # no parece una ruta
            if sin_desplegar and (t.startswith(creados_por_despliegue)
                                  or t.rstrip('/') in ('Procesado', 'Procedimientos', 'Manuales')):
                continue  # los crea el despliegue (F0)
            rel = t.rstrip('/')
            existe = any(os.path.exists(os.path.join(base, *rel.split('/')))
                         for base in (L.RAIZ, os.path.join(L.RAIZ, L.RECURSOS), os.path.join(L.RAIZ, '.claude')))
            if not existe and '/' not in rel:
                existe = rel.lower() in nombres
            if not existe and t not in inexistentes:
                inexistentes.append(t)
    return inexistentes


def ramas_sin_glosa(L):
    glosas = L.glosas_orquestador()
    sin_glosa = []

    def recorrer(ruta, relativo):
        for nombre in sorted(os.listdir(ruta)):
            if nombre in L.EXCLUIDOS:
                continue
            completo = os.path.join(ruta, nombre)
            rel = relativo + nombre + ('/' if os.path.isdir(completo) else '')
            if L.glosa_de(rel, glosas) is None:
                sin_glosa.append(rel)
            if os.path.isdir(completo):
                recorrer(completo, rel)
    recorrer(L.RAIZ, '')
    return sin_glosa, glosas


def main():
    try:
        import lib_sistema as L
        limpiar_marcas(L)
        secciones = []

        arranque = L.pendientes_arranque()
        if arranque:
            secciones.append('F0 (arranque del sistema): ' + ' | '.join(arranque)
                             + '. Ejecutar la skill desplegar-sistema (/desplegar-sistema).')

        bandeja = os.path.join(L.RAIZ, 'En_proceso')
        if os.path.isdir(bandeja):
            pendientes = [n for n in sorted(os.listdir(bandeja)) if n not in ('Procesado', '.gitkeep')]
            if pendientes:
                secciones.append('F1 (QA de la bandeja): %d elemento(s) en En_proceso/: %s. Procesar según '
                                 '00_Recursos_metodologia/Instrucciones_de_actuacion.md.' % (len(pendientes), '; '.join(pendientes)))

        inexistentes = rutas_citadas_inexistentes(L, bool(arranque))
        if inexistentes:
            secciones.append('F2 (coherencia y desfase): rutas citadas que no existen: ' + '; '.join(inexistentes) + '.')
        fuera = L.carpetas_fuera_del_mapa()
        if fuera:
            secciones.append('F2 (coherencia y desfase): carpetas de macroproceso que no figuran en el mapa de procesos: '
                             + '; '.join(fuera) + '. El sistema nunca las borra: decide el usuario.')

        anomalias, sin_inscribir = [], []
        for _, carpeta in L.carpetas_mpr():
            for dirpath, _, filenames in os.walk(carpeta):
                for nombre in filenames:
                    accion, motivo, _ = L.estado_codigo(os.path.join(dirpath, nombre))
                    if accion == 'Anomalia':
                        anomalias.append(motivo)
                    elif accion == 'PorRegistrar':
                        sin_inscribir.append(nombre)
        if anomalias:
            secciones.append('F3 (registro de códigos): anomalías: ' + ' | '.join(anomalias) + '.')
        if sin_inscribir:
            secciones.append('F3 (registro de códigos): documentos válidos sin inscribir: ' + '; '.join(sin_inscribir) + '.')

        sin_glosa, glosas = ramas_sin_glosa(L)
        if sin_glosa:
            secciones.append('F7 (ramas sin glosa): sin fila en Orquestador.md §1: ' + '; '.join(sin_glosa) + '.')

        parsers = list(L.legibilidad_registro())
        if not glosas:
            parsers.append('Orquestador.md: no se puede leer la tabla del apartado 1 (el árbol quedaría sin glosas)')
        cabecera_mapa, _ = L.primera_tabla(L.seccion(L.leer(L.RUTA_MAPA), 1)) if os.path.exists(L.RUTA_MAPA) else (None, [])
        if not cabecera_mapa or [L.sin_tildes(c) for c in cabecera_mapa[:3]] != ['codigo', 'nombre', 'tipo']:
            parsers.append('00_Mapa_procesos.md: no se encuentra la tabla «Código | Nombre | Tipo» del apartado 1')
        for ruta, inicio, fin in ((L.RUTA_ARBOL, '<!-- ARBOL:INICIO -->', '<!-- ARBOL:FIN -->'),
                                  (L.RUTA_FICHAS, '<!-- FICHAS:INICIO -->', '<!-- FICHAS:FIN -->')):
            if not os.path.exists(ruta):
                parsers.append('falta ' + L.ruta_relativa(ruta))
            elif inicio not in L.leer(ruta) or fin not in L.leer(ruta):
                parsers.append(L.ruta_relativa(ruta) + ': faltan los marcadores que lee su hook')
        if parsers:
            secciones.append('AUTOCOMPROBACIÓN (automatismos en riesgo de fallar en silencio): ' + ' | '.join(parsers))

        if not secciones:
            salida('Triaje de arranque (process-atlas): sin pendientes. Sistema desplegado, bandeja vacía, rutas citadas '
                   'existentes, registro de códigos coherente, todas las ramas con glosa y automatismos legibles.')
        else:
            salida('Triaje de arranque (process-atlas). Funciones del orquestador pendientes (Orquestador.md §3):\n- '
                   + '\n- '.join(secciones))
    except Exception as e:
        salida('Triaje de arranque: el script de triaje falló (%s). Revisar .claude/hooks/triaje_sesion.py antes de '
               'confiar en el estado del sistema.' % e)


if __name__ == '__main__':
    main()
