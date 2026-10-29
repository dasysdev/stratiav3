---
id: T-083
title: Universo de la auditoría: cruce con los sitemaps y páginas de D-167 sobre el rastreo
status: pendiente
depends: T-082
milestone:
created: 2026-10-29
---

## Objetivo

Sobre lo que capturó la araña: el universo es la unión del rastreo y los sitemaps. Cada URL registra si se alcanzó, si está en los sitemaps y su tipo de página (ficha, categoría, política, portada u otra), con varias señales y no solo el marcado. Las URL de los sitemaps no alcanzadas se capturan una vez. Las páginas de D-167 (portada, políticas desde el pie, categoría por las migas) se localizan sobre lo capturado. pages audit toma las fichas del universo.

## Criterios de aceptación

- [ ] El manifiesto lista el universo: cada URL con alcanzada (sí/no), in_sitemaps y tipo de página; lo dudoso queda sin clasificar
- [ ] Las URL de los sitemaps no alcanzadas se capturan una vez y quedan registradas como no alcanzadas
- [ ] Portada, políticas y categorías de D-167 se localizan sobre lo capturado; solo lo no rastreado se pide aparte
- [ ] Las fichas auditadas se eligen del universo; pruebas de capture en verde

## Notas
