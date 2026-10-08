# Mapa de procesos — {{ORG_NOMBRE}}

Documento maestro del mapa de procesos: qué macroprocesos tiene la organización. Es el punto de partida del sistema. El despliegue (función F0, `Orquestador.md` §3) crea a partir de esta tabla una carpeta `MPR_NNN/` por macroproceso, con sus procedimientos, sus manuales y su mapa local de relaciones, y la matriz del mapa global.

**Cómo se rellena:**

- Una fila por macroproceso. Basta con nombrarlo y clasificarlo: las áreas, las actividades y las relaciones se documentan después, al redactar cada macroproceso.
- **Código:** `MPR-001`, `MPR-002`… correlativos y sin huecos. Hasta `MPR-999`.
- **Nombre:** el nombre con el que la organización conoce el macroproceso, por ejemplo «Gestión comercial». El título formal se construye al redactar el `MPR` con la fórmula de `Sistema_de_nomenclatura.md` §4.2, y en ese momento esta columna se actualiza con él (§4.4).
- **Tipo:** `Estratégico`, `Operativo` o `Soporte`.

**Cambios posteriores:** para añadir un macroproceso se añade su fila y se vuelve a desplegar; solo se crea lo nuevo. Un código emitido no se reasigna a otro macroproceso. Quitar una fila no borra su carpeta: el triaje lo avisa y decide el usuario.

---

## 1. Macroprocesos

| Código | Nombre | Tipo |
|---|---|---|

---

## 2. Control documental

**Propietario:** {{ORG_AREA_PROCESOS}}

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
