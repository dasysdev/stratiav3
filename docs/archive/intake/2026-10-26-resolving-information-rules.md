# Reglas del motor que determinan la información resolutiva

*Update decidido en la conversación del 2026-10-26, a continuación de `INTAKE 2026-10-26-resolving-information` (D-062). Se transcribe para su trazabilidad: las palabras del usuario y el texto de la propuesta que aprobó.*

## Antecedente

D-062 dejó abierta (OQ-54) la forma en que el motor determina la información resolutiva de cada requisito. Ante la tanda de control con los 14 casos de referencia, Claude explicó que, con lo decidido, los requisitos saldrían sin ese campo, y preguntó si incluirla en esa vía o dejarla para después. Opción elegida por el usuario: «Diseñarla antes de T-030»: «Primero propuesta y muestra de las reglas de OQ-54 y tu decisión; después T-030 y T-031 las implantan, y la tanda de control mide también la información resolutiva.»

## Propuesta de Claude

«Te propongo montar la información resolutiva como una lista por requisito con cuatro orígenes, que compila el entrenamiento: la ley para la capa general, las fuentes de referencia, lo que publican las fichas reales y lo que se infiere sin respaldo. Cada tipo de la lista queda ligado al componente de la pregunta al que aporta y guarda su origen, como hoy cada requisito guarda la regla que decidió su importancia.»

Qué guardaría cada requisito: una lista de tipos; cada tipo lleva su componente (la parte de la pregunta a la que aporta), su origen y respaldo (de dónde sale: la ley, la propiedad de referencia, las fichas…) y en qué tiendas se ha observado («es solo evidencia, no un peso ni una importancia»).

| Origen | Cómo se obtiene | Quién decide |
|---|---|---|
| Marco (capa general) | De la ley que ya es fuente del requisito; por ejemplo, el art. 97.1 j, k y m para gen/11 | Tú; la lista se fija como el resto de la capa general |
| Referencias | El código extrae los títulos y las descripciones de las propiedades de Amazon (y de sus subpropiedades) y los atributos de Shopify con sus valores. Quien redacta los convierte en tipos ligados a componentes. Ejemplo: `SOFA.sleeping_area_dimensions` trae «Altura del área para dormir: desde el suelo hasta la superficie…» | La redacción, sin juicio de importancia |
| Fichas reales | El clasificador ya liga cada hecho declarado al requisito que responde (`answers`). Además indicaría qué tipo de la lista es, o propondría uno nuevo ligado a un componente. El entrenamiento acepta un tipo propuesto cuando aparece en dos tiendas distintas y aporta a un componente de la pregunta | Reglas inducidas |
| Inferida | Información que resuelve, aunque ni las referencias ni las fichas la muestren, como un certificado de ensayo | Quien redacta; queda provisional y marcada como inferida |

«Ningún tipo se retira por no observarse. Que nadie lo publique no significa que no resuelva, y justamente esos tipos son los que más necesita una recomendación.»

«Por qué cuento tiendas y no fichas: las 31 fichas con hechos de gen/11 vienen de solo 4 tiendas. Si se contaran fichas, la plantilla de una tienda pesaría como si fueran muchas.»

## Muestra (datos reales de las ejecuciones v4 y del control)

**`cat.sofas-cama/01`, medidas de la cama abierta**

| Tipo de información | Componente | Origen | Tiendas que lo publican |
|---|---|---|---|
| largo de la superficie de descanso, con unidad | largo | referencias (`sleeping_area_dimensions.length`) | grupotodoplano |
| ancho de la superficie de descanso, con unidad | ancho | referencias (`…width`) | grupotodoplano |
| altura desde el suelo hasta la superficie | altura | referencias (`…height`) | ninguna |
| equivalencia con un tamaño estándar de cama | largo y ancho | fichas («cama de matrimonio», Luna) | 1, queda propuesto hasta verlo en una segunda tienda |
| plano o imagen acotada de la cama abierta | largo, ancho y altura | inferida (provisional) | ninguna |

**`cat.sofas/07`, tapicería**

| Tipo de información | Componente | Origen | Tiendas que lo publican |
|---|---|---|---|
| material o tejido, aunque sea un nombre comercial | material | referencias (`seat-upholstery-material`, `upholstery.fabric_type`) | 2 («tela Victor», Luna; «piel», Stressless) |
| composición en fibras con porcentajes | composición | referencias (`upholstery.material_composition`) | ninguna |
| material por zona (asiento, respaldo) | material | referencias (`seat-…`, `backrest-upholstery-material`) | ninguna |

**`cat.sofas/23`, normas y certificaciones**

| Tipo de información | Componente | Origen | Tiendas que lo publican |
|---|---|---|---|
| norma o certificación citada | normas | referencias (`safety-certifications` y sus valores) | ninguna |
| afirmación de comportamiento ante el fuego | fuego | referencias (`special_feature=Resistente al fuego`, `Retardante de fuego`) | ninguna |
| certificado, informe de ensayo o declaración de conformidad | sustento | inferida (provisional) | ninguna |
| clase o resultado obtenido | normas | inferida (provisional) | ninguna |

**`gen/11`, desistimiento y devolución** (31 fichas de 4 tiendas)

| Tipo de información | Componente | Origen | Tiendas que lo publican |
|---|---|---|---|
| plazo para desistir o devolver | plazo | marco (97.1.j) | 3 |
| canal de devolución (tienda, correo) | condiciones y procedimiento | marco (97.1.j) | 2 |
| reembolso (completo, cuándo) | condiciones | marco (97.1.j) | 1 |
| modelo de formulario de desistimiento | procedimiento | marco (97.1.j) | 0 |
| coste de la devolución a cargo del comprador | coste | marco (97.1.k) | 3 |
| cuándo no procede o se pierde el derecho | excepciones | marco (97.1.m) | 0 |
| remisión a una página de condiciones | condiciones | fichas | 2, se acepta |
| plazo de cambio | ninguno | fichas | 2, se rechaza: un cambio no es desistir ni devolver (proximidad temática) |

Cómo cubre las dos funciones: «Localizar: el auditor tiene una lista concreta de qué buscar en cada requisito, con su respaldo. Para dar una ausencia por probada, sabe qué tipos ha revisado. Recomendar: cada tipo que falta en la ficha auditada se convierte en una acción concreta, por ejemplo "publicar la altura al suelo de la cama abierta". Los ceros entre tiendas (formulario de desistimiento, excepciones) señalan carencias de todo el sector, aunque la recomendación siempre se apoya en la deficiencia de la ficha auditada.»

Qué entraría en el motor: T-030 (el campo en el formato de `DRAFTING.md` y en el modelo; el tipo de cada hecho declarado, o el tipo nuevo propuesto, en la salida del clasificador, con su comprobación; en `bin/train`, extraer los títulos de las referencias, aceptar los tipos observados con la regla de las dos tiendas y una sección en el informe: tipos propuestos, aceptados, rechazados y nunca observados); T-031 (quien redacta rellena las listas de todos los requisitos de categoría a partir de sus fuentes, más los inferidos); capa general («redacto las listas a partir de la ley y te las paso para aprobarlas, igual que se hizo con su importancia»).

Decisiones planteadas: «1. ¿Apruebas el diseño de los cuatro orígenes compilados por el entrenamiento? 2. ¿El mínimo para aceptar un tipo observado es "dos tiendas distintas"? Es la opción que recomiendo. La alternativa, "dos fichas", deja que una sola tienda decida con su plantilla.»

## Decisión del usuario

«OK.»
