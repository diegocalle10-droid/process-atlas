# Metodología de relaciones entre documentos — {{ORG_NOMBRE}}

---

## 1. Propósito

El sistema de procesos de {{ORG_NOMBRE}} no es una colección de documentos independientes: es una red. Un apartado de un procedimiento desarrolla una actividad de un macroproceso; un riesgo se controla mediante una regla declarada en otro documento; una definición vive en un único sitio y se usa desde varios.

Este documento establece cómo se declaran, se escriben y se registran esas relaciones, y cómo se mantienen coherentes en el tiempo.

Es lectura obligatoria antes de crear o modificar cualquier relación entre documentos.

**Alcance:** relaciones entre documentos del sistema de procesos (`MPR`, `PRC`, `MAN`) y entre sus apartados.

**Documento complementario:** las reglas de nombrado de códigos, archivos y apartados están en `00_Recursos_metodologia/Nomenclatura/Sistema_de_nomenclatura.md`. Esta metodología las aplica; no las redefine.

---

## 2. Principios

1. **Una definición, un lugar.** Un concepto, una tabla maestra o una regla se define en un único documento. Los demás la referencian; nunca la reproducen.
2. **Toda relación es explícita.** Si dos documentos dependen entre sí, la dependencia está escrita. Una relación que solo existe en la cabeza de quien redactó no existe.
3. **Toda relación es bidireccional en el registro.** Se escribe en el texto desde un lado, pero queda registrada en los mapas de ambos documentos implicados.
4. **La referencia apunta a un apartado, no a un documento.** Citar un documento entero no informa de nada; citar `PRC-002 §2.7.1` sí.
5. **La relación no sustituye al contenido.** Un documento debe entenderse por sí mismo; la referencia amplía, no completa lo imprescindible.
6. **La referencia evita el desfase de versiones.** Declarar un mismo concepto en dos documentos obliga a actualizar dos orígenes, y cualquier actualización futura que solo alcance a uno deja al otro desfasado sin que nadie lo advierta. La referencia elimina esa brecha: hay un único origen que mantener.

   Esto no contradice el principio 5. Un texto explicativo que sitúa al lector —qué es el concepto, por qué importa aquí— es legítimo y mantiene el documento comprensible por sí mismo. Lo que no se reproduce es el contenido normativo: la definición exacta, la tabla maestra, los valores, los criterios. Explicar no es declarar: el texto explicativo orienta, la referencia aporta el dato vigente.

   Regla práctica: si al cambiar el original habría que cambiar también este texto, entonces es contenido duplicado y debe sustituirse por una referencia.

---

## 3. Tipos de relación

| Tipo | Significado | Dirección | Ejemplo |
|---|---|---|---|
| `desarrolla` | Un procedimiento desarrolla la ejecución de una actividad de un macroproceso. | `PRC` → `MPR` | `PRC-001` desarrolla `MPR-001 §3.1.1` |
| `pertenece a` | Un documento forma parte del ámbito de un macroproceso. | `PRC`/`MAN` → `MPR` | `MAN-001` pertenece a `MPR-001` |
| `precede a` | La ejecución de un documento debe completarse antes que la de otro. | Secuencial | `PRC-001` precede a `PRC-002` |
| `depende de` | Un apartado necesita un dato, estructura o estado producido en otro. | Unidireccional | `PRC-004 §3.1.1` depende de `PRC-002 §2.7.4` |
| `usa definición de` | Un apartado emplea un concepto o tabla maestra definidos en otro. | Unidireccional | `MPR-001 §2.6` usa definición de `PRC-002 §2.7.1` |
| `controla` | Una regla o prohibición de un documento actúa como control de un riesgo de otro. | Unidireccional | `PRC-001 §5` controla `MPR-001 §5` |
| `explica` | Un manual explica el uso operativo de lo regulado en otro documento. | `MAN` → `PRC`/`MPR` | `MAN-001` explica `PRC-005 §2.8` |

Reglas:

- Estos siete tipos son los únicos admitidos. Si una relación no encaja en ninguno, se replantea: probablemente el contenido está mal ubicado.
- Cada tipo tiene un inverso implícito (`desarrolla` / `desarrollado por`, `precede a` / `sigue a`, `depende de` / `da soporte a`). El inverso se registra en el mapa del documento receptor; no se escribe como tipo propio.

