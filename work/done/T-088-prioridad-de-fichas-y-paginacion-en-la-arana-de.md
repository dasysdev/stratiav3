---
id: T-088
title: Prioridad de fichas y paginación en la araña de capture
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

La araña captura primero lo que más probablemente es una ficha: confirma fichas por señales del documento (og:type, Product en JSON-LD o microdatos), prioriza las URL con la forma de las fichas confirmadas y después los listados que más fichas descubren. Sigue las URL cuyo único parámetro es de paginación numérico; las facetas siguen fuera. Decisión del usuario (2026-10-29): aprender en el rastreo, sin configuración por sitio; admitir solo paginación.

## Criterios de aceptación

- [x] Con un tope que corta el rastreo de un sitio local, la araña captura sus fichas antes que las categorías y las demás páginas
- [x] La araña sigue ?page=N (único parámetro, numérico) y no sigue ?q= ni otros filtros
- [x] Cada página registra sus señales de ficha y su forma de URL; el manifiesto resume las formas (visitadas, fichas, rendimiento)
- [x] La reanudación reconstruye la prioridad desde el diario sin volver a pedir nada
- [x] Canon (enmienda de D-173) con /docs-update; README de capture y CLAUDE.md al día; pruebas en verde

## Resultado

La araña captura primero las fichas (aprendidas en el rastreo) y sigue la paginación numérica (D-204)

## Notas

- 2026-10-29 Hecho: spider con planificador por forma de URL (product > probe > other por fichas descubiertas por página), señales de ficha (og:type, Product en lo alto del JSON-LD o microdatos), paginación numérica como único parámetro; entrada con shape, chosen_as y product_signals; crawl.shapes y product_pages en el manifiesto. burritoblanco: 35 fichas en 40 URL. Canon: D-204 (D-174 lo tomó en paralelo otra sesión, repaso de OQ; renumerado). check_docs no detecta ID de decisión duplicados. 255 pruebas en verde.
