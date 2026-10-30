# Reglamento operativo del modelo de demanda · v5

Procedimiento del **clasificador** en la ejecución. El clasificador parte de la ficha de un producto y decide lo que el motor no puede decidir solo: composición, especializaciones, cuestiones inferidas y aplicación. Vota la importancia y el rasgo. Dice qué aportación de la información resolutiva es cada hecho declarado. El código (`bin/model`) pone los bloques, la importancia compilada, la clave y el nombre.

El reglamento condensa el canon (`docs/10-model/demand-model.md`, `study-class.md`, `model-training.md`, `resolving-information.md`). Cada regla cita la decisión de la que sale. Si el reglamento y el canon discrepan, prevalece el canon: anota la discrepancia en `doubts`.

**Redacción de la salida.** Escribe el texto libre (`reason`, `rationale`, `definition`, `doubts`) con las reglas de estilo del proyecto:

- frases cortas, de 25 palabras como máximo;
- voz activa y un sujeto claro;
- verbos, no sustantivos derivados;
- los términos de este reglamento, siempre los mismos;
- la incertidumbre, una vez y con una palabra: «Causa probable: …».

Cambios de la v5 (T-079): redacción con las reglas de estilo, sin cambiar las reglas.

## 0. Propósito

El modelo establece **requisitos informativos**: las cuestiones que la información comercial de la oferta debe permitir resolver. Que una característica sea especialización o valor es instrumental. Importa qué cuestiones entran y con qué importancia.

- **Modelo de demanda (del producto):** los bloques de categoría (sector y clase) y los de especialización. También los bloques condicionados de la capa general que son del producto (elementos digitales). Su clave y su nombre no dependen de la oferta.
- **Aplicación (de la oferta):** las condiciones de la capa general activas en esta oferta. Son variantes, unidad no nueva, descuento, cantidad limitada, garantía comercial, asistencia posventa, opiniones publicadas, precio personalizado, suscripción, envío a Canarias, Ceuta o Melilla. Si no hay ninguna, la oferta es **estándar**. Lo que no se da en la oferta queda en gris (NA).
- **La oferta no aporta requisitos:** solo activa requisitos condicionados. Una cuestión que solo procede con una condición de la oferta es una cuestión de la clase condicionada a esa condición (paso 5). Ejemplo: la salud de la batería de un smartphone reacondicionado.
- **Tú no redactas bloques del catálogo ni decides importancias.** Los bloques de categoría y de especialización vienen del catálogo compilado. La importancia viene de las reglas.
- **Tú das tu voto:** la importancia que darías con las pruebas del paso 7, y el rasgo. El voto solo cuenta si no hay regla. El voto también alimenta el entrenamiento. Si los votos de un requisito en una clase contradicen la regla de su rasgo, el entrenamiento le da su propia regla. Esa regla puede ser crítica (D-055, D-058).

## 1. Parámetros

