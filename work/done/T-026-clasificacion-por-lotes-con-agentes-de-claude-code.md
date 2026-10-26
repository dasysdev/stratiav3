---
id: T-026
title: Clasificación por lotes con agentes de Claude Code
status: hecha
depends: T-025
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Procedimiento para clasificar un lote de fichas congeladas con agentes de Claude Code en paralelo (como /demand-model, decisión del usuario: «para clasificar usamos claude code»), con la misma salida y la misma comprobación (bin/model check), incluida la generación de los bloques que falten, y el ensamblado de cada modelo

## Criterios de aceptación

- [x] Procedimiento documentado (skill) que reparte un lote de fichas entre agentes en paralelo y deja var/runs/RUN/ID.json validado por bin/model check y ensamblado con bin/model assemble
- [x] Bloques que falten generados con catalog/DRAFTING.md en una primera fase (un caso por categoría) para no duplicarlos dentro del lote
- [x] Probado con 3 fichas del piloto de tipos distintos: salidas correctas y modelos ensamblados
- [x] Consumo de tokens por caso y por ejecución registrado
- [x] D-045 enmendada con /docs-update (el entrenamiento a escala clasifica con agentes de Claude Code, no con la API); README de demand-engine al día

## Resultado

Skill classify-batch y bin/train batch (fases, estado, tokens por transcripción, ensamblado en serie); guardia de register; prueba 3/3 ensamblada, 1,79 M tokens por caso

## Notas

- 2026-10-25 D-054 registrada con /docs-update (enmienda la ejecución a escala de D-045: clasificación con agentes de Claude Code); model-training 1.4. Falta del criterio 5 el README de demand-engine cuando exista el procedimiento.
- 2026-10-25 Skill .claude/skills/classify-batch y bin/train batch plan|status|usage|assemble (src/demand_engine/demand/batch.py): plan fijo en RUN/batch.json (fase 1 = primer caso capturado de cada tipo; fase 2 = el resto, tandas de ≤10 agentes), estado por caso (pendiente, con problemas, comprobada, ensamblada) y ensamblado en serie (comparten var/queue.jsonl). bin/model register rechaza el bloque de una categoría que ya tiene bloque de ejecución salvo --replace, y serializa los registros con un cerrojo (var/register.lock); el reglamento (paso 3) dice al agente que reutilice el bloque. Pruebas en verde.
- 2026-10-25 Consumo: el subagent_tokens de la notificación es el contexto de la última petición, no el consumo; train batch usage suma las peticiones de la transcripción del agente (output_file). Prueba con 3 fichas (var/runs/2026-10-25-eci-t026: mermelada, deportiva infantil, lijadora; fase 1 en paralelo): 3/3 correctas y ensambladas, 0 hechos sin pregunta. 5,38 M tokens en total (1,79 M por caso; 69.537 de salida, 5,0 M de lectura de caché, 305 k de escritura), 80 peticiones, 15,2 min de agente (212–390 s por caso). Bloques generados: 7 de categoría y 2 vacías (ha-15, aa-8-11). Proyección del piloto de 30: ~54 M tokens (algo menos en la fase 2, sin bloques que redactar).
- 2026-10-25 Dudas de los agentes para el ciclo de entrenamiento: (1) la mermelada subió propiedades del PTD FOOD a cat.alimentos aunque DRAFTING solo prevé bajar candidatos a una hija; (2) la lijadora puso parent cat.herramientas en un bloque cuya madre (ha-15) es vacía, y check no lo señala; (3) dudas de hechos: ante frente a composición sintética, ECI PLUS contado como promoción en gen/16, origen «Huétor Tájar» en gen/20. El guardia contra duplicados no se ejerció en la prueba (sin madres comunes): lo cubre la prueba unitaria; se verá en T-027 (bolso y mochila).
