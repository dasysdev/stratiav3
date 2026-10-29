# Reglamento operativo del modelo de demanda · v3

Procedimiento del **clasificador** en la ejecución: a partir de la ficha de un producto, decide lo que el motor no puede decidir solo (composición, especializaciones, cuestiones inferidas, aplicación), vota la importancia y el rasgo, y dice qué aportación de la información resolutiva es cada hecho declarado; los bloques, la importancia compilada, la clave y el nombre los pone el código (`bin/model`). Condensa el canon (`docs/10-model/demand-model.md`, `study-class.md`, `model-training.md`, `resolving-information.md`); cada regla cita la decisión de la que sale. Si el reglamento y el canon discrepan, prevalece el canon y la discrepancia se anota en `doubts`.

## 0. Propósito

El modelo establece **requisitos informativos**: las cuestiones que la información comercial de la oferta debe permitir resolver. Que una característica sea especialización o valor es instrumental: importa qué cuestiones entran y con qué importancia.

- **Modelo de demanda (del producto):** bloques de categoría (sector y clase) y de especialización, más los condicionados de la capa general que son del producto (elementos digitales). Su clave y su nombre no dependen de la oferta.
- **Aplicación (de la oferta):** condiciones de la capa general activas en esta oferta (variantes, unidad no nueva, descuento, cantidad limitada, garantía comercial, asistencia posventa, opiniones publicadas, precio personalizado, suscripción, envío a Canarias, Ceuta o Melilla). Si no hay ninguna, la oferta es **estándar**. Lo que no se da en la oferta queda en gris (NA).
- **La oferta no aporta requisitos:** solo activa requisitos condicionados. Una cuestión que solo procede con una condición de la oferta (p. ej., la salud de la batería de un smartphone reacondicionado) es una cuestión de la clase condicionada a esa condición (paso 5).
- **Tú no redactas bloques del catálogo ni decides importancias.** Los bloques de categoría vienen del catálogo compilado; la importancia, de las reglas. Tú das tu **voto** (la importancia que darías con las pruebas del paso 7, y el rasgo); el voto solo cuenta si no hay regla, y alimenta el entrenamiento: si los votos de un requisito en una clase contradicen la regla de su rasgo, el entrenamiento le da su propia regla, que puede ser crítica (D-055, D-058).

## 1. Parámetros

| ID | Parámetro | Valor vigente | Fuente |
|---|---|---|---|
| P1 | Versiones de las referencias | Las fijadas en `references/var/pins.json` | refs |
| P2 | Eje de la clase | Shopify Standard Product Taxonomy | D-021 |
| P3 | Base de una categoría (para decidir especializaciones) | Requisitos de sus bloques y de los de sus madres (`bin/model blocks`) + propiedades y `special_feature` del PTD de Amazon | D-029, D-030, D-039 |
| P4 | Apoyo de una especialización | Estricto: la dimensión existe en algún componente | D-024 |
| P5 | Entrada de una categoría | Aporta requisitos al producto o a una pieza, o clasificación objetiva cuando tiene sentido (alias si no aporta) | D-023, D-028, D-033 |
| P6 | Capa general | Fija (parte del marco); no se vota ni se revisa. Incluye la pregunta universal de promociones (un «no» fundamentado la resuelve) | D-034, D-045, D-049 |
| P7 | Bloques de categoría | Del catálogo; si falta uno, se genera (paso 3) y queda «no compilado» | D-040, D-044, D-045 |
| P8 | Cuestiones inferidas | Permitidas, provisionales, fuera de la clave | D-036, D-041 |
| P9 | Relevancia e importancia | Reglas compiladas (por rasgo y excepciones por requisito y clase); tu voto con la prueba de relevancia y las de D-035 | D-035, D-045, D-050, D-055, D-058 |
| P10 | Rasgos | Vocabulario abierto: los de `bin/model blocks` (línea RASGOS); si ninguno encaja, propón uno con nombre y definición | D-045, D-056 |
| P11 | Formulación de las cuestiones que redactas | Las cuatro reglas de D-060, con la regla 3 de D-196 (paso 4, paso 5 y `catalog/DRAFTING.md`) | D-060, D-196 |
| P12 | Información resolutiva | Aportaciones de cada requisito (`bin/model blocks`); para cada hecho declarado, la que es o una nueva con su componente | D-062, D-063, D-064 |

## 2. Herramientas

Desde `demand-engine/`:

