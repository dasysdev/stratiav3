---
id: T-109
title: Pistas: revisar los 4 avisos de D-209 (gen/03, gen/04, cat.ropa-de-casa/03)
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

Un revisor decide si cada par de pistas que llega a un requisito por llaves distintas dice lo mismo (D-209), antes de rehacer los modelos del piloto: los 3 requisitos están en sus dos modelos.

## Criterios de aceptación

- [ ] Cada aviso de bin/model hints check (PV-47/PV-24, PV-21/PV-33, PV-20/PV-34, PV-20/PV-35) tiene su decisión y su motivo anotados en la tarea
- [ ] Una pista que repite a otra se retira o se funde según D-209; bin/model hints check termina sin errores
- [ ] Tests en verde

## Notas
