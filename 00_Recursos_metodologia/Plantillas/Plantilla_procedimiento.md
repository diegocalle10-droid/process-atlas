# Plantilla de procedimiento

Modelo de estructura para todo documento `PRC-NNN`. Se copia íntegra y se sustituye cada campo entre corchetes.

**Antes de redactar:** leer `Metodologia_de_redaccion.md` (qué contiene cada nodo y cuándo está completo), `Sistema_de_nomenclatura.md` (códigos y títulos) y `Metodologia_de_relaciones.md` (referencias). Todo contenido se redacta con la skill `estilo-redaccion`.

**Reglas de uso:**

- Los nodos numerados son fijos: existen siempre y conservan su número, incluidas las actuaciones prohibidas del apartado 5.
- Un nodo que no aplica se conserva con `*No aplica* — [justificación]`.
- Un nodo sin información se marca `*(Pendiente de desarrollo)*`.
- La versión se numera según `Sistema_de_nomenclatura.md` §6.4 (`0.N` en curso, `1.0` en versión definitiva) y se registra en la tabla del 7.4.
- El contenido añadido al bloque 2 se numera desde 2.7; nunca entre nodos fijos.
- El detalle de las actividades es el de una instrucción de trabajo, con las dimensiones de la columna PRC de `Metodologia_de_redaccion.md` §6.8.
- Las referencias nunca van dentro de la frase ni de una celda: van en una línea propia tras el párrafo, el paso o la tabla, y apuntan al apartado donde se desarrolla el contenido (`Metodologia_de_relaciones.md` §4.4 y §4.5).
- La numeración correlativa de `PRC` es global: el código se toma del registro de códigos y se inscribe en él como último paso de la creación.
- El Anexo 1 es estándar: la ficha técnica del procedimiento, generada con `Plantilla_ficha_tecnica.md` solo en la versión definitiva; mientras tanto se conserva *(Pendiente de desarrollo)*. Los anexos adicionales empiezan en el 2.

---

```markdown
# PRC-NNN – Procedimiento de [acción] de [objeto]

---

## 1. Identificación del procedimiento

**1.1. Nombre del procedimiento:** [nombre literal del título, sin código]

**1.2. Tipo de procedimiento:** [Procedimiento operativo | Procedimiento de soporte | Procedimiento estratégico]

**1.3. Código del procedimiento:** PRC-NNN

---

## 2. Definición del procedimiento

### 2.1. Definición

[Qué es el procedimiento y qué función cumple. Arranca nombrando el tipo: «Procedimiento operativo que establece…». Declara a qué macroproceso pertenece y qué actividad desarrolla, con referencia resoluble al apartado del macroproceso.]

### 2.2. Objetivo

[Resultado que el procedimiento garantiza. Arranca con verbo en infinitivo: «Garantizar que…».]

### 2.3. Alcance

[Delimitación del procedimiento: objeto al que aplica y, si no hereda del macroproceso, las demás dimensiones.]

**Excepciones:** [excepciones declaradas, o «No existen excepciones.»]

### 2.4. Inicio del procedimiento

[Evento concreto que abre el procedimiento: qué acción, quién la ejecuta, en qué sistema y qué la determina.]

### 2.5. Fin del procedimiento

[Evento concreto que cierra el procedimiento, coherente con el alcance declarado en 2.3.]

### 2.6. Entradas y salidas del procedimiento

[Párrafo de encuadre.]

| Actividad | Entrada | Origen de la entrada | Salida | Destino de la salida |
|---|---|---|---|---|
| [nombre literal del 3.1] | [un único activo de información] | [persona, canal o sistema, con su ubicación] | [resultado generado] | [sistema con su ruta completa, o persona o área que lo recibe] |

[Bloque 2.7 en adelante: contenido añadido cuando el procedimiento lo requiere.]

### 2.7. Principios [opcional]

- **[Nombre del principio]:** [regla en frase imperativa que ninguna actividad puede contravenir]

### 2.8. Marco conceptual [opcional]

[Tablas maestras, tipologías, correlaciones o definiciones propias que las actividades necesitan para ejecutarse. Preferentemente en tablas.]

---

## 3. Descripción de actividades principales

[Párrafo que sitúa el conjunto de actividades y, si procede, declara qué se ejecuta en paralelo o en distinto orden según el caso.]

### 3.1. Listado de actividades

#### 3.1.1. [Actividad] *(crítico)*

[Detalle de ejecución con las dimensiones de la columna PRC de `Metodologia_de_redaccion.md` §6.8. Alguien sin experiencia previa debe poder ejecutarla siguiendo el texto. Cada paso nombra la acción, el sistema y el lugar exactos, en prosa continua.]

1. [Paso ejecutable.]

   *Referencia:* [qué aporta el destino], [[archivo#encabezado|CÓDIGO §apartado]]

[Si falta contenido: *(Pendiente de desarrollo)* y, debajo, el mapa de preguntas `# | Dimensión | Pregunta | Respuesta`.]

