---
id: glossary
title: Glosario y registro de conceptos
layer: meta
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE, FUND, GSC0 Anexo C, TAX, MPIR]
---

# Glosario y registro de conceptos

Esta es la capa de enrutamiento. Cada término tiene una definición breve (orientativa) y su **módulo canónico**. Cuando importa la precisión, la definición válida es siempre la del canon.

**Estados:** `V` vigente · `P` propuesta V1 · `—` pendiente.

## Contexto

| Término | Definición breve | Canon | Estado |
|---|---|---|---|
| **Agentic Commerce** | Comercio en el que agentes de IA intervienen en fases de la compra. | [scope](00-context/scope.md#marco-funcional-agentic-commerce) | V |
| **Agentic Commerce Readiness** | Preparación del ecommerce para las capacidades que requieren los agentes. El estudio solo cubre las condiciones informativas y técnicas para el descubrimiento y la decisión de compra. | [scope](00-context/scope.md#marco-funcional-agentic-commerce) | V |
| **Descubrimiento y decisión de compra** | Única fase del ciclo de compra dentro del alcance. | [scope](00-context/scope.md#marco-funcional-agentic-commerce) | V |
| **Sin navegación interactiva** | Modalidad de consumo examinada: no se operan páginas ni procesos. | [scope](00-context/scope.md#alcance-y-límites) | V |
| **Hipótesis aplicada** | Más calidad informativa → mejores condiciones para la IA → potencial efecto comercial. No es causalidad demostrada. | [business-model](00-context/business-model.md#hipótesis-aplicada-no-causalidad-demostrada) | V |

## Modelo conceptual

| Término | Definición breve | Canon | Estado |
|---|---|---|---|
| **Información comercial** | Contenidos, datos, afirmaciones y relaciones que describen productos, variantes, ofertas, vendedores y condiciones. | [commercial-information](10-model/commercial-information.md#información-comercial) | V |
| **Representación** | Forma concreta en que la información se expresa y organiza en una interfaz. | [commercial-information](10-model/commercial-information.md#representación-y-exposición) | V |
| **Exposición** | Condiciones bajo las que la información se publica, distribuye, recupera y consume. | [commercial-information](10-model/commercial-information.md#representación-y-exposición) | V |
| **Calidad (de la información comercial)** | Capacidad de resolver cuestiones relevantes con respuestas suficientes, interpretables, atribuibles y fundamentadas. | [commercial-information](10-model/commercial-information.md#calidad) | V |
| **Dimensión técnica / informativa** | Cómo se implementa y expone la interfaz, frente a qué permite determinar y fundamentar la información. | [commercial-information](10-model/commercial-information.md#dos-dimensiones-de-evaluación) | V |
| **Funciones informativas de la IA** | Descubrir, Acceder, Identificar, Comprender, Comparar, Evaluar, Justificar. No puntúan. | [ai-functions](10-model/ai-functions.md#definición) | V |
| **Interfaz de exposición** | Medio técnico con el que el ecommerce publica y distribuye información. | [evaluation-scopes](10-model/evaluation-scopes.md#interfaces-de-exposición) | V |
| **Ámbito de evaluación** | Base de información evaluada: Catálogos distribuidos, Web o Web Schema.org. En la unidad de evaluación es sinónimo de «interfaz» (D-010). | [evaluation-scopes](10-model/evaluation-scopes.md#ámbitos-de-evaluación) | V |
| **Catálogos distribuidos** | Feeds y catálogos para plataformas (Google Merchant Center, Meta Commerce). | [evaluation-scopes](10-model/evaluation-scopes.md#ámbitos-de-evaluación) | V |
| **Web** | Recurso web completo: HTML + Schema.org combinables si la relación está justificada. | [evaluation-scopes](10-model/evaluation-scopes.md#ámbitos-de-evaluación) | V |
| **Web Schema.org** | Solo el marcado Schema.org, aislado del HTML. No se agrega automáticamente con Web. | [evaluation-scopes](10-model/evaluation-scopes.md#ámbitos-de-evaluación) | V |
| **Requisito técnico general** | Condición de implementación, publicación, acceso, consumo o distribución de un ámbito. Obligatoria o recomendada. | [evaluation-scopes](10-model/evaluation-scopes.md#requisitos-técnicos-generales) | V |
| **Perfil de consumo** | Condiciones bajo las que un recurso se obtiene y lee en un ámbito. | [evaluation-scopes](10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) · operativa: [inputs-outputs](20-methods/audit-gsc/inputs-outputs.md#perfil-de-consumo) | P |
| **Modelo de demanda** | Representación estructurada de las cuestiones informativas relevantes para una clase de producto u oferta. Se materializa en un catálogo de RI. | [demand-model](10-model/demand-model.md#modelo-de-demanda) | V |
| **Relevancia** | Poder responder la cuestión cumple un papel justificable en la evaluación de la clase. | [demand-model](10-model/demand-model.md#modelo-de-demanda) | V |
| **RI (requisito informativo)** | Necesidad de conocimiento formulada como cuestión evaluable sobre una oferta. | [demand-model](10-model/demand-model.md#requisito-informativo-ri) | V |
| **Importancia relativa** | Crítico / Principal / Complementario. Cualitativa y ordinal, sin pesos. | [demand-model](10-model/demand-model.md#importancia-relativa) | V |
| **Núcleo de conocimiento** | Entidad, hecho o relación, desagregación y condiciones que caracterizan un RI. | [demand-model](10-model/demand-model.md#núcleo-de-conocimiento-y-perfil-de-resolución-y-pertinencia) | V |
| **Pertinencia informativa** | Contribución identificable y justificable a una necesidad constitutiva del RI. La proximidad temática no basta. | [demand-model](10-model/demand-model.md#núcleo-de-conocimiento-y-perfil-de-resolución-y-pertinencia) · operativa: [relevance](20-methods/audit-gsc/relevance.md#distinción-rectora) | V |
| **Escenario de compra** | Necesidades y restricciones de un comprador concreto. Posible extensión, no unidad de valoración. | [demand-model](10-model/demand-model.md#escenarios-de-compra-posible-extensión-no-unidad-de-valoración) | — |
| **Modelo de evaluación de calidad informativa** | Determina en qué grado la información de cada ámbito resuelve los RI pertinentes. | [evaluation-architecture](10-model/evaluation-architecture.md#definición) | V |
| **Cadena de análisis informativo** | RI → localización → pertinencia → disponibilidad → propiedades → GSC → IR. | [evaluation-architecture](10-model/evaluation-architecture.md#cadena-de-análisis-informativo) | V |
| **Disponibilidad efectiva** | Puerta binaria 0/1: ¿hay al menos un elemento pertinente obtenible y legible? 0 → IR = 0. | [effective-availability](10-model/effective-availability.md#definición) | V |
| **AC (criterio de aceptación)** | Condición evaluativa de un aspecto de la capacidad de resolver un RI. Son seis. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Concreción** | Cobertura de los componentes de la cuestión con la extensión y el detalle necesarios. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Precisión** | Significado inequívoco de afirmaciones, términos, valores y relaciones. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Aplicabilidad** | Atribución clara a la entidad, el alcance y las condiciones del RI. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Comparabilidad** | Contraste sobre bases equivalentes o equivalencias justificadas. NA si el RI no lo requiere. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Fiabilidad** | Corrección, actualidad y consistencia suficientemente sustentadas. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Justificación** | Base identificable y suficiente para sostener y reconstruir la respuesta. | [acceptance-criteria](10-model/acceptance-criteria.md#definición) | V |
| **Propiedades de calidad (P06–P18)** | Características observables que fundamentan los juicios. Sin puntuación propia. | [quality-properties](10-model/quality-properties.md#definición) | V |
| **P06–P13 (informativas y semánticas)** | Completitud, Granularidad, Explicitud, Claridad, Estructuración semántica, Identificabilidad, Contextualización, Normalización. | [quality-properties](10-model/quality-properties.md#informativas-y-semánticas) | V |
| **P14–P18 (fiabilidad y fundamentación)** | Exactitud, Actualidad, Coherencia, Trazabilidad, Verificabilidad. | [quality-properties](10-model/quality-properties.md#fiabilidad-y-fundamentación) | V |
| **Legibilidad técnica u operativa** | Que un dato pueda recuperarse y leerse. ≠ Claridad (P09). | [quality-properties](10-model/quality-properties.md#lectura-efectiva-frente-a-propiedades-semánticas) | V |
| **GSC (grado de satisfacción de criterio)** | Escala ordinal 0 No · 1 Parcialmente · 2 Sí, es suficiente, por AC × RI × ámbito. | [scoring-systems](10-model/scoring-systems.md#grado-de-satisfacción-de-criterio-gsc) | V |
| **NA (no aplicable)** | El criterio o requisito no corresponde a la cuestión o al ámbito. No es puntuación. | [scoring-systems](10-model/scoring-systems.md#grado-de-satisfacción-de-criterio-gsc) | V |
| **NE (no evaluable)** | Pertinente, pero sin evidencia para un juicio fundado. ≠ 0. | [scoring-systems](10-model/scoring-systems.md#grado-de-satisfacción-de-criterio-gsc) | V |
| **IR (indicador de resolución de requisito)** | Resolución de un RI por ámbito, en escala 0–10. Sin fórmula de agregación aprobada; disponibilidad 0 → IR = 0. | [scoring-systems](10-model/scoring-systems.md#indicador-de-resolución-de-requisito-informativo-ir) | V |
| **ICI (indicador de calidad informativa)** | Calidad informativa de un ámbito, según los IR y la importancia relativa. Sin fórmula. | [scoring-systems](10-model/scoring-systems.md#indicador-de-calidad-informativa-ici) | V |
| **TRI (tasa de resolución informativa)** | Proporción de RI suficientemente resueltos en un ámbito. Alias: indicador general de resolución informativa. | [scoring-systems](10-model/scoring-systems.md#tasa-de-resolución-informativa-tri) | V |
| **Estado binario de resolución** | Normalización 0/1 del IR: resolución suficiente o insuficiente. Es la noción «suficientemente resuelto» de la TRI. Regla pendiente. | [scoring-systems](10-model/scoring-systems.md#estado-binario-de-resolución) | P |
| **Prominencia informativa** | Clasificación 1/0 de cada componente resuelto según tenga soporte en una zona HTML prominente (title, metadescripción, H1, descripción inicial…). | [informative-prominence](10-model/informative-prominence.md#clasificación-binaria-de-prominencia-html) | P |
| **IP** | Porcentaje (0–100 %) de componentes resueltos con soporte en ubicaciones prominentes: `100 × C/N`; NA si N = 0. | [informative-prominence](10-model/informative-prominence.md#ip) | P |
| **Calidad ajustada** | Usa el IP como modificador secundario, sin cambiar el IR ni su estado binario. Fórmula y peso pendientes. | [informative-prominence](10-model/informative-prominence.md#calidad-ajustada) | P |
| **Tasa de cumplimiento técnico** | Proporción de requisitos técnicos satisfechos por ámbito. Alias: indicador general de resolución técnica. | [scoring-systems](10-model/scoring-systems.md#tasa-de-cumplimiento-técnico) | V |

## Auditoría operativa (GSC)

| Término | Definición breve | Canon | Estado |
|---|---|---|---|
| **Principios M01–M12** | Principios transversales de ejecución (fidelidad al RI, neutralidad, pertinencia funcional…). | [audit-gsc](20-methods/audit-gsc/README.md#principios-transversales-de-ejecución-m01m12) | P |
| **Unidad evaluada** | RI × ámbito aplicado a una entidad, oferta, recurso y condiciones concretos. | [inputs-outputs](20-methods/audit-gsc/inputs-outputs.md#unidad-evaluada) | P |
| **Bloqueo de preparación** | No puede delimitarse la entidad, el ámbito o el perfil. No se emiten GSC. | [inputs-outputs](20-methods/audit-gsc/inputs-outputs.md#validación-previa-de-entradas) | P |
| **Perfil operativo del RI** | Especificación reutilizable de qué buscar y qué constituye una contribución. | [ri-profile](20-methods/audit-gsc/ri-profile.md#campos-del-perfil-operativo) | P |
| **Componentes sustantivos / auxiliares** | El hecho solicitado, frente a la identificación, el vínculo, la unidad o el contexto necesarios. | [ri-profile](20-methods/audit-gsc/ri-profile.md#componentes-sustantivos-y-auxiliares) | P |
| **Candidato** | Elemento localizado cuya contribución al RI está por comprobar. | [exploration](20-methods/audit-gsc/exploration.md#inventario-de-candidatos) | P |
| **Estados de candidato** | Inicial · Pertinente · Pendiente de aclaración · No pertinente. | [relevance](20-methods/audit-gsc/relevance.md#estados-procedimentales-de-candidatos) | P |
| **Prueba de pertinencia (PF-01–PF-03)** | Contribución · Función · Fundamento. | [relevance](20-methods/audit-gsc/relevance.md#prueba-obligatoria-de-pertinencia-pf-01-a-pf-03) | P |
| **Conjunto pertinente** | Datos, afirmaciones, entidades, condiciones y relaciones contextualizados, con procedencia. | [relevance](20-methods/audit-gsc/relevance.md#conjunto-pertinente) | P |
| **Ruta de respuesta** | Afirmaciones y relaciones sustentadas que reconstruyen una conclusión. Sin escala de longitud. | [relevance](20-methods/audit-gsc/relevance.md#ruta-de-respuesta) | P |
| **Cobertura** | Alcance de la inspección que sustenta una conclusión. Más exigente para afirmar una ausencia. | [availability-coverage](20-methods/audit-gsc/availability-coverage.md#cobertura) | P |
| **Comprobación inconclusa** | Estado procedimental cuando no puede fundamentarse el binario 0/1. No es un tercer valor. | [availability-coverage](20-methods/audit-gsc/availability-coverage.md#comprobación-previa) | P |
| **Evidencia** | Contenido o resultado de una comprobación identificable, con contenido original y localizador. | [evidence](20-methods/audit-gsc/evidence.md#tipos-de-registro) | P |
| **Hallazgo** | Interpretación fundada de una suficiencia, limitación, discrepancia o ausencia. | [evidence](20-methods/audit-gsc/evidence.md#tipos-de-registro) | P |
| **Materialidad** | Una limitación reduce el GSC solo si afecta a la condición del AC para esa cuestión. | [gsc-decision](20-methods/audit-gsc/gsc-decision.md#materialidad) | P |
| **Árbol de decisión GSC** | Aplicabilidad → disponibilidad → NA/NE → 2/1/0 con prueba. | [gsc-decision](20-methods/audit-gsc/gsc-decision.md#árbol-de-decisión-operativo) | P |
| **Anclajes GSC por AC** | Reglas provisionales 0/1/2 de cada criterio. | [ac-guides](20-methods/audit-gsc/ac-guides.md#cómo-utilizar-los-anclajes) | P |
| **Expediente** | Registro estructurado y reexaminable de observaciones, decisiones y soportes. | [dossier](20-methods/audit-gsc/dossier.md#objetos-del-expediente) | P |
| **Informe de auditoría** | Resultados, limitaciones, GSC y recomendaciones verificables, vinculados al expediente. | [dossier](20-methods/audit-gsc/dossier.md#estructura-del-informe) | P |

## Construcción del modelo de demanda

| Término | Definición breve | Canon | Estado |
|---|---|---|---|
| **Clase interna** | Conjunto de productos u ofertas con reglas claras y necesidades informativas homogéneas. | [product-taxonomy](20-methods/product-taxonomy/README.md#conceptos-que-no-deben-confundirse) | P |
| **Subclase interna** | Clase más específica cuya diferenciación informativa está justificada. | [product-taxonomy](20-methods/product-taxonomy/README.md#conceptos-que-no-deben-confundirse) | P |
| **Faceta** | Dimensión transversal (uso, protección, estilo…) que segmenta sin exigir una rama exclusiva. | [product-taxonomy](20-methods/product-taxonomy/README.md#conceptos-que-no-deben-confundirse) | P |
| **Categoría externa** | Nodo de Shopify, Google o Amazon que responde a fines de la plataforma. | [product-taxonomy](20-methods/product-taxonomy/README.md#conceptos-que-no-deben-confundirse) | P |
| **Correspondencia (mapeo)** | Relación semántica versionada entre concepto externo y clase interna (equivalente, más amplia, solapamiento…). | [integration](20-methods/product-taxonomy/integration.md#relaciones-que-debe-poder-registrar-un-mapeo) | P |
| **Semáforo de validación** | Validado · Provisional · No verificado · Rechazado. Gobierno de la taxonomía, no calidad. | [integration](20-methods/product-taxonomy/integration.md#semáforo-de-validación-de-las-relaciones-no-puntuación-de-calidad) | P |
| **Prueba de especialización** | Preguntas de control para decidir entre subclase, faceta o aplicabilidad condicionada. | [subclasses](20-methods/product-taxonomy/subclasses.md#prueba-de-especialización) | P |
| **MPIR** | Modelo de Prácticas Informativas de Referencia: evidencia indirecta de necesidades, a partir de ecommerce referentes. | [mpir](20-methods/mpir/README.md#resumen) | P |
| **Ecommerce referente** | Comercio seleccionado con criterios documentados por su pertinencia o especialización. | [concepts-architecture](20-methods/mpir/concepts-architecture.md#definiciones-operativas) | P |
| **Unidad de contenido estructurada** | Menor fragmento que mantiene íntegra una relación informativa, con localizador. | [concepts-architecture](20-methods/mpir/concepts-architecture.md#definiciones-operativas) | P |
| **Señal informativa (SI-01–SI-08)** | Observación que sugiere una cuestión, un criterio o una relación potencialmente relevante. | [corpus-signals](20-methods/mpir/corpus-signals.md#clasificación-inicial-de-señales-informativas) | P |
| **Práctica / patrón de referencia** | Forma en que un referente usa la información, frente a su formulación normalizada entre fuentes. | [concepts-architecture](20-methods/mpir/concepts-architecture.md#definiciones-operativas) | P |
| **Cuestión candidata de demanda** | Pregunta inferida pendiente de normalizarse y justificarse como RI. | [concepts-architecture](20-methods/mpir/concepts-architecture.md#definiciones-operativas) | P |
| **Filtro de transferencia** | Seis comprobaciones antes de pasar una cuestión candidata al catálogo de demanda. | [interpretation-transfer](20-methods/mpir/interpretation-transfer.md#filtro-de-transferencia) | P |
| **Saturación cualitativa** | Cuando nuevos referentes ya no aportan patrones sustantivamente distintos. Sin umbral fijo. | [operation-validation](20-methods/mpir/operation-validation.md#saturación-cualitativa) | P |
