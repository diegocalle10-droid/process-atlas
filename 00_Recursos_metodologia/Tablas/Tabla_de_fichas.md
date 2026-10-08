# Tabla de fichas — {{ORG_NOMBRE}}

Catálogo de todos los documentos oficiales del sistema (`MPR`, `PRC`, `MAN`): una fila por documento, con sus datos de identificación y su ubicación. Es la vista de consulta de los documentos publicados.

**Cómo se mantiene:** la tabla se genera automáticamente a partir de la ficha técnica de cada documento (su anexo de ficha, según `Plantillas/Plantilla_ficha_tecnica.md`), mediante `.claude/hooks/actualizar_vistas.py`. No se edita a mano: para cambiar una fila se modifica la ficha del documento correspondiente. La columna Ubicación no sale de la ficha: la calcula el hook a partir de la ruta del archivo.

**Relación con el registro de códigos:** `Nomenclatura/Registro_de_codigos.md` es el libro de emisión de códigos, incluidos los retirados y anulados. Esta tabla solo muestra los documentos que existen en el repositorio y lo que declara su ficha.

<!-- FICHAS:INICIO -->
| Código | Nombre | Tipo | Macroproceso | Versión | Propietario | Fecha de aprobación | Ubicación |
|---|---|---|---|---|---|---|---|

Sin documentos oficiales registrados.
<!-- FICHAS:FIN -->

---

## Control documental

**Propietario:** {{ORG_AREA_PROCESOS}}

**Control de versiones:**

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.0 | 08/10/2026 | Versión pública inicial. | process-atlas |
