# Vistas general y particular de la evaluación técnica, y descubribilidad por sitemap

Decisión del usuario del 2026-10-28, tomada en sesión (T-074) tras el triaje de los requisitos técnicos de Web (T-073). La recoge Claude el mismo día.

## Contexto

El usuario planteó dos cosas:

> y otro aspecto que hay que considerar para el descubrimiento. sitemaps.xml
>
> Aprovecho esto para comentar lo siguiente: evaluación técnica con una visión general (aquellos que aplican de forma general) y con una visión particular (aquellos que aplican al caso (pagina de producto, categoria, pagina de contenido, etc))

(Texto original: «y otro aspecto que hay que consideras apra el descubvrimiento. sitemaps.xml […] evaluación técnica con una visión general (aquellos que aplican de forma general) y con una visión particular (aquellos que aplican al caso (paginad e producto, categoria, pagina de contenido, etc))».)

Claude comprobó en origen qué dicen las fuentes sobre los sitemaps:
- sitemaps.org y la guía de Google («Build a sitemap») fijan con must la **forma** de un sitemap publicado: UTF-8, `<urlset>`, `<loc>` obligatorio, URL absolutas de un solo host y de menos de 2048 caracteres, límites de tamaño y escape de entidades.
- Google **recomienda** publicarlo en la raíz, y su lectura de robots.txt dice que el campo `sitemap:` «must be a fully qualified URL».
- **Ninguna fuente exige ni recomienda tener un sitemap.** Google dice que un sitio grande «might need» uno y que «in most cases, your site will benefit». OpenAI, Anthropic y Perplexity no los mencionan.

Después propuso dos vistas, tres formas de marcarlas y tres preguntas.

## Respuesta del usuario

- A «¿Adopto las dos vistas (general por sitio, particular por tipo de página) como concepto del canon, marcadas con un campo en cada requisito (opción A)?»: «Sí, opción A».
  - La opción decía: «Intake con /docs-update (D-161, evaluation-scopes): vista general y particular, tipos de página (ficha de producto, categoría, políticas y contenido, portada). Campo view en el formato y en el validador.»
- A «¿Cómo entran los sitemaps?»: «lo que fijan las fuentes. Pero añado un criterio nuestro. Toda pagina que se audita debe estar en el sitemaps. lo asumo como requisito de descubribilidad.» (Texto original: «lo que fijan las fuentes. Pero añado un crierio nuestro. Toda pagina que se audita debe estar en el sitemaps. lo suamso como requsisito de descubribilidad.»)
- A «¿Vuelve el descubrimiento por enlaces internos a la vista general?»: «No, solo sitemaps».

## 1. Vistas de la evaluación técnica (propuesta aprobada)

| Vista | Qué evalúa | Ejemplos |
|---|---|---|
| **General** | Lo que se evalúa una vez por sitio u origen: sus recursos de sitio y las entidades de nivel de sitio | Robots.txt: estado y forma del fichero, campo `sitemap:` y política por bot. Sitemaps: su forma. En Web Schema.org, la organización y sus políticas (Organization, devoluciones, envíos, logo) |
| **Particular** | Lo que se evalúa en cada página auditada, según su tipo | Ficha de producto: los requisitos de acceso y lectura de Web y los de Product y Offer de Web Schema.org |

- **Tipos de página:** ficha de producto, categoría o listado, políticas y contenido (envíos, devoluciones, contacto, aviso legal), portada.
- Las dos vistas valen para Web y Web Schema.org, y para Catálogos distribuidos cuando tenga perfil (el feed frente al artículo).
- La vista general se acota al descubrimiento y al acceso de las páginas que llevan la información comercial. Sigue sin ser «una auditoría integral del rastreo».
- **Marca:** cada requisito técnico dice su vista y, si es particular, los tipos de página a los que se aplica.

## 2. Sitemaps

- **Lo que fijan las fuentes:** la forma de un sitemap publicado y la del campo `sitemap:` de robots.txt, como requisitos técnicos con la naturaleza que fija cada fuente.
- **Criterio del proyecto:** «Toda página que se audita debe estar en el sitemaps.» Es un requisito de descubribilidad. Ninguna especificación lo pide: lo funda una condición adoptada por el proyecto, como el perfil sin JavaScript (D-156).
- Que el sitio tenga o no un sitemap no es requisito aparte: sin sitemap, ninguna página está en él.

## 3. Enlaces internos

No vuelven. El descubrimiento se limita a robots.txt y a los sitemaps, y el bloque «rastreo del sitio» del triaje de Web sigue fuera.

## 4. Fuera de docs

- **Referencia técnica:** los campos `view` y `page_types` en cada requisito; requisitos fundados en una decisión del canon en lugar de en una especificación; las fuentes de los sitemaps (sitemaps.org, guías de Google).
- **Capture:** congelar robots.txt, los sitemaps (los grandes, por muestreo o búsqueda de la URL) y las páginas de cada tipo.
