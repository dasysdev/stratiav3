---
id: T-036
title: Resolver I-36 a I-39 y desacoplar la aplicación esperada de los casos de control
status: hecha
depends:
milestone:
created: 2026-10-26
closed: 2026-10-26
---

## Objetivo

Aplicar las recomendaciones de I-36 a I-39 (decisión del usuario del 2026-10-26) en el canon, el reglamento, DRAFTING, el catálogo y el código, y quitar de cases/ la aplicación esperada (la estabilidad A/B la mide sin mantenimiento)

## Criterios de aceptación

- [x] Decisiones registradas e I-36 a I-39 resueltas; módulos y changelog al día; check_docs sin errores
- [x] Catálogo: los requisitos de I-37 revisados y las aportaciones de I-39 en gen.json; bin/model check --catalog correcto
- [x] Reglamento, DRAFTING y código con I-36 a I-38; cases/ sin aplicación esperada; bin/run dev test en verde

## Resultado

I-36 a I-39 resueltas (D-086 a D-089): alcance de juego, regla 3 sobre sí o no, propuestas al bloque en el código, precio anterior y unitario en la capa general; cases/ sin aplicación esperada

## Notas

- 2026-10-26 D-086 (juego: piezas y cuántas; medidas en los bloques de cada pieza), D-087 (regla 3 prevalece: cat.sofas-cama/02 → /02, /18, /19; cat.juguetes-para-perros/06 → /06, /16; cat.cojines-decorativos/01 → /01, /14 por magnitud; cat.mantas/05 sin cambio: peso y grosor son magnitud), D-088 (propuestas al bloque: model check las comprueba, train compile las incorpora con id nuevo, el informe lista las pendientes; 2 pruebas nuevas) y D-089 (Ley 7/1996 art. 20.1 y RD 3423/2000 art. 3.2, verificados en el BOE, en gen.descuento/01 y gen/04). Índice de rasgos reconstruido (bin/train index sin ejecuciones: solo cambian 4 fuentes). cases/: sin aplicación esperada (14). Revisión independiente con docs-reviewer (Sonnet): 3 retoques menores aplicados. Catálogo 444 requisitos; 92 pruebas en verde.
