---
id: T-110
title: PAA: fundir los duplicados entre conjuntos en la pasada al catálogo
status: pendiente
depends:
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

Que la pasada de PAA no meta dos requisitos para el mismo hecho cuando dos conjuntos lo proponen. Decisión del usuario (2026-10-30): compile avisa de los posibles duplicados, un revisor decide si son el mismo hecho y se funden en un requisito con las fuentes de todos. Caso real: mantas y sábanas metieron cat.ropa-de-casa/07 y /08 (variedad de la fibra).

## Criterios de aceptación

- [ ] bin/paa compile lista los posibles duplicados: candidatos de conjuntos distintos con el mismo rasgo en el mismo bloque o en un bloque y su antepasado
- [ ] bin/paa compile no escribe nada si un posible duplicado no tiene decisión, y lo dice
- [ ] Las decisiones del revisor quedan en training/reports/paa/ con su motivo; un grupo fundido entra como un solo requisito, en el bloque más alto, con las fuentes de todos
- [ ] La pasada se compila de nuevo sin duplicados: model check --catalog, hints check y refs sin errores; la tarea anota los grupos y su decisión
- [ ] El canon recoge la regla con /docs-update
- [ ] Tests en verde

## Notas
