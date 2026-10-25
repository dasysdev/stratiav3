# Experimento base · reglamento v0 · 2026-10-25

Tres agentes nuevos clasificaron los 14 casos del conjunto (`demand-engine/cases/`, todos de desarrollo). Solo tenían el reglamento (`classifier/rulebook.md`) y `bin/taxo`; no veían la documentación ni los resultados esperados. Cada caso se ejecutó una vez. Comparación: `bin/compare demand-engine/var/runs/2026-10-25-baseline`, más una revisión manual de las cuestiones.

## Resultado

| Nivel | Coincidencia |
|---|---|
| Componentes (categorías de Shopify) | **14/14** |
| Descartes esperados (Juegos de cama, duplicados, homónimos) | **5/5** |
| Etiquetas de especialización | 7/14 |
| Requisitos (cuestiones), revisión manual | 7 iguales · 5 con una cuestión de más o de menos · 2 con diferencias reales |

| Caso | Etiquetas | Requisitos | Diferencia |
|---|---|---|---|
| bota-polo-e | = | ≈ | Equitación: falta «ajuste de la caña»; añade disciplina y espuelas |
| cojin-018 | = | ≈ | Reciclado: falta «en qué parte»; añade preconsumo/posconsumo y certificación |
| funda-nordica-bordada-401 | = | = | El peinado como requisito condicionado («¿peinado o cardado?») |
| funda-nordica-salvia-642 | = | = | — |
| protector-basic-010 | = | = | — |
| toallas-azul-080 | = | = | La toalla de bidé en Toallas de mano (el caso la deja provisional) |
| zapatillas-bano-50 | = | = | Etiquetas cruzadas (uso de baño y rizo), mismas cuestiones |
| stressless-wave-outlet | ≠ | = | Reclinable y piel como valor que condiciona, con las mismas cuestiones; outlet como especialización de oferta |
| manta-nacarina-046 | ≠ | = | Polar como valor que condiciona; las bolitas siguen como cuestión |
| sabanas-coralina-999 | ≠ | ≈ | Polar e invierno como valores que condicionan; falta «pérdida de pelo» |
| plaid-punto-101 | ≠ | ≈ | Punto como valor que condiciona; faltan las bolitas |
| cuerda-tootoy | ≠ | ≈ | Cuerda como valor que condiciona; falta «ingestión de fibras» |
| pienso-josera-sea-fish | ≠ | ≠ | Seco «cubierto por la categoría» sin la cuestión del tamaño de la croqueta; añade «perros activos» como requisito condicionado (energía y ración) |
| sofa-cama-luna | ≠ | ≠ | Añade la especialización «almacenamiento integrado» (revistero). La apertura no está declarada: el esperado estaba mal (ver abajo) |

## Lectura

1. **La clase general es robusta.** Los componentes, las piezas de los juegos y los descartes coinciden en todos los casos, incluidos los difíciles (homónimos, duplicados, Juegos de cama).
2. **La etiqueta especialización/valor es la parte inestable, como se esperaba.** Las 7 discrepancias van en la misma dirección: el agente aplica la regla de las cuestiones propias con la base ampliada (D-026 + D-030) y convierte en «valor que condiciona» lo que los casos esperados llaman especialización. En varios casos, la lectura del agente es más fiel a las reglas vigentes que el esperado. Ejemplo: `SOFA` tiene `seat_recline`, `reclining_position_count` y `furniture_wall_clearance`, así que las cuestiones de «reclinable» están en la base. Los esperados de reclinable, piel, polar, punto, seco y cuerda se decidieron antes de D-030 y no se han revisado con ella.
3. **En requisitos, la coincidencia es mucho mayor que en etiquetas.** Las diferencias reales se reducen a dos casos. Las demás son una cuestión de más o de menos, porque generar las cuestiones es abierto.
4. **Un error del esperado.** En el sofá cama Luna, «apertura italiana» solo aparece en el nombre de un icono (`apertura-italiana-facil.svg`); el texto dice «sistema de apertura fácil». El agente aplicó bien «solo lo declarado».

