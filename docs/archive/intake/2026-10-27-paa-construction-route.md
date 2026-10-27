# PAA como vía de construcción del modelo de demanda, MPIR aparcado y excepción de legitimidad

Fecha: 2026-10-27. Tarea T-039. Cierra OQ-57.

Origen: las sondas de People Also Ask (PAA) sobre la clase de sábanas (2026-10-26) y el motor PAA (T-037, `demand-engine/src/demand_engine/paa/README.md`). Las decisiones del usuario están en ese README (legitimidad, límites de ejecución) y en el objetivo de T-039 («adopte PAA como vía de construcción del modelo de demanda (enmienda D-009 y D-036, MPIR aparcado) y registre la excepción a D-042 para el robots.txt de Google (investigación y uso interno), con los límites de ejecución decididos»). La etiqueta de origen (§4) y el alcance de «aparcado» (§2) son propuesta de Claude, que T-039 encarga definir.

## 1. PAA, vía de construcción del modelo de demanda

Las preguntas de «Más preguntas» (People Also Ask) de google.es, recogidas para un conjunto de semillas de una clase, son una **vía de construcción** del modelo de demanda. Son preguntas de los compradores, filtradas por Google. Sirven para:

- **reconocer criterios de elección** de la clase (las preguntas valorativas), a los que se aplica la regla C1–C4 (D-091);
- **confirmar requisitos** del catálogo;
- **confirmar o revisar cuestiones inferidas**: lo que D-036 encargaba al MPIR «cuando exista» lo hace PAA.

Solo se conservan las **preguntas**. Las respuestas son texto de la IA de Google («Vista creada con IA»), no evidencia de ninguna página: ni se leen ni se cargan. PAA no aporta información resolutiva.

Como cualquier fuente, PAA no prueba por sí sola la importancia relativa, que sigue saliendo de las reglas. Que una pregunta aparezca, o en qué posición, no se puntúa.

La estrategia de semillas (núcleo + valores del rasgo que más condiciona las prestaciones, 8 clics) es operativa y vive en el README del motor; está calibrada con una sola clase.

Enmienda D-009 y D-036.

## 2. MPIR aparcado

El MPIR queda **aparcado**: su método sigue en el canon como propuesta, pero no se ejecuta ni se desarrolla por ahora. Mientras esté aparcado:

- su papel en la construcción (reconocer criterios de elección y confirmar cuestiones inferidas) lo cumple PAA;
- las cuestiones abiertas del MPIR siguen abiertas, sin trabajarse;
- el motor de captura sigue en uso, porque es compartido con el entrenamiento (D-046).

Retomarlo es una decisión nueva.

## 3. Excepción a D-042: robots.txt de Google

El robots.txt de Google excluye `/search` para cualquier agente (`User-agent: *`, `Disallow: /search`), y sus condiciones de servicio (España, vigentes desde el 30-07-2026) prohíben el acceso automatizado que lo contravenga. El motor de captura aplica robots.txt a todas sus capturas (D-042); **el motor PAA no lo hace**.

Es una **excepción que decidió el usuario para investigación y uso interno**, no para ofrecer un servicio. Se limita a las búsquedas del motor PAA en google.es. No se extiende a ninguna otra captura, que sigue con las políticas de acceso de D-042.

Del principio del motor de captura se mantiene todo lo demás:

- Chrome estable con ventana, sin banderas de automatización, con perfil y puerto propios.
- Una sola ventana y una sola sesión: las búsquedas nunca van en paralelo.
- Bloquea las peticiones de las respuestas de IA, como haría un bloqueador de contenido; no modifica el navegador ni el JavaScript de la página.
- Ante un desafío (`/sorry/`, CAPTCHA, 403/429) **para**: no lo resuelve, no rota IP y no aplica parches antidetección.

**Límites de ejecución** (decididos por el usuario el 2026-10-26 y el 2026-10-27):

| Límite | Valor |
|---|---|
| Búsquedas a la vez | Una |
| Pausa entre búsquedas | 5 s |
| Pausa larga, horario, tope diario y tope por hora | Ninguno |
| Clics por búsqueda | 8, con parada tras 2 sin nada nuevo |
| Ante un bloqueo | Para todo el motor; reintento a las 6 h; tras el segundo, parado hasta que una persona lo desbloquea |

Los límites se endurecen cuando Google bloquee, no antes: primero una pausa larga cada cierto número de búsquedas y, si no basta, una pausa mayor entre búsquedas, con valores fijados por lo observado en ese bloqueo.

**Riesgo asumido:** la IP es la de la conexión desde la que se ejecuta. Si Google la marca, también verá CAPTCHAs quien busque desde ella.

## 4. Etiqueta de origen «paa»

Un requisito que entra en el catálogo **solo** por PAA (un criterio de elección que cumple C1–C4 y que ninguna referencia recoge) lleva origen **«paa»**, con las preguntas que lo apoyan como fuentes. Se suma a «referencias», «normativa» e «inferida».

- Si una referencia o una norma lo recoge, conserva su origen; las preguntas PAA se añaden como apoyo.
- Una cuestión inferida que PAA confirma pasa a origen «paa», con sus preguntas como fuentes.
- «paa» es un origen de requisitos, no de aportaciones resolutivas: PAA no aporta información resolutiva.
- Como las inferidas, la auditoría puede informar con ellos y sin ellos.
