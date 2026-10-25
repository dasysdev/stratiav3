# Clasificación objetiva, base de la clase en las referencias y material reciclado

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad. Procede de la evaluación del método con cinco casos más de burritoblanco.com (tarea T-008): manta super suave tejido Nacarina diseño 046 color Secuoya (https://www.burritoblanco.com/manta-super-suave-tejido-nacarina-diseno-046-color-secuoya-p-6008-93553.html), plaid de punto color Arena diseño 101 (https://www.burritoblanco.com/plaid-de-punto-color-arena-diseno-101-p-5454-90771.html), zapatillas de baño color Blanco 50 (https://www.burritoblanco.com/zapatillas-de-bano-color-blanco-50-p-573-1841.html), protector de colchón Basic 010 (https://www.burritoblanco.com/protector-de-colchon-basic-010-p-699-28.html) y cojines decorativos con relleno 018 Azul (https://www.burritoblanco.com/cojines-decorativos-con-relleno-018-azul-p-5777-92767.html).*

*Los bloques A a D son decisiones del usuario. El bloque A es una puntualización suya, con las lecturas de Claude aceptadas («ok»). En los bloques B a D, el usuario eligió las opciones que Claude recomendó. El bloque E es la aplicación a los casos, elaborada por Claude e ilustrativa.*

## A. Clasificación objetiva

Enmienda D-023. Palabras del usuario: «Por ordenamiento y coherencia, si hubiera una candidata que el producto entraría por clasificación objetiva, aunque no aporte nada, la añadimos. El caso es el de manta decorativa para plaid».

Regla: una categoría candidata en la que el producto entra por clasificación objetiva forma parte de la composición aunque no aporte requisitos propios. Sustituye «Una categoría que no aporta requisitos propios no entra»: aportar requisitos al producto o a alguna de sus piezas sigue siendo vía de entrada, pero no la única.

Lecturas aceptadas por el usuario («ok»):

- En el plaid entra Mantas decorativas (hg-15-1-4-2) y no Mantas para sillones y sofás (hg-3-77), que es una entrada duplicada en Decoración para el mismo tipo de producto.
- En la manta Nacarina, la clasificación objetiva es Mantas (hg-15-1-4) y no Mantas decorativas, porque el uso en sofá depende de la variante (medida).

Consecuencia aceptada: el sofá cama Luna, que es objetivamente un sofá de dos plazas, pasa a Sofás cama + Sofás de dos plazas (fr-22-4). Corrige el caso documentado, donde Sofás de dos plazas no entraba por tener los mismos 9 atributos.

## B. Base de una categoría de Shopify

Precisa D-023, D-024 y D-026. Decisión del usuario: la base de una categoría de Shopify son sus atributos propios más los de sus categorías madre (una categoría hija es un tipo de su madre).

Motivo: en Shopify v2026-08, 1749 de 14580 categorías hijas tienen solo una parte de los atributos de su madre (Mantas decorativas tiene 3 y Mantas, 9; Sofás cama, 9 y Sofás, 17). Con la lectura literal, hg-3-77 aportaría al plaid tejido, color, cuidados y patrón, y entraría como segunda categoría de un producto de una sola pieza.

## C. Características especiales de un PTD

Precisa D-024 y D-026. Decisión del usuario: los valores de la propiedad «Características especiales» (special_feature) de un PTD de Amazon cuentan como dimensiones de la base de la clase (regla de las cuestiones propias) y como apoyo (condición 4).

Motivo: son listas propias de cada tipo de producto (BLANKET, SLIPPER y PILLOW tienen listas distintas). Riesgo reconocido: el resultado depende de qué valores incluyó Amazon en cada lista (la de BLANKET no tiene «Resistente a la formación de bolitas»; la de SLIPPER sí).

## D. Material reciclado

Precisa D-025. Decisión del usuario: «material reciclado» es especialización, no beneficio reclamado: es composición verificable y trae cuestiones propias (qué proporción y en qué parte). «Sostenible» sí es beneficio reclamado (D-025).

## E. Aplicación a los casos (ilustrativa; no son clases aprobadas)

1. **Manta Nacarina 046.** Manta de cama o de sofá, tejido Nacarina® («pelito extraído de la fibra», tacto aterciopelado), 100 % poliéster, «para las noches más frías del invierno», 3 medidas (140×200 «mantita de sofá», 170×240 y 230×240).
   - Clase general: Mantas (Shopify hg-15-1-4 = Google 1985; Amazon «Mantas y colchas > Mantas para cama» 3250001031, PTD BLANKET).
   - Especialización: tejido polar, con Nacarina® como valor. Electricidad estática y pelusa ya están en la base de BLANKET (special_feature «Antiestático» y «Sin pelusa»; bloque C). Trae las bolitas, que no están en la base.
   - Invierno es valor: temporada y abrigo están en la base (Shopify season y warmth-rating; BLANKET seasons y thermal_performance_description), al contrario que en las sábanas, donde el abrigo no está en la base.
   - Poliéster, color secuoya y medidas: valores o variantes.
   - Clase de estudio: Mantas → tejido polar.
2. **Plaid de punto 101.** Plaid de punto con trenzas, 100 % acrílico, 130×170, para el sofá o decorativo.
   - Clase general: Mantas decorativas (hg-15-1-4-2 → Google 1985, más amplia; Amazon no tiene nodo de plaid; PTD BLANKET), por clasificación objetiva (bloque A) y con la base de Mantas (bloque B).
   - Especialización: tejido de punto. Trae enganchones, deformación y bolitas. Apoyo: BLANKET weave_type «Tejido de Punto Ancho» (más estrecha); Shopify no tiene dimensión de punto en mantas.
   - El acrílico es valor: las bolitas ya las trae el punto y el acrílico solo cambia la respuesta esperada.
   - Trenzas: valor estético.
   - Clase de estudio: Mantas decorativas → tejido de punto.
3. **Zapatillas de baño 50.** Rizo de algodón 100 %, 450 g/m², tallas 40 y 46, «1 juego» por talla.
   - Clase general: Pantuflas (aa-8-7 → Google 187, más amplia; Amazon «Zapatos > Zapatillas de estar por casa», PTD SLIPPER).
   - Uso de baño: ninguna referencia tiene dimensión de uso (falla la condición 4). El agarre sobre suelo mojado queda como requisito condicionado (D-024).
   - El rizo es valor: absorción («Absorbe la humedad») y gramaje (apparel_fabric_weight_class) están en la base de SLIPPER (bloque C).
   - «1 juego» es un par, la unidad normal de la clase: no es la especialización «juego».
   - Clase de estudio: Pantuflas, sin especializaciones.
4. **Protector de colchón Basic 010.** Protector acolchado, algodón 100 %, cama de 200.
   - Clase general: Cubrecolchones (hg-15-1-6-2, Mattress Pads = Google 2991; Amazon «Almohadillas de colchón» 27003778031 y «Protectores de colchón» 2822732031, PTD MATTRESS_COVER).
   - El acolchado ya es la categoría (D-021), no especialización.
   - Algodón: valor.
   - Impermeabilidad y relleno no declarados: corresponden a la auditoría.
   - Clase de estudio: Cubrecolchones, sin especializaciones.
5. **Cojín decorativo con relleno 018.** Funda con una cara texturada y otra en efecto jacquard, 87 % algodón reciclado y 13 % poliéster reciclado según la descripción, 50×50, incluye funda y relleno, «producto sostenible».
   - Clase general: Cojines (hg-3-64 = Google 4454; Amazon «Cojines y accesorios > Cojines» 2844244031, PTD PILLOW).
   - Funda y relleno son partes que la categoría ya modela (atributos cover-* y filler-*), no piezas de un juego. Ninguna categoría de fundas aporta requisitos propios ni es su clasificación objetiva.
   - Especialización: material reciclado (bloque D); apoyo en PILLOW special_feature «Reciclada» (bloque C).
   - «Sostenible»: beneficio (D-025).
   - Jacquard y colores: valores.
   - Clase de estudio: Cojines → material reciclado.

## Observaciones (no son reglas)

- En dos casos (zapatillas y protector) no sale ninguna especialización.
- La misma característica cambia según la base: invierno es especialización en sábanas y valor en mantas.
- En Shopify en español hay nombres que coinciden: «Cubrecolchones» son hg-15-1-6-2 (Mattress Pads) y hg-15-1-12 (Mattress Toppers), y «Zapatillas» (aa-8-8) es calzado deportivo. Por eso se trabaja con identificadores.
- La página del cojín se contradice en la composición (87/13 en la descripción; 54 % algodón y 13 % poliéster en la ficha). Es un hallazgo para la auditoría.
