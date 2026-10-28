---
id: mpir-sampling-capture
title: MPIR — diseño de la muestra y estrategia de captura
layer: method
status: propuesta
version: 1.5
updated: 2026-10-28
sources: [MPIR §4, MPIR §5, INTAKE 2026-10-25-mpir-capture-engine, INTAKE 2026-10-26-open-issues-resolution, INTAKE 2026-10-28-capture-system]
---

# MPIR — diseño de la muestra y estrategia de captura

Parte de [MPIR](README.md).

## Diseño de la muestra: qué ecommerce y qué recursos observar

### Delimitación por clase

Antes del rastreo se registra: identificador y versión de la clase interna, definición, inclusiones/exclusiones, subclases o facetas relevantes, mercado, idioma, periodo y temas taxonómicos ya reconocidos. Se prepara una **matriz inicial de cobertura** que permita detectar diferencias entre segmentos y tipologías de producto.

La lista de atributos conocida sirve de **guía de contraste**, no de filtro excluyente de la extracción.

### Panel de ecommerce referentes

Se propone un **muestreo intencional y diversificado**, no una lista basada solo en tráfico o notoriedad. En la selección se considera:

- **Especialización y pertinencia:** conocimiento o surtido significativo de la clase estudiada.
- **Diversidad de modelos comerciales:** especialistas, distribuidores multimarca, fabricantes con venta directa y, si aporta contraste, generalistas.
- **Diversidad de segmentos:** usos, niveles de especialización, gamas, públicos y subclases pertinentes.
- **Riqueza de recursos informativos:** existencia de guías, comparadores, FAQ, filtros u otras formas de ayudar a elegir; sin descartar por sistema fuentes con formatos distintos.
- **Independencia editorial:** evitar contar como múltiples observaciones independientes el mismo contenido del fabricante replicado por varios vendedores.
- **Relevancia territorial y temporal:** preferir información aplicable al mercado estudiado y marcar expresamente diferencias de país, idioma o vigencia.
- **Viabilidad y legitimidad de acceso:** restricciones, condiciones de uso y cobertura realmente obtenible.

Cada comercio tendrá ficha de selección, tipo, motivos de inclusión, sesgos posibles y grado de independencia respecto de los demás. **No se establece un número universal de ecommerce:** la cantidad y mezcla se calibrarán en el piloto según diversidad y rendimiento informativo.

### Perfiles de recursos

| Perfil | Qué permite observar | Precaución |
|---|---|---|
| **Ficha de producto / variante / oferta** | Atributos, prestaciones, diferenciadores, descripciones, relaciones, advertencias y condiciones comerciales. | No reducir el contenido a campos técnicos ni tratar todo argumento promocional como demanda. |
| **Página de categoría y filtros** | Facetas de búsqueda, criterios de selección, segmentación por usos o características. | Un filtro puede obedecer a restricciones de plataforma o merchandising. |
| **Comparador y tabla de alternativas** | Dimensiones de contraste, equivalencias, diferencias y compromisos. | Conservar asociaciones entre filas, columnas y entidades. |
| **Guías de compra y artículos técnicos** | Problemas, preguntas, contextos, recomendaciones, relaciones causa-uso y límites de adecuación. | Separar recomendaciones generales de hechos atribuidos a productos concretos. |
| **FAQ y contenidos de ayuda precompra** | Dudas anticipadas y condiciones que el comercio considera necesario explicar. | Distinguir contenido editorial de preguntas auténticas de usuarios cuando sea posible. |
| **Selectores y asistentes de elección** | Variables utilizadas para orientar una recomendación y secuencia de decisiones. | La exploración interactiva es investigación de referencia, no prueba del perfil de auditoría. |
| **Páginas informativas de condiciones comerciales** | Cuestiones previas a decidir sobre disponibilidad, envío, garantías o devoluciones. | No extender el análisis a la ejecución de procesos postcompra. |

Las reseñas, preguntas de usuarios y otros contenidos generados por terceros, cuando se incluyan, se marcarán como **evidencia de procedencia distinta**: no deben atribuirse a una decisión editorial del ecommerce sin justificación.

### Selección de productos y casos

En cada perfil se seleccionan recursos representativos de los segmentos definidos: productos comunes, especializaciones relevantes, variantes o configuraciones diferenciadas, casos fronterizos y ofertas con condiciones distintas cuando ello pueda cambiar la cuestión informativa.

El muestreo debe permitir reconocer **preguntas compartidas, específicas y condicionadas**. No se presupone que cada subcategoría, variante o valor de un atributo exija un modelo de demanda independiente.

## Estrategia técnica de captura y scraping

### Principio rector

**Capturar con amplitud razonable dentro de un perímetro comercial definido, conservar la estructura y posponer las conclusiones semánticas.** No se pretende almacenar indiscriminadamente todo el dominio ni extraer únicamente los atributos previstos por la taxonomía.

