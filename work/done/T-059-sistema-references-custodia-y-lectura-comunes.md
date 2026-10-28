---
id: T-059
title: Sistema references: custodia y lectura comunes de las fuentes externas
status: hecha
depends:
milestone: codigo
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Crear el miembro de primer nivel references/ (reorganización de las referencias aprobada el 2026-10-28, opción A): una sola custodia (registro, versiones congeladas, versión fijada, diff) y los lectores por formato de las 36 fuentes que hoy guardan demand-engine y web-audit por separado. Las fuentes se comparten; su interpretación sigue en cada sistema (catálogo en demand-engine, fichas y requisitos técnicos en web-audit). Esta tarea construye y prueba references/ sin mover datos ni consumidores (eso es la tarea siguiente).

## Criterios de aceptación

- [x] Decisión registrada con /docs-update: las fuentes congeladas viven en references/ (enmienda D-133 y la regla 4 de evaluation-scopes) y la referencia técnica sigue en web-audit/reference/; python3 tools/check_docs.py correcto
- [x] references/ es miembro del workspace de uv con bin/refs (status, check, fetch, diff, pin), solo biblioteca estándar, y entra en el contenedor (pyproject raíz, testpaths, PYTHONPATH y COPY del Dockerfile)
- [x] Un solo almacén de versiones sustituye a los dos (Snapshot de demand-engine y store() de web-audit) y conserva sus reglas: versiones inmutables, descarga igual a la última descartada, .gz comparado por su contenido descomprimido, HTML por su texto, orden natural de versiones y primera versión fijada sola
- [x] references/sources.json registra las 36 fuentes con sus ids actuales (las 31 de web-audit/reference/sources.json más shopify, shopify-google, google, amazon-btg y amazon-ptd, que hoy están en el código), cada una con uses: los sistemas que la usan
- [x] refs pin lista los sistemas de uses de la fuente y cómo revisa cada uno (web-audit: reqs check; demand-engine: entrenamiento)
- [x] Lectores en references.read con la misma salida que los actuales: taxonomía (categorías, atributos, mapeo a Google y nombres), PTD de Amazon (definición y valores), vocabulario de Schema.org y secciones de text.md
- [x] Pruebas de references en verde con REFS_DIR de prueba, incluidas las de demand-engine/tests/tools/test_refs.py y web-audit/tests/test_refs.py trasladadas

## Resultado

references/ construido y probado: custodia común (registro de 36 fuentes con uses, un almacén, pins único, diff), lectores equivalentes a los actuales y D-149 en el canon; 166 pruebas en verde

## Notas

- 2026-10-28 Equivalencia comprobada con los datos reales sin moverlos (REFS_DIR temporal con enlaces a los dos var/refs y pins combinados): taxonomía, 1877 PTD, 1167 secciones y términos idénticos a demand_engine.refs y web_audit.reqs; el texto de las 28 page.html congeladas coincide con su text.md; pins('demand-engine') y pins('web-audit') igualan a cada pins.json actual.
- 2026-10-28 Para T-060: (1) ids sin cambios, kinds nuevos: shopify-taxonomy, shopify-google, google-taxonomy, amazon-browse-tree, amazon-ptd. (2) engine.refs y refs de importance.json: usar store.pins('demand-engine'). (3) taxo.py lee el árbol de Amazon con read.browse_tree(). (4) reqs: las secciones dan RefsError (no ReqsError); citable/section_text/headings/document_section/vocabulary/literal/VOCABULARY están en references.read. (5) web-audit/reference/sources.json queda duplicado en references/sources.json hasta el corte; los test_refs.py antiguos siguen mientras existan sus módulos. (6) references/tests/__init__.py es necesario: sin él pytest (importlib) nombra las pruebas references.* y tapa el paquete. (7) La comprobación de versión ya existente pasa al commit; shopify, schemaorg y amazon la hacen antes de descargar.
- 2026-10-28 refs check 2026-10-28: Shopify publicó v2026-10 (fijada v2026-08, shopify y shopify-google). No se descargó.
