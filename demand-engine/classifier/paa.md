# Reglamento de clasificación de las preguntas PAA · v8

Procedimiento del **agente** que clasifica las preguntas de «Más preguntas» (PAA) de un conjunto de semillas. El agente decide el perímetro y el objeto de cada pregunta y la contrasta con el catálogo de la clase. Reconoce los **criterios de elección**. Propone **requisitos candidatos**, **revisiones** de requisitos existentes, **aportaciones**, **pistas de valoración**, **marcas de dimensión de comparación** y **especializaciones**. Condensa el canon (`docs/10-model/choice-criteria.md`, `construction-routes.md`, `demand-model.md`, `assessment-hints.md`, `quality-properties.md`; `docs/20-methods/product-taxonomy/requirement-blocks.md`). Cada regla cita la decisión de la que sale. Si el reglamento y el canon discrepan, prevalece el canon: anota la discrepancia en `doubts`.

**Redacción de la salida.** Escribe el texto libre (`note`, `why`, `rationale`, `proposal`, `reason`, `doubts`) con las reglas de estilo del proyecto:

- frases cortas, de 25 palabras como máximo;
- voz activa y un sujeto claro;
- verbos, no sustantivos derivados;
- los términos de este reglamento, siempre los mismos;
- la incertidumbre, una vez y con una palabra: «Causa probable: …».

Cambios de la v2 (D-100 a D-107): lectura sobre la oferta, confirmaciones y aportaciones, apoyo mínimo, separación por dimensión, criterios intermedios, tacto, certificaciones, bloques hermanos y revisiones. Cambios de la v3 (D-108 a D-110): preguntas distintas para la prueba (a), cualquier atributo de lista, lista ausente en la clase, preguntas de grado, efecto frío al tacto, necesidades distintas de una fibra y sacar sin preguntas. Cambios de la v4 (D-125 a D-128, D-139): el paso 8 escribe pistas de valoración y marcas de dimensión de comparación en lugar de la pertinencia de los AC. Cambios de la v5 (D-141, D-142): productos vecinos fuera, antes de la lectura sobre la oferta; moda, popularidad, preferencia general y alternativa de producto. Cambios de la v6 (D-146): la categoría madre va dentro en lo que la clase hereda de su bloque; el material, si la clase lo tiene o lo hereda; denominación ambigua. Cambios de la v7 (D-218; T-057, T-079): prueba de la respuesta natural para la madre; especializaciones desde PAA; redacción con las reglas de estilo, sin cambiar las demás reglas. Cambios de la v8 (T-106): ampliar un requisito solo vale para el mismo hecho.

## 0. Propósito

PAA es una vía de construcción del modelo de demanda (D-094). Sus preguntas son de compradores y sirven para:

- confirmar requisitos del catálogo y cuestiones inferidas;
- reconocer criterios de elección;
- proponer requisitos nuevos (D-099);
- proponer especializaciones de la clase (D-218).

Las preguntas **no** aportan información resolutiva. La aparición de una pregunta, o su posición, no prueba la importancia de nada (D-094).

Tú no cambias el catálogo ni decides importancias. Los candidatos, las revisiones, las aportaciones, las pistas, las marcas y las especializaciones son propuestas para el entrenamiento. Los candidatos entran con origen «paa» (D-097).

## 1. Entrada y salida

- **Entrada:** `classify/input.md` del conjunto. Contiene:
  - las preguntas numeradas, con las semillas que las mostraron;
  - el catálogo de la clase: capa general, bloques de la clave con sus fuentes y cuestiones inferidas;
  - las otras especializaciones de la clase en el catálogo, con sus requisitos;
  - las pistas de valoración que ya llegan a cada requisito y su marca de dimensión de comparación;
  - las hijas de cada bloque en la taxonomía;
  - el vocabulario de rasgos.
- **Salida:** `classify/output.json` (formato en §4). Comprueba la salida con `bin/paa classify check CONJUNTO`. Repite hasta que diga «correcto».
- Las semillas solo dan contexto. Ejemplo hipotético: «¿Abriga mucho?» desde «mantas de lana» trata de la lana de las mantas.

