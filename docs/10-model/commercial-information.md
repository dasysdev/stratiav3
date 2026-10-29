---
id: commercial-information
title: Información comercial, representación, exposición y calidad
layer: model
status: vigente
version: 1.7
updated: 2026-10-30
sources: [BASE §1, CTX §1, CTX §3, FUND §1.1-1.2, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-minimum-representation-image, INTAKE 2026-10-28-technical-informative-frontier, INTAKE 2026-10-28-minimum-members-structural-formation, INTAKE 2026-10-28-web-implementation-profile, INTAKE 2026-10-28-technical-rate-pages-web-minimum, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Información comercial, representación, exposición y calidad

## Definición

### Información comercial

> La **información comercial** es el conjunto de contenidos, datos, afirmaciones y relaciones mediante los que un ecommerce describe sus productos, variantes, ofertas, vendedores y condiciones de comercialización. Comprende los hechos expresados, su significado, las relaciones entre entidades, su atribución y las circunstancias en las que resultan válidos. — BASE §1

### Representación y exposición

> La **representación** es la forma concreta en que esa información se expresa y organiza en una interfaz; la **exposición** comprende las condiciones bajo las que se publica, distribuye, recupera y consume. Una misma realidad comercial puede disponer de distintas representaciones, con niveles de detalle y funciones diferentes. — BASE §1

| Concepto | Significado en el sistema |
|---|---|
| **Información comercial** | Contenidos, datos, afirmaciones y relaciones que describen la realidad comercial, sus entidades y condiciones. |
| **Representación** | Forma concreta en que esa información se expresa y organiza en una interfaz. |
| **Exposición** | Condiciones bajo las que la información se publica, distribuye, recupera y consume. |

### Calidad

> La calidad se determina por la **capacidad de la información comercial y de sus condiciones de representación y exposición para resolver cuestiones informativas relevantes**, proporcionando respuestas suficientes, interpretables, atribuibles y fundamentadas para la entidad y las condiciones consideradas. — BASE §1

### Dos dimensiones de evaluación

- **Técnica:** condiciones de publicación, acceso, legibilidad, estructura, conformidad y distribución que permiten localizar, recuperar y consumir la información comercial mediante las interfaces pertinentes. — CTX §3
- **Informativa y semántica:** suficiencia, detalle, significado, relaciones, atribución, vigencia, coherencia y fundamento de la información necesaria para resolver las cuestiones relevantes. — CTX §3

La vigencia ya no se juzga como tal: la propiedad P15 · Actualidad está retirada porque no hay forma de evaluarla ([D-123](../30-governance/decisions.md#d-123)). Lo detectable (una fecha de validez vencida, un feed desfasado frente a la web) se cubre con las comprobaciones de [Fiabilidad](acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones) y con la [consistencia transversal](evaluation-scopes.md#consistencia-transversal).

### Mínimo de representación

> El **mínimo de representación** son los datos sin los que no existe una representación de la oferta. Son los que hacen falta para **descubrirla, acceder a ella e identificarla**, según las [funciones informativas de la IA](ai-functions.md). Lo que sirve para **comprender, comparar, evaluar y justificar** es contenido. — INTAKE 2026-10-28-minimum-representation-image

- **Dos tipos** ([D-143](../30-governance/decisions.md#d-143)):
  - datos que llevan un hecho comercial, como el nombre o los identificadores (en Marcado, el SKU; GTIN y MPN quedan fuera por la prueba de universalidad);
  - datos que solo sostienen la representación y no responden a ninguna cuestión: la url, el identificador de la entidad, que el Product esté enlazado a su Offer y la imagen ([D-144](../30-governance/decisions.md#d-144); qué vale lo que muestra: [effective-availability](effective-availability.md#imágenes-lo-que-muestran-y-lo-que-expresan)).
- **Cómo se evalúan:**
  - si existen y están bien formados lo dice la **evaluación técnica** (con el alcance que fija la [frontera general](evaluation-scopes.md#frontera-entre-la-evaluación-técnica-y-la-informativa));
  - los que llevan un hecho comercial los juzga **también la informativa** por lo que transmiten, como cualquier otra información: disponibilidad efectiva y criterios de aceptación;
  - los de sostén, en su papel de sostén, solo los mira la técnica.
- **No es doble cómputo:** cada sistema informa en sus propios términos, y un incumplimiento técnico no descuenta el GSC: solo cuenta su efecto sobre la disponibilidad. Ejemplo (hipotético): si falta el nombre, el requisito técnico queda no satisfecho y, si nada más responde las cuestiones que dependen de él, su disponibilidad es 0.
- **No crea requisitos técnicos:** sus comprobaciones son las de las especificaciones del perfil. En Marcado, name, image y offers son obligatorias en las fichas de comerciante de Google. Si un dato del mínimo no tiene requisito en el perfil de un ámbito, se registra el hueco; no se inventa el requisito.
- **Con la [frontera general](evaluation-scopes.md#frontera-entre-la-evaluación-técnica-y-la-informativa)** ([D-145](../30-governance/decisions.md#d-145)), lo que el consumidor exige ya es técnico. El mínimo sirve para mantener en la técnica los datos del mínimo que el consumidor solo recomienda.
- **Qué datos lo forman** ([D-147](../30-governance/decisions.md#d-147)) sale de dos pruebas:
  1. **Función:** ¿hace falta para descubrir la oferta, acceder a ella o identificarla? Si solo ayuda, es contenido.
  2. **Universalidad:** ¿lo tiene toda oferta a la que se aplica? Si un producto puede no tenerlo legítimamente (sin GTIN, sin marca), su ausencia puede ser un hecho del producto, que resuelve la informativa con un «no» fundamentado: la técnica no puede distinguir «no tiene» de «no lo publica».

  En **Marcado**:

  | Dato | Tipo | Requisitos (`ws-consumer/…`) |
  |---|---|---|
  | url de la oferta | Sostén | `066`; `202` (url del grupo en un sitio de una sola página) |
  | Enlace Product → Offer | Sostén | `001` (obligatorio); `153` |
  | Relación variante ↔ grupo | Sostén | `193` (obligatorio); `032`, `034`, `192` |
  | variesBy (en qué difieren las variantes) | Sostén | `205` |
  | Identificador de la entidad (`@id`) | Sostén | Ninguno: hueco que se registra |
  | Imagen | Sostén | `003` (obligatorio) y su formación ([D-144](../30-governance/decisions.md#d-144)) |
  | Nombre del producto y del grupo | Con hecho | `002`, `150`, `187` (obligatorios) |
  | SKU | Con hecho | `042` |
  | Nombre del vendedor | Con hecho | `339` |

  Quedan fuera, como contenido: GTIN y MPN (gen/03), la marca (gen/02), la descripción, la categoría y los datos legales, de contacto, la url y el logo del vendedor (gen/13, gen/14). En Merchant Center, que pertenece a Catálogos distribuidos, el GTIN es muy recomendado si existe, y el MPN (sin GTIN) y la marca (productos nuevos) son obligaciones condicionales.

  En **Contenido** ([D-168](../30-governance/decisions.md#d-168); ⚠ [OQ-92](../30-governance/open-questions.md#f-evaluación-técnica)):

  > | Dato | Tipo | Fuente |
  > |---|---|---|
  > | url de la página | Sostén | Los requisitos de acceso (200, indexable, sin bloqueo) |
  > | Título del documento (`<title>`) | Con hecho (el nombre) | WHATWG HTML: exactamente un `title` |
  > | URL canónica (`link rel=canonical`) | Sostén | Google Search recomienda su presencia; su forma (en `<head>`, absoluta, sin fragmento, sin canónicas contradictorias) es técnica |
  > | Imagen | Sostén | `og:image` cuando la página usa Open Graph; si no, hueco registrado |
  >
  > - **Open Graph, condicional:** si la página publica alguna propiedad `og:`, lleva `og:title`, `og:type`, `og:image` y `og:url`, bien formadas, y `og:url` coincide con la URL canónica. Sin Open Graph, esos requisitos son NA.
  > - **Fuera del mínimo:** `meta description` (contenido) y el idioma del documento.
  > - **No técnico:** que coincidan `title`, `og:title`, el encabezado principal y el `name` del marcado es un juicio informativo (Fiabilidad dentro del ámbito o consistencia transversal).

  Lectura con [D-220](../30-governance/decisions.md#d-220): el contraste entre `title` o el encabezado y el `name` del marcado solo es consistencia transversal (Contenido ↔ Marcado); `og:title` no forma parte de Contenido.
  >
  > — INTAKE 2026-10-28-technical-rate-pages-web-minimum

## Reglas e invariantes

1. **Información, representación y exposición no son sinónimos.** La representación es una dimensión del objeto de estudio, pero **no sustituye a la información comercial como objeto principal**.
2. **Las dos dimensiones no son equivalentes.** Una interfaz técnicamente conforme puede exponer información insuficiente para responder una cuestión de compra. A su vez, que una respuesta pueda fundamentarse en una interfaz no elimina las limitaciones técnicas o informativas de otra.
3. **Lo que separa ambas dimensiones es el objeto de la pregunta evaluativa:**
   - la técnica examina **cómo se implementa y expone la interfaz** conforme a sus especificaciones;
   - la informativa examina, para una cuestión de demanda concreta, **qué información pertinente puede obtenerse y leerse y qué permite determinar y fundamentar**.
4. **La calidad evaluada es la de la información expuesta**, no la del producto. Una respuesta suficientemente fundamentada puede acreditar tanto la adecuación como la incompatibilidad de una oferta con una necesidad.
5. **La calidad no se mide por acumulación** de atributos ni por cumplimiento formal de un formato.

## Distinciones

| Frente a | Diferencia |
|---|---|
| Calidad del producto | Se evalúa la información sobre el producto, no el producto. |
| Conveniencia para un comprador | Se evalúa si puede determinarse la respuesta, no si la respuesta es favorable. |
| Conformidad técnica | No basta para resolver cuestiones, y su incumplimiento no determina por sí mismo una insuficiencia informativa. Solo cuenta su efecto sobre la información pertinente utilizable. Ver [evaluation-scopes](evaluation-scopes.md#punto-de-contacto-entre-la-evaluación-técnica-y-la-informativa). |
| Cantidad de datos | Más atributos no implica mayor capacidad de resolver las cuestiones pertinentes. |

## Interpretación

Una misma realidad comercial (un producto, sus variantes, una oferta) puede aparecer en varias representaciones: el HTML de la ficha, el marcado Schema.org o el feed de un catálogo. Esas representaciones tienen funciones, alcances y niveles de detalle distintos. Para interpretar información de varias representaciones hay que preservar la identidad de las entidades, el alcance, las condiciones y el momento de cada afirmación. Ver [evaluation-scopes](evaluation-scopes.md#complementariedad-y-coherencia-entre-representaciones).

## Pendiente

- Datos del mínimo de representación en Catálogos distribuidos, al definir su perfil: [OQ-30](../30-governance/open-questions.md#f-evaluación-técnica).

## Relacionado

- [scope](../00-context/scope.md): problema y objeto del estudio.
- [ai-functions](ai-functions.md): qué operaciones de conocimiento debe favorecer la información.
- [demand-model](demand-model.md): las cuestiones que la información debe poder resolver.
- [evaluation-architecture](evaluation-architecture.md): cómo se evalúan ambas dimensiones.
