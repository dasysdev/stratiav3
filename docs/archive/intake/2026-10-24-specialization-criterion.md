# Criterio de especialización y eje de base de la clase de estudio

*Update descrito por el usuario en la conversación del 2026-10-24 y transcrito para su trazabilidad. Procede del caso de trabajo T-005: juego de sábanas Coralina de burritoblanco.com (https://www.burritoblanco.com/juego-de-sabanas-coralina-color-marfil-diseno-trenzado-999-p-6153-95005.html). El usuario aceptó expresamente los tres bloques.*

## A. Regla «Shopify fija el eje de base»

Concreta el paso 1 de D-020 y la vía taxonómica de D-009. La clase general de una clase de estudio es una categoría de la Shopify Standard Product Taxonomy, en la versión fijada. Lo que Shopify no distingue como categoría entra como especialización. En el caso, Shopify no tiene «juego de sábanas»: la clase general es Sábanas (hg-15-1-2) y «juego» es una especialización.

## B. Respuesta a OQ-38

Criterio y evidencia para reconocer que una especialización «introduce o modifica cuestiones informativas relevantes». Una característica es especialización de la clase de estudio cuando cumple las cinco condiciones:

1. **Es del producto y estable:** un uso, material o función declarados. No es una variante, ni un valor estético, ni una etiqueta promocional.
2. **Tiene un efecto comparativo.** Frente a la clase general sin esa característica, produce al menos uno de estos efectos, expresado como cuestión concreta y neutral respecto de la respuesta: añade una cuestión; cambia el alcance o la desagregación de una cuestión; cambia la aplicabilidad (incluido que una cuestión deje de aplicarse); cambia la importancia relativa.
3. **Las cuestiones afectadas son relevantes** para evaluar la clase, no para un comprador concreto.
4. **Tiene apoyo en las referencias:** al menos la dimensión existe en Shopify, Amazon o Google, y el valor queda anclado con una relación tipada (equivalente, más amplia…).
5. **Nivel:** la especialización se fija en el nivel más general cuyos miembros comparten las cuestiones que introduce. Solo se baja de nivel si el inferior añade o modifica cuestiones. El valor concreto del producto se registra como valor de esa dimensión. El anclaje se hace en ese nivel; si la referencia no lo tiene, se ancla con una relación tipada.

**No cuentan:** un nodo o valor que solo existe en una referencia; un cambio de los valores esperados; una característica de variante; la proximidad temática; un requisito de plataforma o de feed.

**Evidencia** (opción B elegida por el usuario): con las cinco condiciones razonadas en la ficha, la especialización queda provisional. La valida el usuario, como responsable. El contraste con ecommerce referentes (MPIR) la confirma o la revisa después, cuando exista. No se fija ningún umbral numérico.

Relación: complementa la prueba de especialización de `subclasses.md` y aporta a OQ-06. OQ-37 (representación de la clase compuesta) sigue abierta.

## C. Caso ilustrativo (no es una clase aprobada)

Producto: juego de sábanas Coralina, marfil, diseño trenzado, 100 % poliéster, declarado «de invierno», con 7 medidas.

- **Clase general:** Sábanas, Shopify hg-15-1-2 (Bed Sheets). Equivale a Google 2314 según el mapeo oficial de Shopify a Google 2021-09-21. Amazon.es 3250022031 «Sábanas y fundas de almohada» es más amplia. Se descarta Shopify hg-15-1-11 «Juegos de cama» (Bedding Sets): Google la mapea a la genérica 569 y sus atributos (Nivel de calidez «del edredón o la colcha») corresponden a juegos de edredón.
- **Especialización «juego»** (función o composición): Shopify, atributo bedding-pieces-included en Sábanas; Amazon, nodo 3250028031 «Juegos de sábanas y fundas de almohada» con PTD BED_LINEN_SET (included_components, number_of_pieces). Añade cuestiones sobre las piezas incluidas y cambia el alcance (medidas de cada pieza).
- **Especialización «uso invernal»** (uso): la página la declara; Amazon PTD BED_LINEN_SET, propiedad seasons = Invierno; Shopify warmth-level «Cálido (invierno)», pero solo asignado a Juegos de cama. Añade cuestiones de abrigo y temporada.
- **Especialización «tejido polar»** (material): Shopify fabric__fleece (etiqueta «Vellón») en el atributo «Tejido» de Sábanas, y atributo fleece-finish-surface, cuya definición vincula el acabado con la formación de bolitas. Amazon usa «Forro polar» como material en unos 120 tipos PTD. «Coralina» no existe en ninguna referencia y es el valor declarado del tejido. Aplicando la condición 5: «tejido de pelo» es demasiado amplio (la franela y el terciopelo no comparten las cuestiones) y «coralina» no añade cuestiones frente a otros polares (cambian los valores). Añade cuestiones sobre bolitas, electricidad estática, transpirabilidad, abrigo y gramaje, y pérdida de pelo; y deja de aplicar el número de hilos.
- **Descartadas:** diseño trenzado y color marfil (valores estéticos), medida de 90 cm (variante), infantil (no declarado).
- **Clase de estudio:** Sábanas → juego + uso invernal + tejido polar (con coralina como valor del tejido).

Nota sobre el ejemplo del intake define-class («juegos de sábanas + uso invernal + tejido de coralina»): es ilustrativo y se conserva literal. Al aplicarle la condición 5, el tejido queda en polar y coralina como valor.

Observaciones del caso útiles para el método: las especializaciones salieron de atributos (temporada, tejido, piezas), no de nodos de los árboles; Shopify asigna atributos de forma incompleta (warmth-level no está en Sábanas); el anclaje más preciso de «juego» vino de Amazon; Google solo confirmó Sábanas.