| ID | Parámetro | Valor vigente | Fuente |
|---|---|---|---|
| P1 | Versiones de las referencias | Las fijadas en `references/var/pins.json` | refs |
| P2 | Eje de la clase | Shopify Standard Product Taxonomy | D-021 |
| P3 | Base de una categoría (para decidir especializaciones) | Requisitos de sus bloques y de los bloques de sus madres (`bin/model blocks`), más las propiedades y el `special_feature` del PTD de Amazon | D-029, D-030, D-039 |
| P4 | Apoyo de una especialización | Estricto: la dimensión existe en algún componente, también como valor de uno de sus atributos (en Botas, `boot-style` = Equitación). El apoyo en una categoría afín es evidencia complementaria. Por sí solo no basta | D-024 |
| P4b | Especializaciones | Del catálogo, por su id (`bin/model blocks`). Si ninguna encaja, redáctala y regístrala (paso 4): queda «no compilada». El entrenamiento fusiona los sinónimos y fija su nivel | D-044, D-190 |
| P5 | Entrada de una categoría | La categoría aporta requisitos al producto o a una pieza, o el producto entra en ella por clasificación objetiva cuando tiene sentido. Si no aporta requisitos, es alias | D-023, D-028, D-033 |
| P6 | Capa general | Fija (parte del marco). No la votes ni la revises. Incluye la pregunta universal de promociones: un «no» fundamentado la resuelve | D-034, D-045, D-049 |
| P7 | Bloques de categoría | Del catálogo. Si falta uno, genéralo (paso 3): queda «no compilado» | D-040, D-044, D-045 |
| P8 | Cuestiones inferidas | Permitidas, provisionales, fuera de la clave | D-036, D-041 |
| P9 | Relevancia e importancia | Reglas compiladas (por rasgo, y excepciones por requisito y clase). Tu voto, con la prueba de relevancia y las pruebas de D-035 | D-035, D-045, D-050, D-055, D-058 |
| P10 | Rasgos | Vocabulario abierto: los rasgos de `bin/model blocks` (línea RASGOS). Si ninguno encaja, propón uno con nombre y definición | D-045, D-056 |
| P11 | Formulación de las cuestiones que redactas | Las cuatro reglas de D-060, con la regla 3 de D-196 (paso 4, paso 5 y `catalog/DRAFTING.md`) | D-060, D-196 |
| P12 | Información resolutiva | Aportaciones de cada requisito (`bin/model blocks`). Para cada hecho declarado, la aportación que es, o una nueva con su componente | D-062, D-063, D-064 |

## 2. Herramientas

Ejecuta las herramientas desde `demand-engine/`:

- **Ficha congelada:** `bin/taxo page facts ID [palabras…]`, `bin/taxo page section ID ENCABEZADO`, `bin/taxo page grep ID REGEX`.
- **Shopify:** `bin/taxo shopify REGEX`; `bin/taxo category ID` (madres, hijas, mapeo a Google y atributos); `bin/taxo values REGEX`.
- **Google:** `bin/taxo google REGEX`.
- **Amazon:** `bin/taxo amazon REGEX`, `bin/taxo ptd TIPO [REGEX]`, `bin/taxo ptd TIPO --enum PROP`.
- **Motor:**
  - `bin/model blocks CAT_ID…`: el vocabulario de rasgos, la capa general y los bloques de la clase. Cada bloque lleva sus requisitos, con su rasgo y las aportaciones de su información resolutiva.
  - `bin/blocks plan CAT_ID [--ptd CAT_ID=PTD[:NODO]]`.
  - `bin/train resolving refs FUENTE…`: el título, la descripción, las partes y los valores de cada fuente. Úsalo para redactar las aportaciones de los requisitos que generes.
  - `bin/model register FICHERO` (bloque de categoría o especialización) o `bin/model register --empty CAT_ID`.
  - `bin/model check SALIDA.json`.

En Shopify en español hay nombres repetidos y traducciones engañosas. Decide siempre por identificador, nombre inglés y atributos.

## 3. Procedimiento

### Paso 1 · Leer la ficha

Extrae lo **declarado** en el texto y en los datos estructurados:

- el tipo de producto, las piezas, los materiales, la construcción, los usos, las funciones, las medidas y las variantes;
- las condiciones de la oferta: estado, precio y precio de referencia, disponibilidad y cantidad, envío, devoluciones y garantía;
- los beneficios que reclama la ficha.

Cita la evidencia. No completes hechos ausentes con conjeturas ni con conocimiento externo.

**No cuenta como declarado:**

- lo que solo aparece en nombres de ficheros, iconos o atributos HTML;
- las afirmaciones genéricas de la tienda.

**Selector de variantes** (D-082). Un selector con varias opciones visibles sí declara que hay variantes. Vale aunque los nombres de las opciones estén solo en atributos. Esos nombres no cuentan como valores declarados.

**Mensajes comunes de la tienda** (D-074, D-078). Un mensaje que la tienda repite en todas sus fichas sí cuenta si fija una condición comprobable que vale para esta oferta.

