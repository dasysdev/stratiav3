---
id: T-102
title: Ámbitos Contenido y Marcado en demand-engine e info-audit (D-220)
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

Llevar a demand-engine e info-audit el cambio de nombre de D-220 (Web → Contenido, content; Web Schema.org → Marcado, markup) y la ficha de Contenido sin la localización de Marcado, sin cambiar ningún requisito informativo. web-audit va en T-108.

## Criterios de aceptación

- [x] demand-engine: las fichas de ámbito se llaman content y markup; la de Contenido no incluye la localización de Marcado; bin/model scope escribe CASO.content.json y CASO.markup.json
- [x] info-audit acepta solo los ámbitos Contenido y Marcado: retira la equivalencia con Web y Web Schema.org (records.py, MODEL_SCOPES)
- [x] La skill /demand-model y el README de demand-engine usan los nombres nuevos
- [x] Las pruebas de demand-engine e info-audit pasan con bin/run dev test
- [x] Ningún fichero de demand-engine, info-audit ni .claude/skills/demand-model nombra Web o Web Schema.org como ámbito vigente (grep anotado en la tarea)

## Resultado

Ámbitos content y markup en demand-engine e info-audit; Contenido sin la localización de Marcado; PV-13 → PV-49

## Notas

- 2026-10-30 Partida (saneamiento del piloto): la parte de web-audit, /web-audit, /web-reference y el README de capture pasa a T-108, fuera del milestone. Hoy las 22 unidades con localización de Contenido del piloto apuntan a propiedades Schema.org (ficha web@0.1 con include web-schema-org): D-220 lo retira.
- 2026-10-30 Hecho (agente): fichas content@0.2 (sin localización) y markup@0.2 (solo cambia el nombre); retirado localization.include (sheet_problems lo rechaza); info-audit exige model.scope == record.scope. bin/model scope sobre una copia del edredón: Contenido 66 unidades y 0 con localización; Marcado 66 y 22, igual que web-schema-org. 175 pruebas de demand-engine e info-audit en verde.
- 2026-10-30 Grep: quedaban 3 textos en demand-engine/catalog. Corregidos por mí: la nota de google-search.json y note_references de gen.json (perfil de Marcado) y PV-13, retirada y sustituida por PV-49 sin «en Web, su marcado» (D-220, D-124; D-202). Lo que queda nombra Web solo como nombre antiguo (content.json, markup.json, test_records.py). Las unidades del piloto (var/runs/live/bb-*) siguen en web/web-schema-org hasta T-105.
