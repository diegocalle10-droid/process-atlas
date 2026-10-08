# Plantilla de ficha técnica

Modelo único de ficha técnica para todo documento oficial del sistema: macroproceso (`MPR`), procedimiento (`PRC`) y manual (`MAN`). Cada documento lleva su propia ficha como anexo fijo; la ficha es la versión tangible y compilable del documento para su consulta por las áreas.

**Antes de redactar:** leer `Metodologia_de_redaccion.md` §7.3 (anexos del macroproceso), §8.2 (anexos del procedimiento) y §9 (manuales).

**Reglas de uso:**

- **Ubicación del anexo:**

  | Documento | Anexo | Encabezado exacto |
  |---|---|---|
  | `MPR` | Anexo 2 | `### Anexo 2. Ficha técnica del macroproceso` |
  | `PRC` | Anexo 1 | `### Anexo 1. Ficha técnica del procedimiento` |
  | `MAN` | Anexo 1 | `### Anexo 1. Ficha técnica del manual` |

- **Momento:** la ficha es un producto final. Se genera solo cuando el documento se aprueba como versión definitiva, sea cual sea su ruta de entrada, sobre el cuerpo ya sin marcas de trabajo (`Metodologia_de_redaccion.md` §12). Si una versión definitiva posterior cambia el cuerpo, se regenera en el mismo cambio.
- **La ficha solo resume.** No contiene información que no esté en el cuerpo del documento.
- **Campos fijos.** Las etiquetas de la columna `Campo` no se renombran, no se reordenan y no se eliminan: `Tablas/Tabla_de_fichas.md` las lee por su nombre.
- **Campos que no aplican.** Un campo que no corresponde al tipo de documento se conserva con `*No aplica*`. Un campo sin información se marca `*(Pendiente de desarrollo)*`.
- **Formato de datos:** códigos con guion medio (`PRC-001`), fechas `dd/mm/aaaa`, áreas según `Metodologia_de_redaccion.md` §10.2, y sistemas con la grafía de `Sistema_de_nomenclatura.md` §7.

**Origen de cada campo en el cuerpo del documento:**

| Campo | `MPR` | `PRC` | `MAN` |
|---|---|---|---|
| Código, Nombre, Tipo | 1.1–1.3 | 1.1–1.3 | Título y cabecera |
| Macroproceso | *No aplica* | Macroproceso al que pertenece | Macroproceso al que pertenece |
| Versión | Última fila de la tabla de 8.4 | Última fila de la tabla de 7.4 | Última fila de la tabla del control documental |
| Definición | 2.1 | 2.1 | *No aplica* |
| Objetivo | 2.2 | 2.2 | Apartado 1, propósito |
| Alcance, Inicio, Fin | 2.3–2.5 | 2.3–2.5 | *No aplica* |
| Entradas, Salidas | 2.6 | 2.6 | *No aplica* |
| Actividades principales | 3.1 | 3.1 | *No aplica* |
| Indicadores KPI | 6 | *No aplica* | *No aplica* |
| Riesgos y controles | 5 | 4 | *No aplica* |
| Registros generados | 7 | 6 | *No aplica* |
| Anexos y diagramas | Anexos 1, 3 y 4+ | Anexos 2+ | Anexos 2+ |
| Propietario | 8.1 | 7.1 | Control documental |
| Elaborado, revisado y aprobado | 8.6 | 7.6 | Control documental |

---

```markdown
### Anexo [N]. Ficha técnica del [macroproceso|procedimiento|manual]

| Campo | Contenido |
|---|---|
| Código | [MPR-NNN / PRC-NNN / MAN-NNN] |
| Nombre | [nombre literal del título, sin código] |
| Tipo | [Macroproceso operativo, de soporte o estratégico / Procedimiento operativo, de soporte o estratégico / Manual] |
| Macroproceso | [MPR-NNN al que pertenece, o *No aplica*] |
| Versión | [versión vigente] |
| Definición | [síntesis de 2.1] |
| Objetivo | [síntesis de 2.2] |
| Alcance | [síntesis de 2.3] |
| Inicio | [evento de inicio] |
| Fin | [evento de fin] |
| Entradas | [activos de información de entrada] |
| Salidas | [resultados generados] |
| Actividades principales | [nombres literales de 3.1] |
| Indicadores KPI | [códigos y nombres de 6.N] |
| Riesgos y controles | [riesgos principales y su control] |
| Registros generados | [registros de evidencia] |
| Anexos y diagramas | [anexos del documento] |
| Propietario | [área] |
| Elaborado por | [área o persona] |
| Fecha de elaboración | [dd/mm/aaaa] |
| Revisado por | [área o persona] |
| Fecha de revisión | [dd/mm/aaaa] |
| Aprobado por | [área o persona] |
| Fecha de aprobación | [dd/mm/aaaa] |
```
