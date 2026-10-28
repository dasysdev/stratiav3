# Mínimo de representación de la oferta y papel de la imagen

Fecha: 2026-10-28. Update descrito por el usuario en la sesión sobre cómo se reparten la evaluación técnica y la de calidad informativa en Web Schema.org. Claude estudió el caso de la imagen en el canon, el catálogo, la ley, las referencias de los consumidores y las fichas congeladas, comparó tres alternativas y recomendó una. Ortografía de las citas normalizada.

Palabras del usuario:

- «En nuestro canon estamos estudiando la representación de la oferta. Hay cuestiones fundamentales para poder representar esa oferta, como el nombre, la descripción, la imagen, la url, etc., que son requisitos mínimos de representación. Hay una frontera que no consigo dibujar sobre estos datos. También es probable que deban analizarse desde dos evaluaciones. Estos datos, que son críticos para formar la representación, podrían analizarse, si existen y están bien formados, desde la evaluación técnica, y la calidad de la información que transmiten, desde la evaluación de calidad.»
- Ante la pregunta de si el mínimo incluye también los datos que solo sostienen la representación sin responder a ninguna cuestión (url, identificador de la entidad, Product enlazado a su Offer): «sí».
- Sobre la imagen: «tengo dudas. Estúdialo a fondo y propón». Ante la propuesta: «A ok».

## 1. Mínimo de representación

- **Definición:** los datos sin los que no existe una representación de la oferta. Son los que hacen falta para **descubrirla, acceder a ella e identificarla**, según las funciones informativas de la IA (ai-functions). Lo que sirve para **comprender, comparar, evaluar y justificar** es contenido.
- **Dos tipos:**
  - datos que llevan un hecho comercial: el nombre o los identificadores;
  - datos que solo sostienen la representación y no responden a ninguna cuestión: la url, el identificador de la entidad, que el Product esté enlazado a su Offer, la imagen (punto 2).
- **Cómo se evalúan:**
  - Si existen y están bien formados lo dice la **evaluación técnica**.
  - Los que llevan un hecho comercial los juzga **también la evaluación informativa** por lo que transmiten, como cualquier otra información: disponibilidad efectiva y criterios de aceptación.
  - Los de sostén solo los mira la técnica.
- **No es doble cómputo:** cada sistema informa en sus propios términos. Se mantiene la invariante de que un incumplimiento técnico no descuenta el GSC: solo cuenta su efecto sobre la disponibilidad del RI. Que falte el nombre es un requisito técnico no satisfecho y, si nada más lo responde, disponibilidad 0 en las cuestiones que dependen de él.
- **No crea requisitos técnicos.** Sus comprobaciones son las de las especificaciones del perfil. En Web Schema.org, por ejemplo, name, image y offers son obligatorias en las fichas de comerciante de Google. Si un dato del mínimo no tiene requisito en el perfil de un ámbito, eso es un hueco que se registra; no se inventa el requisito.
- **Qué datos lo forman,** salvo la imagen, está por decidir. Con el criterio de las funciones, la descripción quedaría como contenido y no como mínimo: sirve para comprender, y Google solo la recomienda.

## 2. La imagen

### Decisión (alternativa A)

La imagen **forma parte del mínimo de representación como sostén**, por dos vías:

- **Identificar:** el art. 19.c del Reglamento (UE) 2023/988 (GPSR) exige que la oferta a distancia incluya «información que permita identificar el producto, incluida una imagen suya, su tipo y otros identificadores». Comprobado en el texto oficial alemán («Angaben, die die Identifizierung des Produkts ermöglichen, einschließlich einer Abbildung des Produkts, seiner Art und sonstiger Produktidentifikatoren»). La obligación es de la oferta en su conjunto, no de un ámbito concreto.
- **Descubrir:** en las fichas de comerciante de Google, image es una propiedad obligatoria, con name y offers.

La imagen se evalúa en la **evaluación técnica**: que exista, que su URL sea válida, que se pueda recuperar y que tenga un formato admitido. En Web Schema.org son los requisitos `ws-consumer/003`–`010` y `185`–`186`, que el usuario decidió conservar en el triaje del 2026-10-28.

**Lo que la imagen muestra no es información. La información explícita que lleva sí lo es.** La imagen muestra, no afirma.

