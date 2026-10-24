---
id: product-taxonomy-sources
title: Taxonomía — inventario de fuentes externas y referencias
layer: method
status: propuesta
version: 1.0
updated: 2026-10-24
sources: [TAX §2, TAX §12]
---

# Taxonomía — inventario de fuentes externas y referencias

Parte de [Taxonomía de clases de producto](README.md).

## Shopify: base estructural y vocabulario de atributos

La **Shopify Standard Product Taxonomy** dispone de categorías jerárquicas, atributos, valores, localizaciones y archivos de correspondencias con otras clasificaciones. Su repositorio es abierto y proporciona distribuciones versionadas [R1, R2]. La última versión estable verificada para esta referencia es **v2026-08**, publicada el 24 de agosto de 2026 [R3].

Su utilidad principal es ofrecer un **esqueleto compartido de familias y clases candidatas** con IDs, rutas y relaciones de categorías, junto con atributos que pueden sugerir dimensiones de demanda. No debe interpretarse que cada hoja es una clase obligatoria del proyecto ni que cada atributo se transforma automáticamente en un requisito.

Shopify también publica mapeos hacia Google, pero la integración documentada con Google está referida a la taxonomía **2021-09-21**; no debe suponerse que representa la última semántica de Google o que constituye un mapeo exhaustivo a Amazon [R4].

**Tratamiento:** mantener una instantánea fija del sistema externo, conservar ID, nombre, ruta, jerarquía, versión y procedencia de sus atributos. Las denominaciones traducidas son etiquetas de presentación, no claves de identidad.

## Amazon: especialización comercial, con dos sistemas distintos

Amazon dispone de una estructura de **nodos de navegación (browse nodes / Browse Tree Guides)** destinada a clasificar y hacer descubribles productos. Los nodos pueden formar parte de múltiples rutas; por ello su organización no debe convertirse sin análisis en un árbol único [R5, R6].

Además, las **Product Type Definitions (PTD)** proporcionan esquemas JSON de atributos y reglas de datos para los tipos de producto del catálogo Amazon. Un *product type* de Amazon no es el mismo objeto que un *browse node*, aunque ambos puedan relacionarse durante la publicación y clasificación de ofertas [R7, R8].

El informe `GET_XML_BROWSE_TREE_DATA` expone la jerarquía y los refinamientos de la navegación por marketplace, pero requiere acceso autorizado como vendedor mediante la SP-API [R5]. Por ello **no se afirma la existencia o vigencia en Amazon.es de un nodo concreto de botas de montaña** hasta contrastarlo con una extracción actual del marketplace español.

**Tratamiento:** usar el árbol Amazon como descubridor de especializaciones candidatas y los PTD como fuente adicional de atributos y condiciones descriptivas. Documentar marketplace, fecha, identificador de nodo o tipo, ruta y nivel de comprobación.

## Google: contraste, datos comerciales y vocabulario de exposición

Google mantiene una **Product Taxonomy** para clasificar productos en Merchant Center y permite a los comerciantes declarar su propio `product_type`; este último no es una rama oficial añadida por Google [R9, R10].

La **Product Data Specification** de Merchant Center define atributos, formatos, valores y reglas según producto, mercado o destino [R11]. El atributo `product_detail` permite publicar especificaciones adicionales mediante nombres y valores elegidos por el comerciante, pero no constituye una ontología universal y cerrada por categoría [R12]. **Manufacturer Center** aporta especificaciones adicionales desde la perspectiva de fabricante [R13].

Las guías de **Google Search sobre `Product`, `Offer` y `ProductGroup`** documentan expresiones de información estructurada y relaciones entre variantes, pero **no son una taxonomía de subclases de producto** [R14, R15]. Son especialmente útiles para relacionar el futuro modelo de demanda con su evaluación por interfaces, sin determinar por sí mismas la segmentación de clases.

**Tratamiento:** emplear Google para contrastar el alcance de clases, identificar dimensiones de información comercial y verificar vocabulario de los canales. Las obligaciones de un feed se estudian separadamente como requisitos técnicos o de plataforma: **no equivalen a requisitos informativos críticos por definición** ([modelo de demanda](../../10-model/demand-model.md)).

