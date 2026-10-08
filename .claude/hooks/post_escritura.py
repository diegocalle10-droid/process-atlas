"""PostToolUse (Write). Tras escribir un archivo:

1. Consume siempre la marca de pre_escritura.py, antes de cualquier otra comprobación, para
   que no queden marcas huérfanas en .claude/hooks/.state/.
2. Si el archivo es un documento de una carpeta MPR_NNN/ con código válido y aún no
   inscrito, lo inscribe en Registro_de_codigos.md (último paso de la creación). Si el
   código es inválido, avisa: la escritura ya ocurrió y no se deshace.
3. Si el archivo es nuevo y está en el ámbito de la nomenclatura (00_Recursos_metodologia/,
   MPR_NNN/ y documentos 00_ de la raíz), normaliza su nombre según
   Sistema_de_nomenclatura.md §5.2.1 e informa de la ruta nueva.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_sistema as L  # noqa: E402


def nombre_normalizado(nombre):
    base, ext = os.path.splitext(nombre)
    norm = re.sub(r'[\s\-]+', '_', base)
    norm = re.sub(r'_+', '_', norm).strip('_')
    m = re.match(r'^(MPR|PRC|MAN)_?([0-9]+)_?(.*)$', norm, re.IGNORECASE)
    if m:
        resto = re.sub(r'_+', '_', m.group(3).lower()).strip('_')
        nuevo = '%s_%s' % (m.group(1).upper(), m.group(2)) + ('_' + resto if resto else '')
    else:
        m = re.match(r'^([0-9]+_)(.*)$', norm)
        prefijo, resto = (m.group(1), m.group(2)) if m else ('', norm)
        resto = resto.lower()
        nuevo = prefijo + resto[:1].upper() + resto[1:]
    return nuevo + ext.lower()


def main():
    try:
        ruta = (L.leer_evento().get('tool_input') or {}).get('file_path')
        if not ruta:
            return
        marca = L.ruta_marca(ruta)
        es_nuevo = False
        if os.path.exists(marca):
            with open(marca, encoding='utf-8') as f:
                es_nuevo = f.read().strip() == 'NEW'
            os.remove(marca)
        if not os.path.isfile(ruta):
            return
        mensajes, contexto = [], None
        accion, motivo = L.sincronizar(ruta)
        if accion == 'Registrado':
            mensajes.append('Código inscrito en Registro_de_codigos.md: ' + L.ruta_relativa(ruta))
        elif accion == 'Anomalia':
            mensajes.append('AVISO registro de códigos: ' + motivo)
        if es_nuevo and L.ambito_normalizacion(ruta):
            nombre = os.path.basename(ruta)
            nuevo = nombre_normalizado(nombre)
            destino = os.path.join(os.path.dirname(ruta), nuevo)
            if nuevo != nombre and not os.path.exists(destino):
                os.rename(ruta, destino)
                mensajes.append('Archivo renombrado por la regla de nomenclatura: %s -> %s' % (nombre, nuevo))
                contexto = ('El archivo recién creado «%s» se ha renombrado a «%s» (ruta: %s) según '
                            'Sistema_de_nomenclatura.md §5.2.1. Usa esa ruta en lecturas y ediciones posteriores.'
                            % (nombre, nuevo, destino))
        if mensajes:
            datos = {'systemMessage': ' -- '.join(mensajes)}
            if contexto:
                datos['hookSpecificOutput'] = {'hookEventName': 'PostToolUse', 'additionalContext': contexto}
            L.salida_hook(datos)
    except Exception:
        pass


if __name__ == '__main__':
    main()
