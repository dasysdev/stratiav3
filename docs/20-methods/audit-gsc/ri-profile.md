---
id: audit-gsc-ri-profile
title: Estructuración operativa universal del RI
layer: method
status: propuesta
version: 0.4
updated: 2026-10-29
sources: [GSC0 §4, GSC0 §14.2, FUND §3.6, INTAKE 2026-10-27-hint-fields, INTAKE 2026-10-28-scope-sheet, INTAKE 2026-10-29-oq-review]
---

# Estructuración operativa universal del RI

> **Estado: propuesta V1.** Desarrolla operativamente el **perfil de resolución y pertinencia** que FUND §3.6 plantea como instrumento auxiliar cuya forma definitiva debe concretarse ([modelo de demanda](../../10-model/demand-model.md)).

## Objetivo y límite

Transformar un RI, ya definido en el modelo de demanda, en una **especificación informativa reutilizable** que oriente qué buscar y qué constituye una contribución. **No** convertir el RI en una lista cerrada de campos, formatos, expresiones comerciales o respuestas esperadas.

**El modelo de demanda determina la necesidad de conocimiento. El agente de auditoría la aplica a la información que realmente encuentra.**

## Campos del perfil operativo

El motor de demanda compone el perfil del RI desde el modelo ([D-177](../../30-governance/decisions.md#d-177)). El auditor no rellena los campos que salen del modelo: solo registra hipótesis (RI-09).

| Campo | Regla general | Exigencia en V1 |
|---|---|---|
| `ri_id`, `pregunta` | Conservar identificación y texto exacto. | Obligatorio. |
| `dimension`, `clase_oferta` | Preservar el marco temático; sin inventar nuevas dimensiones. | Obligatorio si figura en el catálogo. |
| `objeto` | Identificar entidad o conjunto sobre el que se pregunta. Sale de la [descripción](../../10-model/requirement-description.md) del requisito (partes 1 y 3). | Automático ([D-177](../../30-governance/decisions.md#d-177)). |
| `hecho_relacion_solicitado` | Expresar qué se debe determinar/fundamentar. | Obligatorio. |
| `componentes_respuesta` | Enumerar conocimientos constitutivos de una respuesta, no campos técnicos. Los componentes y sus aportaciones salen de la [información resolutiva](../../10-model/resolving-information.md). | Automático ([D-177](../../30-governance/decisions.md#d-177)). |
| `desagregacion` | Definir si se responde por producto, variante, oferta, vendedor, condición o combinación. | Obligatorio cuando lo exige el RI. |
| `alcance` | Delimitar el conjunto y sus fronteras. Sale de la descripción del requisito (partes 1 y 3). | Automático ([D-177](../../30-governance/decisions.md#d-177)). |
| `condiciones` | Mercado, canal, ubicación, tiempo u otras restricciones que modifiquen la respuesta. | Cuando procedan; especificar «no determinada» si es necesario aclarar. |
| `aplicabilidad` | Precisar cuándo corresponde examinar este RI. | Obligatorio. |
| `relaciones_resolutivas` | Describir relaciones lógicas necesarias y posibles composiciones/derivaciones. | Recomendado; obligatorio si la respuesta es relacional. |
| `funciones_informativas` | Identificar cómo un elemento puede describir, identificar, relacionar, contextualizar, sustentar o contrastar. | Obligatorio como referencia de búsqueda, ampliable. |
| `expresiones_ejemplo` | Ejemplos de sinónimos, campos y representaciones. Incluye, por ámbito, la localización de la [ficha del ámbito](../../10-model/demand-model.md#ficha-de-ámbito) (en Web Schema.org, las propiedades relacionadas con las aportaciones del RI) ([D-155](../../30-governance/decisions.md#d-155)). | Opcional, nunca excluyente: orienta, no cierra la búsqueda ni decide la pertinencia. |
| `casos_frontera` | Ejemplos de pertinencia parcial, conexión dudosa o proximidad solo temática. Sale de la descripción del requisito (partes 1 y 3). | Automático ([D-177](../../30-governance/decisions.md#d-177)). |
| `ambitos_pertinentes` | Interfaces en las que el RI debe evaluarse: todas, salvo las excepciones de la ficha de cada ámbito, con su fundamento ([D-155](../../30-governance/decisions.md#d-155)). | Obligatorio. |
| `pistas_valoracion` | Pistas de valoración del requisito, ya resueltas en el modelo ([assessment-hints](../../10-model/assessment-hints.md#reglas-e-invariantes)). Se rellena solo desde el modelo; el auditor no lo escribe. | Automático ([D-135](../../30-governance/decisions.md#d-135)). |
| `fundamento_perfil` | Justificar inclusiones, límites y decisiones no explícitas en el RI. | Obligatorio cuando hay interpretación. |

## Procedimiento de elaboración (RI-01 a RI-09)

Si un campo sale del modelo, el auditor no lo reescribe: RI-01 a RI-08 guían cómo lo lee y RI-09 dice qué registra ([D-177](../../30-governance/decisions.md#d-177)).

**RI-01.** Leer literalmente la cuestión; fijar el **hecho o relación solicitados** antes de proponer datos candidatos.

**RI-02.** Identificar **objeto, entidades, granularidad requerida, conjunto, alcance y condiciones**. No equiparar «por variante» a «por modelo».

**RI-03.** Descomponer en el **mínimo conjunto suficiente de necesidades constitutivas**: aquellas sin las cuales no puede interpretarse o fundamentarse la respuesta solicitada. Evitar descomposición en multitud de atributos accesorios.

**RI-04.** Distinguir **componentes sustantivos** de respuesta (hecho o valor solicitado) y **componentes auxiliares** (identificación, vínculo, unidad, marco temporal, condiciones o soporte). Ambos pueden ser pertinentes; no desempeñan la misma función.

**RI-05.** Describir **relaciones necesarias** cuando la cuestión exige atribución, agregación, comparación, conversión o derivación. No imponer que la respuesta exista en una única frase.

**RI-06.** Admitir **representaciones alternativas** si aportan la misma contribución justificable; no condicionar pertinencia a coincidencias de etiquetas ni a un vocabulario único.

**RI-07.** Incorporar ejemplos positivos, parciales y negativos **solo como ayudas de interpretación**; nunca como enumeración exhaustiva. Una lista con «p. ej.» o «…» orienta y no forma componentes. Solo un conjunto declarado (en la pregunta o en la descripción) cuenta para la [Concreción](ac-guides.md#concreción) (regla ratificada por [D-197](../../30-governance/decisions.md#d-197)).

**RI-08.** Separar los casos **no aplicables** de los casos **aplicables pero sin información**. La ausencia de característica no implica ausencia de necesidad de conocimiento si una respuesta negativa puede resolverla.

**RI-09.** Registrar toda hipótesis o ambigüedad que no esté resuelta por la formulación del RI. Si afecta materialmente a la pregunta, remitir a revisión del modelo de demanda antes de emitir valoraciones definitivas.

## Componentes sustantivos y auxiliares

- **Componente sustantivo:** el hecho o valor solicitado por el RI.
- **Componente auxiliar:** identificación, vínculo, unidad, marco temporal, condiciones o soporte necesarios para interpretar o fundamentar el sustantivo.

Resumen de RI-04. Ambos pueden ser pertinentes ([relevance.md](relevance.md)), pero no desempeñan la misma función. La prueba de [Concreción](ac-guides.md#concreción) despliega componentes sustantivos **y** auxiliares (GSC0 §11.2 a).

## Prueba de calidad del perfil

Se acepta para exploración si permite a otro auditor: (i) decir qué se pregunta y a quién; (ii) reconocer una contribución parcial; (iii) distinguir información auxiliar de una respuesta; (iv) excluir conexiones meramente temáticas; (v) localizar expresiones alternativas sin alterar el RI. Si falla alguna comprobación, revisar el perfil antes de la búsqueda dirigida.

## Ejemplo generalizable: disponibilidad por variante

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?»

- **Objeto:** variantes comerciales del modelo.
- **Hecho solicitado:** estado de disponibilidad comercial.
- **Desagregación:** cada variante del conjunto pertinente.
- **Componentes sustantivos:** estado de disponibilidad, explícito o legítimamente derivable, para las variantes del alcance.
- **Componentes auxiliares:** identidad de variantes, correspondencias variante–SKU, relación SKU–estado, momento, oferta y canal cuando determinen el significado del estado.
- **Relación:** `variante → estado comercial`; puede expresarse mediante identificadores intermedios sustentados.
- **Ejemplos de contenido parcial:** «modelo disponible»; listado de variantes sin estados.
- **Ejemplos solo temáticos:** popularidad o capacidad de fabricación sin conexión acreditada con la disponibilidad de esas variantes.

La descomposición se reutiliza para distintas tiendas y representaciones; **los valores publicados no forman parte del perfil teórico del RI**.

## Plantilla de ficha del RI (YAML ilustrativo)

```yaml
ri_id: "RI-XXX"
version_perfil: "borrador-V1"
clase_oferta: "<clase del modelo de demanda>"
dimension: "<dimension>"
pregunta: "<pregunta literal>"
objeto: "<entidad o conjunto>"
hecho_relacion_solicitado: "<necesidad de conocimiento>"
componentes_respuesta:
  sustantivos:
    - "<componente principal>"
  auxiliares:
    - "<identificacion, relacion o contexto necesario>"
desagregacion: "<unidad/entidad del RI>"
alcance: "<conjunto delimitado>"
condiciones: []
aplicabilidad: "<cuando procede el RI>"
relaciones_resolutivas: []
funciones_informativas:
  - "describir"
  - "identificar"
  - "relacionar"
  - "contextualizar"
  - "sustentar_o_contrastar"
expresiones_ejemplo: []
casos_frontera: []
ambitos_pertinentes:
  - "Web"
fundamento_perfil: "<justificacion de decisiones interpretativas>"
pendientes_de_definicion: []
```

Los registros de la auditoría informativa son **JSON validado y versionado**, con el mismo patrón que web-audit ([D-199](../../30-governance/decisions.md#d-199)). Los campos exactos se fijan al implementar el auditor. Hasta entonces, este YAML es solo ilustrativo y no es una lista cerrada de funciones. El perfil se versiona cuando cambian objeto, componentes sustantivos, desagregación, condiciones o aplicabilidad.

## Relacionado

- [Modelo de demanda](../../10-model/demand-model.md) — RI, importancia relativa y perfil de resolución y pertinencia (concepto).
- [exploration.md](exploration.md) — uso del perfil en la exploración dirigida.