## 2. Procedimiento

### Paso 1 · Perímetro

**`dentro`:** la pregunta trata de los productos de la clase (sus categorías y especializaciones). También va dentro si trata de una característica de sus materiales, tejidos o piezas, tal como la vive quien compra en la clase.

**Categoría madre** (D-146). Ejemplo hipotético: «mochila» en una clase de mochilas escolares.

- Si la pregunta trata de algo que la clase **hereda de su bloque**, ponla dentro. Lo heredado es un requisito o una aportación de un bloque heredado, o un criterio de elección que vale igual para el producto de la clase.
- Si solo tiene sentido para otro producto, ponla fuera.
- **Prueba de la respuesta natural** (D-218). Si la pregunta pide elegir un producto de la madre para una necesidad, ponla dentro solo si un producto de la clase es una respuesta natural. Lo que la clase comparte con la madre (cuidado, material, precio) sigue dentro.
- Ejemplos hipotéticos, en mochilas escolares:
  - «¿Cómo se lava una mochila?»: dentro (cuidado heredado).
  - «¿Qué mochila me compro?»: dentro (preferencia general).
  - «¿Qué mochila es mejor para hacer trekking?»: fuera. Una mochila escolar no es una respuesta natural.
  - «¿Qué mochila recomiendan los fisioterapeutas para la espalda?»: fuera, por la misma prueba.
- No toques las semillas de la madre.
- Esta regla vale para la madre directa de la clase. Si la pregunta trata de una categoría más general (la abuela o el sector), ponla fuera. Ejemplo hipotético, en mochilas escolares: «¿Qué complementos se llevan este año?». Excepción: la pregunta por un requisito o una aportación heredados va dentro.

**Especializaciones** (D-218). Una pregunta puede tratar de una especialización de la clase: un tipo de producto de la clase por su uso, su material o su función.

- Si la especialización está en la clave o en «Otras especializaciones de la clase», pon su id en `specialization`.
- Si el catálogo no la tiene, propónla en `specializations` (S1, S2…) y pon ese id en `specialization`. Una especialización propuesta lleva nombre, orden y disparador.
- Lo que apoya una pregunta de una especialización va al bloque de esa especialización. No va a la categoría ni a la especialización del caso.
- No uses esa pregunta para confirmar el requisito de la clase que nombra el uso o el tipo.
- Propón una especialización solo para un tipo que el mercado nombra como tal. Un valor que solo cambia la respuesta de un requisito de la clase no es una especialización. Ejemplo hipotético: «chaqueta de lana» es un valor del material.
- La pregunta sobre la madre que pasa la prueba de la respuesta natural también puede ir a una especialización.
- Ejemplo hipotético, en una clase de chaquetas con un caso de chaqueta de esquí: «¿Cuáles son las mejores marcas de chaquetas de moto?» y «¿Qué prenda es mejor para ir en moto?» van a una especialización nueva, «de moto». No van a la de esquí ni a la categoría.
- Tú solo propones la especialización. El entrenamiento la admite con el criterio de especialización (D-216).

**`fuera`:**

- La pregunta trata de **otro producto** (D-141, D-146): un hermano, o la madre en lo que solo tiene sentido para otro producto. Ejemplo hipotético, en una clase de mochilas escolares: «¿Qué maleta de cabina es más ligera?» (un hermano). Ponla fuera **siempre**, aunque se pudiera releer sobre la oferta.
- La pregunta trata de textiles en general sin relación con la clase, o de curiosidades (el producto más caro del mundo, historia).
- La pregunta es de **confección casera:** coser, hacer o arreglar la pieza. No hay compra (D-100).

**Reglas comunes:**

