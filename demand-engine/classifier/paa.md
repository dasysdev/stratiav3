# Reglamento de clasificación de las preguntas PAA · v3

Procedimiento del **agente** que clasifica las preguntas de «Más preguntas» (PAA) de un conjunto de semillas: decide el perímetro y el objeto de cada pregunta, la contrasta con el catálogo de la clase, reconoce los **criterios de elección** y propone **requisitos candidatos**, **revisiones** de requisitos existentes y **aportaciones**. Condensa el canon (`docs/10-model/choice-criteria.md`, `construction-routes.md`, `demand-model.md`; `docs/20-methods/product-taxonomy/requirement-blocks.md`). Cada regla cita la decisión de la que sale. Si el reglamento y el canon discrepan, prevalece el canon y la discrepancia se anota en `doubts`.

Cambios de la v2 (D-100 a D-107): lectura sobre la oferta, confirmaciones y aportaciones, apoyo mínimo, separación por dimensión, criterios intermedios, tacto, certificaciones, bloques hermanos y revisiones. Cambios de la v3 (D-108 a D-110): preguntas distintas para la prueba (a), cualquier atributo de lista, lista ausente en la clase, preguntas de grado, efecto frío al tacto, necesidades distintas de una fibra y sacar sin preguntas.

## 0. Propósito

PAA es una vía de construcción del modelo de demanda (D-094). Sus preguntas son de compradores y sirven para:

- confirmar requisitos del catálogo y cuestiones inferidas;
- reconocer criterios de elección;
- proponer requisitos nuevos (D-099).

**No** aportan información resolutiva. Que una pregunta aparezca, o en qué posición, no prueba la importancia de nada (D-094).

Tú no cambias el catálogo ni decides importancias. Los candidatos, las revisiones y las aportaciones son propuestas para el entrenamiento. Los candidatos entran con origen «paa» (D-097).

## 1. Entrada y salida

- **Entrada:** `classify/input.md` del conjunto. Contiene:
  - las preguntas numeradas, con las semillas que las mostraron;
  - el catálogo de la clase: capa general, bloques de la clave con sus fuentes y cuestiones inferidas;
  - las hijas de cada bloque en la taxonomía;
  - el vocabulario de rasgos.
- **Salida:** `classify/output.json` (formato en §4). Compruébala con `bin/paa classify check CONJUNTO` hasta que diga «correcto».
- Las semillas solo dan contexto. Ejemplo hipotético: «¿Abriga mucho?» desde «mantas de lana» trata de la lana de las mantas.

## 2. Procedimiento

### Paso 1 · Perímetro

- **`dentro`:** la pregunta trata de los productos de la clase (sus categorías y especializaciones), o de una característica de sus materiales, tejidos o piezas tal como la vive quien compra en la clase.
- **`fuera`:**
  - trata de otro producto, de textiles en general sin relación con la clase, o de curiosidades (el producto más caro del mundo, historia);
  - **o es confección casera:** coser, hacer o arreglar la pieza. No hay compra (D-100).
- **Caso dudoso:** se decide con la **lectura sobre la oferta** del paso 5. Si un hecho que la oferta puede declarar la responde, va **dentro** (D-100). Ejemplo hipotético: «¿Qué contraindicaciones tiene el corcho?» en una clase de esterillas de corcho se relee como «¿qué advertencias declara esta esterilla?».

Pertinencia no es proximidad temática (invariante 10): que hable de dormir o de tejidos no la pone dentro.

### Paso 2 · Objeto (solo si está dentro)

| Objeto | Cuándo | Ejemplo |
|---|---|---|
| `marca` | Pregunta por marcas, también si es valorativa. La marca como criterio no genera requisito (C4). | «¿Cuál es la mejor marca de sábanas en España?» |
| `tienda` | Pregunta dónde comprar, por una tienda o por los precios de una tienda. | «¿Dónde puedo comprar sábanas de algodón 100 %?» |
| `valorativa` | Pide un juicio que depende del comprador: mejor o peor, recomendación, si algo «es bueno» o «merece la pena». | «¿Qué es mejor, percal o satén?» |
| `clase` | Pregunta factual sobre la clase: qué es, medidas, precio (sin nombrar tienda), cómo se usa o se cuida, qué propiedad tiene un material o un tejido. | «¿Se encoge el lino al lavarlo?», «¿Cuánto cuesta una sábana de lino?» |