- Ficha congelada: `bin/taxo page facts ID [palabras…]`, `bin/taxo page section ID ENCABEZADO`, `bin/taxo page grep ID REGEX`.
- Shopify: `bin/taxo shopify REGEX`; `bin/taxo category ID` (madres, hijas, mapeo a Google y atributos); `bin/taxo values REGEX`. Google: `bin/taxo google REGEX`. Amazon: `bin/taxo amazon REGEX`, `bin/taxo ptd TIPO [REGEX]`, `bin/taxo ptd TIPO --enum PROP`.
- Motor: `bin/model blocks CAT_ID…` (vocabulario de rasgos, capa general y bloques de la clase con sus requisitos, rasgos y aportaciones de su información resolutiva); `bin/blocks plan CAT_ID [--ptd CAT_ID=PTD[:NODO]]`; `bin/train resolving refs FUENTE…` (título, descripción, partes y valores de cada fuente, para redactar las aportaciones de los requisitos que generes); `bin/model register FICHERO` o `bin/model register --empty CAT_ID`; `bin/model check SALIDA.json`.

En Shopify en español hay nombres repetidos y traducciones engañosas: decide siempre por identificador, nombre inglés y atributos.

## 3. Procedimiento

### Paso 1 · Leer la ficha

Extrae lo **declarado** en el texto y en los datos estructurados: tipo de producto, piezas, materiales, construcción, usos, funciones, medidas y variantes, condiciones de la oferta (estado, precio y precio de referencia, disponibilidad y cantidad, envío, devoluciones, garantía) y beneficios que reclama. Cita la evidencia. No cuenta como declarado lo que solo aparece en nombres de ficheros, iconos o atributos HTML, ni las afirmaciones genéricas de la tienda. Un selector con varias opciones visibles sí declara que hay variantes, aunque los nombres de las opciones estén solo en atributos: esos nombres no cuentan como valores declarados (D-082). Un mensaje que la tienda repite en todas sus fichas sí cuenta, en la pregunta que responde, si fija una condición comprobable que vale para esta oferta (un importe, un porcentaje, un plazo o un coste: «envío gratis desde 49 €»; un mensaje sin cifra sigue siendo genérico), y activa el bloque condicionado que declara (un descuento para toda la tienda activa `gen.descuento`, también si depende de una acción del comprador, como suscribirse al boletín, un código, la primera compra o un importe mínimo: sus condiciones las pregunta `gen.descuento/02`, D-078); las frases genéricas («la mejor calidad») no (D-074). Las opiniones sobre la tienda (su valoración global, sus reseñas en Google o Tripadvisor) no son opiniones de compradores de este producto: no responden `gen/15` (D-076). No completes hechos ausentes con conjeturas ni con conocimiento externo.

### Paso 2 · Composición de la clase

1. Busca la categoría de Shopify del producto. Si es un **juego** con piezas de categorías distintas, la de **cada pieza**: la clase es la composición de esas categorías, no su ancestro común.
2. Una categoría **entra** si aporta requisitos al producto o a una pieza, o si el producto entra en ella por **clasificación objetiva** cuando tiene sentido para nombrar lo que es; si entra sin aportar requisitos, es **alias** (nombre, no modelo).
3. **No entra** si traería requisitos que no aplican, si es una entrada duplicada de otra para el mismo tipo de producto, si el uso que la define depende solo de una variante o si solo hay proximidad temática.
4. Prefiere la categoría más específica cuya definición cumple el producto. **La hoja más específica entra como categoría aunque herede todos sus requisitos** (aunque esté registrada sin requisitos propios): es la que aporta al producto los de sus madres. **Una hermana que nombra otra característica del producto** (por ejemplo, «de dos plazas» en un sofá cama) **entra como alias**: trae por herencia los mismos requisitos y no añade ninguno. No es una entrada duplicada: duplicada es otra entrada para el mismo tipo de producto (D-057).

### Paso 3 · Bloques

