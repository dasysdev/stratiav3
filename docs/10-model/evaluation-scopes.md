---
id: evaluation-scopes
title: Interfaces, ámbitos de evaluación y requisitos técnicos
layer: model
status: vigente
version: 3.0
updated: 2026-10-30
sources: [BASE §3, BASE §3.1, CTX §5, FUND §4, FUND §7.3, FUND §10.4, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-web-schema-technical-framework, INTAKE 2026-10-28-minimum-representation-image, INTAKE 2026-10-28-technical-informative-frontier, INTAKE 2026-10-28-minimum-members-structural-formation, INTAKE 2026-10-28-references-system, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-scope-sheet, INTAKE 2026-10-28-single-consumption-profile, INTAKE 2026-10-28-request-context-and-scripts, INTAKE 2026-10-28-web-implementation-profile, INTAKE 2026-10-28-technical-views-and-sitemaps, INTAKE 2026-10-28-capture-profile-no-js, INTAKE 2026-10-28-technical-rate-pages-web-minimum, INTAKE 2026-10-29-audit-discovery-and-tdm, INTAKE 2026-10-29-spider-no-query, INTAKE 2026-10-29-spider-products-first, INTAKE 2026-10-29-issues-review, INTAKE 2026-10-29-spider-all-categories, INTAKE 2026-10-29-audit-on-the-crawl, INTAKE 2026-10-29-sitemap-canonical-url, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Interfaces, ámbitos de evaluación y requisitos técnicos

## Definición

### Interfaces de exposición

> Las **interfaces de exposición** son los medios técnicos mediante los que el ecommerce publica, estructura y distribuye información comercial para su consulta y utilización por otros sistemas. — BASE §3

### Ámbitos de evaluación

El sistema establece tres **ámbitos de evaluación**. Cada ámbito determina qué información se examina y qué requisitos informativos son pertinentes.

| Ámbito | Información comercial examinada | Áreas de comprobación técnica |
|---|---|---|
| **Catálogos distribuidos** | Información publicada y distribuida mediante feeds y catálogos destinados a plataformas como Google Merchant Center y Meta Commerce. | Generación, transformación, formato, validación, actualización, entrega, sincronización y distribución. |
| **Contenido** (`content`) | El contenido textual del documento web, tal como lo da su [filtro de lectura](reading-filters.md) (Alfa): el título y el texto del cuerpo, también el oculto, y el texto alternativo de las imágenes. Sin el marcado. | Publicación, recuperación, lectura efectiva y presencia del marcado Schema.org (⚠ [OQ-92](../30-governance/open-questions.md#f-evaluación-técnica)). |
| **Marcado** (`markup`) | Información expresada mediante el marcado Schema.org (JSON-LD, microdatos y RDFa) del mismo documento, considerada aisladamente del contenido. | Sintaxis, estructura, vocabularios y conformidad con las especificaciones del marcado. |

> - **Contenido:** el título del documento y el contenido textual de su cuerpo, tal como resultan de analizar la respuesta HTTP con los scripts desactivados, sin el contenido de `<script>` ni `<style>`. Incluye el texto alternativo de las imágenes. No incluye los demás atributos, los metadatos del `<head>` ni lo que solo existe al ejecutar JavaScript.
> - **Marcado:** el marcado Schema.org (JSON-LD, microdatos y RDFa) de la misma respuesta HTTP, considerado aisladamente del contenido.
> - **Ningún ámbito evalúa el HTML entero.** Contenido no usa el marcado y Marcado no usa el contenido.
>
> — INTAKE 2026-10-30-content-and-markup-scopes

- **Nombres** ([D-220](../30-governance/decisions.md#d-220)): Contenido sustituye a **Web** y Marcado, a **Web Schema.org**. Las citas literales anteriores que dicen «Web» o «Web Schema.org» se conservan y se leen como Contenido y Marcado, salvo donde D-220 cambia su sentido. «Contenido» con mayúscula nombra el ámbito; cuando haga falta, «ámbito Contenido».
- **Origen común:** la página web es la interfaz de exposición, el medio técnico del que salen Contenido y Marcado. Los dos leen la misma respuesta HTTP, cada uno con su representación ([perfil de consumo](#perfil-de-consumo-no-interactivo)).

### Requisitos técnicos generales

> Los **requisitos técnicos generales** expresan las condiciones de implementación, publicación, acceso, consumo y distribución aplicables a cada ámbito, según sus especificaciones. — BASE §3.1

- **Contenido:** se comprueban las condiciones técnicas de recuperación y lectura del recurso, incluida la **implementación de marcado Schema.org como requisito técnico** (⚠ [OQ-92](../30-governance/open-questions.md#f-evaluación-técnica)).
- **Marcado:** se examinan los requisitos técnicos específicos del marcado (sintaxis, estructura, conformidad).
- **Catálogos distribuidos:** se examinan generación, formato, validación, actualización, entrega y distribución **por perfil**.

Los evalúa el sistema **web-audit** en Contenido y Marcado, empezando por Marcado. Es solo técnico: no hace la evaluación informativa, que es de la auditoría GSC ([D-129](../30-governance/decisions.md#d-129)).

### Perfil de implementación

> El **perfil de implementación** es el conjunto de especificaciones aplicables respecto del cual se determinan los requisitos técnicos pertinentes de un ámbito y su naturaleza obligatoria o recomendada. — INTAKE 2026-10-27-web-schema-technical-framework

- La naturaleza **obligatoria o recomendada** de un requisito técnico es **relativa al perfil** que la establece. La fija la especificación, nunca el auditor.
- En **Marcado**, el perfil tiene tres niveles:

| Nivel | Especificaciones | Qué fijan |
|---|---|---|
| **Serialización** | JSON-LD 1.1 (con su procesado), Microdata y RDFa 1.1 | Sintaxis y estructura del marcado |
| **Vocabulario** | Schema.org, versión fijada **30.1** | Tipos, propiedades, dominios, rangos y enumeraciones |
| **Consumidor** | Google Search: fichas de comerciante (Merchant listing), variantes de producto, políticas de devolución y de envío, organización y fragmentos de producto (Product snippet) | Lo que exige ese consumidor y la forma de lo que se publica. La presencia de lo que solo recomienda es, en general, apoyo del modelo de demanda, sin ámbito, y localizador en la ficha de Marcado ([frontera](#frontera-entre-la-evaluación-técnica-y-la-informativa), [D-155](../30-governance/decisions.md#d-155)) |

- Schema.org es permisivo por diseño: los rangos son tipos esperados, admite texto donde espera una entidad y no tiene propiedades obligatorias. Por eso las condiciones de sintaxis salen de la serialización, y las propiedades exigidas y recomendadas, de los consumidores. De las recomendadas, su presencia no es un requisito técnico, salvo las partes de la [formación estructural](#frontera-entre-la-evaluación-técnica-y-la-informativa) y los datos del mínimo de representación ([D-145](../30-governance/decisions.md#d-145), [D-147](../30-governance/decisions.md#d-147), [D-148](../30-governance/decisions.md#d-148)).
- La versión del vocabulario se fija y queda registrada con cada resultado. Cambiarla obliga a revisar los requisitos que dependen de ella.
- **Google Merchant Center** pertenece a Catálogos distribuidos. En Marcado solo sirve para la [consistencia transversal](#consistencia-transversal).
- En Marcado no se añaden otros consumidores por ahora; podrían añadirse como perfil nuevo ([D-130](../30-governance/decisions.md#d-130), interpretación adoptada).
- En **Contenido**, el perfil también tiene tres niveles ([D-159](../30-governance/decisions.md#d-159)):

| Nivel | Especificaciones | Qué fijan |
|---|---|---|
| **Protocolo** | HTTP Semantics (RFC 9110), Robots Exclusion Protocol (RFC 9309) y el protocolo de sitemaps (sitemaps.org; [D-162](../30-governance/decisions.md#d-162)) | La respuesta (estado, redirecciones, `Content-Type`, `Content-Encoding`), cómo se leen las reglas de robots.txt y la forma de un sitemap |
| **Documento** | HTML (WHATWG Living Standard: sintaxis, codificación de caracteres, enlaces y errores de análisis), Encoding (WHATWG) y, si la página lo usa, Open Graph ([D-168](../30-governance/decisions.md#d-168)) | La codificación declarada y UTF-8, la sintaxis del documento, la forma de los enlaces, el título y, con Open Graph, sus cuatro propiedades exigidas |
| **Consumidor** | **Google Search**: requisitos técnicos de Search Essentials, enlaces rastreables, robots.txt, meta robots y `X-Robots-Tag`, bloqueo de la indexación, códigos de estado HTTP, redirecciones, tipos de fichero indexables, JavaScript, sitemaps (D-162), la URL canónica (D-168) y las directrices generales de datos estructurados (presencia del marcado). **Operadores de IA**: OpenAI, Anthropic y Perplexity, cada uno con su página de bots | Lo que el consumidor exige o recomienda para rastrear, indexar o recuperar la página: que su bot no esté bloqueado, un 200, contenido indexable y marcado |

> - Como en Web Schema.org, la naturaleza la fija la especificación: un operador de IA da requisito solo donde su página dice must, should o recommend (OpenAI y Perplexity recomiendan permitir en robots.txt su bot de búsqueda; la página de Anthropic describe sus bots y no fija nada).
> - El marcado Schema.org se examina en Web solo por su **presencia**; su sintaxis, estructura y conformidad son de Web Schema.org.
>
> — INTAKE 2026-10-28-web-implementation-profile

- El [perfil de consumo](#perfil-de-consumo-no-interactivo) no da requisitos técnicos propios en Contenido (D-159): las condiciones de la petición son el perfil ([D-157](../30-governance/decisions.md#d-157)); de lo que solo aparece al ejecutar JavaScript, que no es utilizable ([D-156](../30-governance/decisions.md#d-156)), solo es técnico que el documento de la respuesta tenga contenido indexable; y lo que exige operar la página tiene efecto informativo.
- El perfil de Catálogos distribuidos está pendiente.

### Estados del requisito técnico

| Estado | Valores | Tratamiento |
|---|---|---|
| **Satisfacción** | **Satisfecho** · **no satisfecho** | Según la comprobación de su método. |
| **Aplicabilidad** | **No aplicable (NA)** | El requisito no corresponde al perfil o al recurso examinado. Se justifica y se separa de los pertinentes. |
| **Evaluación** | **No evaluable (NE)** | **Incidencia de la auditoría:** una comprobación que no se pudo hacer. No es una puntuación y **no equivale a «no satisfecho»**. |

NE recibe el mismo tratamiento que en la evaluación informativa ([scoring-systems](scoring-systems.md#grado-de-satisfacción-de-criterio-gsc)). El sistema cuantitativo es la [tasa de cumplimiento técnico](scoring-systems.md#tasa-de-cumplimiento-técnico): una sola tasa sin pesos ni umbrales, con su desglose por naturaleza y su cobertura ([D-131](../30-governance/decisions.md#d-131), [D-166](../30-governance/decisions.md#d-166)).

### Vistas de la evaluación técnica

| Vista | Qué evalúa | Ejemplos |
|---|---|---|
| **General** | Lo que se evalúa una vez por sitio u origen: sus recursos de sitio y las entidades de nivel de sitio | Robots.txt: estado y forma del fichero, campo `sitemap:` y política por bot. Sitemaps: su forma. En Marcado, la organización y sus políticas (Organization, devoluciones, envíos, logo) |
| **Particular** | Lo que se evalúa en cada página auditada, según su tipo | Ficha de producto: los requisitos de acceso y lectura de Contenido y los de Product y Offer de Marcado |

> - **Tipos de página:** ficha de producto, categoría o listado, políticas y contenido (envíos, devoluciones, contacto, aviso legal), portada.
> - La vista general se acota al descubrimiento y al acceso de las páginas que llevan la información comercial. Sigue sin ser «una auditoría integral del rastreo».
>
> — INTAKE 2026-10-28-technical-views-and-sitemaps

- Cada requisito técnico dice su vista y, si es particular, los tipos de página a los que se aplica ([D-161](../30-governance/decisions.md#d-161)). Valen para Contenido y Marcado, y para Catálogos distribuidos cuando tenga perfil (el feed frente al artículo).
- **Páginas de una auditoría** ([D-167](../30-governance/decisions.md#d-167); el origen de las fichas lo enmiendan [D-170](../30-governance/decisions.md#d-170) y [D-217](../30-governance/decisions.md#d-217)):

> - **Fichas de producto:** las del encargo, las mismas URL (y la misma instantánea) que la auditoría informativa (enmendada por [D-217](../30-governance/decisions.md#d-217): sin lista del encargo, todas las fichas del universo). **Portada:** siempre.
> - **Políticas y contenido:** siempre: envíos, devoluciones, contacto y aviso legal, localizadas desde la portada y su pie. La que no se localiza se registra como no localizada; no se sustituye por otra.
> - **Categoría o listado:** la inmediata de cada ficha, por sus migas de pan (enmendada por [D-215](../30-governance/decisions.md#d-215): todas las categorías del sitio). Si la ficha no tiene migas, se registra.
> - **Recursos de la vista general:** robots.txt y los sitemaps (los declarados en robots.txt o, si no hay ninguno, `/sitemap.xml`; con sus índices y gzip). Todo se captura con el perfil de auditoría.
>
> — INTAKE 2026-10-28-technical-rate-pages-web-minimum

- **Universo de la auditoría** ([D-170](../30-governance/decisions.md#d-170), que enmienda D-167 en el origen de las fichas):

> - **Universo de la auditoría:** las páginas de una auditoría se descubren por la unión del rastreo del sitio y de sus sitemaps.
> - **Rastreo:** parte de la portada y sigue los enlaces `<a href>` del documento de la respuesta HTTP sin ejecutar JavaScript (enmendada por [D-173](../30-governance/decisions.md#d-173) y [D-204](../30-governance/decisions.md#d-204): solo las URL sin parámetros, salvo la paginación). Los enlaces `nofollow` se siguen y se registran.
> - **Los enlaces solo descubren:** no se valoran ni se auditan los enlaces ni la rastreabilidad.
> - **Fuera del universo:** lo que no se descubre se considera no rastreable.
> - **Fichas auditadas:** salen del universo descubierto.
> - **Un solo proceso:** el rastreo usa el perfil de auditoría y captura cada página en la misma visita que la descubre.
>
> — INTAKE 2026-10-29-audit-discovery-and-tdm

- **URL con parámetros** ([D-173](../30-governance/decisions.md#d-173)):

> - **Rastreo:** la araña solo rastrea URL sin parámetros (query) (enmendada por [D-204](../30-governance/decisions.md#d-204): salvo la paginación). Los enlaces con parámetros no se siguen; se cuentan.
>
> — INTAKE 2026-10-29-spider-no-query

- **Paginación y fichas primero** ([D-204](../30-governance/decisions.md#d-204); el orden lo enmienda [D-215](../30-governance/decisions.md#d-215): categoría a categoría):

> 1. **Prioridad de fichas, aprendida en el rastreo** (sin configuración por sitio). La araña confirma una ficha por las señales de su documento: `og:type` `product`, o `Product` en JSON-LD o microdatos. Da prioridad a las URL con la forma de URL de las fichas confirmadas. Después visita los listados que más fichas descubren. Sustituye la lectura «recorrido en anchura» de D-173.
> 2. **Paginación:** «admitir solo paginación». La araña sigue una URL cuyo único parámetro es de paginación y tiene valor numérico (`page`, `p`, `pag`, `pagina`, `pg`). Las facetas (`?q=`, filtros) siguen fuera. Enmienda D-173.
>
> — INTAKE 2026-10-29-spider-products-first

- El orden solo importa si el rastreo se corta: uno completo alcanza las mismas páginas. Las señales de ficha de la araña ordenan; no clasifican el tipo de página del universo.
- **Todas las categorías; categoría a categoría** ([D-215](../30-governance/decisions.md#d-215)):

> 1. **Categorías de la auditoría:** todas las categorías del sitio, no solo la inmediata de cada ficha. Enmienda D-167 (ítem «Categoría o listado»).
> 2. **Orden de la araña:** primero las políticas de D-167, localizadas desde la portada. Después, categoría a categoría: la categoría, toda su paginación y las fichas que listan sus páginas; luego, la siguiente categoría. Enmienda D-204.
>
> — INTAKE 2026-10-29-spider-all-categories

- Lecturas de Claude ([D-215](../30-governance/decisions.md#d-215)): una categoría es un enlace de las migas de una ficha, a cualquier nivel, y cualquier URL con su forma; la paginación sigue mientras la página lista fichas; una categoría capturada antes de saberse que lo era se recorre igual, sin volver a pedirla; después de las categorías van las fichas halladas en otras páginas, las formas de URL aún no capturadas y el resto.

- Una URL con parámetros (salvo la paginación) no entra en el universo por el rastreo; puede entrar por los sitemaps. Lecturas de Claude ([D-173](../30-governance/decisions.md#d-173)): solo enlaces `http` y `https` del host de inicio y el host final de la portada; no se siguen los recursos que no son páginas (por su extensión); un bloqueo para el rastreo. La cobertura queda incompleta por el tope, un bloqueo, una reserva, una interrupción o páginas con error cuyos enlaces no se leyeron; no por una exclusión de robots.txt ni por un 404.
- Lecturas de Claude ([D-170](../30-governance/decisions.md#d-170)):
  - El encargo sigue eligiendo las fichas auditadas, ahora entre las del universo; sin lista del encargo, se auditan todas ([D-217](../30-governance/decisions.md#d-217)).
  - «No rastreable» es un hecho registrado, no un estado. Como toda ausencia, exige cobertura (por analogía con [effective-availability](effective-availability.md#reglas-e-invariantes), regla 5): solo se afirma si el rastreo terminó completo. Si quedó incompleto, se registra su cobertura.
- **Auditoría sobre el rastreo** ([D-217](../30-governance/decisions.md#d-217)):

> 1. **Sobre el rastreo:** las páginas de una auditoría (D-167) se eligen sobre el resultado del rastreo, con la instantánea de su visita. La auditoría no pide nada al sitio. Una página de D-167 que el rastreo no capturó se registra y no se audita.
> 2. **Fichas sin lista del encargo:** se auditan todas las fichas del universo. Enmienda D-167 (ítem «Fichas de producto»).
>
> — INTAKE 2026-10-29-audit-on-the-crawl

- Lecturas de Claude ([D-217](../30-governance/decisions.md#d-217)):
  - El rastreo lee los sitemaps después de la portada. Al final captura una vez las URL de los sitemaps que no alcanzó, aunque lleven parámetros. Registra sus enlaces y no los sigue.
  - Una URL de los sitemaps que es la URL, la URL final o la canónica de una página del rastreo es esa página.
  - Cada URL del universo registra si el rastreo la alcanzó, si está en los sitemaps y su tipo de página. «No» solo se afirma con la cobertura completa; si no, queda indeterminado.
  - El tipo (portada, política, ficha, categoría u otra) se decide por varias señales, no solo el marcado. Lo dudoso queda sin tipo; también lo no capturado, lo que no es HTML y lo de otro host. Las señales de cada tipo, en D-217.
  - Las categorías auditadas son todas las del universo, sin su paginación, y la inmediata de cada ficha.
  - Una ficha del encargo fuera del universo no se audita. Se registra como no alcanzada solo si el rastreo terminó completo.
  - Un rastreo parado por una reserva TDM no se audita.
- **Reserva de minería de textos y datos** ([D-171](../30-governance/decisions.md#d-171)): antes de capturar ninguna página de una auditoría, se comprueba si el sitio tiene reserva. Si la hay, no se captura nada: el proceso para y avisa. Los demás procesos de captura siguen [D-042](../30-governance/decisions.md#d-042).
- **Descubribilidad** ([D-162](../30-governance/decisions.md#d-162)): «Toda página que se audita debe estar en el sitemaps» es un requisito obligatorio que funda una **condición del proyecto**, porque ninguna especificación lo pide. Sin sitemap, ninguna página está en él. La URL que se busca es la canónica que declara la página; sin canónica, su URL final; con varias distintas, la comprobación queda NE. De los sitemaps publicados, su forma la fijan las fuentes. Los enlaces internos no se auditan: solo descubren las páginas, y este es el único requisito que se valora del descubrimiento ([D-170](../30-governance/decisions.md#d-170)).

## Reglas e invariantes

1. **Contenido y Marcado leen representaciones distintas** del mismo documento: Contenido no incluye el marcado, y Marcado no incluye el contenido. Sus resultados se mantienen **diferenciados** y **no se suman ni se promedian** ([D-220](../30-governance/decisions.md#d-220)).
2. **Contenido** examina solo el contenido textual que da su [filtro de lectura](reading-filters.md). **No usa el marcado para completar respuestas.**
3. **Marcado** examina solo la representación estructurada. **No usa el contenido para completar respuestas.**
4. Cada ámbito tiene su propio conjunto de requisitos informativos pertinentes, derivados del catálogo del [modelo de demanda](demand-model.md). **Un ámbito no es defectuoso por omitir una cuestión que no le corresponde exponer** según su función y alcance. El conjunto sale de componer el modelo, que es uno, con la [ficha del ámbito](demand-model.md#ficha-de-ámbito): todo RI es pertinente salvo las excepciones fundamentadas en la función del ámbito; la falta de una propiedad o un campo no es motivo ([D-155](../30-governance/decisions.md#d-155)).
5. La evaluación técnica usa un **sistema cuantitativo propio**, independiente de la evaluación de calidad informativa. Las [propiedades de calidad](quality-properties.md) pertenecen **exclusivamente** al modelo informativo y no son unidades de evaluación técnica.
6. La revisión de requisitos técnicos **no depende** de haber seleccionado antes una pregunta del catálogo de demanda.
7. Para cada requisito técnico se documentan:
   - el ámbito;
   - la especificación aplicable, o la condición del proyecto que lo funda ([D-162](../30-governance/decisions.md#d-162));
   - su vista y, si es particular, sus tipos de página ([D-161](../30-governance/decisions.md#d-161));
   - su naturaleza **obligatoria o recomendada**, según su [perfil](#perfil-de-implementación);
   - el método de comprobación;
   - la evidencia;
   - los [estados](#estados-del-requisito-técnico) de satisfacción, aplicabilidad y evaluación.

## Fuentes de los requisitos técnicos

1. Un requisito técnico lo fundamenta una **especificación aplicable** (de serialización, de vocabulario, de protocolo, de documento o de un consumidor, según el perfil del ámbito; [D-159](../30-governance/decisions.md#d-159)) o, por excepción, una **condición del proyecto** adoptada en el canon, que fija su naturaleza ([D-162](../30-governance/decisions.md#d-162)). Las demás fuentes tienen otra función:

| Clase | Ejemplos | Función |
|---|---|---|
| Instrumento del sistema | SHACL, PROV-O | Sirven para construir el auditor (perfiles como restricciones, procedencia de las evidencias); no son condiciones que deba cumplir el ecommerce. |
| Principios generales | W3C Data on the Web Best Practices | Orientan; no dan requisitos comprobables de una ficha. |
| Método de comprobación | Schema Markup Validator, Rich Results Test | Sirven para comprobar y calibrar; no son fuente de criterios ni equivalen a calidad informativa. |
| Práctica de terceros | Skills de auditoría SEO | Listas de errores frecuentes, sin autoridad. |
| Antecedente histórico | GS1 SmartSearch (2015) | Solo contexto. |
| Datos comerciales distribuidos | Merchant Center | Catálogos distribuidos y consistencia transversal. |

2. Un requisito técnico expresa **una sola condición comprobable**.
3. Cada requisito técnico **cita literalmente** su especificación: fuente, sección y versión congelada ([D-132](../30-governance/decisions.md#d-132)). El que funda una condición del proyecto nombra su decisión.
4. **Referencia técnica:** vive en `web-audit/reference/`, como datos y fichas gobernados por el canon, igual que el catálogo de bloques del modelo de demanda. Reúne una ficha por fuente con citas literales y los requisitos técnicos, con los campos de la regla 7, su perfil y su cita. Las fuentes congeladas por versión (fuera de git) viven en `references/`, la custodia común de las fuentes externas de todos los sistemas; la referencia las cita a su versión fijada (enmendada por [D-149](../30-governance/decisions.md#d-149)).
5. Los requisitos técnicos los **deciden los agentes**, siempre con cita; el usuario los revisa si lo pide. Una skill los crea y los mantiene (añadir una fuente, actualizar ante una versión nueva, validar) y no crea conceptos, estados, pesos ni fórmulas: si le falta algo, va al intake ([D-133](../30-governance/decisions.md#d-133)).
6. La auditoría GSC puede consultar la referencia para **interpretar** el marcado. Eso no convierte los requisitos técnicos en criterios informativos ([D-129](../30-governance/decisions.md#d-129)).

## Perfil de consumo no interactivo

En Contenido y Marcado, el perfil de consumo no interactivo debe precisar **qué información puede recuperarse y leerse sin operar la página**. Cuando sea relevante, se documenta si la exposición de los datos depende de ejecutar JavaScript. Esa circunstancia **no se convierte en una prohibición técnica universal** desligada de las vías de consumo definidas.

**Perfil de consumo de Contenido y Marcado** ([D-151](../30-governance/decisions.md#d-151), enmendada por [D-156](../30-governance/decisions.md#d-156) y [D-220](../30-governance/decisions.md#d-220)): un solo perfil. La **respuesta HTTP del recurso, sin ejecutar JavaScript** ni operar la página (en [capture](../../capture/README.md), `response.html`). Cada ámbito lee de ella su representación: Contenido, la salida del [filtro Alfa](reading-filters.md#alfa-el-filtro-del-ámbito-contenido); Marcado, el marcado Schema.org (JSON-LD, microdatos y RDFa).

> vamos dejar solo un perfil que no ejecuta js y utiliza todo el DOM […]. Nos basamos en que es más compatible y preferible generalmente que la información no dependa de ejecución de javascript (aunque algunos sistemas sí puedan leerla). Es una condición que decidimos adoptar ahora. — INTAKE 2026-10-28-single-consumption-profile (enmendada por [D-220](../30-governance/decisions.md#d-220): cada ámbito lee su representación, no todo el documento)

Es una condición adoptada, no una afirmación de que ningún sistema ejecute JavaScript. Lo que solo aparece al ejecutarlo, incluido el marcado inyectado, no es utilizable bajo este perfil, y su efecto se refleja en la disponibilidad efectiva. **Navegador real que no ejecuta JavaScript** ([D-157](../30-governance/decisions.md#d-157)): navegador real, para evitar bloqueos, con este contexto de petición:

| Parámetro | Valor |
|---|---|
| Estado | Limpio por ficha: un contexto de navegador nuevo por ficha, sin cookies, almacenamiento ni caché de ningún sitio ([D-163](../30-governance/decisions.md#d-163)); nunca se acepta un banner. Un desafío es una incidencia, no una ausencia. |
| `Accept-Language` | `es-ES`, registrado en la ficha. |
| IP de origen | España, con país y ASN registrados (no se comprueban: [D-163](../30-governance/decisions.md#d-163)); sin proxies. |
| User agent | El real del navegador ([D-042](../30-governance/decisions.md#d-042), [D-046](../30-governance/decisions.md#d-046)). |
| robots.txt | Se registra qué permite a cada bot de IA y de buscador, como hecho técnico; no afecta al GSC. |
| Sondas | Ninguna: si un cliente vende fuera de España, perfil nuevo. |

**Representación de cada ámbito** (enmienda la frontera del documento de [D-157](../30-governance/decisions.md#d-157)): en Contenido cuenta lo que da el filtro Alfa; en Marcado, el marcado Schema.org (de los scripts, solo `application/ld+json`). Los datos de los demás scripts (estado de la aplicación en JSON, variables de JavaScript) **no son información**: no dan disponibilidad ni sirven de base a los AC, y solo se registran como hallazgo de diagnóstico si el dato existe ahí pero no se publica. El motor de captura cumple «no ejecuta JavaScript» desactivándolo en el navegador: un desafío que lo exige no se pasa y queda como incidencia ([D-163](../30-governance/decisions.md#d-163)).

Puede revisarse de forma auxiliar la política de acceso para sistemas automatizados y la existencia de bloqueos efectivos, cuando afecten a las vías examinadas. Eso **no** constituye una auditoría integral del rastreo, la infraestructura o la seguridad.

## Punto de contacto entre la evaluación técnica y la informativa

La comprobación informativa **no reproduce** los controles técnicos. Atiende a la exposición técnica solo por sus **consecuencias para el RI examinado**: si la información pertinente puede obtenerse y leerse efectivamente con el perfil de consumo definido. Ver [effective-availability](effective-availability.md).

- La conformidad técnica general **no sustituye** a esta comprobación contextual.
- Una incidencia técnica **no determina automáticamente** una insuficiencia informativa.
- Si un factor técnico (formato, marcado, transformación, validación, distribución, mecanismo de acceso) impide consumir la información pertinente, su **consecuencia informativa** se refleja en la disponibilidad efectiva. La **causa** y el incumplimiento se documentan en el expediente técnico.
- Los datos del [mínimo de representación](commercial-information.md#mínimo-de-representación) se examinan en la técnica, que dice si existen y están bien formados (en Marcado, los de la [lista del mínimo](commercial-information.md#mínimo-de-representación), [D-147](../30-governance/decisions.md#d-147)). Los que llevan un hecho comercial se examinan también en la informativa, por lo que transmiten; los de sostén, solo en la técnica ([D-143](../30-governance/decisions.md#d-143)).

**Ejemplo:** una incidencia de marcado Schema.org puede ser relevante para la conformidad técnica. No afecta a **Contenido**, que no lee el marcado. En **Marcado** hay que comprobar qué información pertinente del marcado puede utilizarse.

### Frontera entre la evaluación técnica y la informativa

Se formula para el perfil de Marcado; la de Contenido, [al final de esta sección](#en-contenido); la de Catálogos distribuidos sigue en [OQ-30](../30-governance/open-questions.md#f-evaluación-técnica).

> - **Evaluación técnica:** cómo está construido lo que se publica, más la presencia de lo que el consumidor **exige**.
> - **Evaluación informativa:** si se publica lo que el consumidor solo **recomienda**, como cualquier otra cuestión del modelo de demanda: disponibilidad efectiva y criterios de aceptación.
> - **El criterio es la naturaleza que fija la especificación** (obligatoria o recomendada), no un juicio del auditor. Vale igual en el primer nivel y en lo anidado.
>
> — INTAKE 2026-10-28-technical-informative-frontier

- **Lo técnico** ([D-145](../30-governance/decisions.md#d-145), [D-148](../30-governance/decisions.md#d-148)) son tres categorías y dos presencias:
  - sintaxis y vocabulario;
  - acceso y exposición;
  - **formación estructural**, que incluye la forma del valor (formatos, códigos, enumeraciones, cardinalidad), también la de lo recomendado;
  - presencia de los datos exigidos de primer nivel (name, image y offers del Product; precio y moneda de la Offer). Lo exigido incluye lo condicional, con la condición como aplicabilidad del requisito: en la referencia, 169 obligatorios del consumidor, 9 universales y 160 condicionales ([D-147](../30-governance/decisions.md#d-147));
  - presencia de los datos del mínimo de representación.

> **Formación estructural** (técnica): cuando se publica una estructura,
> 1. tiene las partes que el consumidor **exige** para ella;
> 2. tiene las partes sin las que un valor publicado **no se puede interpretar**: la unidad del peso, la escala de una valoración (`bestRating`/`worstRating`), el sistema de tallas, la moneda de un precio unitario;
> 3. sus partes son **coherentes entre sí**: con `doesNotShip` no hay tarifa; con devolución gratuita no hay importe de devolución.
>
> Las partes que solo **añaden otro hecho** (tipo de reembolso, tarifa de reposición, tiempo de preparación de un servicio de envío) son presencia de lo recomendado → informativa.
>
> — INTAKE 2026-10-28-minimum-members-structural-formation

- La estructura puede ser opcional y estar incluida: lo que cuenta es que, si se publica, no quede incompleta. Ejemplo con el envío en la oferta:
  - sin `shippingDetails` (recomendado): no es un defecto técnico; la informativa juzga si el ámbito responde al coste y al plazo del envío;
  - con `shippingDetails` y sin `deliveryTime`, que Google exige dentro de esa estructura (`ws-consumer/105`): técnico, estructura incompleta; la informativa ve además su efecto en el plazo de entrega (gen/08);
  - con todas las partes exigidas y sin `handlingTime` (recomendado, `122`): solo informativo, es un hecho más sobre el plazo.
- Lectura de [D-148](../30-governance/decisions.md#d-148): la coherencia entre partes recoge también las reglas de estructura del marcado de la página, como una sola moneda (`ws-consumer/147`, `174`) o URL distintas por variante (`200`).
- **Doble lectura, solo en lo exigido.** Si falta el precio, la técnica dice que el consumidor lo exige y falta; la informativa, que la cuestión no tiene respuesta en el ámbito. No es doble cómputo: la incidencia técnica y su efecto sobre la disponibilidad se registran por separado (punto de contacto, arriba).
- **Mínimo de representación:** mantiene en la técnica los datos del [mínimo](commercial-information.md#mínimo-de-representación) que el consumidor recomienda sin exigir; en Marcado, nueve requisitos ([D-147](../30-governance/decisions.md#d-147)).
- **Lo recomendado** pasa al modelo de demanda como apoyo «referencias», sin ámbito, y a la ficha de Marcado como localizador ([D-155](../30-governance/decisions.md#d-155)): ver [demand-model](demand-model.md#propiedades-recomendadas-de-marcado).

#### En Contenido

> - **Técnico:** el acceso y la recuperación del recurso, la forma de la respuesta y del documento, y la presencia de lo que el consumidor exige para la página (no bloqueado, 200, contenido indexable, marcado). Las recomendaciones del consumidor sobre el acceso y la forma (permitir un bot, enlaces `<a href>`) son técnicas: no añaden un hecho comercial.
> - **Informativo:** si la información comercial pertinente está en el documento y se puede leer (disponibilidad efectiva y AC).
>
> — INTAKE 2026-10-28-web-implementation-profile

- Es la lectura de D-145 en Contenido ([D-160](../30-governance/decisions.md#d-160)): que haya contenido indexable es técnico; que ese contenido sea la información comercial, no. La «lectura» de las áreas técnicas de Contenido (tabla de [ámbitos](#ámbitos-de-evaluación)) es la del documento: tipo, codificación y análisis.
- El [mínimo de representación](commercial-information.md#mínimo-de-representación) de Contenido (⚠ [OQ-92](../30-governance/open-questions.md#f-evaluación-técnica)): url, título y URL canónica, y la imagen con Open Graph ([D-168](../30-governance/decisions.md#d-168)).

## Complementariedad y coherencia entre representaciones

- La información de distintas representaciones puede ser complementaria. Para interpretarla hay que preservar la **identidad de producto, variante, oferta o vendedor**, el alcance comercial, las condiciones y el momento de cada afirmación.
- Una discrepancia solo es una **contradicción material** cuando las afirmaciones se refieren a **la misma realidad comercial bajo condiciones y momentos comparables**.
- **La coincidencia entre representaciones no demuestra por sí sola la exactitud** de lo afirmado.
- Contenido y Marcado **no comparten información examinada**: leen representaciones distintas del mismo documento y ninguno sustituye al otro. Desaparece la «evaluación conjunta del recurso web» de FUND §4.1 y §4.3 ([D-220](../30-governance/decisions.md#d-220)).
- Una limitación observada en Marcado **no implica** una limitación en Contenido, ni al revés. Los resultados se documentan por separado, conservando la procedencia de cada afirmación; las discrepancias entre los dos ámbitos son [consistencia transversal](#consistencia-transversal).

### Consistencia transversal

> La consistencia se puede evaluar para cada ámbito y, a nivel transversal, «adquiere una nueva dimensión de análisis». **Unidad:** RI × par de ámbitos. **Forma:** hallazgos sin escala; por RI y par de ámbitos, hecho, valores, momento, materialidad, y si la diferencia es legítima (p. ej., un precio propio de un canal, declarado). Una diferencia legítima y declarada no es incoherencia. **No modifica el GSC de ningún ámbito ni se agrega.** — INTAKE 2026-10-27-ac-applicability-and-reliability

- **Lo que aporta:** lo que el juicio por ámbito no puede expresar. Ejemplo (hipotético): un marcado coherente consigo mismo a 89 € en una página que dice 79 €; quien solo lee el marcado no puede saberlo. Lo mismo, un feed desfasado.
- **Por qué no toca el GSC:** no se puede saber cuál de los dos lados está mal, y mezclarlos rompería la separación de Contenido y Marcado. La consistencia **dentro** de cada ámbito sí cuenta en su Fiabilidad ([acceptance-criteria](acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones)).
- **Pares:**
  - Catálogos distribuidos ↔ Contenido;
  - Catálogos distribuidos ↔ Marcado;
  - Contenido ↔ Marcado: el único par de la V1; el contraste entre el contenido y el marcado ya no es coherencia dentro de un ámbito ([D-220](../30-governance/decisions.md#d-220));
  - entre perfiles de Catálogos distribuidos (Google, Meta).
- **Condiciones de operación:** captura de los ámbitos en un momento comparable; identidad de la entidad entre ámbitos (GTIN, SKU o `item_group_id` frente a URL y variante); acceso al feed.
- Es una dimensión de análisis, no un indicador ni una escala ([D-124](../30-governance/decisions.md#d-124)). Un estado cualitativo por RI queda pendiente ([OQ-67](../30-governance/open-questions.md)).

## Distinciones

- **Interfaz** y **ámbito de evaluación**. En la unidad de evaluación (RI × interfaz / RI × ámbito) y en los sistemas de valoración son **sinónimos** ([D-010](../30-governance/decisions.md#d-010)). Fuera de ese contexto, «interfaz de exposición» designa además el medio técnico mediante el que se publica la información. En texto nuevo se prefiere «ámbito» para la unidad evaluada.
- **Contenido** frente a **texto visible** y frente a **contenido principal**: Contenido incluye lo oculto, la cabecera, el menú y el pie; el texto visible depende de CSS y el contenido principal descarta regiones ([reading-filters](reading-filters.md#distinciones)).
- **Legibilidad técnica u operativa** frente a **P09 · Claridad** y **P10 · Estructuración semántica**. Ver [quality-properties](quality-properties.md#lectura-efectiva-frente-a-propiedades-semánticas).

## Pendiente

- El perfil de Catálogos distribuidos. Ver [OQ-30](../30-governance/open-questions.md#f-evaluación-técnica).
- Los requisitos técnicos del perfil de Contenido que miran el documento entero (presencia del marcado, Open Graph, URL canónica). Ver [OQ-92](../30-governance/open-questions.md#f-evaluación-técnica).

## Relacionado

- [effective-availability](effective-availability.md)
- [reading-filters](reading-filters.md)
- [evaluation-architecture](evaluation-architecture.md)
- [scoring-systems](scoring-systems.md#tasa-de-cumplimiento-técnico)
