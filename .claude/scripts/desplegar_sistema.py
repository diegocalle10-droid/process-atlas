"""Despliega el sistema de procesos a partir del perfil de la organización y del mapa de procesos
(función F0 del orquestador, Orquestador.md §3).

Lee 00_Recursos_metodologia/Metodologia/00_Perfil_organizacion.md y 00_Mapa_procesos.md y:

1. Sustituye cada marcador {{…}} de los documentos del sistema (.claude/ y
   00_Recursos_metodologia/) por la respuesta de su pregunta en el perfil. Una pregunta
   opcional sin respuesta se sustituye por *(Pendiente de desarrollo)*.
2. Crea por cada macroproceso del mapa su carpeta MPR_NNN/ con Procedimientos/, Manuales/ y su
   mapa local de relaciones generado desde su plantilla.
3. Crea o actualiza en la raíz 00_Mapa_global_relaciones.md (matriz N×N de macroprocesos),
   00_Mapa_contenidos_pendientes.md y la bandeja En_proceso/Procesado/.
4. Fija en Registro_de_codigos.md el rango de la serie MPR según el mapa.

Es idempotente: lo que ya existe no se toca y solo se crea lo que falta. Nunca borra: una
carpeta MPR_NNN/ que ya no figura en el mapa se avisa y decide el usuario.

Uso: python .claude/scripts/desplegar_sistema.py [--comprobar]
     --comprobar  solo informa de lo que haría, sin escribir nada.
"""
import os
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'hooks'))
import lib_sistema as L  # noqa: E402

VACIO = '*(Pendiente de desarrollo)*'


def bloque_plantilla(nombre):
    """Contenido del bloque ```markdown … ``` de una plantilla, con saltos de línea \\n."""
    texto = L.leer(os.path.join(L.RUTA_PLANTILLAS, nombre)).replace('\r\n', '\n')
    m = re.search(r'```markdown\n(.*?)\n```\s*$', texto, re.S)
    if not m:
        raise ValueError('la plantilla %s no tiene bloque ```markdown' % nombre)
    return m.group(1) + '\n'


def vaciar_tablas(texto):
    """Sustituye cada tabla de ejemplo seguida de su nota «[Si …: «X».]» por X."""
    return re.sub(r'(?m)(?:^\|.*\n)+\n\[Si[^\]\n]*?«(.+?)»\.?\]', lambda m: m.group(1), texto)


def matriz(codigos, marcas):
    cab = '| Origen ↓ / Destino → | ' + ' | '.join(codigos) + ' |'
    sep = '|---|' + '---|' * len(codigos)
    filas = []
    for o in codigos:
        celdas = ['—' if o == d else marcas.get((o, d), '') for d in codigos]
        filas.append('| **%s** |' % o + '|'.join(' %s ' % c if c else ' ' for c in celdas) + '|')
    return '\n'.join([cab, sep] + filas)


def marcas_existentes(texto):
    cabecera, filas = L.primera_tabla(L.seccion(texto, 1))
    marcas = {}
    if not cabecera:
        return marcas
    destinos = cabecera[1:]
    for f in filas:
        origen = f[0].strip('* ')
        for d, valor in zip(destinos, f[1:]):
            if valor and valor != '—':
                marcas[(origen, d)] = valor
    return marcas


