---
id: T-055
title: Retirar de la referencia técnica de web-audit los requisitos que salen de la evaluación técnica
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Aplicar a web-audit/reference/requirements las decisiones del triaje del 2026-10-28 (26 no se auditan) y de la frontera general entre evaluaciones (126 de presencia recomendada pasan a la evaluación informativa, salvo los datos que OQ-74 incluya en el mínimo de representación). Los retirados se conservan en un registro con su motivo, porque los de presencia recomendada son la entrada de la tarea del motor de demanda. Esperar a que OQ-74 esté decidida.

## Criterios de aceptación

- [x] Los 26 descartados y los de presencia recomendada están fuera de requirements/, sin reutilizar sus ids
- [x] Registro de retirados en web-audit/reference/ con id, condición, especificación, naturaleza y motivo (no se audita / pasa al modelo de demanda), con el formato documentado en reference/README.md
- [x] Los recomendados que sirven para interpretar un valor ya publicado (bestRating, worstRating, unitCode del peso, URL del logo) siguen en requirements/
- [x] web-audit/bin/reqs check correcto y pruebas de web-audit en verde

## Resultado

Retirados 118 requisitos a reference/retired.json (registro y contrato para T-056), validador y pruebas, README, skill e inventario; hueco del @id registrado

## Notas

- 2026-10-28 D-145: además de retirar, ajustar la skill /web-reference (.claude/skills/web-reference/SKILL.md, paso 5) y web-audit/reference/README.md para que una pasada nueva no escriba requisitos de presencia recomendada: del consumidor solo se escriben lo exigido y la forma de lo que se publica, más los recomendados que sirven para interpretar un valor publicado. Los recomendados del mínimo de representación, según OQ-74.
- 2026-10-28 Desbloqueada por D-147 y D-148 (OQ-74 cerrada). Se quedan en requirements/ los 9 recomendados del mínimo: ws-consumer/032, 034, 042, 066, 153, 192, 202, 205, 339. Se quedan también las partes de formación estructural (D-148): las exigidas dentro de una estructura publicada, las que sirven para interpretar un valor (unidad, escala bestRating/worstRating, sistema y grupo de tallas, moneda del precio unitario, inCodeSet, valueReference…) y las reglas de coherencia («Ningún… tiene…», una sola moneda). Salen a registro las de presencia recomendada que solo añaden otro hecho. Registrar el hueco del @id (mínimo sin requisito).
- 2026-10-28 Reorganización de referencias (T-059 a T-061): T-056 leerá las propiedades y su versión de references, pero sigue necesitando de esta tarea qué recomendados quedan en la técnica (mínimo y formación estructural). Documentar el registro de retirados pensando en que puede ser el contrato que lea T-056 (decisión de OQ-76). Si T-060 se hace antes, sources.json ya no estará en web-audit/reference/.
- 2026-10-28 Retirados 118 (26 triaje, 92 al modelo de demanda) a web-audit/reference/retired.json; quedan 322. Criterio y casos dudosos en reference/reports/2026-10-28-retirada.md. Para revisión del usuario: 173 (misma condición que 146, que el triaje sacó) sigue dentro; 077/078/082/253 se quedan por interpretación; 267–272 salen.
