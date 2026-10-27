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
   - **Fiabilidad** se lee de forma refutadora: 2 = sin defectos detectados en las comprobaciones, nunca «exacto» ([D-121](docs/30-governance/decisions.md#d-121)).
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
| [demand-engine/](demand-engine/README.md) | Sistema de construcción del modelo de demanda: referencias, taxo, catálogo de bloques, clasificador y motor de captura compartido. **Cada sistema del proyecto es un directorio de primer nivel** y un miembro del workspace de uv. |
| `demand-engine/bin/refs` · `demand-engine/var/refs/` | Material de referencia externo de la taxonomía (Shopify, su mapeo oficial a Google, Google y Amazon.es), congelado por versión y fuera de git; las versiones usadas quedan en las reglas del entrenamiento y en cada modelo. `demand-engine/bin/refs --help`. Ficheros grandes: consúltalos con `zcat`/`grep`, no los leas enteros. |
| `demand-engine/classifier/` · `cases/` · `var/runs/` · `training/reports/` · `bin/taxo` · `bin/compare` | Clasificador de la clase de estudio: reglamento operativo (versión en su cabecera; cada regla cita su decisión; el canon prevalece), conjunto de control (14 casos con lo esperado), ejecuciones (desechables) y el informe de cada ciclo, consulta de referencias y páginas congeladas (`var/pages/`). |
| `demand-engine/bin/model` · `bin/train` · `catalog/` · `training/selection/` | Motor de demanda, primera versión ([D-045](docs/30-governance/decisions.md#d-045)): ensamblado del modelo desde el catálogo compilado y las reglas de importancia; entrenamiento (selección del catálogo de entrenamiento en tiendas reales, [D-053](docs/30-governance/decisions.md#d-053); rasgos, reglas por el árbol de Shopify, compilación, informe). Producto real: `/demand-model URL`; catálogo de entrenamiento, por lotes con agentes: `/classify-batch` ([D-054](docs/30-governance/decisions.md#d-054)). |
| `demand-engine/src/demand_engine/capture/` | Motor de captura compartido ([D-046](docs/30-governance/decisions.md#d-046)): Chrome real por CDP, legitimidad (robots.txt, reservas TDM), parada ante desafíos; por lotes a ritmo de lector (MPIR, entrenamiento) o una página suelta (`bin/taxo page fetch`, que desde el host delega en el contenedor). Ver [su README](demand-engine/src/demand_engine/capture/README.md). |
| `demand-engine/src/demand_engine/mpir/` · `bin/mpir` | MPIR, capa A (aparcado, [D-095](docs/30-governance/decisions.md#d-095)): plan de observación, fichas de referente, inventario e ingesta manual sobre el motor de captura. Lo que se define, en `demand-engine/studies/`; corpus y estado, en `demand-engine/var/mpir/`, fuera de git. Ver [su README](demand-engine/src/demand_engine/mpir/README.md). |
| `demand-engine/src/demand_engine/paa/` · `bin/paa` · `demand-engine/paa/` | Motor PAA: preguntas de «Más preguntas» de google.es para un conjunto de semillas de una clase (estrategia optimizada: núcleo + valores del material, 8 clics). Vía de construcción del modelo de demanda ([D-094](docs/30-governance/decisions.md#d-094)), con excepción al robots.txt de Google para investigación y uso interno ([D-096](docs/30-governance/decisions.md#d-096)). Clasificación de sus preguntas con un agente: `/paa-classify CONJUNTO` (reglamento `demand-engine/classifier/paa.md`; criterios de elección, C1–C4 y requisitos candidatos «paa»). Ver [su README](demand-engine/src/demand_engine/paa/README.md). |
| `bin/run` · `docker-compose.yml` · `env/docker/` · `pyproject.toml` | Entorno dockerizado del código (Python 3.13, uv, Chrome sobre Xvfb): `bin/run dev up\|test\|shell\|lock\|exec`. Workspace de uv con un miembro por sistema y un solo `uv.lock`. |
| `bin/pm` · `work/` | Gestión del trabajo del entorno y del código: una tarea por fichero. |

## Reglas de trabajo

- **Idioma:** contenido y conversación en español. Nombres de fichero, `id` y código en inglés.
- **Precedencia:** `00-context` y `10-model` prevalecen sobre `20-methods`. Un método no crea conceptos, escalas ni indicadores.
- **El intake prevalece.** Lo que se deposita en `docs/intake/` sobrescribe el canon, incluidas estas invariantes; se aplica sin pedir aprobación y se informa después ([D-016](docs/30-governance/decisions.md#d-016)).
- **Fuera del intake, no resuelvas incoherencias en silencio.** Regístralas en `issues.md` con una propuesta.
- **Para modificar documentación,** usa la skill **`/docs-update`**. Los updates se depositan en [docs/intake/](docs/intake/README.md). La skill sigue el flujo de [docs/CLAUDE.md](docs/CLAUDE.md#flujo-de-cambio) y termina ejecutando `python3 tools/check_docs.py`.
- `docs/archive/` es de solo lectura: contiene la línea base v0 y los artefactos de intake procesados. Los originales de `tmp/docs/` se eliminaron; su única copia es `docs/archive/v0-2026-10-24/`.
- El proyecto **no usa git** por ahora: la trazabilidad depende de `changelog.md` y del archivo v0.
- **Qué entra en git** (cuando se adopte, T-003): lo que gobierna el sistema y los resultados del entrenamiento. `demand-engine/var/` es desechable y no tiene copia; git no es una copia de seguridad. Detalle en [demand-engine/README.md](demand-engine/README.md#qué-entra-en-git).

## Gestión del trabajo

El trabajo del entorno y del código se gestiona con `bin/pm`: una tarea es un fichero en `work/`. Al arrancar cada sesión, un hook inyecta `bin/pm ready`. No leas `work/` entero ni `work/log.md`: consulta con `bin/pm show ID`.

- **Una tarea = una sesión.** Al terminar, `bin/pm check ID N…` y `bin/pm close ID "resumen de una línea"`; después, `/clear`.
- **Si la sesión acaba a medias,** deja el relevo con `bin/pm next ID "…"`: es lo único que necesita la siguiente.
- **Abre tareas completas en una sola llamada:** `bin/pm new "título" --goal "…" --ac "…" --ac "…"`. Los criterios han de ser observables; sin ellos la tarea no se puede cerrar.
- **Cada hecho, una sola vez.** El detalle vive en la tarea (los hallazgos, con `bin/pm note ID "…"`) y el registro guarda una línea por tarea cerrada. No hay sprints ni ficheros de estado.
- Las cuestiones metodológicas siguen en [open-questions](docs/30-governance/open-questions.md) e [issues](docs/30-governance/issues.md), no en `work/`.
- `bin/pm --help` lista el resto de comandos.
