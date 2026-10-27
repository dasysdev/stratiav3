# Criterios de clasificación de las preguntas PAA (segunda ronda)

Fecha: 2026-10-27. Tarea T-041. Sigue a `INTAKE 2026-10-27-paa-classification-criteria`.

## Contexto

El conjunto `sabanas` se volvió a clasificar con el reglamento PAA v2, que recoge D-100 a D-107. Lo general salió como se había acordado, pero el agente se apartó de lo decidido en varios puntos donde la regla era ambigua o no llegaba al caso. El usuario resolvió cada punto con Claude, paso a paso, eligiendo entre alternativas. Las decisiones que siguen son del usuario.

## 1. Prueba (a) de la separación por dimensión

El agente separó el secado de la lista de resistencias con una sola pregunta: «¿Qué seca más, la microfibra o el algodón?». Esa pregunta nombra dos materiales y además es comparativa, así que el agente la contó para las dos pruebas.

Decisión del usuario:

- **La prueba (a) exige preguntas distintas** sobre dos o más materiales o tejidos.
- **Una misma pregunta no cuenta para (a) y (b) a la vez.**

Con esta regla, el secado se queda en la lista.

## 2. Lista ausente en la clase

Las listas de Amazon (`special_feature`) existen en las fundas, pero no en las sábanas: los PTD de sábanas no la traen. El agente convirtió cada valor preguntado en un candidato suelto (encogimiento, transpiración).

Decisión del usuario:

- Si la clase no tiene la lista y un bloque hermano sí, el candidato es **la misma lista**, con la misma pregunta (D-107) y sin los valores que se separaron. Las preguntas sueltas apoyan esa lista.
- Si no hay lista en ningún bloque hermano, los valores se agrupan por tema (D-043, criterio 2).

## 3. Cualquier atributo de lista

Con la regla general D-106, el agente dio por cubierta la piel en sábanas. `cat.sabanas/02` («¿Qué otras certificaciones o estándares de producto acredita…?») recoge la declaración de hipoalergenicidad, y la regla dice que entonces la cubre. El usuario había decidido otra cosa para el caso: sacar esa declaración a un requisito de piel.

`cat.sabanas/02` sale del atributo de Shopify `product-certifications-standards`, que es una lista de reclamos con la misma estructura que `special_feature`.

Decisión del usuario:

- **La separación por dimensión vale para cualquier atributo de lista de una referencia**, de Amazon o de Shopify, incluidas las listas de certificaciones.
- D-106 rige cuando PAA no muestra la dimensión.

Así, la decisión de la piel se deduce de las reglas:

- (a): «¿Qué hace el bambú en la piel?» y «¿Por qué es bueno dormir con funda de seda?», preguntas distintas sobre materiales distintos;
- (b): «¿Por qué es bueno dormir con funda de seda?».

## 4. Preguntas de grado

La única pregunta de tacto es «¿Por qué las sábanas de los hoteles son tan suaves?». El agente concluyó que no genera, porque se pregunta por el grado (D-105). El ejemplo del canon la releía sobre la oferta y concluía que sí genera.

Decisión del usuario (regla general):

- **Una pregunta de grado** («tan suaves», «las más frescas», «cuál se arruga menos») indica el aspecto.
- **C2 se juzga sobre el requisito, formulado por tipo o por declaración.** Si la oferta puede declarar el tipo, la pregunta de grado apoya ese requisito.
- No genera cuando el aspecto solo admite más o menos y ninguna categoría declarable lo resuelve (la marca, C4).
- D-105 es la aplicación de esta regla al tacto: el tacto genera.

## 5. Sujeción de la bajera

El agente propuso un candidato: «¿Qué sujeción al colchón ofrece la bajera (se mantiene en su sitio sin salirse ni desplazarse)?». Lo apoyan «¿Cómo hacer para que no se salga la sábana de abajo?» y «¿Qué sábanas no se salen?».

El ejemplo del canon lo daba por cubierto con:

- `inf/02`: «¿Cómo se ajusta la bajera al colchón…?»;
- `cat.sabanas-ajustables/01`: «¿Hasta qué altura de colchón se ajusta…?».

Decisión del usuario: **genera candidato** (rasgo `prestacion`, en `cat.sabanas-ajustables`). De cómo se ajusta y hasta qué altura llega solo se deduciría que no se sale (D-090). La resuelve la declaración de sujeción o un ensayo del elástico. El ejemplo del canon cambia.

## 6. Ya decidido, para el reglamento

D-108 ya recoge que el «efecto frío al tacto» es un tipo de tacto y que la variedad y el origen de la fibra son candidatos distintos. El reglamento PAA v2 no lo recogía y se añade en la v3.

La acción «sacar» un valor de su lista no necesita preguntas de apoyo: se justifica por el tema de la lista.
