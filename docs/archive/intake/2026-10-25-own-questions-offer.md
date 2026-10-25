# Cuestiones propias y especializaciones de oferta

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad. Procede de la evaluación del método con cuatro casos más (tarea T-007): bota Polo E de 5vvalverde.com (https://5vvalverde.com/es/producto/bota-polo-e/), sofá Stressless Wave Cinema outlet de grupotodoplano.com (https://www.grupotodoplano.com/sofa-stressless-wave-cinema-outlet), juego de funda nórdica algodón 144 hilos Salvia floral 642 de burritoblanco.com (https://www.burritoblanco.com/juego-de-funda-nordica-algodon-144-hilos-salvia-floral-642-p-6179-95168.html) y Josera High Protein Adult Sea Fish de guaw.com (https://guaw.com/josera-high-protein-adult-sea-fish-pienso-para-perros-con-pescado.html).*

*Los bloques A y B son decisiones del usuario («1. si», «2. A»). El bloque C es la aplicación de A y B a los casos, elaborada por Claude e ilustrativa.*

## A. Regla de las «cuestiones propias»

Precisa la condición 2 de D-022. Para una dimensión que todo producto de la clase tiene (tapicería, tejido, forma del pienso, etapa vital…), la condición 2 no puede compararse con «la clase general sin esa característica».

Regla aceptada:

> Para una dimensión que todo producto de la clase tiene, un valor es especialización solo si trae cuestiones propias, que no salen de las dimensiones de la clase general. Si solo cambia los valores, o solo hace que algunas cuestiones dejen de aplicarse, es un valor que condiciona (como en D-024).

Consecuencias aceptadas por el usuario:

- Polar (sábanas) sigue siendo especialización: trae bolitas, electricidad estática y pérdida de pelo.
- Algodón (sábanas, toallas, funda nórdica) es valor: número de hilos, ligamento y gramaje ya están en la base.
- Polipropileno (cuerda) es valor.
- La tela del sofá cama Luna pasa a ser especialización: trae resistencia a la abrasión, desenfundable y antimanchas. Corrige el caso documentado en D-023, donde figuraba como valor.
- La piel del Stressless es especialización: tipo y acabado de la piel.
- El pienso seco es especialización: tamaño de la croqueta.
- Adulto es valor: solo deja de aplicar lo de crecimiento.

## B. Condición 1 ampliada a la oferta

Opción A; enmienda la condición 1 de D-022. La condición 1 pasa a decir: «es del producto o de la oferta, y estable». Lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta. Resuelve la parte de OQ-37 sobre si la regla se aplica a las clases de oferta (BASE §4: «clase de producto u oferta»).

## C. Aplicación a los casos (ilustrativa; no son clases aprobadas)

1. **Sofá cama Luna (corrección).** Sofás cama → tapicería textil (valor: tela Victor).
   - Apoyo: dimensión de tapicería en Shopify Sofás cama (seat-upholstery-material) y en PTD SOFA (fabric_type).
   - SOFA no tiene dimensiones de abrasión ni de tipo de cuero.
2. **Bota Polo E.** Bota de equitación de hombre, piel de novillo, forrada en piel, piso de suela y goma, fabricación Goodyear, cremallera lateral y dos broches.
   - Clase general: Botas (Shopify aa-8-3 → Google 187, más amplia).
   - Especialización: uso de equitación. Apoyo: Shopify boot-style = Equitación; Amazon «Botas de equitación» (de campo, de cuadra, largas, paddock), con PTD BOOT. Trae compatibilidad con el estribo y ajuste de la caña.
   - El subtipo (largas…) no se declara.
   - La piel es valor: PTD BOOT ya tiene leather_type, así que no trae cuestiones fuera de la base.
   - Goodyear, hombre, cremallera y broches son valores.
   - Clase de estudio: Botas → equitación.
3. **Sofá Stressless Wave Cinema outlet.** Sofá con asientos reclinables individuales (sistema Glide), tapizado en piel, última unidad de exposición, garantía de 1 año «por ser producto outlet».
   - Clase general: Sofás (Shopify fr-22 = Google 460; no encaja en ninguna hija).
   - Especialización «reclinable». Apoyo: Shopify reclining-mechanism; PTD SOFA seat_recline, reclining_seat_count y reclining_position_count. Trae mecanismo, posiciones y espacio necesario.
   - Especialización «tapicería de piel» (bloque A).
   - Especialización de oferta (bloque B): estado de la unidad distinto de nuevo, con «exposición» como valor. Apoyo: grupo de oferta de PTD SOFA (condition_type, condition_note, garantía). Trae estado de la unidad, posibles marcas, si se recibe la unidad expuesta y garantía reducida.
   - «Cinema» solo aparece en el nombre comercial: no declarado.
   - Clase de estudio: Sofás → reclinable + tapicería de piel + estado distinto de nuevo (exposición).
4. **Juego de funda nórdica Salvia floral 642.** Funda nórdica, bajera y 1 o 2 fundas de almohada según medida, 100 % algodón, 144 hilos, estampado floral, bajera para colchones de hasta 32 cm, 4 medidas.
   - Composición por piezas: Fundas de nórdico (Shopify hg-15-1-5 = Google 2541; tiene bedding-pieces-included y fabric-weave) + Sábanas ajustables (bajera) + Fundas de almohada.
   - Más «juego» (Amazon 3250005031 «Juegos de fundas para edredón», PTD BED_LINEN_SET con thread y weave_type).
   - Algodón y 144 hilos son valores (bloque A). Estampado, 32 cm y medidas son valores o variantes.
5. **Josera High Protein Adult Sea Fish.** Pienso seco para perros adultos, todos los tamaños, sabor pescado, sin cereales, proteína 34 %, para perros activos, con «cuidado articular», 12,5 kg.
   - Clase general: Comida para perros sin prescripción médica (Shopify ap-2-3-3-1 = Google 543682; Amazon Perros > Comida > Seca 13442210031, PTD PET_FOOD).
   - Especialización: pienso seco. Apoyo: Shopify pet-food-form = Seco; Amazon nodo «Seca». Trae tamaño de la croqueta.
   - Adulto, sin cereales, alto en proteína, perros activos, sabor y 12,5 kg son valores.
   - «Cuidado articular» es un beneficio reclamado (D-025): Shopify lo tiene como valor de pet-dietary-requirements, que no es un tipo de producto.
   - Clase de estudio: Comida para perros sin prescripción → seco.

## Observaciones (no son reglas)

- La regla A se decide con la base de la clase en las referencias. Por ejemplo, leather_type está en BOOT pero no en SOFA, así que la piel es valor en botas y especialización en sofás.
- Las características de oferta solo tienen apoyo en el grupo de oferta de PTD.
