---
name: desplegar-sistema
description: Arranque y despliegue del sistema de procesos (función F0). Recaba por preguntas el perfil de la organización, ayuda a declarar el mapa de procesos y ejecuta el despliegue, que sustituye los marcadores del sistema y crea una carpeta MPR_NNN/ por macroproceso con sus procedimientos, manuales y mapa local, además de los mapas de la raíz y la bandeja. Úsala en el primer uso del repositorio, cuando el triaje indique F0 o cuando cambie el perfil o el mapa de procesos.
when_to_use: Primer arranque de un repositorio recién clonado; triaje con F0 pendiente; añadir un macroproceso al mapa; completar una respuesta del perfil.
---

# Desplegar el sistema — función F0

Esta skill convierte el repositorio genérico en el sistema de procesos de una organización concreta. No redacta ningún `MPR`, `PRC` ni `MAN`: deja preparado el terreno para hacerlo (función F4).

Documentos que intervienen:

- `00_Recursos_metodologia/Metodologia/00_Perfil_organizacion.md`: preguntas con identificador (`P-01`…) y marcador. Cada marcador aparece en los documentos del sistema y se sustituye por su respuesta.
- `00_Recursos_metodologia/Metodologia/00_Mapa_procesos.md`: código, nombre y tipo de cada macroproceso.
- `.claude/scripts/desplegar_sistema.py`: el motor. Con `--comprobar` informa sin escribir.

## Flujo

### 1. Situar

Ejecuta `python .claude/scripts/desplegar_sistema.py --comprobar` y lee el resultado junto con el triaje. Te dice qué preguntas faltan, si el mapa es válido y qué se crearía. Si el sistema ya está desplegado y no hay cambios, dilo y termina.

### 2. Perfil de la organización

Por cada pregunta sin respuesta, en el orden de sus identificadores:

1. Hazla citando su identificador: «P-02. ¿A qué se dedica la organización?…». Una pregunta cada vez; si el usuario prefiere responder varias de golpe, acéptalo.
2. Escribe la respuesta en la columna «Respuesta» de su fila, literal: con la grafía, las mayúsculas y las tildes que da el usuario. No la mejores, no la completes, no la traduzcas.
3. Una pregunta opcional que el usuario no quiere responder se deja vacía: el despliegue la convertirá en *(Pendiente de desarrollo)*.

Nunca propongas una respuesta como si fuera un dato de la organización. Si el usuario pide un ejemplo, dalo como ejemplo, marcado como tal, y espera su respuesta.

### 3. Mapa de procesos

1. Pide al usuario la lista de sus macroprocesos: cómo los llama y de qué tipo es cada uno (`Estratégico`, `Operativo` o `Soporte`). Basta con eso: las áreas, actividades y relaciones se documentan después.
2. Si no conoce el tipo, explícale en una frase cada uno, pero la clasificación la decide él.
3. Asigna los códigos `MPR-001`, `MPR-002`… correlativos, en el orden que dé el usuario, y escribe una fila por macroproceso en la tabla del apartado 1.
4. Si pide ayuda para identificar sus macroprocesos, puedes proponer una lista, presentada como propuesta `[INFERENCIA — BAJA]`, con su base. No se escribe en el mapa nada que no haya confirmado.
5. Muestra la tabla final y pide confirmación antes de desplegar.

Si el mapa ya estaba desplegado y se añade un macroproceso, va al final con el siguiente código. Un código existente no se reasigna a otro macroproceso.

### 4. Desplegar

1. Ejecuta de nuevo `--comprobar` y presenta al usuario lo que se va a crear.
2. Con su conformidad, ejecuta `python .claude/scripts/desplegar_sistema.py`.
3. Si el script responde «BLOQUEADO», explica cada motivo y vuelve al paso que corresponda. No edites los documentos del sistema a mano para sortear el bloqueo.

### 5. Cerrar

Informa al usuario de:

- los marcadores sustituidos y las carpetas creadas;
- las carpetas `MPR_NNN/` que existen pero ya no figuran en el mapa: el despliegue no las borra, decide el usuario;
- los siguientes pasos: redactar el primer macroproceso (F4, `Orquestador.md` §2.1) o dejar el material de una reunión en `En_proceso/` (F1).

## Límites

- El despliegue nunca borra: ni carpetas, ni documentos, ni filas del registro de códigos.
- La sustitución de marcadores se hace una sola vez. Si después cambia un dato del perfil, se corrige en los documentos que lo usan (función F2) y se actualiza su respuesta en el perfil.
- Los nombres de área no forman parte del perfil ni del mapa: se fijan con el usuario al redactar cada documento (`Metodologia_de_redaccion.md` §10.2).