- **Decide el perímetro antes de la lectura sobre la oferta** (D-141). La lectura del paso 5 no decide el perímetro. Solo decide si una pregunta sobre el producto de la clase pide un hecho declarable.
- **Un vecino nunca apoya requisitos de la clase:** ni `answered_by`, ni criterio, ni candidato, ni revisión, ni aportación.
- Si muchas preguntas de un conjunto son de vecinos, anótalo en `doubts`. Es una señal para las semillas (D-114).
- Una pregunta sobre un **material** que la clase tiene o hereda no es de un vecino: ponla dentro (D-100, D-146). Vale aunque no nombre el producto. Ejemplo hipotético, en una clase de esterillas de corcho: «¿Qué contraindicaciones tiene el corcho?» o «¿Cómo saber si es corcho natural?».
- Si una **denominación ambigua** no tiene señal del vecino, léela como la clase (D-146). Ejemplo hipotético, en una clase de batas de casa: «bata» sin señal de uso sanitario o de laboratorio es la clase.

Pertinencia no es proximidad temática (invariante 10). Que una pregunta hable de dormir o de tejidos no la pone dentro.

### Paso 2 · Objeto (solo si está dentro)

| Objeto | Cuándo | Ejemplo |
|---|---|---|
| `marca` | Pregunta por marcas, también si es valorativa. La marca como criterio no genera requisito (C4). | «¿Cuál es la mejor marca de sábanas en España?» |
| `tienda` | Pregunta dónde comprar, por una tienda o por los precios de una tienda. | «¿Dónde puedo comprar sábanas de algodón 100 %?» |
| `valorativa` | Pide un juicio que depende del comprador: mejor o peor, recomendación, si algo «es bueno» o «merece la pena». | «¿Qué es mejor, percal o satén?» |
| `clase` | Pregunta factual sobre la clase: qué es, medidas, precio (sin nombrar tienda), cómo se usa o se cuida, qué propiedad tiene un material o un tejido. | «¿Se encoge el lino al lavarlo?», «¿Cuánto cuesta una sábana de lino?» |

### Paso 3 · Contraste con el catálogo

En `answered_by`, pon los requisitos del catálogo (capa general, bloques, especializaciones o `inf/`) que **responden la pregunta sin derivar**. Son los que dan la respuesta para una oferta cuando la oferta los resuelve.

- **Un requisito responde solo si trata del mismo hecho.** Un requisito vecino no responde. Ejemplo hipotético: «¿Encoge el algodón al lavarlo?» no la responde «¿Cómo se lava?». Si ninguno trata del mismo hecho, sigue al paso 5.
- **El atributo del que se deduciría una prestación no responde.** Que la oferta declare «percal» o «100 % algodón» no dice si la sábana es fresca, si se arruga o si encoge (D-090).
- **Un requisito de certificaciones** responde una prestación solo si su información resolutiva recoge la declaración de esa prestación (D-106). Ejemplo: «declaración de hipoalergenicidad».
- **Salvedad** (D-109). Si las preguntas muestran que esa prestación es una dimensión de comparación de la clase (las dos pruebas del paso 7), propón separarla de la lista de certificaciones.
- **Confirmaciones** (D-101):
  - Una pregunta de **tienda o marca que nombra un atributo** confirma el requisito de ese atributo: quien compra busca y filtra por él. Ejemplo: «¿Dónde comprar sábanas 100 % algodón?».
  - El **precio sin tienda** confirma `gen/04`.
  - Una **verificación** confirma el requisito del atributo verificado. Ejemplo: «¿Cómo saber si es 100 % algodón?».
  - Una pregunta por el **significado de un término** confirma el requisito del atributo al que pertenece el término. Ejemplos: «¿Qué significa *queen*?», «¿Qué es el modal?».
- **Aportaciones** (D-101). Si una pregunta muestra que un término comercial no basta para resolver un requisito, propón una aportación de **precisión** para ese requisito en `contributions`. Ejemplos:
  - la denominación de la fibra según el Reglamento (UE) 1007/2011;
  - la unidad de un recuento;
  - la equivalencia en cm de una talla.
- Una verificación propone una aportación de **sustento**, como la certificación del contenido o del origen.
- Si la pregunta responde una cuestión inferida (`inf/…`), la confirma (D-097).

### Paso 4 · Criterios de elección

A cada pregunta valorativa, asígnale el **criterio de elección** que revela. Un criterio es el aspecto por el que quien compra juzga si una oferta le conviene (D-091).

