---
id: T-046
title: Formato de la referencia técnica, validador y skill web-reference
status: hecha
depends: T-044
milestone:
created: 2026-10-27
closed: 2026-10-27
---

## Objetivo

Fijar el formato de la documentación de referencia de web-audit (ficha por fuente con citas literales; requisito técnico con los siete campos del canon, perfil y cita a una versión congelada) y crear el validador y la skill de creación y mantenimiento (añadir fuente, actualizar, validar)

## Criterios de aceptación

- [x] Esquema de la ficha de fuente y del requisito técnico documentados en web-audit/reference/README.md
- [x] web-audit/bin/reqs check valida campos, ids únicos, citas que resuelven a una versión congelada y una condición por requisito, con pruebas
- [x] .claude/skills/web-reference/SKILL.md con las operaciones añadir, actualizar y validar; el canon prevalece y no crea estados, pesos ni fórmulas
- [x] Skill y comandos en el mapa de CLAUDE.md y en el README de web-audit

## Resultado

Formato B de la referencia técnica (fichas por fuente, requisitos por nivel), web-audit/bin/reqs check/section con 7 pruebas y skill /web-reference; mapa y README al día

## Notas

- 2026-10-27 Viene de T-045: web-audit/reference/sources.json es el registro que lee refs (id, kind, title, publisher, url; opcionales inventory y note). Una cita puede nombrar id + versión fijada (var/refs/pins.json) + sección: en HTML, el ancla {#id} de text.md; la cita literal se busca en text.md (o en el fichero, si no es HTML). Lectura: web_audit.refs.pinned(id). Evitar repetir en inventory.md lo que ya está en sources.json.
- 2026-10-27 Formato elegido por el usuario: B («B», 2026-10-27), entre A (ficha y requisitos en un fichero por fuente, recomendada), B (ficha por fuente y requisitos por nivel, citas fuente#qNN) y C (cita en línea en el requisito). Requisito: id ws-<nivel>/NNN, scope, spec, condition, nature, quotes, method, evidence, applicability, not_evaluable, rationale opcional; estados = condition/applicability/not_evaluable. reqs check: campos cerrados, valores del canon, cita literal en la sección de la versión fijada, spec aplicable y de su nivel, término normativo de la naturaleza en una cita de spec, condición de una frase. reqs section para copiar citas. 7 pruebas nuevas (16 en web-audit).
