# Sistema de nomenclatura — {{ORG_NOMBRE}}

---

## 1. Propósito y alcance

Este documento define de forma exhaustiva cómo se nombra todo elemento del sistema de procesos de {{ORG_NOMBRE}}: los documentos, sus archivos, sus carpetas, sus apartados y los identificadores internos que contienen.

Desarrolla en detalle lo que la `Metodologia_de_redaccion.md` establece a grandes rasgos. Ante cualquier duda de nombrado, este documento es la referencia.

**Alcance:** documentos del sistema de procesos (macroprocesos, procedimientos y manuales), sus archivos y carpetas en el repositorio, y los identificadores internos que generan.

**Fuera de alcance:** el nombrado de los documentos operativos que genera la actividad de la organización —contratos, actas, informes, registros de trabajo—, que se rige por sus propias reglas (§9).

---

## 2. Principios

1. **Identificación autónoma.** Un nombre debe permitir saber qué es el elemento sin abrirlo y sin conocer su ubicación.
2. **Unicidad.** Un código identifica un único elemento en todo el sistema, de forma permanente.
3. **Estabilidad.** Un nombre asignado no cambia por conveniencia. Si cambia, lo hace por un motivo documentado en el control de versiones.
4. **Predictibilidad.** Dado el tipo de elemento, su nombre se deduce aplicando la regla, sin criterio personal.
5. **Separación de planos.** El código identifica; el nombre describe. Nunca se sustituyen entre sí.

---

## 3. Códigos de documento

### 3.1. Estructura

`[PREFIJO]-[NNN]`

| Prefijo | Nivel documental | Rango |
|---|---|---|
| `MPR` | Macroproceso | `MPR-001` a `MPR-999`, según el mapa de procesos |
| `PRC` | Procedimiento | `PRC-001` en adelante |
| `MAN` | Manual | `MAN-001` en adelante |

Reglas:

- Prefijo siempre en mayúsculas, tres letras.
- Número siempre de tres dígitos, con ceros a la izquierda: `PRC-007`, nunca `PRC-7`.
- No existen otros prefijos. Cualquier documento que no sea macroproceso, procedimiento o manual no recibe código de este sistema.

### 3.2. Asignación

- **Macroprocesos:** los códigos los asigna el mapa de procesos (`00_Mapa_procesos.md`), correlativos desde `MPR-001`. No se emite un código `MPR` que no figure en el mapa: para añadir un macroproceso se añade su fila al mapa y se despliega.
- **Procedimientos y manuales:** numeración **correlativa global**. La serie es única para todo el proyecto y no se reinicia al cambiar de macroproceso. `PRC` y `MAN` mantienen series independientes entre sí.
- **Antes de asignar un código** se consulta el registro de códigos (§3.4) y se toma el siguiente disponible de la serie. Nunca se deduce del contenido del repositorio, del contexto ni de la continuidad aparente de la numeración.
- **Un código emitido no se reutiliza ni se reasigna**, aunque el documento se retire, se anule o nunca llegue a redactarse.
- **No existen códigos provisionales.** Un documento aún no creado se referencia como *(Pendiente de desarrollo)*, nunca como `PRC-00X`, `PRC-XXX` o equivalentes.

### 3.3. Separador según contexto

| Contexto | Forma | Ejemplo |
|---|---|---|
| Contenido de los documentos: títulos, apartados, tablas, referencias, texto corrido | Guion medio | `MPR-001`, `PRC-005` |
| Nombres de archivo y de carpeta | Guion bajo | `MPR_001`, `PRC_005` |

En el repositorio, el guion medio no se usa nunca como separador de nombres de archivo o carpeta. Dentro del contenido de un documento sí puede aparecer con su función ortográfica normal.

### 3.4. Registro de códigos

Todos los códigos emitidos se inscriben en `00_Recursos_metodologia/Nomenclatura/Registro_de_codigos.md`. Es la única fuente de verdad sobre qué códigos existen, cuál es el último emitido de cada serie y cuál es el siguiente disponible.

