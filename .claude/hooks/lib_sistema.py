"""Librería común de process-atlas.

Una sola definición de cómo se leen el registro de códigos, el mapa de procesos, el perfil de
la organización y la tabla de glosas del orquestador, y de cómo se decide si un archivo
pertenece a un macroproceso. La cargan los hooks de .claude/hooks/ y los scripts de
.claude/scripts/. Solo usa la biblioteca estándar de Python (3.9 o superior).
"""
import datetime
import fnmatch
import hashlib
import json
import os
import re
import sys

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
RECURSOS = '00_Recursos_metodologia'
RUTA_REGISTRO = os.path.join(RAIZ, RECURSOS, 'Nomenclatura', 'Registro_de_codigos.md')
RUTA_MAPA = os.path.join(RAIZ, RECURSOS, 'Metodologia', '00_Mapa_procesos.md')
RUTA_PERFIL = os.path.join(RAIZ, RECURSOS, 'Metodologia', '00_Perfil_organizacion.md')
RUTA_ORQUESTADOR = os.path.join(RAIZ, RECURSOS, 'Orquestador.md')
RUTA_ARBOL = os.path.join(RAIZ, RECURSOS, 'Arbol_del_proyecto.md')
RUTA_FICHAS = os.path.join(RAIZ, RECURSOS, 'Tablas', 'Tabla_de_fichas.md')
RUTA_PLANTILLAS = os.path.join(RAIZ, RECURSOS, 'Plantillas')
RUTA_ESTADO = os.path.join(RAIZ, '.claude', 'hooks', '.state')

RE_CARPETA_MPR = re.compile(r'^MPR_(\d{3})$')
RE_MARCADOR = re.compile(r'\{\{([A-Z][A-Z0-9_]*)\}\}')
EXCLUIDOS = {'.git', '.state', '__pycache__', 'node_modules', '.venv', 'settings.local.json', '.gitkeep'}
SECCION_REGISTRO = {'MPR': 4, 'PRC': 5, 'MAN': 6}
COLUMNAS_REGISTRO = {4: 5, 5: 6, 6: 6}
SUBCARPETA = {'PRC': 'Procedimientos', 'MAN': 'Manuales'}
TIPOS_MPR = {'estrategico': 'Estratégico', 'operativo': 'Operativo', 'soporte': 'Soporte'}
SIN_GLOSA = '\u2014'


# ---------------------------------------------------------------- E/S y rutas

def leer(ruta):
    with open(ruta, encoding='utf-8-sig', newline='') as f:
        return f.read()


def escribir(ruta, texto):
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    with open(ruta, 'w', encoding='utf-8', newline='') as f:
        f.write(texto)


def hoy():
    return datetime.date.today().strftime('%d/%m/%Y')


def ruta_relativa(ruta):
    """Ruta relativa a la raíz con «/», o None si el archivo está fuera del repositorio."""
    try:
        rel = os.path.relpath(os.path.abspath(ruta), RAIZ)
    except ValueError:  # otra unidad en Windows
        return None
    rel = rel.replace(os.sep, '/')
    if rel == '.' or rel.startswith('../') or rel == '..':
        return None
    return rel


def macroproceso_de(ruta):
    """Número del macroproceso si el PRIMER segmento de la ruta es una carpeta MPR_NNN.

    Solo cuenta la carpeta de primer nivel: un archivo de En_proceso/ cuyo nombre contenga
    «MPR_001» no pertenece a ningún macroproceso.
    """
    rel = ruta_relativa(ruta)
    if not rel:
        return None
    m = RE_CARPETA_MPR.match(rel.split('/')[0])
    return int(m.group(1)) if m else None


def carpetas_mpr():
    """Carpetas MPR_NNN existentes en la raíz, ordenadas: [(n, ruta absoluta)]."""
    salida = []
    for nombre in os.listdir(RAIZ):
        m = RE_CARPETA_MPR.match(nombre)
        if m and os.path.isdir(os.path.join(RAIZ, nombre)):
            salida.append((int(m.group(1)), os.path.join(RAIZ, nombre)))
    return sorted(salida)


def salida_hook(datos):
    sys.stdout.write(json.dumps(datos, ensure_ascii=True))
    sys.stdout.flush()


