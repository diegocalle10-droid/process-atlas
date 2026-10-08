# Modo fichas y tablas

Se aplica, junto al modo del tipo de documento, al generar o actualizar una ficha técnica, al completar tablas de cuerpo o anexos y al escribir en un mapa de relaciones. La norma está en Metodología §10.8.

## Ficha técnica

1. La ficha se genera solo cuando el usuario aprueba el documento como versión definitiva, después de eliminar las marcas de trabajo del cuerpo (Metodología §12). Mientras el documento está en curso, el anexo queda *(Pendiente de desarrollo)* y no se rellena.
2. Abre `00_Recursos_metodologia/Plantillas/Plantilla_ficha_tecnica.md` y sigue su tabla «Origen de cada campo»: cada celda se rellena desde su apartado de origen, nunca desde la fuente original ni desde la memoria de la sesión.
3. Campos literales: se copian. Campos de síntesis: una o dos frases con términos que ya están en el cuerpo.
4. Las etiquetas de la columna `Campo` no se tocan: el hook de `Tablas/Tabla_de_fichas.md` las lee por su nombre.
5. Comprobación final: ninguna celda contiene un dato que no esté en el cuerpo (Metodología §11, error 12).

## Tablas de cuerpo y anexos

- Estilo de celda, celdas vacías y marcas de veracidad según §10.8.
- Las columnas que reproducen nombres de otro apartado (actividades, procedimientos, áreas) se copian literalmente de ese apartado (Metodología §11, errores 2 y 9).
- Una tabla no introduce un dato que el cuerpo no contenga, salvo que la tabla sea el lugar propio de ese dato según la metodología.

## Mapas de relaciones

La estructura y el registro de cada relación los gobierna `Metodologia_de_relaciones.md`. Este modo solo afecta a los textos descriptivos: una frase por relación que diga qué aporta un documento al otro, con la misma terminología que ambos documentos.