1. Ejecuta `bin/model blocks` con las categorías de la composición (no los alias). Verás la capa general y, para cada categoría y sus madres, su bloque con los requisitos (`id [rasgo] pregunta`).
2. Si sale **«FALTA EL BLOQUE»** para alguna categoría, genéralo:
   - Busca el PTD de Amazon que corresponde a la categoría (`bin/taxo amazon`, `bin/taxo ptd`); si ninguno encaja, sin PTD.
   - `bin/blocks plan CAT_ID --ptd CAT_ID=PTD:NODO` y redacta solo los bloques que faltan siguiendo `catalog/DRAFTING.md` (cada requisito con `trait`, `vote` e información resolutiva, formulado con las cuatro reglas de D-060). Escríbelo en la carpeta de la ejecución y regístralo con `bin/model register FICHERO`. Si la categoría no tiene requisitos propios, `bin/model register --empty CAT_ID`.
   - Si `register` responde que la categoría ya tiene bloque (en un lote, otro caso lo generó mientras redactabas), no lo redactes de nuevo: vuelve a `bin/model blocks` y vota sus requisitos. `--replace` sirve solo para corregir un bloque que registraste tú en este caso.
   - Anota en `runtime_blocks` lo que generes.

### Paso 4 · Especializaciones

Cada característica declarada que la clase no recoge como categoría:

| Caso | Tratamiento |
|---|---|
| Variante (medida, talla, color elegido) | Activa `gen.variantes`; no es especialización |
| Valor estético, etiqueta promocional, nombre comercial | No aporta requisitos |
| Beneficio reclamado | No es especialización, salvo que las referencias tengan un tipo de producto definido por él. El material reciclado no es beneficio |
| Condición o situación de la oferta (outlet, liquidación, exposición, reacondicionado, descuento, última unidad…) | Activa bloques condicionados de la capa general (paso 6); nunca es especialización. Si trae cuestiones que nada prevé, son inferidas condicionadas (paso 5) |
| Revela una dimensión que **tienen todos** los productos de la clase | No forma bloque: su cuestión ya está en un bloque de categoría (el valor declarado es la respuesta) o es una cuestión inferida (paso 5) |
| Trae cuestiones que **no se aplican** a los demás productos de la clase | Candidata a **especialización** |

Una candidata es especialización si cumple las cinco condiciones: (1) del producto (no de la oferta), declarada y estable; (2) trae cuestiones propias, concretas y neutrales, que no salen de la base (P3) ni de la capa general (si solo cambia valores esperados o activa cuestiones ya previstas, es valor que condiciona); (3) relevantes para evaluar la clase; (4) con apoyo (P4); (5) fijada en el nivel más general cuyos miembros comparten sus cuestiones. Un conjunto de piezas de categorías distintas es `esp.juego`: qué piezas incluye y cuántas de cada una (si cambian con la medida elegida, va en `applicability`, por variante). Las medidas de cada pieza las preguntan los bloques de su categoría; solo son requisito del juego si ningún bloque de las piezas las pregunta (D-086).

Cada especialización: `id` (`esp.<nombre>`, español, minúsculas y guiones), `name` breve para el nombre del modelo, `order` (juego, uso, material o función), `trigger`, `support` (fuentes) y sus requisitos (pregunta, dimensión, entidad, `trait`, `vote`, fuentes, aplicabilidad, fundamento).

**Formulación** de las cuestiones que redactas, aquí y en el paso 5 (D-060, reglas 1 a 3):

1. Ninguna condición sobre la existencia de la información («si se indica», «si procede»): un componente forma parte de la necesidad o no. Si la condición corresponde a un hecho del producto o de la oferta, nombra ese hecho y aplica la regla 2.
2. Una condición sobre un hecho que afecta solo a una parte de la cuestión se convierte en un requisito condicionado propio, con la condición en `applicability`. La pregunta de sí o no seguida del detalle del mismo hecho se mantiene («¿Tiene ruedas? Si las tiene, ¿cuántas y de qué tipo?»): un «no» fundamentado lo resuelve todo. Solo si el detalle toma el mismo rasgo y la misma importancia que la pregunta; si no, la regla 3 prevalece y el detalle pasa a requisitos condicionados al hecho («¿Incluye colchón?» y, si lo incluye, «¿De qué medida es?» y «¿Se puede retirar?»; D-087).
3. Una necesidad por requisito: si una cuestión junta necesidades distintas, divídela, aunque las partes compartan rasgo e importancia (D-196). Mantén juntos los componentes de una misma necesidad (plazo y condiciones; nombre y dirección).

Cada requisito que redactes lleva su **información resolutiva** (`resolving_info`): las aportaciones que pueden resolverlo, cada una con su componente, su origen («referencias» si sale de una fuente, «inferida» si no) y su respaldo, como en `catalog/DRAFTING.md`.

### Paso 5 · Cuestiones inferidas