## Evidencia comercial y otras referencias

La publicación real de **ecommerce referentes** sigue siendo fuente principal para inferir las cuestiones de demanda ([modelo de demanda](../../10-model/demand-model.md); método en [MPIR](../mpir/README.md)). En esta fase también sirve para comprobar si una especialización es reconocible de forma estable en el mercado y si sus características se diferencian de las de otras clases.

Como vocabulario metodológico de correspondencias puede utilizarse **SKOS**, estándar del W3C que distingue `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch` y `relatedMatch` [R16]. Su aplicación es una **opción de diseño** y exige definir las reglas de uso locales. No cubre por sí solo todos los casos de solapamiento parcial y pertenencia condicional que pueden darse entre clasificaciones comerciales.

## Referencias externas (consulta: 24 de octubre de 2026)

- **[R1] Shopify.** [Standard Product Taxonomy: repositorio, modelo y distribución](https://github.com/Shopify/product-taxonomy). Fuente principal de estructura, atributos y política de versiones.
- **[R2] Shopify.** [Taxonomy Explorer](https://shopify.github.io/product-taxonomy/). Exploración de categorías y atributos.
- **[R3] Shopify.** [Release v2026-08](https://github.com/Shopify/product-taxonomy/releases/tag/v2026-08). Versión estable fijada para la referencia inicial.
- **[R4] Shopify.** [Integrations / mapping documentation](https://github.com/Shopify/product-taxonomy/blob/main/data/integrations/README.md). Mapeos disponibles y versiones de Google usadas.
- **[R5] Amazon SP-API.** [Browse Tree Reports](https://developer-docs.amazon/sp-api/docs/report-type-values-browse-tree). Informe `GET_XML_BROWSE_TREE_DATA`, contenido y permisos de acceso.
- **[R6] Amazon Seller Central.** [Browse for products (Amazon.es)](https://sellercentral.amazon.es/help/hub/reference/external/G202078740) y [Change a product’s category or browse path](https://sellercentral.amazon.com/help/hub/reference/external/G201950630). Jerarquía de navegación, asignación por nodo y posibilidad de múltiples rutas (la segunda guía corresponde al marketplace estadounidense; la propiedad se usa como precaución estructural).
- **[R7] Amazon SP-API.** [Product Type Definitions API](https://developer-docs.amazon/sp-api/docs/product-type-definitions-api). Esquemas de requisitos de datos por tipo de producto.
- **[R8] Amazon SP-API.** [Catalog Items API v2022-04-01](https://developer-docs.amazon/sp-api/lang-es_es/docs/catalog-items-api-v2022-04-01-reference). Datasets diferenciados `attributes`, `classifications` y `productTypes`.
- **[R9] Google Merchant Center.** [Categoría de producto de Google](https://support.google.com/merchants/answer/6324436?hl=es). Jerarquía propia y asignación de categoría.
- **[R10] Google Merchant Center.** [Tipo de producto del comerciante](https://support.google.com/merchants/answer/6324406?hl=es-es). Diferencia entre `product_type` y categoría Google.
- **[R11] Google Merchant Center.** [Especificación de datos de producto](https://support.google.com/merchants/answer/7052112?hl=es). Atributos y reglas por categoría / mercado / destino.
- **[R12] Google Merchant Center.** [Detalles del producto (`product_detail`)](https://support.google.com/merchants/answer/9218260?hl=es). Vocabulario abierto para detalles adicionales.
- **[R13] Google Manufacturer Center.** [Product data specification](https://support.google.com/manufacturers/answer/6124116?hl=en). Datos ampliados de fabricante.
- **[R14] Google Search Central.** [Introduction to Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product). Distinción de tipos de marcado y fuentes de datos.
- **[R15] Google Search Central.** [Product variant structured data (`ProductGroup`)](https://developers.google.com/search/docs/appearance/structured-data/product-variants). Modelo de relaciones entre producto y variantes.
- **[R16] W3C.** [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/). Vocabulario metodológico de relaciones de correspondencia.
