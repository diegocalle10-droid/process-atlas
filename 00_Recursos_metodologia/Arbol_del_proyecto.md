# Árbol del proyecto — {{ORG_NOMBRE}}

Inventario físico del repositorio: qué existe hoy y dónde, con una glosa de una frase por rama. Qué es cada documento, cuándo se usa y en qué orden está en `Orquestador.md`, de donde procede cada glosa.

El bloque lo regenera `.claude/hooks/actualizar_vistas.py` cada vez que cambia el árbol. No se edita a mano.

<!-- ARBOL:INICIO -->
```
./
├── .claude/ — configuración de Claude Code del proyecto
│   ├── agents/ — agentes del proyecto
│   │   └── orquestador-procesos.md — agente orquestador, sesión principal
│   ├── hooks/ — automatismos deterministas
│   │   ├── actualizar_vistas.py — regenera el árbol y la tabla de fichas
│   │   ├── auditar_codigos.py — audita códigos tras operaciones de shell
│   │   ├── lib_sistema.py — librería común del sistema
│   │   ├── post_escritura.py — inscribe códigos y normaliza nombres
│   │   ├── pre_escritura.py — valida códigos antes de escribir
│   │   └── triaje_sesion.py — triaje de arranque de sesión
│   ├── scripts/ — scripts a demanda
│   │   ├── comprobar_ciclos.py — detecta ciclos de dependencia
│   │   ├── comprobar_enlaces.py — comprueba enlaces
│   │   ├── comprobar_referencias_en_prosa.py — comprueba el formato de las referencias
│   │   ├── desplegar_sistema.py — motor de despliegue
│   │   ├── listar_referencias.py — lista referencias de un macroproceso
│   │   └── quitar_marcas_trabajo.py — elimina marcas de trabajo
│   ├── skills/ — skills del proyecto
│   │   ├── desplegar-sistema/ — skill de arranque y despliegue
│   │   │   └── SKILL.md — procedimiento de arranque
│   │   └── estilo-redaccion/ — skill de estilo de redacción
│   │       ├── extraccion_de_crudos.md — extracción de crudos
│   │       ├── modo_fichas_tablas.md — modo fichas y tablas
│   │       ├── modo_manual.md — modo manual
│   │       ├── modo_mpr_prc.md — modo MPR y PRC
│   │       └── SKILL.md — núcleo de la skill
│   ├── CLAUDE.md — instrucciones de arranque de la sesión
│   └── settings.json — configuración de hooks y agente
├── .github/ — integración continua
│   └── workflows/ — integración continua
│       └── pruebas.yml — integración continua
├── 00_Recursos_metodologia/ — recursos de metodología y navegación
│   ├── Metodologia/ — perfil, mapa y normas de redacción y relación
│   │   ├── 00_Mapa_procesos.md — mapa de macroprocesos
│   │   ├── 00_Perfil_organizacion.md — perfil de la organización
│   │   ├── Metodologia_de_redaccion.md — norma maestra de redacción
│   │   └── Metodologia_de_relaciones.md — norma de relaciones entre documentos
│   ├── Nomenclatura/ — nombrado y codificación
│   │   ├── Registro_de_codigos.md — libro de códigos emitidos
│   │   └── Sistema_de_nomenclatura.md — reglas de nombrado y códigos
│   ├── Plantillas/ — plantillas de uso obligatorio
│   │   ├── Plantilla_ficha_tecnica.md — plantilla de ficha técnica
│   │   ├── Plantilla_macroproceso.md — plantilla de macroproceso
│   │   ├── Plantilla_manual.md — plantilla de manual
│   │   ├── Plantilla_mapa_contenidos_pendientes.md — plantilla de contenidos pendientes
│   │   ├── Plantilla_mapa_global_relaciones.md — plantilla de mapa global
│   │   ├── Plantilla_mapa_local_relaciones.md — plantilla de mapa local
│   │   ├── Plantilla_matriz_actividades.md — diagnóstico de actividades principales
│   │   └── Plantilla_procedimiento.md — plantilla de procedimiento
│   ├── Tablas/ — tablas maestras
│   │   └── Tabla_de_fichas.md — catálogo de documentos oficiales
│   ├── Arbol_del_proyecto.md — inventario físico del repositorio
│   ├── Instrucciones_de_actuacion.md — pipeline de la bandeja de entrada
│   └── Orquestador.md — qué es cada documento y cuándo se usa
├── ejemplos/ — ejemplo de organización ficticia
│   ├── panaderia/ — ejemplo de organización ficticia
│   │   ├── 00_Mapa_procesos.md — ejemplo de organización ficticia
│   │   └── 00_Perfil_organizacion.md — ejemplo de organización ficticia
│   └── README.md — ejemplo de organización ficticia
├── tests/ — pruebas del motor
│   └── test_motor.py — pruebas del motor
├── .gitignore — exclusiones de git
├── CHANGELOG.md — historial de versiones públicas
├── CITATION.cff — cita del proyecto
├── LICENSE — licencia del código (MIT)
├── LICENSE-DOCS.md — licencia de la documentación (CC BY 4.0)
└── README.md — presentación del proyecto
```
<!-- ARBOL:FIN -->
