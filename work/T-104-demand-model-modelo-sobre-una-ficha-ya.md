---
id: T-104
title: demand-model: modelo sobre una ficha ya capturada (--page ID)
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

/demand-model acepta el page-ID de una ficha ya congelada en capture/var/pages/ (de cualquier perfil, también audit-es) y clasifica sobre ella sin capturar de nuevo. El modelo de demanda y la auditoría usan así la misma ficha por construcción.

## Criterios de aceptación

- [ ] Con --page ID, la skill no ejecuta page fetch y el clasificador lee ../capture/var/pages/ID.html
- [ ] Si el page-ID no existe, la skill lo dice y para; no captura en su lugar
- [ ] El modelo ensamblado registra el page-ID y el perfil de captura de la ficha usada
- [ ] SKILL.md y demand-engine/README describen la opción; sin --page, el comportamiento no cambia

## Notas

- 2026-10-30 Entra en el milestone (saneamiento): tras la pasada PAA de T-107, T-105 rehace los 2 modelos del piloto con --page sobre las fichas audit-es (audit-bb-edredon-6172, audit-bb-barbie-5611), la misma ficha que audita info-audit, y con el clasificador sobre el catálogo nuevo.