## Dudas que repiten los tres agentes

Hay 80 dudas anotadas en total. Estas aparecen en los tres agentes, así que apuntan a reglas ambiguas y no a errores puntuales:

1. **Cuestiones propias (4.2):** qué significa que «todo producto tiene la dimensión»; con qué granularidad una cuestión «sale de la base» (¿basta un valor de `special_feature`?); y si «cambia la importancia relativa» basta para ser especialización (OQ-41).
2. **Circularidad entre las condiciones 2 y 4:** si la base no tiene la dimensión, el valor trae cuestiones propias pero le falta apoyo y acaba como requisito condicionado; si la tiene, la misma dimensión sirve de base y de apoyo.
3. **Juego:**
   - «Juegos de cama» es una categoría de Shopify (2.6), pero «juego» es especialización (4.3).
   - `bedding-pieces-included` ya está en la base de Fundas de nórdico.
   - La «unidad de venta normal» no está definida.
4. **Base de Amazon:** en un juego, si cuenta el PTD del conjunto, el de las piezas o la unión; qué hacer cuando un PTD no tiene `special_feature` (`BED_LINEN_SET`, `DUVET_COVER`, `FITTED_SHEET`) o lo tiene vacío (`PET_FOOD`); y si cuentan los grupos fuera de `product_details`.
5. **Huecos de la propia clase general:** hay cuestiones que comparte toda la clase pero ninguna referencia recoge, como el mecanismo de apertura y la superficie de descanso de un sofá cama. El reglamento no les da sitio.
6. **Duplicados y clasificación objetiva:** no hay criterio para elegir entre duplicados, y «cuando tiene sentido» no basta para decidir (OQ-43).
7. **Beneficios que son valores de atributos:** «cuidado articular» es un valor de `pet-dietary-requirements` y «cálida», de `warmth-rating`.
8. **Qué cuenta como declarado:** título HTML frente a descripción, iconos y afirmaciones genéricas («todos nuestros productos»).
9. **Variante frente a producto:** cuando el uso se declara para el producto y además para una sola medida.

## Propuestas (pendientes de decisión)

1. **Evaluar y producir en requisitos, no en etiquetas (D-032).** El paso 5 debe listar las cuestiones de toda característica que aporte o condicione, incluida la que cubre la categoría. La comparación se hace sobre cuestiones. Así desaparece la mayor fuente de discrepancia sin perder nada de lo que importa.
2. **Revisar los esperados con las reglas vigentes:** reclinable, piel, polar, punto, seco y cuerda (como se hizo con el Luna en I-14), y corregir la apertura del Luna.
3. **Dar sitio a las cuestiones comunes de la clase que no recogen las referencias.** Hoy se pierden. Es la vía que en el canon cubre el MPIR.
4. **Precisar el reglamento** en los puntos 3, 4, 8 y 9 de las dudas, que son operativos y no cambian el canon.
5. **Herramienta:** un comando `taxo base` que una la base de Shopify y la del PTD (propiedades y `special_feature`) de cada componente o pieza. Reduce trabajo y variación.

## Coste y límites

- Unos 750.000 tokens para 14 casos (unos 53.000 por caso). Cada agente tardó entre 9 y 13 minutos.
- Cada caso se ejecutó una sola vez, así que no se ha medido la variación entre ejecuciones.
- Todos los casos son de desarrollo y salieron de las mismas rondas en que se escribieron las reglas. La prueba sobre casos nuevos de otros sectores está pendiente.
- Como efecto secundario, los agentes anotaron incoherencias de las fichas útiles para la auditoría: la composición del cojín, «agotado» frente a «instock» en el pienso, devoluciones de 14 frente a 45 días, «pelota cuerda» frente a hueso, y la plantilla de sillón en el Stressless.
