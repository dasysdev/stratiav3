# Amazon como fuente de requisitos y bloques de categoría deterministas

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-016). Procede del segundo experimento del clasificador (tarea T-012, `demand-engine/runs/2026-10-25-v1-report.md`). El usuario aceptó las propuestas 1 y 2 del informe: «ok a 1 y 2».*

## Contexto del experimento

En el experimento se perdió un 35 % de las cuestiones clave. La causa principal es un hueco entre D-009, D-030 y D-036:

- Una cuestión que solo recoge Amazon cuenta como «base» para decidir la etiqueta (D-030), así que la característica pasa a valor.
- Pero Amazon no es fuente de requisitos (D-009).
- Y la cuestión tampoco es «inferida», porque una referencia la recoge (D-036).
- Resultado: se queda sin sitio.

Además, los bloques de sector son inestables: solo 4 de 14 coinciden entre las dos ejecuciones. Shopify repite color, patrón, tejido y cuidados como atributos propios en varios niveles, y unos agentes los asignan al bloque más específico y otros al más general.

## Propuesta 1 (aceptada)

Cerrar el hueco de Amazon, que es una decisión de canon: que las propiedades de los PTD de Amazon, incluidos los valores de special_feature, puedan ser fuente de requisitos de la categoría cuando son relevantes para la clase, con origen «referencias». Es una enmienda de D-009.

La alternativa descartada era mantener D-009 y tratarlas como inferidas con Amazon de apoyo, lo que exigía redefinir «inferida».

## Propuesta 2 (aceptada)

Construir los bloques de categoría de forma determinista: un atributo repetido va siempre al bloque de la categoría más general que lo lista, para que un bloque de sector no cambie según el producto.

Además, crear un catálogo de bloques cat. (preguntas e importancia por defecto), generado con la herramienta y revisado una vez por categoría. El clasificador elegiría bloques en lugar de redactarlos, lo que reduce la variación y el coste.