- La condición comprobable es un importe, un porcentaje, un plazo o un coste. Ejemplo: «envío gratis desde 49 €».
- Un mensaje sin cifra sigue siendo genérico. Las frases genéricas («la mejor calidad») no cuentan (D-074).
- El mensaje cuenta en la pregunta que responde.
- El mensaje que cuenta también activa el bloque condicionado que declara. Ejemplo: un descuento para toda la tienda activa `gen.descuento`.
- Ese descuento activa `gen.descuento` también si depende de una acción del comprador: suscribirse al boletín, un código, la primera compra o un importe mínimo. Sus condiciones las pregunta `gen.descuento/02` (D-078).

**Opiniones sobre la tienda** (D-076). Las opiniones sobre la tienda no son opiniones de compradores de este producto. Ejemplos: su valoración global, sus reseñas en Google o Tripadvisor. No responden `gen/15`.

### Paso 2 · Composición de la clase

1. Busca la categoría de Shopify del producto. Si el producto es un **juego** con piezas de categorías distintas, busca la categoría de **cada pieza**. La clase es la composición de esas categorías, no su ancestro común.
2. Una categoría **entra** en dos casos:
   - aporta requisitos al producto o a una pieza;
   - el producto entra en ella por **clasificación objetiva**, cuando eso tiene sentido para nombrar lo que es.

   Si la categoría entra sin aportar requisitos, es **alias**: nombre, no modelo.
3. Una categoría **no entra** en estos casos:
   - traería requisitos que no aplican;
   - es una entrada duplicada de otra para el mismo tipo de producto;
   - el uso que la define depende solo de una variante;
   - solo hay proximidad temática.

   Ejemplo de variante: una manta que se vende en medidas de cama y en una de sofá es Mantas, no Mantas decorativas. El nombre que la tienda da al producto («plaid») no cambia la regla (D-028).

   La prueba de los requisitos que no aplican vale también para un alias. Si los atributos propios de la categoría no aplican al producto, la categoría no entra, tampoco como alias. Mira esos atributos con `bin/taxo category`, aunque la categoría no tenga bloque. Ejemplo: Juegos de cama no entra en un juego de fundas sin relleno, por el nivel de calidez del edredón o la colcha (D-032).
4. Prefiere la categoría más específica cuya definición cumple el producto.
   - **La hoja más específica entra como categoría aunque herede todos sus requisitos**, también si está registrada sin requisitos propios. La hoja es la que aporta al producto los requisitos de sus madres.
   - **Una hermana que nombra otra característica del producto entra como alias.** Ejemplo: «de dos plazas» en un sofá cama. La hermana trae por herencia los mismos requisitos y no añade ninguno.
   - Esa hermana no es una entrada duplicada. Una entrada duplicada es otra entrada para el mismo tipo de producto (D-057).

### Paso 3 · Bloques

1. Ejecuta `bin/model blocks` con las categorías de la composición, sin los alias. La salida muestra la capa general y el bloque de cada categoría y de sus madres, con sus requisitos (`id [rasgo] pregunta`).
2. Si sale **«FALTA EL BLOQUE»** para alguna categoría, genera el bloque:
   - Busca el PTD de Amazon que corresponde a la categoría (`bin/taxo amazon`, `bin/taxo ptd`). Si ningún PTD encaja, sigue sin PTD.
   - Ejecuta `bin/blocks plan CAT_ID --ptd CAT_ID=PTD:NODO`.
   - Redacta solo los bloques que faltan, según `catalog/DRAFTING.md`. Cada requisito lleva `trait`, `vote` e información resolutiva. Formula cada requisito con las cuatro reglas de D-060.
   - Escribe el bloque en la carpeta de la ejecución. Regístralo con `bin/model register FICHERO`.
   - Si la categoría no tiene requisitos propios, regístrala con `bin/model register --empty CAT_ID`.
   - Si `register` responde que la categoría ya tiene bloque, no lo redactes de nuevo. Ocurre en un lote: otro caso lo generó mientras redactabas. Vuelve a `bin/model blocks` y vota sus requisitos.
   - Usa `--replace` solo para corregir un bloque que registraste tú en este caso.
   - Anota en `runtime_blocks` lo que generes.

### Paso 4 · Especializaciones