| Papel | Ejemplo | Tratamiento |
|---|---|---|
| **Sostiene la identificación** | Foto del producto | Evaluación técnica (mínimo de representación). |
| **Expresa información explícita** | Plano acotado, tabla de tallas, etiqueta energética, advertencias de seguridad | Es información como cualquier otra, si el ámbito permite leerla. En Web Schema.org, solo si está en texto en el marcado (`caption`, `embeddedTextCaption` de ImageObject). En Web, depende de las pruebas de legibilidad (pendiente). |
| **Muestra lo que no afirma** | Color, piezas, aspecto | No es información pertinente: no da disponibilidad, no resuelve ningún RI y no sirve para refutar en Fiabilidad. Sí puede crear una necesidad que el texto tiene que resolver: lo que sale en la foto y no se entrega (descripción de `gen/21`). |

### Fundamento

- **Disponibilidad efectiva:** exige al menos un dato, afirmación o relación que pueda obtenerse y leerse. Lo que una foto muestra no es nada de eso.
- **Funciones de la IA:** la auditoría no toma como patrón la capacidad máxima de inferencia de un sistema avanzado, y leer lo que muestra una foto es inferencia visual.
- **Prueba de derivación:** reconocer el modelo a partir de una foto exige hechos particulares del producto tomados de fuera, y eso no se admite.
- **Paralelo con D-119:** el atributo puede acompañar a la prestación declarada como contexto, pero no la resuelve. La imagen acompaña igual a la identificación.
- **Coherencia con lo que ya hay:** el «plano o imagen acotada» de resolving-information sigue siendo válido, porque es información explícita.

### Evidencia reunida

- **Google, fichas de comerciante:** image es obligatoria. Description y la url de la oferta son recomendadas.
- **Google Merchant Center:**
  - image_link es obligatorio;
  - tiene reglas de contenido: que muestre el producto con exactitud, sin imagen genérica ni texto promocional;
  - exige 500×500 píxeles desde el 31 de enero de 2027, dentro del perímetro.
- **Amazon (1.877 tipos de producto, 2026-10-24):** la imagen principal está en todos, pero el esquema no la exige (sí exige item_name y product_description). Todos tienen seis campos de imágenes de seguridad del producto.
- **Schema.org 30.1:** name, description, image y url son propiedades de Thing. ImageObject tiene `caption` y `embeddedTextCaption`.
- **Fichas congeladas (45, de 6 tiendas):** las 42 que tienen Product en JSON-LD tienen image. Ninguna muestra en la primera carga avisos del tipo «imagen no contractual». La ausencia de imagen es rara; lo que importa es qué vale lo que muestra.

### Lo que no se juzga

Si la foto es genérica o de otra variante:

- en Catálogos distribuidos, como regla de contenido de Merchant Center, cuando exista ese perfil;
- en Web Schema.org no se juzga: el contraste del marcado con la página o con la realidad quedó fuera en el triaje (bloque «marcado frente a página»).

### Alternativas descartadas

- **B, dos evaluaciones:** un requisito propio («¿Cómo es el producto?») valorado con los AC. Se descarta porque:
  - crea una cuestión nueva, contra D-052;
  - los criterios de aceptación están pensados para afirmaciones;
  - el juicio visual es difícil de reproducir.
- **C, sin estatus especial:** una propiedad recomendada más. Se descarta porque Google la exige y el GPSR la liga a la identificación del producto.

## 3. Catálogo de demanda

- La aportación resolutiva «imagen que permite identificar el producto» de `gen/24` deja de ser aportación. La imagen sostiene la identificación como mínimo de representación, pero no resuelve `gen/24`.
- Se enmienda la interpretación de D-052, según la cual la imagen del art. 19.c «es un medio de responder qué es el producto (gen/01) y su identificación». La imagen no resuelve `gen/01` ni `gen/24`. Con esto desaparece también la discrepancia entre D-052, que habla de `gen/01`, y el catálogo, que la tenía en `gen/24`.

## 4. Pendiente

- **Texto dentro de una imagen en Web:** si se puede leer con reconocimiento de texto y cuenta como legible. Va con las pruebas de obtención y legibilidad de la disponibilidad efectiva. Caso práctico: advertencias de seguridad publicadas solo como imagen de la etiqueta (`gen/19`).
- **El resto de la frontera del mínimo de representación:** la descripción, la url, los identificadores y los demás datos.
- **La frontera general entre las dos evaluaciones** sigue en estudio: la técnica mira la forma; la informativa, la presencia y la suficiencia. También los 83 requisitos técnicos que el usuario tratará como informativos (`web-audit/reference/reports/2026-10-28-triaje.md`).
