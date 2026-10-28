---
id: T-068
title: Inestabilidad de paa/test_e2e.py::test_run_set
status: pendiente
depends:
milestone:
created: 2026-10-28
---

## Objetivo

La prueba falló una vez en la suite completa (summary['captured'] == 0 en vez de 3) y pasa aislada: encontrar la causa (temporización de Chrome con las páginas locales, estado compartido con otras pruebas) y estabilizarla

## Criterios de aceptación

- [ ] Causa identificada y anotada en la tarea
- [ ] bin/run dev test pasa entera tres veces seguidas sin fallos de test_run_set

## Notas