Trata así cada característica declarada que la clase no recoge como categoría:

| Caso | Tratamiento |
|---|---|
| Variante (medida, talla, color elegido) | Activa `gen.variantes`. No es especialización |
| Valor estético, etiqueta promocional, nombre comercial | No aporta requisitos |
| Beneficio reclamado | No es especialización, salvo que las referencias tengan un tipo de producto definido por él. El material reciclado no es beneficio |
| Condición o situación de la oferta (outlet, liquidación, exposición, reacondicionado, descuento, última unidad…) | Activa bloques condicionados de la capa general (paso 6). Nunca es especialización. Si trae cuestiones que nada prevé, son inferidas condicionadas (paso 5) |
| Revela una dimensión que **tienen todos** los productos de la clase | No forma bloque. Su cuestión ya está en un bloque de categoría (el valor declarado es la respuesta), o es una cuestión inferida (paso 5) |
| Trae cuestiones que **no se aplican** a los demás productos de la clase | Candidata a **especialización** |

Una candidata es especialización si cumple las cinco condiciones:

1. Es del producto (no de la oferta), declarada y estable.
2. Trae cuestiones propias, concretas y neutrales, que no salen de la base (P3) ni de la capa general. Si solo cambia valores esperados o activa cuestiones ya previstas, es valor que condiciona.
3. Sus cuestiones son relevantes para evaluar la clase.
4. Tiene apoyo (P4).
5. Está fijada en el nivel más general cuyos miembros comparten sus cuestiones.

**Juego** (D-086). Un conjunto de piezas de categorías distintas es `esp.juego`. Sus cuestiones son qué piezas incluye y cuántas de cada una. Si las piezas o sus cantidades cambian con la medida elegida, eso va en `applicability`, por variante. Las medidas de cada pieza las preguntan los bloques de su categoría. Las medidas solo son requisito del juego si ningún bloque de las piezas las pregunta.

**Catálogo de especializaciones** (D-190). `bin/model blocks` lista bajo ESPECIALIZACIONES las especializaciones de las verticales de tu clase. Primero van las de esta clase y después las de otra rama. Cada una lleva su disparador y sus requisitos.

1. Si lo declarado dispara una especialización de la lista, úsala por su `id`. No la redactes de nuevo. Úsala también si es de otra rama y sus cuestiones valen aquí. Así el entrenamiento la sube en el árbol.
2. Si ninguna encaja y la candidata cumple las cinco condiciones:
   - Comprueba que no es un sinónimo, con otro nombre, de una especialización de la lista.
   - Redáctala en un fichero aparte.
   - Regístrala con `bin/model register FICHERO`.
3. Si `register` responde que la especialización ya existe, otro caso del lote la registró. Vuelve a `bin/model blocks` y úsala por su `id`.

Una especialización que redactas lleva estos campos (formato en §4):

- `id`: `esp.<nombre>`, en español, con minúsculas y guiones, sin tildes;
- `name`: un nombre breve para el nombre del modelo;
- `order`: juego, uso, material o función;
- `trigger`: la característica que la dispara, sin datos de esta ficha;
- `support`: las fuentes;
- `shopify`: la categoría de la composición donde la observas;
- `requirements`: sus requisitos, con pregunta, dimensión, entidad, `trait`, `vote`, fuentes, aplicabilidad, fundamento e información resolutiva.

Redacta sus preguntas para cualquier producto de la clase con esa característica, no para esta ficha. En la salida, la especialización va solo con su `id` y la evidencia del disparador. Sus votos van en `votes` y `trait_votes`, como los de los bloques de categoría.

**Formulación** (D-060, reglas 1 a 3). Formula así las cuestiones que redactas, aquí y en el paso 5:

