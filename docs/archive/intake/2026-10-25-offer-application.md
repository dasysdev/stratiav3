# Modelo del producto, aplicación de la oferta y promociones

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-019). Lo forman cinco mensajes del usuario y las propuestas de Claude que el usuario aprobó («todo aparece OK»; «respuesta afirmativa a tus recomendaciones»). La ortografía de los mensajes del usuario está normalizada.*

## 1. Promociones y descuentos

Usuario: «¿Consideras que las promociones y descuentos podríamos tratarlos como bloques de requisitos que siempre están presentes? No tratarlo como una aplicación. Ya que responder que no hay promoción o descuento podría ser útil y esto podría aplicar a cualquier producto del mundo. Estudiemos esto.»

Estudio de Claude (resumen):

- Hoy la capa general solo tiene la parte condicionada (`gen.descuento`: «¿Desde qué precio de referencia y en qué condiciones se aplica el descuento?», complementaria) y entra en la clave y el nombre («— con descuento»). No hay ninguna pregunta universal sobre si hay promoción.
- A favor: un «no» fundamentado resuelve la cuestión (invariante 13) y es útil; la identidad del modelo dejaría de cambiar con las rebajas; es el patrón que ya se usa para estado (gen/07 + `gen.unidad-no-nueva`) y variantes (gen/06 + `gen.variantes`).
- En contra: casi ninguna ficha dice «sin promoción», y el «no» habría que derivarlo del precio sin tachar (invariante 11); los detalles (precio anterior, condiciones, vigencia) solo existen si hay descuento.
- Borrador de preguntas: «¿Tiene la oferta alguna promoción o descuento vigente (rebaja, cupón, regalo, unidades gratis…) y en qué consiste?», siempre (un «no» fundamentado la resuelve), complementaria; «¿Cuál es el precio anterior de referencia y cuánto se rebaja?», si hay reducción de precio; «¿En qué condiciones se aplica y hasta cuándo es válida?», si hay promoción.

## 2. Requisitos condicionados en gris

Usuario: «Los condicionales quedarían como requisitos generales pero que pueden no ser aplicables con resultado NA, desactivados, "en gris". ¿Es así?»

Respuesta de Claude: sí, con tres precisiones. (1) En gris solo quedan los detalles; la pregunta universal nunca es NA. (2) Lo que los pone en gris es el hecho declarado, como hoy (D-037): si la ficha no declara descuento, los detalles son NA y la duda de si hay promoción se valora una sola vez, en la pregunta universal. (3) El detalle está siempre en el modelo; en la oferta que no lo tiene aparece en gris («no aplica: no se declara descuento») y la auditoría lo registra como NA justificado. El canon ya lo permite: NA es «el criterio o requisito no corresponde a la cuestión», se justifica y se separa de las unidades pertinentes; e «incluir un RI en el catálogo no obliga a aplicarlo a todas las ofertas».

## 3. El modelo va con el producto; la aplicación, con la oferta

Usuario: «Consideremos sacar la aplicación de la denominación. Ya que parecen ser cuestiones de estado temporal. Entonces las vinculamos a la oferta y no al producto. Modelo de demanda se vincula al producto, aplicación a la oferta. De los 14 casos, ¿cómo aplicaría esta idea? Estudiémoslo.»

Estudio de Claude (resumen):

