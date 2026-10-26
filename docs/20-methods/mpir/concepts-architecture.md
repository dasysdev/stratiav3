---
id: mpir-concepts-architecture
title: MPIR — definiciones operativas, arquitectura y modelo lógico
layer: method
status: propuesta
version: 1.1
updated: 2026-10-26
sources: [MPIR §3, MPIR §13, INTAKE 2026-10-26-open-issues-resolution]
---

# MPIR — definiciones operativas, arquitectura y modelo lógico

Parte de [MPIR](README.md).

## Definiciones operativas

| Concepto | Definición dentro del MPIR |
|---|---|
| **Ecommerce referente** | Comercio seleccionado por su pertinencia, experiencia o especialización respecto de una clase, mediante criterios documentados. |
| **Recurso comercial** | Página o recurso del ecommerce examinado: ficha, categoría, guía, comparador, FAQ, selector, etc. |
| **Instantánea original** | Versión preservada del recurso obtenido, con contexto técnico y temporal suficiente para su revisión. |
| **Unidad de contenido estructurada** | Fragmento delimitado del recurso con sus valores, etiquetas, contexto, entidades y relaciones relevantes conservados. |
| **Señal informativa** | Observación contextualizada que sugiere una cuestión, criterio de elección, relación o condición informativa potencialmente relevante. |
| **Práctica informativa observada** | Forma identificable en que el ecommerce utiliza información para describir, orientar, explicar, relacionar, comparar o delimitar una decisión de compra. |
| **Patrón de referencia** | Formulación normalizada de una práctica o necesidad sugerida por una o varias evidencias, preservando variantes y excepciones. |
| **Cuestión candidata de demanda** | Pregunta potencialmente evaluable inferida a partir de un patrón o evidencia, todavía pendiente de normalización y justificación como requisito informativo. |
| **Requisito informativo (RI)** | Cuestión evaluable del modelo de demanda; su validación pertenece a dicho modelo ([definición canónica](../../10-model/demand-model.md)). |

**Diferencia esencial:** el corpus guarda **lo publicado**; las anotaciones semánticas registran **lo interpretado**; el MPIR consolida **prácticas y patrones**; el modelo de demanda define **lo que importa poder conocer**.

## Arquitectura de información

```text
Clase interna y facetas (Taxonomía de clases de producto)
                       |
                       v
      Panel de ecommerce y recursos seleccionados
                       |
                       v
        [A] Corpus de recursos originales
            HTML / DOM / datos admitidos
            procedencia, captura y versiones
                       |
                       v
        [B] Corpus estructurado de evidencias
            bloques, tablas, filtros, FAQ,
            entidades, contexto y relaciones
                       |
                       v
        [C] Capa de señales e interpretaciones
            funciones, prácticas candidatas,
            preguntas sugeridas, incertidumbres
                       |
                       v
        [D] Modelo de Prácticas Informativas
            patrones normalizados entre fuentes
                       |
             contraste con taxonomías
                       v
        [E] Construcción del modelo de demanda
            requisitos informativos justificados
```

Las capas **A, B, C y D** se mantienen diferenciadas y vinculadas por identificadores. La **E** pertenece al proceso posterior de construcción de demanda; el MPIR le suministra evidencias y propuestas, sin aprobar automáticamente requisitos.

## Modelo lógico de datos y trazabilidad

El diseño lógico mínimo separa entidades para que una fuente sustente varios patrones, un patrón reúna múltiples evidencias y una evidencia pueda apoyar distintas cuestiones sin copiarse artificialmente.

| Entidad lógica | Campos clave o relaciones |
|---|---|
| `reference_site` | ID, dominio, tipo de ecommerce, mercado, especialización, justificación de selección, grupo editorial. |
| `observation_plan` | Clase interna/versionada, segmentos, perfiles, periodo, panel, criterios de muestra. |
| `resource_snapshot` | ID, ecommerce, URL, tipo, captura, versión/huella, método, estado, instantánea preservada. |
| `content_unit` | ID, instantánea, localizador, estructura original, contexto, entidades, relaciones, procedencia. |
| `informative_signal` | ID, unidad(es), código(s) SI, interpretación, función, soporte y estado. |
| `reference_practice` | ID, descripción neutral, señales, función y alcance, estado de revisión. |
| `practice_pattern` | ID canónico, prácticas/evidencias, clases, variantes, relaciones, conflictos y versión. |
| `demand_question_candidate` | ID, pregunta candidata, patrón(es), objeto y condiciones, justificación, estado de transferencia. |
| `taxonomy_alignment` | Cuestión/patrón, clase/faceta/atributo taxonómico, tipo de aportación al modelo de demanda, fundamento. |
| `review_log` | Revisor o procedimiento, fecha, decisión, cambios, incertidumbres y soporte. |

**Integración recomendada:** reutilizar los IDs de clases de producto y las correspondencias del [modelo taxonómico](../product-taxonomy/data-model-governance.md#modelo-de-datos-de-referencia-sin-importar-árboles-completos); no crear una segunda clasificación de productos desconectada. Los IDs de prácticas y patrones serán internos y estables, con versiones explícitas cuando cambie su significado.

## Relacionado

- Campos mínimos de una unidad de evidencia: [corpus-signals.md](corpus-signals.md#campos-mínimos-de-una-unidad-de-evidencia).
- Campos de un patrón: [interpretation-transfer.md](interpretation-transfer.md#campos-de-un-patrón-mpir).
