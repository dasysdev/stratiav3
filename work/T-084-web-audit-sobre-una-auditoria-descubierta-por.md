---
id: T-084
title: web-audit sobre una auditoría descubierta por la araña
status: pendiente
depends: T-083
milestone:
created: 2026-10-29
---

## Objetivo

Que web-audit/bin/audit lea una auditoría hecha con la araña (universo y páginas de D-167) y evalúe el requisito del sitemap en cada página auditada, también en las que solo encontró el rastreo.

## Criterios de aceptación

- [ ] bin/audit run funciona sobre una auditoría de la araña sin cambiar el método de los requisitos
- [ ] El requisito del sitemap se evalúa en cada página auditada, también en las que no están en los sitemaps
- [ ] Pruebas de web-audit en verde

## Notas
