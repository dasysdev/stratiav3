---
id: T-098
title: info-audit: fase 1, disponibilidad por ficha × ámbito (D-153)
status: pendiente
depends: T-094, T-096, T-097, T-103, T-105
milestone: piloto-gsc-bb
created: 2026-10-29
---

## Objetivo

Un agente por ficha × ámbito explora la representación completa, decide la pertinencia y la disponibilidad efectiva de todos los RI y deja la prueba de cobertura de cada ausencia (OP-03…07). Piloto: 2 fichas × Contenido y Marcado.

## Criterios de aceptación

- [ ] Hay un reglamento de la fase 1 en info-audit, con cada regla citando su módulo de audit-gsc o su decisión
- [ ] Las 4 salidas (2 fichas × 2 ámbitos) pasan bin/audit validate
- [ ] Cada RI tiene disponibilidad 0, 1 o comprobación inconclusa; cada 0 tiene su registro de cobertura; los RI con 0 cierran con IR = 0
- [ ] Los agentes de Marcado solo usan el marcado y los de Contenido, solo la salida del filtro Alfa (audit-es + alfa/1), nunca el HTML entero (D-220, D-223)
- [ ] La tarea anota por ficha y ámbito el recuento de 0, 1 e inconclusas y los tokens de cada agente

## Notas

- 2026-10-30 Decisión del usuario (2026-10-30): el piloto no usa el expediente de web-audit. La fase 1 no cita causas técnicas de un 0 ni depende de /web-audit.
- 2026-10-30 Entrada (T-094): sin auditoría de capture ni audit.json. Las 2 fichas audit-es están en capture/var/pages/: audit-bb-edredon-6172 y audit-bb-barbie-5611.
- 2026-10-30 Entrada (T-097): los registros siguen info-audit/schemas/availability.v1.json y se validan con info-audit/bin/audit validate. La representación de Marcado es markup/1 (reader, version, ficha, blocks[].text, ver info-audit/README): su lector falta y es parte de esta tarea.
- 2026-10-30 Riesgo (saneamiento): solo 5 de 1594 requisitos del catálogo tienen descripción. En el piloto, 47 de 51 (Barbie) y 62 de 66 (edredón) unidades llegan con objeto, alcance y casos_frontera vacíos (pendientes_de_definicion). D-177: el auditor no los completa. Anotar en cada decisión de pertinencia si la falta de perfil pesó; lo mide T-100.
