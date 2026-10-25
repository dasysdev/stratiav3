# Propósito de la clase de estudio: los requisitos informativos

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad. Procede de la tarea T-008. Hay dos orígenes: la revisión independiente del update `2026-10-25-objective-classification`, que abrió la incidencia I-14, y dos casos más de burritoblanco.com. Uno es el juego de fundas nórdicas bordadas algodón percal 200 hilos 401 Blanco (https://www.burritoblanco.com/fundas-nordicas-bordadas-algodon-percal-200-hilos401-blanco-p-5191-10308.html). El otro es el protector de colchón Basic 010, revisado con las reglas nuevas.*

*El bloque A son palabras del usuario. El bloque B son lecturas de Claude que el usuario aceptó («si»). El bloque C es la aplicación a los casos, elaborada por Claude e ilustrativa.*

## A. Propósito

Palabras del usuario: «Recuerda que el propósito es establecer requisitos informativos. Esto es lo más importante (+ el matiz de denominación que hemos especificado cuando tiene sentido aunque no aporte)».

El matiz de denominación es la clasificación objetiva (D-028): una categoría en la que el producto entra objetivamente se añade aunque no aporte requisitos.

## B. Lecturas aceptadas por el usuario

Lectura general: la pregunta que manda es qué requisitos informativos produce la clase. Que algo sea especialización o valor es instrumental. Lo único que entra sin aportar requisitos es lo que nombra la clase por clasificación objetiva, cuando tiene sentido.

1. **Sofá cama Luna.** Los requisitos no cambian: resistencia a la abrasión, desenfundable y antimanchas siguen siendo requisitos. Ahora salen de la base del PTD SOFA (special_feature «Resistente a la abrasión», «Resistente a las manchas» y «Funda extraíble»; D-030). Que la tela pase a valor es un cambio de etiqueta. El matiz de denominación no se aplica, porque no es una categoría de clasificación objetiva. La clase queda en Sofás cama + Sofás de dos plazas. Sofás de dos plazas sí está bien añadido: no aporta requisitos, pero nombra lo que el producto es.
2. **Resto de I-14.** No cambia ningún requisito:
   - El lavado de la cuerda y la resistencia a la mordida siguen siendo requisitos.
   - Las bolitas, la electricidad estática y la pérdida de pelo del polar también.
   - Las piezas del juego, cuántas son y en qué medidas, también.
   - Lo que queda es redacción de los casos y documentar el apoyo del polar en la manta.
   - Leer la base pieza a pieza o para todo el juego no altera el resultado: queda como nota.
   - Se aplican las propuestas de I-14. Cuerda: sigue siendo especialización por el deshilachado y la ingestión de fibras, y el lavado pasa a la base. Mordedor: comprobar si «Uso rudo» cubre la resistencia a la mordida. Sábanas: el polar sigue siendo especialización, porque la pérdida de pelo no está en ninguna base. Juego: su efecto se escribe con los requisitos del conjunto de D-023 (qué piezas, cuántas y en qué medidas). Manta: se documenta el apoyo del polar (Shopify Mantas fabric «Vellón»; BLANKET material «Forro polar» y weave_type «Tejido de pelo»).
3. **Juegos de cama (hg-15-1-11).** No entra en el juego de funda nórdica. No aporta requisitos y además traería uno que no aplica: el nivel de calidez «del edredón o la colcha» (warmth-level), en un juego de fundas sin relleno. Añadirlo empeoraría los requisitos, así que tampoco tiene sentido por denominación. Además, Amazon separa los juegos de edredón o colcha (PTD BEDDING_SET, con fill_material) de los juegos de fundas (BED_LINEN_SET).

## C. Aplicación a los casos (ilustrativa; no son clases aprobadas)

1. **Juego de fundas nórdicas bordadas 401.** Contiene funda nórdica, bajera ajustable y una funda de almohada (cama de 135) o dos (resto de medidas). Algodón percal de 200 hilos, peinado y mercerizado, con tiras bordadas en la funda nórdica y en las bocas de las fundas de almohada y pliegues decorativos. Tiene 5 medidas (de 135 a 200) y descuento del 30 %.
   - Clase general (composición por piezas): Fundas de nórdico (hg-15-1-5 = Google 2541) + Sábanas ajustables + Fundas de almohada.
   - Especialización «juego»: Amazon 3250005031 «Juegos de fundas para edredón», PTD BED_LINEN_SET (included_components, number_of_pieces). Aporta qué piezas incluye, cuántas y en qué medidas.
   - Juegos de cama (hg-15-1-11): no entra (bloque B.3).
   - Percal y 200 hilos: valores (Shopify fabric-weave; BED_LINEN_SET weave_type y thread).
   - Mercerizado: valor; la dimensión de acabado existe en BED_LINEN_SET (finish_type).
   - Peinado: valor. No hay dimensión en ropa de cama (solo en fibras de manualidades). Cambia la respuesta esperada, no añade cuestiones.
   - «Más resistente y suave» y «mayor brillo»: beneficios reclamados (D-025).
   - Bordado y pliegues: valor estético (condición 1).
   - -30 % y «Alta calidad»: etiquetas promocionales (condición 1).
   - Clase de estudio: Fundas de nórdico + Sábanas ajustables + Fundas de almohada → juego, el mismo resultado que el juego Salvia 642.
   - Para la auditoría: el marcado declara como categoría «Inicio», y la ruta de navegación no tiene categoría.
2. **Protector de colchón Basic 010, revisado con D-028 y D-029.** Sin cambios.
   - Los atributos de su madre, Protectores para colchones, entran en la base heredada.
   - Cubrecolchones hg-15-1-12 (Mattress Toppers), homónimo en español, no es su clasificación objetiva.
   - Clase de estudio: Cubrecolchones, sin especializaciones.
