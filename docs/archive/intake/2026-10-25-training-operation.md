# Operación del entrenamiento (primera versión) y motor de captura compartido

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-019). Lo forman la propuesta de Claude para la primera versión del motor de demanda, la objeción del usuario al punto 2 y la opción que la sustituye, el matiz del usuario sobre el entrenamiento y los ajustes aprobados. La ortografía de los mensajes del usuario está normalizada.*

## 1. Propuesta de Claude para la primera versión

Lo que falta para probar productos reales: la ejecución de principio a fin, las reglas de importancia y un entrenamiento mínimo. Decisiones sobre OQ-47 e I-19:

| # | Decisión | Recomendación |
|---|---|---|
| 1 | Rasgos de un requisito | Rasgo principal: qué resuelve la cuestión, de una lista cerrada: identidad, contenido, medida que fija lo vendido, medida descriptiva, material, construcción, prestación, uso y compatibilidad, seguridad, cuidado, estética y certificación u origen. Además, los rasgos que ya tenemos: entidad, origen, aplicabilidad y posición del bloque. Cada atributo de Shopify o propiedad de Amazon se etiqueta una sola vez y se reutiliza en todas las categorías; así una categoría nueva hereda casi todo ya etiquetado. |
| 2 | Cómo se inducen las reglas de importancia | (Sustituida por la opción C, sección 2.) |
| 3 | Métricas, sin umbrales inventados | Cobertura: las cuestiones clave esperadas que aparecen en el modelo (solo en los casos que tienen resultado esperado). Estabilidad: el mismo resultado en dos ejecuciones (composición, bloques, importancia). Coherencia: cuántos requisitos con los mismos rasgos tienen importancias distintas. Una regla se acepta si ninguna métrica empeora y al menos una mejora. |
| 4 | Casos de entrenamiento | (Ajustado en la sección 4.) |
| 5 | Cómo se ejecuta | A: un comando de Claude Code (`/demand-model URL`) que lanza los agentes y llama al código determinista. B: código Python que llama a la API de Anthropic. Recomendada A. |
| 6 | Alcance de esta versión | Inducción solo para la importancia. Para la composición, las especializaciones, la relevancia de Amazon y las inferidas, se miden las divergencias y el informe las agrupa por patrón, pero sus reglas se inducen en la versión siguiente. |
| 7 | I-19 | La clave del modelo lleva la versión de cada bloque. Un bloque generado en ejecución lleva el estado «no compilado» hasta que el entrenamiento lo compila. |

Explicación del punto 2 original, pedida por el usuario: cada requisito lleva una etiqueta que dice de qué trata; la regla sale de mirar qué importancia tienen hoy los requisitos con la misma etiqueta; las excepciones constantes dan reglas específicas; los agentes proponen en cada producto nuevo la importancia que darían («votos»), pero manda la regla; si muchos votos contradicen una regla, el entrenamiento la cambia si las métricas mejoran; el marco pone límites que ninguna regla puede saltarse (ninguna regla puede hacer crítica la estética, ni tocar la capa general ni el criterio de las medidas).

## 2. Objeción del usuario al punto 2 y opción que lo sustituye

Usuario: «Ok. Lo único que no me encaja es que se mire a nivel global. Estas reglas deberían ser al menos para clases generales. ¿Qué opinas, sin sesgos?»

Respuesta de Claude:

- Por qué no encaja lo global: la prueba de «principal» se define respecto a la clase (D-035: «uno de los criterios con los que se comparan y eligen ofertas de la clase»), y una regla global arrastraría el sesgo del catálogo actual, casi todo textil del hogar.
- Lo que se pierde si se hace solo por clase: pocos datos por clase, y una clase nueva no tendría ninguna regla.

| | Cómo funciona | A favor | En contra |
|---|---|---|---|
| A. Global | Una regla por etiqueta para todo | Muchos datos | Contradice D-035 y arrastra el sesgo textil |
| B. Solo por clase | Reglas por categoría, aisladas | Fiel a D-035 | No generaliza: casi una regla por requisito |
| C. Por el árbol de Shopify | La regla vive en la clase y sube a la categoría madre solo si vale para todas sus hijas | Fiel a D-035 y generaliza donde los datos coinciden | Más reglas y un informe más largo |

Recomendada C, con el mismo principio que D-043, criterio 4 (una propiedad sube a la madre solo si vale para todas las hijas), y dos matices:

- **El crítico sí es global.** Su prueba no depende de la clase: sin la cuestión, ¿se sabe qué se vende, cuánto cuesta y si se puede adquirir? Por eso la capa general y la medida que fija lo vendido valen para todo.
- **Si una clase no tiene regla todavía** (por ejemplo, el primer producto de electrónica), no se le aplica una regla de otra rama: se usa la importancia que propone el agente, marcada como provisional y encolada, como ya prevé D-044 para lo no compilado. Cuando haya suficientes casos de esa rama, el entrenamiento compila sus reglas.

Ejemplo: «estética → complementario» sube a Ropa de casa si así está en mantas, sábanas y toallas; si en Cojines decorativos la estética es principal, esa regla se queda en Cojines y la de arriba no se aplica ahí.

Usuario: «Sí.» (aprueba la opción C y el resto del plan).

## 3. Matiz del usuario sobre el entrenamiento

«Un matiz sobre el entrenamiento que convendrá probablemente una tarea aparte. El entrenamiento lo vamos a hacer con un catálogo de miles de productos de diferentes tipos. Deberá usar el motor de captura del MPIR, que está preparado para el scraping. Entonces el motor de captura ya no es algo exclusivo del MPIR. Es algo que nos permite capturar información de ecommerce de referencia. Tenemos un motor de captura compartido para el modelo de taxo y MPIR. ¿Lo has entendido?»

## 4. Ajustes propuestos por Claude y aprobados

- **Casos de entrenamiento:** el conjunto de entrenamiento será un catálogo grande capturado por el motor. Los 14 casos actuales quedan como conjunto de control: son los únicos con resultado esperado y sirven para detectar si algo empeora.
- **Cobertura:** con miles de fichas nadie escribe lo esperado. Se cuentan los hechos que declaran las fichas de una clase (materiales, medidas, funciones…) y cuántos no tienen ninguna pregunta en el modelo: cada hecho sin pregunta es un hueco. Lo estético y lo promocional no cuentan (el clasificador ya los separa). Se mide sola y mejora con el volumen.
- **Ejecución:** para probar productos reales ahora, un comando de Claude Code; para entrenar con miles de fichas no escala y hacen falta llamadas a la API por lotes (tarea aparte).
- **Reglas por el árbol (opción C):** encajan mejor, porque con miles de fichas casi todas las ramas tendrán datos para compilar sus propias reglas.
- **Reparto:** ahora, documentar, montar la ejecución completa, compilar las reglas de importancia con el catálogo actual, pasar los 14 casos de control y entregar el comando. En una tarea aparte (entrenamiento a escala): elegir qué tiendas y qué fichas forman el catálogo (sin Amazon.es), mover el motor de `mpir/` a un módulo de captura común, pasar a la API por lotes y montar el ciclo de entrenamiento completo. El cambio de código del motor se deja para esa tarea, porque otra sesión trabaja con él (T-014, T-015); en la documentación solo se declara que el motor es compartido, sin reescribir sus módulos.

Usuario: «Sí.»
