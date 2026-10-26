---
id: T-020
title: Entrenamiento a escala con el motor de captura compartido
status: bloqueada
depends: T-019
milestone: codigo
reason: Dividida en T-024…T-029 (piloto de 30, después escalado); se cierra con T-029
created: 2026-10-25
---

## Objetivo

Entrenar el modelo de demanda con un catálogo de miles de fichas de tipos distintos capturadas con el motor de captura compartido (D-046): selección de tiendas y fichas, módulo de captura común fuera de mpir/, clasificación por lotes con agentes de Claude Code y ciclo de entrenamiento completo

## Criterios de aceptación

- [x] Módulo de captura común en src/demand_engine/ usado por el MPIR y por el entrenamiento, coordinado con T-014 y T-015
- [ ] Criterio de selección del catálogo de entrenamiento documentado (tiendas, tipos, fichas; sin Amazon.es)
- [ ] Clasificación por lotes con agentes de Claude Code y ciclo de entrenamiento completo sobre el catálogo, con informe agregado

## Notas

- 2026-10-25 Desde T-018, taxo page fetch es demand_engine.pages.fetch: descarga simple con urllib y user-agent de Chrome. T-019 vio que burritoblanco.com devuelve un desafío de Cloudflare a esa descarga; candidato a pasar por el motor de captura común.
- 2026-10-25 T-021 creó el módulo común src/demand_engine/capture/: el criterio 1 queda a falta de que el entrenamiento lo use (crawl con SiteRun para lotes; once para fichas sueltas). Ver su README.
- 2026-10-25 Dividida en subtareas en cadena: T-024 selección ECI (300 fichas, 3 por categoría) → T-025 captura por lotes (tope 300/día para ECI) → T-026 clasificador por la API → T-027 clasificación (dos ejecuciones) → T-028 ciclo de entrenamiento e informe; T-028 cierra T-020
- 2026-10-25 El usuario pide validar primero con un piloto de 30 fichas (T-024 a T-028); el escalado a 300 y el cierre de T-020 pasan a T-029
- 2026-10-25 Decisión del usuario (2026-10-25): «para clasificar usamos claude code»; T-026 pasa a clasificación por lotes con agentes de Claude Code; D-045 se enmienda con /docs-update
