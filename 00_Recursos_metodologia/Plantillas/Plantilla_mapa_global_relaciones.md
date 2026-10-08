# Plantilla de mapa global de relaciones

Modelo de estructura para `00_Mapa_global_relaciones.md`, documento único ubicado en la raíz del repositorio.

**Antes de redactar:** leer `Metodologia_de_relaciones.md` (tipos de relación, formato de referencia y reglas de integridad).

**Reglas de uso:**

- **Lo crea el despliegue** (función F0, `.claude/scripts/desplegar_sistema.py`), aunque no haya ninguna relación que registrar.
- La matriz del apartado 1 tiene una fila y una columna por macroproceso del mapa de procesos. La genera el despliegue y cada nuevo despliegue la ajusta al mapa conservando las marcas existentes.
- Registra **únicamente** relaciones entre documentos de macroprocesos distintos. Las internas viven en el mapa local de cada macroproceso.
- Cada fila del apartado 2 tiene su correspondencia en los mapas locales de ambos macroprocesos implicados.
- El índice de definiciones compartidas es el mecanismo que hace cumplir el principio de «una definición, un lugar»: antes de definir un concepto, se comprueba aquí si ya está definido en otro sitio.

---

```markdown
# Mapa global de relaciones — {{ORG_NOMBRE}}

Registro de las relaciones entre documentos de macroprocesos distintos. Se consulta antes de redactar cualquier documento con relaciones externas y antes de definir cualquier concepto o tabla maestra.

**Última actualización:** [dd/mm/aaaa]

---

## 1. Matriz de macroprocesos

Qué macroprocesos se relacionan con cuáles. Cada marca indica que existe al menos una relación registrada en el apartado 2.

| Origen ↓ / Destino → | MPR-001 | MPR-002 |
|---|---|---|
| **MPR-001** | — | |
| **MPR-002** | | — |

---

## 2. Relaciones cruzadas

| Origen | Tipo | Destino | Descripción |
|---|---|---|---|
| [[PRC_NNN_descriptor#3.1.1. Nombre\|PRC-NNN §3.1.1]] | depende de | [[PRC_MMM_descriptor#2.7.1. Nombre\|PRC-MMM §2.7.1]] | [qué aporta el destino al origen, en una línea] |

[Si no existen todavía: «Sin relaciones registradas.»]

---

## 3. Índice de definiciones compartidas

Dónde se define cada concepto, tabla maestra o criterio que se usa desde más de un documento. Antes de definir algo, se comprueba aquí si ya existe.

| Concepto | Definido en | Usado desde |
|---|---|---|
| [concepto o tabla maestra] | [[PRC_NNN_descriptor#2.8.1. Nombre\|PRC-NNN §2.8.1]] | [[MPR_MMM#2.6. Entradas y salidas del proceso\|MPR-MMM §2.6]], [[PRC_PPP_descriptor#3.1.2. Nombre\|PRC-PPP §3.1.2]] |

[Si no existen todavía: «Sin definiciones compartidas registradas.»]

---

## 4. Relaciones previstas

Relaciones cruzadas identificadas cuyo documento de destino aún no existe.

| Origen | Tipo | Destino previsto | Descripción |
|---|---|---|---|
| [[PRC_NNN_descriptor#3.1.1. Nombre\|PRC-NNN §3.1.1]] | depende de | *(Pendiente de desarrollo)* — [qué documento se espera] | [descripción] |

[Si no existen: «Sin relaciones previstas.»]
```
