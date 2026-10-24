---
id: mpir-corpus-signals
title: MPIR — corpus estructurado y clasificación de señales informativas
layer: method
status: propuesta
version: 1.0
updated: 2026-10-24
sources: [MPIR §6, MPIR §7]
---

# MPIR — corpus estructurado y clasificación de señales informativas

Parte de [MPIR](README.md). Definiciones de los objetos en [concepts-architecture.md](concepts-architecture.md#definiciones-operativas).

## Corpus estructurado: unidad mínima y reglas de segmentación

La unidad mínima recomendada es la **unidad de contenido estructurada y contextualizada**, identificada mediante un ID propio y un localizador reproducible en el recurso original.

No se fija un tamaño textual universal: debe conservarse la **menor unidad que mantenga íntegra la relación informativa que se pretende analizar**. Puede ser una pregunta con su respuesta, una fila con su cabecera de tabla, un filtro con sus opciones o un párrafo junto a sus condiciones de uso.

### Reglas de segmentación

1. Preservar **literalidad** o la representación estructural del contenido original, sin convertir interpretaciones en citas.
2. Mantener el **contexto inmediato** necesario: sección, categoría, productos, variantes, unidades, mercado y condiciones.
3. Conservar las **relaciones entre elementos**; una tabla de compatibilidades no se descompone en valores desvinculados.
4. Admitir unidades compuestas y vínculos entre unidades cuando una relación necesite más de un bloque.
5. Evitar duplicar como evidencias independientes copias idénticas del mismo contenido o plantilla.
6. Registrar el **origen editorial o de terceros** cuando pueda distinguirse.
7. No descartar información por no coincidir con atributos conocidos o códigos semánticos previstos.

### Campos mínimos de una unidad de evidencia

| Grupo | Campos operativos |
|---|---|
| Identificación | `content_unit_id`, `snapshot_id`, `reference_site_id`, `product_class_id`, versión. |
| Localización | URL, tipo de recurso, sección, selector o localizador, orden relativo dentro del recurso. |
| Contenido | Texto literal o estructura preservada (tabla, filtros, pregunta-respuesta, relación), idioma. |
| Contexto | Entidades y vínculos identificables, unidades, alcance de producto/variante/oferta, mercado y momento cuando consten. |
| Captura | Método de recuperación, estado de renderizado, interacción realizada, momento, incidencias. |
| Procedencia | Autoría editorial/tercero si es reconocible, dependencia o duplicación respecto de otra fuente. |
| Control | Estado de extracción, comprobación de integridad, referencia a original y limitaciones. |

Los campos de interpretación (cuestión sugerida, práctica, pertinencia o grado de confianza) se almacenan **en otra capa**, referidos a la unidad original por su ID.

## Clasificación inicial de señales informativas

La siguiente tipología dirige la **observación**, no clasifica automáticamente los futuros requisitos ni define criterios de calidad. Es una taxonomía **abierta y versionable** de señales: un mismo bloque puede recibir varias etiquetas.

| Código orientativo | Tipo de señal | Pregunta de extracción |
|---|---|---|
| `SI-01` | **Cuestión explícita** | ¿Qué pregunta de compra o duda se formula o responde? |
| `SI-02` | **Criterio de selección** | ¿Qué dimensión se utiliza para filtrar, segmentar o elegir? |
| `SI-03` | **Criterio de comparación** | ¿Qué se contrasta entre alternativas, con qué base y para qué decisión? |
| `SI-04` | **Necesidad o contexto de uso** | ¿Qué actividad, problema, condición o situación da significado a la información? |
| `SI-05` | **Relación o compromiso funcional** | ¿Qué vínculo entre características, prestaciones o limitaciones se explica? |
| `SI-06` | **Adecuación o compatibilidad** | ¿Qué correspondencia entre producto, uso, sistema o condición de aplicación se informa? |
| `SI-07` | **Restricción o advertencia** | ¿Qué incompatibilidad, límite o condición excluyente se expresa? |
| `SI-08` | **Cuestión comercial precompra** | ¿Qué aspecto de variantes, precio, disponibilidad, entrega, garantía o devolución se explica para decidir? |

Los **atributos, afirmaciones, valores y relaciones** de producto se capturan aunque no constituyan por sí solos una señal diferencial. Pueden dar soporte a varias señales y a posibles requisitos; el objetivo del MPIR no es duplicar indiscriminadamente el diccionario taxonómico.

## Relacionado

- Interpretación de señales y estados de anotación: [interpretation-transfer.md](interpretation-transfer.md).
- Captura que alimenta el corpus: [sampling-capture.md](sampling-capture.md#qué-se-conserva-en-la-capa-original).
