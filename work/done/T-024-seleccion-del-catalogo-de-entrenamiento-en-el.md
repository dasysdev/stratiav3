---
id: T-024
title: Selección del catálogo de entrenamiento en El Corte Inglés (300 fichas)
status: hecha
depends:
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Elegir 300 fichas de elcorteingles.es (3 por categoría de ECI, unas 100 categorías repartidas entre departamentos) desde el sitemap de variantes (https://www.elcorteingles.es/sgfm/statics-front/front-msh3-eci-es/contents/sitemap-variants/sitemap.xml.gz), leído con el motor de captura, y documentar el criterio (OQ-48); de ellas, un piloto de 30 (10 categorías × 3, de departamentos distintos) para validar el sistema de entrenamiento

## Criterios de aceptación

- [x] check_site de www.elcorteingles.es con veredicto ok y evidencia guardada; si no es ok, la tarea se bloquea con el motivo
- [x] Sitemap de variantes descubierto con capture.sitemaps desde la ventana del sitio (sin curl), con el recuento de URL por categoría de ECI
- [x] Variantes deduplicadas: una ficha por producto; solo fichas de producto
- [x] Lista en demand-engine/training/selection/ con 300 fichas (URL, ID, categoría de ECI), 3 por categoría elegidas al azar con semilla fija, más reservas por categoría y el piloto de 30 marcado; ninguna excluida por robots.txt
- [x] Criterio de selección documentado y OQ-48 actualizada con /docs-update; check_docs sin errores

## Resultado

Selección ECI: bin/train discover|select, 100 tipos de 26 departamentos, 300 fichas + 200 reservas, piloto de 30; criterio en training/selection/README.md; D-053 y OQ-48

## Notas

- 2026-10-25 bin/train discover|select (src/demand_engine/demand/selection.py, tests/demand/test_selection.py; 65 pruebas en verde). check_site ECI ok (Akamai presente; robots excluye Bytespider y Amazonbot). Descubrimiento var/training/eci/discovery-20261025T220205: 48 sitemaps de producto, 501.645 URL → 397.810 productos (102.715 variantes). Dos formas de URL (con -pr- y variante, y sin ella). Tipo = primera palabra en singular sin palabras vacías y con categoría de ECI que lo nombra (filtra marcas). Selección training/selection/eci-2026-10-25.json: 100 tipos de 26 departamentos, 300 fichas + 200 reservas; piloto 30 (mermelada, sopera, bolso de viaje, música, piercing, deportiva infantil, mochila escolar, lijadora, botella térmica, aceite de motor). Criterio en training/selection/README.md; D-053 y OQ-48 con /docs-update.
