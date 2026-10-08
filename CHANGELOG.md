# Changelog

Cambios por versión publicada de process-atlas. El formato sigue [Keep a Changelog](https://keepachangelog.com/es-ES/1.1.0/) y las versiones, [SemVer](https://semver.org/lang/es/).

## [0.1.0] — 2026-10-08

Primera versión pública.

### Añadido

- Arranque por perfil y mapa de procesos (función F0): skill `desplegar-sistema` y script `desplegar_sistema.py`. Preguntas con identificador y marcador que adaptan el sistema a cada organización; una carpeta `MPR_NNN/` por macroproceso, hasta `MPR-999`.
- Hooks deterministas en Python (Windows, macOS y Linux): triaje de arranque, validación y registro de códigos, normalización de nombres y regeneración del árbol y de la tabla de fichas.
- Pruebas automáticas del motor e integración continua en los tres sistemas.
- Ejemplo de organización ficticia en `ejemplos/panaderia/`.

### Metodología incluida

- Metodología de redacción (esqueletos de `MPR`, `PRC` y `MAN`, dimensiones de una actividad, estilo, veracidad y ciclo de vida).
- Metodología de relaciones (siete tipos de relación, referencia legible y resoluble, mapas local y global).
- Sistema de nomenclatura y registro de códigos.
- Plantillas de macroproceso, procedimiento, manual, ficha técnica, matriz de actividades y mapas.
- Skill `estilo-redaccion` con extracción de crudos (transcripciones y notas) con inventario.
