# Criterios de clasificación de las preguntas PAA

Fecha: 2026-10-27. Tareas T-040 (clasificador de preguntas PAA con un agente) y T-041 (resolución de sus dudas).

## Contexto

T-040 clasificó con un agente las 200 preguntas PAA del conjunto `sabanas` (reglamento `demand-engine/classifier/paa.md` v1; resultado en `demand-engine/var/paa/sets/sabanas/report.md`). El resultado dejó dudas. El usuario las resolvió paso a paso con Claude: Claude analizó cada una y propuso, y el usuario decidió. Lo que sigue son esas decisiones. Las que interpretan la regla C1–C4 (D-091), D-094, D-099 y D-043 son canon. El detalle operativo va al reglamento del agente.

## 1. Lectura sobre la oferta

El agente había aplicado C2 a la pregunta tal como está escrita. Por eso cayeron en C2 cosas muy distintas: «¿Qué es una sábana encimera?», «¿Qué significa 144 hilos?», «¿Cómo coser una bajera?», «¿Cada cuánto se cambian las sábanas?»…

Decisión del usuario, sobre la propuesta de Claude:

- **Antes de aplicar C2 a una pregunta de clase, se relee sobre la oferta:** «¿… esta oferta?».
  - Si un hecho que la oferta puede declarar la responde, la pregunta confirma ese requisito o propone un candidato.
  - C2 solo se aplica cuando ningún hecho de la oferta la responde: hábitos («¿cada cuánto se lavan?»), saber doméstico («¿cómo se dobla?»).
  - Ejemplo: «¿Qué es una sábana encimera?», releída como «¿qué es esta pieza?», confirma `gen/01`.
- **La confección casera** (coser, hacer o arreglar la pieza) queda **fuera del perímetro**: no hay compra.
- La misma lectura vale para el **perímetro dudoso**. «¿Cuáles son las contraindicaciones del bambú?» va dentro, porque responde a las advertencias y a los efectos sobre la piel que declara la oferta. «¿Qué país produce la mejor seda?» también va dentro: es el origen de la fibra (§9). Las curiosidades («¿Cuál es la seda más cara?») siguen fuera.

## 2. Preguntas por el significado de un término

«¿La microfibra es plástico?», «¿Qué significa 144 hilos?», «¿Qué significa *full* en las sábanas?», «¿Cómo se llama la seda falsa?».

Decisión del usuario: **confirman el requisito del atributo** y proponen **aportaciones de precisión** para él, como estas:

- la denominación de la fibra según el Reglamento (UE) 1007/2011 («poliéster», no «microfibra»);
- la unidad del recuento de hilos;
- la equivalencia en cm de una denominación de talla.

No generan requisitos nuevos.

## 3. Apoyo mínimo de un candidato

Decisión del usuario: **basta una pregunta** para que un candidato que cumple C1–C4 entre como tal. La presencia de una pregunta no se puntúa (D-094) y D-099 admite la pregunta como fuente. Este apoyo es para que el requisito **exista**. Para **separar** un requisito hace falta otra prueba (§4).

## 4. Separación por dimensión (atributos de lista)

`cat.fundas-de-almohada/06` agrupa 11 valores de `special_feature` de Amazon de tres temas: durabilidad, mantenimiento y confección. El agente separó las arrugas solo porque les votó otra importancia.

Palabras del usuario:

> en general sería A. pero debería haber algún criterio de separación más sofisticado. /06 me inclino más a como amazon lo plantea y con arrugas por separado ya que PAA le da ese apoyo. Discutámoslo. no lo planteo como una regla universal. quiero que entendamos y construyamos un criterio de esta reflexión.

De la discusión salió este criterio, que el usuario aprobó («si»; «usamos las 2 pruebas»; el dobladillo, «sí, sácalo»):

