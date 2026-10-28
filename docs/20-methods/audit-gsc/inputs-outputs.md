---
id: audit-gsc-inputs-outputs
title: Contratos de entrada y de salida
layer: method
status: propuesta
version: 0.8
updated: 2026-10-28
sources: [GSC0 §3, GSC0 Anexo D, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-scope-sheet, INTAKE 2026-10-28-single-consumption-profile, INTAKE 2026-10-28-request-context-and-scripts, INTAKE 2026-10-28-capture-profile-no-js]
---

# Contratos de entrada y de salida

> **Estado: propuesta V1.** Forma parte del [marco operativo GSC](README.md).

## Contrato de entrada mínimo

Antes de ejecutar, deben estar disponibles:

| Entrada | Exigencia mínima | Quién la aporta |
|---|---|---|
| **RI identificado** | ID, redacción exacta, dimensión y clase de oferta. | Modelo de demanda. |
| **Objeto y alcance** | Entidad/es interrogadas, desagregación, condiciones y aplicabilidad. | Modelo de demanda; aclaración de auditoría si procede. |
| **Ámbito pertinente** | Catálogos distribuidos, Web o Web Schema.org. En la V1, Web o Web Schema.org ([D-152](../../30-governance/decisions.md#d-152)). Todo RI del modelo es pertinente salvo las excepciones de la ficha del ámbito; se registra la versión de la ficha ([D-155](../../30-governance/decisions.md#d-155)). | Modelo de demanda compuesto con la [ficha del ámbito](../../10-model/demand-model.md#ficha-de-ámbito). |
| **Perfil informativo del RI** | Núcleo del hecho/relación solicitados y componentes de respuesta; puede elaborarse con el protocolo de [ri-profile.md](ri-profile.md) si no existe. | Modelo de demanda o fase preparatoria controlada. |
| **Caso evaluado** | Ecommerce, oferta/recurso, identificadores disponibles y momento/mercado relevantes. | Configuración de auditoría. |
| **Perfil de consumo** | Qué vías de obtención/lectura están permitidas y qué recursos se incluyen. | Configuración de ámbito. |
| **Soporte de inspección** | Acceso a recursos o instantáneas realmente obtenidos y posibilidad de guardar evidencias. | Entorno de ejecución. |

La **importancia relativa** del RI puede acompañar al expediente, pero **no altera individualmente un GSC**; pertenece al [modelo de demanda](../../10-model/demand-model.md#importancia-relativa) y actúa en niveles superiores de síntesis ([ICI](../../10-model/scoring-systems.md#indicador-de-calidad-informativa-ici)).

### Perfil de consumo

Condiciones bajo las que el recurso se obtiene y lee en un ámbito: vías de obtención/lectura permitidas y recursos incluidos. La modalidad es **sin navegación interactiva**; el perfil documentado determina qué es utilizable, sin establecer una prohibición universal de JavaScript desvinculada de él ([ámbitos de evaluación](../../10-model/evaluation-scopes.md)). Se versiona cuando cambian las representaciones o vías admitidas; no se comparan resultados de distintos perfiles sin advertirlo.

En Web y Web Schema.org hay **un solo perfil**: la **respuesta HTTP sin ejecutar JavaScript** (`response.html` de la ficha congelada en capture), de la que se usa todo el documento, no solo el texto visible ([D-156](../../30-governance/decisions.md#d-156), [evaluation-scopes](../../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo)). Es un navegador real que no ejecuta JavaScript, con estado limpio por ficha, `es-ES`, IP española y el user agent real; los scripts que no son marcado no cuentan ([D-157](../../30-governance/decisions.md#d-157)). En capture es el perfil de captura `audit-es`: JavaScript desactivado y un contexto de navegador nuevo por ficha ([D-163](../../30-governance/decisions.md#d-163)).

## Validación previa de entradas

- Si falta un dato **inferible sin alterar el significado** (por ejemplo, enumerar los componentes explícitos de un RI bien formulado), crear una **propuesta de descomposición** y señalar su procedencia.
- Si falta una decisión que determina el alcance (por ejemplo, «disponibilidad» sin especificar canal cuando el RI lo requiere), **no elegir silenciosamente** una interpretación. Registrar la ambigüedad; continuar únicamente con las partes inequívocas o solicitar definición del modelo de demanda.
- Si no puede delimitarse la entidad, el ámbito o el perfil de consumo, **no emitir un GSC como si la evaluación estuviera completa**. Registrar **bloqueo de preparación** o evaluación inconclusa, sin convertirlo en NA ni NE automáticamente.
- Si el RI no es aplicable a la oferta concreta, registrar **NA del RI** con fundamento. No hay NA de un AC aislado dentro de un RI aplicable, salvo el de Comparabilidad en los requisitos que no son dimensión de comparación ([D-126](../../30-governance/decisions.md#d-126)).

## Contrato de salida mínimo

Cada caso debe producir:

1. Identificación y configuración.
2. Perfil RI utilizado.
3. Recursos y cobertura.
4. Candidatos significativos y decisiones de pertinencia.
5. Conjunto pertinente.
6. Disponibilidad efectiva o estado procedimental inconcluso.
7. Evidencias originales.
8. Hallazgos con propiedades.
9. Valoración **por cada AC** (GSC, o NE por incidencia).
10. Justificación de cada decisión.
11. Limitaciones y controles de validación.

La estructura de registros figura en [dossier.md](dossier.md), [evidence.md](evidence.md) y [gsc-decision.md](gsc-decision.md).

## Unidad evaluada

La unidad básica es **RI × ámbito pertinente**, aplicada a la entidad, oferta, recurso y condiciones concretas de la inspección ([arquitectura](../../10-model/evaluation-architecture.md)). En este contexto, «requisito informativo × interfaz pertinente» (BASE) y «RI × ámbito» son sinónimos ([D-010](../../30-governance/decisions.md#d-010)).

Es admisible procesar varios RI sobre una misma representación obtenida, siempre que cada evaluación conserve su pertinencia, cobertura y GSC **por unidad RI × ámbito** ([execution.md](execution.md)).

## Relacionado

- [ri-profile.md](ri-profile.md) — elaboración del perfil del RI.
- [execution.md](execution.md) — secuencia OP-01..12.
- [qa.md](qa.md) — QA-01 a QA-03 verifican estas entradas.
