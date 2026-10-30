---
id: T-102
title: Ámbitos Contenido y Marcado en demand-engine e info-audit (D-220)
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

Llevar a demand-engine e info-audit el cambio de nombre de D-220 (Web → Contenido, content; Web Schema.org → Marcado, markup) y la ficha de Contenido sin la localización de Marcado, sin cambiar ningún requisito informativo. web-audit va en T-108.

## Criterios de aceptación

- [ ] demand-engine: las fichas de ámbito se llaman content y markup; la de Contenido no incluye la localización de Marcado; bin/model scope escribe CASO.content.json y CASO.markup.json
- [ ] info-audit acepta solo los ámbitos Contenido y Marcado: retira la equivalencia con Web y Web Schema.org (records.py, MODEL_SCOPES)
- [ ] La skill /demand-model y el README de demand-engine usan los nombres nuevos
- [ ] Las pruebas de demand-engine e info-audit pasan con bin/run dev test
- [ ] Ningún fichero de demand-engine, info-audit ni .claude/skills/demand-model nombra Web o Web Schema.org como ámbito vigente (grep anotado en la tarea)

## Notas

- 2026-10-30 Partida (saneamiento del piloto): la parte de web-audit, /web-audit, /web-reference y el README de capture pasa a T-108, fuera del milestone. Hoy las 22 unidades con localización de Contenido del piloto apuntan a propiedades Schema.org (ficha web@0.1 con include web-schema-org): D-220 lo retira.
