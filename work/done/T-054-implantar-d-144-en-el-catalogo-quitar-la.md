---
id: T-054
title: Implantar D-144 en el catálogo: quitar la aportación de imagen de gen/24
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Aplicar D-144 al catálogo de demanda: la imagen deja de ser aportación resolutiva de gen/24 (es sostén del mínimo de representación). Afecta a demand-engine/catalog/gen.json (capa general) y a demand-engine/catalog/rules/resolving.json, que también la lista en gen/24

## Criterios de aceptación

- [x] gen.json sin la aportación «imagen que permite identificar el producto» en gen/24 y con la versión de la capa general subida (0.6 → 0.7)
- [x] rules/resolving.json sin esa aportación en gen/24, regenerado o editado según el procedimiento del motor
- [x] Pruebas de demand-engine en verde (bin/run dev test demand-engine/tests)
- [x] Nota en la tarea con lo cambiado y el comando de compilación usado, si lo hubo

## Resultado

D-144 en el catálogo: aportación de imagen fuera de gen/24 en gen.json (capa general 0.7) y en rules/resolving.json; 105 pruebas en verde

## Notas

- 2026-10-28 gen.json: quitada la aportación «imagen que permite identificar el producto» de gen/24 (queda «tipo o modelo del producto»), versión de la capa general y del bloque gen 0.6 → 0.7 y D-144 en decisions. rules/resolving.json editado a mano (solo la entrada de never_observed de gen/24): regenerarlo exige bin/train compile sobre las ejecuciones y recompilaría todo el catálogo. Sin compilación. bin/model check --catalog y bin/model refs solo dan el problema previo de cat.confituras-y-gelatinas/02 (T-064); 105 pruebas de demand-engine en verde.