- Usa un criterio por aspecto, con un id corto en minúsculas.
- Una pregunta de marca o de clase que trata del mismo aspecto puede llevar también ese criterio.
- Si un criterio mezcla aspectos que se juzgan por separado, divídelo.
- **Dos extremos del mismo eje son un solo criterio.** Ejemplo hipotético: «¿qué edredón abriga más?» y «¿cuál es el más fresco?».
- **Criterio intermedio** (D-104). Es un criterio que no es una prestación: «calidad», «material» o «tipo de tejido», cuando se pregunta cuál es mejor.
  - Márcalo `cubierto`. En `covered_by`, pon el requisito que dice qué es (la composición) y los requisitos o candidatos de las prestaciones en que se descompone.
  - Una **pregunta genérica** no nombra ninguna prestación. Ejemplos: «¿es bueno el lino?», «beneficios del bambú». Apoya el criterio intermedio, pero no una prestación concreta. No le pongas el criterio ni el candidato de una prestación.
  - Solo apoya una prestación la pregunta que la nombra.
- **Preferencia general** (D-142): «¿cuál es el mejor X?», «¿qué X me compro?», sin nombrar ningún aspecto. Es un criterio intermedio, como «calidad». Márcalo `cubierto`, con `"intermediate": true`, y descomponlo en las prestaciones. No es `no-genera`.

Aplica a cada criterio la regla C1–C4 (D-091). Un criterio genera un requisito solo si cumple **todas** las condiciones:

| # | Condición | Si no se cumple |
|---|---|---|
| C1 | Ningún requisito existente lo responde sin derivar. | `cubierto`, con los requisitos (o criterios, o candidatos) en `covered_by`. |
| C2 | Es un hecho que la oferta puede declarar: una prestación, un resultado de ensayo, una indicación de uso. | `no-genera`: solo lo juzga quien compra («que me guste»). |
| C3 | Se aplica a toda la clase o a una especialización, no a un comprador. | `no-genera`: es una condición de compra o un escenario. |
| C4 | Se puede formular neutral y sobre la oferta. | `no-genera`: solo admite «mejor o peor» (marca, reputación). |

- **Preguntas de grado** (D-110). Una pregunta de grado indica el aspecto. Ejemplos: «tan suaves», «las más frescas», «cuál se arruga menos».
  - Juzga C2 sobre el requisito, formulado por tipo o por declaración.
  - Si la oferta puede declarar el tipo, la pregunta de grado apoya ese requisito.
  - Solo no genera si el aspecto únicamente admite más o menos y ninguna categoría declarable lo resuelve (la marca, C4).
- **Moda o tendencia** (D-142): «¿qué X se llevan?», «¿qué X están de moda?», «tendencias en X para este año».
  - **Nunca genera.** Estar de moda depende del mercado y del momento, y ninguna oferta lo puede declarar (C2, o C4 si solo admite más o menos).
  - Es un caso de la excepción de las preguntas de grado.
  - Una oferta puede declarar su estilo, pero una pregunta de moda no apoya un candidato de estilo.
- **Popularidad** (D-142): «¿cuál es el X más vendido?». No genera: es reputación (C4). No se mide la conversión (invariante 14).
- **Alternativa de producto** (D-142): «¿qué es mejor, un X o un Y?», cuando X e Y son productos distintos que cubren la misma necesidad. Ejemplo hipotético: «¿mochila o trolley escolar?». No son dos valores de un atributo de la clase. Elegir entre dos productos depende de la situación de quien compra: no genera (C3).
- **Tacto** (D-105, D-110):
  - Formula el tacto por su **tipo** (sedoso o liso, crujiente, afelpado, fresco al tacto), no por el grado de suavidad.
  - Una pregunta por lo suave que es apoya ese requisito.
  - El **efecto frío al tacto** es un tipo de tacto, no un nivel térmico. Ejemplos de reclamo: «Enfriamiento», «tacto fresco». El nivel térmico es la temporada o el abrigo (D-108).
  - Su rasgo es `sensorial`, por decisión del usuario. Si aún no está en el vocabulario, declara su definición en `proposed_traits`.

### Paso 5 · Preguntas de clase

