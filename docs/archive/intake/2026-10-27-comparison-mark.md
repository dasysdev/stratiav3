# Cómo se fija la marca de dimensión de comparación

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de pistas de valoración. Resuelve OQ-69 (valor por defecto de la marca y qué prueba la establece). Ortografía de las citas normalizada.

## 1. Propuesta y respuesta

Claude estudió los 489 requisitos del catálogo y vio que el tipo (rasgo × entidad) no decide bien la marca: dentro de un mismo tipo hay requisitos que se comparan y otros que no. Propuso decidirla requisito a requisito, con un criterio, «se compara» por defecto, y las mismas pruebas, escritores y momentos que las pistas. Usuario: «en principio es tal cual propones». Duda del usuario: «si por defecto "compara" es adecuado. Haz un estudio rápido de si para el caso de la comparación es más frecuente que un requisito pueda compararse o no».

## 2. Estudio rápido

Muestra al azar de 70 de los 489 requisitos, clasificada por Claude con el criterio (orientativa: muestra pequeña y un solo clasificador):

| Resultado | Requisitos | % |
|---|---|---|
| Se compara | 34 | 49 % |
| No se compara | 30 | 43 % |
| Dudoso | 6 | 9 % |

- Salen más o menos mitad y mitad: ningún valor por defecto acierta en la mayoría.
- Los «no» son casi todos **filtros o gustos** (color, estampado, forma, medidas, talla, público, idioma, temporada, tarea) y unos pocos que **identifican** (compositor, fecha de edición, fabricante, género musical). Ninguno de tipo «igual para todos» en la muestra; esos están en la capa general (garantía legal).
- El rasgo orienta en algunos casos (material: se compara; prestación: casi siempre; estética y medida: casi nunca; uso, identidad y construcción: mezclados). Sirve de ayuda para redactar, no como regla.

Usuario: «todo OK».

## 3. Decisiones

- **Marca por requisito**, no por tipo. El árbol de bloques evita la duplicidad: cada requisito se escribe una vez y lo heredan sus clases.
- **Se decide con un criterio, no con una lista:**

  > Un requisito **se compara** si su respuesta cambia de una oferta a otra y el comprador elige por ese valor: prefiere más, menos o uno mejor.
  > **No se compara** si: (a) es igual en todas las ofertas, porque lo fija la ley o es universal (garantía legal); (b) solo sirve para que la oferta encaje con una **necesidad o un gusto** que ya se tiene: es un filtro (tamaño de cama, compatibilidad, idioma, color); (c) identifica la oferta o dice en qué estado está (identificadores, vendedor, disponibilidad).

- **Sin valor por defecto.** Cada requisito lleva su marca explícita y un motivo corto según el criterio.
- **Dudosos:** «se compara» mientras no haya pruebas, para no quitar un criterio sin motivo.
- **Pruebas:** preguntas comparativas de PAA («¿qué es mejor, lino o algodón?», «¿cuántos hilos debe tener?»); la justificación del requisito en taxo; una ley que exista para poder comparar (precio por unidad, etiqueta energética).
- **Quién y cuándo:** igual que las pistas. Para el catálogo actual, una pasada manual de Claude; después, al crear modelos y en los entrenamientos. Si dos fuentes se contradicen, se marca como duda.

Ejemplos (hipotéticos):

| Requisito | Marca | Por qué |
|---|---|---|
| Precio, coste de envío, plazo de entrega | Se compara | El comprador prefiere menos |
| Composición, gramaje, número de hilos | Se compara | PAA los compara |
| Opiniones | Se compara | Se prefiere mejor valoración |
| Garantía legal | No | (a): la misma para todos |
| Tamaño de cama | No | (b): es un filtro |
| Identificadores, vendedor, disponibilidad | No | (c): identifican o dicen el estado |
| Marca, plazo de devolución | Dudoso: se compara mientras no haya pruebas | Lo resolvería la evidencia |
