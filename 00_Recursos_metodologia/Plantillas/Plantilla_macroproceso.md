# Plantilla de macroproceso

Modelo de estructura para todo documento `MPR-NNN`. Se copia íntegra y se sustituye cada campo entre corchetes.

**Antes de redactar:** leer `Metodologia_de_redaccion.md` (qué contiene cada nodo y cuándo está completo), `Sistema_de_nomenclatura.md` (códigos y títulos) y `Metodologia_de_relaciones.md` (referencias). Todo contenido se redacta con la skill `estilo-redaccion`.

**Reglas de uso:**

- Los nodos numerados son fijos: existen siempre y conservan su número.
- Un nodo que no aplica se conserva con `*No aplica* — [justificación]`.
- Un nodo sin información se marca `*(Pendiente de desarrollo)*`.
- La versión se numera según `Sistema_de_nomenclatura.md` §6.4 (`0.N` en curso, `1.0` en versión definitiva) y se registra en la tabla del 8.4.
- El contenido añadido al bloque 2 se numera desde 2.7; nunca entre nodos fijos.
- Los anexos 1, 2 y 3 son estándar. Los adicionales empiezan en el 4. El Anexo 2 se genera con `Plantilla_ficha_tecnica.md` solo en la versión definitiva; mientras tanto se conserva *(Pendiente de desarrollo)*.
- Si las actividades principales todavía no están identificadas, se diagnostican antes de redactar el apartado 3 con `Plantilla_matriz_actividades.md` (herramienta de trabajo, no se conserva como anexo).
- El código `MPR` lo asigna el mapa de procesos y su carpeta la crea el despliegue; el documento se inscribe igualmente en el registro de códigos al crearse.
- Las referencias nunca van dentro de la frase ni de una celda del cuerpo: van en una línea propia tras el párrafo o la tabla, y apuntan al procedimiento que desarrolla el contenido, o lo nombran como pendiente de redactar (`Metodologia_de_relaciones.md` §4.4 y §4.5). El Anexo 3 y los mapas de relaciones sí llevan el enlace en la celda.
- La tabla del 2.6 tiene cinco columnas y una fila por entrada (`Metodologia_de_redaccion.md` §6.6).

---