**Lectura sobre la oferta** (D-100). Antes de aplicar C2, relee la pregunta sobre la oferta: «¿… esta oferta?».

- «¿Qué es una sábana encimera?» → «¿qué es esta pieza?».
- Ejemplo hipotético: «¿Cómo se monta una lámpara de pie?» → «¿qué instrucciones de montaje trae esta?».

Si un hecho que la oferta puede declarar responde la pregunta, la pregunta confirma ese requisito o propone un candidato. Aplica C2 solo si **ningún** hecho de la oferta la responde. Ejemplos: hábitos («¿cada cuánto se lavan?»), saber doméstico («¿cómo se dobla?»), cantidades que dependen de quien compra (C3).

Cada pregunta de objeto `clase` acaba de una de estas tres formas:

1. **Respondida:** `answered_by` con uno o más requisitos.
2. **Candidata:** ningún requisito la responde y cumple C2–C4 (D-099). Lleva el `candidate` que propone. Si pertenece a un criterio que genera, lleva el candidato de ese criterio.
3. **No genera:** en `fails`, la primera condición que no cumple (`C2`, `C3` o `C4`).

**Basta una pregunta** para que exista un candidato que cumple C1–C4 (D-102).

### Paso 6 · Requisitos candidatos

Cada criterio que genera y cada pregunta de clase candidata dan un requisito candidato. Si varias preguntas piden lo mismo, propón **un** candidato.

- **Formulación:** aplica las cuatro reglas de D-060 (`catalog/DRAFTING.md`, regla 8):
  - una cuestión neutral y sobre la oferta;
  - una necesidad por requisito;
  - sin condiciones sobre la existencia de la información.
  - Ejemplo: la variedad de una fibra (seda de morera, algodón de fibra larga) y su origen geográfico (país o región de cultivo) son dos necesidades. Dan dos candidatos (D-108).
- **Lista ausente** (D-109). Caso: en un bloque de la clase falta un atributo de lista que tiene un bloque hermano. Las fuentes de esa lista son de un tipo de producto de la referencia que la clase no tiene.
  - Propón como candidato **la misma lista**: la misma pregunta, sin los valores que se separen, con su id en `mirrors`.
  - Las preguntas sueltas sobre sus valores apoyan la lista. No propongas un candidato por valor.
  - Si ningún hermano tiene la lista, agrupa los valores por tema (D-043, criterio 2).
- **Descripción** (`description`, D-092), en tres partes:
  1. qué se pregunta en concreto, con ejemplos de lo que abarca;
  2. qué tipo de información lo responde;
  3. qué no lo responde y con qué requisito vecino no se confunde.
- **Información resolutiva** (`resolving_info`): la declaración de la prestación, un ensayo o una certificación. **Nunca** pongas el atributo del que se deduciría la prestación (D-090). Son aportaciones inferidas: PAA no aporta información resolutiva (D-097).
- **Bloques** (`blocks`; D-043, criterio 4; D-107). Mira las hijas de cada bloque en la entrada.
  - Pon el candidato en el bloque más alto de la clave cuyo requisito valga para **todas** sus hijas.
  - Si no vale para todas las hijas de la madre común, el candidato **no sube**. Ejemplo: una hija cuyo producto no tiene esa propiedad. Repítelo en cada bloque hermano al que se aplica, con la **misma pregunta y la misma descripción**.
  - Si el candidato es de una especialización, ponlo en el bloque de esa especialización: su id del catálogo o su S (D-218).
- **Rasgo** (`trait`): uno del vocabulario, o uno de `proposed_traits` con su definición.
- **Voto** (`vote`): aplica las pruebas de `catalog/DRAFTING.md` (regla 5). La importancia la deciden las reglas del entrenamiento. Que los compradores pregunten no la prueba.
- **Origen:** «paa». El código pone las fuentes: las preguntas que apoyan el candidato.

### Paso 7 · Revisiones de requisitos existentes

Si las preguntas muestran que un requisito del catálogo debe cambiar, propón una **revisión** en `revisions`. Tipos (`action`):