**Por qué existe.** El repositorio solo muestra los documentos que existen en un momento dado. Un código retirado, anulado o asignado a un documento que nunca llegó a redactarse desaparece del árbol, y con él la constancia de que fue emitido. Sin un registro independiente del repositorio, la prohibición de reutilizar códigos no puede cumplirse: nada distingue un código libre de un código consumido. El registro conserva ese historial y mantiene el inventario de identificadores permanentemente actualizado.

**Procedimiento.** La creación de cualquier documento con código (`MPR`, `PRC`, `MAN`) sigue siempre estos tres pasos, en este orden:

1. **Consultar.** Antes de nombrar nada, se abre el registro y se identifica el siguiente código disponible de la serie.
2. **Asignar.** Se usa exactamente ese código en el título, en el nombre de archivo y en cualquier referencia.
3. **Registrar.** Como último paso obligatorio de la creación, una vez el documento existe, se graba en el registro el código emitido, con su título, macroproceso, estado, fecha de emisión y observaciones, y se actualiza el control de series. La creación no está terminada mientras su código no esté registrado.

Este procedimiento está automatizado: un hook determinista valida el código antes de que el documento se cree dentro de una carpeta `MPR_NNN/` y lo inscribe en el registro justo después. La regla no depende de que quien redacta recuerde ejecutarla.

**Reglas de integridad.**

- El registro es acumulativo: no se eliminan filas ni se modifican los códigos ya inscritos. Un documento retirado o anulado cambia de estado; no desaparece.
- Antes de asignar, se comprueba que ningún archivo del repositorio lleve un código ausente del registro. Si existe, hay una discrepancia: se inscribe ese código o se comunica la incidencia, y no se asigna ningún código nuevo hasta resolverla.
- Las altas y los cambios de estado no generan versión nueva del registro; solo los cambios de su estructura o de sus reglas.
- Los identificadores internos del apartado 6.2 (indicadores, riesgos, anexos) no forman parte de este sistema de códigos y no se registran.

---

## 4. Título del documento

El título es la primera línea del archivo, con encabezado `#`, y sigue la fórmula:

`[CÓDIGO] – [Nombre del documento]`

El separador entre código y nombre es una raya (`–`), con espacio a cada lado.

### 4.1. Construcción del nombre

| Componente | Función | Obligatorio en |
|---|---|---|
| Tipo de documento y nivel | Sitúa el documento en la arquitectura. | Todos |
| Acción rectora sustantivada | Define la acción o propósito global. | Todos |
| Objeto de gestión | Indica qué se gestiona, transforma o explica. | Todos |
| Ámbito | Delimita la unidad de análisis. | MPR; opcional en PRC y MAN |
| Organización | Cierra el nombre. | MPR |

### 4.2. Fórmula por nivel

**Macroproceso**

`MPR-NNN – Macroproceso [tipo] de [acción] de [objeto] para [ámbito] en {{ORG_NOMBRE}}`

```
MPR-001 – Macroproceso estratégico de planificación y dirección de la actividad en {{ORG_NOMBRE}}
MPR-002 – Macroproceso operativo de gestión comercial de clientes y pedidos en {{ORG_NOMBRE}}
```

**Procedimiento**

`PRC-NNN – Procedimiento de [acción] de [objeto]`

```
PRC-001 – Procedimiento de alta de clientes y verificación de sus datos
PRC-004 – Procedimiento de registro de pedidos en el ERP
```

**Manual**

`MAN-NNN – Manual de [finalidad] — [objeto]`

```
MAN-001 – Manual de uso — Estructura de carpetas del repositorio documental
```

### 4.3. Reglas de redacción del nombre

- Mayúscula inicial solo en la primera palabra y en nombres propios de sistemas o áreas.
- Acción rectora en forma sustantivada: «gestión», «captación», «alta», «registro», «control». No en infinitivo.
- El nombre describe el objeto, no la herramienta, salvo que la herramienta sea el objeto del documento (`PRC-004`, `MAN-001`).
- Sin abreviaturas, sin siglas no corporativas, sin versiones, sin fechas.
- El apartado 1.1 del documento reproduce este nombre de forma literal, sin el código.

### 4.4. Nombre en el mapa de procesos