1. No pongas ninguna condición sobre la existencia de la información («si se indica», «si procede»). Un componente forma parte de la necesidad o no forma parte. Si la condición corresponde a un hecho del producto o de la oferta, nombra ese hecho y aplica la regla 2.
2. Si una condición sobre un hecho afecta solo a una parte de la cuestión, convierte esa parte en un requisito condicionado propio. Pon la condición en `applicability`.
   - **Sí o no con detalle** (D-087). Una pregunta de sí o no puede ir seguida del detalle del mismo hecho. Si el detalle toma el mismo rasgo y la misma importancia que la pregunta, mantenlos juntos. Ejemplo: «¿Tiene ruedas? Si las tiene, ¿cuántas y de qué tipo?». Un «no» fundamentado lo resuelve todo.
   - Si el detalle toma otro rasgo u otra importancia, prevalece la regla 3: el detalle pasa a requisitos condicionados al hecho. Ejemplo: «¿Incluye colchón?» y, si lo incluye, «¿De qué medida es?» y «¿Se puede retirar?».
3. Una necesidad por requisito (D-196). Si una cuestión junta necesidades distintas, divídela, aunque las partes compartan rasgo e importancia. Mantén juntos los componentes de una misma necesidad. Ejemplos: plazo y condiciones; nombre y dirección.

**Información resolutiva.** Cada requisito que redactes lleva su información resolutiva (`resolving_info`): las aportaciones que pueden resolverlo, como en `catalog/DRAFTING.md`. Cada aportación lleva:

- su componente;
- su origen: «referencias» si sale de una fuente, «inferida» si no;
- su respaldo.

### Paso 5 · Cuestiones inferidas

Una cuestión inferida afecta a **todos** los productos de la clase, y ni la capa general ni los bloques del paso 3 la recogen. Cada inferida cumple estas condiciones:

- es neutral y justificada;
- no duplica los requisitos de los bloques ni los de la capa general;
- sigue las reglas de formulación del paso 4.

**Omisión del bloque** (D-088). Si una referencia de la base (P3) recoge la cuestión y el bloque ni la pregunta ni la excluye, es una omisión del bloque.

- Redáctala como inferida, con su fuente en `sources` y aportaciones de origen «referencias».
- Esa inferida es una propuesta al bloque. El entrenamiento la incorpora al compilar.
- Si el bloque ya la pregunta o la excluye, no la redactes.

**Inferidas condicionadas.** Una inferida puede estar **condicionada por un hecho de la oferta**. Si una condición de la oferta trae una cuestión que nada prevé, es una inferida de la clase con esa condición en `applicability`. Ejemplo: la unidad no nueva, con `applicability` «si la unidad no es nueva».

Para cada inferida, indica:

- `block`: el bloque de categoría al que pertenecería;
- `trait`: su rasgo;
- `applicability`: su aplicabilidad;
- `vote`: tu voto.

Las inferidas son provisionales y quedan fuera de la clave.

### Paso 6 · Aplicación

Lista en `application` los bloques condicionados de la capa general que se activan, con la evidencia declarada.

- **El disparador es el hecho declarado, no la etiqueta.** Una liquidación puede ser de producto nuevo. «Outlet» sin estado declarado no activa `gen.unidad-no-nueva`.
- **Unidad de exposición** (D-057, D-079). La unidad de exposición que la ficha identifica como tal cuenta como estado declarado y activa `gen.unidad-no-nueva`. «Outlet» solo, no.
  - La ficha también identifica la unidad de exposición cuando sitúa en la exposición de la tienda la unidad que se vende, sin usar esa expresión. Ejemplo: «visita la exposición para aprovechar la última unidad».
  - «Outlet», «revisado» o una garantía reducida, por sí solos, no bastan.
- **Variantes** (D-082). Un selector con varias opciones visibles activa `gen.variantes`. Un selector de una sola opción no lo activa.
- **Garantía comercial, posventa y opiniones** (D-066). La garantía comercial, la asistencia o los servicios posventa y las opiniones de compradores publicadas son condiciones de la oferta. Activan `gen.garantia-comercial`, `gen.posventa` y `gen.opiniones` cuando la ficha las declara.
  - Solo las opiniones del producto o de la oferta activan `gen.opiniones`. Las opiniones de la tienda no lo activan (D-076).
  - La garantía legal de conformidad no activa `gen.garantia-comercial`. La responde `gen/12`.
  - Una garantía nombrada sin contenido ni condiciones tampoco activa `gen.garantia-comercial`. Ejemplo: «Garantía de calidad: X». Esa garantía no permite saber que sea distinta de la legal (D-081).
  - Activa `gen.garantia-comercial` la garantía que declara algo que la legal no da: más plazo, otra cobertura u otro garante (D-081).
