---
id: T-079
title: Reglamentos y prompts de agentes con el estilo de redacción (ASD-STE100)
status: pendiente
depends:
milestone:
created: 2026-10-29
---

## Objetivo

Reescribir los reglamentos vigentes y los prompts de agentes con las reglas de CLAUDE.md § Estilo de redacción, para reducir la variación entre ejecuciones, sin cambiar ninguna regla.

## Criterios de aceptación

- [ ] demand-engine/classifier/rulebook.md pasa a v4, reescrito con las reglas de estilo; cada regla conserva su sentido y la decisión que cita
- [ ] demand-engine/classifier/paa.md pasa a v7, reescrito con las reglas de estilo; cada regla conserva su sentido y la decisión que cita
- [ ] La cabecera de los dos reglamentos pide que el texto libre de la salida del agente (doubts, justificaciones) siga las reglas de estilo
- [ ] El conjunto de control del clasificador (demand-engine/cases/, 14 casos) con v4 da lo esperado, o cada diferencia queda anotada con su causa
- [ ] El control de PAA con v7 no tiene regresiones frente a v6, o cada diferencia queda anotada con su causa
- [ ] Los prompts de agentes de las skills classify-batch, demand-model, paa-classify y web-audit, revisados con las reglas de estilo
- [ ] Los tests del workspace pasan (bin/run dev test)

## Notas
