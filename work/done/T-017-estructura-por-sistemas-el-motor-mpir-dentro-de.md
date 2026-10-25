---
id: T-017
title: Estructura por sistemas: el motor MPIR dentro de demand-engine
status: hecha
depends:
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Cada sistema es un directorio de primer nivel; demand-engine encapsula taxo, el clasificador y el motor de captura del MPIR. Workspace de uv con un miembro por sistema y un solo lock

## Criterios de aceptación

- [x] mpir/ movido a demand-engine/src/demand_engine/mpir/, sus pruebas a demand-engine/tests/mpir/ y su corpus a demand-engine/var/mpir/
- [x] pyproject raíz como workspace de uv con demand-engine como miembro; imagen reconstruida
- [x] Pruebas en verde y demand-engine/bin/mpir status funciona con el corpus movido; taxo sigue funcionando en el host
- [x] CLAUDE.md, README de demand-engine y enlaces de docs actualizados; check_docs sin errores

## Resultado

Motor MPIR dentro de demand-engine (src/demand_engine/mpir, tests/mpir, var/mpir); workspace de uv con un miembro por sistema; 29 pruebas en verde; README de demand-engine, CLAUDE.md y enlaces de docs al día

## Notas

- 2026-10-25 Decisión del usuario: sin nivel systems/; cada sistema es un directorio de primer nivel. bin/run sustituye «mpir» por «exec» genérico. PYTHONPATH de la imagen: /work/demand-engine/src (se amplía con cada sistema). Las herramientas de la biblioteca estándar (refs, taxo, blocks, catalog-review, compare) siguen en el host; no se han tocado.