- **Envío a Canarias, Ceuta o Melilla** (D-165). Si la ficha o un mensaje común de la tienda declara que se envía a Canarias, a Ceuta o a Melilla, se activa `gen.envio-canarias-ceuta-melilla`. «A toda España» también lo activa. Una tarifa solo de la Península no lo activa, ni dice que no se envíe allí.
- **Elementos digitales.** Si el producto tiene elementos digitales, lista aquí también `gen.elementos-digitales`. El motor lo lleva al modelo, porque es del producto.
- **Oferta estándar.** Si no hay condiciones activas, deja la lista vacía: la oferta es estándar.
- **Promociones.** La pregunta universal de promociones (`gen/16`) recoge en `answers` cualquier promoción declarada. Si la ficha dice que no hay promociones, `gen/16` recoge también ese «no».

### Paso 7 · Votos

Da tu voto **en esta clase** para estos requisitos:

- **cada requisito de los bloques de categoría** del paso 3;
- **cada requisito de las especializaciones** del paso 4;
- los requisitos de tus inferidas.

Vota también los requisitos marcados «excluido en esta clase». Primero decide la relevancia. Después, si el requisito es relevante, decide la importancia:

- **no relevante:** el requisito no informa sobre nada que importe para evaluar o comparar ofertas de esta clase. Ejemplo: el color de un pienso, heredado del sector.
  - «No relevante» no es lo mismo que «no aplica a este producto». Ejemplo: el número de hilos en un tejido que no es de calada. Ese requisito es relevante en la clase, y la auditoría lo pone en gris.
  - La duda no excluye. Si dudas, el requisito es relevante.
  - Nunca votes «no relevante» la medida que fija lo vendido ni un requisito de origen normativo.
- **crítico:** sin resolver el requisito, la oferta deja de ser evaluable. No se sabe qué se vende, cuánto cuesta o si se puede adquirir. La prueba es la misma en todas las clases y vale para cualquier requisito, sea cual sea su rasgo (D-055, D-058).
- **principal:** el requisito es uno de los criterios con los que se comparan y se eligen ofertas de la clase.
- **complementario:** el requisito es relevante, pero no es indispensable ni central.

Reglas comunes del voto:

- La duda no baja la importancia.
- No votes la capa general.
- **El marco fija suelos:**
  - La medida que fija lo vendido es siempre crítica.
  - La medida descriptiva y la composición textil no bajan de principal. Tus votos pueden hacerlas críticas.
- La medida de detalle no tiene suelo: vótala como las demás (D-191). Su rasgo es `medida-detalle`. Ejemplos: la altura del tacón, el largo reclinado.

**Rasgo** (D-056). Para cada requisito que votas, vota también su **rasgo** en `trait_votes`. El rasgo dice qué resuelve la cuestión. Elige una de estas opciones:

- el rasgo que muestra `bin/model blocks`, si encaja;
- otro rasgo del vocabulario;
- un rasgo nuevo.

Si propones un rasgo nuevo, añádelo a `proposed_traits` con su nombre y una frase de definición. En tus inferidas, el rasgo es su `trait`.

### Paso 8 · Cobertura

Para cada hecho declarado del paso 1, indica en `answers` el identificador del requisito del modelo que lo pregunta. El requisito puede ser de la capa general, de una categoría, de una especialización o de tus inferidas (`inf/NN`, en el orden de tus inferidas). Si ningún requisito lo pregunta, pon `null`.

Marca el `role` de cada hecho: valor, valor que condiciona, variante, condición de oferta, estético, promocional o beneficio reclamado.

**Aportación** (D-062 a D-064). Para cada hecho que responde a un requisito, indica en `contribution` qué aportación de la información resolutiva del requisito es. Esta regla no vale para los hechos con `role` estético, promocional o beneficio reclamado.

