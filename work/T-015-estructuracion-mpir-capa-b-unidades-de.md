---
id: T-015
title: Estructuración MPIR (capa B): unidades de contenido con localizador
status: bloqueada
depends: T-013
milestone: codigo
reason: Aparcada por D-095 (MPIR aparcado); retomarlo es una decisión nueva
created: 2026-10-25
---

## Objetivo

Segmentar las instantáneas en unidades de contenido (encabezado y contenido, FAQ, tablas, filtros, JSON-LD) con localizador y visibilidad, reprocesables sin red

## Criterios de aceptación

- [ ] Unidades con localizador, tipo, visibilidad y procedencia, enlazadas a la instantánea
- [ ] Reprocesar un corpus no hace peticiones de red
- [ ] Probada con capturas reales de ropa de cama

## Notas

- 2026-10-25 Desde T-021 la raíz de cada bloque oculto lleva data-capture-hidden="1" (antes data-mpir-hidden; la instantánea de prueba-humo conserva el nombre antiguo). Formato de la instantánea: README de src/demand_engine/capture/.