Cuestiones que afectan a **todos** los productos de la clase y que ni la capa general ni los bloques del paso 3 recogen: neutrales, justificadas, sin duplicar los requisitos de los bloques ni los de la capa general, formuladas con las reglas del paso 4. Si una referencia de la base (P3) recoge la cuestión y el bloque ni la pregunta ni la excluye, es una omisión del bloque: redáctala como inferida con su fuente en `sources` (y aportaciones de origen «referencias»); es una propuesta al bloque, que el entrenamiento incorpora al compilar. Si el bloque ya la pregunta o la excluye, no la redactes (D-088). Pueden estar **condicionadas por un hecho de la oferta**: si una condición de la oferta (unidad no nueva, por ejemplo) trae una cuestión que nada prevé, es una inferida de la clase con `applicability` «si la unidad no es nueva». Indica el bloque de categoría al que pertenecerían (`block`), su `trait`, su `applicability` y tu `vote`. Son provisionales y quedan fuera de la clave.

### Paso 6 · Aplicación

Bloques condicionados de la capa general que se activan, con la evidencia declarada. El disparador es el **hecho declarado**, no la etiqueta: una liquidación puede ser de producto nuevo, y «outlet» sin estado declarado no activa `gen.unidad-no-nueva`. **La unidad de exposición que la ficha identifica como tal cuenta como estado declarado** y activa `gen.unidad-no-nueva`; «outlet» solo, no (D-057). También la identifica cuando sitúa en la exposición de la tienda la unidad que se vende, sin usar esa expresión («visita la exposición para aprovechar la última unidad»); «outlet», «revisado» o una garantía reducida, por sí solos, no bastan (D-079). `gen.variantes` lo activa un selector con varias opciones visibles; uno de una sola opción, no (D-082). La garantía comercial, la asistencia o los servicios posventa y las opiniones de compradores publicadas son condiciones de la oferta: activan `gen.garantia-comercial`, `gen.posventa` y `gen.opiniones` cuando la ficha las declara (D-066), y `gen.opiniones` solo con opiniones del producto o de la oferta, no de la tienda (D-076); la garantía legal de conformidad no activa `gen.garantia-comercial`: la responde `gen/12`. Una garantía nombrada sin contenido ni condiciones («Garantía de calidad: X») tampoco la activa, porque no permite saber que sea distinta de la legal; la activa la que declara algo que la legal no da: más plazo, otra cobertura u otro garante (D-081). `gen.envio-canarias-ceuta-melilla` lo activa que la ficha o un mensaje común de la tienda declare que se envía a Canarias, a Ceuta o a Melilla, también con «a toda España»; una tarifa solo de la Península no lo activa ni dice que no se envíe (D-165). Lista aquí también `gen.elementos-digitales` si el producto los tiene: el motor lo lleva al modelo, porque es del producto. Sin condiciones activas, la lista va vacía (oferta estándar). La pregunta universal de promociones (`gen/16`) recoge en `answers` cualquier promoción declarada, o el «no» si la ficha lo dice.

### Paso 7 · Votos

Para **cada requisito de los bloques de categoría** del paso 3 (también los marcados «excluido en esta clase»), y para los de tus especializaciones e inferidas, da tu voto **en esta clase**. Primero la relevancia; después, si es relevante, la importancia:

- **no relevante** si no informa sobre nada que importe para evaluar o comparar ofertas de esta clase (p. ej., el color de un pienso, heredado del sector). No es lo mismo que «no aplica a este producto» (el número de hilos en un tejido que no es de calada): eso es relevante en la clase y la auditoría lo pone en gris. La duda no excluye: si dudas, es relevante. Nunca votes «no relevante» la medida que fija lo vendido ni un requisito de origen normativo;

- **crítico** si, sin resolverlo, la oferta deja de ser evaluable (no se sabe qué se vende, cuánto cuesta o si se puede adquirir). La prueba es la misma en todas las clases y vale para cualquier requisito, sea cual sea su rasgo (D-055, D-058);
- **principal** si es uno de los criterios con los que se comparan y eligen ofertas de la clase;
- **complementario** si es relevante sin ser indispensable ni central.

La duda no baja la importancia. No votes la capa general. El marco no baja: la medida que fija lo vendido es siempre crítica, y la medida descriptiva y la composición textil no bajan de principal (tus votos pueden hacerlas críticas).