---

## 4. Formato de referencia

Cada referencia tiene dos capas que conviven en un único constructo: una legible para una persona y otra resoluble por un sistema de enlaces tipo wiki.

### 4.1. Referencia legible

`[CÓDIGO] §[apartado]`

```
PRC-001 §3.1.2
MPR-002 §4.1
MAN-001 §6
```

- El código va con guion medio, según el `Sistema_de_nomenclatura.md`.
- El símbolo `§` precede siempre al número de apartado, sin espacio entre ambos.
- Para citar un documento completo se omite el `§` y el número: `PRC-001`.
- Un rango de apartados se escribe con guion: `PRC-002 §2.7.1–2.7.4`.

### 4.2. Enlace resoluble

`[[archivo#encabezado|referencia legible]]`

```
[[PRC_001_alta_clientes#3.1.2. Verificación de los datos del cliente|PRC-001 §3.1.2]]
[[MPR_002#4.1. Mapa de procedimientos|MPR-002 §4.1]]
```

- `archivo` es el nombre del archivo sin extensión, tal como lo fija el `Sistema_de_nomenclatura.md`.
- `encabezado` es el texto literal y completo del encabezado destino, incluida su numeración y su punto. Si no coincide exactamente, el enlace no resuelve.
- El texto tras `|` es siempre la referencia legible del apartado anterior. Es lo que ve quien lee.
- Para enlazar un documento completo se omite `#encabezado`: `[[PRC_001_alta_clientes|PRC-001]]`.

### 4.3. Cuál usar

| Contexto | Formato |
|---|---|
| Prosa del cuerpo de un documento (`MPR`, `PRC`, `MAN`) | Enlace resoluble en una línea de referencia propia (§4.4), nunca dentro de la frase |
| Tablas del cuerpo | Ninguno dentro de la celda: la línea de referencia va bajo la tabla. La celda puede nombrar el documento en texto llano («el macroproceso MPR-002») |
| Tablas cuya función es referenciar: mapas de relaciones, mapa de procedimientos (4.1) y Anexo 3 del macroproceso, índice de definiciones compartidas | Enlace resoluble en la celda, siempre |
| Títulos y encabezados | Ninguno: nunca se referencia desde un encabezado |

### 4.4. Línea de referencia

La referencia no se integra en la frase. La prosa se escribe para leerse de corrido, y la referencia va en una línea propia inmediatamente después del párrafo, del paso o de la tabla que sostiene. La línea declara qué aporta el destino y lleva el enlace resoluble:

`*Referencia:* [qué aporta el destino], [[archivo#encabezado|CÓDIGO §apartado]]`

Si son varias, se separan con un punto medio: `*Referencias:* [qué aporta], [[…]] · [qué aporta], [[…]]`. Dentro de un paso numerado, la línea se sangra bajo el paso, como un párrafo propio del mismo punto. Una referencia a un apartado del mismo documento se escribe sin enlace: «*Referencia:* tipos de cliente, 2.7.2».

- Correcto: «*Referencia:* estado Desestimado, [[PRC_003…|PRC-003 §2.8.3]]»
- Incorrecto: «…le asigna el estado Desestimado, que define [[PRC_003…|PRC-003 §2.8.3]], y lo comunica…» (enlace intercalado en la frase).
- Incorrecto: «*Referencia:* [[PRC_003…|PRC-003 §2.8.3]]» (no declara qué aporta el destino).
- Incorrecto: «Ver [[PRC_002…|PRC-002 §3.1.5]].»
- Incorrecto: «Como ya se ha explicado antes.» (referencia implícita, no resoluble)

### 4.5. Destino de la referencia

La referencia apunta al apartado donde el contenido se desarrolla, no al lugar donde solo se enuncia.

- Desde un procedimiento se remite al procedimiento que desarrolla el contenido, nunca a la descripción de una actividad del macroproceso.
- Al macroproceso solo se remite por lo que vive en él: sus principios, sus indicadores, sus riesgos, las definiciones compartidas que el índice del mapa global le atribuye y las actividades que no tienen procedimiento propio. El 2.1 de cada procedimiento remite además a la actividad del macroproceso que desarrolla, como declaración de pertenencia.
- Si el procedimiento que debe desarrollar el contenido aún no existe, la línea lo nombra sin enlace: «*Referencia:* procedimiento de emisión de presupuestos, pendiente de redactar». La relación se anota como prevista en el mapa local (§8, regla 1).

