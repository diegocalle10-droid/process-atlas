"""PostToolUse (Bash|PowerShell). Las copias y movimientos hechos por shell (cp, mv,
Move-Item…) no pasan por pre_escritura.py ni post_escritura.py. Este hook barre todas las
carpetas MPR_NNN/ (árbol pequeño: barrer es barato), inscribe los códigos válidos que falten
y avisa de los inválidos, que no se pueden deshacer porque la operación ya ocurrió.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib_sistema as L  # noqa: E402


def main():
    try:
        registrados, anomalias = [], []
        for _, carpeta in L.carpetas_mpr():
            for dirpath, _, filenames in os.walk(carpeta):
                for nombre in sorted(filenames):
                    ruta = os.path.join(dirpath, nombre)
                    accion, motivo = L.sincronizar(ruta)
                    if accion == 'Registrado':
                        registrados.append(L.ruta_relativa(ruta))
                    elif accion == 'Anomalia':
                        anomalias.append(motivo)
        partes = []
        if registrados:
            partes.append('Registro de códigos: inscritos tras operación de shell: ' + '; '.join(registrados))
        if anomalias:
            partes.append('AVISO registro de códigos, revisar antes de seguir: ' + ' | '.join(anomalias))
        if partes:
            L.salida_hook({'systemMessage': ' -- '.join(partes)})
    except Exception:
        pass


if __name__ == '__main__':
    main()