| Acción | Cuándo |
|---|---|
| `separar` | **Separación por dimensión** (D-103, D-109). Vale para **cualquier atributo de lista** de una referencia, de Amazon o de Shopify, también las listas de certificaciones: sus valores son reclamos que la oferta marca o no.<br>Mantén la lista agrupada como la plantea la referencia. Separa un valor en un requisito propio solo si PAA lo muestra como **dimensión de comparación de la clase**. Pon **las dos pruebas** en `tests`:<br>(a) **transversal**: **preguntas distintas** sobre dos o más materiales o tejidos;<br>(b) **comparativa o de elección**: «¿qué X más?», «¿cuál X menos?».<br>**Una misma pregunta no cuenta para (a) y (b) a la vez.** Las preguntas genéricas no cuentan. El valor separado es un candidato (en `into`). |
| `sacar` | Un valor de la lista no pertenece a su tema. Ejemplo: una confección en una lista de resistencias. El valor sale de la lista aunque la referencia lo incluya (D-103). No necesita preguntas de apoyo (D-109). |
| `partir-por-tema` | El requisito mezcla temas o beneficiarios distintos (D-043, criterio 2). Ejemplo hipotético: «protección de la piel o del colchón». |
| `reformular` | La pregunta del requisito se queda corta para lo que PAA muestra. Ejemplo: una inferida que solo cubre un extremo de un eje. Una inferida que PAA confirma pasa a origen «paa» (D-097). |
| `mover` | Una aportación está en un requisito y pertenece a otro (a un candidato, por ejemplo). |

Cada revisión lleva:

- el requisito (`target`);
- la propuesta, en prosa;
- las preguntas que la apoyan (salvo `sacar`);
- los candidatos que crea, si los crea.

Aplica igual en todos los bloques hermanos la revisión de un requisito repetido en ellos (D-107).

Cuándo escribir una revisión en lugar de un candidato:

- Si lo que muestra la pregunta cabe en un requisito existente al ampliar su pregunta, propón `reformular`. No propongas un candidato. Ejemplo hipotético: «¿Se deshilacha la tapicería?» amplía «¿Qué resistencia al desgaste declara?».
- Ampliar solo vale para el mismo hecho (prueba del paso 3). Si la pregunta trae otro hecho, propón un candidato. Ejemplo hipotético: «¿Encoge el algodón al lavarlo?» no amplía «¿Cómo se lava?».
- Si una pregunta confirma una cuestión inferida (`inf/…` o un requisito de origen «inferida»), escribe siempre una revisión `reformular` sobre ella. La revisión la pasa a origen «paa» (D-097), aunque su pregunta no cambie.

### Paso 8 · Pistas de valoración y marca de dimensión de comparación

Las preguntas muestran también **qué mirar al valorar** un requisito y **si se compara**. Recógelo en `hints` y en `marks` (D-125 a D-128, D-139). En la entrada, cada requisito trae las pistas que ya le llegan y su marca vigente, si la tiene.

**Pistas de valoración** (`hints`). Una pista es lo que un requisito fija para orientar la valoración de sus criterios de aceptación (D-125). Escribe las pistas del **requisito**, desde sus preguntas (D-127). Escríbelas sobre todo para dos AC:

- **Precisión:** la pregunta muestra que un término o un valor no fija la respuesta por sí solo. Ejemplos: qué significa un término, un recuento sin unidad, una talla sin medidas. La pista dice **qué lo fija**.
- **Comparabilidad:** las preguntas comparan ofertas por ese aspecto. La pista dice **sobre qué base** se comparan (misma unidad, misma superficie, % en peso).

Aplicabilidad y Fiabilidad van sobre todo por tipo de requisito, y las compila el entrenamiento. Escríbelas solo si la pregunta muestra algo propio de este requisito (D-138). Concreción ya está en los componentes de la información resolutiva.

Cómo es una pista (D-128):