def leer_evento():
    crudo = sys.stdin.buffer.read().decode('utf-8', errors='replace')
    return json.loads(crudo) if crudo.strip() else {}


# ---------------------------------------------------------------- tablas markdown

def celdas(linea):
    """Celdas de una fila de tabla. Respeta las barras escapadas de los enlaces [[a\\|b]]."""
    contenido = linea.strip()
    if contenido.startswith('|'):
        contenido = contenido[1:]
    if contenido.endswith('|') and not contenido.endswith('\\|'):
        contenido = contenido[:-1]
    return [c.strip() for c in re.split(r'(?<!\\)\|', contenido)]


def seccion(texto, numero):
    """Texto del bloque «## N.» hasta el siguiente encabezado de nivel 2."""
    m = re.search(r'(?ms)^## %s\..*?(?=^## |\Z)' % re.escape(str(numero)), texto)
    return m.group(0) if m else ''


def primera_tabla(bloque):
    """(cabecera, filas) de la primera tabla del bloque. Filas sin el separador."""
    lineas, dentro = [], False
    for linea in bloque.splitlines():
        if linea.lstrip().startswith('|'):
            lineas.append(linea)
            dentro = True
        elif dentro:
            break
    if len(lineas) < 2:
        return None, []
    filas = [celdas(l) for l in lineas[2:]]
    return celdas(lineas[0]), [f for f in filas if any(f)]


def sin_tildes(texto):
    import unicodedata
    d = unicodedata.normalize('NFD', texto)
    return ''.join(c for c in d if unicodedata.category(c) != 'Mn').lower().strip()


# ---------------------------------------------------------------- mapa de procesos

def macroprocesos_del_mapa():
    """Filas del mapa de procesos: [{'n', 'codigo', 'nombre', 'tipo'}]. Lista vacía si no hay."""
    if not os.path.exists(RUTA_MAPA):
        return []
    cabecera, filas = primera_tabla(seccion(leer(RUTA_MAPA), 1))
    if not cabecera:
        return []
    salida = []
    for f in filas:
        f = (f + ['', '', ''])[:3]
        m = re.fullmatch(r'`?MPR-(\d{3})`?', f[0])
        if not m and not f[1]:
            continue
        salida.append({'n': int(m.group(1)) if m else None, 'codigo': f[0].strip('`'),
                       'nombre': f[1], 'tipo': f[2]})
    return salida


def validar_mapa(filas):
    """Errores del mapa: códigos MPR-NNN correlativos desde 001, nombre y tipo admitido."""
    errores = []
    if not filas:
        return ['el mapa de procesos no tiene ningún macroproceso']
    esperado = 1
    for f in filas:
        if f['n'] is None:
            errores.append('código no válido «%s» (formato MPR-NNN)' % f['codigo'])
            continue
        if f['n'] != esperado:
            errores.append('%s: se esperaba MPR-%03d (correlativos desde MPR-001, sin huecos)' % (f['codigo'], esperado))
        esperado = f['n'] + 1
        if not f['nombre']:
            errores.append('%s: falta el nombre' % f['codigo'])
        if sin_tildes(f['tipo']) not in TIPOS_MPR:
            errores.append('%s: tipo «%s» no admitido (Estratégico, Operativo o Soporte)' % (f['codigo'], f['tipo']))
    return errores


# ---------------------------------------------------------------- perfil de la organización

def preguntas_del_perfil():
    """Filas del perfil: [{'id', 'marcador', 'pregunta', 'obligatoria', 'respuesta'}]."""
    if not os.path.exists(RUTA_PERFIL):
        return []
    cabecera, filas = primera_tabla(seccion(leer(RUTA_PERFIL), 1))
    salida = []
    for f in filas:
        f = (f + [''] * 5)[:5]
        m = RE_MARCADOR.search(f[1])
        if not m:
            continue
        respuesta = f[4]
        if re.fullmatch(r'\*?\(?pendiente.*', sin_tildes(respuesta)):
            respuesta = ''
        salida.append({'id': f[0], 'marcador': m.group(1), 'pregunta': f[2],
                       'obligatoria': sin_tildes(f[3]).startswith('s'), 'respuesta': respuesta})
    return salida


