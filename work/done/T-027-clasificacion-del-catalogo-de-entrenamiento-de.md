---
id: T-027
title: Clasificación del catálogo de entrenamiento de ECI (dos ejecuciones)
status: hecha
depends: T-026
milestone: codigo
created: 2026-10-25
closed: 2026-10-26
---

## Objetivo

Clasificar y ensamblar con agentes de Claude Code (procedimiento de T-026) las 30 fichas del piloto capturadas en T-025, en dos ejecuciones para medir la estabilidad

## Criterios de aceptación

- [x] Ejecuciones var/runs/FECHA-eci-a y -b con todas las fichas capturadas, comprobadas (bin/model check) y ensambladas (bin/model assemble)
- [x] Bloques de las clases nuevas generados con estado no compilado y var/queue.jsonl al día
- [x] Recuento de clases y verticales de Shopify cubiertos por las fichas
- [x] Consumo de tokens de cada ejecución registrado

## Resultado

ECI piloto clasificado dos veces (eci-a, eci-b): 60/60 ensamblados, 15 clases en 8 verticales, 32 bloques generados, 55,6 M tokens; clave estable 28/30

## Notas

- 2026-10-26 Ejecuciones var/runs/2026-10-25-eci-a y -b (skill classify-batch): 30/30 comprobadas y ensambladas en cada una, sin reintentos. A: 33,17 M tokens (1,11 M por caso; fase 1 15,48 M con generación de bloques, fase 2 17,69 M), 434.654 de salida, 85 min de agente. B: 22,48 M (0,75 M por caso; fase 1 7,15 M, fase 2 15,32 M), sin bloques que generar. Total del ciclo: 55,6 M. Caso sin bloques: 0,45–0,9 M; caso que redacta bloques: 1,2–3,2 M.
- 2026-10-26 Catálogo: 32 bloques de categoría en catalog/runtime (no compilados; 7 de la prueba de T-026) y 5 categorías vacías de ejecución (ha-15, aa-8-11, vp, vp-1-5-5, bt). La guardia de register actuó 3 veces en A (cocina-y-comedor, maletas-y-bolsos-de-viaje, lijadoras + lijadoras-orbitales) sin duplicados. var/queue.jsonl al día (92 entradas).
- 2026-10-26 Cobertura: 15 clases de Shopify (14 hojas + porta chupete en un juego) en 8 verticales (aa, bt, fb, ha, hg, lb, me, vp): aceite de motor (2 clases), bloques de lija, lijadoras orbitales, bolsas de viaje, botellas de agua, CD, LP, confituras, joyas para piercings, mochilas escolares, mochilas para portátil, soperas, zapatillas infantiles, clips para chupetes. El tipo de la selección no es la clase: música (CD/LP), lijadora (bloque/orbital), mochila (escolar/portátil/juego) y aceite (sintético/genérico) se parten. Huecos de cobertura: A 10/539, B 8/527.
- 2026-10-26 Estabilidad A/B: misma composición 30/30; misma clave 28/30 y misma oferta 29/30. Divergencias: lijadoras a batería con especialización de nombre distinto (esp.a-bateria en A, esp.bateria en B) y la Einhell sin especialización en A y con ella en B; mochila Totto Tempera con gen.variantes solo en B («varias tonalidades» con un solo color seleccionable). Dudas recurrentes para T-028: vinilo me-3-4 frente a me-3-6; texto de plantilla de ECI («No incluye adaptador», «DVD Zona») y pestañas vacías en la primera carga (devoluciones, seguridad); descuento por cantidad sin precio tachado; críticos dispares en medidas (capacidad de sopera principal/crítica, viscosidad); base del aceite como inferida o como material; especializaciones sin campo de nivel (batería, compartimento portátil, luces).
