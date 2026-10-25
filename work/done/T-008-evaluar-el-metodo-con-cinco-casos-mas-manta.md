---
id: T-008
title: Evaluar el método con cinco casos más (manta, plaid, zapatillas de baño, protector de colchón, cojín)
status: hecha
depends:
milestone:
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Aplicar D-020 a D-027 a mano a cinco productos de Burrito Blanco y anotar dónde el método funciona o falla

## Criterios de aceptación

- [x] Cada caso con su composición (categorías y especializaciones) y contraste en Google y Amazon
- [x] Cada candidata evaluada con las cinco condiciones y las reglas D-024 a D-027
- [x] Hallazgos sobre el método

## Resultado

Seis casos más (manta, plaid, zapatillas, protector, cojín, funda nórdica bordada): clasificación objetiva, base heredada, características especiales de PTD, material reciclado y propósito de la clase en el canon (D-028 a D-032)

## Notas

- 2026-10-25 Manta Nacarina 046: Mantas hg-15-1-4 = Google 1985; Amazon Mantas para cama 3250001031 (BLANKET). Mantas decorativas (hg-15-1-4-2) y Mantas para sillones y sofás (hg-3-77) no aportan requisitos (atributos incluidos en Mantas): no entran. Uso sofá/cama ligado a la medida (variante). Tejido polar (valor Nacarina®): estática y pelusa ya en la base de BLANKET (special_feature Antiestático, Sin pelusa); trae bolitas → especialización. Invierno: valor (season, warmth-rating y thermal_performance en la base), al revés que en sábanas.
- 2026-10-25 Plaid de punto 101: Mantas decorativas hg-15-1-4-2 → Google 1985 (más amplia); Amazon sin nodo de plaid (BLANKET). La hoja tiene 3 atributos y la madre 9: si la base es literal, hg-3-77 aportaría tejido, color, cuidados y patrón (composición absurda de una sola pieza). En Shopify, 1749 hijas tienen menos atributos que su madre. Tejido de punto: trae enganchones, deformación y bolitas; apoyo BLANKET weave_type 'Tejido de Punto Ancho' (más estrecha); Shopify sin dimensión de punto en mantas. Acrílico: valor. Trenzas: estético.
- 2026-10-25 Zapatillas de baño 50: Pantuflas aa-8-7 → Google 187 (más amplia); Amazon Zapatillas de estar por casa (SLIPPER). Uso de baño: sin dimensión de uso en ninguna referencia (condición 4) → requisitos condicionados. Rizo 450 g/m²: valor (Absorbe la humedad y apparel_fabric_weight_class en la base de SLIPPER). '1 juego' = un par, no es la especialización juego. Shopify ES 'Zapatillas' aa-8-8 = sneakers.
- 2026-10-25 Protector Basic 010: Cubrecolchones hg-15-1-6-2 (Mattress Pads) = Google 2991; Amazon Almohadillas de colchón 27003778031 / Protectores de colchón 2822732031 (MATTRESS_COVER). Acolchado ya es la categoría (D-021). Algodón: valor. Impermeable y relleno no declarados (auditoría). Shopify ES llama 'Cubrecolchones' a dos categorías (hg-15-1-6-2 Mattress Pads y hg-15-1-12 Mattress Toppers).
- 2026-10-25 Cojín 018: Cojines hg-3-64 = Google 4454; Amazon Cojines 2844244031 (PILLOW). Funda + relleno: partes que la categoría ya modela (cover-*, filler-*), no piezas de un juego; ninguna categoría de fundas aporta requisitos propios. Material reciclado: apoyo PILLOW special_feature 'Reciclada'; trae proporción y componente → especialización candidata; 'sostenible' = beneficio (D-025). Composición contradictoria en la página (87/13 frente a 54/13): auditoría.
- 2026-10-25 Decisión del usuario: una categoría candidata en la que el producto entra por clasificación objetiva se añade aunque no aporte requisitos (orden y coherencia); enmienda D-023. Aceptadas las lecturas: plaid = Mantas decorativas, sin hg-3-77 (entrada duplicada); manta Nacarina = Mantas (el uso en sofá depende de la variante). Consecuencia: sofá cama Luna pasa a Sofás cama + Sofás de dos plazas.
- 2026-10-25 Decisiones del usuario: (1) base de una categoría de Shopify = atributos propios + los de sus madres; (2) las Características especiales (special_feature) de un PTD cuentan como dimensiones de la base y como apoyo; (3) material reciclado = especialización; 'sostenible' = beneficio (D-025).
- 2026-10-25 Funda nórdica bordada 401 (percal 200 hilos, peinado y mercerizado; funda nórdica + bajera + 1 o 2 fundas de almohada según medida): Fundas de nórdico + Sábanas ajustables + Fundas de almohada → juego (Amazon 3250005031, BED_LINEN_SET), como Salvia 642. Percal y 200 hilos: valores (fabric-weave, weave_type, thread). Mercerizado: valor de acabado (BED_LINEN_SET finish_type); peinado sin dimensión en ropa de cama (solo fibras de manualidades); sus efectos (resistencia, suavidad, brillo) son beneficios (D-025). Bordado y pliegues: estético. -30 %: promocional. Juegos de cama hg-15-1-11: warmth-level 'del edredón o la colcha' y Amazon separa BEDDING_SET (con fill_material) de BED_LINEN_SET → no es su clasificación objetiva (pendiente de confirmar, OQ-43). Página: category 'Inicio' en el marcado. Protector Basic 010 revisado con D-028/D-029: sin cambios.
- 2026-10-25 Documentado: D-028 (clasificación objetiva), D-029 (base de Shopify con madres), D-030 (special_feature de PTD), D-031 (material reciclado); demand-model 1.6, cases 1.1, subclasses 1.5, README 1.4; I-12 resuelta, nueva OQ-43. Revisión independiente aplicada; nueva I-14 (casos que cambian con la base ampliada: Luna, cuerda, polar en fundas, juego, apoyo del polar en la manta). Pendiente: decisión sobre Juegos de cama y sobre I-14; documentar la funda nórdica bordada 401.
- 2026-10-25 Documentado D-032 (propósito: requisitos informativos; la denominación por clasificación objetiva solo cuando tiene sentido); I-14 resuelta; Luna y mordedor a valor (el mordedor por interpretación provisional); Juegos de cama no entra; caso de la funda nórdica bordada 401. Revisión independiente aplicada; nueva I-15. demand-model en 250 líneas: propuesto separar «Clase de estudio» en un módulo propio, pendiente de aprobación del usuario.