La columna «Nombre» del mapa de procesos (`00_Mapa_procesos.md`) arranca con el nombre con el que la organización conoce el macroproceso, para que el despliegue sea ligero. Al redactar el `MPR-NNN` se construye su título con la fórmula del §4.2 y, en el mismo cambio, la columna se actualiza con ese nombre, en prosa y sin el código. No es un slug ni usa guion bajo. Desde entonces se mantiene sincronizada con el título real.

---

## 5. Nombres de archivo y carpeta

### 5.1. Reglas generales

- Separador: guion bajo. Nunca espacios, guiones medios ni puntos intermedios.
- Sin tildes ni `ñ`: `Metodologia`, no `Metodología`; `Diseno`, no `Diseño`.
- Sin caracteres especiales: `/ \ : * ? " < > | # % & { } $ ! ' @ + ´ =`.
- Extensión de los documentos del sistema: `.md`.
- Los nombres de carpeta y archivo no llevan versión ni fecha. El control de versiones vive dentro del documento.

### 5.2. Capitalización

Regla única: **mayúscula inicial solo en la primera palabra; el resto del nombre, en minúsculas.** La única excepción son los prefijos de código `MPR`, `PRC` y `MAN`, que van siempre en mayúsculas.

| Elemento | Convención | Ejemplo |
|---|---|---|
| Carpetas | Inicial mayúscula, resto en minúsculas | `00_Recursos_metodologia`, `Procedimientos`, `Manuales` |
| Documentos del sistema (MPR, PRC, MAN) | Código en mayúsculas + resto en minúsculas | `PRC_001_alta_clientes.md` |
| Documentos de recursos y metodología | Inicial mayúscula, resto en minúsculas | `Metodologia_de_redaccion.md`, `Arbol_del_proyecto.md` |
| Documentos de orden fijo en la raíz de una carpeta | Prefijo numérico `00_` + inicial mayúscula | `00_Mapa_procesos.md`, `00_Mapa_global_relaciones.md` |

Queda prohibida la capitalización de cada palabra significativa: `Metodologia_de_Redaccion.md` es incorrecto; `Metodologia_de_redaccion.md` es correcto.

El prefijo `00_` se reserva para documentos que deben aparecer primero en la ordenación alfabética de su carpeta por ser el punto de entrada a su contenido.

### 5.2.1. Normalización automática

El repositorio dispone de un hook de tipo *posttool* (`.claude/hooks/post_escritura.py`) que se dispara al crear un archivo del árbol documental y normaliza su nombre. El árbol documental es `00_Recursos_metodologia/`, las carpetas `MPR_NNN/` y los documentos `00_` de la raíz. Queda fuera la carpeta `.claude/`: sus archivos (agentes, skills, hooks, configuración) siguen las convenciones propias de Claude Code. Queda fuera la bandeja `En_proceso/`: los crudos llegan con su propio nombre y su archivo de inventario lo conserva como prefijo. Quedan fuera los archivos propios del repositorio (`README.md`, licencias, pruebas y ejemplos).

- Sustituye los espacios por guion bajo.
- Pasa a minúsculas todo el nombre salvo el segmento de código (`MPR`, `PRC`, `MAN`) y la inicial de la primera palabra.

El hook es una red de seguridad, no un sustituto de la regla: los nombres se escriben ya correctos en origen.

### 5.3. Nombres por tipo de elemento

| Elemento | Patrón | Ejemplo |
|---|---|---|
| Carpeta de macroproceso | `MPR_NNN` | `MPR_001` |
| Documento de macroproceso | `MPR_NNN.md` | `MPR_001.md` |
| Mapa de relaciones de macroproceso | `MPR_NNN_mapa_relaciones.md` | `MPR_001_mapa_relaciones.md` |
| Procedimiento | `PRC_NNN_[descriptor].md` | `PRC_001_alta_clientes.md` |
| Manual | `MAN_NNN_[descriptor].md` | `MAN_001_estructura_carpetas.md` |
| Mapa global de relaciones | `00_Mapa_global_relaciones.md` | — |
| Mapa de procesos | `00_Mapa_procesos.md` | — |
| Perfil de la organización | `00_Perfil_organizacion.md` | — |
| Mapa de contenidos pendientes | `00_Mapa_contenidos_pendientes.md` | — |
| Plantilla de documento | `Plantilla_[tipo].md` | `Plantilla_macroproceso.md` |
| Tabla maestra | `Tabla_[objeto].md` | `Tabla_de_fichas.md` |
| Bandeja de entrada | `En_proceso` | — |
| Crudos procesados | `En_proceso/Procesado` | — |
| Inventario de extracción de un crudo | `[nombre del crudo sin extensión]_inventario.md`, junto al crudo | `Reunion_ventas_inventario.md` |

