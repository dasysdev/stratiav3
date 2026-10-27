# Criterios de elección, derivación de prestaciones y descripción de los requisitos

**Estado:** pendiente de procesar. El usuario pidió dejarlo anotado «para cuando toque actualizar».

## Contexto

Este artefacto sale de las sondas de People Also Ask (PAA) en google.es, hechas con el modelo de demanda de sábanas Coralina (`demand-engine/var/runs/2026-10-26-v6-b/sabanas-coralina-999.model.md`; sondas en `demand-engine/var/paa/`). Las preguntas valorativas de PAA («¿Cuál es el mejor tipo de sábana para dormir?», «¿Qué se arruga más, el satén o el percal?») no son requisitos informativos:

- no preguntan por una oferta;
- no son neutrales respecto de la respuesta;
- dependen del comprador.

Revelan, en cambio, los **criterios de elección** de la clase: los aspectos por los que los compradores juzgan si una oferta les conviene (frescor o abrigo, arrugas, durabilidad, tacto…). La expresión «criterios de elección» ya aparece en demand-model (vía MPIR). Se prefiere a «criterios de evaluación», que se confundiría con los criterios de aceptación.

Fuera de este artefacto, sin decidir: si PAA se adopta como vía de construcción del modelo de demanda, y la excepción a D-042 (robots.txt de Google) que exigiría.

## 1. Derivar una prestación de un atributo no resuelve el requisito de la prestación

Palabras del usuario:

> en el ejemplo. derivar frescura de «percal 100 % algodón» no es aceptable. Demasiado nivel de derivación. pero eso ya es tarea de la valoración de criterios de aceptación. pero para ello sí necesitamos requisitos informativos para hacer esa evaluación.

- Que una ficha declare el tejido o la composición («percal», «100 % algodón») no resuelve un requisito sobre la prestación («¿qué sensación térmica ofrece?»). La derivación tiene demasiados pasos y se apoya en conocimiento del dominio.
- Quien lo dictamina es la **valoración de los criterios de aceptación**, en la auditoría, no el modelo de demanda.
- Para que la auditoría pueda dictaminarlo, el requisito de la prestación **tiene que existir** en el modelo.

## 2. Los criterios de elección generan requisitos en algunos casos

Palabras del usuario:

> Entonces los criterios de elección en algunos casos sí deberían generar requisitos

Regla propuesta por Claude; el usuario aprobó registrarla («OK»). Un criterio de elección genera un requisito cuando cumple **todas** estas condiciones:

| # | Condición | Si no se cumple |
|---|---|---|
| C1 | Ningún requisito existente lo responde sin derivar. | Ya está cubierto. Ejemplo: la «calidad» medida en hilos la cubre `cat.sabanas/03`. |
| C2 | Es un hecho que la oferta puede declarar (una prestación, un resultado de ensayo, una indicación de uso). | Si solo lo puede juzgar quien compra («que me guste»), no genera requisito. |
| C3 | Se aplica a toda la clase o a una especialización, no a un comprador. | Es una condición de compra o un escenario. |
| C4 | Se puede formular neutral y sobre la oferta. | Si solo admite «mejor/peor» (marca, reputación), se descarta. |

Cómo se aplica:

- El requisito resultante es un requisito ordinario; en el catálogo de rasgos, casi siempre `prestacion`. **No** se crea un concepto nuevo en el modelo.
- El criterio de elección queda como **fundamento** del requisito.
- Su información resolutiva es la declaración de la prestación, un ensayo o una certificación. Nunca el atributo del que se deduciría la prestación (punto 1).
- Que los compradores usen un criterio para elegir no prueba su importancia relativa: la importancia sigue saliendo de las reglas.

Ejemplos de las sondas, para la clase de sábanas:

| Criterio de elección | Preguntas PAA que lo apoyan | ¿Genera requisito? |
|---|---|---|
| Frescor o abrigo | «¿Qué calienta más, la franela o la coralina?», «¿Qué tipo de sábanas no dan calor?» | Sí. `inf/01` cubre en parte el nivel de abrigo; la sensación térmica solo existe en las fundas (`cat.fundas-de-almohada/05`). |
| Arrugas | «¿Qué se arruga más, el satén o el percal?», «¿Se arruga mucho el algodón percal?» | Sí. Hoy solo existe en las fundas (`cat.fundas-de-almohada/06`). |
| Durabilidad | «¿Cuánto dura la coralina?» | Sí. Mismo caso que las arrugas. |
| Ajuste de la bajera | «¿Cómo hacer para que no se salga la sábana de abajo?» | Ya cubierto (`inf/02`, `cat.sabanas-ajustables/01`). |
| Calidad en general | «¿Cuáles son las sábanas de mejor calidad?» | No: se descompone en los criterios anteriores (C1). |
| Marca | «¿Cuál es la mejor marca de sábanas en España?» | No (C4). |

## 3. Los requisitos informativos llevan una descripción

Palabras del usuario:

> Los requisitos informativos necesitan una descripción. A veces el título puede ser bastante abstracto y la descripción debe ayudar a concretarlo.

La descripción concreta el título. El usuario aceptó este patrón de tres partes:

1. qué se pregunta en concreto, con ejemplos de lo que abarca;
2. qué tipo de información lo responde;
3. qué no lo responde y con qué requisito vecino no se confunde.

Ejemplos que el usuario dio por buenos:

- **cat.fundas-de-almohada/06 · ¿Qué resistencia al uso y al lavado tiene?** — Si la pieza mantiene su aspecto y sus medidas con el uso y los lavados: si destiñe, encoge, forma bolitas, se arruga, se mancha o se desgarra con facilidad. Lo responde una declaración del vendedor o del fabricante sobre esas prestaciones, o el resultado de un ensayo (solidez del color, estabilidad dimensional). No lo responden el material ni el tejido por sí solos («percal», «100 % algodón»). Tampoco las instrucciones de lavado: son otro requisito, `cat.ropa-de-casa/02`.
- **¿Qué sensación térmica ofrece la sábana?** (candidato) — Si la sábana resulta fresca o abriga al dormir, y para qué temporada o clima está pensada. Lo responde una declaración expresa («fresca y transpirable», «cálida, para invierno») o un ensayo de frescor o de transpirabilidad. No lo responden el tejido ni la composición («percal», «coralina»): deducir la sensación térmica de ellos es una derivación que no se admite.
- **gen/21 · ¿Qué incluye exactamente la oferta?** — Todas las piezas, unidades y accesorios que recibe el comprador por el precio indicado. Incluye también lo que aparece en las imágenes o en el nombre pero no se entrega (por ejemplo, el relleno en la foto de una funda nórdica; ejemplo hipotético). En un juego, la composición de piezas es otro requisito, `esp.juego/01`.
- **cat.sabanas-ajustables/01 · ¿Hasta qué altura de colchón se ajusta?** — La altura máxima de colchón, o el rango de alturas, que admite la bajera, normalmente como profundidad del bolsillo en cm. Cómo se sujeta al colchón es otra cuestión, `inf/02`.

**Punto abierto para el procesamiento.** Las partes 2 y 3 se solapan con la información resolutiva (D-062 a D-064) y con el perfil de resolución y pertinencia (OQ-03). Propuesta de Claude, sin decidir: la descripción es prosa para personas y agentes, y la información resolutiva es la lista estructurada. La descripción no repite esa lista.