def archivos_con_marcadores():
    """Archivos .md del sistema (.claude/ y 00_Recursos_metodologia/) que conservan marcadores."""
    salida = {}
    for base in ('.claude', RECURSOS):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, base)):
            dirnames[:] = [d for d in dirnames if d not in EXCLUIDOS]
            for nombre in filenames:
                ruta = os.path.join(dirpath, nombre)
                if not nombre.endswith('.md') or os.path.abspath(ruta) == os.path.abspath(RUTA_PERFIL):
                    continue
                encontrados = sorted(set(RE_MARCADOR.findall(leer(ruta))))
                if encontrados:
                    salida[ruta_relativa(ruta)] = encontrados
    return salida


# ---------------------------------------------------------------- registro de códigos

def codigo_desde_nombre(nombre):
    """(prefijo, número) del nombre de archivo, o None.

    PRC y MAN llevan descriptor tras el código (PRC_001_alta_clientes.md). El documento del
    macroproceso es MPR_NNN.md a secas: MPR_NNN_mapa_relaciones.md no es un código.
    """
    base = os.path.splitext(nombre)[0]
    m = re.match(r'^(MPR|PRC|MAN)_(\d{3})(?:_|$)', base)
    if not m:
        return None
    if m.group(1) == 'MPR' and base != 'MPR_%s' % m.group(2):
        return None
    return m.group(1), int(m.group(2))


def guion(prefijo, numero):
    return '%s-%03d' % (prefijo, numero)


def filas_registro(texto, prefijo):
    cabecera, filas = primera_tabla(seccion(texto, SECCION_REGISTRO[prefijo]))
    return [f for f in filas if re.fullmatch(r'`?%s-\d{3}`?' % prefijo, f[0])]


def numeros_registrados(texto, prefijo):
    return {int(f[0].strip('`')[4:]): f for f in filas_registro(texto, prefijo)}


def siguiente_disponible(texto, prefijo):
    usados = numeros_registrados(texto, prefijo)
    return (max(usados) if usados else 0) + 1


def titulo_desde_archivo(ruta):
    try:
        primera = leer(ruta).splitlines()[0]
    except (IndexError, OSError):
        return ''
    m = re.match(r'^#\s*[A-Z]{3}-\d{3}\s*[\u2013\u2014-]\s*(.+)$', primera)
    return (m.group(1) if m else re.sub(r'^#\s*', '', primera)).strip()


def estado_codigo(ruta, texto_registro=None, mapa=None):
    """Diagnóstico de solo lectura de un archivo frente al registro.

    Devuelve (accion, motivo, codigo). accion: Fuera (no pertenece a un macroproceso o no es
    un documento), Ignorado (mapa local), YaRegistrado, PorRegistrar o Anomalia.
    """
    n = macroproceso_de(ruta)
    nombre = os.path.basename(ruta)
    if n is None or not nombre.endswith('.md'):
        return 'Fuera', '', None
    partes = ruta_relativa(ruta).split('/')
    if nombre == 'MPR_%03d_mapa_relaciones.md' % n and len(partes) == 2:
        return 'Ignorado', '', None
    codigo = codigo_desde_nombre(nombre)
    if not codigo:
        return 'Anomalia', 'archivo dentro de un macroproceso sin prefijo de código válido (MPR_NNN, PRC_NNN_…, MAN_NNN_…): %s' % ruta_relativa(ruta), None
    prefijo, numero = codigo
    cg = guion(prefijo, numero)
    if prefijo == 'MPR':
        if len(partes) != 2:
            return 'Anomalia', '%s debe estar en la raíz de su carpeta MPR_%03d/' % (cg, n), cg
        if numero != n:
            return 'Anomalia', 'el código %s no coincide con la carpeta MPR_%03d que lo contiene' % (cg, n), cg
    elif len(partes) != 3 or partes[1] != SUBCARPETA[prefijo]:
        return 'Anomalia', '%s debe estar en MPR_%03d/%s/' % (cg, n, SUBCARPETA[prefijo]), cg
    texto = texto_registro if texto_registro is not None else (leer(RUTA_REGISTRO) if os.path.exists(RUTA_REGISTRO) else None)
    if texto is None:
        return 'Anomalia', 'no se encuentra Registro_de_codigos.md', cg
    if numero in numeros_registrados(texto, prefijo):
        return 'YaRegistrado', '', cg
    if prefijo == 'MPR':
        mapa = mapa if mapa is not None else macroprocesos_del_mapa()
        if numero not in {f['n'] for f in mapa}:
            return 'Anomalia', '%s no figura en el mapa de procesos (00_Mapa_procesos.md)' % cg, cg
        return 'PorRegistrar', '', cg
    esperado = siguiente_disponible(texto, prefijo)
    if numero != esperado:
        return 'Anomalia', 'el código %s no es el siguiente disponible de la serie %s; siguiente disponible: %s' % (cg, prefijo, guion(prefijo, esperado)), cg
    return 'PorRegistrar', '', cg