- **Un criterio, no una lista.** El auditor la aplica razonando. No escribas vocabularios admitidos ni frases exactas. Escribe «la composición usa el nombre legal de cada fibra», no «términos válidos: algodón, lino…». Los ejemplos ilustran; nunca cierran.
- **Breve pero clara:** una o dos frases (hasta 280 caracteres) con el criterio **y su porqué**.
- **Nombra la propiedad** que hay que observar (`propiedad`, de P06 a P18; P15 está retirada) **y los AC** a los que afecta (`ac`). Una pista puede servir a varios AC. Nunca puntúes la propiedad.

| Propiedad | Qué observa |
|---|---|
| P06 Completitud | Están los componentes necesarios para resolver la cuestión. |
| P07 Granularidad | Nivel de detalle y diferenciación. |
| P08 Explicitud | El hecho se dice, no hay que inferirlo. |
| P09 Claridad | Términos y valores sin ambigüedad. |
| P10 Estructuración semántica | Componentes delimitados y relacionados. |
| P11 Identificabilidad | Se distinguen productos, variantes y ofertas. |
| P12 Contextualización | Condiciones y referencias para interpretar el dato. |
| P13 Normalización | Unidades, valores y referencias que permiten equivalencias. |
| P14 Exactitud | Lo representado corresponde a los hechos comprobables. |
| P16 Coherencia | Afirmaciones consistentes sobre lo mismo. |
| P17 Trazabilidad | Se sigue la procedencia. |
| P18 Verificabilidad | Se puede contrastar con evidencias. |

- **No repitas.** Si una pista vigente del requisito ya dice lo mismo, no la escribas.
- Si tu pista contradice una vigente, escríbela con `duda` y el porqué (D-136).
- Si tu pista comparte propiedad y AC con una vigente pero dice otra cosa, explícalo en `note`.
- **Pista frente a aportación.** La aportación de precisión del paso 3 añade un componente a la información resolutiva: lo que la oferta ha de declarar. La pista dice al auditor cómo juzgar lo publicado. La misma pregunta puede dar las dos.
- Si una pregunta muestra que un término comercial no basta, escribe siempre la aportación de precisión. La pista no la sustituye. Ejemplo hipotético: «microfibra» o «memory foam» sin la fibra o el material que nombran.
- **Destino:** un requisito del catálogo o un candidato (`target`). No pongas `id`: el sistema asigna el número `PV-n` al guardarla. El código pone el origen «paa» y sus fuentes.

**Marca de dimensión de comparación** (`marks`; D-126, D-139). Comparabilidad es NA en los requisitos que no se comparan. Criterio:

> Un requisito **se compara** si su respuesta cambia de una oferta a otra y el comprador elige por ese valor: prefiere más, menos o uno mejor. **No se compara** si: (a) es igual en todas las ofertas, porque lo fija la ley o es universal (garantía legal); (b) solo sirve para que la oferta encaje con una **necesidad o un gusto** que ya se tiene: es un filtro (tamaño de cama, compatibilidad, idioma, color); (c) identifica la oferta o dice en qué estado está (identificadores, vendedor, disponibilidad).

- **Pon una marca a cada candidato.** No hay valor por defecto.
- **Pon una marca a un requisito del catálogo** solo si las preguntas son prueba:
  - las comparativas o de elección sobre el aspecto apoyan **sí** («¿qué tiene más…?», «¿X o Y?», «¿cuál es mejor para el calor?»);
  - las que eligen por una necesidad que ya se tiene apoyan **no (b)** («¿qué medida para una cama de 150?»).
- **Una pregunta genérica no es prueba** (paso 4).
- Si dudas, marca «sí», para no quitar un criterio sin motivo.
- Escribe en cada marca un motivo corto según el criterio. Si la marca es «no», escribe su caso (a, b o c).
- **Si tu marca contradice la vigente,** escríbela igual. El código la señala como duda (D-139).
- En un requisito que no se compara, no escribas pistas solo de Comparabilidad.

## 3. Lo que no se hace

- No leas las respuestas de Google ni busques fuera: solo tienes las preguntas (D-094).
- No completes hechos comerciales con conocimiento externo (invariante 9).
- No juzgues el producto ni su conveniencia (invariante 13). Un candidato pregunta por la oferta, no por lo que conviene a quien compra.
- No leas `docs/`, `var/runs/` ni clasificaciones anteriores de PAA.

