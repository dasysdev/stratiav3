---
id: T-104
title: demand-model: modelo sobre una ficha ya capturada (--page ID)
status: hecha
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

/demand-model acepta el page-ID de una ficha ya congelada en capture/var/pages/ (de cualquier perfil, también audit-es) y clasifica sobre ella sin capturar de nuevo. El modelo de demanda y la auditoría usan así la misma ficha por construcción.

## Criterios de aceptación

- [x] Con --page ID, la skill no ejecuta page fetch y el clasificador lee ../capture/var/pages/ID.html
- [x] Si el page-ID no existe, la skill lo dice y para; no captura en su lugar
- [x] El modelo ensamblado registra el page-ID y el perfil de captura de la ficha usada
- [x] SKILL.md y demand-engine/README describen la opción; sin --page, el comportamiento no cambia

## Resultado

/demand-model --page ID clasifica sobre una ficha congelada; el modelo registra la ficha y su perfil de captura

## Notas

- 2026-10-30 Entra en el milestone (saneamiento): tras la pasada PAA de T-107, T-105 rehace los 2 modelos del piloto con --page sobre las fichas audit-es (audit-bb-edredon-6172, audit-bb-barbie-5611), la misma ficha que audita info-audit, y con el clasificador sobre el catálogo nuevo.
- 2026-10-30 Hecho (agente): con --page ID la skill no captura; el caso se llama como la ficha (taxo page facts lee por el ID del caso), así que en T-105 los casos son audit-bb-edredon-6172 y audit-bb-barbie-5611. Si falta ID.html o ID.json, para. Si var/runs/live/ID.json ya existe, para salvo que se pida rehacerlo.
- 2026-10-30 El modelo lleva page {id, profile} (ficha sin perfil = reader; sin ficha = null) y la línea «Ficha» en el .md. Corregido por mí: model.py lee el almacén con capture.pages (bin/model añade capture/src, como taxo). 98 pruebas de demand-engine/tests/demand en verde; CLAUDE.md nombra --page.