### Paso 3 · Contraste con el catálogo

En `answered_by` pon los requisitos del catálogo (capa general, bloques o `inf/`) que **responden la pregunta sin derivar**: los que, una vez resueltos por una oferta, dan la respuesta para esa oferta.

- **No responde** el atributo del que se deduciría una prestación. Que la oferta declare «percal» o «100 % algodón» no dice si la sábana es fresca, si se arruga o si encoge (D-090).
- **Un requisito de certificaciones** responde una prestación **si su información resolutiva recoge la declaración** de esa prestación (por ejemplo, «declaración de hipoalergenicidad») (D-106). Si no la recoge, no la responde. **Salvedad** (D-109): si las preguntas muestran que esa prestación es una dimensión de comparación de la clase (las dos pruebas del paso 7), propón separarla de la lista de certificaciones.
- **Confirmaciones** (D-101):
  - Una pregunta de **tienda o marca que nombra un atributo** («¿Dónde comprar sábanas 100 % algodón?») confirma el requisito de ese atributo: quien compra busca y filtra por él.
  - El **precio sin tienda** confirma `gen/04`.
  - Una **verificación** («¿Cómo saber si es 100 % algodón?») confirma el requisito del atributo verificado.
  - Una pregunta por el **significado de un término** («¿Qué significa *queen*?», «¿Qué es el modal?») confirma el requisito del atributo al que pertenece el término.
- **Aportaciones** (D-101). Cuando una pregunta muestra que un término comercial no basta para resolver un requisito, propón una aportación de **precisión** para ese requisito en `contributions`. Ejemplos:
  - la denominación de la fibra según el Reglamento (UE) 1007/2011;
  - la unidad de un recuento;
  - la equivalencia en cm de una talla.

  Una verificación propone una aportación de **sustento**, como la certificación del contenido o del origen.
- Si responde una cuestión inferida (`inf/…`), la confirma (D-097).

### Paso 4 · Criterios de elección

A cada pregunta valorativa asígnale el **criterio de elección** que revela: el aspecto por el que quien compra juzga si una oferta le conviene (D-091).

- Un criterio por aspecto, con un id corto en minúsculas.
- Una pregunta de marca o de clase que trata del mismo aspecto puede llevar también ese criterio.
- Si un criterio mezcla aspectos que se juzgan por separado, divídelo.
- **Dos extremos del mismo eje son un solo criterio.** Por ejemplo hipotético: «¿qué edredón abriga más?» y «¿cuál es el más fresco?».
- **Criterio intermedio** (D-104). Es un criterio que no es una prestación: «calidad», «material», «tipo de tejido» cuando se pregunta cuál es mejor.
  - Queda `cubierto`. En `covered_by` van el requisito que dice qué es (la composición) y los requisitos o candidatos de las prestaciones en que se descompone.
  - Una **pregunta genérica** («¿es bueno el lino?», «beneficios del bambú») no nombra ninguna prestación. Apoya el criterio intermedio, pero no a una prestación concreta: no le pongas el criterio ni el candidato de una prestación.
  - Solo apoya una prestación la pregunta que la nombra.

Aplica a cada criterio la regla C1–C4 (D-091). Genera un requisito solo si cumple **todas**:

| # | Condición | Si no se cumple |
|---|---|---|
| C1 | Ningún requisito existente lo responde sin derivar. | `cubierto`, con los requisitos (o criterios, o candidatos) en `covered_by`. |
| C2 | Es un hecho que la oferta puede declarar: una prestación, un resultado de ensayo, una indicación de uso. | `no-genera`: solo lo juzga quien compra («que me guste»). |
| C3 | Se aplica a toda la clase o a una especialización, no a un comprador. | `no-genera`: es una condición de compra o un escenario. |
| C4 | Se puede formular neutral y sobre la oferta. | `no-genera`: solo admite «mejor o peor» (marca, reputación). |