- **Modelo de demanda (producto):** bloques de categoría y especialización; nombre «Categorías (alias) · especializaciones», sin aplicación.
- **Aplicación (oferta):** condiciones activas de esa oferta; no forma parte del nombre ni de la clave del modelo. Lo que se audita es la oferta = modelo de su producto + su aplicación; lo que no se da en esa oferta queda en gris (NA justificado).
- En los 14 casos: las fundas nórdicas 401 y 642 comparten modelo («Fundas de nórdico + Sábanas ajustables + Fundas de almohada · juego») y solo difieren en la oferta (con descuento); el Stressless de outlet tiene el mismo modelo que uno nuevo de piel («Sofás · tapicería de piel»), con la oferta «unidad no nueva, con descuento, cantidad limitada»; 13 modelos para 14 ofertas.
- Con la aplicación fuera de la identidad, para las promociones basta añadir la pregunta universal «¿tiene promoción o descuento?», si se quiere que un «no» cuente; los detalles siguen siendo condiciones de la oferta, en gris cuando no aplican.
- Tres puntos: `gen.elementos-digitales` es propiedad del producto y pasaría al modelo, como un bloque más de la clave («Televisores · con elementos digitales»); las variantes se cuentan como oferta (la misma tienda o otra puede ofrecer más o menos medidas); una especialización de oferta (D-037: la salud de la batería en un móvil reacondicionado) iría con la oferta.
- Cambios en el canon: D-033 («Identidad = modelo de requisitos + aplicación concreta» pasa a «el modelo se identifica por sus bloques; la aplicación es de la oferta»), D-038 (clave y nombre sin aplicación), D-027 y D-037, y el ejemplo «Sofás · tapicería de piel — unidad no nueva, con descuento».

Usuario: «Todo aparece OK. Dos cosas para cerrar:
- La aplicación "—" no es coherente. La aplicación es "por defecto", "general" u otras opciones. Estudia qué término tiene más sentido, propón términos.
- Cómo se resolvería que la aplicación aporta nuevos requisitos que no podrían haberse inferido sin la aplicación. Caso 3 de estado de batería.»

## 4. Término para la oferta sin condiciones

Propuesta de Claude: una oferta sin condiciones activas no es una ausencia sino un resultado (el clasificador ha comprobado que no se declara ninguna: unidad nueva, presentación única, precio sin rebaja, stock sin límite, compra única). Términos estudiados: **estándar** (se entiende sin explicación y no se usa en el canon con otro sentido), ordinaria (recuerda la distinción legal entre venta ordinaria y promociones, pero solo cubre promociones), por defecto (ya se usa para «importancia por defecto» y suena a supuesto, no comprobado), general (choca con «capa general»), simple o básica (pueden leerse como de menor calidad). Recomendado: **estándar**. Ejemplos: «Cojines · material reciclado» — oferta estándar; «Botas · uso de equitación» — oferta con variantes; «Sofás · tapicería de piel» — oferta unidad no nueva, con descuento, cantidad limitada.

## 5. Requisitos que solo aparecen con una condición de la oferta

Propuesta de Claude: **la oferta nunca aporta requisitos; solo activa requisitos condicionados que ya viven en el modelo del producto.** La salud de la batería es una pregunta de smartphones que solo procede cuando la unidad no es nueva: su sitio es el bloque de la clase, como requisito condicionado («aplicable si la unidad no es nueva»), no la oferta. El smartphone nuevo y el reacondicionado tienen el mismo modelo; en el nuevo (oferta estándar) la pregunta está en gris (NA: la unidad es nueva); en el reacondicionado (oferta unidad no nueva) está activa, junto con `gen.unidad-no-nueva`.

- Descubrimiento: la primera vez que llega un smartphone reacondicionado, el clasificador propone la pregunta como cuestión inferida de la clase con la aplicabilidad «si la unidad no es nueva»; se usa como provisional y se encola; el entrenamiento la acepta y la incorpora al bloque de la clase como nueva versión. Con el catálogo grande, en cuanto haya ofertas reacondicionadas de una clase aparecen sus preguntas propias.
- Por qué no como especialización de oferta: la pregunta depende de la clase (un sofá reacondicionado no tiene batería); no hace falta ningún concepto nuevo (el requisito condicionado ya existe, D-024, y NA cubre lo que no aplica); el producto no cambia de modelo por estar reacondicionado. Desaparece la «especialización de oferta» que dejaba abierta D-037.
- Lo que no cubre: una condición de oferta que la capa general no tenga (por ejemplo, la preventa o reserva) habría que añadirla a la capa general, que es marco; el informe del entrenamiento la señalaría como hueco en lugar de inventarla.

Usuario: «Respuesta afirmativa a tus recomendaciones.»
