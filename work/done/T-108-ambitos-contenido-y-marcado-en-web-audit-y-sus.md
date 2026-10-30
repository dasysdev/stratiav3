---
id: T-108
title: Ámbitos Contenido y Marcado en web-audit y sus skills (D-220)
status: hecha
depends:
milestone:
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

Llevar a web-audit el cambio de nombre de D-220 (Web → Contenido; Web Schema.org → Marcado) sin cambiar ningún requisito técnico. Sale de T-102: el piloto GSC no usa web-audit.

## Criterios de aceptación

- [x] La referencia técnica, el auditado y el expediente de web-audit nombran los ámbitos Contenido y Marcado; reqs check pasa
- [x] Las skills /web-audit y /web-reference y los README de web-audit y capture usan los nombres nuevos
- [x] Las pruebas de web-audit pasan con bin/run dev test
- [x] Ningún fichero fuera de docs/archive, docs/30-governance y research_notes nombra Web o Web Schema.org como ámbito vigente (grep anotado en la tarea)

## Resultado

web-audit, sus skills, capture, references y CLAUDE.md nombran los ámbitos Contenido y Marcado

## Notas

- 2026-10-30 Hecho (agente): 80 ficheros, ninguno renombrado. scope «Contenido»/«Marcado» en requisitos, retired.json y fichas; ids, citas literales, spec, nature, view, page_types y reason iguales (comprobado contra HEAD; en google-search-sitemaps-build solo cambia la nota de q05). reqs check: Marcado 323, Contenido 33; 112 pruebas de web-audit y capture en verde; model check --catalog correcto.
- 2026-10-30 Se quedan los nombres de fichero y módulo (web-protocol/document/consumer.json, checks/web.py, prefijos w-/ws-), con una línea «Nombres» en el README. Los informes fechados de reference/reports llevan una nota y conservan su texto. Los expedientes de web-audit/var/audits tienen cases.json con los nombres antiguos: para rehacerlos, audit run antes de finish.
- 2026-10-30 Grep (136 líneas, scratchpad grep-criterion4-classified.txt): solo otros sentidos de Web (on the Web, Claude-Web, GS1 Web Vocabulary), nombres antiguos dichos como tales, citas literales, informes fechados y work/. Corregidos por mí fuera de su alcance: capture/src/capture/profiles.py y 21 notas de references/sources.json. Queda reports/Perfil de consumo de agentes IA.md, informe fechado.
