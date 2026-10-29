# stratia.cic — Calidad de información comercial

**stratia.cic** (stratia, calidad de información comercial) es el nombre del proyecto y del sistema; el directorio se llama `stratiav3` ([D-011](docs/30-governance/decisions.md#d-011)).

Sistema de auditoría que evalúa si la información comercial que publica un ecommerce permite a los sistemas de IA **descubrir, comprender, comparar, evaluar y justificar** sus ofertas durante el **descubrimiento y la decisión de compra** (Agentic Commerce).

- **Perímetro:** España, desde octubre de 2026 hasta al menos el primer trimestre de 2027.
- **Consumo:** sin navegación interactiva.
- **Fase actual:** diseño metodológico. Todavía no hay código de producto; la base es la documentación de [docs/](docs/README.md).

## Cómo orientarte

1. **Primero [docs/glossary.md](docs/glossary.md):** cada término con su definición breve, su módulo canónico y su estado.
2. Después, **solo el módulo canónico** que necesites. Los módulos tienen 80–250 líneas: no leas más de lo necesario.
3. Para operar una auditoría, ve a [docs/20-methods/audit-gsc/](docs/20-methods/audit-gsc/README.md).
4. **Archivo** (`docs/archive/`: v0 e intake procesado): solo para trazar el origen de un texto (claves `sources` del frontmatter). No es canon.
5. Antes de proponer algo, consulta los pendientes ([open-questions](docs/30-governance/open-questions.md)) y las incoherencias conocidas ([issues](docs/30-governance/issues.md)).

## Invariantes del modelo (no se violan nunca)

1. **Unidad informativa:** RI × ámbito. En este contexto «ámbito» e «interfaz» son sinónimos. Los ámbitos son **Catálogos distribuidos**, **Web** (HTML + Schema.org) y **Web Schema.org** (solo marcado).
2. **Web y Web Schema.org no se agregan:** sus resultados se interpretan por separado. La **consistencia transversal** (RI × par de ámbitos) es una dimensión de análisis aparte: hallazgos sin escala que no modifican el GSC de ningún ámbito ([D-124](docs/30-governance/decisions.md#d-124)).
3. **Disponibilidad efectiva binaria (0/1)** y previa a todo lo demás. **0 → IR = 0** y no se valoran los AC. Una comprobación inconclusa queda **fuera** de la escala: no existe un tercer valor.
4. **Seis criterios de aceptación:** Concreción, Precisión, Aplicabilidad, Comparabilidad, Fiabilidad y Justificación.
   - Se aplican siempre y se valoran con un **GSC ordinal 0/1/2**. No hay NA de criterio, salvo el de Comparabilidad en los requisitos marcados como no dimensión de comparación ([D-117](docs/30-governance/decisions.md#d-117), [D-126](docs/30-governance/decisions.md#d-126)). Qué mira cada AC en un requisito lo orientan sus [pistas de valoración](docs/10-model/assessment-hints.md): criterios breves, no listas.
   - **NE es una incidencia** de la auditoría (una comprobación que no se pudo hacer), no una puntuación. NE ≠ 0.
   - **Fiabilidad** se lee de forma refutadora: 2 = sin defectos detectados en las comprobaciones, nunca «exacto» ([D-121](docs/30-governance/decisions.md#d-121)). **Sin fuentes externas:** estructura del dato, conocimiento del dominio y consistencia dentro del ámbito; lo que el modelo auditor sepa de un producto concreto es una sospecha, que no gradúa ([D-154](docs/30-governance/decisions.md#d-154)).
   - No hay GSC global ni media de los seis AC.
5. **Propiedades P06–P18:** solo fundamentan juicios. P15 · Actualidad está retirada ([D-123](docs/30-governance/decisions.md#d-123)).
   - **Nunca** reciben puntuación, pesos ni sumas.
   - Pertenecen al modelo informativo, no al técnico.
6. **Importancia relativa** (Crítico / Principal / Complementario): cualitativa y ordinal, **sin pesos numéricos**. Pertenece al modelo de demanda, no al resultado observado.
7. **El IR se expresa en escala 0–10** ([D-017](docs/30-governance/decisions.md#d-017)), pero **IR, ICI y TRI no tienen fórmula de agregación aprobada**.
   - **En propuesta:** el estado binario de resolución (0/1, sin regla definida), el **IP** (fórmula `100 × C/N`) y la **calidad ajustada** (sin fórmula ni peso). Ver [informative-prominence](docs/10-model/informative-prominence.md).
   - No se inventan fórmulas, pesos, umbrales ni topes.
8. **La evaluación técnica es independiente** y tiene su propio sistema cuantitativo. Un incumplimiento técnico no descuenta el GSC: solo cuenta su efecto sobre la disponibilidad del RI.
9. **Derivaciones justificadas, admitidas.** No se penaliza el número de pasos. **Nunca** se completan hechos comerciales ausentes con conjeturas o conocimiento externo. Se admite la derivación cuya conclusión no puede ser falsa si lo publicado es verdad, con reglas generales, descriptivas y citadas ([prueba de derivación](docs/10-model/effective-availability.md#prueba-de-derivación), [D-120](docs/30-governance/decisions.md#d-120)); un atributo por sí solo no es pertinente para una prestación ([D-119](docs/30-governance/decisions.md#d-119)).
10. **Pertinencia ≠ proximidad temática.**
11. **Una ausencia exige prueba de cobertura.** Una búsqueda fallida no demuestra ausencia.
12. **Ausencia de corroboración ≠ falsedad.** Ausencia de contradicción ≠ exactitud.
13. **Neutralidad de respuesta:** un «no» fundamentado resuelve la cuestión. Se evalúa la información, no el producto ni su conveniencia para un comprador.
14. **No se mide** el comportamiento de una IA concreta, ni la visibilidad, ni la conversión.

Decisiones explícitamente no adoptadas: [D-006](docs/30-governance/decisions.md#d-006).

## Mapa de la documentación

| Ruta | Contenido |
|---|---|
| [docs/00-context/](docs/00-context/scope.md) | Problema, objeto, alcance, límites y encaje de negocio. |
| [docs/10-model/](docs/10-model/evaluation-architecture.md) | **Canon conceptual**: información comercial, funciones IA, ámbitos, modelo de demanda, disponibilidad, AC, propiedades y sistemas de valoración. |
| [docs/20-methods/](docs/README.md#20-methods--procedimientos-propuesta) | Procedimientos (propuesta V1): taxonomía de clases, MPIR y auditoría GSC. |
| [docs/30-governance/](docs/30-governance/decisions.md) | Decisiones, cuestiones abiertas, incidencias y changelog. |
| `tools/check_docs.py` | Validador de integridad de la documentación. |
| [demand-engine/](demand-engine/README.md) | Sistema de construcción del modelo de demanda: referencias, taxo, catálogo de bloques, clasificador, entrenamiento, MPIR y PAA; captura y lee las fichas con [capture/](capture/README.md). **Cada sistema del proyecto es un directorio de primer nivel** y un miembro del workspace de uv. |
| `demand-engine/classifier/` · `cases/` · `var/runs/` · `training/reports/` · `bin/taxo` · `bin/compare` | Clasificador de la clase de estudio: reglamento operativo (versión en su cabecera; cada regla cita su decisión; el canon prevalece), conjunto de control (14 casos con lo esperado), ejecuciones (desechables) y el informe de cada ciclo, consulta de referencias y páginas congeladas (`capture/var/pages/`). |
| `demand-engine/bin/model` · `bin/train` · `catalog/` · `training/selection/` | Motor de demanda, primera versión ([D-045](docs/30-governance/decisions.md#d-045)): ensamblado del modelo desde el catálogo compilado y las reglas de importancia; entrenamiento (selección del catálogo de entrenamiento en tiendas reales, [D-053](docs/30-governance/decisions.md#d-053); rasgos, reglas por el árbol de Shopify, compilación, informe). Producto real: `/demand-model URL`; catálogo de entrenamiento, por lotes con agentes: `/classify-batch` ([D-054](docs/30-governance/decisions.md#d-054)). Un modelo y una ficha por ámbito ([D-155](docs/30-governance/decisions.md#d-155)): `catalog/scopes/` (pertinencia por excepción y localización) y `bin/model scope MODEL.json`, que compone las unidades RI × ámbito; las propiedades recomendadas de Google Search son apoyo «referencias» sin ámbito (capa general y `catalog/google-search.json`). |
| `demand-engine/src/demand_engine/mpir/` · `bin/mpir` | MPIR, capa A (aparcado, [D-095](docs/30-governance/decisions.md#d-095)): plan de observación, fichas de referente, inventario e ingesta manual sobre el motor de captura. Lo que se define, en `demand-engine/studies/`; corpus y estado, en `demand-engine/var/mpir/`, fuera de git. Ver [su README](demand-engine/src/demand_engine/mpir/README.md). |
| `demand-engine/src/demand_engine/paa/` · `bin/paa` · `demand-engine/paa/` | Motor PAA: preguntas de «Más preguntas» de google.es para un conjunto de semillas de una clase (estrategia optimizada: núcleo + valores del material, 8 clics). Vía de construcción del modelo de demanda ([D-094](docs/30-governance/decisions.md#d-094)), con excepción al robots.txt de Google para investigación y uso interno ([D-096](docs/30-governance/decisions.md#d-096)). Clasificación de sus preguntas con un agente: `/paa-classify CONJUNTO` (reglamento `demand-engine/classifier/paa.md`; criterios de elección, C1–C4 y requisitos candidatos «paa»). Ver [su README](demand-engine/src/demand_engine/paa/README.md). |
| [capture/](capture/README.md) · `capture/bin/pages` | Motor de captura y almacén común de fichas congeladas ([D-150](docs/30-governance/decisions.md#d-150), que enmienda [D-046](docs/30-governance/decisions.md#d-046)): Chrome real por CDP, legitimidad (robots.txt, reservas TDM), parada ante desafíos; por lotes a ritmo de lector o una ficha suelta (`capture/bin/pages fetch ID URL`, que desde el host delega en el contenedor); las páginas de una auditoría (D-167: fichas del encargo, portada, políticas, categoría inmediata, robots.txt y sitemaps), con `audit-es`, en `capture/var/audits/AUDIT/` (`capture/bin/pages audit AUDIT URL…`); una reserva TDM (`tdmrep.json`, o la cabecera o la meta de la portada o de una página) para la auditoría, que lo registra en el manifiesto y termina con error (D-171). **Perfiles de captura** con nombre, que elige quien captura: `reader` (por defecto: Chrome persistente con JavaScript; PAA, el entrenamiento y el MPIR) y `audit-es` (D-157: contexto desechable por ficha, sin JavaScript, la respuesta HTTP con sus bytes originales, contexto de la petición y robots.txt por bot; `--profile audit-es`). Las fichas, en `capture/var/pages/` (fuera de git), y el perfil de Chrome, en `capture/var/chrome-profile/`; un ID existente se rechaza y nunca se sustituye una ficha. Lo usan, en demand-engine, `bin/taxo page fetch` (misma regla) y la lectura de fichas, la captura del entrenamiento, el MPIR y PAA (su navegador). La interpretación de cada ficha queda en cada sistema. Miembro del workspace de uv. |
| [references/](references/README.md) · `references/bin/refs` | Custodia común de las fuentes externas de todos los sistemas ([D-149](docs/30-governance/decisions.md#d-149)): registro `references/sources.json` (con `uses`: los sistemas que usan cada fuente), versiones congeladas en `references/var/` (fuera de git), una versión fijada por fuente para todos, diff y lectores por formato (`references.read`). Hoy: la taxonomía de Shopify, su mapeo oficial a Google, Google, Amazon.es y las normas que cita el catálogo (BOE y EUR-Lex por Cellar; `refs law`) (demand-engine); el vocabulario Schema.org, los documentos de las especificaciones (también las del perfil de Web: HTTP, robots.txt, HTML, Encoding, Google Search y los bots de OpenAI, Anthropic y Perplexity) y los códigos ISO 4217 e ISO 3166-1 (web-audit); los documentos de Google Search con tablas de propiedades, los dos (`refs props`). demand-engine comprueba sus citas con `bin/model refs`. La interpretación de cada fuente queda en su sistema; las versiones que usó un resultado quedan en él (reglas del entrenamiento, cada modelo). Credenciales de SP-API en `references/.env`. `references/bin/refs --help`. Ficheros grandes: consúltalos con `zcat`/`grep`, no los leas enteros. Miembro del workspace de uv. |
| [web-audit/](web-audit/README.md) | Sistema de la evaluación técnica de Web y Web Schema.org, solo técnico ([D-129](docs/30-governance/decisions.md#d-129)): referencia técnica en `web-audit/reference/` ([D-133](docs/30-governance/decisions.md#d-133)), sobre las fuentes de references/, y el auditado (T-049): `web-audit/bin/audit` aplica los requisitos técnicos a las páginas de una auditoría de capture y escribe el expediente técnico con la tasa de cumplimiento técnico (D-166) en `web-audit/var/audits/AUDIT/`; lo que pide juicio lo decide un agente con **`/web-audit`**. Miembro del workspace de uv. |
| `web-audit/bin/reqs` · `web-audit/reference/cards/` · `web-audit/reference/requirements/` | Referencia técnica: una ficha por fuente (clase y nivel en el canon, versión fijada, citas literales por sección) y los requisitos técnicos de Web Schema.org y de Web ([D-159](docs/30-governance/decisions.md#d-159)), un fichero por nivel del perfil de cada ámbito, con los campos del canon y sus citas ([formato](web-audit/reference/README.md)). Se crea y se mantiene con **`/web-reference`** (añadir una fuente, actualizar ante una versión nueva, validar); `reqs check` valida y `reqs section` muestra el texto citable. |
| `bin/run` · `docker-compose.yml` · `env/docker/` · `pyproject.toml` | Entorno dockerizado del código (Python 3.13, uv, Chrome sobre Xvfb): `bin/run dev up\|test\|shell\|lock\|exec`. Workspace de uv con un miembro por sistema y un solo `uv.lock`. |
| `bin/pm` · `work/` | Gestión del trabajo del entorno y del código: una tarea por fichero. |

## Reglas de trabajo

- **Idioma:** contenido y conversación en español. Nombres de fichero, `id` y código en inglés.
- **Precedencia:** `00-context` y `10-model` prevalecen sobre `20-methods`. Un método no crea conceptos, escalas ni indicadores.
- **El intake prevalece.** Lo que se deposita en `docs/intake/` sobrescribe el canon, incluidas estas invariantes; se aplica sin pedir aprobación y se informa después ([D-016](docs/30-governance/decisions.md#d-016)).
- **Fuera del intake, no resuelvas incoherencias en silencio.** Regístralas en `issues.md` con una propuesta.
- **Para modificar documentación,** usa la skill **`/docs-update`**. Los updates se depositan en [docs/intake/](docs/intake/README.md). La skill sigue el flujo de [docs/CLAUDE.md](docs/CLAUDE.md#flujo-de-cambio) y termina ejecutando `python3 tools/check_docs.py`.
- `docs/archive/` es de solo lectura: contiene la línea base v0 y los artefactos de intake procesados. Los originales de `tmp/docs/` se eliminaron; su única copia es `docs/archive/v0-2026-10-24/`.
- El proyecto **usa git** (rama `main`; T-003): diffs y marcha atrás del código y de la documentación. La trazabilidad del canon sigue en `changelog.md` y en el archivo v0.
- **Qué entra en git:** lo que gobierna el sistema y los resultados del entrenamiento. `demand-engine/var/`, `capture/var/` y `references/var/` son desechables y no tienen copia; git no es una copia de seguridad. Detalle en [demand-engine/README.md](demand-engine/README.md#qué-entra-en-git), [capture/README.md](capture/README.md#qué-entra-en-git), [references/README.md](references/README.md#qué-entra-en-git) y [web-audit/README.md](web-audit/README.md#qué-entra-en-git).

## Estilo de redacción

Para el texto que dice **qué hacer** o **cómo es algo**, se siguen las reglas de redacción de ASD-STE100 (Issue 9) adaptadas al español, sin su diccionario, y UNE-ISO 24495-1:2024.

- **Se aplica a:** las respuestas en la conversación (resultados, pasos, lo pendiente), los procedimientos y los README operativos, los reglamentos y los prompts de agentes, los criterios y las notas de `bin/pm`, los mensajes de commit, los mensajes y las ayudas de la CLI, y los enunciados normativos nuevos del canon.
- **No se aplica a:** la comparación de alternativas, el debate metodológico, la justificación de una decisión, las citas literales y el código. Las definiciones normativas en vigor son literales ([docs/CLAUDE.md](docs/CLAUDE.md#reglas-de-redacción)): no se reescriben por estilo.

Reglas:

1. **Frases cortas:** 20 palabras como máximo en una instrucción y 25 en una descripción. Un párrafo trata un tema y tiene 6 frases como máximo.
2. **Una instrucción por frase,** en imperativo. La condición va antes de la acción: «Si la ficha ya existe, usa otro ID.»
3. **Voz activa y sujeto explícito** cuando hay más de un agente (tú, yo, el agente, el motor). La pasiva con «se», solo si el agente no importa.
4. **Verbos, no sustantivos derivados:** «comprobar», no «realizar la comprobación de». Sin cadenas de «de».
5. **Un término, un significado:** el del [glosario](docs/glossary.md), siempre el mismo. Sin sinónimos por estilo.
6. **Tiempos simples.** Sin gerundios encadenados ni condicionales apilados.
7. **La incertidumbre, con una palabra y una vez:** «Causa probable: …».
8. **Listas** para los pasos y las alternativas.

### Commits

- **Una sola línea:** `ruta: intención`. La intención del commit, no la lista de lo que cambia. Sin cuerpo.
- **Intención:** en presente («añade», «corrige», «retira»), con 72 caracteres como máximo y sin punto final.
- **Ruta:** el módulo afectado, con la precisión que haga falta, como migas de pan desde el sistema: `demand-engine/paa/classify`, `web-audit/reference/cards`, `docs/10-model/scoring-systems`. Si no hay un módulo más preciso, solo el sistema (`capture`, `references`, `docs`). Un sistema es un directorio de primer nivel.
- **Varios sistemas:** un commit por sistema. Si un cambio no se puede partir, nombra los sistemas separados por coma: `docs, web-audit: …`.
- **Sin coautoría:** sin líneas `Co-Authored-By` ni de atribución.

## Gestión del trabajo

El trabajo del entorno y del código se gestiona con `bin/pm`: una tarea es un fichero en `work/`. Al arrancar cada sesión, un hook inyecta `bin/pm ready`. No leas `work/` entero ni `work/log.md`: consulta con `bin/pm show ID`.

- **Una tarea = una sesión.** Al terminar, `bin/pm check ID N…` y `bin/pm close ID "resumen de una línea"`; después, `/clear`.
- **Si la sesión acaba a medias,** deja el relevo con `bin/pm next ID "…"`: es lo único que necesita la siguiente.
- **Abre tareas completas en una sola llamada:** `bin/pm new "título" --goal "…" --ac "…" --ac "…"`. Los criterios han de ser observables; sin ellos la tarea no se puede cerrar.
- **Cada hecho, una sola vez.** El detalle vive en la tarea (los hallazgos, con `bin/pm note ID "…"`) y el registro guarda una línea por tarea cerrada. No hay sprints ni ficheros de estado.
- Las cuestiones metodológicas siguen en [open-questions](docs/30-governance/open-questions.md) e [issues](docs/30-governance/issues.md), no en `work/`.
- `bin/pm --help` lista el resto de comandos.
