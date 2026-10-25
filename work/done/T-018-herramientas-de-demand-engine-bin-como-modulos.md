---
id: T-018
title: Herramientas de demand-engine/bin como módulos de demand_engine
status: hecha
depends: T-019
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Pasar refs, taxo, blocks, catalog-review y compare de scripts sueltos a módulos de src/demand_engine/, para que demand-engine sea una sola aplicación; en bin/ quedan envoltorios con la misma ruta y los mismos argumentos

## Criterios de aceptación

- [x] Código de refs, taxo, blocks, catalog-review y compare en src/demand_engine/ con una función main por herramienta
- [x] demand-engine/bin/<herramienta> conserva ruta, argumentos y salida, y sigue funcionando en el host con la biblioteca estándar
- [x] Código compartido entre herramientas (lectura de pins y referencias congeladas, páginas) en un solo módulo, sin duplicados
- [x] Pruebas mínimas por herramienta en demand-engine/tests/ y bin/run dev test en verde

## Resultado

Herramientas de demand-engine/bin como módulos de demand_engine (refs, taxo, pages, blocks, compare, catalog_review) con envoltorios de 9 líneas; lectura de referencias sin duplicados; 35/37 salidas idénticas y 2 mejoras de error; 51 pruebas en verde

## Notas

- 2026-10-25 Esperar a que cierre T-016: su sesión trabaja con bin/blocks, bin/catalog-review y bin/taxo. Al empezar, comprobar con bin/pm ready que T-016 está hecha y releer esos scripts (pueden haber cambiado).
- 2026-10-25 Dependencia movida de T-016 a T-019: T-019 crea bin/model y bin/train y modifica bin/blocks y bin/compare.
- 2026-10-25 Verificado con 37 órdenes de solo lectura (taxo, refs, blocks, catalog-review, compare, model, train) antes y después: 35 salidas idénticas byte a byte; cambian dos: blocks plan --ptd con un PTD inexistente da ahora «blocks: no existe el PTD X» en vez de una traza, y la traza ya existente de compare --pair con ejecuciones v2 (application es una lista en v2; compare solo conoce v0 y v1) cambia de ruta. Ese fallo de compare no se ha tocado. Lectura común en refs (pinned, load_gz, short, shopify_categories/attributes, google_mapping/names, ptd, enum_values; con caché) usada por taxo, blocks y demand.catalog; fichas congeladas en pages. 13 pruebas nuevas en tests/tools/ sobre referencias de juguete; 51 en verde.