def control_de_series(texto, mapa=None):
    """Reescribe la tabla del apartado 2 del registro a partir de las tablas 4–6 y del mapa."""
    mapa = mapa if mapa is not None else macroprocesos_del_mapa()
    numeros = [f['n'] for f in mapa if f['n']]
    rango_mpr = ('`MPR-001` a `%s` (fijado por el mapa de procesos)' % guion('MPR', max(numeros))) if numeros else '*(Pendiente de desarrollo)*: lo fija el mapa de procesos'
    filas = []
    for prefijo in ('MPR', 'PRC', 'MAN'):
        usados = numeros_registrados(texto, prefijo)
        ultimo = guion(prefijo, max(usados)) if usados else '\u2014'
        if prefijo == 'MPR':
            filas.append('| `MPR` | %s | %s | \u2014 |' % (rango_mpr, ultimo))
        else:
            filas.append('| `%s` | `%s-001` en adelante | %s | %s |' % (prefijo, prefijo, ultimo, guion(prefijo, siguiente_disponible(texto, prefijo))))
    tabla = '| Serie | Rango | Último código emitido | Siguiente disponible |\n|---|---|---|---|\n' + '\n'.join(filas)
    bloque = seccion(texto, 2)
    if not bloque:
        return texto
    nuevo_bloque = re.sub(r'(?m)(^\|.*\n?)+', tabla + '\n', bloque, count=1)
    return texto.replace(bloque, nuevo_bloque, 1)


def inscribir(ruta, codigo):
    """Añade la fila del código a su tabla, recalcula el control de series y la fecha."""
    texto = leer(RUTA_REGISTRO)
    prefijo = codigo[:3]
    numero = int(codigo[4:])
    if numero in numeros_registrados(texto, prefijo):
        return False
    titulo = titulo_desde_archivo(ruta).replace('|', '\\|')
    if prefijo == 'MPR':
        fila = '| %s | %s | En curso | %s | |' % (codigo, titulo, hoy())
    else:
        fila = '| %s | %s | %s | En curso | %s | |' % (codigo, titulo, guion('MPR', macroproceso_de(ruta)), hoy())
    bloque = seccion(texto, SECCION_REGISTRO[prefijo])
    lineas = bloque.split('\n')
    ultima = max(i for i, l in enumerate(lineas) if l.lstrip().startswith('|'))
    lineas.insert(ultima + 1, fila)
    texto = texto.replace(bloque, '\n'.join(lineas), 1)
    texto = control_de_series(texto)
    texto = re.sub(r'(?m)^\*\*Última actualización:\*\*.*$', '**Última actualización:** ' + hoy(), texto)
    escribir(RUTA_REGISTRO, texto)
    return True


def sincronizar(ruta):
    """Inscribe el código si es válido y falta; devuelve (accion, motivo)."""
    accion, motivo, codigo = estado_codigo(ruta)
    if accion == 'PorRegistrar':
        inscribir(ruta, codigo)
        return 'Registrado', ''
    return accion, motivo


def legibilidad_registro():
    problemas = []
    if not os.path.exists(RUTA_REGISTRO):
        return ['no se encuentra Registro_de_codigos.md']
    texto = leer(RUTA_REGISTRO)
    for sec, n in COLUMNAS_REGISTRO.items():
        cabecera, _ = primera_tabla(seccion(texto, sec))
        if not cabecera:
            problemas.append('Registro de códigos: no se encuentra la tabla del apartado %d' % sec)
        elif len(cabecera) != n:
            problemas.append('Registro de códigos: la tabla del apartado %d tiene %d columnas (se esperan %d)' % (sec, len(cabecera), n))
    return problemas


# ---------------------------------------------------------------- glosas del orquestador

