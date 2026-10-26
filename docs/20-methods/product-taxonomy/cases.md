---
id: product-taxonomy-cases
title: Taxonomía — casos de evaluación de la clase de estudio
layer: method
status: propuesta
version: 1.12
updated: 2026-10-26
sources: [INTAKE 2026-10-25-class-composition, INTAKE 2026-10-25-own-questions-offer, INTAKE 2026-10-25-objective-classification, INTAKE 2026-10-25-requirements-purpose, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-amazon-source-blocks, INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-offer-application, INTAKE 2026-10-26-general-layer-issues, INTAKE 2026-10-26-open-issues-resolution, INTAKE 2026-10-26-model-name-full-composition]
---

# Taxonomía — casos de evaluación de la clase de estudio

Parte de [Taxonomía de clases de producto](README.md).

> **Casos ilustrativos.** Aplican el [eje de base](../../10-model/study-class.md#clase-general-el-eje-de-base), la [composición de la clase](../../10-model/study-class.md#composición-de-la-clase) y el [criterio de especialización](../../10-model/study-class.md#criterio-de-especialización); **no son clases aprobadas**. Fuentes: `INTAKE 2026-10-25-class-composition` (toallas, sofá cama, juguete de cuerda), `INTAKE 2026-10-25-own-questions-offer` (corrección del sofá cama y los cuatro casos siguientes), `INTAKE 2026-10-25-objective-classification` (segunda corrección del sofá cama y cinco casos más) e `INTAKE 2026-10-25-requirements-purpose` (tercera corrección del sofá cama, juguete de cuerda y juego de funda nórdica revisados, apoyo del polar de la manta, protector revisado y juego de funda nórdica bordada) y `INTAKE 2026-10-25-requirement-blocks` (Stressless, sofá cama y funda bordada revisados con la capa general y las cuestiones inferidas, [D-036](../../30-governance/decisions.md#d-036) y [D-037](../../30-governance/decisions.md#d-037)) e `INTAKE 2026-10-25-offer-application` (modelo del producto y aplicación de la oferta, [D-047](../../30-governance/decisions.md#d-047)). En los casos de los cuatro últimos, las reglas y sus consecuencias son decisiones del usuario; la aplicación a los casos la elaboró Claude, es ilustrativa y sus especializaciones quedan provisionales hasta su validación ([D-022](../../30-governance/decisions.md#d-022)). El caso de trabajo inicial, el juego de sábanas de coralina, está en [subclasses](subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).

## Juego de toallas

**Producto:** juego de toallas Azul 080 de burritoblanco.com: 3 toallas (bidé 30×50, lavabo 50×100, ducha 70×140), 100 % algodón, lisas con cenefa jacquard.

| Componente | Apoyo en las referencias | Resultado |
|---|---|---|
| Toallas de baño (`hg-15-4-1-1` → Google `576`), para la de ducha | Categoría de Shopify | Entra |
| Toallas de mano (`hg-15-4-5` → Google `4077`, más amplia), para la de lavabo | Mismos atributos que Toallas de baño (`color`, `fabric`, `pattern`, `towel-weave`) y mismo PTD `TOWEL` | Entra: aporta requisitos a otra pieza |
| Toalla de bidé | Entre Toallas de mano y Toallitas (`hg-15-4-1-2`) | Provisional |
| Juego | Amazon `3244792031` «Juegos de toallas», PTD `TOWEL` con `towel_form_type`. Shopify no tiene atributo de piezas incluidas en Toallas | Especialización |
| Algodón | — | Valor: «número de hilos, ligamento y gramaje ya están en la base» ([D-026](../../30-governance/decisions.md#d-026)) |
| Cenefa jacquard, azul | — | Valores |

**Clase de estudio:** Toallas de baño + Toallas de mano (la de bidé, provisional entre Toallas de mano y Toallitas) → juego. La especialización «uso de baño», que se consideró al subir a la categoría madre Toallas, deja de ser necesaria.

## Sofá cama

**Producto:** sofá cama Luna de dos plazas de grupotodoplano.com: tela Victor, «sistema de apertura fácil» (sin mecanismo declarado), revistero lateral, 2 cojines, sofá de 92×131×94 cm y cama de 131×180 cm, para uso diario o para invitados.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Sofás cama (`fr-22-7` → Google `460`, más amplia) | Amazon: «Sofás cama con patas» `56171664031` (PTD `BED`) y Salón > Sofás (PTD `SOFA`: `sofa_type` = Sofá cama, `mattress`, `sleeping_area_dimensions`) | Entra |
| Sofás de dos plazas (`fr-22-4`) | Mismos 9 atributos que Sofás cama. En Amazon, «dos plazas» es un valor de `sofa_type` y de `seating_capacity`, sin PTD propio | Entra por clasificación objetiva, aunque no aporta requisitos propios: nombra lo que el producto es. Es un alias: etiqueta la denominación, fuera de la identidad ([D-033](../../30-governance/decisions.md#d-033), [D-028](../../30-governance/decisions.md#d-028), [D-032](../../30-governance/decisions.md#d-032)) |
| Mecanismo de apertura | No declarado: «apertura italiana» solo aparece en el nombre de un icono. Ni Shopify Sofás cama ni PTD `SOFA` tienen la dimensión (solo `futon-frame-conversion-mechanism`, en Futones) | Cuestión inferida, añadido provisional fuera de la clave hasta su aceptación ([D-041](../../30-governance/decisions.md#d-041)): «¿qué mecanismo de apertura tiene?» (principal) ([D-036](../../30-governance/decisions.md#d-036)) |
| Tela Victor (tapicería textil) | Dimensión de tapicería en Shopify Sofás cama (`seat-upholstery-material`) y en PTD `SOFA` (`fabric_type`). `SOFA` no tiene propiedad de abrasión ni de tipo de cuero, pero su `special_feature` incluye «Resistente a la abrasión», «Resistente a las manchas» y «Funda extraíble» | Valor que condiciona: resistencia a la abrasión, desenfundable y antimanchas están en la base y siguen siendo requisitos ([D-030](../../30-governance/decisions.md#d-030), [D-032](../../30-governance/decisions.md#d-032), [D-039](../../30-governance/decisions.md#d-039)) |
| Color, revistero, cojines, medidas | — | Valores |

**Clase de estudio:** Sofás cama + Sofás de dos plazas.

Observaciones (no son reglas): lo que distingue a Sofás cama solo lo recoge Amazon. En Shopify, las hojas tienen menos atributos que su madre: Sofás tiene 17 y sus hijas, 9. Con la base heredada ([D-029](../../30-governance/decisions.md#d-029)), Sofás cama incluye los atributos de Sofás.

## Juguete de cuerda para perro

**Producto:** hueso mordedor de cuerda Tootoy! de kiwoko.com: fibra de polipropileno trenzada, para morder, lanzar o tirar, 20 cm, apto para todos los tamaños, con efecto declarado de higiene dental.

| Componente o candidata | Apoyo en las referencias | Efecto sobre las cuestiones | Resultado |
|---|---|---|---|
| Juguetes para perros (`ap-2-3-7` = Google `5010`; Amazon `13441958031`, PTD `PET_SUPPLIES`; sus nodos hijos, entre ellos Cuerdas y Juguetes para morder, tienen PTD `PET_TOY`) | — | — | Clase general |
| Cuerda | Shopify `dog-toy-type` = Soga; Amazon `13442235031` «Cuerdas»; PTD `PET_TOY`, `pet_toy_type` = Juguete para tirar | Añade deshilachado e ingestión de fibras; el lavado está en la base (`PET_TOY` «Lavable», [D-030](../../30-governance/decisions.md#d-030)) y sigue siendo requisito ([D-032](../../30-governance/decisions.md#d-032), [D-039](../../30-governance/decisions.md#d-039)) | Especialización |
| Mordedor | Shopify: Mordedor y Mordedor agresivo; Amazon `13442241031` «Juguetes para morder» | La resistencia a la mordida está en la base (`PET_TOY` «Uso rudo» y «Tecnología Chew Guard», [D-030](../../30-governance/decisions.md#d-030)) y sigue siendo requisito | Valor que condiciona, por interpretación provisional ([D-032](../../30-governance/decisions.md#d-032)) |
| Tirar, lanzar | — | Cubiertas por «cuerda» (condición 5) | Absorbidas |
| Higiene dental | «Dental» solo existe para snacks | Beneficio reclamado | No es especialización |
| Polipropileno, forma de hueso, 20 cm, color | — | — | Valores |

**Clase de estudio:** Juguetes para perros → cuerda.

## Bota de equitación

**Producto:** bota Polo E de 5vvalverde.com: bota de equitación de hombre, piel de novillo, forrada en piel, piso de suela y goma, fabricación Goodyear, cremallera lateral y dos broches.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Botas (`aa-8-3` → Google `187`, más amplia) | — | Clase general |
| Uso de equitación | Shopify `boot-style` = Equitación; Amazon «Botas de equitación» (de campo, de cuadra, largas, paddock), PTD `BOOT` | Especialización: trae compatibilidad con el estribo y ajuste de la caña |
| Subtipo (largas…) | — | No declarado |
| Piel de novillo | PTD `BOOT` ya tiene `leather_type` | Valor: no trae cuestiones fuera de la base |
| Goodyear, hombre, cremallera, broches | — | Valores |

**Clase de estudio:** Botas → equitación.

## Sofá reclinable de exposición

**Producto:** sofá Stressless Wave Cinema outlet de grupotodoplano.com: asientos reclinables individuales (sistema Glide), tapizado en piel, última unidad de exposición, con un precio de 5.815 € junto a uno de 9.693 € («última unidad a precio único»), garantía de 1 año «por ser producto outlet».

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Sofás (`fr-22` = Google `460`) | No encaja en ninguna hija | Clase general |
| Reclinable | Shopify `reclining-mechanism`; PTD `SOFA` `seat_recline`, `reclining_seat_count`, `reclining_position_count`, `furniture_wall_clearance` | Valor que condiciona: mecanismo, posiciones y espacio necesario están en la base ([D-037](../../30-governance/decisions.md#d-037)) |
| Tapicería de piel | Shopify `material` de Sofás («Piel», «Cuero»); PTD `SOFA` `upholstery.fabric_type` = «Cuero» ([D-071](../../30-governance/decisions.md#d-071)) | Especialización: trae tipo y acabado de la piel ([D-026](../../30-governance/decisions.md#d-026)) |
| Outlet: unidad de exposición | Capa general: estado de la unidad, garantía, devoluciones, descuento ([D-034](../../30-governance/decisions.md#d-034)) | Valor de la oferta que activa las cuestiones condicionadas de unidad no nueva: aplicación de la oferta, no especialización ([D-037](../../30-governance/decisions.md#d-037)) |
| «Cinema» | Solo en el nombre comercial | No declarado |

**Clase de estudio:** Sofás → tapicería de piel. Modelo de demanda: «Mobiliario › Sofás · tapicería de piel» ([D-077](../../30-governance/decisions.md#d-077)); aplicación de la oferta: unidad no nueva, con descuento, cantidad limitada ([D-047](../../30-governance/decisions.md#d-047); anterior a [D-066](../../30-governance/decisions.md#d-066), que añade garantía comercial, asistencia posventa y opiniones publicadas).

## Juego de funda nórdica

**Producto:** juego de funda nórdica Salvia floral 642 de burritoblanco.com: funda nórdica, bajera y 1 o 2 fundas de almohada según medida, 100 % algodón, 144 hilos, estampado floral, bajera para colchones de hasta 32 cm, 4 medidas.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Fundas de nórdico (`hg-15-1-5` = Google `2541`) | Tiene `bedding-pieces-included` y `fabric-weave` | Entra (funda nórdica) |
| Sábanas ajustables | — | Entra (bajera) |
| Fundas de almohada | — | Entra (fundas) |
| Juego | Amazon `3250005031` «Juegos de fundas para edredón», PTD `BED_LINEN_SET` (`included_components`, `number_of_pieces`; también `thread` y `weave_type`) | Especialización: aporta qué piezas incluye y cuántas de cada una; las medidas, los bloques de cada pieza ([D-086](../../30-governance/decisions.md#d-086)) ([D-023](../../30-governance/decisions.md#d-023), [D-032](../../30-governance/decisions.md#d-032)) |
| Algodón, 144 hilos | — | Valores: «número de hilos, ligamento y gramaje ya están en la base» ([D-026](../../30-governance/decisions.md#d-026)) |
| Estampado, 32 cm, medidas | — | Valores o variantes |

**Clase de estudio:** Fundas de nórdico + Sábanas ajustables + Fundas de almohada → juego.

## Pienso para perros

**Producto:** Josera High Protein Adult Sea Fish de guaw.com: pienso seco para perros adultos, todos los tamaños, sabor pescado, sin cereales, proteína 34 %, para perros activos, con «cuidado articular», 12,5 kg.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Comida para perros sin prescripción médica (`ap-2-3-3-1` = Google `543682`; Amazon Perros > Comida > Seca `13442210031`, PTD `PET_FOOD`) | — | Clase general |
| Pienso seco | Shopify `pet-food-form` = Seco; Amazon nodo «Seca» | Especialización: trae tamaño de la croqueta |
| Adulto | — | Valor: «solo deja de aplicar lo de crecimiento» ([D-026](../../30-governance/decisions.md#d-026)) |
| Sin cereales, alto en proteína, perros activos, sabor, 12,5 kg | — | Valores |
| Cuidado articular | Shopify lo tiene como valor de `pet-dietary-requirements`, que no es un tipo de producto | Beneficio reclamado ([D-025](../../30-governance/decisions.md#d-025)) |

**Clase de estudio:** Comida para perros sin prescripción → seco.

## Manta de cama o de sofá

**Producto:** manta super suave tejido Nacarina® diseño 046 color Secuoya de burritoblanco.com: manta de cama o de sofá, tejido Nacarina® («pelito extraído de la fibra», tacto aterciopelado), 100 % poliéster, «para las noches más frías del invierno», 3 medidas (140×200 «mantita de sofá», 170×240 y 230×240).

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Mantas (`hg-15-1-4` = Google `1985`; Amazon «Mantas y colchas > Mantas para cama» `3250001031`, PTD `BLANKET`) | — | Clase general |
| Mantas decorativas (`hg-15-1-4-2`) | El uso en sofá depende de la medida (variante) | No entra: no es su clasificación objetiva ([D-028](../../30-governance/decisions.md#d-028)) |
| Tejido polar (valor: Nacarina®) | Electricidad estática y pelusa ya están en la base de `BLANKET` (`special_feature` «Antiestático» y «Sin pelusa», [D-030](../../30-governance/decisions.md#d-030)). Apoyo: Shopify Mantas `fabric` «Vellón»; `BLANKET` `material` «Forro polar» y `weave_type` «Tejido de pelo» | Especialización: trae las bolitas, que no están en la base ([D-026](../../30-governance/decisions.md#d-026)) |
| Invierno | Temporada y abrigo en la base: Shopify `season` y `warmth-rating`; `BLANKET` `seasons` y `thermal_performance_description` | Valor, al contrario que en las sábanas, donde el abrigo no está en la base |
| Poliéster, color secuoya, medidas | — | Valores o variantes |

**Clase de estudio:** Mantas → tejido polar.

## Plaid de punto

**Producto:** plaid de punto color Arena diseño 101 de burritoblanco.com: punto con trenzas, 100 % acrílico, 130×170, para el sofá o decorativo.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Mantas decorativas (`hg-15-1-4-2` → Google `1985`, más amplia; Amazon no tiene nodo de plaid, PTD `BLANKET`) | Con la base de Mantas ([D-029](../../30-governance/decisions.md#d-029)) | Clase general, por clasificación objetiva ([D-028](../../30-governance/decisions.md#d-028)) |
| Mantas para sillones y sofás (`hg-3-77`) | Entrada duplicada en Decoración para el mismo tipo de producto | No entra |
| Tejido de punto | `BLANKET` `weave_type` «Tejido de Punto Ancho» (más estrecha). Shopify no tiene dimensión de punto en mantas | Especialización: trae enganchones, deformación y bolitas |
| Acrílico | — | Valor: las bolitas ya las trae el punto y el acrílico solo cambia la respuesta esperada |
| Trenzas | — | Valor estético |

**Clase de estudio:** Mantas decorativas → tejido de punto.

## Zapatillas de baño

**Producto:** zapatillas de baño color Blanco 50 de burritoblanco.com: rizo de algodón 100 %, 450 g/m², tallas 40 y 46, «1 juego» por talla.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Pantuflas (`aa-8-7` → Google `187`, más amplia; Amazon «Zapatos > Zapatillas de estar por casa», PTD `SLIPPER`) | — | Clase general |
| Uso de baño | Ninguna referencia tiene dimensión de uso | No cumple la condición 4. El agarre sobre suelo mojado queda como requisito condicionado ([D-024](../../30-governance/decisions.md#d-024)) |
| Rizo | Absorción (`special_feature` «Absorbe la humedad») y gramaje (`apparel_fabric_weight_class`) en la base de `SLIPPER` ([D-030](../../30-governance/decisions.md#d-030)) | Valor |
| «1 juego» | Es un par, la unidad normal de la clase | No es la especialización «juego» |

**Clase de estudio:** Pantuflas, sin especializaciones.

## Protector de colchón

**Producto:** protector de colchón Basic 010 de burritoblanco.com: acolchado, algodón 100 %, cama de 200.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Cubrecolchones (`hg-15-1-6-2`, *Mattress Pads* = Google `2991`; Amazon «Almohadillas de colchón» `27003778031` y «Protectores de colchón» `2822732031`, PTD `MATTRESS_COVER`) | Con la base de Protectores para colchones ([D-029](../../30-governance/decisions.md#d-029)) | Clase general |
| Acolchado | Ya es la categoría ([D-021](../../30-governance/decisions.md#d-021)) | No es especialización |
| Algodón | — | Valor |
| Impermeabilidad, relleno | No declarados | Corresponden a la auditoría |
| Cubrecolchones `hg-15-1-12` (*Mattress Toppers*) | Homónimo en español | No es su clasificación objetiva ([D-028](../../30-governance/decisions.md#d-028)) |

**Clase de estudio:** Cubrecolchones, sin especializaciones.

## Cojín decorativo con relleno

**Producto:** cojines decorativos con relleno 018 Azul de burritoblanco.com: funda con una cara texturada y otra en efecto jacquard, 87 % algodón reciclado y 13 % poliéster reciclado según la descripción, 50×50, incluye funda y relleno, «producto sostenible».

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Cojines (`hg-3-64` = Google `4454`; Amazon «Cojines y accesorios > Cojines» `2844244031`, PTD `PILLOW`) | — | Clase general |
| Funda y relleno | Partes que la categoría ya modela (atributos `cover-*` y `filler-*`) | No son piezas de un juego. Ninguna categoría de fundas aporta requisitos propios ni es su clasificación objetiva |
| Material reciclado | `PILLOW` `special_feature` «Reciclada» ([D-030](../../30-governance/decisions.md#d-030)) | Especialización: trae qué proporción y en qué parte ([D-031](../../30-governance/decisions.md#d-031)) |
| «Sostenible» | — | Beneficio reclamado ([D-025](../../30-governance/decisions.md#d-025)) |
| Jacquard, colores | — | Valores |

**Clase de estudio:** Cojines → material reciclado.

## Juego de funda nórdica bordada

**Producto:** fundas nórdicas bordadas algodón percal 200 hilos 401 Blanco de burritoblanco.com: funda nórdica, bajera ajustable y una funda de almohada (cama de 135) o dos (resto de medidas); algodón percal de 200 hilos, peinado y mercerizado; tiras bordadas en la funda nórdica y en las bocas de las fundas de almohada, y pliegues decorativos; 5 medidas (de 135 a 200); descuento del 30 %.

| Componente o candidata | Apoyo en las referencias | Resultado |
|---|---|---|
| Fundas de nórdico (`hg-15-1-5` = Google `2541`) + Sábanas ajustables + Fundas de almohada | Una categoría por pieza | Clase general (composición por piezas) |
| Juego | Amazon `3250005031` «Juegos de fundas para edredón», PTD `BED_LINEN_SET` (`included_components`, `number_of_pieces`) | Especialización: aporta qué piezas incluye y cuántas de cada una; las medidas, los bloques de cada pieza ([D-086](../../30-governance/decisions.md#d-086)) |
| Juegos de cama (`hg-15-1-11`) | Sus atributos distintivos son `warmth-level`, «del edredón o la colcha», y `material-treatment`. Amazon separa los juegos de edredón o colcha (PTD `BEDDING_SET`, con `fill_material`) de los juegos de fundas (`BED_LINEN_SET`) | No entra: no aporta requisitos y traería uno que no aplica (el nivel de calidez, en un juego de fundas sin relleno); tampoco tiene sentido por denominación ([D-032](../../30-governance/decisions.md#d-032)) |
| Percal, 200 hilos | Shopify `fabric-weave`; `BED_LINEN_SET` `weave_type` y `thread` | Valores |
| Mercerizado | Dimensión de acabado en `BED_LINEN_SET` (`finish_type`) | Respuesta a un requisito de la categoría con origen «referencias» (`amazon-ptd-prop:BED_LINEN_SET.finish_type`, [D-039](../../30-governance/decisions.md#d-039)) |
| Peinado | Sin dimensión en ropa de cama (solo en fibras de manualidades) | Respuesta a la cuestión inferida, añadido provisional hasta su aceptación ([D-041](../../30-governance/decisions.md#d-041)), sobre la preparación del algodón (complementaria); el acabado sale de la base ([D-036](../../30-governance/decisions.md#d-036)) |
| «Más resistente y suave», «mayor brillo» | — | Beneficios reclamados ([D-025](../../30-governance/decisions.md#d-025)) |
| Bordado, pliegues | — | Valor de la decoración: su cuestión es la de la base (patrón) y el valor es la respuesta ([D-033](../../30-governance/decisions.md#d-033)) |
| -30 % | Capa general: descuento | Valor de la oferta que activa la cuestión condicionada de descuento (aplicación: con descuento) ([D-034](../../30-governance/decisions.md#d-034), [D-037](../../30-governance/decisions.md#d-037)) |
| «Alta calidad» | — | Etiqueta promocional (condición 1) |

**Clase de estudio:** Fundas de nórdico + Sábanas ajustables + Fundas de almohada → juego, el mismo resultado que el juego de funda nórdica Salvia. Para la auditoría: el marcado declara como categoría «Inicio», y la ruta de navegación no tiene categoría.

Con [D-047](../../30-governance/decisions.md#d-047), las dos fundas nórdicas comparten modelo de demanda y solo difieren en la oferta (esta, con descuento): los 14 casos dan 13 modelos para 14 ofertas.

## Observaciones de la evaluación

No son reglas.

De `INTAKE 2026-10-25-class-composition` (toallas, sofá cama, juguete de cuerda y sábanas):

- Google solo confirmó la clase general en todos los casos.
- Amazon aportó el anclaje más fino (juegos, cuerdas, mordedores), y PTD, las dimensiones (`seasons`, `pet_toy_type`, `mattress`).
- El «juego» se repite como especialización, y en Shopify solo aparece como atributo en algunas categorías (Sábanas sí, Toallas no).
- Dos observaciones de ese update quedan superadas por la [regla de las cuestiones propias](../../10-model/study-class.md#criterio-de-especialización) ([D-026](../../30-governance/decisions.md#d-026)): «el material habitual de la clase queda como valor» y «el método no fuerza especializaciones (sofá cama)». La segunda vuelve a valer: con la base ampliada, la tela del sofá cama es valor ([D-032](../../30-governance/decisions.md#d-032)).

De `INTAKE 2026-10-25-own-questions-offer` (bota, sofá reclinable, funda nórdica, pienso):

- La regla de las cuestiones propias se decide con la base de la clase en las referencias: `leather_type` está en PTD `BOOT` pero no en `SOFA`, así que la piel es valor en botas y especialización en sofás.
- Las características de oferta solo tienen apoyo en el grupo de oferta de PTD. Queda sin objeto con la capa general ([D-037](../../30-governance/decisions.md#d-037)).

De `INTAKE 2026-10-25-objective-classification` (manta, plaid, zapatillas de baño, protector de colchón y cojín):

- En dos casos (zapatillas y protector) no sale ninguna especialización.
- La misma característica cambia según la base: invierno es especialización en sábanas y valor en mantas.
- En Shopify en español hay nombres que coinciden: «Cubrecolchones» son `hg-15-1-6-2` (*Mattress Pads*) y `hg-15-1-12` (*Mattress Toppers*), y «Zapatillas» (`aa-8-8`) es calzado deportivo. Por eso se trabaja con identificadores.
- La página del cojín se contradice en la composición (87/13 en la descripción; 54 % algodón y 13 % poliéster en la ficha). Es un hallazgo para la auditoría.

## Relacionado

- [subclasses](subclasses.md) — prueba de especialización y caso de las sábanas.
- [study-class](../../10-model/study-class.md) — clase de estudio (canon).
