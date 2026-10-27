# Motor PAA

Recoge las preguntas de **«Más preguntas»** (People Also Ask) de google.es para un conjunto de semillas de una clase. Son preguntas de los compradores, filtradas por Google. PAA es una [vía de construcción](../../../../docs/10-model/construction-routes.md) del modelo de demanda ([D-094](../../../../docs/30-governance/decisions.md#d-094)): confirma requisitos, confirma o revisa cuestiones inferidas, descubre **criterios de elección** y **propone requisitos nuevos**. La regla C1–C4 decide cuándo un criterio de elección, o una pregunta factual que ningún requisito responde, genera un requisito ([D-091](../../../../docs/30-governance/decisions.md#d-091), [D-099](../../../../docs/30-governance/decisions.md#d-099)); un requisito que entra solo por PAA lleva origen «paa» ([D-097](../../../../docs/30-governance/decisions.md#d-097)).

Solo se conservan las **preguntas**. Las respuestas son texto de la IA de Google («Vista creada con IA»), no evidencia de ninguna página: **ni se leen ni se cargan** (ver [Una búsqueda](#una-búsqueda)).

## Legitimidad: excepción a D-042

El robots.txt de Google excluye `/search` para cualquier agente (`User-agent: *`, `Disallow: /search`). Sus condiciones de servicio (España, vigentes desde el 30-07-2026) prohíben el acceso automatizado que contravenga el robots.txt. El motor de captura aplica robots.txt a todas sus capturas ([D-042](../../../../docs/30-governance/decisions.md#d-042)); **este motor no lo hace**.

Es una excepción que decidió el usuario para **investigación y uso interno**, no para ofrecer un servicio, registrada en [D-096](../../../../docs/30-governance/decisions.md#d-096) con los límites de ejecución de abajo. Se limita a las búsquedas de este motor; cualquier otra captura sigue con las políticas de D-042.

Del principio del [motor de captura](../capture/README.md#principio) se mantiene todo lo demás:

- Chrome estable con ventana, sin banderas de automatización. Perfil y puerto propios (`var/paa/chrome-profile`, 9224), separados del Chrome de captura.
- Una sola ventana y una sola sesión: las búsquedas nunca van en paralelo.
- Una pausa entre búsquedas (ver [Límites de ejecución](#límites-de-ejecución)).
- Bloquea las peticiones de las respuestas de IA, como haría un bloqueador de contenido. No modifica el navegador ni el JavaScript de la página, y pide a Google menos datos de los que pediría una persona.
- Ante un desafío (`/sorry/`, CAPTCHA, 403/429) **para**: no lo resuelve, no rota IP y no aplica parches antidetección.

## Estrategia de semillas

Viene de dos sondas sobre la clase de sábanas (2026-10-26). La de 25 semillas, con 6 clics, dio 330 preguntas únicas en 82 minutos.

| Hallazgo | Consecuencia |
|---|---|
| El rendimiento **por clic** no cae hasta el sexto (≈ 1,7 preguntas útiles nuevas por semilla y clic). Un clic cuesta unos segundos; una búsqueda, más de un minuto con su pausa. | **Más clics y menos semillas.** 8 clics por búsqueda, con parada tras 2 clics que no añaden nada. |
| **Núcleo + material** (10 semillas) con 6 clics recogió **todos los tipos** de criterio y de requisito (el 43 % de las preguntas útiles). | Esas son las semillas por defecto. |
| Medida, construcción (hilos, colchón alto) y comparativas («X o Y») no aportaron ningún tipo nuevo; las comparativas repetían lo que traen las semillas de cada valor. | Fuera por defecto. |
| El tacto solo apareció con clics profundos. | No recortar clics para ahorrar tiempo. |
| Las 4 semillas repetidas, hora y media después, devolvieron las mismas preguntas en el mismo orden. | Una ejecución basta. |
| Un tercio de las preguntas es valorativo («¿cuál es la mejor…?») sin forzarlo. | No hacen falta semillas con marcos valorativos. |

**Regla:**

1. **Núcleo:** una semilla por cada categoría y especialización de la clave del modelo, con el nombre que se usa en el mercado español («sábana encimera», no «sábana plana»).
2. **Valores:** una semilla por valor del rasgo que más condiciona las prestaciones, tomado de las referencias. En los textiles es el material (Shopify `material`/`fabric`, Amazon `material`). Solo valores con uso en España.

Está calibrada con **una sola clase**. En otra, el rasgo de los valores puede ser otro (tecnología, tipo), y la regla se revisa con datos.

## Límites de ejecución

Decididos por el usuario (2026-10-26 y 2026-10-27): **pausa de 5 s entre búsquedas**, sin pausa larga, sin horario, sin tope diario y sin tope por hora. Un conjunto puede fijar cualquiera de ellos en su `pacing`.

| Límite | Valor | Fundamento |
|---|---|---|
| Búsquedas a la vez | Una: una ventana y una sesión | Una sola IP |
| Pausa entre búsquedas | 5 s | Decisión del usuario: se endurece cuando Google bloquee, no antes |
| Pausa larga | Ninguna | Ídem |
| Clics por búsqueda | 8, con parada tras 2 sin nada nuevo | Hasta 6, medido en las sondas; 8, en la prueba del 2026-10-27 (~2,4 s por clic) |
| Ante un bloqueo | Para **todo el motor** (`var/paa/engine.json`): Google bloquea la IP, no un conjunto. Reintento a las 6 h; tras el segundo bloqueo, parado hasta `paa unblock` | Como el MPIR |

Una búsqueda con 8 clics son unos 25 s de página: en marcha continua, unas 2 búsquedas por minuto.

> **Atención: qué hacer cuando Google bloquee.** Un bloqueo es una redirección a `/sorry/`, un CAPTCHA o una respuesta 403/429 (`paa status` lo muestra como «bloqueos del motor»). Entonces se añade una **pausa larga cada X búsquedas** en el `pacing` del conjunto (`long_every`, `long_pause_s`; por ejemplo, `[12, 18]` y `[60, 180]`). Si no basta, se alarga `pause_s`. Los valores se fijan con lo que se observe en ese bloqueo: cuántas búsquedas seguidas lo provocaron y cuánto tardó en levantarse. Se anotan aquí.

**Riesgo asumido:** la IP es la de la conexión desde la que se ejecuta. Si Google la marca, también verá CAPTCHAs quien busque desde ella durante horas.

## Uso

Módulo de [demand-engine](../../../README.md). Se ejecuta dentro del contenedor (`bin/run dev up`); `demand-engine/bin/paa` lanza `python -m demand_engine.paa` en él.

```bash
demand-engine/bin/paa list                  # conjuntos y su avance
demand-engine/bin/paa run sabanas           # busca las semillas pendientes, una a una
demand-engine/bin/paa status sabanas        # estado de cada semilla y bloqueos
demand-engine/bin/paa questions sabanas     # preguntas consolidadas (--json, con su procedencia)
demand-engine/bin/paa unblock               # tras revisar un bloqueo (es del motor)
```

`run` es reanudable: lo capturado no se repite, y un fallo o un bloqueo se reintentan en la siguiente ejecución. `--max N` limita las búsquedas; `--ignore-hours` ignora el horario, si el conjunto fija uno.

## Conjunto de semillas

`demand-engine/paa/<conjunto>.json`, en git. Lo que no se indica toma el valor por defecto (`DEFAULTS` en `store.py`):

| Campo | Contenido | Por defecto |
|---|---|---|
| `class` · `model` · `rule` | Clase, modelo de demanda del que sale y regla con que se hicieron las semillas | — |
| `seeds` | `[{"q": "sábanas", "group": "núcleo"}, …]` | — |
| `market` | `base`, `hl`, `gl` | `https://www.google.es`, `es`, `es` |
| `clicks` · `patience` | Preguntas que se abren por búsqueda · clics seguidos sin nada nuevo que la terminan | 8 · 2 |
| `pacing` | `pause_s` entre búsquedas, `dwell_s` antes del primer clic, pausa larga (`long_every`, `long_pause_s`), `daily_cap` (de todos los conjuntos: una IP), `hours`, `timezone` | 5 s, 1,5–4 s, sin pausa larga, sin tope, sin horario, Europe/Madrid |
| `block_retry_hours` | Espera tras un bloqueo; tras el segundo, el motor queda parado hasta `unblock` | 6 |

## Sesión de Chrome

- **En una ejecución:** un Chrome, una ventana y una pestaña. Todas las búsquedas navegan en ella, con las mismas cookies: Google ve una sesión continua.
- **Entre ejecuciones:** el perfil persiste (`var/paa/chrome-profile`), con las cookies de Google y el consentimiento rechazado. Cada ejecución arranca Chrome y lo cierra al terminar. Si ya hay uno vivo en el puerto 9224, lo reutiliza.
- **Al empezar, cierra cualquier otra pestaña de su Chrome.** Una ejecución cortada deja la suya, y una pestaña colgada comparte el proceso de la página nueva del mismo sitio (2026-10-26).

## Una búsqueda

1. Antes de la primera, abre la portada, como haría una persona, y rechaza el consentimiento («Rechazar todo»).
2. Abre `/search?q=…&hl=es&gl=es` y espera a que aparezca la caja (o un desafío). Si vuelve a salir el consentimiento, lo rechaza y recarga.
3. Lee las preguntas (`data-q`) sin el eco de la búsqueda. Después hace clic, con el ratón, en la primera que no ha abierto; espera a que la caja crezca, no un tiempo fijo, y anota las nuevas con la pregunta que las desplegó.
4. **No carga las respuestas de IA.** Al abrir una pregunta, Google hace dos tipos de llamada `async/callback`: una trae las preguntas nuevas (`data-q`, ~5 KB) y otras traen la respuesta (~40–50 KB, sin preguntas). El motor aprende en cada ejecución qué llamadas son respuestas y las bloquea (`Network.setBlockedURLs`) desde ese momento:
   - **Cuándo es una respuesta:** al menos dos respuestas sin preguntas y ninguna con ellas.
   - **Qué no se bloquea nunca:** una llamada que alguna vez trajo preguntas.

   El 2026-10-27 aprendió `6761` tras el primer clic y respetó `10041`, la de las preguntas. Los identificadores son de Google y pueden cambiar; quedan en `blocked_callbacks` del registro.
5. Guarda el registro, con el tiempo de cada paso (`timings`), y el DOM final.

Una página que deja de responder (una evaluación sin respuesta en 30 s) es **`failed`, no un bloqueo**. La ejecución se para y la semilla queda pendiente.

## Ficheros

Lo que produce el motor es desechable, en `demand-engine/var/paa/sets/<conjunto>/`:

| Ruta | Contenido |
|---|---|
| `state.json` | Estado de cada semilla (`pending`, `captured`, `blocked`, `failed`). |
| `searches/<semilla>/<fecha>/record.json` | URL pedida y final, estado HTTP, acciones (consentimiento, clics, bloqueos de respuestas aprendidos), preguntas con `position` y `via`, búsquedas relacionadas, si hay caja y vista de IA, llamadas bloqueadas (`blocked_callbacks`), tiempo de cada paso y navegador. |
| `searches/<semilla>/<fecha>/dom.html.gz` | El DOM tras la última apertura (solo si se capturó). |
| `questions.json` · `related.json` | Cada pregunta o búsqueda relacionada una vez, con todas las búsquedas que la mostraron. |
| `log.jsonl` | Una línea por búsqueda, consentimiento, bloqueo y pestañas cerradas al empezar. |
| `classify/` | Clasificación: entrada del agente (`input.md`, `input.json`), su salida (`output.json`) y su consumo (`usage.json`). |
| `classified.json` · `report.md` | Resultado de la clasificación (ver [Clasificación de las preguntas](#clasificación-de-las-preguntas)). |

Y, para todo el motor, `demand-engine/var/paa/engine.json`: los bloqueos (fecha, conjunto, evidencia) y hasta cuándo dura el último.

## Incidencia del 2026-10-26/27: la página dejaba de responder

**Qué pasaba:**
- Cada pregunta abierta hacía la búsqueda más lenta (2–4 minutos con 6–8 clics).
- Desde el segundo o tercer clic, el hilo principal de la página estaba al 100 %, hasta que dejaba de responder.
- No había `/sorry/`, ni CAPTCHA, ni errores HTTP, y la búsqueda manual desde la misma conexión iba bien.

**Descartado, una cosa cada vez:** el bloqueo de Google, el estado del perfil (con un perfil vacío pasaba igual), cerrar las respuestas, los eventos de red de CDP, la preferencia «reducir movimiento», una ventana más pequeña y la vista móvil.

**Causa:** una traza mostró un bucle de `requestAnimationFrame` (60 fotogramas por segundo) de los scripts de las respuestas de IA, que crecía con cada respuesta. Sin GPU, Chrome pinta cada fotograma por software.

**Solución:** no cargar las respuestas (paso 4 de [Una búsqueda](#una-búsqueda)). Con 8 clics, ~2,4 s por clic, CPU de la página por debajo del 10 % y 27 preguntas.

Que Chrome sobreviviera a ejecuciones cortadas, con su pestaña colgada dentro, confundió el diagnóstico: de ahí la limpieza de pestañas al empezar.

## Clasificación de las preguntas

Un agente de Claude Code clasifica todas las preguntas de un conjunto con el reglamento [`classifier/paa.md`](../../../classifier/paa.md) (T-040). Lo lanza la skill **`/paa-classify CONJUNTO`**. Es uno solo para que nombre cada criterio de elección una vez y lo aplique igual a todas las preguntas.

Para cada pregunta, el agente decide:

- **perímetro:** dentro o fuera de la clase;
- **objeto:** clase, marca, tienda o valorativa;
- **requisitos del catálogo** que la responden sin derivar, con lo que confirma requisitos y cuestiones inferidas;
- **criterio de elección**, si es valorativa.

Antes de aplicar C2 a una pregunta de clase, la relee sobre la oferta (D-100). A cada criterio le aplica la regla C1–C4 (D-091). Los criterios intermedios («material», «calidad») quedan cubiertos y se descomponen en prestaciones (D-104). De los criterios que cumplen C1–C4, y de las preguntas de clase que ningún requisito responde (D-099), saca **requisitos candidatos** de origen «paa» (D-097). Basta una pregunta (D-102). Cada candidato lleva su descripción, sus bloques (repetido en las hermanas si no vale para todas las hijas de la madre: D-107), su rasgo, su voto y su información resolutiva.

Propone además **revisiones** de requisitos existentes (separación por dimensión en los atributos de lista, D-103; partir por tema, reformular, mover aportaciones), **aportaciones** de precisión y de sustento (D-101) y, como propuesta, la **pertinencia de los criterios de aceptación** que muestran las preguntas (OQ-59).

El resto es determinista y se ejecuta en el host (`bin/paa classify …` no usa el contenedor):

```bash
demand-engine/bin/paa classify prepare sabanas    # classify/input.md: preguntas, catálogo de la clase (del modelo del conjunto) y rasgos
demand-engine/bin/paa classify check sabanas      # lo que falla en classify/output.json, hasta «correcto»
demand-engine/bin/paa classify usage sabanas TRANSCRIPCIÓN   # tokens del agente
demand-engine/bin/paa classify report sabanas --compare var/paa/probe-20261026T204606/classified.json \
    --previous var/paa/sets/sabanas/classify/v1/classified.json   # contra la sonda manual y contra la ejecución anterior
```

`report` escribe en la carpeta del conjunto:

- `classified.json`: cada pregunta con su clasificación y su procedencia, y los criterios y candidatos, con las preguntas como fuentes (`paa-q:<conjunto>:<pregunta>`);
- `report.md`: reparto, criterios con C1–C4, candidatos, revisiones, aportaciones, pertinencia de AC, requisitos confirmados, preguntas que no generan, contraste con la ejecución anterior y con una clasificación manual, y consumo.

Para comparar dos reglamentos, guarda antes la ejecución anterior (`classify/v1/`, por ejemplo) y pásala con `--previous`.

Los candidatos **no entran solos en el catálogo**: se deciden en el entrenamiento.

## Pruebas

`tests/paa/`: semillas, estado, bloqueos, consolidación y clasificación (entrada, comprobación, resultado y contraste). Con Chrome (`test_e2e.py`), una imitación local de la página de resultados que hace, como Google, una llamada con las preguntas y otras con la respuesta. Cubre consentimiento, eco de la búsqueda, despliegue por clics, aprendizaje y bloqueo de las respuestas, parada temprana, pestaña sobrante, bloqueo y página que deja de responder.