### 5.4. Descriptor del nombre de archivo

En procedimientos y manuales, el descriptor es la versión abreviada del nombre del título:

- Máximo cuatro palabras, en minúsculas y separadas por guion bajo.
- Recoge la esencia del documento, no su tipo genérico: `alta_clientes`, no `procedimiento_alta`.
- Omite artículos, preposiciones y conectores: `registro_pedidos_erp`, no `registro_de_los_pedidos_en_el_erp`.
- Se mantiene estable aunque el título se matice, salvo que el objeto del documento cambie.

| Título | Descriptor correcto | Descriptor incorrecto |
|---|---|---|
| `PRC-001 – Procedimiento de alta de clientes y verificación de sus datos` | `alta_clientes` | `procedimiento_prc001` |
| `PRC-004 – Procedimiento de registro de pedidos en el ERP` | `registro_pedidos_erp` | `pedidos_v2` |
| `MAN-001 – Manual de uso — Estructura de carpetas del repositorio documental` | `estructura_carpetas` | `manual_carpetas` |

---

## 6. Nomenclatura interna de los documentos

### 6.1. Apartados

- Encabezados de bloque: `## N. Nombre del bloque`.
- Subapartados: `### N.N. Nombre`, `#### N.N.N. Nombre`, `##### N.N.N.N. Nombre`.
- La numeración lleva siempre punto final: `2.1.`, `3.1.2.`.
- La profundidad máxima recomendada es de cuatro niveles. Más allá, el contenido se reorganiza o se traslada a un anexo.
- El nombre del apartado es un sintagma nominal, no una frase: «Registros generados del proceso», no «Se generan estos registros».
- Los nodos fijos conservan siempre su número. El contenido añadido se numera a continuación del último nodo fijo de su bloque.

### 6.2. Identificadores internos

| Identificador | Patrón | Ejemplo | Ámbito de unicidad |
|---|---|---|---|
| Indicador (KPI) | `KPI-MPR-NNN-MM` | `KPI-MPR-001-01` | Único en su macroproceso |
| Riesgo | `RN` | `R1`, `R2` | Único en su documento |
| Actividad | Numeración del apartado | `3.1.2` | Único en su documento |
| Anexo | `Anexo N. [Nombre]` | `Anexo 1. Matriz RASCI – MPR-001` | Único en su documento |
| Rol RASCI | Letra única | `R`, `A`, `S`, `C`, `I` | Sistema |

Reglas:

- Los identificadores de riesgo se numeran de forma consecutiva desde `R1` en cada documento, sin saltos.
- Un identificador retirado de un documento vivo no se reutiliza dentro de la misma versión.
- Los anexos estándar mantienen su numeración fija:
  - Macroproceso: `Anexo 1` matriz RASCI, `Anexo 2` ficha técnica, `Anexo 3` relación de fichas de procedimientos adheridos. Los adicionales empiezan en `Anexo 4`.
  - Procedimiento y manual: `Anexo 1` ficha técnica. Los adicionales empiezan en `Anexo 2`.

### 6.3. Marcas de estado

| Marca | Uso |
|---|---|
| `*(Pendiente de desarrollo)*` | Apartado, código o anexo aún sin contenido. |
| `*No aplica* — [justificación]` | Nodo fijo que no corresponde a la naturaleza del documento. |
| `*(crítico)*` | Sufijo en el encabezado de una actividad de criticidad alta. |

### 6.4. Numeración de versiones

La versión de un `MPR`, `PRC` o `MAN` se registra en la tabla de control de versiones de su propio control documental (`MPR` §8.4, `PRC` §7.4, `MAN` último apartado), según `Metodologia_de_redaccion.md` §6.11. No se registra en el nombre del archivo (§5.1).

