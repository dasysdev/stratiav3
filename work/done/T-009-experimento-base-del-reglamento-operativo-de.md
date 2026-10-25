---
id: T-009
title: Experimento base del reglamento operativo de clasificación
status: hecha
depends:
milestone:
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Condensar D-020 a D-032 en un reglamento operativo con parámetros, convertir los 14 casos en un conjunto de casos y medir cuánto se acerca un agente nuevo, que solo ve el reglamento, al criterio del usuario

## Criterios de aceptación

- [x] Reglamento operativo v0 en demand-engine, con parámetros y formato de salida
- [x] Conjunto de casos con los 14 productos, su página congelada y la clase esperada
- [x] Herramienta de consulta de referencias para el agente (base heredada, PTD, mapeo Shopify→Google)
- [x] Ejecución de agentes nuevos sobre los 14 casos y comparación con el criterio del usuario, distinguiendo diferencias que cambian requisitos y diferencias de etiqueta
- [x] Informe con coincidencias, reglas ambiguas y huecos de herramientas

## Resultado

Experimento base: reglamento v0, 14 casos, taxo y compare; componentes 14/14, etiquetas 7/14, requisitos casi equivalentes en 12/14; propuestas en demand-engine/runs/2026-10-25-baseline/report.md

## Notas

- 2026-10-25 Montado: fuente nueva shopify-google en bin/refs (mapeo oficial Shopify→Google de la release v2026-08, fijada); demand-engine/bin/taxo (consulta de referencias con base heredada, PTD con special_feature y páginas congeladas en var/pages/); reglamento v0 en demand-engine/classifier/rulebook.md (9 parámetros, procedimiento en 5 pasos, salida JSON), sin ejemplos de los casos de prueba para no filtrar respuestas; 14 casos en demand-engine/cases/ (split dev); bin/compare. Ejecución: 3 agentes nuevos (5+5+4 casos) en demand-engine/runs/2026-10-25-baseline/.
- 2026-10-25 Resultado: componentes 14/14, descartes 5/5, etiquetas 7/14; en requisitos, 7 iguales, 5 con una cuestión de diferencia y 2 con diferencias reales (pienso, Luna). Las discrepancias de etiqueta van todas en la misma dirección (el agente aplica D-026+D-030 y deja como valor que condiciona lo que el esperado llama especialización; varios esperados son anteriores a D-030). Error del esperado: «apertura italiana» del Luna solo está en un icono. Informe en demand-engine/runs/2026-10-25-baseline/report.md, con 5 propuestas pendientes de decisión.