---

## 5. Los mapas de relaciones

Existen dos niveles de registro. Toda relación se registra en el nivel local; las que cruzan macroprocesos se registran además en el global.

| Mapa | Archivo | Ámbito |
|---|---|---|
| Local | `MPR_NNN/MPR_NNN_mapa_relaciones.md` | Relaciones internas del macroproceso y relaciones salientes hacia otros. |
| Global | `00_Mapa_global_relaciones.md` (raíz del repositorio) | Únicamente relaciones entre documentos de macroprocesos distintos. |

### 5.1. Qué contiene el mapa local

Un mapa local por macroproceso, con cuatro secciones:

1. **Inventario del macroproceso.** Documentos que lo componen: el documento del macroproceso, sus procedimientos y sus manuales, con su estado.
2. **Relaciones internas.** Entre documentos del mismo macroproceso.
3. **Relaciones externas.** Con documentos de otros macroprocesos, separadas en salientes y entrantes. Cada fila de esta sección tiene su correspondencia en el mapa global.
4. **Relaciones previstas.** Relaciones detectadas cuyo documento de destino aún no existe. No se escribe el enlace en el cuerpo hasta que el destino se cree (§8.1).

Plantilla lista para copiar, de uso obligatorio: `00_Recursos_metodologia/Plantillas/Plantilla_mapa_local_relaciones.md`.

### 5.2. Qué contiene el mapa global

1. **Matriz de macroprocesos.** Qué macroprocesos se relacionan con cuáles, de un vistazo.
2. **Relaciones cruzadas.** Una fila por relación, con origen, tipo, destino y descripción.
3. **Índice de definiciones compartidas.** Qué concepto o tabla maestra se define en qué apartado y desde dónde se usa. Es lo que hace cumplir el principio de «una definición, un lugar».
4. **Relaciones previstas.** Relaciones cruzadas identificadas cuyo documento de destino aún no existe, en el mismo sentido que en el mapa local.

Plantilla lista para copiar, de uso obligatorio: `00_Recursos_metodologia/Plantillas/Plantilla_mapa_global_relaciones.md`.

### 5.3. Estructura de la tabla de relaciones

Las secciones de relaciones registradas (inventario aparte) usan la misma tabla:

| Origen | Tipo | Destino | Descripción |
|---|---|---|---|
| Enlace resoluble al apartado de origen | Uno de los siete tipos del apartado 3 | Enlace resoluble al apartado de destino | Qué aporta el destino al origen, en una línea |

La sección «Relaciones previstas» usa una variante, con `Destino previsto` en lugar de `Destino`, porque el destino todavía no existe y no se enlaza (§8.1).

---

## 6. Cómo se lee

Antes de redactar o modificar un documento:

1. Abrir el mapa local de su macroproceso. Indica qué documentos existen y de qué depende el que se va a tocar.
2. Abrir únicamente los documentos que el mapa señale como relacionados. No se recorre el árbol entero.
3. Si el documento tiene relaciones externas, consultar el mapa global para ver el contexto completo.

**Si el mapa no existe todavía.** En la primera redacción de un macroproceso, o en el primer despliegue del repositorio, el mapa local o el global aún no se han creado. En ese caso no se omite el paso: se crea el mapa a partir de su plantilla antes de continuar, aunque no tenga ninguna relación que registrar.

Un mapa recién creado contiene su inventario y sus tablas vacías. Existir vacío es correcto; no existir, no. El mapa es el punto de entrada del macroproceso, y crearlo desde el principio evita que las primeras relaciones se escriban sin registro.

Antes de modificar un apartado que otros referencian:

1. Buscar el apartado como destino en el mapa local y en el global.
2. Revisar cada documento que lo cita antes de cambiar su numeración, su nombre o su contenido.

---

## 7. Cómo se retroalimentan

El sistema se mantiene coherente porque escribir una referencia obliga a registrarla. La secuencia es siempre la misma:

