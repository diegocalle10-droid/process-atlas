# Plantilla de manual

Modelo de estructura para todo documento `MAN-NNN`. Se copia y se sustituye cada campo entre corchetes.

**Antes de redactar:** leer `Metodologia_de_redaccion.md` §9 (reglas del manual), `Sistema_de_nomenclatura.md` (códigos y títulos) y `Metodologia_de_relaciones.md` (referencias). Todo contenido se redacta con la skill `estilo-redaccion`.

**Reglas de uso:**

- El manual se dirige a quien usa un sistema o una estructura. Se redacta en **segunda persona del singular**, a diferencia de los `MPR` y `PRC`, que son impersonales.
- La estructura del cuerpo es **libre**: se organiza por lo que el usuario necesita hacer. Solo son obligatorios el bloque de cabecera, el apartado 1, el control documental como último apartado y el Anexo 1 (ficha técnica del manual, generada con `Plantilla_ficha_tecnica.md` solo en la versión definitiva).
- La versión se numera según `Sistema_de_nomenclatura.md` §6.4 y se registra en la tabla del control documental.
- **El manual no crea reglas.** Toda regla que contenga debe existir en el procedimiento o macroproceso de referencia. Si manual y procedimiento discrepan, prevalece el procedimiento.
- Los apartados intermedios de esta plantilla son un armazón habitual, no obligatorio: se añaden, se reordenan o se omiten según el objeto del manual.
- La numeración correlativa de `MAN` es global, igual que la de `PRC`: el código se toma del registro de códigos y se inscribe en él como último paso de la creación.

---

```markdown
# MAN-NNN – Manual de [finalidad] — [objeto]

**Documento:** [nombre del manual]
**Versión:** [versión]
**Propietario:** [área]
**Repositorio:** [ubicación]

---

## 1. Propósito del documento

[Qué explica este manual, a quién se dirige y por qué conviene leerlo antes de operar. Declara el macroproceso al que pertenece y los procedimientos que explica, con referencia resoluble.]

---

## 2. [Contexto o estructura del sistema] [habitual]

[Qué es aquello que vas a usar y cómo está organizado. Conviene antes de cualquier instrucción: sin el mapa mental, los pasos no se entienden.]

---

## 3. [Cómo hacer cada cosa] [habitual]

[Uno o varios apartados organizados por tarea del usuario, no por estructura del sistema. Cada tarea explica qué hacer, dónde y con qué criterio.]

### 3.1. [Tarea]

[Instrucciones en segunda persona: «Abre…», «Selecciona…», «Comprueba que…».]

---

## 4. Reglas de uso [habitual]

**Lo que nunca debes hacer**

- [acción prohibida]

**Lo que siempre debes hacer**

- [acción obligatoria]

[Estas reglas proceden del procedimiento de referencia; aquí se expresan en lenguaje de uso, sin alterar su contenido.]

---

## 5. Resolución de incidencias [habitual]

| Situación | Qué hacer | A quién acudir |
|---|---|---|
| [situación] | [acción] | [área] |

---

## 6. Instrucciones para agentes de IA [opcional]

[Se incluye solo cuando el manual también sirve como fuente de conocimiento para un agente. Indica cómo debe interpretar el contenido y qué límites tiene.]

---

## [N]. Control documental

| Campo | Valor |
|---|---|
| Propietario | [área] |
| Revisión ordinaria | [periodicidad] |
| Revisión extraordinaria | [desencadenantes] |
| Versión | [versión] |
| Ubicación | [ruta en el repositorio] |
| Elaborado por | [área o persona] — [dd/mm/aaaa] |
| Revisado por | [área o persona] — [dd/mm/aaaa] |
| Aprobado por | [área o persona] — [dd/mm/aaaa] |

Toda modificación del documento deberá quedar registrada mediante control de versiones, indicando versión, fecha de actualización, descripción del cambio y responsable de la modificación.

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| [0.1] | [dd/mm/aaaa] | [descripción] | [área o persona] |

---

## Anexos

### Anexo 1. Ficha técnica del manual

*(Pendiente de desarrollo)* [Se genera con `Plantillas/Plantilla_ficha_tecnica.md` solo cuando el manual se aprueba como versión definitiva. Solo resume: no contiene información ausente del manual.]
```
