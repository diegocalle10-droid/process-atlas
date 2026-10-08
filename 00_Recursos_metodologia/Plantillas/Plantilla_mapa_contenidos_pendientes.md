# Plantilla de mapa de contenidos pendientes

Modelo de estructura para `00_Mapa_contenidos_pendientes.md`, documento único ubicado en la raíz del repositorio. Lo crea el despliegue (función F0).

**Reglas de uso:**

- Cada fila es un **contenido** de rigor que el sistema todavía no cubre: un ámbito que ningún documento regula o una relación con un macroproceso aún no redactado. Acabará en un `MPR`, un `PRC`, un `MAN` o un anexo.
- No entran las tareas de sesión ni los apartados pendientes de un documento en curso: esos se marcan *(Pendiente de desarrollo)* en el propio documento y se siguen en los inventarios de los crudos.
- Se consulta al iniciar un macroproceso. Una fila se añade al detectar el hueco y se retira cuando su contenido queda redactado.

---

```markdown
# Mapa de contenidos pendientes — {{ORG_NOMBRE}}

Registro, por macroproceso, de los contenidos transversales que el sistema documental todavía no cubre: ámbitos que ningún documento regula y relaciones con macroprocesos aún no redactados. Cada fila es un contenido que acabará en un `MPR`, un `PRC`, un `MAN` o un anexo, no una tarea.

No entran aquí las tareas de sesión ni los apartados pendientes de un documento en curso: esos se marcan *(Pendiente de desarrollo)* en el propio documento y se siguen en los inventarios de los crudos. Una fila se retira cuando su contenido queda redactado en el documento que le corresponde.

**Última actualización:** [dd/mm/aaaa]

---

## 1. Contenidos pendientes por macroproceso

| Macroproceso | Contenido pendiente | Dónde se manifiesta | Origen |
|---|---|---|---|
| MPR-NNN | [contenido que falta] | [documento y apartado] | [usuario y fecha, o relación prevista del mapa local] |

[Si no existen: «Sin contenidos pendientes registrados.»]
```
