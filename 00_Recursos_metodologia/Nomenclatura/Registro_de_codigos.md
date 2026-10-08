# Registro de códigos — {{ORG_NOMBRE}}

Inventario de todos los códigos emitidos en el sistema de procesos (`MPR`, `PRC`, `MAN`). Es la única fuente de verdad sobre qué códigos existen, cuál es el último emitido de cada serie y cuál es el siguiente disponible.

**Última actualización:** 08/10/2026

---

## 1. Reglas de uso

1. **Consultar antes de asignar.** Antes de nombrar cualquier documento con código se lee el apartado 2 y se toma el siguiente disponible de la serie.
2. **Registrar como último paso.** Una vez creado el documento se graba su código en la tabla de su serie y se actualiza el apartado 2. La creación no está terminada mientras su código no esté aquí.
3. **Registro acumulativo.** No se eliminan filas ni se modifican los códigos ya registrados. Un documento retirado o anulado cambia de estado; no desaparece.
4. **Sin reutilización.** Ningún código registrado, en cualquier estado, se vuelve a asignar.
5. **Discrepancias.** Si el repositorio contiene un código ausente de este registro, se registra ese código o se comunica la discrepancia antes de asignar ninguno nuevo.
6. **Sin versionado por alta.** Las altas y los cambios de estado de este registro no generan nueva versión del documento; solo los cambios de su estructura o de sus reglas.

Las reglas completas están en `Sistema_de_nomenclatura.md` §3.4. Las altas y el apartado 2 los mantienen los hooks de `.claude/hooks/`; el rango de la serie `MPR` lo fija el despliegue a partir del mapa de procesos.

---

## 2. Control de series

| Serie | Rango | Último código emitido | Siguiente disponible |
|---|---|---|---|
| `MPR` | *(Pendiente de desarrollo)*: lo fija el mapa de procesos | — | — |
| `PRC` | `PRC-001` en adelante | — | PRC-001 |
| `MAN` | `MAN-001` en adelante | — | MAN-001 |

---

## 3. Estados

| Estado | Significado |
|---|---|
| En curso | El documento existe y se está desarrollando. |
| Versión definitiva | El documento está completo y validado. |
| Retirado | El documento existió y dejó de estar vigente. El código no se reasigna. |
| Anulado | El código se asignó pero el documento nunca llegó a redactarse. El código no se reasigna. |

---

## 4. Registro de macroprocesos (`MPR`)

| Código | Título del documento | Estado | Fecha de emisión | Observaciones |
|---|---|---|---|---|

---

## 5. Registro de procedimientos (`PRC`)

| Código | Título del documento | Macroproceso | Estado | Fecha de emisión | Observaciones |
|---|---|---|---|---|---|

---

## 6. Registro de manuales (`MAN`)

| Código | Título del documento | Macroproceso | Estado | Fecha de emisión | Observaciones |
|---|---|---|---|---|---|

---

## 7. Control documental

**Propietario:** {{ORG_AREA_PROCESOS}}

**Responsables de revisión:** *(Pendiente de desarrollo)*

**Periodicidad de revisión:** *(Pendiente de desarrollo)*. De forma extraordinaria, ante cualquier cambio en la estructura del registro o en las reglas de asignación.

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
