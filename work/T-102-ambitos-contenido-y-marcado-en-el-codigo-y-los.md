---
id: T-102
title: Ámbitos Contenido y Marcado en el código y los datos (D-220)
status: pendiente
depends:
milestone:
created: 2026-10-30
---

## Objetivo

Llevar a los sistemas el cambio de nombre de D-220 (Web → Contenido, content; Web Schema.org → Marcado, markup) y la ficha de Contenido sin la localización de Marcado, sin cambiar ningún requisito técnico ni informativo.

## Criterios de aceptación

- [ ] demand-engine: las fichas de ámbito se llaman content y markup; la de Contenido no incluye la localización de Marcado; bin/model scope escribe CASO.content.json y CASO.markup.json
- [ ] web-audit: la referencia técnica, el auditado y el expediente nombran los ámbitos Contenido y Marcado; reqs check pasa
- [ ] Las skills (/demand-model, /web-audit, /web-reference) y los README de demand-engine, web-audit y capture usan los nombres nuevos
- [ ] Las pruebas de demand-engine y web-audit pasan con bin/run dev test
- [ ] Ningún fichero fuera de docs/archive, docs/30-governance y research_notes nombra Web o Web Schema.org como ámbito vigente (grep anotado en la tarea)

## Notas
