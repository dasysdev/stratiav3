# Datos del mínimo de representación en Web Schema.org y formación estructural

Fecha: 2026-10-28. Update descrito por el usuario en la sesión sobre la estructura de la auditoría. Responde a OQ-74 y precisa D-145. Claude aplicó a los candidatos dos pruebas y comprobó en las fuentes congeladas qué exigen Google Search y Merchant Center. El usuario propuso ver como formación estructural la completitud de las estructuras publicadas. Ortografía de las citas normalizada.

Palabras del usuario:

- «¿Estás teniendo en cuenta lo que el consumidor (Google) indica como obligatorio o requerido? ¿Incluso lo que sería obligatorio sobre lo condicional?»
- «¿Y sobre los datos obligatorios cuando un requisito es atributo, es opcional, pero está incluido? Quizás es más un análisis de formación estructural: que una estructura de datos que debe tener varias partes no quede incompleta.»
- Ante la propuesta conjunta (datos del mínimo y formación estructural): «yes».

## 1. Datos del mínimo de representación en Web Schema.org (OQ-74)

### Dos pruebas

1. **Función** (D-143): ¿**hace falta** para descubrir la oferta, acceder a ella o identificarla? Si solo ayuda, es contenido.
2. **Universalidad:** ¿lo tiene **toda** oferta a la que se aplica?
   - Si un producto puede no tenerlo legítimamente (sin GTIN, sin marca), su ausencia puede ser un hecho del producto.
   - Eso lo resuelve la evaluación informativa con un «no» fundamentado. La técnica no puede distinguir «no tiene» de «no lo publica».

### Resultado

| Dato | Tipo | Requisitos |
|---|---|---|
| url de la oferta | Sostén | `ws-consumer/066`; `202` (url del grupo en un sitio de una sola página) |
| Enlace Product → Offer | Sostén | `001` (obligatorio); `153` |
| Relación variante ↔ grupo | Sostén | `193` (obligatorio); `032`, `034`, `192` |
| variesBy (en qué difieren las variantes) | Sostén | `205` |
| Identificador de la entidad (`@id`) | Sostén | Ninguno: es un hueco que se registra (D-143) |
| Imagen | Sostén | D-144 |
| Nombre del producto y del grupo | Con hecho | `002`, `150`, `187` (obligatorios) |
| SKU | Con hecho | `042` |
| Nombre del vendedor | Con hecho | `339` |

- **Fuera del mínimo en Web Schema.org** (contenido; su presencia la juzga la informativa):
  - GTIN y MPN (gen/03);
  - la marca (gen/02);
  - la descripción y la categoría;
  - la razón social, el NIF, la dirección, el contacto, la url y el logo del vendedor (gen/13, gen/14).
- **Recomendados que se quedan en la técnica por ser parte del mínimo:** 9 (`032`, `034`, `042`, `066`, `153`, `192`, `202`, `205`, `339`). Los demás de presencia recomendada, unos 117, pasan a la informativa (T-055).

### Lo obligatorio, también lo condicional

- Todo lo que el consumidor exige, también lo condicional, es técnico (D-145). En la referencia hay 169 requisitos obligatorios del consumidor: 9 universales y 160 condicionales, con la condición en su aplicabilidad.
- **Variantes:** Google Search exige un identificador por variante («Each variant must have a unique ID… for example, using the sku or gtin properties», `195`) y el identificador del grupo (`193`). Son técnicos con independencia del mínimo.
- **GTIN, MPN y marca:** en Google Search son recomendados. Sus obligaciones condicionales son de Merchant Center:
  - GTIN, «It depends», muy recomendado si existe;
  - MPN, obligatorio solo si no hay GTIN del fabricante;
  - marca, obligatoria en productos nuevos (salvo películas, libros y música).
  - Merchant Center pertenece a Catálogos distribuidos y en Web Schema.org solo sirve para la consistencia transversal (D-130). Cuando se defina ese perfil, D-145 las hará técnicas allí.
- Merchant Center confirma la prueba de universalidad: exige el GTIN solo cuando el producto lo tiene y ofrece `identifier_exists` para declarar que no existe. En el marcado Schema.org no hay un campo equivalente.

## 2. Formación estructural (precisa D-145)

> **Formación estructural** (técnica): cuando se publica una estructura,
> 1. tiene las partes que el consumidor **exige** para ella;
> 2. tiene las partes sin las que un valor publicado **no se puede interpretar**: la unidad del peso, la escala de una valoración (`bestRating`/`worstRating`), el sistema de tallas, la moneda de un precio unitario;
> 3. sus partes son **coherentes entre sí**: con `doesNotShip` no hay tarifa; con devolución gratuita no hay importe de devolución.
>
> Las partes que solo **añaden otro hecho** (tipo de reembolso, tarifa de reposición, tiempo de preparación de un servicio de envío) son presencia de lo recomendado → informativa.

- La estructura puede ser opcional y estar incluida: lo que cuenta es que, si se publica, no quede incompleta.
- **Absorbe la excepción de D-145:** los recomendados que sirven para interpretar un valor ya publicado son el punto 2.
- **Lo técnico queda en tres categorías, más dos presencias:**
  - sintaxis y vocabulario;
  - acceso y exposición;
  - formación estructural, que incluye la forma del valor;
  - presencia de los datos exigidos de primer nivel;
  - presencia de los datos del mínimo de representación.

### Ejemplo: el envío en la oferta

- **No hay `shippingDetails`** (recomendado): no es un defecto técnico. La informativa juzga si el ámbito responde al coste y al plazo del envío.
- **Hay `shippingDetails` sin `deliveryTime`**, que Google exige dentro de esa estructura (`105`): técnico, estructura incompleta. La informativa ve además su efecto en el plazo de entrega (gen/08).
- **Están todas las partes exigidas, pero falta `handlingTime`** (recomendado, `122`): solo informativo, es un hecho más sobre el plazo.

### Evidencia: estructuras de la referencia

| Estructura | Partes que exige si se publica | Partes que solo recomienda |
|---|---|---|
| Envío de la tienda (ShippingService…) | 16 | 22 |
| Devolución de la tienda | 9 | 13 |
| Envío en la oferta | 9 | 2 |
| Reseñas y valoración | 9 | 5 |
| Especificación de precio (precio unitario, tachado) | 7 | 8 |
| Certificación | 6 | 1 |
| Devolución en la oferta | 5 | 4 |
| Otras (3DModel, AggregateOffer, SizeSpecification, dirección…) | 10 | 23 |

## 3. Pendiente

- **T-055 queda desbloqueada.** Retira los requisitos con estos criterios, separa requisito a requisito las partes de interpretación y las reglas de coherencia, y registra el hueco del `@id`.
- **Perfil de Catálogos distribuidos** (OQ-30): ahí entrarán como técnicas las obligaciones condicionales de Merchant Center.