```markdown
# MPR-NNN – Macroproceso [tipo] de [acción] de [objeto] para [ámbito] en {{ORG_NOMBRE}}

---

## 1. Identificación del proceso

**1.1. Nombre del proceso:** [nombre literal del título, sin código]

**1.2. Tipo de proceso:** [Macroproceso operativo | Macroproceso de soporte | Macroproceso estratégico]

**1.3. Código de proceso:** MPR-NNN

---

## 2. Definición del proceso

### 2.1. Definición

[Qué es el macroproceso y qué función cumple en el sistema. Arranca nombrando el tipo: «Macroproceso orientado a…». No incluye beneficios ni límites.]

### 2.2. Objetivo

[Resultado que el macroproceso garantiza. Arranca con verbo en infinitivo: «Garantizar que…». Debe permitir derivar al menos un indicador del apartado 6.]

[Si hay varios beneficios separables:]
- **[Beneficio]:** [descripción]

### 2.3. Alcance

[Delimitación explícita en las dimensiones que apliquen:]

- **Objeto:** [a qué unidades aplica]
- **Funcional:** [qué funciones abarca]
- **Organizacional:** [áreas implicadas]
- **Tecnológico:** [sistemas corporativos]
- **Temporal:** [fase o ciclo de vida]

**Excepciones:** [excepciones declaradas, o «No existen excepciones.»]

### 2.4. Inicio del proceso

[Evento concreto que abre el proceso: qué acción, quién la ejecuta, en qué sistema y qué la determina.]

### 2.5. Fin del proceso

[Evento concreto que cierra el proceso, coherente con el alcance declarado en 2.3.]

### 2.6. Entradas y salidas del proceso

[Párrafo de encuadre. Las entradas y salidas se registran como activos de información, no como datos o campos concretos.]

| Actividad | Entrada | Origen de la entrada | Salida | Destino de la salida |
|---|---|---|---|---|
| [nombre literal del 3.1] | [un único activo de información] | [persona, canal o sistema, con su ubicación] | [resultado generado] | [sistema con su ruta completa, o persona o área que lo recibe] |

[Bloque 2.7 en adelante: contenido añadido cuando el macroproceso lo requiere.]

### 2.7. Principios [opcional]

- **[Nombre del principio]:** [regla en frase imperativa]

### 2.8. Marco conceptual [opcional]

[Tablas maestras, tipologías o definiciones propias que las actividades necesitan para ejecutarse.]

---

## 3. Descripción de actividades principales

[Párrafo que sitúa el conjunto de actividades y, si procede, declara qué se ejecuta en paralelo o en distinto orden según el caso.]

### 3.1. Listado de actividades

#### 3.1.1. [Actividad en infinitivo] *(crítico)*

[Uno a tres párrafos con las dimensiones de la columna MPR de `Metodologia_de_redaccion.md` §6.8. No se detallan pasos: el detalle vive en el procedimiento.]

#### 3.1.2. [Actividad en infinitivo]

[…]

---

## 4. Procedimientos asociados al proceso

[Párrafo que explica que cada procedimiento desarrolla el cómo de una actividad del apartado 3.1.]

### 4.1. Mapa de procedimientos

| Actividad | Procedimiento | Código |
|---|---|---|
| [nombre literal e idéntico al del 3.1] | [título literal del procedimiento] | PRC-NNN |
| [actividad sin procedimiento] | *(Pendiente de desarrollo)* | *(Pendiente de desarrollo)* |

---

## 5. Riesgos y controles asociados

[Párrafo que sitúa dónde se concentran los riesgos del macroproceso.]

| Categoría | Actividad | Riesgo potencial | Impacto | Probabilidad | Controles asociados |
|---|---|---|---|---|---|
| [categoría] | [nombre literal del 3.1] | [riesgo] | [Crítico \| Alto \| Medio \| Bajo] | [Alta \| Media \| Baja] | [control identificable] |

---

## 6. Indicadores KPIs

[Párrafo que declara la finalidad del sistema de indicadores del macroproceso. Cada indicador es propio de este proceso: no se hereda de ningún otro.]

### 6.1. [Nombre del indicador] (KPI-MPR-NNN-01)

**Qué mide:** [una línea]

**Fórmula:**

> [expresión de cálculo]

**Definición de términos:**

- **[Término]:** [definición]

**Periodicidad de medición:** [periodicidad]

**Periodicidad de reporte:** [periodicidad]

### 6.2. [Nombre del indicador] (KPI-MPR-NNN-02)

[…]

---

## 7. Registros generados del proceso

[Párrafo de encuadre.]

### 7.1. Tipología de registros generados

**[Categoría de registro]**

[Una línea que declara qué evidencia esta categoría.]

- [registro]

### 7.2. Custodia y disponibilidad

[Dónde se custodian los registros, quién accede a ellos y bajo qué condiciones de conservación y disponibilidad.]

---

## 8. Control documental del macroproceso

El presente apartado establece los criterios de control, mantenimiento y actualización del macroproceso MPR-NNN, garantizando su vigencia, trazabilidad y correcta gestión dentro del sistema de calidad de la organización.

### 8.1. Propietario del proceso

Responsable de asegurar la vigencia del contenido, promover su correcta aplicación y coordinar futuras revisiones del documento.

**Propietario:** [área]

### 8.2. Responsables de revisión

Participan en la revisión periódica del macroproceso para asegurar su alineación con la evolución de herramientas, normativa y modelo operativo.

Áreas involucradas:
- [área]

### 8.3. Periodicidad de revisión

El macroproceso será revisado:

- De forma ordinaria: **[periodicidad]**.
- De forma extraordinaria cuando ocurra alguna de las siguientes situaciones:
  - [desencadenante]

### 8.4. Control de versiones

Toda modificación del documento deberá quedar registrada mediante control de versiones, indicando:

- Versión
- Fecha de actualización
- Descripción del cambio
- Responsable de la modificación

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| [0.1] | [dd/mm/aaaa] | [descripción] | [área o persona] |

### 8.5. Ubicación y acceso

La versión vigente del macroproceso se encuentra disponible en el repositorio documental corporativo, siendo la única versión válida para su aplicación.

### 8.6. Elaboración, revisión y aprobación

La versión vigente del macroproceso ha sido elaborada, revisada y aprobada por:

| Rol | Área o persona | Fecha |
|---|---|---|
| Elaborado por | [área o persona] | [dd/mm/aaaa] |
| Revisado por | [área o persona] | [dd/mm/aaaa] |
| Aprobado por | [área o persona] | [dd/mm/aaaa] |

---

## Anexos

### Anexo 1. Matriz RASCI – MPR-NNN

La matriz RASCI identifica, para cada actividad del macroproceso, qué área ejecuta, aprueba, apoya, es consultada y es informada.

**Actores**

| Actor | Función en el macroproceso |
|---|---|
| [área] | [función] |

**Roles**

| Rol | Nombre | Definición |
|---|---|---|
| R | Responsable | Persona o área que realiza el trabajo de forma directa. Puede haber más de un R por actividad. |
| A | Aprobador | Quien rinde cuentas del resultado y tiene la autoridad final para aprobar o rechazar. Solo puede haber uno por actividad. |
| S | Soporte | Quien asiste o apoya al responsable durante la ejecución, aportando recursos, datos o capacidad operativa. No decide, pero su participación es necesaria. |
| C | Consultado | Quien debe ser consultado antes o durante la actividad. La comunicación es bidireccional. Su opinión influye en la ejecución. |
| I | Informado | Quien debe ser notificado del resultado una vez la actividad termina. La comunicación es unidireccional: recibe, no interviene. |

**Reglas de aplicación**

- Solo un actor con rol A por actividad.
- Toda actividad tiene al menos un R.
- Un exceso de C e I en una misma fila indica exceso de comunicación o actores innecesarios.

**Matriz**

| Cód. | Actividad del macroproceso | [área] | [área] | [área] |
|---|---|---|---|---|
| PRC-NNN | [nombre literal del 3.1] | R | A | I |

### Anexo 2. Ficha técnica del macroproceso

*(Pendiente de desarrollo)* [Se genera con `Plantillas/Plantilla_ficha_tecnica.md` solo cuando el documento se aprueba como versión definitiva. Solo resume: no contiene información ausente del cuerpo.]

### Anexo 3. Relación de fichas de procedimientos adheridos

| Código | Procedimiento | Ficha |
|---|---|---|
| PRC-NNN | [título literal del procedimiento, en el mismo orden que 4.1] | [[PRC_NNN_descriptor#Anexo 1. Ficha técnica del procedimiento\|PRC-NNN Anexo 1]] |
| *(Pendiente de desarrollo)* | [actividad sin procedimiento] | *(Pendiente de desarrollo)* |

### Anexo 4. [Nombre] [opcional]

[Diagramas BPMN 2.0, mapas de interrelaciones, matrices vinculantes o ejemplos.]
```