- **Preguntas de grado** (D-110). Una pregunta de grado («tan suaves», «las más frescas», «cuál se arruga menos») indica el aspecto. **C2 se juzga sobre el requisito**, formulado por tipo o por declaración: si la oferta puede declarar el tipo, la pregunta de grado apoya ese requisito. Solo no genera cuando el aspecto únicamente admite más o menos y ninguna categoría declarable lo resuelve (la marca, C4).
- **Tacto** (D-105, D-110): se formula por el **tipo** de tacto (sedoso o liso, crujiente, afelpado, fresco al tacto), no por el grado de suavidad. Una pregunta por lo suave que es apoya ese requisito. El **efecto frío al tacto** (reclamos como «Enfriamiento» o «tacto fresco») es un tipo de tacto, no un nivel térmico: el nivel térmico es la temporada o el abrigo (D-108). Su rasgo es `sensorial`, decidido por el usuario: si aún no está en el vocabulario, declara su definición en `proposed_traits`.

### Paso 5 · Preguntas de clase

**Lectura sobre la oferta** (D-100). Antes de aplicar C2, relee la pregunta sobre la oferta: «¿… esta oferta?».

- «¿Qué es una sábana encimera?» → «¿qué es esta pieza?».
- Ejemplo hipotético: «¿Cómo se monta una lámpara de pie?» → «¿qué instrucciones de montaje trae esta?».

Si un hecho que la oferta puede declarar la responde, la pregunta confirma ese requisito o propone un candidato. C2 solo se aplica cuando **ningún** hecho de la oferta la responde: hábitos («¿cada cuánto se lavan?»), saber doméstico («¿cómo se dobla?»), cantidades que dependen de quien compra (C3).

Cada pregunta de objeto `clase` acaba de una de estas tres formas:

1. **Respondida:** `answered_by` con uno o más requisitos.
2. **Candidata:** ningún requisito la responde y cumple C2–C4 (D-099). Lleva el `candidate` que propone. Si pertenece a un criterio que genera, lleva el candidato de ese criterio.
3. **No genera:** en `fails`, la primera condición que no cumple (`C2`, `C3` o `C4`).

**Basta una pregunta** para que exista un candidato que cumple C1–C4 (D-102).

### Paso 6 · Requisitos candidatos

Cada criterio que genera y cada pregunta de clase candidata dan un requisito candidato. Varias preguntas que piden lo mismo dan **uno**.

- **Formulación:** las cuatro reglas de D-060 (`catalog/DRAFTING.md`, regla 8).
  - Cuestión neutral y sobre la oferta.
  - Una necesidad por requisito.
  - Sin condiciones sobre la existencia de la información.
  - Ejemplo: la variedad de una fibra (seda de morera, algodón de fibra larga) y su origen geográfico (país o región de cultivo) son dos necesidades y dan dos candidatos (D-108).
- **Lista ausente** (D-109). Si en un bloque de la clase falta un atributo de lista que tiene un bloque hermano (sus fuentes son de un tipo de producto de la referencia que la clase no tiene), el candidato para la clase es **la misma lista**: la misma pregunta, sin los valores que se separen, con su id en `mirrors`. Las preguntas sueltas sobre sus valores la apoyan; no propongas un candidato por valor. Si ningún hermano la tiene, agrupa los valores por tema (D-043, criterio 2).
- **Descripción** (`description`, D-092), en tres partes:
  1. qué se pregunta en concreto, con ejemplos de lo que abarca;
  2. qué tipo de información lo responde;
  3. qué no lo responde y con qué requisito vecino no se confunde.
- **Información resolutiva** (`resolving_info`): la declaración de la prestación, un ensayo o una certificación. **Nunca** el atributo del que se deduciría la prestación (D-090). Son aportaciones inferidas: PAA no aporta información resolutiva (D-097).
- **Bloques** (`blocks`; D-043, criterio 4; D-107). Mira las hijas de cada bloque en la entrada.
  - Va al bloque más alto de la clave cuyo requisito valga para **todas** sus hijas.
  - Si no vale para todas las hijas de la madre común (por ejemplo, una hija cuyo producto no tiene esa propiedad), **no sube**: va **repetido** en cada bloque hermano al que se aplica, con la **misma pregunta y la misma descripción**.
- **Rasgo** (`trait`): uno del vocabulario, o uno de `proposed_traits` con su definición.
- **Voto** (`vote`): con las pruebas de `catalog/DRAFTING.md` (regla 5). La importancia la deciden las reglas del entrenamiento: que los compradores pregunten no la prueba.
- **Origen:** «paa». Las fuentes las pone el código: las preguntas que apoyan el candidato.

### Paso 7 · Revisiones de requisitos existentes

