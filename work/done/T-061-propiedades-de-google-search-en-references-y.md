---
id: T-061
title: Propiedades de Google Search en references y control de versiones citadas en demand-engine
status: hecha
depends: T-060
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Que demand-engine pueda leer y citar, a la versión fijada compartida, las propiedades que publican los documentos de Google Search del perfil de Web Schema.org, como base de T-056 (OQ-76), y que vea qué citas suyas han quedado en una versión distinta de la fijada cuando otro sistema cambie un pin.

## Criterios de aceptación

- [x] references.read devuelve, para cada documento de Google Search con tablas de propiedades, cada propiedad con su tipo, su sección (exigida o recomendada) y la versión fijada; pruebas sobre los text.md congelados
- [x] Una cita fuente:Tipo.propiedad@versión (p. ej. google-search-merchant-listing:Product.audience@2026-10-27) se resuelve con el lector, o da error si no existe en esa versión
- [x] Contraste con los requisitos de presencia de primer nivel de la referencia técnica (en requirements/consumer.json o, si T-055 ya los retiró, en su registro de retirados): misma propiedad y naturaleza, con las discrepancias explicadas en una nota de la tarea
- [x] demand-engine tiene una comprobación que lista las citas del catálogo (refs, sources, support y pistas por fuente) cuya versión no es la fijada; sale limpia con el catálogo actual e informa aparte de las citas a fuentes sin registro (ley:)
- [x] Pruebas en verde (bin/run dev test)

## Resultado

Lector de tablas de propiedades de Google Search en references (properties, citas fuente:Tipo.propiedad@versión, refs props), contraste 72/72 con la referencia técnica, bin/model refs en demand-engine (0 errores) y demand-engine en uses de los 7 documentos; 167 pruebas en verde

## Notas

- 2026-10-28 Contraste lector ↔ requirements/consumer.json (T-055 aún no ha retirado nada): los 72 requisitos de presencia de primer nivel («Cada [entidad] X del marcado | de nivel superior del marcado tiene la propiedad p.») de merchant-listing, product-snippet, product-variants y organization se resuelven con el lector (tipo X, p entre los nombres de la fila) y coinciden todos en naturaleza (obligatoria = tabla required; recomendada = recommended): 0 discrepancias. Las filas de esos tipos sin requisito de primer nivel están cubiertas con otra redacción: alternativas (price o priceSpecification.price, ws-consumer/052, 157), identificadores (gtin…, 024; duns/leiCode/iso6523Code, 321-322), condicionales (isVariantOf e inProductGroupWithID para variantes, 032-034; url de ProductGroup solo en una página, 202), anidadas (address.*, shippingRate.*, brand.name 015/190). En los requisitos anidados y condicionales (104 con «tiene [la propiedad] p.») hay 23 obligatorios cuya fila está en recommended o no existe: no es error del lector, la obligación condicional sale del texto de la celda («only required if…», «required for European Energy Labels», escala distinta de 1-5) o de otra propiedad (certificationRating.ratingValue, aggregateRating con varias Review). Consecuencia para T-056: la tabla da la naturaleza incondicional; una fila recommended puede llevar en su texto una obligación condicional, que el lector conserva en «text».
- 2026-10-28 Lector: references.read.property_rows/properties/property_citation (sección #structured-data-type-definitions de un text.md; tipo del encabezado, del ancestro que lo nombra o el único del H1, p. ej. Organization). Filas: 75 merchant-listing (25 required), 30 organization, 21 product-snippet, 11 product-variants, 23 return-policy (Option A/B como grupo), 15 review-snippet, 44 shipping-policy; javascript y sd-policies sin tablas. Casos raros cubiertos: «gtin | gtin8 | …» (barras dentro de la celda), «(or suggestedAge.maxValue)», «itemReviewed (if …)», filas de prosa sin nombres (3), y Certification.name, que el HTML de Google deja sin <tr> y sale suelto en text.md (se recupera). CLI: refs props FUENTE [TIPO] y refs props CITA. Pruebas: sintéticas y sobre los text.md congelados 2026-10-27 (se saltan si faltan).
- 2026-10-28 demand-engine: bin/model refs (demand_engine/demand/citations.py). Con el catálogo actual: 4379 citas, 0 errores; aparte, ley: 191 sin registro; 3864 sin versión propia que toman la de refs de su bloque; 37 sin ninguna: 33 amazon-ptd-prop en cat/alimentos.json y cat/mochilas.json (sus refs no citan amazon-ptd con versión: hueco menor del catálogo, sin arreglar aquí) y 3 shopify-attr en hints.json para.fuente (por diseño: se casan por prefijo). Errores: versión distinta de la fijada, fuente sin demand-engine en uses, propiedad de documento inexistente en su versión.
- 2026-10-28 Registro: demand-engine añadido a uses de los 7 documentos de Google Search con tablas (merchant-listing, organization, product-snippet, product-variants, return-policy, review-snippet, shipping-policy), para que refs pin avise a demand-engine; su review cita bin/model refs. Efecto: los modelos nuevos registran también esas 7 versiones en engine.refs, y pins('demand-engine') ya no es igual a refs de rules/importance.json hasta el próximo entrenamiento (no hay comprobación que lo exija). READMEs de references y demand-engine y CLAUDE.md al día. Pruebas: 167 en verde (bin/run dev test).