| Estado del documento | Numeración | Ejemplo |
|---|---|---|
| En curso | `0.1` con la primera versión redactada; cada sesión con cambios suma una décima | `0.1`, `0.2` |
| Versión definitiva | `1.0` al aprobarse por primera vez | `1.0` |
| Revisiones posteriores | Cada sesión con cambios suma una décima; tras la `.9` se pasa a la siguiente unidad | `1.1` … `1.9`, `2.0` |

---

## 7. Nomenclatura de entidades

Las entidades se nombran siempre igual en todo el sistema. Un mismo elemento con dos nombres rompe la coherencia del árbol.

### 7.1. Sistemas corporativos

Se escriben con la grafía oficial que usa la organización, respetando mayúsculas internas. Sistemas declarados en el perfil de la organización:

{{ORG_SISTEMAS}}

La primera mención en un documento puede ir acompañada de una aclaración; las siguientes usan la forma corta. Un sistema que no figura en esta lista se pregunta antes de escribirlo y, confirmada su grafía, se añade aquí.

**Bases de datos y repositorios.** Cuando un mismo sistema aloja varias bases de datos o repositorios, cada uno se nombra en los documentos por su función, no por su nombre técnico ni por el del sistema que lo aloja: el sistema no es una base concreta. La equivalencia se registra aquí la primera vez que aparece:

| Nombre en los documentos | Nombre técnico | Función |
|---|---|---|
| *(Pendiente de desarrollo)* | *(Pendiente de desarrollo)* | *(Pendiente de desarrollo)* |

En la primera mención de un documento puede añadirse el sistema que la aloja.

### 7.2. Unidades y magnitudes

| Magnitud | Forma | Observación |
|---|---|---|
| Unidades propias del negocio | {{ORG_UNIDADES}} | Declaradas en el perfil de la organización. |
| Porcentaje | `%` | Pegado a la cifra. |
| Fechas en contenido | `dd/mm/aaaa` | — |

---

## 8. Referencias entre documentos

La construcción de referencias y enlaces se rige por `00_Recursos_metodologia/Metodologia/Metodologia_de_relaciones.md`.

De este documento se hereda únicamente la forma de nombrar lo referenciado: toda referencia legible identifica el documento por su **código con guion medio** y el apartado por su **numeración con puntos**.

`PRC-001 §3.1.2`, `MPR-002 apartado 4.1`

---

## 9. Documentos operativos de proyecto

Los documentos operativos que genera la actividad de la organización —contratos, actas, informes, registros de trabajo, material audiovisual— **no** siguen este sistema.

---

## 10. Errores frecuentes

1. Usar guion medio en un nombre de archivo o carpeta.
2. Usar guion bajo en un código dentro del contenido de un documento.
3. Escribir el código sin ceros a la izquierda: `PRC-7`.
4. Emitir un código sin consultar el registro de códigos.
5. Reiniciar la numeración de procedimientos al cambiar de macroproceso.
6. Reutilizar el código de un documento retirado.
7. Usar códigos provisionales (`PRC-00X`) en lugar de *(Pendiente de desarrollo)*.
8. Incluir versión o fecha en el nombre del archivo.
9. Usar tildes o `ñ` en nombres de archivo o carpeta.
10. Capitalizar cada palabra significativa de un nombre de archivo o carpeta en lugar de solo la inicial.
11. Que el nombre del apartado 1.1 no coincida literalmente con el del título.
12. Nombrar un mismo sistema de dos formas distintas en el mismo documento.
13. Numerar un anexo estándar fuera de su orden fijo.
14. Aplicar a un documento del sistema de procesos las reglas de nombrado de los documentos operativos de la organización.
15. Deducir el siguiente código del contenido del repositorio en lugar de leerlo del registro de códigos.
16. Dar por terminada la creación de un documento sin haber registrado su código.
17. Modificar o eliminar filas ya inscritas en el registro de códigos.

---

## 11. Control documental

**Propietario:** {{ORG_AREA_PROCESOS}}

**Responsables de revisión:** *(Pendiente de desarrollo)*

**Periodicidad de revisión:** *(Pendiente de desarrollo)*. De forma extraordinaria, ante cualquier cambio en la estructura del repositorio o en la codificación del sistema.

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
