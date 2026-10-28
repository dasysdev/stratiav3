# Entrenar con los modelos de una auditoría completa: idea

Conversación del usuario con Claude del 2026-10-28, recogida por Claude el mismo día. El usuario pidió documentarla «como una idea»: no es una decisión.

## Pregunta del usuario

«Si lo que quisiera es que, por ejemplo, tras ejecutar una auditoría completa de una tienda quisiera entrenar el modelo con los modelos generados. ¿Lo ves adecuado lo que hay y esta estrategia?»

## Análisis de Claude

- **La estrategia es la del canon.** Lo que la ejecución usa sin compilar se encola y el entrenamiento lo convierte en reglas. Casi no cuesta nada: para auditar ya hay que clasificar cada ficha, así que los votos ya existen, y el ciclo de entrenamiento es determinista.
- **Lo que hay no basta.** Faltan cuatro cosas, de más a menos importante.

## Propuesta de Claude

1. **Voto por tienda y clase.** La regla de una clase es la mayoría de los votos, y cada ficha vota. Una tienda con 2.000 productos casi iguales de una clase aporta 2.000 votos que son, en la práctica, una sola opinión, y fijaría las reglas de esa clase. Propuesta: agregar primero el voto por tienda y clase (mayoría dentro de la tienda) y contar después cada tienda como un voto, con el mismo espíritu que la regla de las dos tiendas de la información resolutiva. Enmendaría la regla de una clase de D-045.
2. **Una ejecución, no dos.** El paso 2 del entrenamiento aplica las reglas dos veces por caso; una auditoría da una ejecución. Propuesta: la ejecución de la auditoría cuenta como una de las dos y la estabilidad se mide repitiendo una muestra (ya se planteó en T-029). Tampoco está en el canon.
3. **Control por vertical.** Una regla se acepta si el control no empeora, pero los 14 casos de control son de pocas verticales (casa, mascotas, calzado). Las reglas de una tienda de otra vertical pasarían sin contraste. Propuesta: añadir unos pocos casos de control por cada vertical nueva, con lo esperado decidido por el usuario.
4. **Conexión (solo código).** `bin/train` entrena con las carpetas de ejecuciones que se le pasan; nada lee `var/queue.jsonl`. Los resultados de una auditoría quedarían en `var/`, desechable, y son la materia del entrenamiento.

Consecuencia: si se vuelve a auditar la misma tienda tras entrenar, salen modelos distintos (otra clave, menos partes provisionales). La auditoría ya entregada no cambia, porque guarda lo que usó sin compilar.

## Relación

El usuario plantea a la vez otro enfoque: un catálogo curado de casos de entrenamiento, al que un caso auditado entraría como candidato. Está en revisión y no forma parte de este artefacto.
