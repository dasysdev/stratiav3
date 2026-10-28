---
id: T-045
title: Sistema web-audit y congelación de fuentes de referencia
status: hecha
depends:
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Crear web-audit como sistema de primer nivel y miembro del workspace de uv, con bin/refs para congelar por versión las fuentes oficiales del inventario de Schema.org (páginas y vocabulario 30.1 en formato máquina), siguiendo el patrón de demand-engine/var/refs

## Criterios de aceptación

- [x] web-audit/ con pyproject, README (estructura y qué entra en git) y fila en el mapa de CLAUDE.md
- [x] web-audit/bin/refs con status, check, fetch, diff y pin; MANIFEST con origen, sha256 y fecha; versión fijada en pins.json
- [x] Fuentes oficiales del inventario y vocabulario Schema.org 30.1 congelados en web-audit/var/refs/
- [x] Pruebas de refs pasando con bin/run dev test

## Resultado

web-audit creado (workspace, imagen); bin/refs con status/check/fetch/diff/pin; Schema.org 30.1 y 23 documentos oficiales del inventario congelados en web-audit/var/refs; 9 pruebas

## Notas

- 2026-10-27 Hecho: web-audit (miembro del workspace, imagen reconstruida, uv.lock regenerado); refs autónomo (solo stdlib) con el mismo patrón que demand-engine/refs, sin código compartido entre sistemas. Fuentes: 'schemaorg' (release 30.1 de GitHub, sha de git) y 'document' (versión = fecha; HTML guardado + text.md, que es lo que cuenta para versionar porque el HTML de Google cambia en cada petición). 24 fuentes: vocabulario + 23 oficiales del inventario; fuera, VAL-01/02 (aplicaciones) y SKL-* (D-132). Google en inglés (original), no hl=es. GS1-01 = gs1Voc.jsonld (la página es una app JS).
