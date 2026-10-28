---
id: T-070
title: Retirar las pistas de registro de certificados (D-154)
status: pendiente
depends:
milestone:
created: 2026-10-28
---

## Objetivo

Aplicar D-154 al catálogo de pistas de demand-engine: la auditoría no consulta registros externos, así que las pistas que lo piden se retiran y las del alcance de la certificación pasan a Aplicabilidad.

## Criterios de aceptación

- [ ] PV-5 y PV-39 marcadas como retiradas en catalog/hints.json, sin reutilizar sus números
- [ ] PV-6 y PV-40 retiradas y reescritas como pistas de Aplicabilidad con número nuevo y su origen
- [ ] bin/model hints check correcto y pruebas de demand-engine en verde

## Notas