def glosas_orquestador():
    """Filas del apartado 1 de Orquestador.md: [(ruta o patrón, glosa)]."""
    if not os.path.exists(RUTA_ORQUESTADOR):
        return []
    cabecera, filas = primera_tabla(seccion(leer(RUTA_ORQUESTADOR), 1))
    salida = []
    for f in filas:
        if len(f) < 4:
            continue
        ruta = f[3].strip('` ')
        if ruta and ruta != 'Ruta':
            salida.append((ruta, f[2]))
    return salida


def glosa_de(rel, glosas):
    """Glosa de una ruta relativa (las carpetas terminan en «/»).

    Coincidencia exacta primero y después patrón. None si no hay fila o la glosa es una raya.
    Los archivos de En_proceso/ son transitorios: devuelven '' (sin glosa, sin aviso), salvo
    los que tienen fila exacta (Procesado/).
    """
    fila = next((g for r, g in glosas if r == rel), None)
    if fila is None and rel.startswith('En_proceso/') and rel != 'En_proceso/':
        return ''
    if fila is None:
        fila = next((g for r, g in glosas if fnmatch.fnmatchcase(rel, r)), None)
    if not fila or fila == SIN_GLOSA:
        return None
    return fila


# ---------------------------------------------------------------- marcas de pre-escritura

def ruta_marca(ruta):
    clave = os.path.normcase(os.path.abspath(ruta)).encode('utf-8')
    return os.path.join(RUTA_ESTADO, hashlib.md5(clave).hexdigest() + '.marker')


def ambito_normalizacion(ruta):
    """El nombre se normaliza en el árbol documental: 00_Recursos_metodologia/, las carpetas
    MPR_NNN/ y los documentos 00_ de la raíz. Quedan fuera .claude/, En_proceso/ y los
    archivos del repositorio (README, licencias, tests, ejemplos…)."""
    rel = ruta_relativa(ruta)
    if not rel:
        return False
    primero = rel.split('/')[0]
    if '/' not in rel:
        return primero.startswith('00_')
    return primero == RECURSOS or bool(RE_CARPETA_MPR.match(primero))


# ---------------------------------------------------------------- estado del arranque (F0)

ARCHIVOS_RAIZ_DESPLIEGUE = ['00_Mapa_global_relaciones.md', '00_Mapa_contenidos_pendientes.md']


def pendientes_arranque():
    """Lo que falta para que el sistema esté desplegado (función F0). Lista vacía si nada."""
    pendientes = []
    preguntas = preguntas_del_perfil()
    if not preguntas:
        pendientes.append('no se puede leer el perfil de la organización (00_Perfil_organizacion.md)')
    sin_responder = [p['id'] for p in preguntas if p['obligatoria'] and not p['respuesta']]
    if sin_responder:
        pendientes.append('preguntas obligatorias del perfil sin responder: ' + ', '.join(sin_responder))
    marcadores = archivos_con_marcadores()
    if marcadores:
        pendientes.append('marcadores {{…}} sin sustituir en %d archivo(s) del sistema' % len(marcadores))
    mapa = macroprocesos_del_mapa()
    errores = validar_mapa(mapa)
    if errores:
        pendientes.append('mapa de procesos: ' + '; '.join(errores))
    else:
        for f in mapa:
            carpeta = os.path.join(RAIZ, 'MPR_%03d' % f['n'])
            necesarios = [carpeta, os.path.join(carpeta, 'Procedimientos'), os.path.join(carpeta, 'Manuales'),
                          os.path.join(carpeta, 'MPR_%03d_mapa_relaciones.md' % f['n'])]
            if not all(os.path.exists(r) for r in necesarios):
                pendientes.append('%s figura en el mapa pero su carpeta no está desplegada completa' % f['codigo'])
    faltan = [a for a in ARCHIVOS_RAIZ_DESPLIEGUE if not os.path.exists(os.path.join(RAIZ, a))]
    if not os.path.isdir(os.path.join(RAIZ, 'En_proceso', 'Procesado')):
        faltan.append('En_proceso/Procesado/')
    if faltan:
        pendientes.append('falta(n) en la raíz: ' + ', '.join(faltan))
    return pendientes


def carpetas_fuera_del_mapa():
    en_mapa = {f['n'] for f in macroprocesos_del_mapa()}
    return ['MPR_%03d/' % n for n, _ in carpetas_mpr() if n not in en_mapa]
