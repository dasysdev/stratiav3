---
id: T-098
title: info-audit: fase 1, disponibilidad por ficha × ámbito (D-153)
status: pendiente
depends: T-094, T-096, T-097
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

Un agente por ficha × ámbito explora la representación completa, decide la pertinencia y la disponibilidad efectiva de todos los RI y deja la prueba de cobertura de cada ausencia (OP-03…07). Piloto: 2 fichas × Web y Web Schema.org.

## Criterios de aceptación

- [ ] Hay un reglamento de la fase 1 en info-audit, con cada regla citando su módulo de audit-gsc o su decisión
- [ ] Las 4 salidas (2 fichas × 2 ámbitos) pasan bin/audit validate
- [ ] Cada RI tiene disponibilidad 0, 1 o comprobación inconclusa; cada 0 tiene su registro de cobertura; los RI con 0 cierran con IR = 0
- [ ] Los agentes de Web Schema.org solo usan el marcado y los de Web, HTML + Schema.org, sobre la respuesta audit-es (D-156)
- [ ] La tarea anota por ficha y ámbito el recuento de 0, 1 e inconclusas y los tokens de cada agente

## Notas
