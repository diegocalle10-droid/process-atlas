"""PreToolUse (Write). Dos funciones antes de que la tool escriba:

1. Bloquea la creación de un documento dentro de una carpeta MPR_NNN/ cuyo código no sea
   válido frente a Registro_de_codigos.md y al mapa de procesos: código duplicado, con
   hueco, en carpeta o subcarpeta equivocada, o macroproceso fuera del mapa. Falla cerrado:
   si la validación no puede ejecutarse, la creación se deniega.
2. Anota si el archivo es nuevo (marca en .claude/hooks/.state/) para que post_escritura.py
   normalice solo los nombres de los archivos recién creados. En NTFS la fecha de creación no
   es fiable para saberlo (tunneling), por eso se anota antes de escribir.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def denegar(motivo):
    sys.stdout.write(json.dumps({'hookSpecificOutput': {
        'hookEventName': 'PreToolUse',
        'permissionDecision': 'deny',
        'permissionDecisionReason': 'Registro de códigos: ' + motivo}}, ensure_ascii=True))


def main():
    ruta = None
    try:
        import lib_sistema as L
        ruta = (L.leer_evento().get('tool_input') or {}).get('file_path')
        if not ruta:
            return
        existe = os.path.exists(ruta)
        if not existe and ruta.endswith('.md') and L.macroproceso_de(ruta) is not None:
            accion, motivo, _ = L.estado_codigo(ruta)
            if accion == 'Anomalia':
                denegar(motivo)
                return
        if L.ambito_normalizacion(ruta):
            os.makedirs(L.RUTA_ESTADO, exist_ok=True)
            with open(L.ruta_marca(ruta), 'w', encoding='utf-8') as f:
                f.write('EXISTING' if existe else 'NEW')
    except Exception as e:
        # Falla cerrado solo cuando la escritura cae dentro de una carpeta de macroproceso.
        if ruta and re.search(r'[\\/]MPR_\d{3}[\\/]', ruta):
            denegar('el hook de validación falló (%s); no se puede verificar el código y la creación se bloquea por seguridad.' % e)


if __name__ == '__main__':
    main()
