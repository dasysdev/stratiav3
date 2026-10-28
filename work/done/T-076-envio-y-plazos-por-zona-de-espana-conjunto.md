---
id: T-076
title: Envío y plazos por zona de España: conjunto explícito y AC
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Incorporar al canon y a la capa general (gen.json) el tratamiento de las zonas de envío de España (Península, Baleares, Canarias, Ceuta y Melilla) como unidades de un conjunto valoradas por los AC, con el requisito de impuestos y aduana condicionado.

## Criterios de aceptación

- [x] Decisiones registradas en decisions.md y canon actualizado; check_docs con 0 errores
- [x] gen.json v0.9 con gen/25 y gen/08 reformulados y el bloque condicionado de impuestos y aduana; bin/model check sin errores
- [x] Normas de apoyo del requisito de impuestos registradas en references o pendiente registrado
- [x] Ficha de Web Schema.org y rules/resolving.json coherentes con las nuevas aportaciones

## Resultado

Zonas de envío de España como conjunto valorado por los AC (D-164, D-165): gen/25 y gen/08 reformulados, bloque gen.envio-canarias-ceuta-melilla, gen.json 0.9, tres normas en references

## Notas

- 2026-10-28 rules/resolving.json no se edita a mano: es la compilación del entrenamiento (2026-10-26); sus never_observed de gen/25 y gen/08 llevan los nombres antiguos y se regeneran en el próximo entrenamiento. Pistas nuevas PV-42 (gen/25, Aplicabilidad), PV-43 (P08) y PV-44 (P09) (gen/08, Precisión). model.py pasa la descripción (D-092) al modelo ensamblado. Reglamento del clasificador: disparador de gen.envio-canarias-ceuta-melilla en paso 0 y paso 6.
