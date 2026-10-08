# Ejemplos

Organizaciones ficticias para ver el despliegue funcionando sin tocar tus datos. Cualquier parecido con una organización real es casual.

## `panaderia/` — Panadería La Espiga

Perfil respondido y mapa de cinco macroprocesos de un obrador artesanal ficticio.

Para probarlo en una copia del repositorio (nunca en el repositorio donde documentas tu organización):

1. Copia `panaderia/00_Perfil_organizacion.md` y `panaderia/00_Mapa_procesos.md` sobre los de `00_Recursos_metodologia/Metodologia/`.
2. Ejecuta `python .claude/scripts/desplegar_sistema.py --comprobar` para ver qué haría.
3. Ejecuta `python .claude/scripts/desplegar_sistema.py` para desplegar.

Las pruebas automáticas de `tests/` hacen exactamente esto en una carpeta temporal.
