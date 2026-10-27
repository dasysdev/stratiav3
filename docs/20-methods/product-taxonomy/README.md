---
id: product-taxonomy
title: Taxonomía de clases de producto — marco metodológico
layer: method
status: propuesta
version: 1.8
updated: 2026-10-27
sources: [TAX Resumen, TAX §1, INTAKE 2026-10-24-define-class, INTAKE 2026-10-24-specialization-criterion, INTAKE 2026-10-25-class-composition, INTAKE 2026-10-25-own-questions-offer, INTAKE 2026-10-25-objective-classification, INTAKE 2026-10-25-requirements-purpose, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-amazon-source-blocks, INTAKE 2026-10-27-paa-construction-route]
---

# Taxonomía de clases de producto — marco metodológico

*Referencias, estrategia de integración y reglas para los modelos de demanda.*

Documento metodológico de referencia y propuesta de diseño. No incluye los catálogos taxonómicos de las plataformas ni sustituye el canon del modelo ([`10-model/`](../../10-model/demand-model.md)).

## Resumen ejecutivo

El proyecto necesita una **taxonomía propia de clases de producto u oferta** que permita seleccionar la unidad adecuada para construir modelos de demanda. Su finalidad no es replicar la navegación de una tienda ni validar datos de un marketplace: es disponer de clases suficientemente bien delimitadas para formular y justificar las cuestiones informativas que deben poder resolverse durante el descubrimiento y la decisión de compra.

La conclusión de la investigación es que **Shopify, Amazon y Google son fuentes complementarias, pero sus estructuras no son directamente fusionables en un único árbol sin interpretación semántica**. Shopify constituye una buena estructura principal de referencia por sus categorías y atributos normalizados; Amazon puede aportar especializaciones de navegación y esquemas de atributos; Google sirve para contrastar categorías, vocabulario comercial y reglas de datos. La información publicada por ecommerce referentes sigue siendo una fuente principal para inferir requisitos informativos ([modelo de demanda](../../10-model/demand-model.md); vía desarrollada en [MPIR](../mpir/README.md)).

