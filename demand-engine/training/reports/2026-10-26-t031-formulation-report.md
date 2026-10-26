# T-031 · Nueva redacción del catálogo con las reglas de formulación (D-060)

Fecha: 2026-10-26. Reglas de [D-060](../../../docs/30-governance/decisions.md#d-060), aplicadas con `catalog/DRAFTING.md` (punto 8) a los 60 bloques de `catalog/cat/`; la capa general, con [D-065](../../../docs/30-governance/decisions.md#d-065). Información resolutiva de [D-063](../../../docs/30-governance/decisions.md#d-063) en todos los requisitos. Ciclo de entrenamiento: reglas 6 ([informe del ciclo](2026-10-26-v6-report.md)).

## Resumen

- Catálogo de categorías: 382 → 440 requisitos. 71 requisitos redactados de nuevo en 27 bloques y 58 requisitos nuevos: 41 partes separadas con sus fuentes y 17 cuestiones inferidas.
- Capa general ([D-065](../../../docs/30-governance/decisions.md#d-065), decisión del usuario): 27 → 46 requisitos, versión 0.4.
- Información resolutiva en los 486 requisitos (440 de categoría y 46 de la capa general).
- Reglas 6 aceptadas: ninguna métrica empeora; frente a las reglas 5 sobre el catálogo nuevo, mejoran la coherencia por requisito (18 → 17) y los requisitos sin regla (7 → 0).

### Requisitos que cambian por regla

Un requisito puede cambiar por varias reglas; «nuevos» cuenta los requisitos que salen de él.

| Regla | Requisitos redactados de nuevo | Requisitos nuevos |
|---|---|---|
| 1. Ninguna condición sobre la existencia de la información | 5 | 3 |
| 2. Condición sobre un hecho que afecta a una parte: requisito condicionado propio | 12 | 10 |
| 3. Una necesidad por requisito: se divide si las partes tomarían otro rasgo u otra importancia | 45 | 41 |
| 4. Cada componente con fuente; sin ella, cuestión inferida | 21 | 17 |

Combinaciones: regla 1: 2; regla 1 + 3: 2; regla 1 + 4: 1; regla 2: 6; regla 2 + 3: 4; regla 2 + 4: 2; regla 3: 36; regla 3 + 4: 3; regla 4: 15.

## Criterios de aplicación

- **Parte principal.** Conserva el id la parte que mantiene el rasgo del requisito original, para que sus votos sigan contando para la misma necesidad; si ninguna lo mantiene, la cabeza de la pregunta (`cat.juguetes-para-perros/08` pasa de contenido a material: que contenga comida ya es su condición).
- **Ids nuevos.** Nunca reutilizan un número usado antes en el catálogo, las ejecuciones, los informes o las reglas (las botas empiezan en /19, las pantuflas en /17 y los sofás cama en /16).
- **Regla 1.** Si la condición nombra un hecho, se aplica la regla 2. Si el componente existe siempre, la condición se quita: todo bloque de lija tiene base; todo material tiene composición.
- **Regla 3 estrecha.** El rasgo y la importancia de cada parte son los que tomaría con el vocabulario y las reglas 5 de su clase. Las partes de igual rasgo e importancia siguen juntas (par de calibración `cat.sofas/13` y `cat.sofas/05`). A veces la parte separada cabe en un requisito existente del mismo rasgo: entonces pasa allí (manchas a `cat.camas-para-mascotas/08`; lavado a máquina a `cat.protectores-de-colchon/07`; lo no tóxico a `cat.sofas/23`).
- **Regla 4.** Un componente sin fuente sale como cuestión inferida, con los controles de D-036. Hay dos excepciones: si una referencia sí lo recoge, se añade la fuente (`cat.comida-para-perros/07`, `cat.mochilas/13`); si otro requisito ya lo pregunta o no es de toda la clase, se retira (ver «Retirado»).
- **Votos de los nuevos.** Los requisitos nuevos llevan la importancia que daría quien redacta (DRAFTING, punto 5) como etiqueta del catálogo; la decide la regla compilada de su rasgo y clase.

## Regla 1: ninguna condición sobre la existencia de la información

5 requisitos.

| Requisito | Antes | Después | Requisitos nuevos |
|---|---|---|---|
| `cat.botas/07` | ¿Qué aislamiento térmico o abrigo ofrece (forro aislante, felpa…) y, si se indica, hasta qué temperatura? | ¿Qué aislamiento térmico o abrigo ofrece (forro aislante, felpa…)?<br>*«si se indica» condiciona a la existencia de la información, y la temperatura no tiene fuente (los valores Aislado y De felpa no la recogen): sale como inferida condicionada* | `cat.botas/23` ¿Hasta qué temperatura exterior protege del frío? (prestacion, complementario, inferida; si ofrece aislamiento térmico o abrigo) |
| `cat.botas/08` | ¿Qué protecciones de seguridad ofrece (suela antiperforación, disipación de electricidad estática, resistencia a llamas, a productos químicos o a impactos, elementos reflectantes)? ⟨si es bota de trabajo o de seguridad, o declara alguna protección⟩ | (misma pregunta) ⟨si es bota de trabajo o de seguridad⟩<br>*«o declara alguna protección» condicionaba a la existencia de la información* | — |
| `cat.calzado/06` | ¿Tiene puntera de protección y de qué tipo (acero, aluminio, material compuesto, no metálica…)? ⟨si es calzado de seguridad o de trabajo, o declara protección en la puntera⟩ | (misma pregunta) ⟨si es calzado de seguridad o de trabajo⟩<br>*«o declara protección en la puntera» condicionaba a la existencia de la información* | — |
| `cat.cd-de-musica/01` | ¿Quién es el artista o intérprete principal (o si es un recopilatorio de varios artistas) y, si procede, el compositor? | ¿Quién es el artista o intérprete principal, o es un recopilatorio de varios artistas?<br>*«si procede» corresponde a un hecho (obras de un compositor distinto del intérprete): requisito condicionado propio, que además toma otra importancia que el artista* | `cat.cd-de-musica/11` ¿Quién es el compositor de las obras? (identidad, principal; si las obras no son del propio intérprete (música clásica, bandas sonoras, versiones…)) |
| `cat.discos-y-lp/01` | ¿Quién es el artista o intérprete principal y, si procede, el compositor? | ¿Quién es el artista o intérprete principal?<br>*«si procede» corresponde a un hecho (obras de un compositor distinto del intérprete): requisito condicionado propio, que además toma otra importancia que el artista* | `cat.discos-y-lp/13` ¿Quién es el compositor de las obras? (identidad, principal; si las obras no son del propio intérprete (música clásica, bandas sonoras, versiones…)) |

## Regla 2: condición sobre un hecho que afecta a una parte: requisito condicionado propio

12 requisitos.

| Requisito | Antes | Después | Requisitos nuevos |
|---|---|---|---|
| `cat.bloques-de-lija/03` | ¿De qué material está hecho el bloque (cuerpo y, si la tiene, la base o almohadilla: corcho, goma, plástico, espuma, aluminio…)? | ¿De qué material está hecho el bloque, incluida su base o almohadilla de lijado (corcho, goma, plástico, espuma, aluminio…)?<br>*«si la tiene» sobra: todo bloque tiene base de lijado, del mismo material que el cuerpo o de otro* | — |
| `cat.botas/04` | ¿Qué tipo de cuero o piel es (flor entera, nobuk, ante, serraje, charol…) y, si lleva piel con pelo, es natural o sintética y de qué animal? | ¿Qué tipo de cuero o piel es (flor entera, nobuk, ante, serraje, charol…)?<br>*la piel con pelo es un hecho que solo afecta a una parte: requisito condicionado propio* | `cat.botas/20` ¿La piel con pelo es natural o sintética y de qué animal procede? (material, principal; si lleva piel con pelo) |
| `cat.botas/05` | ¿Qué tipo de tacón tiene (sin tacón, plano, de bloque, cuña, aguja, cubano…) y, si tiene plataforma, qué altura? | ¿Qué tipo de tacón tiene (sin tacón, plano, de bloque, cuña, aguja, cubano…)?<br>*la plataforma es un hecho que solo afecta a una parte, y su altura es una medida (otro rasgo)* | `cat.botas/21` ¿Qué altura tiene la plataforma? (medida, principal; si tiene plataforma) |
| `cat.calzado/22` | ¿Qué flexibilidad o rigidez tiene la suela (y, en el calzado de caña, la caña)? | ¿Qué flexibilidad o rigidez tiene la suela?<br>*la caña es un hecho que solo afecta a una parte; su rigidez pasa a un requisito de las botas, el bloque al que se aplica (con BOOT.item_firmness_description)* | `cat.botas/24` ¿Qué rigidez tiene la caña (blanda, semirrígida, rígida)? (prestacion, complementario) |
| `cat.camas-para-mascotas/05` | ¿De qué material es la superficie o funda y, si es textil, cuál es su composición en fibras? | ¿De qué material es la superficie o funda y cuál es su composición?<br>*«si es textil» sobra: todo material tiene composición, que en los textiles se expresa en fibras (Reglamento 1007/2011)* | — |
| `cat.cd-de-musica/07` | ¿Qué tipo de disco es y con qué reproductores es compatible (CD de audio estándar, SACD híbrido o solo SACD, CD mejorado o CD-ROM con contenido para ordenador, CD oro; código de región del DVD si lo incluye) y lleva sistema anticopia? | ¿Qué tipo de disco es y con qué reproductores es compatible (CD de audio estándar, SACD híbrido o solo SACD, CD mejorado o CD-ROM, CD oro), y lleva sistema anticopia?<br>*el código de región del DVD depende de un hecho (que incluya DVD) y no tiene fuente: sale como inferida condicionada* | `cat.cd-de-musica/13` ¿Para qué región está codificado el DVD o el Blu-ray que incluye? (uso, complementario, inferida; si incluye un DVD o un Blu-ray) |
| `cat.joyeria/01` | ¿De qué material es la pieza y, si lo tiene, qué baño o recubrimiento lleva (metal base, plata u oro, bañado en oro o rodio, acero, aleación…)? | ¿De qué material es la pieza (metal base, plata, oro, acero, aleación…)?<br>*el baño es un hecho que solo afecta a una parte: requisito condicionado propio* | `cat.joyeria/07` ¿De qué es el baño o recubrimiento (oro, oro rosa, rodio, paladio…)? (material, principal; si la pieza está bañada o recubierta) |
| `cat.juguetes-para-perros/08` | ¿Contiene o incluye comida o premios y, si es así, qué ingredientes tienen y cómo se conservan? | ¿Qué ingredientes tienen la comida o los premios que contiene o incluye? · rasgo contenido → material<br>*que contenga comida es la condición (ya en applicability); su detalle reúne dos necesidades de otro rasgo: los ingredientes (material, este requisito) y la conservación (cuidado). El rasgo pasa de contenido a material* | `cat.juguetes-para-perros/15` ¿Cómo se conservan la comida o los premios que contiene o incluye y hasta cuándo se pueden consumir? (cuidado, complementario; si el juguete es comestible o contiene o incluye comida o premios) |
| `cat.pantuflas/06` | ¿Qué tipo de cuero o piel es (ante, nobuk, piel de oveja…) y, si lleva piel con pelo, es natural o sintética y de qué animal? | ¿Qué tipo de cuero o piel es (ante, nobuk, piel de oveja…)?<br>*la piel con pelo es un hecho que solo afecta a una parte: requisito condicionado propio* | `cat.pantuflas/18` ¿La piel con pelo es natural o sintética y de qué animal procede? (material, complementario; si lleva piel con pelo) |
| `cat.sofas/16` | ¿Qué partes son regulables (asientos reclinables o deslizantes, reposapiés, cabezales, respaldo, altura), con qué mecanismo se accionan (manual, eléctrico, mando) y, si reclina, cuántas plazas lo hacen y en cuántas posiciones? | ¿Qué partes son regulables (asientos reclinables o deslizantes, reposapiés, cabezales, respaldo, altura) y con qué mecanismo se accionan (manual, eléctrico, mando)?<br>*«si reclina» es un hecho que solo afecta a una parte: requisito condicionado propio, como /17 (ejemplo de D-060)* | `cat.sofas/32` Si es reclinable, ¿cuántas plazas reclinan y en cuántas posiciones? (construccion, complementario; si es reclinable) |
| `cat.sofas/25` | ¿Se puede personalizar (tapicería, color, medidas, composición de módulos) y con qué opciones? | ¿Se puede personalizar (tapicería, color, medidas, composición de módulos)?<br>*SOFA.is_customizable solo dice si es personalizable; las opciones, detalle sin fuente, salen como inferida condicionada* | `cat.sofas/34` ¿Con qué opciones se puede personalizar? (estetica, complementario, inferida; si se puede personalizar) |
| `cat.zapatillas-para-bebes-y-ninos/01` | ¿Qué tipo de zapatilla es (deportiva de uso diario, de lona, para correr, multideporte, con ruedas…) y, si está pensada para un deporte o actividad concretos, cuál? | ¿Qué tipo de zapatilla es (deportiva de uso diario, de lona, para correr, multideporte, con ruedas…)?<br>*«si está pensada para un deporte» es un hecho que solo afecta a una parte, y el uso (uso) toma otro rasgo que el tipo (identidad); el nuevo requisito es universal: el uso diario también lo responde* | `cat.zapatillas-para-bebes-y-ninos/08` ¿Para qué uso, deporte o actividad está pensada (uso diario, correr, baloncesto, senderismo…)? (uso, complementario) |

## Regla 3: una necesidad por requisito: se divide si las partes tomarían otro rasgo u otra importancia

45 requisitos.

| Requisito | Antes | Después | Requisitos nuevos |
|---|---|---|---|
| `cat.botas/01` | ¿Qué tipo de bota es y para qué uso está pensada (botín, Chelsea, chukka, de agua, de nieve, de montaña, de trabajo, de montar, vaquera, motera…)? | ¿Qué tipo de bota es (botín, Chelsea, chukka, de agua, de nieve, vaquera, motera…)?<br>*el tipo (identidad) y el uso o la actividad (uso) se responden por separado y toman otro rasgo* | `cat.botas/19` ¿Para qué uso o actividad está pensada (montaña, trabajo, equitación, nieve, ciudad…)? (uso, principal) |
| `cat.botas/05` | — | ver regla 2 | — |
| `cat.botas/06` | ¿De qué material es la plantilla y es extraíble? | ¿De qué material es la plantilla?<br>*el material (material) y que sea extraíble (construcción) toman otro rasgo* | `cat.botas/22` ¿Es extraíble la plantilla? (construccion, principal) |
| `cat.calzado/19` | ¿Lleva materiales reciclados o de origen animal, y qué atributos ambientales declara (ecológico, origen sostenible…)? | ¿Lleva materiales reciclados o de origen animal, o es vegano?<br>*los materiales (material) y los atributos ambientales declarados (certificación u origen) toman otro rasgo* | `cat.calzado/26` ¿Qué atributos ambientales declara (ecológico, abastecimiento sostenible…)? (certificacion-origen, complementario) |
| `cat.camas-de-enfriamiento-para-mascotas/01` | ¿Cómo enfría: con qué sistema o material refrigerante (gel que se activa por presión, agua, tejido refrigerante, ventilación, eléctrico) y qué necesita para funcionar (refrigeración previa, llenado de agua, corriente)? | ¿Con qué sistema o material enfría (gel que se activa por presión, agua, tejido refrigerante, ventilación, eléctrico)?<br>*lo que necesita para funcionar no lo recogen los valores Refrescante y Ajuste de temperatura, y es otro rasgo (uso): sale como inferida* | `cat.camas-de-enfriamiento-para-mascotas/04` ¿Qué necesita para enfriar (refrigeración previa, llenado de agua, corriente eléctrica) o enfría sin preparación? (uso, principal, inferida) |
| `cat.camas-para-mascotas/06` | Si tiene relleno o acolchado, ¿de qué material es y qué soporte ofrece (espuma viscoelástica u ortopédica, fibra, grosor)? | Si tiene relleno o acolchado, ¿de qué material es (espuma viscoelástica, fibra…)?<br>*el material del relleno (material) y el soporte que ofrece (prestación) toman otro rasgo; el grosor ya lo pregunta /03* | `cat.camas-para-mascotas/14` Si tiene relleno o acolchado, ¿qué soporte ofrece (ortopédico, firme, que se adapta al cuerpo…)? (prestacion, principal; si tiene relleno o acolchado) |
| `cat.camas-para-mascotas/08` | ¿Qué resistencia tiene a mordidas, arañazos y desgarros, y a la decoloración? | ¿Qué resistencia tiene a mordidas, arañazos y desgarros, a la decoloración y a las manchas?<br>*recibe la resistencia a las manchas de /11, del mismo rasgo* | — |
| `cat.camas-para-mascotas/11` | ¿Cómo se limpia: es lavable (a máquina, a mano, solo por manchas), tiene funda extraíble y resiste las manchas? | ¿Cómo se limpia: es lavable (a máquina, a mano, solo por manchas) y tiene funda extraíble?<br>*la resistencia a las manchas (prestación) pasa a /08, que pregunta las resistencias* | — |
| `cat.camas-para-mascotas/12` | ¿Es plegable, ligera o portátil para transportarla o guardarla, y cuánto pesa? | ¿Es plegable, ligera o portátil para transportarla o guardarla?<br>*el peso (magnitud) toma otro rasgo que el transporte y el plegado (construcción)* | `cat.camas-para-mascotas/15` ¿Cuánto pesa? (magnitud, complementario) |
| `cat.cd-de-musica/01` | — | ver regla 1 | — |
| `cat.cd-de-musica/08` | ¿Qué tipo de grabación es (estudio o en directo) y cuál es su proceso de grabación, mezcla y masterizado (AAD, ADD, DDD)? | ¿Cuál es su proceso de grabación, mezcla y masterizado (AAD, ADD, DDD)?<br>*estudio o directo (identidad) y el procesado (construcción) toman otro rasgo y otra importancia* | `cat.cd-de-musica/14` ¿Es una grabación de estudio o en directo? (identidad, principal) |
| `cat.cd-de-musica/09` | ¿Qué presentación tiene (caja jewel, digipak, funda de cartón, cofre) y qué material adicional incluye (libreto, letras, código de descarga)? | ¿Qué material adicional incluye (libreto, letras, código de descarga…)?<br>*la presentación (construcción) y el material incluido (contenido) toman otro rasgo* | `cat.cd-de-musica/15` ¿Qué presentación tiene (caja jewel, digipak, funda de cartón, cofre…)? (construccion, complementario) |
| `cat.cojines-decorativos/09` | ¿Es apto para exterior y cómo resiste el agua, el sol y la intemperie? | ¿Está pensado para interior, para exterior o para ambos?<br>*el lugar de uso (uso) y la resistencia a la intemperie (prestación) toman otro rasgo* | `cat.cojines-decorativos/12` ¿Cómo resiste el agua, el sol y la intemperie? (prestacion, complementario) |
| `cat.cojines-decorativos/10` | ¿Qué propiedades higiénicas o de seguridad tiene (hipoalergénico, antiácaros, antibacteriano, resistencia al fuego)? | ¿Qué propiedades higiénicas tiene (hipoalergénico, antiácaros, antibacteriano…)?<br>*el comportamiento ante el fuego (seguridad) toma otro rasgo que la higiene (prestación)* | `cat.cojines-decorativos/13` ¿Cómo se comporta ante el fuego (resistente o retardante del fuego)? (seguridad, complementario) |
| `cat.cubrecolchones/02` | ¿Qué grosor y qué firmeza tiene el acolchado? | ¿Qué firmeza tiene el acolchado?<br>*el grosor (magnitud) y la firmeza (prestación) toman otro rasgo y otra importancia* | `cat.cubrecolchones/05` ¿Qué grosor tiene el acolchado? (magnitud, complementario) |
| `cat.cubrecolchones/03` | ¿Es compatible con somieres articulados y se puede usar por las dos caras? | ¿Es compatible con somieres articulados?<br>*la compatibilidad (uso) y el uso por las dos caras (construcción) toman otro rasgo* | `cat.cubrecolchones/06` ¿Se puede usar por las dos caras? (construccion, complementario) |
| `cat.discos-y-lp/01` | — | ver regla 1 | — |
| `cat.discos-y-lp/10` | ¿Qué tipo de grabación es (estudio o en directo) y cuál es su proceso de grabación, mezcla y masterizado (AAD, ADD, DDD)? | ¿Cuál es su proceso de grabación, mezcla y masterizado (AAD, ADD, DDD)?<br>*estudio o directo (identidad) y el procesado (construcción) toman otro rasgo y otra importancia* | `cat.discos-y-lp/15` ¿Es una grabación de estudio o en directo? (identidad, principal) |
| `cat.discos-y-lp/11` | ¿Qué presentación tiene (funda simple, doble o desplegable, cofre) y qué material adicional incluye (encarte, libreto, código de descarga)? | ¿Qué material adicional incluye (encarte, libreto, código de descarga…)?<br>*la presentación (construcción) y el material incluido (contenido) toman otro rasgo* | `cat.discos-y-lp/16` ¿Qué presentación tiene (funda simple, doble o desplegable, cofre…)? (construccion, complementario) |
| `cat.joyas-para-piercings/06` | ¿Lleva piedras, cristales o perlas, de qué tipo, cuántas y de qué tamaño o peso? | ¿Lleva piedras, cristales o perlas, de qué tipo y cuántas?<br>*el detalle de la pregunta de sí o no reúne otra necesidad: el tamaño o el peso de las piedras (magnitud) toma otro rasgo y otra importancia* | `cat.joyas-para-piercings/11` ¿Qué tamaño o peso tienen las piedras o perlas (quilates, diámetro)? (magnitud, complementario; si lleva piedras, cristales o perlas) |
| `cat.juguetes-para-perros/01` | ¿Qué tipo de juguete es y para qué tipo de juego está pensado (pelota, mordedor, cuerda para tirar, peluche, chirriante, dispensador de premios, rompecabezas, para lanzar, de entrenamiento…)? | ¿Qué tipo de juguete es (pelota, mordedor, cuerda, peluche, chirriante, dispensador de premios, rompecabezas, frisbi…)?<br>*el tipo (identidad) y el juego o la actividad para los que está pensado (uso) toman otro rasgo y otra importancia* | `cat.juguetes-para-perros/12` ¿Para qué tipo de juego o actividad está pensado (lanzar y traer, morder, tirar, estimulación mental, entrenamiento…)? (uso, complementario) |
| `cat.juguetes-para-perros/03` | ¿Qué tamaño, medidas y peso tiene el juguete? | ¿Qué tamaño y medidas tiene el juguete?<br>*el peso (magnitud) toma otro rasgo que las medidas (medida)* | `cat.juguetes-para-perros/13` ¿Cuánto pesa el juguete? (magnitud, complementario) |
| `cat.juguetes-para-perros/07` | ¿En qué entorno se puede usar (interior, exterior, agua) y resiste el agua o flota? | ¿En qué entorno se puede usar (interior, exterior, agua)?<br>*el entorno (uso) y la resistencia al agua o la flotación (prestación) toman otro rasgo y otra importancia* | `cat.juguetes-para-perros/14` ¿Resiste el agua y flota? (prestacion, complementario) |
| `cat.juguetes-para-perros/08` | — | ver regla 2 | — |
| `cat.maletas-y-bolsos-de-viaje/01` | ¿Cómo se transporta (asas de mano, correa de hombro, bandolera, correas de mochila, funda para carrito…) y qué correas son desmontables o ajustables? | ¿Cómo se transporta (asas de mano, correa de hombro, bandolera, correas de mochila, funda para carrito…)?<br>*el modo de transporte (uso) y las correas desmontables o regulables (construcción) toman otro rasgo y otra importancia* | `cat.maletas-y-bolsos-de-viaje/05` ¿Qué correas son desmontables o regulables? (construccion, complementario) |
| `cat.mantas/01` | ¿Qué nivel de abrigo tiene y para qué época del año es adecuada? | ¿Qué nivel de abrigo tiene?<br>*el abrigo (prestación) y la temporada (uso) toman otro rasgo y otra importancia* | `cat.mantas/12` ¿Para qué época del año es adecuada? (uso, complementario) |
| `cat.mantas/10` | ¿Qué propiedades de salud y seguridad declara (hipoalergénica, antibacteriana, no tóxica, resistente a las llamas)? | ¿Qué propiedades higiénicas declara (hipoalergénica, antibacteriana, antimicrobiana)?<br>*la ausencia de toxicidad y el comportamiento ante las llamas (seguridad) toman otro rasgo que la higiene (prestación)* | `cat.mantas/13` ¿Qué propiedades de seguridad declara (no tóxica, resistente a las llamas)? (seguridad, complementario) |
| `cat.mochilas-escolares/03` | ¿Qué tirantes y espalda tiene (acolchados, regulables, ergonómicos, con correa de pecho o de cintura, panel trasero transpirable) y para qué talla de espalda? | ¿Qué tirantes y espalda tiene (acolchados, regulables, ergonómicos, con correa de pecho o de cintura, panel trasero transpirable)?<br>*la talla de espalda (uso: ajuste al cuerpo) toma otro rasgo que los tirantes (construcción)* | `cat.mochilas-escolares/08` ¿Para qué talla de espalda o estatura está pensada? (uso, complementario) |
| `cat.pantuflas/01` | ¿Qué tipo de zapatilla de casa es (cerrada, abierta o destalonada, chancla, botín, zueco, calcetín…) y qué altura tiene? | ¿Qué tipo de zapatilla de casa es (cerrada, abierta o destalonada, chancla, botín, zueco, calcetín…)?<br>*el tipo (identidad) y la altura (medida) toman otro rasgo* | `cat.pantuflas/17` ¿Qué altura tiene (por debajo del tobillo, hasta el tobillo o más alta)? (medida, principal) |
| `cat.protectores-de-colchon/06` | ¿Qué resistencia al uso y qué facilidad de mantenimiento tiene (antimanchas, secado rápido, no encoge, sin pelusa…)? | ¿Qué resistencia al uso y al lavado tiene (antimanchas, secado rápido, no encoge, sin pelusa…)?<br>*el lavado a máquina (cuidado) pasa a /07, del mismo rasgo; aquí queda la resistencia (prestación)* | — |
| `cat.protectores-de-colchon/07` | ¿Se puede retirar la cubierta o la capa superior para lavarla aparte? | ¿Se puede lavar a máquina y retirar la cubierta o la capa superior para lavarla aparte?<br>*recibe el lavado a máquina de /06, del mismo rasgo* | — |
| `cat.sofas-cama/02` | ¿Incluye colchón y, si lo incluye, qué medida, material y grosor tiene y se puede retirar? | ¿Incluye colchón y, si lo incluye, de qué medida es y se puede retirar?<br>*la pregunta de sí o no con su detalle se mantiene (regla 2); el material y el grosor del colchón no los recoge SOFA.mattress (solo size_name): salen como inferidas, una por rasgo (material y magnitud)* | `cat.sofas-cama/16` ¿De qué material es el colchón incluido? (material, principal, inferida; si incluye colchón)<br>`cat.sofas-cama/17` ¿Qué grosor tiene el colchón incluido? (magnitud, principal, inferida; si incluye colchón) |
| `cat.sofas/01` | ¿Qué tipo de sofá es y cómo está configurado (recto, con chaise longue, rinconera, modular…), y de cuántas piezas o módulos se compone? | ¿Qué tipo de sofá es y cómo está configurado (recto, con chaise longue, rinconera, modular…)?<br>*el tipo y la configuración (identidad) y el número de piezas o módulos (contenido) toman otro rasgo y otra importancia* | `cat.sofas/27` ¿De cuántas piezas o módulos se compone? (contenido, principal) |
| `cat.sofas/06` | ¿De qué material es la estructura (armazón) y cómo está construida (tipo de madera, uniones)? | ¿De qué material es la estructura o armazón (tipo de madera, metal…)?<br>*el material (material) y las uniones (construcción) toman otro rasgo y otra importancia* | `cat.sofas/28` ¿Cómo están unidas las piezas de la estructura (tipo de uniones)? (construccion, complementario) |
| `cat.sofas/11` | ¿Con qué materiales están rellenos el asiento y el respaldo y cómo están construidos los cojines (tipo y densidad de la espuma, muelles, plumas…)? | ¿Con qué materiales están rellenos el asiento y el respaldo (tipo y densidad de la espuma, plumas, fibra…)?<br>*el relleno (material) y la construcción de los cojines (construcción) toman otro rasgo y otra importancia* | `cat.sofas/29` ¿Cómo están construidos los cojines del asiento (muelles ensacados, capas de espuma, sistema antihundimiento…)? (construccion, complementario) |
| `cat.sofas/15` | ¿Cómo son las patas o la base: material, acabado o color y altura? | ¿Qué estilo y qué acabado o color tienen las patas o la base? · fuente añadida: `amz:SOFA.furniture_leg.color`, `amz:SOFA.furniture_leg.style`<br>*el material (material) y la altura de las patas (medida) toman otro rasgo y otra importancia que su aspecto (estética); SOFA.furniture_leg se cita por sus partes* | `cat.sofas/30` ¿De qué material son las patas o la base? (material, principal)<br>`cat.sofas/31` ¿Qué altura tienen las patas? (medida, principal) |
| `cat.sofas/16` | — | ver regla 2 | — |
| `cat.sofas/23` | ¿Qué normas de seguridad o certificaciones cumple, en particular sobre el comportamiento ante el fuego y sobre emisiones o sustancias? | (misma pregunta) · fuente añadida: `amz:SOFA.material_feature=No tóxico`<br>*recibe de /24 la declaración de materiales no tóxicos (seguridad: emisiones o sustancias)* | — |
| `cat.sofas/24` | ¿Qué características ambientales o de salud tienen sus materiales (reciclados, madera recuperada, naturales, orgánicos, no tóxicos)? | ¿Qué características ambientales tienen sus materiales (reciclados, madera recuperada, naturales, orgánicos)? · fuente añadida: `amz:SOFA.material_feature=Madera recuperada`, `amz:SOFA.material_feature=Natural`, `amz:SOFA.material_feature=Orgánico`, `amz:SOFA.material_feature=Reciclado`<br>*lo no tóxico (seguridad) pasa a /23; aquí quedan las características ambientales (material), citadas por sus valores* | — |
| `cat.soperas/01` | ¿Qué capacidad tiene (en litros o centilitros) y para cuántos comensales sirve? | ¿Qué capacidad tiene (en litros o centilitros)?<br>*para cuántos comensales sirve no lo recoge DISHWARE_BOWL.capacity y es otro rasgo (uso): sale como inferida* | `cat.soperas/09` ¿Para cuántos comensales está pensada? (uso, complementario, inferida) |
| `cat.soperas/04` | ¿Se puede usar en el horno o en el congelador, o mantiene el calor (aislada)? | ¿Se puede usar en el horno o en el congelador?<br>*conservar el calor (prestación) toma otro rasgo que los usos térmicos (uso)* | `cat.soperas/10` ¿Mantiene el calor (aislada)? (prestacion, complementario) |
| `cat.toallas/01` | ¿Qué tipo de toalla es por su uso y tamaño (lavabo, ducha, sábana de baño, bidé, pelo…) y qué medidas tiene (largo × ancho en cm)? | ¿Qué medidas tiene la toalla (largo × ancho en cm)?<br>*las medidas (medida que fija lo vendido) y el tipo por su uso (identidad) toman otro rasgo y otra importancia* | `cat.toallas/09` ¿Qué tipo de toalla es por su uso (lavabo, ducha, sábana de baño, bidé, pelo, playa…)? (identidad, principal) |
| `cat.zapatillas-para-bebes-y-ninos/01` | — | ver regla 2 | — |
| `cat.zapatillas-para-bebes-y-ninos/03` | ¿De qué material es la plantilla y es extraíble? | ¿De qué material es la plantilla?<br>*el material (material) y que sea extraíble (construcción) toman otro rasgo* | `cat.zapatillas-para-bebes-y-ninos/09` ¿Es extraíble la plantilla? (construccion, principal) |
| `cat.zapatillas-para-bebes-y-ninos/05` | ¿Para qué superficies o entorno está pensada la suela (calle, interior, multisuelo, tierra…) y deja marcas en suelos de interior? | ¿Para qué superficies o entorno está pensada la suela (calle, interior, multisuelo, tierra…)?<br>*dejar marcas (prestación) toma otro rasgo que la superficie de uso (uso)* | `cat.zapatillas-para-bebes-y-ninos/10` ¿Deja marcas en suelos de interior? (prestacion, complementario) |

## Regla 4: cada componente con fuente; sin ella, cuestión inferida

21 requisitos.

| Requisito | Antes | Después | Requisitos nuevos |
|---|---|---|---|
| `cat.bloques-de-lija/01` | ¿Qué medidas tiene la superficie de lijado (largo × ancho) y, por tanto, qué formato de hoja abrasiva admite? | ¿Qué medidas tiene la superficie de lijado (largo × ancho)?<br>*el formato de hoja que admite no tiene fuente en TOOLS.size; lo pregunta ya la inferida /07 (compatibilidad de hojas), así que no se propone otra* | — |
| `cat.bloques-de-lija/08` | ¿Para qué trabajos o superficies está pensado (grandes superficies, detalle, madera, pintura, masilla; uso aficionado o profesional)? | ¿Para qué nivel de uso (aficionado o profesional) y entorno (interior o exterior) está pensado?<br>*los trabajos y las superficies no los recogen TOOLS.specific_uses_for_product ni TOOLS.product_grade (nivel de uso y entorno): salen como inferida* | `cat.bloques-de-lija/10` ¿Para qué trabajos o superficies está pensado (grandes superficies o detalle; madera, pintura, masilla…)? (uso, principal, inferida) |
| `cat.botas/07` | — | ver regla 1 | — |
| `cat.botellas-de-agua/08` | ¿Es apta para congelador o microondas, o para bebidas calientes o con gas? | ¿Es apta para el congelador?<br>*solo tiene fuente el congelador (special_feature=Congelable); las bebidas calientes o con gas ya las pregunta /07 (para qué bebidas), y el microondas se retira* | — |
| `cat.calzado/01` | ¿Qué talla tiene cada variante y en qué sistema de tallas (EU, UK, US…) se expresa, con su equivalencia? | ¿Qué talla tiene cada variante y en qué sistema de tallas (EU, UK, US…) se expresa?<br>*la equivalencia entre sistemas no la recoge ninguna fuente (footwear_size da sistema, clase y talla): sale como inferida* | `cat.calzado/25` ¿Con qué tallas de otros sistemas o con qué longitud del pie (cm) se corresponde la talla? (uso, principal, inferida) |
| `cat.calzado/05` | ¿Qué altura de tacón tiene (plano, bajo, medio, alto) y cuánto mide? | ¿Qué altura tiene el tacón (plano, bajo, medio o alto)?<br>*«y cuánto mide» pedía la medida en cm, sin fuente en heel-height-type; no es un componente aparte, sino otra expresión de la altura (RI-06), así que no se propone inferida* | — |
| `cat.camas-de-enfriamiento-para-mascotas/01` | — | ver regla 3 | — |
| `cat.cd-de-musica/04` | ¿Cuándo se publicó la grabación y cuándo esta edición? | ¿Cuándo se publicó esta edición?<br>*ABIS_MUSIC.publication_date es la fecha de la edición; la de la grabación original no tiene fuente: sale como inferida* | `cat.cd-de-musica/12` ¿Cuándo se publicó originalmente la grabación? (identidad, principal, inferida) |
| `cat.cd-de-musica/07` | — | ver regla 2 | — |
| `cat.comida-para-perros/07` | ¿Qué cantidad neta contiene (peso o volumen por envase y número de envases)? | (misma pregunta) · fuente añadida: `amz:PET_FOOD.number_of_items`<br>*el número de envases no tenía fuente: lo recoge PET_FOOD.number_of_items, que se añade* | — |
| `cat.comida-para-perros/08` | ¿Qué ingredientes contiene y en qué proporción? | ¿Qué ingredientes contiene?<br>*PET_FOOD.ingredients enumera los ingredientes, sin su proporción: la proporción sale como inferida* | `cat.comida-para-perros/17` ¿En qué proporción lleva sus ingredientes principales (porcentaje de carne, pescado, cereales…)? (material, principal, inferida) |
| `cat.comida-para-perros/15` | ¿Qué composición analítica declara (proteína bruta, grasa bruta, fibra bruta, materia mineral, humedad) y qué aporte energético? | ¿Qué composición analítica declara (proteína bruta, grasa bruta, fibra bruta, materia mineral, humedad)?<br>*el aporte energético no lo exige el Reglamento 767/2009 (11.3, 17.1.f) ni lo recoge otra fuente del requisito: sale como inferida* | `cat.comida-para-perros/18` ¿Qué aporte energético tiene (kcal por kg o por ración)? (material, principal, inferida) |
| `cat.discos-y-lp/04` | ¿Cuándo se publicó la grabación y cuándo esta edición? | ¿Cuándo se publicó esta edición?<br>*ABIS_MUSIC.publication_date es la fecha de la edición; la de la grabación original no tiene fuente: sale como inferida* | `cat.discos-y-lp/14` ¿Cuándo se publicó originalmente la grabación? (identidad, principal, inferida) |
| `cat.lijadoras-orbitales/01` | ¿Qué tipo de movimiento tiene (orbital o roto-orbital/excéntrico) y con qué diámetro de órbita? | ¿Qué tipo de movimiento tiene (orbital o roto-orbital/excéntrico)?<br>*los nodos de Amazon dan el tipo de movimiento, no el diámetro de órbita: sale como inferida* | `cat.lijadoras-orbitales/03` ¿Qué diámetro de órbita tiene (mm)? (prestacion, principal, inferida) |
| `cat.lijadoras/05` | ¿A qué velocidad trabaja (rpm u oscilaciones por minuto) y es regulable? | ¿A qué velocidad trabaja (rpm u oscilaciones por minuto)?<br>*SANDER.maximum_rotational_speed da la velocidad máxima, no si se regula: sale como inferida* | `cat.lijadoras/14` ¿Se puede regular la velocidad? (prestacion, principal, inferida) |
| `cat.mochilas/11` | ¿Lleva materiales de origen animal, es vegana o lleva materiales reciclados? | ¿Lleva materiales de origen animal o es vegana?<br>*los materiales reciclados no los recoge bag-case-features (solo Producto vegano): salen como inferida* | `cat.mochilas/16` ¿Lleva materiales reciclados? (material, complementario, inferida) |
| `cat.mochilas/13` | ¿Tiene compartimento o funda protectora para dispositivos (portátil, tableta) y hasta qué tamaño de pantalla? | (misma pregunta) · fuente añadida: `amz:BACKPACK.compatible_device_size_maximum`<br>*el tamaño de pantalla no tenía fuente en el requisito: lo recoge BACKPACK.compatible_device_size_maximum, que las hijas ya excluían por estar cubierto aquí* | — |
| `cat.sofas-cama/02` | — | ver regla 3 | — |
| `cat.sofas/18` | ¿Qué funciones eléctricas incorpora (puertos USB, iluminación, altavoz, calefacción, masaje) y cómo se alimentan? | ¿Qué funciones eléctricas incorpora (puertos USB, iluminación, altavoz, calefacción, masaje)?<br>*cómo se alimentan no lo recoge ninguna fuente (solo valores de características): sale como inferida condicionada* | `cat.sofas/33` ¿Cómo se alimentan sus funciones eléctricas (enchufe, batería)? (uso, complementario, inferida; si incorpora funciones eléctricas) |
| `cat.sofas/25` | — | ver regla 2 | — |
| `cat.soperas/01` | — | ver regla 3 | — |

## Retirado

- `cat.botellas-de-agua/08`: el uso en microondas sale de la pregunta sin cuestión inferida. No tiene fuente y no es una cuestión de toda la clase de las botellas de agua. Queda en `excluded`; las bebidas calientes o con gas ya las pregunta /07.
- `cat.calzado/22`: la rigidez de la caña no se retira: pasa a `cat.botas/24`, con `BOOT.item_firmness_description`.
- Corrección editorial: `cat.mochilas-escolares/04` decía «rígida o reforzada, con base reforzada»; ahora, «blanda, rígida o híbrida, con base reforzada», como `BACKPACK.shell_type` y `cat.mochilas-para-portatil/04`.

## Capa general (D-065)

Al aprobar la información resolutiva de la capa general, el usuario pidió separar sus requisitos compuestos, en dos rondas: primero con la regla 3 estrecha y después también las partes de igual importancia. Artefactos: `INTAKE 2026-10-26-general-layer-formulation` y `-2`. Las preguntas cambiadas o nuevas:

| Requisito | Antes | Después | Importancia |
|---|---|---|---|
| `gen/01` | ¿Qué es el producto y qué incluye exactamente? | ¿Qué es el producto? | crítico |
| `gen/21` | (nuevo) | ¿Qué incluye exactamente la oferta? | crítico |
| `gen/02` | ¿Qué marca y modelo es? | ¿Qué marca es? | principal |
| `gen/24` | (nuevo) | ¿Qué modelo es? | principal |
| `gen/04` | ¿Cuál es el precio total que paga el comprador, con impuestos y envío a España? | ¿Cuál es el precio con impuestos incluidos? | crítico |
| `gen/25` | (nuevo) | ¿Cuánto cuesta el envío a España? | crítico |
| `gen/06` | ¿Está disponible y en qué variantes? | ¿Está disponible? | crítico |
| `gen/09` | Modalidades de entrega o recogida | ¿Qué modalidades de entrega o recogida ofrece? | complementario |
| `gen/11` | ¿Se puede desistir o devolver, en qué condiciones y plazo, con qué coste de devolución, y cuándo no procede? | ¿Se puede desistir o devolver, en qué plazo y en qué condiciones? | principal |
| `gen/26` | (nuevo) | ¿Qué coste de devolución asume el comprador? | principal |
| `gen/27` | (nuevo) | ¿Cuándo no procede el desistimiento o se pierde el derecho? | principal |
| `gen/12` | ¿Qué garantía legal y, si las hay, qué garantías comerciales y asistencia posventa tiene? | ¿Qué garantía legal de conformidad tiene? | principal |
| `gen/22` | (nuevo) | Si tiene garantía comercial, ¿cuál es y en qué condiciones? | principal |
| `gen/28` | (nuevo) | Si tiene asistencia o servicios posventa, ¿cuáles son y en qué condiciones? | principal |
| `gen/15` | ¿Qué opiniones de compradores tiene y, si se publican, cómo se garantiza que proceden de compradores reales? | ¿Qué opiniones de compradores tiene? | complementario |
| `gen/23` | (nuevo) | Si publica opiniones de compradores, ¿cómo garantiza que proceden de compradores reales? | complementario |
| `gen.variantes/01` | ¿Qué variantes hay y en qué se diferencian? | ¿Qué variantes hay? | crítico |
| `gen.variantes/02` | (nuevo) | ¿Qué variantes están disponibles? | crítico |
| `gen.variantes/03` | (nuevo) | ¿En qué se diferencian las variantes? | crítico |
| `gen.unidad-no-nueva/01` | ¿Por qué motivo (exposición, devolución, tara, fin de serie…) y con qué marcas o defectos se vende, y qué unidad se entrega? | ¿Con qué marcas o defectos se vende la unidad? | principal |
| `gen.unidad-no-nueva/02` | (nuevo) | ¿Qué unidad se entrega? | principal |
| `gen.unidad-no-nueva/03` | (nuevo) | ¿Por qué motivo no es nueva (exposición, devolución, tara, fin de serie…)? | complementario |
| `gen.descuento/01` | ¿Desde qué precio de referencia y en qué condiciones se aplica el descuento? | ¿Desde qué precio de referencia se aplica el descuento? | complementario |
| `gen.descuento/02` | (nuevo) | ¿En qué condiciones se aplica el descuento? | complementario |
| `gen.precio-personalizado/01` | ¿El precio está personalizado por una decisión automatizada y con qué parámetros? | ¿Está personalizado el precio por una decisión automatizada? | principal |
| `gen.precio-personalizado/02` | (nuevo) | ¿Con qué parámetros se ha personalizado el precio? | principal |
| `gen.elementos-digitales/01` | ¿Qué funcionalidad y qué compatibilidad e interoperabilidad tiene? | ¿Qué funcionalidad tienen sus elementos digitales? | principal |
| `gen.elementos-digitales/02` | (nuevo) | ¿Con qué aparatos y programas son compatibles sus elementos digitales? | principal |
| `gen.elementos-digitales/03` | (nuevo) | ¿Qué medidas técnicas de protección se aplican a sus elementos digitales? | principal |
| `gen.elementos-digitales/04` | (nuevo) | ¿Con qué aparatos y programas son interoperables sus elementos digitales? | principal |
| `gen.suscripcion/01` | ¿Qué duración, duración mínima, condiciones de resolución y depósitos tiene? | ¿Qué duración tiene el contrato o, si es indefinido o se prorroga automáticamente, en qué condiciones se resuelve? | por fijar |
| `gen.suscripcion/02` | (nuevo) | ¿Qué duración mínima tienen las obligaciones del comprador? | por fijar |
| `gen.suscripcion/03` | (nuevo) | ¿Qué depósitos u otras garantías financieras exige y en qué condiciones? | por fijar |

Quedan juntos `gen/16` (sí o no con su detalle), `gen/17` y `gen/18` (nombre y dirección, ejemplo de D-060) y `gen/19` (una sola exigencia del GPSR). Incidencias abiertas: I-26 (condicionados sobre hechos de la oferta en el bloque universal) e I-27 (`gen.precio-personalizado/01` repite su disparador).

## Información resolutiva

- **Bloques de categoría:** 1310 aportaciones en 440 requisitos: 950 de origen «referencias», extraídas de sus fuentes con `bin/train resolving refs`, y 360 inferidas (provisionales). Los 35 requisitos inferidos solo llevan inferidas. Aportaciones por requisito: 63 con 1, 143 con 2, 91 con 3, 72 con 4, 33 con 5, 32 con 6, 5 con 7, 1 con 8.
- **Redacción.** La redactaron cuatro agentes en paralelo, por grupos de bloques, con un mismo brief (las reglas de D-062 a D-064 y ejemplos) y un validador común. Cada componente de la pregunta con fuente tiene al menos una aportación de referencias; las fuentes que no responden a ninguna parte de la pregunta se quedan sin aportación (pertinencia ≠ proximidad temática).
- **Fuentes normativas** (composición textil, información alimentaria, piensos, confituras): origen «referencias» con la ley en el respaldo, solo con lo que la pregunta ya dice que exige la norma (I-28).
- **Capa general:** 89 aportaciones, aprobadas por el usuario: 60 de origen «marco» (la letra del TRLGDCU 97.1 o del GPSR 19 que es fuente del requisito), 28 inferidas (sin apoyo en la ley, provisionales) y 1 de referencias (`gen/20`).
- **Observación en las fichas:** ninguna aportación todavía. Las salidas de estas ejecuciones (reglamento v2) no dicen qué aportación es cada hecho; se medirá en T-032.
- `bin/model check --catalog` (nuevo) comprueba en los 60 bloques y en la capa general los ids, los rasgos, el origen y las fuentes, y la información resolutiva: correcto.

## Entrenamiento

Pasos: `bin/train index`, `induce` y `compile` sobre eci-a, eci-b, v4-a y v4-b. El índice se rehace para que las fuentes que cambiaron de requisito tomen el rasgo nuevo: 1025 fuentes, y cuatro compartidas entre requisitos de rasgos distintos que salen del índice. Los 60 bloques pasan a versión nueva (todos reciben información resolutiva).

| Métrica | Reglas 5 · catálogo anterior | Reglas 6 · catálogo nuevo |
|---|---|---|
| Requisitos del catálogo | 382 | 440 |
| Coherencia del catálogo (incoherentes) | 0 | 0 |
| Coherencia de los modelos (incoherentes) | 2 | 2 |
| Coherencia por requisito (pares contra la mayoría) | 17 de 578 | 17 de 578 |
| Estabilidad de la importancia | 908/908 | 908/908 |
| Requisitos del catálogo sin regla | 0 | 0 |
| Coherencia de relevancia | 0 | 0 |
| Hechos declarados sin pregunta | 32 | 32 |

Sobre el catálogo nuevo, las reglas 5 daban 18 pares contra la mayoría y 7 requisitos sin regla (rasgos nuevos en su clase); la candidata 6 los deja en 17 y 0, y se acepta la importancia. La relevancia se descarta (sin mejora), como en el ciclo anterior.

Reglas que cambian: 18 nuevas o cambiadas y 14 retiradas; las excepciones por requisito pasan de 104 a 103.

- Nuevas o cambiadas: `cat.cd-de-musica/07@me-3-3` principal, `cat.juguetes-para-perros/04@ap-2-3-7` principal, `cat.juguetes-para-perros/08@ap-2-3-7` complementario, `cat.mochilas/03@lb-1` principal, `certificacion-origen@aa-8` complementario, `contenido@ap-2-3-3` complementario, `contenido@fr-22` principal, `identidad@hg-15-4` principal, `magnitud@ap-2-3-7` complementario, `magnitud@ap-2-9` complementario, `magnitud@fr-22-7` principal, `material@lb-1` complementario, `material@lb-6` principal, `prestacion@ap-2-3-7` complementario, `prestacion@ap-2-9` principal, `seguridad@hg-3-64` complementario, `uso@me-3-3` complementario, `uso@me-3-4` principal.
- Retiradas: `cat.cd-de-musica/10@me-3-3` complementario, `cat.juguetes-para-perros/09@ap-2-3-7` complementario, `cat.mochilas/03@lb-1-12` principal, `cat.mochilas/03@lb-1-16` principal, `cat.mochilas/11@lb-1` complementario, `contenido@ap-2-3` complementario, `contenido@fr-22-7` principal, `material@lb` principal, `material@lb-1-12` complementario, `material@lb-1-16` complementario, `prestacion@ap-2-3-7` principal, `prestacion@ap-2-9` complementario, `prestacion@ap-2-9-4` principal, `uso@me-3` principal.

Requisitos que conservan su id y cambian de importancia: `cat.camas-para-mascotas/08` complementario → principal (`imp:prestacion@ap-2-9`); `cat.camas-para-mascotas/09` complementario → principal (`imp:prestacion@ap-2-9`); `cat.camas-para-mascotas/10` complementario → principal (`imp:prestacion@ap-2-9`). La etiqueta del nuevo `cat.camas-para-mascotas/14` (soporte, principal) inclina la regla `prestacion@ap-2-9`, que estaba casi empatada en los votos. Los demás requisitos mantienen su importancia.

Importancia compilada de los requisitos nuevos: 31 complementario, 27 principal. No hay críticos nuevos: la parte que conserva el id mantiene la importancia del original y, con ella, su excepción (por ejemplo, `cat.sofas/01` sigue crítico en Sofás).

## Dudas y observaciones

- **Fuentes que encajan mal** (los agentes las dejaron sin aportación o la ligaron con reservas):
  - `ABIS_MUSIC.audio_encoding` no es el código SPARS (AAD/ADD/DDD) de `cat.cd-de-musica/08` y `cat.discos-y-lp/10`;
  - `AUTO_OIL.viscosity_level` no da el grado SAE;
  - `DISHWARE_BOWL.capacity` y `length_range` tienen descripciones de otros productos;
  - `SHOES.shoe_type` da tipos generales de calzado;
  - `care-instructions` tiene valores textiles en joyería y cocina;
  - `FOOD.serving_recommendation` es una ración, no un uso.
  Es candidato para la revisión de fuentes que haga el entrenamiento (relevancia).
- **`cat.aceite-para-motores-de-vehiculos/06`** pregunta por «flujo, filtración», que son prestaciones de filtros heredadas de un atributo de Shopify compartido: puede que haya que reformularla o excluirla.
- **Componentes cubiertos solo por inferidas**, sin fuente que los recoja: la temperatura de lavado, el lavavajillas, la longitud útil del piercing, el número de grano, el ingrediente principal del pienso, entre otros. Son candidatos a cuestiones o fuentes en ciclos futuros.
- **Partes con igual rasgo e importancia que siguen juntas en los bloques de categoría** (regla 3 estrecha): su granularidad sigue aplazada al trabajo de los AC (OQ-22). En la capa general el usuario sí las separó (D-065).