def sustituir_marcadores(respuestas, aplicar):
    cambiados = []
    for rel, encontrados in sorted(L.archivos_con_marcadores().items()):
        ruta = os.path.join(L.RAIZ, *rel.split('/'))
        texto = L.leer(ruta)
        nuevo = L.RE_MARCADOR.sub(lambda m: respuestas.get(m.group(1), m.group(0)), texto)
        if nuevo != texto:
            cambiados.append(rel)
            if aplicar:
                L.escribir(ruta, nuevo)
    return cambiados


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    aplicar = '--comprobar' not in sys.argv
    hechos, avisos = [], []

    preguntas = L.preguntas_del_perfil()
    if not preguntas:
        print('BLOQUEADO: no se puede leer la tabla de preguntas de 00_Perfil_organizacion.md.')
        return 1
    sin_responder = [p for p in preguntas if p['obligatoria'] and not p['respuesta']]
    mapa = L.macroprocesos_del_mapa()
    errores = L.validar_mapa(mapa)
    if sin_responder or errores:
        print('BLOQUEADO: no se despliega nada hasta resolver lo siguiente.')
        for p in sin_responder:
            print('  - %s sin responder: %s' % (p['id'], p['pregunta']))
        for e in errores:
            print('  - mapa de procesos: %s' % e)
        return 1

    # 1. Marcadores
    respuestas = {p['marcador']: (p['respuesta'] or VACIO) for p in preguntas}
    desconocidos = sorted({m for lista in L.archivos_con_marcadores().values() for m in lista} - set(respuestas))
    if desconocidos:
        avisos.append('marcadores sin pregunta en el perfil (se dejan sin sustituir): ' + ', '.join(desconocidos))
    for rel in sustituir_marcadores(respuestas, aplicar):
        hechos.append('marcadores sustituidos en ' + rel)

    fecha = L.hoy()
    # 2. Carpetas de macroproceso
    for f in mapa:
        nombre_carpeta = 'MPR_%03d' % f['n']
        carpeta = os.path.join(L.RAIZ, nombre_carpeta)
        for sub in ('Procedimientos', 'Manuales'):
            destino = os.path.join(carpeta, sub)
            if not os.path.isdir(destino):
                hechos.append('creada %s/%s/' % (nombre_carpeta, sub))
                if aplicar:
                    os.makedirs(destino, exist_ok=True)
                    open(os.path.join(destino, '.gitkeep'), 'w').close()
        mapa_local = os.path.join(carpeta, '%s_mapa_relaciones.md' % nombre_carpeta)
        if not os.path.exists(mapa_local):
            hechos.append('creado %s/%s_mapa_relaciones.md' % (nombre_carpeta, nombre_carpeta))
            if aplicar:
                texto = bloque_plantilla('Plantilla_mapa_local_relaciones.md')
                texto = texto.replace('MPR-NNN', f['codigo']).replace('[nombre del macroproceso]', f['nombre'])
                texto = vaciar_tablas(texto.replace('[dd/mm/aaaa]', fecha))
                L.escribir(mapa_local, texto)

    # 3. Raíz
    codigos = [f['codigo'] for f in mapa]
    ruta_global = os.path.join(L.RAIZ, '00_Mapa_global_relaciones.md')
    if os.path.exists(ruta_global):
        texto = L.leer(ruta_global).replace('\r\n', '\n')
        bloque = L.seccion(texto, 1)
        nuevo = texto.replace(bloque, re.sub(r'(?m)(^\|.*\n?)+', matriz(codigos, marcas_existentes(texto)) + '\n', bloque, count=1), 1)
        if nuevo != texto:
            hechos.append('matriz de 00_Mapa_global_relaciones.md ajustada al mapa (%d macroprocesos)' % len(codigos))
            if aplicar:
                L.escribir(ruta_global, nuevo)
    else:
        hechos.append('creado 00_Mapa_global_relaciones.md (matriz de %d macroprocesos)' % len(codigos))
        if aplicar:
            texto = bloque_plantilla('Plantilla_mapa_global_relaciones.md').replace('[dd/mm/aaaa]', fecha)
            texto = vaciar_tablas(texto)
            bloque = L.seccion(texto, 1)
            texto = texto.replace(bloque, re.sub(r'(?m)(^\|.*\n?)+', matriz(codigos, {}) + '\n', bloque, count=1), 1)
            L.escribir(ruta_global, texto)
    ruta_pendientes = os.path.join(L.RAIZ, '00_Mapa_contenidos_pendientes.md')
    if not os.path.exists(ruta_pendientes):
        hechos.append('creado 00_Mapa_contenidos_pendientes.md')
        if aplicar:
            texto = bloque_plantilla('Plantilla_mapa_contenidos_pendientes.md').replace('[dd/mm/aaaa]', fecha)
            L.escribir(ruta_pendientes, vaciar_tablas(texto))
    procesado = os.path.join(L.RAIZ, 'En_proceso', 'Procesado')
    if not os.path.isdir(procesado):
        hechos.append('creada En_proceso/Procesado/')
        if aplicar:
            os.makedirs(procesado, exist_ok=True)
            open(os.path.join(procesado, '.gitkeep'), 'w').close()

    # 4. Registro de códigos
    texto = L.leer(L.RUTA_REGISTRO)
    nuevo = L.control_de_series(texto, mapa)
    if nuevo != texto:
        hechos.append('rango de la serie MPR fijado en Registro_de_codigos.md: MPR-001 a %s' % codigos[-1])
        if aplicar:
            L.escribir(L.RUTA_REGISTRO, nuevo)

    for carpeta in L.carpetas_fuera_del_mapa():
        avisos.append('%s existe pero no figura en el mapa de procesos: no se borra, decide el usuario' % carpeta)

    print(('Despliegue aplicado.' if aplicar else 'Modo comprobación: no se ha escrito nada.')
          + ' %d macroproceso(s) en el mapa.' % len(mapa))
    for h in hechos or ['nada que hacer: el sistema ya está desplegado según el mapa']:
        print('  + ' + h)
    for a in avisos:
        print('  ! ' + a)
    return 0


if __name__ == '__main__':
    sys.exit(main())
