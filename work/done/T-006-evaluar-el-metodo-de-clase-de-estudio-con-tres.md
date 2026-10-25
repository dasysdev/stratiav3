---
id: T-006
title: Evaluar el método de clase de estudio con tres casos más
status: hecha
depends:
milestone: taxonomia
created: 2026-10-24
closed: 2026-10-25
---

## Objetivo

Aplicar D-020, D-021 y D-022 a mano a toallas (Burrito Blanco), sofá cama (Todoplano) y juguete de cuerda para perro (Kiwoko) y sacar conclusiones sobre el método

## Criterios de aceptación

- [x] Cada caso con clase general Shopify y contraste Google/Amazon
- [x] Cada candidata evaluada con las cinco condiciones
- [x] Clase de estudio compuesta por caso
- [x] Hallazgos sobre el método: dónde funciona, dónde falla y qué falta

## Resultado

Tres casos (toallas, sofá cama, juguete): composición por piezas, condición 4 estricta y beneficios reclamados en el canon (D-023 a D-025)

## Notas

- 2026-10-24 Toallas: general Shopify hg-15-4 Toallas (el juego abarca hg-15-4-1-1 baño y hg-15-4-5 mano) = Google 4077; Amazon 3244784031 (TOWEL). Especializaciones: juego (solo Amazon 3244792031 'Juegos de toallas' y PTD towel_form_type; Shopify sin pieces-included en Toallas) y uso de baño (estrecha la clase: deja fuera playa y cocina). Algodón, cenefa jacquard y azul son valores.
- 2026-10-24 Sofá cama: general Shopify fr-22-7 (también encaja en la hermana fr-22-4 Sofás de dos plazas) → Google 460 (más amplia); Amazon en dos contextos: Dormitorio > Sofás cama con patas (BED) y Salón > Sofás (SOFA: sofa_type, mattress, sleeping_area_dimensions). 'Dos plazas': valor. Apertura italiana: cambia la aplicabilidad de las cuestiones de colchón, pero el único apoyo es futon-frame-conversion-mechanism (en Futones) → caso límite de la condición 4. Sin especializaciones aceptadas.
- 2026-10-24 Juguete: general Shopify ap-2-3-7 = Google 5010; Amazon 13441958031 con hijos Cuerdas y Juguetes para morder (PET_TOY: pet_toy_type, dog_breed_size). Especializaciones: cuerda (Shopify dog-toy-type=Soga; Amazon Cuerdas; PTD 'Juguete para tirar') y mordedor (Shopify Mordedor/Mordedor agresivo; Amazon Juguetes para morder). Higiene dental: reclamo de beneficio; 'Dental' solo existe para snacks → no. Polipropileno, forma de hueso, 20 cm y color: valores.
- 2026-10-24 Decisión del usuario (H1): si el producto abarca varias categorías, la clase es una composición de ellas (toallas = Toallas de baño + Toallas de mano), no el ancestro común; el modelo de clase es un sistema de composición de requisitos.
- 2026-10-24 Decisión del usuario (H3): un beneficio reclamado no es especialización salvo que las referencias tengan un tipo de producto definido por él; su fundamento se evalúa en la auditoría.
- 2026-10-25 Decisión del usuario: una categoría entra en la composición solo si aporta requisitos; condición 4 en lectura estricta (lo que falla queda condicionado dentro de la clase general).
- 2026-10-25 Comprobación del sofá: fr-22-4 (dos plazas) y fr-22-7 (cama) tienen los mismos 9 atributos; ambas son un subconjunto de los 17 de fr-22 Sofás (en Shopify las hojas no heredan todos los atributos de la madre). En Amazon 'dos plazas' es un valor (sofa_type, seating_capacity), sin PTD propio. Por tanto no aporta requisitos y no entra. Sofás cama sí aporta, pero el apoyo viene de Amazon (sofa_type=Sofá cama, mattress, sleeping_area_dimensions), no de Shopify.
- 2026-10-25 Toallas: hg-15-4-1-1 (baño) y hg-15-4-5 (mano) también tienen atributos idénticos y el mismo PTD TOWEL. Mano solo aporta si los requisitos se cuentan por pieza (entidad). Pendiente de confirmar con el usuario, junto con su efecto en el caso de las sábanas.
- 2026-10-25 Decisión del usuario: una categoría entra si aporta requisitos al producto o a alguna de sus piezas (cada pieza de un juego es una entidad). Las sábanas se recomponen por piezas: Sábanas planas + Sábanas ajustables + Fundas de almohada + juego + uso invernal + tejido polar.
- 2026-10-25 Documentado: D-023 (composición por categorías y piezas, modifica D-021), D-024 (condición 4 estricta), D-025 (beneficios reclamados); demand-model 1.4, subclasses 1.3, product-taxonomy 1.2. Revisión independiente aplicada: nuevas I-12, OQ-39 y OQ-40.