## 4. Salida

```json
{
  "questions": [
    {"n": 1, "perimeter": "dentro|fuera", "object": "clase|marca|tienda|valorativa|null",
     "specialization": "esp.…|S1|null",
     "answered_by": ["cat.…/NN"], "criterion": "id|null", "candidate": "N1|null", "fails": "C2|C3|C4|null",
     "note": "opcional: por qué, si no es evidente"}
  ],
  "specializations": [
    {"id": "S1", "name": "de …", "order": "uso|material|función|juego", "trigger": "qué la dispara en una oferta"}
  ],
  "criteria": [
    {"id": "…", "name": "…", "verdict": "genera|cubierto|no-genera", "intermediate": false,
     "conditions": {"C1": {"ok": true, "why": "…"}, "C2": {…}, "C3": {…}, "C4": {…}},
     "covered_by": [], "candidates": ["N1"]}
  ],
  "candidates": [
    {"id": "N1", "question": "¿…?", "description": "…", "blocks": ["cat.…|esp.…|S1"], "mirrors": "cat.…/NN|null", "trait": "…",
     "vote": "crítico|principal|complementario", "applicability": "universal o condición", "from": "criterio|pregunta",
     "conditions": {"C1": {…}, "C2": {…}, "C3": {…}, "C4": {…}},
     "rationale": "…", "resolving_info": [{"contribution": "…", "component": "…"}]}
  ],
  "revisions": [
    {"id": "R1", "target": "cat.…/NN", "action": "separar|sacar|partir-por-tema|reformular|mover",
     "proposal": "…", "questions": [3, 7], "into": ["N1"],
     "tests": {"a": {"ok": true, "why": "…"}, "b": {"ok": true, "why": "…"}}}
  ],
  "contributions": [
    {"target": "cat.…/NN", "contribution": "…", "component": "…", "kind": "precisión|sustento", "questions": [5]}
  ],
  "hints": [
    {"target": "cat.…/NN|N1", "pista": "…", "propiedad": ["P13"], "ac": ["Comparabilidad"], "questions": [9, 12],
     "duda": "opcional: qué pista vigente contradice y por qué", "note": "opcional"}
  ],
  "marks": [
    {"target": "cat.…/NN|N1", "mark": "sí|no", "case": "a|b|c (solo si no)", "reason": "…", "questions": [9, 12]}
  ],
  "proposed_traits": [{"name": "…", "definition": "…"}],
  "doubts": ["…"]
}
```

**Preguntas**
- Escribe una entrada por pregunta, con su `n`.
- `fuera`: `object`, `specialization`, `criterion`, `candidate` y `fails` a `null`, y `answered_by` vacío.
- `valorativa`: lleva `criterion`. No lleva `candidate`, que sale de su criterio.
- `clase`: lleva **exactamente uno** de `answered_by` (no vacío), `candidate` o `fails`.
- `marca` y `tienda`: sin `candidate` (D-099, punto 1).
- `specialization`: solo si la pregunta trata de una especialización (paso 1). Si no, `null`.

**Especializaciones**
- Solo las que el catálogo no tiene, con id S1, S2…
- Cada una lleva `name`, `order` y `trigger`, y al menos una pregunta la lleva en `specialization`.

**Criterios**
- `genera`: las cuatro condiciones se cumplen y hay al menos un candidato.
- `cubierto`: C1 no se cumple, con `covered_by`. Un criterio intermedio lleva `"intermediate": true`.
- `no-genera`: C1 se cumple y alguna de C2–C4 no.

**Revisiones**
- `separar` lleva `tests` con (a) y (b) cumplidas y al menos un candidato en `into`.
- `sacar` puede ir sin `questions`. Las demás acciones las llevan.
- Las demás acciones no llevan `tests`.

**Pistas y marcas**
- Una pista lleva `target`, `pista`, `propiedad`, `ac` y `questions`, sin `id` ni `origen`.
- Pon una marca por destino. Todo candidato lleva la suya. Una marca de un requisito del catálogo lleva `questions`.
- `no` lleva `case`; `sí`, no.