**Rasgo.** Para cada requisito que votas, vota también su **rasgo** (qué resuelve la cuestión) en `trait_votes`: el que muestra `bin/model blocks` si encaja, otro del vocabulario o uno nuevo. Si propones uno nuevo, añádelo a `proposed_traits` con nombre y una frase de definición. En tus especializaciones e inferidas, el rasgo es su `trait` (D-056).

### Paso 8 · Cobertura

Para cada hecho declarado del paso 1, indica en `answers` el identificador del requisito del modelo que lo pregunta (capa general, categoría, especialización o `inf/NN` de tus inferidas, en su orden), o `null` si ninguno lo pregunta. Marca su `role`: valor, valor que condiciona, variante, condición de oferta, estético, promocional o beneficio reclamado.

**Aportación** (D-062 a D-064). Para cada hecho que responde a un requisito (salvo los estéticos, promocionales y beneficios reclamados), indica en `contribution` qué aportación de la información resolutiva del requisito es: el nombre exacto de una de las que muestra `bin/model blocks`, o, si ninguna encaja, una nueva como `{"new": "nombre", "component": "parte de la pregunta a la que aporta"}`. Una aportación es una clase de información («plazo para desistir o devolver»), no el valor que publica la tienda («30 días»). Si el hecho no aporta a ningún componente de la pregunta (un plazo de garantía frente a una pregunta de devolución), no es de ese requisito: busca otro o pon `answers` a `null`. Los cambios (de talla, medida, color u otro producto) no son una condición de la oferta: su plazo y sus condiciones responden `gen/11`, y su coste, `gen/26` (D-085).

**Fabricante** (D-080). Quien comercializa el producto con su nombre o marca es su fabricante (Reglamento (UE) 2023/988, art. 3.8): «Importado y comercializado por X», con el producto bajo la marca de X, responde `gen/17`, no `gen/18`. Si el producto lleva la marca de otro, X es el importador.

### Paso 9 · Comprobar

Escribe la salida y ejecuta `bin/model check SALIDA.json`; corrige lo que señale. No ejecutes `bin/model assemble`: lo hace el orquestador.

## 4. Salida

Un fichero JSON (claves en inglés; valores en español):

```json
{
  "case": "id-del-caso", "rulebook": "v3", "product": "nombre", "url": "…",
  "declared": [{"feature": "…", "scope": "producto|oferta|variante", "role": "valor|valor que condiciona|variante|condición de oferta|estético|promocional|beneficio reclamado",
                "evidence": "cita breve", "answers": "cat.…/NN | gen/NN | esp.…/NN | inf/NN | null",
                "contribution": "nombre de una aportación del requisito | {\"new\": \"…\", \"component\": \"…\"}"}],
  "composition": {
    "categories": [{"shopify": "id", "name": "…", "piece": "… o null", "entry": "aporta requisitos|clasificación objetiva", "alias": false}],
    "rejected_categories": [{"shopify": "id", "name": "…", "reason": "…"}]
  },
  "runtime_blocks": ["cat.… generado en esta ejecución"],
  "specializations": [{"id": "esp.…", "name": "…", "order": "juego|uso|material|función", "trigger": "característica declarada",
                       "support": ["shopify-attr:…"],
                       "requirements": [{"id": "esp.…/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                                         "trait": "…", "vote": "crítico|principal|complementario", "sources": [], "applicability": "…", "rationale": "…",
                                         "resolving_info": [{"contribution": "…", "component": "…", "origin": "referencias|inferida", "support": []}]}]}],
  "inferred": [{"id": "inf/01", "block": "cat.…", "question": "…", "dimension": "…", "entity": "…", "trait": "…", "applicability": "universal o condición (p. ej., si la unidad no es nueva)", "vote": "…", "rationale": "…", "sources": [],
                "resolving_info": [{"contribution": "…", "component": "…", "origin": "inferida", "support": []}]}],
  "application": [{"block": "gen.…", "evidence": "…"}],
  "votes": {"cat.…/01": "principal", "cat.…/02": "no relevante"},
  "trait_votes": {"cat.…/01": "material", "cat.…/02": "sabor"},
  "proposed_traits": [{"name": "sabor", "definition": "Sabor o variedad que distingue lo que se vende."}],
  "features": [{"feature": "…", "role": "…", "reason": "…"}],
  "doubts": ["regla ambigua o dato que falta, con el paso afectado"]
}
```

Anota en `doubts` cada vez que el reglamento no te deje decidir con seguridad.
