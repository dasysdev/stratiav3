# Modelo de demanda por bloques de requisitos, capa general, importancia y cuestiones inferidas

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-010). Procede del experimento base del clasificador (tarea T-009, `demand-engine/runs/2026-10-25-baseline/report.md`). Lo aceptó el usuario («ok», «si. aplica los ajustes»), salvo lo marcado como aplicación de Claude.*

## A. Identidad del modelo de demanda

Palabras del usuario: «mi intención es que el modelo de demanda de un producto se "denomine" por su composición de requisitos. Es decir, composición de clase <> composición de requisitos. El modelo de demanda representa una composición concreta de requisitos. Entonces la denominación del modelo viene de cómo identificamos esa composición».

Lecturas aceptadas:

1. La unidad de composición son **bloques de requisitos**, no preguntas sueltas ni la clase. Tipos de bloque:
   - bloque general universal;
   - bloques generales condicionados (variantes, descuento, unidad no nueva…);
   - bloques de sector (atributos heredados de Shopify);
   - bloques de categoría;
   - bloques de especialización (juego, polar, piel…).

   Un bloque agrupa las cuestiones que trae un mismo hecho. La importancia por defecto va en el bloque, y el modelo puede revisarla con justificación.
2. Palabras del usuario: «en la denominación lo debemos identificar. Quizás la identidad del modelo se compone de {clase de modelo de requisitos} - {aplicación concreta}. Esto reduce la cantidad de modelos».
   - Identidad = **modelo de requisitos** + **aplicación concreta**.
   - El modelo de requisitos es el conjunto de bloques, incluidos los condicionados con su disparador. Es lo que se reutiliza.
   - La aplicación concreta indica qué bloques condicionados se activan o dejan de aplicarse en una oferta.
   - Ambos se identifican en la denominación. Ejemplo: «Sofás · tapicería de piel — unidad no nueva, con descuento».
3. Las categorías por clasificación objetiva que no aportan requisitos quedan como **alias**. Palabras del usuario: «Alias. El objetivo de esto es puramente de etiquetado, denominación».
4. La composición de la clase (categorías, base, especializaciones) es el medio para descubrir los bloques.
   - La especialización es la característica que forma un bloque: trae cuestiones que no se aplican a los demás productos de la clase.
   - Una característica declarada que revela una dimensión que tienen todos los productos de la clase no forma bloque. Ejemplos: el peinado y el mercerizado del algodón, o el bordado como decoración. Su cuestión va al bloque de la clase, para todos, y el valor declarado es la respuesta. Así, una página que informa menos no tiene menos requisitos.
   - Resuelve la parte de OQ-37 sobre si las composiciones se registran: se registran los modelos como composiciones de bloques.

## B. Capa general

Hay requisitos que se aplican a cualquier producto, críticos, principales o complementarios; por ejemplo, saber qué precio tiene.

- La capa general tiene **cuestiones universales**, que se aplican siempre, y **cuestiones condicionadas**, con un disparador declarado: si hay variantes, si hay descuento, si la unidad no es nueva, si la cantidad es limitada…
- El disparador es el hecho declarado, no la etiqueta: una liquidación puede ser de producto nuevo.
- Las importancias son valores por defecto, revisables por clase con justificación (recomendación aceptada).

Borrador inicial, aceptado «para empezar, lo iremos perfeccionando»:

| Entidad | Cuestión | Importancia |
|---|---|---|
| Producto | ¿Qué es el producto y qué incluye exactamente? | Crítico |
| Producto | ¿Qué marca y modelo es? | Principal |
| Producto | ¿Qué identificadores tiene (EAN/GTIN, referencia)? | Principal |
| Variante | ¿Qué variantes hay y en qué se diferencian? (si las hay) | Crítico |
| Oferta | ¿Cuál es el precio final, con impuestos, de cada variante? | Crítico |
| Oferta | ¿Está disponible, en qué variantes y en qué cantidad, si es limitada? | Crítico |
| Oferta | ¿En qué estado se vende la unidad que se entrega, por qué motivo (exposición, devolución, tara, fin de serie…) y con qué marcas o defectos, si los tiene? | Principal. Las marcas, los defectos, el motivo y qué unidad se entrega solo se aplican si la unidad no es nueva |
| Oferta | ¿Hay descuento? ¿Desde qué precio de referencia y en qué condiciones? (si lo hay) | Complementario |
| Entrega | ¿Cuánto cuesta el envío a España y de qué depende? | Principal (duda: ¿crítico, porque forma el precio total?) |
| Entrega | ¿En qué plazo se entrega? | Principal |
| Entrega | Modalidades de entrega o recogida | Complementario |
| Condiciones | ¿Se puede devolver, en qué plazo y con qué coste? | Principal |
| Condiciones | ¿Qué garantía tiene? | Principal |
| Vendedor | ¿Quién vende la oferta? | Principal |

