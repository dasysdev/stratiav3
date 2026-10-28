# Tasa de cumplimiento técnico, páginas de la auditoría y mínimo de representación de Web

Decisiones del usuario del 2026-10-28 (sesión de T-077), elegidas entre alternativas que propuso Claude. Cierran OQ-84 y OQ-85 y fijan el sistema cuantitativo técnico de OQ-30.

## 1. Tasa de cumplimiento técnico (OQ-30)

Usuario: «Una tasa y desglose».

- **Una sola tasa por ámbito y vista:** requisitos satisfechos / requisitos evaluados, donde evaluados = pertinentes − NA − NE. Entran las obligatorias y las recomendadas **sin pesos**: cada requisito cuenta uno.
- **Desglose obligatorio:** la tasa se presenta siempre con su desglose por naturaleza (obligatorias, recomendadas), con el mismo cálculo en cada parte.
- **Cobertura al lado:** evaluados / pertinentes. NE es una incidencia: no entra en el denominador de la tasa y se informa en la cobertura.
- **Sin umbrales** ni estados derivados de la tasa (no hay «conforme»).
- Web y Web Schema.org no se suman ni se promedian (como hasta ahora).

Alternativas descartadas: dos tasas separadas sin tasa conjunta; dos tasas más un estado «conforme»; sin tasa.

## 2. Agregación de las páginas en la vista particular

Usuario: «Por tipo de página».

- La tasa de un **tipo de página** (ficha de producto, categoría o listado, políticas y contenido, portada) cuenta los casos requisito × página.
- Además, **por requisito**, la proporción de páginas del tipo en que se satisface (sobre las páginas en que se evaluó).
- Y el resultado de cada página.
- La vista general se evalúa una vez por sitio y da su propia tasa.

Alternativas descartadas: solo por página; solo por requisito.

## 3. Páginas que entran en una auditoría (OQ-85)

Usuario: «Encargo + fijas».

- **Fichas de producto:** las del encargo, las mismas URL (y la misma instantánea) que la auditoría informativa.
- **Portada:** siempre.
- **Políticas y contenido:** siempre: envíos, devoluciones, contacto y aviso legal, localizadas desde la portada y su pie. La que no se localiza se registra como no localizada; no se sustituye por otra.
- **Categoría o listado:** la inmediata de cada ficha, por sus migas de pan. Si la ficha no tiene migas, se registra.
- **Recursos de la vista general:** robots.txt y los sitemaps (los declarados en robots.txt o, si no hay ninguno, `/sitemap.xml`; con sus índices y gzip).
- Todo se captura con el perfil de auditoría (`audit-es`, D-157, D-163).

Alternativas descartadas: muestra de tamaño fijo por tipo sacada del sitemap; solo fichas y políticas.

## 4. Mínimo de representación de Web (OQ-84)

Usuario: «Título + canónica + OG condicional», tras explorar title, metas, canonical y Open Graph con las dos pruebas de D-147 (función y universalidad).

- **Forman el mínimo de Web:**
  - la **url de la página**, ya cubierta por los requisitos de acceso (200, indexable, sin bloqueo);
  - el **título del documento** (`<title>`): lleva un hecho comercial (el nombre), así que lo juzgan la técnica y la informativa (D-143). WHATWG HTML exige exactamente un `title` (nivel de documento, ya congelado);
  - la **URL canónica** (`link rel=canonical`), de sostén: fija qué URL representa la oferta. Su presencia la recomienda Google (página de consolidación de URL duplicadas, que se congela) y, como dato del mínimo, se queda en la técnica (D-145); su forma (en `<head>`, absoluta, sin fragmento, sin canónicas contradictorias) es técnica;
  - la **imagen**: la cubre `og:image` cuando la página usa Open Graph; si no, es un hueco registrado (ninguna especificación del perfil de Web la exige en HTML).
- **Open Graph se añade al perfil de Web** (enmienda de D-159), en el nivel de documento, **de forma condicional**: si la página publica alguna propiedad `og:`, debe llevar las cuatro que el protocolo exige para toda página (`og:title`, `og:type`, `og:image`, `og:url`), bien formadas, y `og:url` (que el protocolo define como la URL canónica del objeto) debe coincidir con la URL canónica. Una página sin Open Graph no incumple nada: esos requisitos son NA.
- **Fuera del mínimo:** `meta description` (sirve para comprender: es contenido) y el idioma del documento.
- **No técnico:** que coincidan `title`, `og:title`, el encabezado principal y el `name` del marcado es un juicio informativo (Fiabilidad dentro del ámbito o consistencia transversal), no un requisito técnico.
- Motivo de incluir Open Graph aunque ningún consumidor del perfil lo exija: es la única declaración formal de la imagen y de la URL canónica de la página fuera de Schema.org, y Google usa `og:title` como fuente del título.

Alternativas descartadas: título y canónica sin Open Graph; solo título.