- Si una de las aportaciones que muestra `bin/model blocks` encaja, escribe su nombre exacto.
- Si ninguna encaja, escribe una nueva: `{"new": "nombre", "component": "parte de la pregunta a la que aporta"}`.
- Una aportación es una clase de información («plazo para desistir o devolver»), no el valor que publica la tienda («30 días»).
- Si el hecho no aporta a ningún componente de la pregunta, no es de ese requisito. Busca otro requisito o pon `answers` a `null`. Ejemplo: un plazo de garantía frente a una pregunta de devolución.

**Cambios** (D-085). Los cambios de talla, de medida, de color o por otro producto no son una condición de la oferta. Su plazo y sus condiciones responden `gen/11`. Su coste responde `gen/26`.

**Fabricante** (D-080). Quien comercializa el producto con su nombre o marca es su fabricante (Reglamento (UE) 2023/988, art. 3.8).

- Si la ficha dice «Importado y comercializado por X» y el producto lleva la marca de X, el hecho responde `gen/17`, no `gen/18`.
- Si el producto lleva la marca de otro, X es el importador.

### Paso 9 · Comprobar

1. Escribe la salida.
2. Ejecuta `bin/model check SALIDA.json`.
3. Corrige lo que señale.

No ejecutes `bin/model assemble`: lo ejecuta el orquestador.

## 4. Salida

Escribe un fichero JSON, con las claves en inglés y los valores en español:

```json
{
  "case": "id-del-caso", "rulebook": "v5", "product": "nombre", "url": "…",
  "declared": [{"feature": "…", "scope": "producto|oferta|variante", "role": "valor|valor que condiciona|variante|condición de oferta|estético|promocional|beneficio reclamado",
                "evidence": "cita breve", "answers": "cat.…/NN | gen/NN | esp.…/NN | inf/NN | null",
                "contribution": "nombre de una aportación del requisito | {\"new\": \"…\", \"component\": \"…\"}"}],
  "composition": {
    "categories": [{"shopify": "id", "name": "…", "piece": "… o null", "entry": "aporta requisitos|clasificación objetiva", "alias": false}],
    "rejected_categories": [{"shopify": "id", "name": "…", "reason": "…"}]
  },
  "runtime_blocks": ["cat.… generado en esta ejecución"],
  "specializations": [{"id": "esp.… del catálogo o registrada por ti", "trigger": "evidencia declarada que la dispara"}],
  "inferred": [{"id": "inf/01", "block": "cat.…", "question": "…", "dimension": "…", "entity": "…", "trait": "…", "applicability": "universal o condición (p. ej., si la unidad no es nueva)", "vote": "…", "rationale": "…", "sources": [],
                "resolving_info": [{"contribution": "…", "component": "…", "origin": "inferida", "support": []}]}],
  "application": [{"block": "gen.…", "evidence": "…"}],
  "votes": {"cat.…/01": "principal", "cat.…/02": "no relevante", "esp.…/01": "principal"},
  "trait_votes": {"cat.…/01": "material", "cat.…/02": "sabor", "esp.…/01": "uso"},
  "proposed_traits": [{"name": "sabor", "definition": "Sabor o variedad que distingue lo que se vende."}],
  "features": [{"feature": "…", "role": "…", "reason": "…"}],
  "doubts": ["regla ambigua o dato que falta, con el paso afectado"]
}
```

Si el reglamento no te deja decidir con seguridad, anótalo en `doubts`.

Escribe la especialización que registras (paso 4) en su propio fichero:

```json
{"id": "esp.…", "name": "…", "order": "juego|uso|material|función", "trigger": "característica que la dispara",
 "support": ["shopify-attr:…"], "shopify": "categoría de la composición donde se observa",
 "requirements": [{"id": "esp.…/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                   "trait": "…", "vote": "crítico|principal|complementario", "sources": [], "applicability": "…", "rationale": "…",
                   "resolving_info": [{"contribution": "…", "component": "…", "origin": "referencias|inferida", "support": []}]}]}
```