- **Ámbito:** un **atributo de lista** de una referencia (como `special_feature`), cuyos valores son reclamos que la oferta marca o no. No es una regla universal de formulación.
- **La lista se mantiene agrupada** como la plantea la referencia. Sus valores son extras: importan solo si la oferta los reclama.
- **Un valor se separa en requisito propio** cuando PAA muestra que es una **dimensión de comparación de la clase**: algo que quien compra quiere saber de cualquier oferta, la reclame o no. Hacen falta **las dos pruebas**:
  - **(a) Transversal:** se pregunta sobre dos o más valores del rasgo que más condiciona las prestaciones (el material o el tejido).
  - **(b) Comparativa o de elección:** se compara («¿qué se arruga más?») o se elige por ello («¿cuáles se arrugan menos?»).
- Es un criterio de **estructura** (cuándo partir), no de **existencia** (§3).
- Lo que no pertenece al tema de la lista sale de ella aunque la referencia lo incluya. Por ejemplo, el «dobladillo con doble vuelta» es confección, no resistencia.

Aplicado a `/06` en sábanas:

- Solo las **arrugas** pasan las dos pruebas: seis preguntas, cuatro materiales, comparativas y valorativas.
- La duración, el encogimiento y el secado quedan en una lista encabezada por la duración: «¿Qué duración y resistencia al uso y al lavado tiene…?».

Complementa D-043, criterio 2 (división por tema), y D-060, regla 3.

## 5. Dimensión térmica

Decisión del usuario, sobre la propuesta de Claude:

- **El frescor y el abrigo son una sola dimensión con dos polos.**
  - PAA pregunta lo mismo desde los dos lados y sobre el mismo material: «¿Las de microfibra dan calor?» / «¿Son frescas las de microfibra?».
  - La cuestión inferida `inf/01` se reformula para cubrir los dos: «¿Qué nivel de abrigo o de frescor ofrece (fresca de verano, para todo el año, cálida de invierno)?».
  - PAA la confirma, así que pasa a origen «paa» (D-097).
- **La transpiración y la gestión de la humedad y el sudor** quedan como lista agrupada, como la trae Amazon (`fundas/05` sin el frescor). No pasan las dos pruebas de §4.
- **El «efecto frío al tacto»** (Amazon «Enfriamiento») va al tacto (§7).

## 6. Criterios intermedios y pertinencia de los criterios de aceptación

El criterio valorativo «material» reunía 40 preguntas: «¿Qué es mejor, lino o algodón?», «¿Son malas las de microfibra?», «beneficios del bambú»… El agente lo dio por cubierto solo con la composición.

Palabras del usuario:

> Podría ser un requisito. Se me ocurre buen candidato para evaluar los AC. Si es muy comparable, verificable, etc. No sirve para evaluar si existen las funciones informativas para saberlo. Estudiémoslo, todavía no tengo clara la respuesta.

Tras el estudio, el usuario eligió esta síntesis:

- **Un criterio intermedio queda cubierto y se descompone en las prestaciones.** Es el caso del «material» y de la «calidad».
  - El «material» lo cubre la composición en cuanto a qué material es (funciones Comprender y Comparar).
  - En cuanto a si es mejor, se descompone en las prestaciones (función Evaluar): nivel térmico, arrugas, duración y resistencia, humedad, tacto y piel.
  - Deducir esas prestaciones del material es lo que D-090 no admite.
- **Una pregunta genérica** («¿es bueno el lino?», «beneficios del bambú») no nombra ninguna prestación. Apoya la composición, pero no a una prestación concreta, y no cuenta para las pruebas de §4. Solo apoya una prestación la pregunta que la nombra.
- **Propuesta, todavía sin decidir:** PAA como **prueba de qué criterios de aceptación son pertinentes para un requisito**.
  - La pertinencia de cada AC depende del requisito (acceptance-criteria, regla 5) y la Comparabilidad se evalúa cuando la cuestión requiere contraste (regla 6).
  - Para la composición, las preguntas prueban tres pertinencias:
    - Comparabilidad: 11 preguntas comparan materiales.
    - Precisión: «¿La microfibra es plástico?».
    - Fiabilidad: «¿Cómo saber si es 100 % seda?».
  - Para el precio, las preguntas por el precio de cada material prueban la pertinencia de la Comparabilidad.
  - Sería un uso nuevo de PAA (no de importancia) y se registra como cuestión abierta.