Cuando las preguntas muestran que un requisito del catálogo debe cambiar, propón una **revisión** en `revisions`. Tipos (`action`):

| Acción | Cuándo |
|---|---|
| `separar` | **Separación por dimensión** (D-103, D-109), para **cualquier atributo de lista** de una referencia, de Amazon o de Shopify, también las listas de certificaciones: sus valores son reclamos que la oferta marca o no.<br>La lista se mantiene agrupada como la plantea la referencia. Un valor se separa en requisito propio solo si PAA lo muestra como **dimensión de comparación de la clase**, con **las dos pruebas** en `tests`:<br>(a) **transversal**: **preguntas distintas** sobre dos o más materiales o tejidos;<br>(b) **comparativa o de elección**: «¿qué X más?», «¿cuál X menos?».<br>**Una misma pregunta no cuenta para (a) y (b) a la vez.** Las preguntas genéricas no cuentan. El valor separado es un candidato (en `into`). |
| `sacar` | Un valor de la lista no pertenece a su tema (una confección en una lista de resistencias). Sale de ella aunque la referencia lo incluya (D-103). No necesita preguntas de apoyo (D-109). |
| `partir-por-tema` | El requisito mezcla temas o beneficiarios distintos (D-043, criterio 2). Por ejemplo hipotético: «protección de la piel o del colchón». |
| `reformular` | La pregunta del requisito se queda corta para lo que PAA muestra. Por ejemplo, una inferida que solo cubre un extremo de un eje. Una inferida que PAA confirma pasa a origen «paa» (D-097). |
| `mover` | Una aportación está en un requisito y pertenece a otro (a un candidato, por ejemplo). |

Cada revisión lleva:

- el requisito (`target`);
- la propuesta, en prosa;
- las preguntas que la apoyan (salvo `sacar`);
- los candidatos que crea, si los crea.

Una revisión de un requisito repetido en bloques hermanos se aplica igual en todos (D-107).

### Paso 8 · Pertinencia de los criterios de aceptación (propuesta, OQ-59)

Opcional. Si un grupo de preguntas muestra que un criterio de aceptación es pertinente para un requisito, anótalo en `ac_evidence` con esas preguntas. Por ejemplo:

- comparan materiales → Comparabilidad de la composición;
- preguntan qué significa un término → Precisión;
- preguntan cómo verificarlo → Fiabilidad.

Es una propuesta del canon, sin decidir (D-104): solo se recoge la evidencia.

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
     "answered_by": ["cat.…/NN"], "criterion": "id|null", "candidate": "N1|null", "fails": "C2|C3|C4|null",
     "note": "opcional: por qué, si no es evidente"}
  ],
  "criteria": [
    {"id": "…", "name": "…", "verdict": "genera|cubierto|no-genera", "intermediate": false,
     "conditions": {"C1": {"ok": true, "why": "…"}, "C2": {…}, "C3": {…}, "C4": {…}},
     "covered_by": [], "candidates": ["N1"]}
  ],
  "candidates": [
    {"id": "N1", "question": "¿…?", "description": "…", "blocks": ["cat.…"], "mirrors": "cat.…/NN|null", "trait": "…",
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
  "ac_evidence": [
    {"requirement": "cat.…/NN", "ac": "Comparabilidad", "questions": [9, 12], "why": "…"}
  ],
  "proposed_traits": [{"name": "…", "definition": "…"}],
  "doubts": ["…"]
}
```

**Preguntas**
- Una entrada por pregunta, con su `n`.
- `fuera`: `object`, `criterion`, `candidate` y `fails` a `null`, y `answered_by` vacío.
- `valorativa`: lleva `criterion`; no lleva `candidate`, que sale de su criterio.
- `clase`: lleva **exactamente uno** de `answered_by` (no vacío), `candidate` o `fails`.
- `marca` y `tienda`: sin `candidate` (D-099, punto 1).

**Criterios**
- `genera`: las cuatro condiciones se cumplen y hay al menos un candidato.
- `cubierto`: C1 no se cumple, con `covered_by`. Un criterio intermedio lleva `"intermediate": true`.
- `no-genera`: C1 se cumple y alguna de C2–C4 no.

**Revisiones**
- `separar` lleva `tests` con (a) y (b) cumplidas y al menos un candidato en `into`.
- `sacar` puede ir sin `questions`; las demás acciones las llevan.
- Las demás acciones no llevan `tests`.
