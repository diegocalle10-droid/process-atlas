# Plantilla de mapa local de relaciones

Modelo de estructura para todo documento `MPR_NNN_mapa_relaciones.md`, uno por macroproceso, ubicado en la carpeta de su macroproceso.

**Antes de redactar:** leer `Metodologia_de_relaciones.md` (tipos de relación, formato de referencia y reglas de integridad).

**Reglas de uso:**

- **Se crea al iniciar el macroproceso**, aunque no haya ninguna relación que registrar. Un mapa vacío es correcto; un mapa inexistente, no.
- Es el punto de entrada del macroproceso: se lee antes de redactar o modificar cualquiera de sus documentos.
- Registra tanto las relaciones salientes como las entrantes desde otros macroprocesos.
- Toda relación externa registrada aquí tiene su fila correspondiente en `00_Mapa_global_relaciones.md`.
- Los tipos admitidos son los siete de `Metodologia_de_relaciones.md` §3. No se inventan otros.

---

```markdown
# MPR-NNN – Mapa de relaciones

Registro de las relaciones entre los documentos del macroproceso MPR-NNN y con documentos de otros macroprocesos. Se consulta antes de redactar o modificar cualquier documento de este macroproceso.

**Macroproceso:** [nombre del macroproceso]
**Última actualización:** [dd/mm/aaaa]

---

## 1. Inventario del macroproceso

| Código | Documento | Tipo | Estado |
|---|---|---|---|
| MPR-NNN | [[MPR_NNN\|MPR-NNN]] | Macroproceso | [En curso \| Versión definitiva \| Retirado \| Anulado] |
| PRC-NNN | [[PRC_NNN_descriptor\|PRC-NNN]] | Procedimiento | [En curso \| Versión definitiva \| Retirado \| Anulado \| Pendiente de desarrollo] |
| MAN-NNN | [[MAN_NNN_descriptor\|MAN-NNN]] | Manual | [En curso \| Versión definitiva \| Retirado \| Anulado \| Pendiente de desarrollo] |

[Si aún no existe ningún documento: «*(Pendiente de desarrollo)*».]

---

## 2. Relaciones internas

Relaciones entre documentos de este mismo macroproceso.

| Origen | Tipo | Destino | Descripción |
|---|---|---|---|
| [[PRC_NNN_descriptor\|PRC-NNN]] | desarrolla | [[MPR_NNN#3.1.1. Nombre de la actividad\|MPR-NNN §3.1.1]] | [qué aporta el destino al origen, en una línea] |

[Si no existen todavía: «Sin relaciones registradas.»]

---

## 3. Relaciones externas

Relaciones con documentos de otros macroprocesos. Cada fila tiene su correspondencia en `00_Mapa_global_relaciones.md`.

### 3.1. Salientes

Documentos de este macroproceso que referencian a otros.

| Origen | Tipo | Destino | Descripción |
|---|---|---|---|
| [[PRC_NNN_descriptor#3.1.1. Nombre\|PRC-NNN §3.1.1]] | depende de | [[PRC_MMM_descriptor#2.7.1. Nombre\|PRC-MMM §2.7.1]] | [descripción] |

[Si no existen todavía: «Sin relaciones registradas.»]

### 3.2. Entrantes

Documentos de otros macroprocesos que referencian a los de este.

| Origen | Tipo | Destino | Descripción |
|---|---|---|---|
| [[PRC_MMM_descriptor#3.1.2. Nombre\|PRC-MMM §3.1.2]] | usa definición de | [[PRC_NNN_descriptor#2.8.1. Nombre\|PRC-NNN §2.8.1]] | [descripción] |

[Si no existen todavía: «Sin relaciones registradas.»]

---

## 4. Relaciones previstas

Relaciones identificadas cuyo documento de destino aún no existe. No se escribe el enlace en el cuerpo hasta que el destino esté creado.

| Origen | Tipo | Destino previsto | Descripción |
|---|---|---|---|
| [[PRC_NNN_descriptor#3.1.1. Nombre\|PRC-NNN §3.1.1]] | depende de | *(Pendiente de desarrollo)* — [qué documento se espera] | [descripción] |

[Si no existen: «Sin relaciones previstas.»]
```
