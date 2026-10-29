# Inducción de las especializaciones en el entrenamiento

Fecha: 2026-10-29. Origen: revisión del diseño con el usuario al empezar la tarea T-090 (D-190: «La tarea se revisa con el usuario al empezarla»).

## Situación de partida

- El clasificador redacta cada especialización en cada ejecución (`esp.<nombre>@0`, no compilada). No hay catálogo de especializaciones.
- Inestabilidades del piloto: la misma lijadora sale como `esp.a-bateria` en una ejecución y como `esp.bateria` en la otra; `esp.equitacion` sale en una ejecución y no en la otra; las preguntas cambian entre ejecuciones.
- Sin id estable, los requisitos de una especialización nunca tienen regla de importancia propia.

## Diseño propuesto por Claude (sin decisión aparte)

- Las especializaciones son bloques del catálogo, con una regla citable `esp:<id>@<nodo>`.
- `bin/model blocks` muestra al clasificador las especializaciones de las verticales de su clase. Si una encaja con lo declarado, la usa por su id; si ninguna encaja, registra una nueva en ejecución, no compilada y encolada, como los bloques de categoría.
- Con ids estables, sus requisitos toman importancia y relevancia con las reglas de siempre. La clave lleva `esp.x@versión`.
- `train induce` añade la familia «especializaciones»; `train compile` la valida con la puerta de siempre, que suma la estabilidad de la clave y la de las especializaciones. El informe lista cada regla `esp:` con sus casos.

## Decisiones del usuario (las cuatro, la recomendación de Claude)

1. **Sinónimos** (`esp.a-bateria` y `esp.bateria`): «Determinista». Por las palabras significativas del nombre y del disparador, dentro de la misma vertical de Shopify. El id canónico es el más frecuente.
2. **Admisión** (cuándo pasa a compilada una especialización propuesta en ejecución): «Solo la puerta de métricas». Sin umbral de casos: se compila si ninguna métrica empeora y alguna mejora. Sigue al canon del criterio («No se fija ningún umbral numérico»).
3. **Nivel de anclaje** (condición 5 del criterio): «El árbol, como la importancia». Se ancla en la clase donde se observa. Sube a la madre si al menos dos hijas con datos la comparten. No sube por encima de las verticales.
4. **Requisitos del bloque**: «Semilla + propuestas». La primera propuesta registrada es el bloque, como pasa con los bloques de categoría. Lo que otros casos propongan de más entra como propuesta al bloque, como en D-088.

## Lecturas de Claude al construirlo (demand-engine, T-090)

- **Sinónimos:** se comparan el nombre y el id, sin tildes; el disparador no, porque en las salidas del reglamento v3 es la evidencia de la ficha (texto largo y propio de cada página). Dos ids son la misma especialización si comparten al menos la mitad de sus palabras significativas. Si una ya está compilada, conserva su id; si no, gana la más observada y, en un empate, la primera por orden alfabético.
- **Puerta:** suma una tercera métrica, «especializaciones sin compilar en los modelos», que debe bajar. Sobre ejecuciones ya hechas, la puerta solo ve los sinónimos fusionados y lo que se compila; el efecto en el clasificador lo mide la pasada siguiente. La estabilidad de las especializaciones se mide por id (con los sinónimos fusionados), no por la semejanza de los nombres.
- **Marco:** no se compila una especialización sin apoyo en las referencias (D-024), con un orden fuera del reglamento o con un requisito sin pregunta, sin rasgo o sin información resolutiva (D-063).
- **Nivel:** sube a la madre cuando al menos dos hijas la tienen y todas sus hijas con datos la tienen (el mínimo estructural de las reglas de importancia). Se conservan los anclajes ya registrados: no hay datos en contra.
- **Semilla:** en las ejecuciones del reglamento v3, sin registro, es la primera propuesta admisible en el orden de las ejecuciones; su disparador es su nombre. Una propuesta queda cubierta por el bloque si el bloque tiene la mitad de sus palabras significativas o si ella tiene todas las de una pregunta del bloque. Una propuesta sin información resolutiva no entra.
- **Juego:** se muestra al clasificador en cualquier clase, porque une categorías distintas (D-086).
- **Sin cambio:** la composición, las propiedades de Amazon y las inferidas siguen solo medidas (OQ-49).