## 7. Tacto y rasgo «sensorial»

Decisiones del usuario:

- **El tacto cumple C2** si se pregunta por el **tipo de tacto** (sedoso o liso, crujiente, afelpado, fresco al tacto). No lo cumple si se pregunta por el grado de suavidad: eso solo admite más o menos.
  - Ninguna referencia lo recoge en sábanas ni fundas, así que entra con origen «paa».
- **Rasgo nuevo «sensorial»** en el vocabulario (D-056). El entrenamiento reclasifica los requisitos de tacto que ya existen (`cat.toallas/05` y `cat.mantas/08`, hoy `prestacion`).

## 8. Certificación y prestación; piel

Decisiones del usuario:

- **No se adopta** como regla general que un requisito de certificación no cubra la prestación que certifica. Si el requisito de certificaciones recoge la declaración (por ejemplo, «hipoalergénico»), la cubre.
- **En sábanas, el efecto sobre la piel genera candidato** (rasgo `prestacion`, origen «paa»).
  - La hipoalergenicidad y la aptitud para pieles sensibles **pasan** de `cat.sabanas/02` a ese requisito.
  - `sabanas/02` queda en certificaciones y estándares (sin formaldehído, vegano…).
- **`cat.fundas-de-almohada/04` se parte por tema** (D-043.2): efecto en la piel y el cabello, y protección de la almohada (ácaros, chinches, manchas).

## 9. Variedad y origen de la fibra

Decisiones del usuario:

- **Variedad o calidad de la fibra** (algodón Pima o de fibra larga, seda de morera…): se explora como candidato, separado del tratamiento del hilo (peinado, mercerizado), que es construcción.
- **Origen de la fibra** (país o región de cultivo o producción: lino europeo, algodón egipcio…): candidato propio, de origen «paa». Palabras del usuario:

  > gen/20 habla del país de fabricación. no es lo mismo que el origen del material. Es posible que aquí haya requisito nuevo, pero derivado de PAA (porque se pregunta)

## 10. Bloques hermanos

Decisiones del usuario:

- **D-043, criterio 4, tal cual.** Un candidato que vale para sábanas y fundas, pero no para todas las hijas de Ropa de cama (doseles, cubrecanapés, almohadas…), no sube a `cat.ropa-de-cama`: se repite en las hermanas. Esto corrige la propuesta del agente.
- **Un requisito repetido en bloques hermanos lleva la misma pregunta y la misma descripción.** Palabras del usuario:

  > lo de la descripción que digo quizás es un tema de construcción de presentación. Así que la respuesta correcta es la primera.

  Adaptar la descripción a la pieza sería un tema de presentación, no del catálogo.

## 11. Otras confirmaciones

Decisiones del usuario:

- Una pregunta de **tienda o marca que nombra un atributo** («¿Dónde comprar sábanas 100 % algodón?») confirma el requisito de ese atributo: quien compra busca y filtra por él (función Descubrir). Sigue sin proponer requisitos (D-099).
- El **precio sin tienda** («¿Cuánto cuesta una sábana de lino?») es una pregunta de clase y confirma `gen/04`.
- La **verificación** («¿Cómo saber si es 100 % algodón?») confirma la composición y propone la aportación «certificación del contenido o del origen de la fibra».

## 12. Ejemplos del canon desfasados

Los ejemplos de `choice-criteria` (ejemplo mínimo) y de `requirement-description` (`fundas-de-almohada/06`, que incluye las arrugas, y el candidato «¿Qué sensación térmica ofrece la sábana?») quedan desfasados por §4 y §5. Se actualizan.

Los requisitos de sábanas descritos aquí son **candidatos**: entran en el catálogo por el entrenamiento, no a mano.
