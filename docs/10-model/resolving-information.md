---
id: resolving-information
title: Información resolutiva
layer: model
status: vigente
version: 1.8
updated: 2026-10-26
sources: [FUND §3.3, INTAKE 2026-10-26-resolving-information, INTAKE 2026-10-26-resolving-information-rules, INTAKE 2026-10-26-resolving-contribution-name, INTAKE 2026-10-26-general-layer-formulation, INTAKE 2026-10-26-general-layer-formulation-2, INTAKE 2026-10-26-general-layer-issues, INTAKE 2026-10-26-general-layer-resolving-approval, INTAKE 2026-10-26-open-issues-resolution]
---

# Información resolutiva

## Definición

> Para cada requisito, los tipos de información comercial (datos, afirmaciones, relaciones o contenidos, en palabras del canon) que pueden contribuir a resolverla, cada uno ligado al componente de la cuestión al que aporta. Límites del canon: es orientativo y no exhaustivo (RI-07); admite otras representaciones (RI-06); no impone formato ni ubicación (PR-06); no son valores esperados. — INTAKE 2026-10-26-resolving-information

«Información resolutiva» es la forma corta de los «tipos de información potencialmente resolutiva» que FUND §3.3 sitúa entre los registros operativos del catálogo; la definición conserva el «potencialmente» ([D-062](../30-governance/decisions.md#d-062)). El catálogo la registra en cada [requisito informativo](demand-model.md#requisito-informativo-ri).

Cada entrada de la lista se llama **aportación resolutiva** ([D-064](../30-governance/decisions.md#d-064)): una clase de información que puede contribuir a responder la pregunta, como el «plazo para desistir o devolver» en `gen/11`. En las citas de las fuentes de D-062 y D-063 aparece como «tipo». No es la **aportación al modelo de demanda** del MPIR (confirmación, ampliación…). Fuera de `resolving-information`, la aportación resolutiva lleva siempre su adjetivo, y la del MPIR, siempre «al modelo de demanda» ([D-075](../30-governance/decisions.md#d-075)).

## Reglas e invariantes

1. **Finalidad.** Sirve para **localizar información pertinente** (ver [núcleo de conocimiento y perfil](demand-model.md#núcleo-de-conocimiento-y-perfil-de-resolución-y-pertinencia)) y para **recomendar** qué información publicar, concretar o fundamentar, entre otras acciones ([recomendaciones](../20-methods/audit-gsc/dossier.md#recomendaciones)). No cambia las reglas de la exploración, la pertinencia, la cobertura ni las recomendaciones de la auditoría, que la usan como apoyo ([D-062](../30-governance/decisions.md#d-062)). La lista no es exhaustiva: revisarla no prueba por sí sola una ausencia (invariante 11).
2. **Contenido de cada aportación.** Cada aportación lleva su componente (la parte de la pregunta a la que aporta), su origen y respaldo (de dónde sale: la ley, la propiedad de referencia, las fichas…) y las tiendas en que se ha observado. Lo observado es solo evidencia, no un peso ni una importancia ([D-063](../30-governance/decisions.md#d-063)).
3. **Nada se retira por no observarse.** Ninguna aportación se retira por no observarse: que nadie la publique no significa que no resuelva, y justamente esas son las que más necesita una recomendación ([D-063](../30-governance/decisions.md#d-063)).
4. **Cada aportación contribuye a un componente de la pregunta.** Una aportación que no contribuye a ninguno no entra, aunque esté próxima al tema (invariante 10: pertinencia ≠ proximidad temática).
5. **La compila el entrenamiento** a partir de cuatro orígenes, como el catálogo ([model-training](model-training.md)). En la capa general, las aportaciones de origen «marco» salen de la ley que es fuente del requisito y las redacta Claude, sin aprobación del usuario, que las revisa cuando lo pide ([D-084](../30-governance/decisions.md#d-084)); el entrenamiento solo le añade las observadas en las fichas, sin tocar sus preguntas ni sus importancias ([D-063](../30-governance/decisions.md#d-063)). Las aportaciones de la capa general que se redactan sin apoyo en la ley se registran como inferidas y provisionales, como en los bloques de categoría ([D-065](../30-governance/decisions.md#d-065)).

### Orígenes

> | Origen | Cómo se obtiene | Quién decide |
> |---|---|---|
> | Marco (capa general) | De la ley que ya es fuente del requisito; por ejemplo, el art. 97.1 j, k y m para gen/11 | Tú; la lista se fija como el resto de la capa general |
> | Referencias | El código extrae los títulos y las descripciones de las propiedades de Amazon (y de sus subpropiedades) y los atributos de Shopify con sus valores. Quien redacta los convierte en tipos ligados a componentes. Ejemplo: `SOFA.sleeping_area_dimensions` trae «Altura del área para dormir: desde el suelo hasta la superficie…» | La redacción, sin juicio de importancia |
> | Fichas reales | El clasificador ya liga cada hecho declarado al requisito que responde (`answers`). Además indicaría qué tipo de la lista es, o propondría uno nuevo ligado a un componente. El entrenamiento acepta un tipo propuesto cuando aparece en dos tiendas distintas y aporta a un componente de la pregunta | Reglas inducidas |
> | Inferida | Información que resuelve, aunque ni las referencias ni las fichas la muestren, como un certificado de ensayo | Quien redacta; queda provisional y marcada como inferida |
>
> — INTAKE 2026-10-26-resolving-information-rules («Tú» es el usuario; «tipo» es la aportación resolutiva, [D-064](../30-governance/decisions.md#d-064))

En los bloques de categoría, la norma que es fuente de un requisito da aportaciones de origen «referencias», con la ley en el respaldo; el marco es solo de la capa general ([D-068](../30-governance/decisions.md#d-068)).

**Mínimo de aceptación: dos tiendas distintas, no dos fichas** ([D-063](../30-governance/decisions.md#d-063)). «Si se contaran fichas, la plantilla de una tienda pesaría como si fueran muchas»: en la muestra, las 31 fichas con hechos de `gen/11` vienen de solo 4 tiendas.

## Distinciones

| Par | Diferencia |
|---|---|
| Información resolutiva frente a **rasgo** | El [rasgo](model-training.md#rasgos) dice qué resuelve la cuestión; la información resolutiva, qué información puede resolverla. |
| Tiendas en que se observa frente a **importancia** | Lo observado es evidencia del uso real; no es un peso ni cambia la [importancia relativa](demand-model.md#importancia-relativa). |
| Aportación resolutiva frente a **valor publicado** | La aportación es la clase de información («plazo»); el valor es lo que publica una tienda («30 días»). |
| Aportación **propuesta desde las fichas** frente a aportación **inferida** | La propuesta desde las fichas entra cuando aparece en dos tiendas distintas y contribuye a un componente; la inferida la escribe quien redacta sin referencia ni observación y queda provisional. Toda aportación, de cualquier origen, registra las tiendas en que se ha observado. |

## Ejemplo mínimo

Datos reales de las ejecuciones v4 y del control (2026-10-26). Las aceptaciones son ilustrativas hasta que el entrenamiento aplique estas reglas. La lista de `gen/11` es el borrador del marco anterior a la división de la capa general: las aportaciones de las letras k y m corresponden hoy a `gen/26` y `gen/27` ([D-065](../30-governance/decisions.md#d-065)), y la lista aprobada está en el catálogo ([D-069](../30-governance/decisions.md#d-069)).

**`cat.sofas-cama/01`, medidas de la cama abierta**

| Aportación resolutiva | Componente | Origen | Tiendas que la publican |
|---|---|---|---|
| largo de la superficie de descanso, con unidad | largo | referencias (`sleeping_area_dimensions.length`) | 1 |
| ancho de la superficie de descanso, con unidad | ancho | referencias (`…width`) | 1 |
| altura desde el suelo hasta la superficie | altura | referencias (`…height`) | 0 |
| equivalencia con un tamaño estándar de cama | largo y ancho | fichas («cama de matrimonio») | 1: propuesta hasta verla en una segunda tienda |
| plano o imagen acotada de la cama abierta | largo, ancho y altura | inferida (provisional) | 0 |

**`gen/11`, desistimiento y devolución** (31 fichas de 4 tiendas)

| Aportación resolutiva | Componente | Origen | Tiendas que la publican |
|---|---|---|---|
| plazo para desistir o devolver | plazo | marco (97.1.j) | 3 |
| canal de devolución (tienda, correo) | condiciones y procedimiento | marco (97.1.j) | 2 |
| reembolso (completo, cuándo) | condiciones | marco (97.1.j) | 1 |
| modelo de formulario de desistimiento | procedimiento | marco (97.1.j) | 0 |
| coste de la devolución a cargo del comprador | coste | marco (97.1.k) | 3 |
| cuándo no procede o se pierde el derecho | excepciones | marco (97.1.m) | 0 |
| remisión a una página de condiciones | condiciones | fichas | 2: se acepta |
| plazo para solicitar el cambio | plazo | inferida: el cambio entra en `gen/11` ([D-085](../30-governance/decisions.md#d-085)); antes se rechazaba por proximidad temática | 2 |

Con esta lista, la auditoría sabe qué buscar y qué aportaciones ha revisado antes de dar una ausencia por probada, y cada aportación que falta en la ficha auditada se convierte en una acción concreta. Los ceros entre tiendas señalan carencias de todo el sector, pero la recomendación se apoya siempre en la deficiencia de la ficha auditada.

## Pendiente

- Aportaciones observadas en las fichas: el campo, la salida del clasificador y las reglas del entrenamiento están implantados y el catálogo registra las listas, pero aún no hay ejecuciones que declaren la aportación de cada hecho.
- Listas de la capa general: las redacta Claude sin aprobación del usuario ([D-084](../30-governance/decisions.md#d-084); las anteriores las aprobó [D-069](../30-governance/decisions.md#d-069)); las que no tienen apoyo en la ley son inferidas y provisionales ([D-065](../30-governance/decisions.md#d-065)).
- Cómo deja de ser provisional una aportación inferida ([OQ-55](../30-governance/open-questions.md)).
- Relación con los componentes y las expresiones de ejemplo del perfil del RI y su uso en la auditoría ([OQ-03](../30-governance/open-questions.md)).

## Relacionado

- [demand-model](demand-model.md): requisito informativo, núcleo de conocimiento y perfil de resolución.
- [model-training](model-training.md): entrenamiento, rasgos y reglas inducidas.
- [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo): formato del catálogo (método).
- [ri-profile](../20-methods/audit-gsc/ri-profile.md) y [dossier](../20-methods/audit-gsc/dossier.md#recomendaciones): perfil del RI y recomendaciones (método).