##### 3.1.1.1. [Subpaso] [opcional]

[…]

#### 3.1.2. [Actividad]

[…]

---

## 4. Riesgos y controles asociados

[Párrafo que sitúa dónde se concentran los riesgos de la ejecución.]

| # | Riesgo | Causa | Impacto | Probabilidad | Control preventivo | Control detectivo |
|---|---|---|---|---|---|---|
| R1 | [riesgo] | [causa] | [Crítico \| Alto \| Medio \| Bajo] | [Alta \| Media \| Baja] | [control] | [control] |

---

## 5. Actuaciones prohibidas

Quedan expresamente prohibidas las siguientes actuaciones en la ejecución del presente procedimiento:

- [acción concreta prohibida]

[Consecuencia del incumplimiento y área a la que se reporta la incidencia.]

[Si no existen prohibiciones: «*No aplica* — [justificación]».]

---

## 6. Registros generados del procedimiento

La ejecución del presente procedimiento genera los siguientes registros:

| Actividad | Registro | Sistema | Generación | Custodia |
|---|---|---|---|---|
| [nombre literal del 3.1] | [registro] | [sistema] | [cuándo y cómo se genera] | [dónde y quién lo custodia] |

---

## 7. Control documental del procedimiento

El presente apartado establece los criterios de control, mantenimiento y actualización del procedimiento PRC-NNN, garantizando su vigencia, trazabilidad y correcta gestión dentro del sistema de calidad de la organización.

### 7.1. Propietario del procedimiento

Responsable de asegurar la vigencia del contenido, promover su correcta aplicación y coordinar futuras revisiones del documento.

**Propietario:** [área]

### 7.2. Responsables de revisión

Participan en la revisión periódica del procedimiento para asegurar su alineación con la evolución de herramientas, normativa y modelo operativo.

Áreas involucradas:
- [área]

### 7.3. Periodicidad de revisión

El procedimiento será revisado:

- De forma ordinaria: **[periodicidad]**.
- De forma extraordinaria cuando ocurra alguna de las siguientes situaciones:
  - [desencadenante]

### 7.4. Control de versiones

Toda modificación del documento deberá quedar registrada mediante control de versiones, indicando:

- Versión
- Fecha de actualización
- Descripción del cambio
- Responsable de la modificación

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| [0.1] | [dd/mm/aaaa] | [descripción] | [área o persona] |

### 7.5. Ubicación y acceso

La versión vigente del procedimiento se encuentra disponible en el repositorio documental corporativo, siendo la única versión válida para su aplicación.

### 7.6. Elaboración, revisión y aprobación

La versión vigente del procedimiento ha sido elaborada, revisada y aprobada por:

| Rol | Área o persona | Fecha |
|---|---|---|
| Elaborado por | [área o persona] | [dd/mm/aaaa] |
| Revisado por | [área o persona] | [dd/mm/aaaa] |
| Aprobado por | [área o persona] | [dd/mm/aaaa] |

---

## Anexos

### Anexo 1. Ficha técnica del procedimiento

*(Pendiente de desarrollo)* [Se genera con `Plantillas/Plantilla_ficha_tecnica.md` solo cuando el documento se aprueba como versión definitiva. Solo resume: no contiene información ausente del cuerpo.]

### Anexo 2. [Nombre] [opcional]

[Tablas maestras extensas, diagramas o ejemplos.]
```
