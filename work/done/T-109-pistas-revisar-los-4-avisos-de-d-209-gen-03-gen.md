---
id: T-109
title: Pistas: revisar los 4 avisos de D-209 (gen/03, gen/04, cat.ropa-de-casa/03)
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

Un revisor decide si cada par de pistas que llega a un requisito por llaves distintas dice lo mismo (D-209), antes de rehacer los modelos del piloto: los 3 requisitos están en sus dos modelos.

## Criterios de aceptación

- [x] Cada aviso de bin/model hints check (PV-47/PV-24, PV-21/PV-33, PV-20/PV-34, PV-20/PV-35) tiene su decisión y su motivo anotados en la tarea
- [x] Una pista que repite a otra se retira o se funde según D-209; bin/model hints check termina sin errores
- [x] Tests en verde

## Resultado

Avisos D-209 revisados: PV-24 y PV-47 fundidas en PV-48; los otros 3 pares no son duplicados y su aviso queda

## Notas

- 2026-10-30 cat.ropa-de-casa/03, PV-47 y PV-24 (P09, Precisión): dicen lo mismo (la norma concreta, no solo el sello). Retiradas las dos (D-202: un modelo ya las usó) y fundidas en PV-48, que añade la clase o el nivel y llega a los mismos 10 requisitos que PV-47. hints.json 0.3 → 0.4.
- 2026-10-30 gen/03, PV-21 y PV-33 (P11): no dicen lo mismo. PV-21: el modelo o el lote, no solo la gama (GPSR); PV-33: un GTIN por variante. El aviso queda.
- 2026-10-30 gen/04, PV-20 y PV-34 (P09): no dicen lo mismo. PV-20: si el importe incluye impuestos y gastos; PV-34: un único importe vigente con moneda. El aviso queda.
- 2026-10-30 gen/04, PV-20 y PV-35 (P12): no dicen lo mismo. PV-20: qué incluye el importe; PV-35: comparar el total de lo mismo (piezas, medida). El aviso queda; el código no tiene forma de silenciarlo.
- 2026-10-30 Fuera de la tarea: docs/10-model/assessment-hints.md:137 sigue nombrando PV-47 como nueva (pasa al /docs-update del saneamiento). hints check: 0 errores; test_hints.py: 15 en verde.
