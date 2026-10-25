---
id: T-016
title: Amazon como fuente de requisitos y catálogo determinista de bloques de categoría
status: hecha
depends:
milestone:
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Documentar en el canon que los PTD de Amazon pueden ser fuente de requisitos de categoría (enmienda D-009) y la construcción determinista de bloques cat. con catálogo revisado; generar el catálogo de bloques de las categorías de los 14 casos para revisión del usuario

## Criterios de aceptación

- [x] Decisiones documentadas con /docs-update, validador sin errores y revisión independiente aplicada
- [x] Generador determinista de bloques cat. (asignación de atributos repetidos a la categoría más general y candidatos de Amazon)
- [x] Borrador del catálogo de bloques cat. de las categorías de los 14 casos, con un documento de revisión para el usuario

## Resultado

D-039 a D-044 documentadas; generador bin/blocks; catálogo de 26 bloques y 170 requisitos; revisión manual sustituida por el entrenamiento (D-044)

## Notas

- 2026-10-25 D-039 (PTD de Amazon como fuente, enmienda D-009) y D-040 (bloques deterministas, catálogo revisado) documentadas; revisión independiente aplicada; nuevas I-16 (inferidas en bloque fijo) e I-17 (relevancia D-039 frente a D-030). Generador bin/blocks y catalog/amazon-map.json; esqueleto de 33 bloques; redacción del borrador en curso (3 agentes). Pendiente de decisión del usuario: separar entrenamiento (revisión humana) y ejecución (automática).
- 2026-10-25 Documentado D-041 (entrenamiento con revisión humana; ejecución automática; inferidas fuera de la clave hasta aceptarse), I-16 resuelta, nuevas I-19 (estados y versiones del catálogo en ejecución) y OQ-46 (alcance a MPIR y auditoría). Otra sesión trabaja en paralelo en MPIR (D-042, I-18): no tocar sus ficheros. Borrador del catálogo: 27 bloques, 167 requisitos (88 Shopify, 78 Amazon, 1 inferido), 4 críticos, 6 categorías vacías; documento demand-engine/catalog/REVIEW.md (bin/catalog-review). Pendiente: criterios transversales del usuario y revisión.
- 2026-10-25 Catálogo corregido con los criterios de D-043 y D-040: 26 bloques, 170 requisitos, 4 críticos, 8 inferidos→6 (2 de pienso pasan a normativa: Reglamento (CE) 767/2009 arts. 11.3, 15.a, 17.1.f; la cantidad neta no, se puede dar en la entrega). Composición textil normativa (UE 1007/2011 art. 16.1). REVIEW.md regenerado. Comprobado GPSR (UE) 2023/988 art. 19: propuesta para la capa general pendiente del usuario.
- 2026-10-25 Documentado D-044: el usuario solo define el marco (propósito, objetivos, características del resultado, criterios de éxito, invariantes); el entrenamiento induce reglas generales y específicas, compila el catálogo y se valida solo; ejecución automática. Nuevo módulo 10-model/model-training.md; D-041 y D-036 enmendadas; nueva OQ-47 (rasgos, métricas, informe, casos). Diagrama: https://claude.ai/artifact/74invDRN6mqd28sU6fgKtN. El documento catalog/REVIEW.md deja de tener uso como revisión manual. Siguiente: inducción de reglas de importancia con validación automática.
