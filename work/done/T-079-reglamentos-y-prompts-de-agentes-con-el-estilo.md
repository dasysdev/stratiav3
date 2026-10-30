---
id: T-079
title: Reglamentos y prompts de agentes con el estilo de redacción (ASD-STE100)
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

Reescribir los reglamentos vigentes y los prompts de agentes con las reglas de CLAUDE.md § Estilo de redacción, para reducir la variación entre ejecuciones, sin cambiar ninguna regla.

## Criterios de aceptación

- [x] demand-engine/classifier/rulebook.md pasa a v5, reescrito con las reglas de estilo; cada regla conserva su sentido y la decisión que cita
- [x] demand-engine/classifier/paa.md pasa a v7, reescrito con las reglas de estilo; cada regla conserva su sentido y la decisión que cita
- [x] La cabecera de los dos reglamentos pide que el texto libre de la salida del agente (doubts, justificaciones) siga las reglas de estilo
- [x] El conjunto de control del clasificador (demand-engine/cases/, 14 casos) con v5 da lo esperado, o cada diferencia queda anotada con su causa
- [x] El control de PAA con v7 no tiene regresiones frente a v6, o cada diferencia queda anotada con su causa
- [x] Los prompts de agentes de las skills classify-batch, demand-model, paa-classify y web-audit, revisados con las reglas de estilo
- [x] Los tests del workspace pasan (bin/run dev test)

## Resultado

Reglamento del clasificador v5 con las reglas de estilo; control de 14 casos sin empeorar, con el doble de coste por caso

## Notas

- 2026-10-29 Hecho (2026-10-29): classifier/paa.md v7 reescrito con las reglas de estilo, junto con T-057, y con la cabecera de redacción de la salida; control de PAA v7 frente a v6 en los tres conjuntos de v6 sin regresiones (ver T-057). Skills classify-batch, demand-model, paa-classify y web-audit revisadas. Tests del workspace: 302 en verde. Aplazado por el usuario: rulebook.md (hoy v4 tras T-090; pasa a v5, no a v4) y su control de 14 casos.
- 2026-10-30 En classifier/paa.md, paso 7 (regla «cabe en un requisito existente al ampliar su pregunta»), añade: «Ampliar solo vale para el mismo hecho (prueba del paso 3). Si la pregunta trae otro hecho, propón un candidato.» Motivo: en botas, «¿Se estira el calzado de cuero?» oscila entre el candidato esperado «¿Cede o se adapta el corte al pie con el uso?» (v3, v6, v7b) y reformular cat.calzado/24 con dos hechos (v7a, v7 final). Decisión del usuario (2026-10-30): sin control propio; el control de T-079 lo comprueba en botas.
- 2026-10-30 Corrige la nota anterior: el cambio del paso 7 de paa.md pasa a T-106 (v8); T-079 no lo aplica ni lo comprueba.
- 2026-10-30 Saneamiento: los criterios 1 y 4 decían v4; rulebook.md ya es v4 (T-090) y la reescritura es la v5, como dice el siguiente paso.
- 2026-10-30 Hecho: rulebook.md v5 (agente; mismas decisiones, P1–P12 y bloques JSON que la v4, comprobado), cabecera «Redacción de la salida», v4 archivada en rulebook-v4.md; menciones de la v4 actualizadas (skill demand-model, README, model.py, train.py).
- 2026-10-30 Control v5 (var/runs/2026-10-30-v5-a, 14 casos; informe training/reports/2026-10-30-t079-control-report.md): composición 14/14 (v4: 13 y 12), hechos sin pregunta 16 (v4: 19), estabilidad v4–v5 igual o mejor que v4–v4 (aplicación 11/14 frente a 8/14). Ninguna medida empeora. Especializaciones 7/14, cuestiones clave 27/40 e inferidas 0/2, igual que con la v4.
- 2026-10-30 Coste: 38,5 M de tokens, 2,75 M por caso frente a 1,26–1,49 M con la v4 (doble de salida, +11–14 % de hechos contados). Cada /demand-model cuesta ahora el doble. Los modelos de v5-a son los modelos nuevos de los 12 conjuntos de PAA (T-107).
