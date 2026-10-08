# Perfil de la organización

Datos de la organización que adaptan el sistema a ella. Cada pregunta tiene un identificador y un marcador: el marcador aparece en los documentos del sistema (`.claude/` y `00_Recursos_metodologia/`) y el despliegue lo sustituye por la respuesta (función F0, `Orquestador.md` §3).

**Cómo se rellena:** con la skill `desplegar-sistema` (`/desplegar-sistema`), que hace las preguntas una a una y anota aquí cada respuesta, o a mano, escribiendo la respuesta en su columna. Después se ejecuta el despliegue.

**Reglas:**

- Una pregunta obligatoria sin respuesta bloquea el despliegue.
- Una pregunta opcional sin respuesta se sustituye por *(Pendiente de desarrollo)*.
- La respuesta se escribe tal como debe aparecer en los documentos: grafía, mayúsculas y tildes incluidas.
- La sustitución se hace una sola vez. Si después cambia un dato, se corrige en los documentos que lo usan (función F2) y se actualiza aquí la respuesta, para que el perfil siga siendo la fuente.
- Las filas, los identificadores y los marcadores no se renombran: el despliegue los lee por su posición y su forma.

---

## 1. Preguntas

| ID | Marcador | Pregunta | Obligatoria | Respuesta |
|---|---|---|---|---|
| P-01 | `{{ORG_NOMBRE}}` | ¿Cómo se llama la organización, tal como debe aparecer en los documentos? | Sí | |
| P-02 | `{{ORG_ACTIVIDAD}}` | ¿A qué se dedica? Sector y actividad principal en una o dos frases. | Sí | |
| P-03 | `{{ORG_AREA_PROCESOS}}` | ¿Qué área o persona es propietaria del sistema documental de procesos (metodología, plantillas y registro de códigos)? | Sí | |
| P-04 | `{{ORG_IDIOMA}}` | ¿En qué variante del español se redactan los documentos? Por ejemplo: «español de España», «español de México». | Sí | |
| P-05 | `{{ORG_MARCO}}` | ¿Qué marcos de referencia aplica la organización? Si no hay preferencia: «ISO 9001, BPMN 2.0 e ISO 27000». | Sí | |
| P-06 | `{{ORG_SISTEMAS}}` | ¿Qué sistemas corporativos usa (aplicaciones, plataformas, bases de datos) y cómo se escribe oficialmente cada uno? Separados por punto y coma. | No | |
| P-07 | `{{ORG_UNIDADES}}` | ¿Qué unidades o magnitudes propias del negocio aparecen en los procesos y cómo se escriben? Por ejemplo: «superficie: `ha`». Separadas por punto y coma. | No | |

---

## 2. Control documental

**Propietario:** el área o la persona que responde la pregunta P-03.

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
