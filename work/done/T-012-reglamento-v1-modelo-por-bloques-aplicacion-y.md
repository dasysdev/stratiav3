---
id: T-012
title: Reglamento v1 (modelo por bloques + aplicación) y segundo experimento
status: hecha
depends:
milestone:
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Reescribir el reglamento para que produzca el modelo de requisitos por bloques, la aplicación y la denominación (D-033 a D-038), con el catálogo de la capa general como datos, y repetir el experimento con dos ejecuciones por caso midiendo en requisitos y estabilidad

## Criterios de aceptación

- [x] Catálogo de la capa general en demand-engine/catalog/ con el formato de D-038
- [x] Reglamento v1 con salida de bloques, aplicación y denominación, sin ejemplos de los casos de prueba
- [x] Casos esperados ampliados al formato v1 y bin/compare capaz de comparar con lo esperado y entre ejecuciones
- [x] Dos ejecuciones por caso de los 14 casos y comparación
- [x] Informe con coincidencia, estabilidad entre ejecuciones y propuestas

## Resultado

Reglamento v1 y segundo experimento: importancia estable (91 %), especializaciones estables pero divergentes, 35 % de cuestiones clave perdidas por el hueco de Amazon; propuestas en demand-engine/runs/2026-10-25-v1-report.md

## Notas

- 2026-10-25 Montado: catalog/gen.json (capa general, 22 requisitos en 8 bloques), taxo gen y category --own, reglamento v1 (rulebook.md; v0 conservado en rulebook-v0.md) sin filtraciones, expected_v1 en los 14 casos, compare con modo v1 y --pair. Lanzadas dos ejecuciones (v1-a, v1-b) × 3 lotes.
- 2026-10-25 Resultado v1: composición 11-12/14; especializaciones 7-8/14 frente a lo esperado pero 13/14 estables entre ejecuciones; cuestiones clave 65 %; aplicación 6/6 y 5/6; importancia estable al 91 %; bloques de sector inestables (4/14). Hueco D-009/D-030/D-036: las cuestiones que solo recoge Amazon se quedan sin sitio. Informe en demand-engine/runs/2026-10-25-v1-report.md con 5 propuestas.
