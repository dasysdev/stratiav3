---
id: T-054
title: Implantar D-144 en el catálogo: quitar la aportación de imagen de gen/24
status: pendiente
depends:
milestone:
created: 2026-10-28
---

## Objetivo

Aplicar D-144 al catálogo de demanda: la imagen deja de ser aportación resolutiva de gen/24 (es sostén del mínimo de representación). Afecta a demand-engine/catalog/gen.json (capa general) y a demand-engine/catalog/rules/resolving.json, que también la lista en gen/24

## Criterios de aceptación

- [ ] gen.json sin la aportación «imagen que permite identificar el producto» en gen/24 y con la versión de la capa general subida (0.6 → 0.7)
- [ ] rules/resolving.json sin esa aportación en gen/24, regenerado o editado según el procedimiento del motor
- [ ] Pruebas de demand-engine en verde (bin/run dev test demand-engine/tests)
- [ ] Nota en la tarea con lo cambiado y el comando de compilación usado, si lo hubo

## Notas
