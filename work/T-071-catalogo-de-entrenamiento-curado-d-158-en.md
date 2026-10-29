---
id: T-071
title: Catálogo de entrenamiento curado (D-158) en demand-engine
status: pendiente
depends:
milestone:
created: 2026-10-28
---

## Objetivo

Implantar el catálogo curado de D-158: registro versionado de casos, admisión automática de candidatos por filtros F1–F4 y motivos A1–A6 al reunir los casos de bin/train, casos manuales y conservación de sus fichas

## Criterios de aceptación

- [ ] Registro del catálogo en git con origen, motivo, fecha, tienda, clave de entrada y versión del reglamento de cada caso; la selección de ECI migrada como primera vía de entrada
- [ ] bin/train admite candidatos de las ejecuciones (incluidas var/runs/live y la cola) con F1–F4 y A1–A6, topes 3 por clase y 1 por tienda y clase, sustitución del más antiguo sin A2/A3, y entrena solo con el catálogo
- [ ] Comandos para añadir y retirar un caso manual (F1 y F2, sin topes) con su motivo
- [ ] Las fichas congeladas de los casos del catálogo se conservan fuera de lo desechable; README de demand-engine y capture actualizados
- [ ] Pruebas de admisión, topes, duplicados y sustitución en bin/run dev test

## Notas

- 2026-10-29 D-194 ya está en train.pairs (T-091): un modelo con el campo «audit» cuenta como una de las dos ejecuciones si su engine.rulebook y engine.rules son los vigentes. Al conectar los casos de auditoría, pon «audit» en el modelo.
