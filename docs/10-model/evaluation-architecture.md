---
id: evaluation-architecture
title: Arquitectura del sistema de evaluación
layer: model
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE §5, FUND §5.1-5.2, FUND §12]
---

# Arquitectura del sistema de evaluación

## Definición

> El **modelo de evaluación de calidad informativa** determina en qué grado la información comercial expuesta **en cada interfaz** permite resolver los requisitos informativos pertinentes. La resolución significa poder **determinar y fundamentar una respuesta suficiente** para la entidad, el alcance y las condiciones examinadas. — BASE §5

> La evaluación relaciona **requisitos informativos, criterios de aceptación, propiedades de calidad y evidencias**. Para cada requisito e interfaz se comprueba qué información está disponible, cómo debe interpretarse y qué fundamento ofrece para responder. Los resultados distinguen las limitaciones observadas y su efecto sobre la resolución de la cuestión. — BASE §5

### Dos naturalezas de requisitos

| Naturaleza | Qué se evalúa | Unidad básica |
|---|---|---|
| **Técnica** | Cumplimiento de las condiciones de exposición, implementación y consumo especificadas para cada ámbito, mediante un sistema cuantitativo propio. | **Requisito técnico × ámbito** |
| **Informativa** | Capacidad de la información comercial efectivamente utilizable para determinar y fundamentar una cuestión pertinente, mediante la disponibilidad efectiva y los criterios de aceptación. | **Requisito informativo × ámbito** (≡ × interfaz, [D-010](../30-governance/decisions.md#d-010)) |

## Componentes

| Componente | Función | Canon |
|---|---|---|
| **Modelo de demanda** | Identificar y justificar las cuestiones relevantes para la clase de oferta. | [demand-model](demand-model.md) |
| **Requisito informativo** | Fijar la pregunta, la dimensión, la entidad, el alcance, la aplicabilidad y la importancia relativa. | [demand-model](demand-model.md#requisito-informativo-ri) |
| **Interfaz o ámbito pertinente** | Determinar la representación de información comercial que se examina. | [evaluation-scopes](evaluation-scopes.md) |
| **Disponibilidad efectiva** | Comprobar de forma binaria si existe información pertinente efectivamente utilizable. | [effective-availability](effective-availability.md) |
| **Criterios de aceptación** | Formular juicios diferenciados sobre la capacidad de esa información para resolver la cuestión. | [acceptance-criteria](acceptance-criteria.md) |
| **Propiedades de calidad** | Describir características observables que explican fortalezas y limitaciones. | [quality-properties](quality-properties.md) |
| **Comprobaciones y evidencias** | Sustentar la disponibilidad, las valoraciones y las conclusiones. | [audit-gsc/evidence](../20-methods/audit-gsc/evidence.md) |
| **Sistemas de valoración** | Expresar la satisfacción de los criterios, la resolución de los RI y el cumplimiento técnico. | [scoring-systems](scoring-systems.md) |

## Reglas e invariantes

1. **La evaluación técnica y la informativa tienen unidades, procedimientos y sistemas de valoración propios.** Una incidencia técnica puede afectar a la disponibilidad efectiva, pero un incumplimiento técnico **no determina por sí mismo** una valoración informativa negativa. El **punto de contacto** es la información utilizable para la finalidad del RI, no el grado general de conformidad.
2. **La evaluación informativa se realiza en los tres ámbitos**, cada uno con sus RI pertinentes. Web considera HTML y Schema.org conjuntamente; Web Schema.org, solo el marcado. Sus indicadores no se agregan automáticamente.
3. **Propiedades y criterios se relacionan de muchos a muchos.** Las propiedades **no reciben subpuntuaciones** que se sumen automáticamente.
4. **Las propiedades pertenecen solo al modelo informativo.** La valoración técnica se fundamenta en los requisitos técnicos generales.
5. **Los instrumentos operativos no amplían el modelo.** El desarrollo operativo debe dar instrumentos suficientemente precisos y reproducibles para reconocer información pertinente, comprobar la disponibilidad, examinar las propiedades y justificar los criterios sobre evidencias reexaminables. Los perfiles de RI, las pruebas de pertinencia y las rutas de resolución son apoyos al método: **no introducen nuevos RI, AC, propiedades, indicadores ni escalas** (FUND §12).

## Cadena de análisis informativo

```text
RI y ámbito pertinentes
  → estructura informativa del RI
  → exploración y localización de candidatos
  → determinación de pertinencia funcional
  → información pertinente contextualizada
  → disponibilidad efectiva            (si 0 → IR = 0, fin)
  → análisis de propiedades
  → juicio de los criterios (GSC)
  → resolución del RI (IR)
```

Las comprobaciones y evidencias acompañan **transversalmente** todo el proceso. Pueden exigir ampliar la exploración cuando aparezcan relaciones o contextos relevantes.

## Cadena de justificación de un juicio

```text
información observada → evidencia → interpretación y hallazgo
  → propiedad o relación afectada → consecuencia para el criterio → GSC justificado
```

La síntesis del IR se hace con sus propias reglas. **No se confunde con el juicio sobre un criterio.**

## Distinciones

| Nivel | Pregunta que resuelve | Consecuencia |
|---|---|---|
| **Candidato** | ¿Podría desempeñar una función para el RI? | Se examinan su conexión y contexto. |
| **Pertinencia** | ¿Qué contribución identificable y justificable ofrece? | Se incorpora a la información pertinente. |
| **Disponibilidad efectiva** | ¿Hay al menos una información pertinente que pueda obtenerse y leerse? | Habilita los AC o conduce a **IR = 0**. |
| **Satisfacción del criterio** | ¿En qué grado se cumple la condición específica del AC? | Se justifica el **GSC**. |
| **Resolución de la cuestión** | ¿Puede determinarse y fundamentarse suficientemente la respuesta? | Se expresa en el **IR**. |

## Relacionado

- Procedimiento operativo completo (propuesta V1): [audit-gsc](../20-methods/audit-gsc/README.md).
- Lectura integrada de niveles y salidas: [scoring-systems](scoring-systems.md#lectura-integrada-sin-confundir-unidades).
