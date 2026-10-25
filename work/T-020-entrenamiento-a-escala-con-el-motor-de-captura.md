---
id: T-020
title: Entrenamiento a escala con el motor de captura compartido
status: pendiente
depends: T-019
milestone: codigo
created: 2026-10-25
---

## Objetivo

Entrenar el modelo de demanda con un catálogo de miles de fichas de tipos distintos capturadas con el motor de captura compartido (D-046): selección de tiendas y fichas, módulo de captura común fuera de mpir/, ejecución por lotes con la API y ciclo de entrenamiento completo

## Criterios de aceptación

- [ ] Módulo de captura común en src/demand_engine/ usado por el MPIR y por el entrenamiento, coordinado con T-014 y T-015
- [ ] Criterio de selección del catálogo de entrenamiento documentado (tiendas, tipos, fichas; sin Amazon.es)
- [ ] Clasificación por lotes con la API y ciclo de entrenamiento completo sobre el catálogo, con informe agregado

## Notas

- 2026-10-25 Desde T-018, taxo page fetch es demand_engine.pages.fetch: descarga simple con urllib y user-agent de Chrome. T-019 vio que burritoblanco.com devuelve un desafío de Cloudflare a esa descarga; candidato a pasar por el motor de captura común.
- 2026-10-25 T-021 creó el módulo común src/demand_engine/capture/: el criterio 1 queda a falta de que el entrenamiento lo use (crawl con SiteRun para lotes; once para fichas sueltas). Ver su README.