- **Dudas de alcance anotadas:** medios de pago y opiniones de clientes, porque el alcance excluye la transacción.
- **Fuentes de apoyo posibles,** que no definen el requisito: el grupo de oferta de los PTD de Amazon, las propiedades de oferta de Schema.org y la información precontractual de la venta a distancia en España (pendiente de comprobar).
- **Pila:** capa general → sector (D-029) → clase → especializaciones.

## C. Pruebas de importancia

Aceptadas «para empezar, lo iremos perfeccionando», como lectura operativa de las definiciones del canon, sin escala nueva:

- **Crítico:** si esta cuestión no se resuelve, ¿la oferta deja de ser evaluable? Por ejemplo, porque no se sabe qué se vende, cuánto cuesta o si se puede adquirir.
- **Principal:** ¿es uno de los criterios con los que se comparan y eligen ofertas de la clase?
- **Complementario:** es relevante, pero no indispensable ni central para comparar.

Precisiones:

- El canon pregunta si la oferta es evaluable, no si se puede comprar.
- Ejemplo del usuario: el mecanismo de un sofá cama es principal o complementario, porque «no impide comprar, no está al mismo nivel que precio, saber qué producto es».
- Consecuencia: los críticos son pocos y casi todos generales.
- La confianza en un requisito es independiente de su importancia: un requisito dudoso no se baja de nivel por dudoso.

## D. Cuestiones inferidas fuera de las referencias

Hay cuestiones de toda la clase que ninguna referencia recoge. Ejemplo: el mecanismo de apertura de un sofá cama, que no tienen ni Shopify Sofás cama ni el PTD SOFA.

El usuario eligió la opción b (el clasificador las propone) y planteó: «quizás no debemos esperar a validarlos por el MPIR sino darlos por válidos, confiar en el agente que los infiere».

Lectura de Claude que siguió a esa propuesta y que el usuario no objetó:

- Entran en el modelo como provisionales, en el régimen de D-022: se usan en la auditoría, el usuario valida siempre las críticas y una muestra del resto, y el MPIR las confirma o revisa cuando exista.
- Controles:
  - solo cuestiones de toda la clase, neutrales, justificadas y que no dupliquen la base;
  - origen marcado («referencias» o «inferida»);
  - la auditoría puede informar con ellas y sin ellas;
  - la estabilidad se mide con dos ejecuciones por caso.
- Añade una tercera vía de construcción, junto a la taxonomía y el MPIR.

## E. Valores de oferta y activación

Confirmado por el usuario: la condición de la unidad es un requisito general. Por tanto, outlet, liquidación, exposición o reacondicionado son valores de la oferta que condicionan cuestiones generales, no especializaciones, en cualquier producto.

Extensión simétrica de D-026: un valor que **activa** cuestiones condicionadas ya previstas en la base también es un valor que condiciona. Solo es especialización si trae cuestiones que la base no prevé. Ejemplos hipotéticos: la salud de la batería en un móvil reacondicionado; en bienes duraderos de fin de serie, los repuestos y accesorios.

Consecuencias:

- Cae el ejemplo de D-027 «lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta». Se mantiene que la condición 1 incluye la oferta.
- OQ-42 se cierra: en los dos casos, el valor condiciona cuestiones generales.

## F. Revisión de los casos esperados con las reglas vigentes

Aceptada («2. ok»); la aplicación es de Claude.

- **Stressless:**
  - El reclinable pasa a valor que condiciona: el mecanismo está en Shopify (reclining-mechanism), y las posiciones y la distancia a la pared, en el PTD SOFA.
  - La piel sigue siendo especialización: SOFA no tiene tipo de piel.
  - El outlet pasa a valor; en la aplicación, unidad no nueva.
  - Clase de estudio: Sofás → tapicería de piel.
- **Polar (sábanas y manta), punto, seco y cuerda** siguen siendo especialización: sus cuestiones no están en la base y no se aplican a otros productos de la clase.
- **Sofá cama Luna:** el experimento detectó que «apertura italiana» solo aparece en el nombre de un icono; el texto dice «sistema de apertura fácil». Se corrige: el mecanismo no está declarado. La cuestión «¿qué mecanismo de apertura tiene?» pasa al bloque de la clase como cuestión inferida provisional (principal).
- **Funda nórdica bordada:**
  - El peinado y el mercerizado son respuestas a una cuestión inferida del bloque de la clase sobre la preparación y el acabado del algodón (complementaria).
  - El bordado es un valor de la decoración.

## G. Estructura

Aceptada («OK a tu propuesta»):

- Separar la «Clase de estudio» de demand-model en un módulo canónico propio, `10-model/study-class.md`.
- Dejar en demand-model el modelo de demanda, la importancia y la nueva composición por bloques y capa general.
- Poner el catálogo inicial de la capa general y las pruebas de importancia en un módulo de método, con estado propuesta.
