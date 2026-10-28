---
id: T-063
title: Estudio: motor de captura y fichas congeladas fuera de demand-engine
status: hecha
depends:
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Estudiar y proponer, con alternativas y recomendación, dónde viven el motor de captura (D-046) y las fichas congeladas (var/pages, pages.py, taxo page fetch), que hoy están en demand-engine y que web-audit también usa (T-048 lee var/pages; el auditado de T-049 tendrá que capturar). Es el mismo antipatrón que tenían las referencias: lo compartido vive en el primer sistema que lo necesitó.

## Criterios de aceptación

- [x] Propuesta con alternativas, impactos (MPIR, PAA, selección y captura del entrenamiento, taxo page fetch, contenedor, perfiles de Chrome) y recomendación, aprobada por el usuario
- [x] Tareas de implantación abiertas en bin/pm según la alternativa aprobada, con la condición de no volver a capturar ni alterar las fichas congeladas existentes

## Resultado

Estudio del motor de captura y las fichas congeladas: aprobada la alternativa B (sistema capture/ con motor y almacén comunes, un ID existente se rechaza); implantación en T-066 (construir) y T-067 (corte sin recapturar)

## Notas

- 2026-10-28 Inventario: motor (13 módulos, ~1.300 líneas) usado por taxo page fetch, train discover/capture (selection, collect), MPIR (aparcado) y PAA (solo Browser, cdp, detect, pacing.draw, visit.OUTER_HTML y files; perfil y puerto propios en var/paa). Fichas: 45 en var/pages (15 antiguas sin instantánea, 30 chrome-cdp de ECI con instantánea), 66 MB; perfil de Chrome del motor 286 MB. Nadie lee el campo page de cases/*.json; los modelos registran caso y URL, no el sha256 de la ficha. El canon enlaza el README del motor (sampling-capture x2, OQ-14, OQ-15, I-18) y check_docs valida esos enlaces. T-048 ya necesita capturar: 45 fichas de 6 tiendas y pide 10 con Microdata.
- 2026-10-28 Usuario aprueba la alternativa B (sistema capture/ con el motor y el almacén de fichas comunes), con la regla del almacén (un ID existente se rechaza; nunca se sustituye una ficha). Descartadas: A (web-audit dependiente de demand-engine), C (solo el motor; capturas duplicadas por sistema) y D (dentro de references: otra ejecución, otra naturaleza, sin versión fijada). Implantación: T-066 (construir) y T-067 (corte, sin volver a capturar ni alterar fichas).
