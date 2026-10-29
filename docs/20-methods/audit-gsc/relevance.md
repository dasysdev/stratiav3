---
id: audit-gsc-relevance
title: Pertinencia funcional y conjunto pertinente
layer: method
status: propuesta
version: 0.3
updated: 2026-10-30
sources: [GSC0 §6, GSC0 §7, FUND §9.2, FUND §3.6, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Pertinencia funcional y conjunto pertinente

## Distinción rectora

> **Estado: vigente** (FUND §3.6, §9.2). Las definiciones de «relación temática» y «pertinencia informativa» siguen la formulación de GSC0 §6.1 (propuesta V1).

**Relación temática** significa que un contenido guarda alguna asociación con el asunto del RI. **Pertinencia informativa** significa que puede desempeñar una **función identificable y justificable** respecto de una necesidad constitutiva de la cuestión. La primera no basta para acreditar la segunda.

La detección de candidatos debe ser semánticamente amplia; la selección de información pertinente, rigurosa. La prueba de pertinencia **no es la valoración del AC**: un contenido general, incompleto, ambiguo, no desagregado o todavía insuficiente puede seguir siendo pertinente y servir de base para identificar después sus limitaciones de calidad.

Una conexión plausible pero todavía no acreditada se trata como **candidato pendiente de comprobación**; si solo subsiste una asociación temática o una cadena de suposiciones, no se incorpora al conjunto pertinente. No se fija un número máximo de relaciones admisibles: el límite está en la **justificación de cada conexión significativa** y su contribución, no en contar los pasos.

## Prueba obligatoria de pertinencia (PF-01 a PF-03)

Para cada candidato, registrar:

1. **PF-01 · Contribución.** ¿Qué componente de respuesta o necesidad constitutiva del RI puede informar, delimitar o sustentar? Señalar el componente concreto del perfil.
2. **PF-02 · Función.** ¿Aporta el hecho; identifica entidad; establece relación; delimita o contextualiza; sirve de sustento o contraste; o cumple otra función razonada? Nombrar y explicar la función, no solo etiquetarla.
3. **PF-03 · Fundamento.** ¿Qué significado observable, afirmación, vínculo expreso, equivalencia admisible o regla interpretativa sostiene esa contribución? Identificar su evidencia y los supuestos que **no** pueden adoptarse. Si la contribución pasa por una derivación desde otro hecho, aplicar la [prueba de derivación](../../10-model/effective-availability.md#prueba-de-derivación) ([D-120](../../30-governance/decisions.md#d-120)): un atributo por sí solo no es pertinente para una prestación ([D-119](../../30-governance/decisions.md#d-119)).

La clasificación de funciones es **enunciativa, no limitativa**. Toda función adicional debe poder describirse por su contribución concreta y no puede ampliar arbitrariamente el RI.

## Estados procedimentales de candidatos

No son puntuaciones.

| Estado | Condición | Acción |
|---|---|---|
| **Candidato inicial** | Posible contribución aún no analizada. | Examinar función y fundamento. |
| **Pertinente** | Contribución y función justificables, aunque sean parciales. | Incorporar al conjunto pertinente, con evidencia y contexto. |
| **Pendiente de aclaración** | Hay una conexión posible, pero falta comprobar contexto, identidad o relación. | Ampliar dentro del ámbito; registrar incertidumbre si no puede resolverse. |
| **No pertinente** | No hay función justificable para el RI, o solo existe asociación temática/supuestos. | Excluir de la base del RI; documentar descartes relevantes para cobertura. |

Los elementos descartados **no se consideran deficiencias de calidad**. La selección pertinente tampoco acredita por sí misma suficiencia.

## Reglas operativas (PF-04 a PF-12)

**PF-04.** La contribución puede ser **sustantiva, identificadora, relacional, contextual o probatoria**. No exigir que cada fragmento contenga el valor final de la respuesta.

**PF-05.** La afirmación «producto disponible» puede ser pertinente para una pregunta sobre variantes, aunque no permita atribuir correctamente el estado a cada una.

**PF-06.** El significado general de una expresión puede reconocerse por conocimiento lingüístico o del dominio (por ejemplo, `InStock`), pero las **identidades, relaciones y estados comerciales particulares** requieren sustento en las fuentes admitidas.

**PF-07.** No convertir popularidad, capacidad productiva, plazos logísticos u otros factores indirectos en disponibilidad actual sin relaciones comerciales expresas que justifiquen esa conclusión.

**PF-08.** No imponer límites por **número de relaciones o pasos**: comprobar la justificación de cada conexión y su pertinencia final para el RI. No utilizar una escala de grado de derivación.

**PF-09.** Un dato puede quedar como **candidato pendiente**, no pasar por fuerza a pertinente o excluido cuando existe incertidumbre resoluble o falta evidencia.

**PF-10.** Conservar los elementos que permiten reconstruir una relación pertinente: etiquetas, identificadores, sujeto, predicado, objeto, unidades, restricciones, fecha o versión, cuando correspondan.

**PF-11.** Si una información es pertinente para otro RI pero no para este, no importarla como si satisficiera la cuestión actual. Su eventual reutilización pertenece a otra unidad de evaluación.

**PF-12.** La aparición de un elemento nuevo que puede alterar un hallazgo obliga a revisar la selección previa y a actualizar los registros afectados, dejando constancia de la revisión.

## Ejemplo de frontera

**RI:** disponibilidad comercial de cada talla. *(Hipotético.)*

| Contenido | Tratamiento inicial | Justificación |
|---|---|---|
| «Talla 42 → SKU-420» | Pertinente, auxiliar/relacional. | Permite reconocer y vincular una variante. |
| «SKU-420: `InStock`» | Pertinente, sustantivo; requiere comprobar identidad, oferta y momento. | Expresa un estado atribuible a un identificador. |
| «Disponible para compra online» (cabecera de modelo) | Pertinente, parcial. | Informa disponibilidad general, sin desagregación acreditada. |
| «Producto muy vendido» | No pertinente por sí solo. | La popularidad no informa el estado comercial actual. |
| «Producción de 10.000 unidades/mes» | No pertinente por sí solo. | Producción no acredita inventario de una variante. |
| «Reposición prevista el lunes» sin identificar talla/canal | Candidato por aclarar. | Puede delimitar un estado futuro, pero no fundamenta directamente uno actual. |
| «Envío gratuito a partir de 60 €» | No pertinente para este RI. | No contribuye al hecho solicitado. |

## Cierre de selección y candidatos no resueltos

No es necesario resolver toda la información irrelevante del recurso. Sí deben resolverse o explicitarse los **candidatos plausiblemente decisivos** cuya inclusión pudiera cambiar la disponibilidad efectiva o un juicio material de AC.

Si un candidato decisivo no puede comprobarse, registrar su ubicación y causa. **No afirmar una ausencia global ni un GSC definitivo incompatible con esa incertidumbre.** Si ya existe otro elemento pertinente utilizable, la disponibilidad efectiva puede ser 1 aunque continúe una duda que afecte después a un AC.

## Conjunto pertinente

La base informativa de la evaluación es un **conjunto contextualizado de datos, afirmaciones, entidades, condiciones y relaciones**, no necesariamente una colección de párrafos ni una paráfrasis libre del auditor. Puede estar distribuido en varias partes de una representación admitida.

Cada unidad incluida conserva: **contenido literal o valor original, procedencia, localizador, entidad/sujeto, significado atribuible, condiciones, instante y vínculos pertinentes**. Los contextos preservados para entender una evidencia no se convierten automáticamente en contenidos que satisfagan otros componentes del RI.

### Tratamiento (CT-01 a CT-10)

**CT-01 · Normalizar para analizar, no para sustituir.** Pueden prepararse versiones interpretadas de valores, unidades y términos, pero siempre junto al contenido original y la regla usada. La representación transformada no debe reemplazar la evidencia primaria.

**CT-02 · Preservar identidad.** No fusionar producto, variante, oferta y vendedor por similitud de nombres. Utilizar identificadores o relaciones justificadas.

**CT-03 · Preservar alcance.** Asociar cada afirmación con el nivel a que realmente se refiere: modelo, variante, oferta, vendedor, mercado, canal, localidad o momento.

**CT-04 · Preservar condiciones.** Una afirmación sujeta a descuento, localización, fecha, canal o configuración no se generaliza fuera de esas condiciones.

**CT-05 · Relacionar representaciones de forma controlada.** Dentro de un ámbito, combinar afirmaciones solo con conexión suficiente de entidad y contexto. Contenido y Marcado no se combinan entre sí ([D-220](../../30-governance/decisions.md#d-220)). Registrar de qué parte de la representación procede cada afirmación.

**CT-06 · Distinguir equivalencia y contradicción.** Dos valores aparentemente distintos pueden ser compatibles por unidades, periodo, entidad u otras condiciones. No declarar contradicción sin comprobar comparabilidad de alcance y momento.

**CT-07 · Rutas de respuesta.** Cuando la conclusión depende de varios elementos, registrar la sucesión de afirmaciones y conexiones que la fundamenta. No puntuar cantidad de pasos ni dar por publicada una conclusión inferida sin soporte.

**CT-08 · Evitar conocimiento externo sustitutivo.** Puede emplearse una regla aritmética o semántica general válida; no incorporar datos comerciales de otra fuente como si formaran parte de la interfaz examinada.

**CT-09 · No colapsar diferencias de contenido.** Conservar afirmaciones discordantes y variantes alternativas; el resumen informativo del agente no debe ocultar discrepancias.

**CT-10 · Revisión trazada.** Si aparece nueva evidencia, actualizar la interpretación, indicar qué decisión cambió y conservar la referencia a la evidencia que motivó el cambio.

### Ruta de respuesta

Conjunto de afirmaciones y relaciones sustentadas con las que puede reconstruirse una conclusión; **no tiene escala de longitud o esfuerzo**. Una respuesta puede construirse a partir de hechos publicados y relaciones sustentadas: `talla 42 ↔ SKU-420`, `SKU-420 ↔ InStock`. La composición solo es válida si corresponde a la misma entidad comercial y a condiciones y momentos compatibles. Precio base + descuento aplicable + condiciones explícitas pueden permitir un cálculo aritmético válido.

**Regla de cierre:** no se establece una longitud máxima de ruta. Se exige justificar **cada vínculo material para la conclusión** y no usar supuestos comerciales no acreditados. La ausencia de expresión literal no es, por sí sola, una deficiencia informativa.

### Salida de la etapa

El conjunto pertinente debe permitir responder qué elementos contribuyen a qué componente del RI, con qué alcance y soporte; qué candidatos quedan pendientes; y qué partes esenciales todavía no tienen soporte observado. **Es una base para comprobar y valorar, no una respuesta comercial definitiva ni un GSC.**

## Relacionado

- [exploration.md](exploration.md) — origen del inventario de candidatos.
- [availability-coverage.md](availability-coverage.md) — el conjunto pertinente alimenta la disponibilidad efectiva.
- [calibration.md](calibration.md) — casos B e I (derivación válida, popularidad).
