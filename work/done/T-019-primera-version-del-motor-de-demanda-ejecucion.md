---
id: T-019
title: Primera versión del motor de demanda: ejecución y reglas de importancia
status: hecha
depends:
milestone:
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Dejar una primera versión para probar productos reales: documentar la operación del entrenamiento (OQ-47, I-19) y el motor de captura compartido; reglamento v2 que elige bloques del catálogo; ensamblador determinista con clave versionada, lo no compilado y cola; rasgos del catálogo; reglas de importancia inducidas por el árbol de Shopify; pasada de control con los 14 casos e informe; comando /demand-model URL

## Criterios de aceptación

- [x] D-045 y D-046 documentadas con /docs-update, validador sin errores y revisión independiente aplicada
- [x] Reglamento v2, bin/model (bloques y ensamblado) y bin/train (inducción, compilación y medida) funcionando sobre el catálogo
- [x] Catálogo con rasgos y reglas de importancia compiladas; cada requisito guarda la regla que lo decidió
- [x] Pasada de control con los 14 casos (dos ejecuciones) e informe agregado en runs/
- [x] Comando /demand-model URL documentado y probado con un producto

## Resultado

Motor de demanda v1: D-045 a D-049, bin/model y bin/train, reglas de importancia por el árbol, pasada de control (runs/2026-10-25-v2-report.md) y /demand-model probado con un producto real

## Notas

- 2026-10-25 D-045 (operación del entrenamiento v1, cierra OQ-47 e I-19) y D-046 (motor de captura compartido) documentadas; dos revisiones independientes aplicadas. Código: src/demand_engine/demand/ (catalog, model, train, text) con bin/model y bin/train; rasgos etiquetados (170) e índice de 552 fuentes; reglas 1 compiladas (66 reglas; coherencia del catálogo 27 → 0; 29 importancias cambian; críticos: las 4 medidas que fijan lo vendido); reglamento v2; DRAFTING.md para bloques en ejecución; bin/blocks --ptd; skill /demand-model; tests/demand/test_rules.py (9 pruebas, pasan en el host sin pytest). Pasada de control v2-a y v2-b lanzada (6 agentes).
- 2026-10-25 Pasada de control v2 (runs/2026-10-25-v2-a y -b, 1,18 M tokens, 34 min, sin bloques generados); informe runs/2026-10-25-v2-report.md. Estabilidad: clave 12/14, especializaciones 13/14, importancia 320/320 (v1: bloques de sector 4/14, importancia 91 %). Control: composición 10 y 12/14, especializaciones 7 y 7/14, cuestiones clave 62 y 68 %. Hechos declarados sin pregunta: 5/319 y 7/307 (casi todos país de fabricación). Votos que coinciden con la regla: 446/681; más votos en contra: medida descriptiva (marco D-043.1, 27). Candidata 2 con votos descartada por la validación (estabilidad de la importancia 320 → 314, por composición inestable alias/categoría); siguen las reglas 1. Prueba en vivo en curso: guaw.com colchoneta refrescante (Camas para mascotas, ap-2-9, fuera del catálogo). Burritoblanco.com devuelve desafío de Cloudflare a la descarga simple. Pendiente de decisión del usuario: modelo = producto y aplicación = oferta (aceptado), término «estándar» y requisitos condicionados por la oferta (batería del reacondicionado).
- 2026-10-25 D-047 (modelo = producto, aplicación = oferta, oferta estándar, elementos digitales al modelo), D-048 (la oferta no aporta requisitos; sin especializaciones de oferta; sustituye D-027) y D-049 (pregunta universal de promociones, gen/16) documentadas; revisión independiente en curso. Motor: clave y nombre del producto, oferta aparte con su etiqueta, capa general con condicionados en gris; reglamento v2 actualizado; todos los modelos reensamblados. Prueba en vivo: runs/live/colchoneta-refrescante-freedog.model.md (Camas de enfriamiento — oferta con descuento, con variantes); 2 bloques generados al vuelo (no compilados); reglas heredadas de ap-2 y votos provisionales donde la rama no tiene regla.
- 2026-10-25 Revisión de D-047 a D-049 aplicada: condición 1 restablecida («Es del producto y estable»); citas de D-033 y D-038 recortadas; la capa general forma parte de todo modelo y la clave empieza por gen@<versión> (capa general 0.2 con gen/16); «estándar» = ninguna condición declarada (OQ-50, ampliada con la vigencia y las promociones sin rebaja); el ejemplo de fin de serie pasa a hueco del marco; glosario sin «especialización de oferta». Cola: re-ensamblar sustituye la entrada. Pendiente de decisión del usuario (señales de la validación): país de fabricación en la capa general (con GPSR art. 19) y peso, grosor y gramaje fuera de «medida descriptiva».
