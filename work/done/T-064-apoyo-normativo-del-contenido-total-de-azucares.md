---
id: T-064
title: Apoyo normativo del contenido total de azúcares en confituras tras el RD 1026/2025
status: hecha
depends: T-062
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

El RD 1026/2025 (BOE-A-2025-22947, en vigor el 14-06-2026) suprimió el apartado 8.4 de la norma de calidad del RD 863/2003: la indicación del contenido total de azúcares ya no es obligatoria. cat.confituras-y-gelatinas/02 conserva la aportación «contenido total de azúcares por cada 100 g» de origen «referencias» con apoyo ley:ES-RD-863/2003@2003-07-04 (texto anterior), y su rationale dice que la norma obliga a indicarlo. Corregir la aportación y el rationale; el contenido de fruta (8.3) sigue igual.

## Criterios de aceptación

- [x] La aportación de azúcares totales ya no se apoya en el RD 863/2003 (pasa a «inferida» o se retira, con el motivo en una nota) y el rationale de cat.confituras-y-gelatinas/02 no afirma la obligación suprimida
- [x] demand-engine/bin/model refs sale con 0 errores y bin/model check --catalog sin problemas
- [x] Pruebas en verde (bin/run dev test)

## Resultado

Azúcares totales retirados de cat.confituras-y-gelatinas/02 (8.4 suprimido; los cubre cat.alimentos/04); model refs y check --catalog limpios, pruebas en verde

## Notas

- 2026-10-28 Se retira el componente de azúcares de cat.confituras-y-gelatinas/02 (pregunta, dimensión, rationale y sus dos aportaciones): con el 8.4 suprimido por el RD 1026/2025 se queda sin fuente (DRAFTING, regla 4) y los azúcares ya los pide cat.alimentos/04 (UE-1169/2011-9.1.l). El requisito queda solo con el contenido de fruta (8.3). catalog/rules/resolving.json conserva las dos aportaciones en never_observed hasta la siguiente compilación (es resultado compilado y solo lo usan los informes). En la suite completa falló una vez paa/test_e2e.py::test_run_set (captured 0 ≠ 3), ajeno al cambio; aislado pasa.