> El canon reconoce como vías de construcción del modelo de demanda esta taxonomía, el [MPIR](../mpir/README.md) ([D-009](../../30-governance/decisions.md#d-009); aparcado por [D-095](../../30-governance/decisions.md#d-095)) y People Also Ask ([D-094](../../30-governance/decisions.md#d-094)); se suman, como provisionales, las cuestiones inferidas ([D-036](../../30-governance/decisions.md#d-036)). Ver [construction-routes](../../10-model/construction-routes.md). Amazon y Google son fuentes de apoyo de la taxonomía; los PTD de Amazon pueden además ser fuente de requisitos de la categoría cuando son relevantes para la clase ([D-039](../../30-governance/decisions.md#d-039)).

La estrategia es **conservar las fuentes externas sin modificarlas, construir correspondencias auditables y derivar una capa interna de clases y facetas**. Un siguiente nivel de especialización es deseable allí donde cambien sustancialmente las necesidades informativas, pero no debe imponerse a todas las ramas ni justificarse por la mera existencia de una subcategoría en Amazon.

| Decisión metodológica | Orientación propuesta |
|---|---|
| Estructura principal | Shopify Standard Product Taxonomy, fijada por versión como referencia inicial. |
| Ampliación de granularidad | Amazon Browse Tree, y en su caso atributos de Amazon Product Type Definitions. |
| Contraste complementario | Google Product Taxonomy, Merchant Center y Manufacturer Center. |
| Unidad canónica | Clase interna definida por alcance funcional e informativo; identificador propio. |
| Mecanismo de integración | Correspondencias semánticas versionadas, no unión automática de árboles. |
| Vínculo con demanda | La clase delimita el dominio; los requisitos informativos se infieren y validan por separado. |

## Propósito

La taxonomía de clases es una **estructura de referencia anterior al modelo de demanda**. Sirve para:

- delimitar qué productos pertenecen a una clase;
- identificar familias y especializaciones comparables;
- organizar el trabajo de construcción de requisitos;
- reutilizar cuestiones compartidas sin perder aplicabilidad;
- mantener trazabilidad hacia las fuentes que justifican la segmentación.

La taxonomía **no** pretende resolver por sí misma los requisitos de demanda, establecer la calidad de la información publicada, decidir si un producto es adecuado para un comprador particular ni reproducir todas las categorías de comercio digital disponibles.

## Alcance que debe respetarse

Se mantiene el perímetro del estudio ([alcance](../../00-context/scope.md)): descubrimiento y decisión de compra, España desde octubre de 2026 con horizonte al menos hasta el primer trimestre de 2027; productos, variantes, ofertas, vendedores y condiciones comerciales; ámbitos Catálogos distribuidos, Web y Web Schema.org ([ámbitos](../../10-model/evaluation-scopes.md)).

La taxonomía es transversal a esos ámbitos: **no se diseña una clase distinta porque una interfaz tenga o no tenga cierto campo**. El vínculo con interfaces se determina posteriormente al definir qué requisitos resultan pertinentes para cada ámbito.

## Conceptos que no deben confundirse

| Concepto | Significado operativo para el proyecto |
|---|---|
| Categoría externa | Nodo de una clasificación Shopify, Google o Amazon; responde a fines de la plataforma. |
| Tipo de producto externo | Noción propia del sistema proveedor; en Amazon, un tipo PTD no equivale necesariamente a un nodo de navegación. |
| Atributo y valor | Característica y posible valor descriptivo; pueden revelar una especialización, pero no son clases por defecto. |
| Clase interna | Conjunto de productos u ofertas delimitado por reglas claras y necesidades informativas suficientemente homogéneas. |
| Subclase interna | Clase más específica cuya delimitación y diferenciación informativa están justificadas. |
| Faceta | Dimensión transversal (uso, protección, estilo, material...) que ayuda a segmentar sin exigir una rama exclusiva. |
| Clase de estudio | Clase objeto del modelo de demanda: clase general más todas las especializaciones aplicables ([definición canónica](../../10-model/study-class.md)). |
| Modelo de demanda | Catálogo de requisitos informativos pertinentes para la clase ([definición canónica](../../10-model/demand-model.md)). |
| Variante u oferta | Entidades comerciales sobre las que recaen preguntas; no son automáticamente categorías taxonómicas. |

**Precedencia.** En definiciones de calidad informativa, requisitos, ámbitos e indicadores prevalecen los módulos de [`10-model/`](../../10-model/demand-model.md). Este marco propone la arquitectura de clasificación y no modifica aquellas definiciones.

## Índice del marco

| Módulo | Contenido | Secciones v0 |
|---|---|---|
| [sources.md](sources.md) | Inventario razonado de fuentes externas y referencias R1–R16. | TAX §2, §12 |
| [integration.md](integration.md) | Integración semántica, arquitectura de cinco capas, jerarquía y facetas, reglas de alineación, semáforo de validación. | TAX §3–4 |
| [subclasses.md](subclasses.md) | Cuándo crear una subclase, prueba de especialización, ejemplo de botas, caso de trabajo de las sábanas de coralina, de la clase al modelo de demanda. | TAX §5–7 |
| [cases.md](cases.md) | Casos de evaluación de la clase de estudio: toallas, sofá cama, juguete de cuerda, bota de equitación, sofá reclinable de exposición, funda nórdica, pienso, manta, plaid, zapatillas de baño, protector de colchón, cojín y funda nórdica bordada. | — |
| [requirement-blocks.md](requirement-blocks.md) | Bloques de requisitos, capa general con importancias por defecto, pruebas de importancia, formato del catálogo, denominación y cuestiones inferidas (propuesta). | — |
| [data-model-governance.md](data-model-governance.md) | Modelo de datos, procedimiento, piloto, gobierno, riesgos, indicadores de salud, conclusiones, decisiones pendientes y fichas (Anexos A–B). | TAX §8–11, Anexos |

**Nota sobre evidencia:** este marco registra conclusiones de documentación externa y decisiones metodológicas propuestas. No constituye una extracción del árbol completo de Amazon.es ni certifica mapeos específicos entre hojas de las tres plataformas. La aprobación de clases requiere la comprobación indicada en el método.
