# process-atlas

**Sistema para documentar los procesos de una organización con Claude Code: macroprocesos, procedimientos y manuales coherentes entre sí, trazables hasta su fuente y sin contenido inventado.**

*English summary [below](#english).*

---

## Qué es

process-atlas convierte un repositorio en un sistema documental de procesos al estilo ISO 9001. Se parte del mapa de procesos de la organización y se construye, documento a documento, una red de:

- **Macroprocesos (`MPR`)**: qué se hace y para qué.
- **Procedimientos (`PRC`)**: cómo se hace, con el detalle de una instrucción de trabajo.
- **Manuales (`MAN`)**: cómo se usa un sistema o una herramienta.
- **Mapas de relaciones** locales y global: qué documento depende de cuál.

Claude Code redacta siguiendo una metodología completa (plantillas con nodos fijos, norma de estilo, nomenclatura, registro de códigos y metodología de relaciones), y una capa de hooks deterministas en Python vigila que nada se salte las reglas.

## Lo que lo diferencia

- **Antialucinación por diseño.** Todo contenido se marca `[VERIFICADO]` o `[INFERENCIA — ALTA/MEDIA/BAJA]` con su base. Lo que falta se pregunta o se marca *(Pendiente de desarrollo)*: nunca se rellena con conocimiento genérico de normas.
- **Del audio al procedimiento.** Las transcripciones de reuniones (crudos) se extraen con un inventario de unidades y preguntas que sobrevive entre sesiones.
- **Una pregunta, un apartado.** Cada nodo de la plantilla responde a una sola pregunta, con criterios de cuándo está completo.
- **Códigos blindados.** Los hooks impiden duplicar, saltar o reutilizar códigos y los inscriben solos en el registro.
- **Red, no colección.** Cada referencia entre documentos se registra en los mapas local y global; hay scripts que detectan enlaces rotos y dependencias circulares.

## Requisitos

- [Claude Code](https://claude.com/claude-code) con una suscripción o licencia que lo permita.
- Python 3.9 o superior, accesible como `python`. En macOS y Linux, si solo tienes `python3`, instala el alias (`python-is-python3` en Debian/Ubuntu) o cambia `python` por `python3` en `.claude/settings.json`.
- Git.

Funciona en Windows, macOS y Linux: las pruebas automáticas del motor se ejecutan en los tres en cada cambio.

## Puesta en marcha

1. Crea tu repositorio con **Use this template** desde [github.com/diegocalle10-droid/process-atlas](https://github.com/diegocalle10-droid/process-atlas) (o clónalo con `git clone https://github.com/diegocalle10-droid/process-atlas.git`) y abre una terminal en él.
2. Ejecuta `claude`. El triaje de arranque detecta que el sistema no está desplegado (función F0).
3. Ejecuta `/desplegar-sistema`. Claude te hará las preguntas del perfil de la organización (nombre, actividad, área responsable, variante del idioma, marco de referencia, sistemas y unidades).
4. Dale la lista de tus macroprocesos: nombre y tipo (estratégico, operativo o soporte). Nada más.
5. Confirma el despliegue. Se crean las carpetas `MPR_001/`, `MPR_002/`… con sus `Procedimientos/`, `Manuales/` y mapa de relaciones, el mapa global, el mapa de contenidos pendientes y la bandeja `En_proceso/`.

A partir de ahí: pide a Claude que redacte tu primer macroproceso, o deja la transcripción de una reunión en `En_proceso/` y él la procesa.

Para ver el resultado antes de usar tus datos, prueba el ejemplo ficticio de `ejemplos/panaderia/`.

## Cómo está organizado

```
.claude/                    Agente orquestador, skills, hooks y scripts
  agents/                   orquestador-procesos: sesión principal
  skills/                   desplegar-sistema (F0) y estilo-redaccion
  hooks/                    triaje, validación y registro de códigos, vistas
  scripts/                  despliegue y comprobaciones a demanda
00_Recursos_metodologia/    Metodología, nomenclatura, plantillas y tablas
  Orquestador.md            Qué es cada documento y qué función se dispara cuándo
MPR_NNN/                    Una carpeta por macroproceso (la crea el despliegue)
En_proceso/                 Bandeja de entrada de material nuevo
```

El documento de entrada es `00_Recursos_metodologia/Orquestador.md`: funciones F0 a F7, orden operativo para crear cada tipo de documento y glosa de cada archivo.

## Pruebas

```
python -m unittest discover -s tests -v
```

## Privacidad

El repositorio que crees con tus procesos contendrá información interna de tu organización. Mantenlo **privado**. Las grabaciones y transcripciones de reuniones que dejes en `En_proceso/` pueden contener datos personales: revisa `.gitignore` antes de subirlas.

## Licencias

- **Código** (`.claude/hooks/`, `.claude/scripts/`, `tests/`, `.github/`): [MIT](LICENSE).
- **Metodología y documentación** (`00_Recursos_metodologia/`, skills, agente, `CLAUDE.md`, este README y los ejemplos): [CC BY 4.0](LICENSE-DOCS.md). Puedes usarla y adaptarla, también con fines comerciales, citando la autoría.

Los documentos de procesos que generes con el sistema son tuyos.

## Cómo citar

Ver [`CITATION.cff`](CITATION.cff). Formato breve: *Calle Pinedo, D. (2026). process-atlas: sistema de documentación de procesos con Claude Code.*

---

## English

**process-atlas** is a Claude Code template for documenting an organization's processes in an ISO 9001 style: macroprocesses, procedures and manuals that stay consistent with each other, traceable to their source and free of invented content.

- Start from your process map: name and type of each macroprocess. `/desplegar-sistema` asks a few profile questions and scaffolds one `MPR_NNN/` folder per macroprocess, plus the relationship maps and an inbox.
- Claude drafts each document with a full methodology (fixed-node templates, style rules, naming, code registry, cross-references), and deterministic Python hooks enforce code integrity and keep the tree and catalog up to date.
- Anti-hallucination by design: every statement is tagged as verified or inference (with its basis); missing information is asked for, never filled in.
- Meeting transcripts become procedures through a resumable extraction inventory.

The methodology and all documentation are written in **Spanish**. Requirements: Claude Code, Python 3.9+, Git. Code is MIT-licensed; methodology and docs are CC BY 4.0.