1. **Se detecta la relación** al redactar un apartado que necesita algo de otro documento.
2. **Se escribe la referencia** en el cuerpo, con el formato del apartado 4.
3. **Se registra en el mapa local** del macroproceso del documento de origen.
4. **Se registra en el mapa local del destino**, como relación entrante, si el destino pertenece a otro macroproceso.
5. **Se registra en el mapa global** si la relación cruza macroprocesos.
6. **Si la relación usa una definición**, se comprueba el índice de definiciones compartidas del mapa global: si el concepto no está, se añade; si está y apunta a otro sitio, hay una duplicidad que resolver.

En los pasos 3 a 5, si el mapa correspondiente no existe todavía, se crea a partir de su plantilla antes de registrar la relación. Nunca se escribe una referencia en el cuerpo de un documento dejando el registro para más adelante.

Regla de cierre: un documento no se deja sin haber registrado las relaciones detectadas en él. Esta condición forma parte del ciclo de vida definido en `Metodologia_de_redaccion.md`.

### 7.1. Cuándo se revisa un mapa

| Evento | Acción |
|---|---|
| Se inicia un macroproceso | Se crea su mapa local desde la plantilla, aunque esté vacío de relaciones. |
| Se crea un documento | Se añade al inventario del mapa local. |
| Se añade una referencia | Se registra en los mapas que correspondan. |
| Se renumera un apartado | Se actualizan todas las referencias que lo tienen como destino. |
| Se retira un documento | Sus relaciones se eliminan de los mapas; los documentos que lo citaban se revisan. |
| Revisión ordinaria de un macroproceso | Se verifica que cada relación del mapa sigue siendo real. |

---

## 8. Reglas de integridad

1. **Sin referencias colgantes.** Toda referencia apunta a un documento y un apartado que existen. Si el destino aún no existe, no se escribe el enlace: la línea de referencia nombra el documento previsto, «pendiente de redactar» (§4.5), y la relación se anota como prevista en el mapa.
2. **Sin duplicación de contenido.** Si un contenido aparece en dos documentos, uno de los dos debe pasar a referenciar al otro.
3. **Sin ciclos de dependencia.** Dos apartados no pueden depender el uno del otro. Si ocurre, el contenido compartido se extrae a un tercer lugar y ambos lo referencian.
4. **Sin referencias implícitas.** «Como se indicó anteriormente» o «según el procedimiento correspondiente» no son referencias. Se nombra el apartado.
5. **Sin relaciones fuera del sistema.** No se enlaza a documentos externos al repositorio. La documentación externa se cita en texto, indicando fuente y fecha.
6. **El mapa manda sobre la memoria.** Si el mapa y el recuerdo de quien redacta discrepan, se verifica contra el documento real y se corrige el mapa.

---

## 9. Errores frecuentes

1. Reproducir una tabla maestra en dos documentos en lugar de referenciarla.
2. Escribir la referencia en el cuerpo y no registrarla en ningún mapa.
3. Registrar la relación solo en el mapa del origen cuando cruza macroprocesos.
4. Citar un documento completo cuando la información está en un apartado concreto.
5. Usar un enlace cuyo encabezado no coincide literalmente con el del destino.
6. Renumerar un apartado sin revisar quién lo cita.
7. Referenciar a un documento que aún no existe con un código provisional.
8. Usar «ver» o «véase» como única redacción de una referencia.
9. Inventar un tipo de relación fuera de los siete admitidos.
10. Dejar en el mapa una relación cuyo documento de destino ya se retiró.
11. No crear el mapa de un macroproceso por no tener aún relaciones que registrar.
12. Reproducir una definición o unos criterios en lugar de referenciarlos, generando dos orígenes que mantener.
13. Intercalar el enlace dentro de una frase o de una celda del cuerpo, en lugar de llevarlo a su línea de referencia.
14. Remitir desde un procedimiento a la descripción de una actividad del macroproceso, en lugar de al procedimiento que la desarrolla.

---

## 10. Control documental

**Propietario:** {{ORG_AREA_PROCESOS}}

**Responsables de revisión:** *(Pendiente de desarrollo)*

**Periodicidad de revisión:** *(Pendiente de desarrollo)*. De forma extraordinaria, ante cualquier cambio en la estructura del repositorio o en los formatos de referencia.

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
