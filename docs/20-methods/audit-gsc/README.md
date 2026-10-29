---
id: audit-gsc
title: Marco operativo de valoración GSC de los criterios de aceptación
layer: method
status: propuesta
version: 0.6
updated: 2026-10-30
sources: [GSC0 §1, GSC0 §2, GSC0 §13.4, GSC0 Anexo D, FUND §9, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-single-consumption-profile, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Marco operativo de valoración GSC

Procedimiento general y reutilizable para que un **agente auditor** examine información comercial, identifique información pertinente para un requisito informativo (RI), obtenga evidencias y emita el **grado de satisfacción de cada criterio de aceptación (GSC)**.

Aplica a cualquier modelo de demanda construido conforme a los fundamentos del proyecto ([canon](../../README.md#10-model--canon-conceptual-vigente)) y a los ámbitos **Catálogos distribuidos**, **Contenido** y **Marcado** ([ámbitos](../../10-model/evaluation-scopes.md)), con sus perfiles de consumo admitidos.

**Ámbitos de la V1** ([D-152](../../30-governance/decisions.md#d-152), con los nombres de [D-220](../../30-governance/decisions.md#d-220)): Contenido y Marcado, con el único perfil de consumo (la respuesta HTTP sin ejecutar JavaScript, [D-156](../../30-governance/decisions.md#d-156)). Cada ámbito lee su representación: Contenido, la salida del [filtro Alfa](filter-alfa.md); Marcado, el marcado. Catálogos distribuidos queda aplazado; mientras tanto, la consistencia transversal solo examina el par Contenido ↔ Marcado.

**Ejecución automática** ([D-186](../../30-governance/decisions.md#d-186)): el agente auditor ejecuta la auditoría sin intervención humana. Antes de entregar, una persona revisa solo las NE y las comprobaciones inconclusas ([criterio de revisión humana](dossier.md#criterio-de-revisión-humana)).

> **Estado: propuesta V1 para pilotaje.** Consolida los principios acordados y desarrolla reglas prácticas, pero **los anclajes, umbrales de suficiencia y protocolos no están empíricamente validados**. Deben probarse y aprobarse mediante casos de calibración ([calibration.md](calibration.md)). No modifica el marco conceptual ni añade criterios, propiedades, escalas o indicadores de calidad. Las reglas se convierten en instrucciones de Skill **solo después de probarlas** con expedientes reproducibles. Este marco es un **procedimiento general**: los perfiles concretos de RI pertenecen al catálogo de demanda y los resultados de cada ecommerce, al expediente (GSC0 Anexo D.1).

## Pregunta operativa

Para una **unidad evaluada** —RI, ámbito y entidad/oferta concretos, con su alcance y condiciones—:

**¿Qué información comercial pertinente puede obtenerse y leerse; qué evidencia demuestra sus propiedades relevantes; y qué GSC corresponde a cada AC a partir de esas comprobaciones?**

La auditoría evalúa **las condiciones informativas ofrecidas por el ecommerce** para determinar y fundamentar cuestiones de compra. No mide la actuación, el esfuerzo computacional o el éxito de un modelo particular de IA. Una deficiencia no prueba que ningún agente pueda resolver la cuestión por otros medios, y una valoración suficiente tampoco garantiza éxito universal.

## Invariantes del modelo

No se repiten aquí. El procedimiento se subordina a:

- [Arquitectura de evaluación](../../10-model/evaluation-architecture.md) — unidad RI × ámbito, cadena de análisis.
- [Disponibilidad efectiva](../../10-model/effective-availability.md) — puerta binaria 0/1; si 0 → IR = 0 y no se valoran AC.
- [Criterios de aceptación](../../10-model/acceptance-criteria.md) — los seis AC.
- [Propiedades de calidad](../../10-model/quality-properties.md) — P06–P18, sin subpuntuaciones.
- [Sistemas de valoración](../../10-model/scoring-systems.md) — GSC 0/1/2, NE como incidencia; IR/ICI.
- [Ámbitos de evaluación](../../10-model/evaluation-scopes.md) — Contenido, Marcado y Catálogos distribuidos; consumo sin navegación interactiva.
- [Filtros de lectura](../../10-model/reading-filters.md) — el filtro Alfa y el alcance de lectura.

## Principios transversales de ejecución (M01–M12)

**M01 · Fidelidad al RI.** No cambiar la cuestión, el conjunto de entidades, la desagregación ni sus condiciones durante la auditoría. Toda aclaración necesaria debe registrarse y, cuando modifique su significado, tramitarse como revisión del perfil de RI.

**M02 · Neutralidad de respuesta.** Poder responder fundamentadamente «no», «no cumple», «no disponible» o «incompatible» puede satisfacer una cuestión. No confundir la carencia de una característica con la carencia de información sobre ella.

**M03 · Pertinencia funcional.** Incluir contenido por su contribución identificable a la necesidad del RI, no por simple proximidad temática.

**M04 · Cobertura proporcionada.** Explorar lo suficiente para la conclusión que se quiere emitir; exigir más cobertura al afirmar ausencia que al acreditar presencia.

**M05 · Evidencia anterior al juicio.** No asignar el GSC y después buscar ejemplos favorables. Conservar lo observado, evaluar su relevancia y solo entonces decidir.

**M06 · Separación de planos.** Distinguir siempre recurso observado, afirmación comercial, relación sustentada, interpretación del auditor, hallazgo, propiedad afectada y consecuencia para el AC.

**M07 · Suficiencia relativa.** «Suficiente» se determina respecto del contenido y alcance del RI, no respecto de una perfección universal ni de la cantidad total de atributos publicados.

**M08 · Razonamiento justificado.** Admitir reconocimiento semántico, conversiones y derivaciones sustentadas; rechazar conjeturas que suplan estados, entidades, identidades o condiciones comerciales ausentes.

**M09 · No compensación encubierta.** No dar por satisfecho un AC mediante el buen resultado de otro ni sustituir la valoración específica de cada uno por una impresión global.

**M10 · Reexaminabilidad.** La evaluación debe permitir que otro auditor localice la base probatoria, reconstruya las relaciones relevantes y comprenda por qué se adoptó la decisión.

**M11 · Incertidumbre explícita.** No convertir una búsqueda incompleta o una comprobación inconclusa en una ausencia acreditada, una falsedad o un GSC negativo.

**M12 · Portabilidad.** Las reglas se aplican a cualquier modelo de demanda del proyecto. Solo la **necesidad concreta del RI**, el **perfil de interfaz**, los **hechos observados** y la **materialidad de los hallazgos** cambian entre casos.

## Lo que no hace este marco

No construye automáticamente el catálogo de demanda, no determina prioridades o pesos de requisitos, no especifica el sistema de auditoría técnica, no calcula por defecto IR/ICI/TRI, no predice visibilidad, recomendación ni conversión y no impone a toda clase de oferta un inventario idéntico de campos. Estos desarrollos pertenecen a otros niveles del modelo.

## Capas y responsabilidades

| Capa | Establece | No debe hacer |
|---|---|---|
| **Fundamentos** | Definiciones, alcance y arquitectura del estudio. | Resolver por sí sola la ejecución de cada inspección. |
| **Modelo de demanda** | RI, dimensión, objeto, alcance, aplicabilidad, importancia e interfaces pertinentes; perfil de resolución/pertinencia. | Definir valores comerciales particulares de un ecommerce. |
| **Perfil de evaluación** | Entidad/oferta, recurso, ámbito, momento, condiciones y vía de consumo admisible. | Cambiar el contenido informativo exigido por el RI. |
| **Marco operativo general** | Procedimientos, reglas y evidencias válidos para cualquier RI. | Imponer atributos específicos de una categoría. |
| **Agente auditor** | Obtención, localización, comprobación, interpretación, registros y GSC. | Completar hechos ausentes con conocimiento propio o redefinir el RI. |
| **Revisión/calibración** | Comprobar consistencia de reglas, coberturas y anclajes. En la operación, la revisión humana mira solo las NE y las comprobaciones inconclusas (D-186). | Sustituir sin trazabilidad la evidencia del caso original. |

## Cadena de decisión

`RI y ámbito → perfil operativo del RI → recursos permitidos → exploración → candidatos → pertinencia funcional → conjunto pertinente contextualizado → disponibilidad efectiva → comprobación de propiedades → hallazgos por AC → GSC (o NE por incidencia) → validación → expediente e informe`.

En la V1 la cadena se ejecuta en dos fases: disponibilidad de todos los RI por ficha × ámbito y, después, los AC por lotes de RI con disponibilidad 1 ([execution](execution.md#ejecución-en-dos-fases), [D-153](../../30-governance/decisions.md#d-153)).

**La evidencia atraviesa todas las fases.** La búsqueda puede reabrirse si el análisis de AC descubre una relación, contradicción, ausencia aparente o contexto relevante aún no examinado.

### Una cuestión, varias representaciones

Se conserva siempre la procedencia de cada dato o afirmación. **Contenido** no usa el marcado y **Marcado** no usa el contenido como contenido resolutivo ([D-220](../../30-governance/decisions.md#d-220)). En **Catálogos distribuidos** se respeta el perfil, alcance, variante/oferta y momento de distribución examinado.

La auditoría **no consulta fuentes externas** sobre el producto, ni para contrastar: solo la representación del ámbito y reglas generales citadas ([D-154](../../30-governance/decisions.md#d-154)). Lo que el auditor sepa de un producto, una marca o un modelo concretos es una sospecha, que no gradúa.

## Razonamiento permitido

| Permitido | No permitido |
|---|---|
| Reconocer sinónimos, términos de dominio y expresiones equivalentes justificadas. | Seleccionar por asociación temática ilimitada. |
| Relacionar datos de una misma entidad mediante vínculos acreditados. | Suponer identidades porque dos nombres se parecen. |
| Realizar conversiones o cálculos válidos con condiciones conocidas. | Introducir costes, descuentos o estados no publicados para completar un resultado. |
| Refutar en Fiabilidad con reglas generales citadas o imposibilidades físicas o lógicas; anotar como sospecha lo que el auditor sepa de un caso concreto. | Utilizar datos externos como contenido resolutivo de la interfaz auditada, o refutar un dato con lo que el auditor sepa del producto, la marca o el modelo. |
| Reabrir la búsqueda cuando se detecta posible omisión. | Considerar ausencia una búsqueda literal fallida. |
| Declarar NE o fase inconclusa cuando una comprobación no puede hacerse. | Transformar incertidumbre en GSC bajo o alto por intuición. |

## Módulos y orden de lectura

| # | Módulo | Contenido |
|---|---|---|
| 1 | [inputs-outputs.md](inputs-outputs.md) | Contratos de entrada y salida; validación previa. |
| 1b | [filter-alfa.md](filter-alfa.md) | Especificación operativa del filtro Alfa (`alfa/1`) y registro del alcance de lectura con el panel 2026-10. |
| 2 | [ri-profile.md](ri-profile.md) | Perfil operativo del RI (RI-01..09) y plantilla. |
| 3 | [exploration.md](exploration.md) | Exploración y localización (L-01..12). |
| 4 | [relevance.md](relevance.md) | Pertinencia funcional (PF-01..12) y conjunto pertinente (CT-01..10). |
| 5 | [availability-coverage.md](availability-coverage.md) | Disponibilidad efectiva operativa y cobertura (CO-01..09). |
| 6 | [evidence.md](evidence.md) | Protocolo transversal de evidencias (EV-01..15). |
| 7 | [property-checks.md](property-checks.md) | Comprobación de propiedades P06–P18 (PR-01..09). |
| 8 | [ac-guides.md](ac-guides.md) | Guías y anclajes provisionales de los seis AC. |
| 9 | [gsc-decision.md](gsc-decision.md) | Decisión del GSC e incidencias (GSC-01..12), árbol y materialidad. |
| 10 | [execution.md](execution.md) | Secuencia integral OP-01..12, ejecución en dos fases y hoja rápida. |
| 11 | [dossier.md](dossier.md) | Objetos del expediente, informe, diagnóstico y recomendaciones. |
| 12 | [calibration.md](calibration.md) | Casos A–L, matriz de calibración y prueba de aceptación V1. |
| 13 | [qa.md](qa.md) | Validaciones QA-01..15 e incidencias. |