### Descubrimiento y clasificación de recursos

1. Identificar dominios autorizados, categorías y rutas vinculadas a la clase; utilizar sitemaps y enlaces internos cuando sean accesibles.
2. Detectar tipos de recursos por estructura, contenido y función, no exclusivamente por patrones de URL.
3. Registrar recursos candidatos, duplicados, redirecciones, variantes de idioma y paginación.
4. Seleccionar una muestra por clase, ecommerce, perfil de recurso y segmento según la matriz de cobertura.
5. Mantener un inventario también de recursos previstos pero no recuperados, con su causa y alcance.

### Captura estructural como procedimiento principal

El procedimiento principal será la obtención del **HTML/DOM y sus bloques** con selectores CSS/XPath y reglas por plantilla, conservando, cuando sea pertinente:

- Encabezados, subtítulos, párrafos, listas, títulos y contenidos asociados.
- Preguntas y respuestas de FAQ, sin separar cada respuesta de su pregunta.
- Tablas con filas, columnas, cabeceras, unidades y entidad comparada.
- Filtros con etiquetas, valores y contexto de la categoría.
- Datos de producto, variantes y condiciones comerciales con identidades y correspondencias.
- Enlaces entre recursos que establecen continuidad explicativa, comparativa o de compatibilidad.
- Datos estructurados disponibles, como JSON-LD, **como representaciones complementarias**, no como verdad de referencia.
- Anotaciones o advertencias de alcance, uso, compatibilidad y limitaciones.

No se utilizará una única conversión a texto plano si destruye relaciones. Para contenido editorial puede emplearse una extracción de texto principal adicional, **sin reemplazar** el DOM o el contexto de tablas, navegación y filtros.

### Contenido dinámico e interacción selectiva

Cada recurso se abre con un navegador real: el [motor de captura](../../../capture/README.md) guarda en una sola visita el HTML de la respuesta, el DOM renderizado y el MHTML. Cuando resulte pertinente, se abren desplegables, selectores o comparadores; se registra qué acciones se realizaron y qué estado del recurso quedó observado.

El renderizado se aplica **siempre**, no selectivamente: la incoherencia entre capas (peticiones con el user-agent de un navegador, navegadores sin interfaz) es lo que más bloqueos provoca, y con el volumen del piloto el coste es despreciable (`INTAKE 2026-10-25-mpir-capture-engine`, [D-042](../../30-governance/decisions.md#d-042), [D-073](../../30-governance/decisions.md#d-073)). La presencia de JavaScript, por sí misma, no debe confundirse con una limitación metodológica ni con un incumplimiento técnico del ecommerce.

No se eludirán autenticaciones, controles de acceso, bloqueos ni medidas anti-bot. El rastreo respetará las políticas aplicables, las condiciones de uso y límites conservadores de solicitudes; si una fuente no puede inspeccionarse legítimamente, se documentará la limitación y se ajustará la muestra.

Entre las políticas aplicables, el [motor de captura](../../../capture/README.md) aplica robots.txt (RFC 9309) y las reservas de minería de textos y datos expresadas por medios de lectura mecánica (art. 67.3 TRLPI: TDMRep, cabecera y meta `tdm-reservation`). Ante una reserva no conserva el contenido ([D-042](../../30-governance/decisions.md#d-042)).

### Qué se conserva en la capa original

Para cada recurso obtenido se preservan: URL solicitada y final; fecha/hora; ecommerce; clase y perfil; idioma/mercado; método de obtención; código/estado relevante; contenido original o referencia a la instantánea; DOM renderizado cuando exista; acciones de interacción; versión o huella del recurso; restricciones de lectura y errores; y enlaces con otras capturas.

No se conservan capturas de pantalla ([D-042](../../30-governance/decisions.md#d-042)): el método no las exige y evitan juzgar por la prominencia ([cautela 4](README.md#hipótesis-de-observación-y-límites-de-inferencia)).

Se distinguen **fuente no recuperada**, **fuente recuperada sin determinado contenido**, **contenido no inspeccionado** y **contenido inspeccionado donde no se halló una señal**. Ninguna de estas situaciones equivale automáticamente a que la necesidad informativa sea irrelevante.

### Exploración abierta y dirigida

- **Exploración abierta:** localizar señales y relaciones sin exigir coincidencia con los atributos taxonómicos existentes. Es esencial para descubrir cuestiones imprevistas.
- **Exploración dirigida:** utilizar dimensiones, clases, facetas y dudas ya identificadas para comprobar cobertura, matices, equivalencias y ausencias aparentes.

Si aparecen recursos o estructuras no previstos, se registra la incidencia, se amplía el perfil de extracción y se reexploran muestras comparables para evitar sesgos por cambios de procedimiento.
