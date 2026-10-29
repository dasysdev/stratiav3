---
id: product-taxonomy-integration
title: Taxonomía — estrategia de integración y alineación de conceptos
layer: method
status: propuesta
version: 1.3
updated: 2026-10-29
sources: [TAX §3, TAX §4, INTAKE 2026-10-24-define-class, INTAKE 2026-10-24-specialization-criterion, INTAKE 2026-10-29-issues-review]
---

# Taxonomía — estrategia de integración y alineación de conceptos

Parte de [Taxonomía de clases de producto](README.md). Fuentes descritas en [sources.md](sources.md).

## No fusionar literalmente las fuentes: integrar sus significados

La vía recomendada es una **integración semántica con identificadores internos estables**, no la unión de nombres o nodos. Las fuentes siguen existiendo como sistemas autónomos. Cada clase propia explicita a qué nodos o atributos externos se vincula, qué relación mantiene con ellos y con qué fundamento.

Una coincidencia de etiqueta no acredita identidad conceptual; dos conceptos pueden compartir nombre y tener inclusiones distintas. Inversamente, dos categorías con nombres diferentes pueden cubrir prácticamente el mismo dominio. La semántica se verifica por **definición, reglas de inclusión, uso comercial y ejemplos positivos/negativos**, no solo por la ruta nominal.

## Arquitectura de cinco capas

| Capa | Contenido | Resultado esperado |
|---|---|---|
| 0. Fuentes congeladas | Versiones de Shopify, Amazon por marketplace, Google y fuentes documentales. | Procedencia reproducible. |
| 1. Alineación semántica | Conceptos externos, atributos, definiciones y correspondencias con revisión. | Mapa de relaciones, sin perder discrepancias. |
| 2. Taxonomía propia | Clases, subclases, posibles facetas, inclusiones y exclusiones. Superada por D-033 (D-214). | Estructura canónica para delimitar el estudio. |
| 3. Modelos de demanda | Requisitos compartidos y diferenciales, con aplicabilidad e importancia relativa. | Catálogo de preguntas evaluables por clase. |
| 4. Auditoría por ámbito | Evaluación posterior de la resolución de cada requisito en cada interfaz pertinente. | Diagnóstico de calidad informativa; fuera del objeto de esta taxonomía. |

> **Estado: capa 2 superada** por [D-033](../../30-governance/decisions.md#d-033) ([D-214](../../30-governance/decisions.md#d-214)): el sistema no construye clases internas. El modelo de demanda se identifica por sus bloques de requisitos y la herencia sale del árbol de Shopify.

Esta separación evita que el cambio de un nodo Amazon o un atributo de Google obligue a cambiar de inmediato el significado de una clase interna o a reescribir todos los requisitos del estudio.

## Jerarquía y facetas, no profundidad uniforme

La clasificación principal puede mantener una relación **general-específico** y permitir, cuando sea necesario, múltiples pertenencias o facetas. Por ejemplo, el uso previsto y el nivel de protección pueden cruzarse: ciertas botas son simultáneamente calzado de montaña y equipo de protección. No conviene forzar una elección arbitraria entre esas ramas si altera qué requisitos resultan aplicables.

Si la herramienta operativa solo admite un padre, conservar un **padre primario** para navegación y representar las demás relaciones mediante facetas y vínculos tipados. Este es un compromiso de implementación, no una afirmación ontológica de exclusividad.

**No establecer un nivel de profundidad fijo.** El objetivo práctico de obtener al menos una especialización adicional se aplica donde exista una diferencia significativa de demanda y evidencias; no como mandato de subdividir todas las clases Shopify. Para incorporar una especialización a la [clase de estudio](../../10-model/study-class.md) rige, en cambio, el [criterio de especialización](../../10-model/study-class.md#criterio-de-especialización) ([D-022](../../30-governance/decisions.md#d-022)).

## Relaciones que debe poder registrar un mapeo

| Relación | Uso recomendado |
|---|---|
| Equivalente confirmada | Extensiones y definiciones suficientemente alineadas para uso intercambiable en el alcance estudiado. |
| Aproximadamente equivalente | Alta similitud, pero diferencias de frontera o uso que deben conservarse. |
| Más amplia / más específica | Una categoría incluye conceptualmente a la otra dentro del alcance declarado. |
| Relacionada | Relación asociativa sin implicación de inclusión. |
| Solapamiento parcial | Parte de los productos pertenece a ambos conceptos, pero ninguno contiene al otro por completo. |
| Sin correspondencia comprobada | No se identifica un equivalente defendible o la referencia necesaria no está disponible. |

Los tipos anteriores son una propuesta interna inspirada en SKOS [R16]. **No deben confundirse `equivalente` con `identidad absoluta`**, ni representarse todos los solapamientos como equivalencias exactas.

## Procedimiento de correspondencia

1. **Identificar los dos extremos:** sistema, versión, marketplace cuando corresponda, ID, nombre y ruta completa.
2. **Examinar el alcance:** definición, finalidad funcional, productos incluidos y excluidos, atributos distintivos y posibles relaciones con otras ramas.
3. **Proponer la relación:** equivalencia, inclusión jerárquica, aproximación, relación o solapamiento; evitar decisiones binarias precipitadas.
4. **Contrastar con casos:** productos representativos y contraejemplos, información de ecommerce referentes y documentación de las fuentes.
5. **Registrar evidencia y estado:** fuente concreta, justificación, revisión y si el mapeo es provisional o está validado.
6. **Comprobar consecuencias:** qué clases internas, facetas y requisitos informativos se verían afectados por utilizar esa correspondencia. (Las clases internas, superadas por D-033: [D-214](../../30-governance/decisions.md#d-214).)

Se admiten relaciones **uno-a-varios y varios-a-varios**. La ausencia de mapeo no obliga a descartar una clase candidata; obliga a identificar correctamente su origen y el grado de incertidumbre.

## Semáforo de validación de las relaciones (no puntuación de calidad)

- **Validado:** fuentes verificadas y definiciones comparadas; los casos fronterizos se han resuelto o explicitado.
- **Provisional:** correspondencia plausible con algún límite relevante pendiente de contraste.
- **No verificado:** se cuenta con un nombre, ejemplo o referencia parcial, pero faltan evidencias para establecer una relación semántica.
- **Rechazado o sustituido:** la correspondencia se descartó o cambió tras la revisión, conservando historial.

Estos estados son controles de **gobierno de la taxonomía**, no grados de satisfacción de criterios ni indicadores de calidad informativa del sistema de auditoría ([sistemas de valoración](../../10-model/scoring-systems.md)).

## Relacionado

- Ficha de correspondencia: [data-model-governance.md](data-model-governance.md#anexo-b-ficha-de-correspondencia-propuesta).
- Creación de subclases: [subclasses.md](subclasses.md).
- Composición de la clase de estudio con facetas concurrentes (canon): [study-class](../../10-model/study-class.md).
