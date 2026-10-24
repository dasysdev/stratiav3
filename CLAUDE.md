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
2. **Web y Web Schema.org no se agregan:** sus resultados se interpretan por separado.
3. **Disponibilidad efectiva binaria (0/1)** y previa a todo lo demás. **0 → IR = 0** y no se valoran los AC. Una comprobación inconclusa queda **fuera** de la escala: no existe un tercer valor.
4. **Seis criterios de aceptación:** Concreción, Precisión, Aplicabilidad, Comparabilidad, Fiabilidad y Justificación.
   - Se valoran con un **GSC ordinal 0/1/2**, o con **NA**/**NE**, que no son puntuaciones.
   - NE ≠ 0.
   - No hay GSC global ni media de los seis AC.
5. **Propiedades P06–P18:** solo fundamentan juicios.
   - **Nunca** reciben puntuación, pesos ni sumas.
   - Pertenecen al modelo informativo, no al técnico.
6. **Importancia relativa** (Crítico / Principal / Complementario): cualitativa y ordinal, **sin pesos numéricos**. Pertenece al modelo de demanda, no al resultado observado.
7. **El IR se expresa en escala 0–10** ([D-017](docs/30-governance/decisions.md#d-017)), pero **IR, ICI y TRI no tienen fórmula de agregación aprobada**.
   - **En propuesta:** el estado binario de resolución (0/1, sin regla definida), el **IP** (fórmula `100 × C/N`) y la **calidad ajustada** (sin fórmula ni peso). Ver [informative-prominence](docs/10-model/informative-prominence.md).
   - No se inventan fórmulas, pesos, umbrales ni topes.
8. **La evaluación técnica es independiente** y tiene su propio sistema cuantitativo. Un incumplimiento técnico no descuenta el GSC: solo cuenta su efecto sobre la disponibilidad del RI.
9. **Derivaciones justificadas, admitidas.** No se penaliza el número de pasos. **Nunca** se completan hechos comerciales ausentes con conjeturas o conocimiento externo.
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
| `bin/pm` · `work/` | Gestión del trabajo del entorno y del código: una tarea por fichero. |

## Reglas de trabajo

- **Idioma:** contenido y conversación en español. Nombres de fichero, `id` y código en inglés.
- **Precedencia:** `00-context` y `10-model` prevalecen sobre `20-methods`. Un método no crea conceptos, escalas ni indicadores.
- **El intake prevalece.** Lo que se deposita en `docs/intake/` sobrescribe el canon, incluidas estas invariantes; se aplica sin pedir aprobación y se informa después ([D-016](docs/30-governance/decisions.md#d-016)).
- **Fuera del intake, no resuelvas incoherencias en silencio.** Regístralas en `issues.md` con una propuesta.
- **Para modificar documentación,** usa la skill **`/docs-update`**. Los updates se depositan en [docs/intake/](docs/intake/README.md). La skill sigue el flujo de [docs/CLAUDE.md](docs/CLAUDE.md#flujo-de-cambio) y termina ejecutando `python3 tools/check_docs.py`.
- `docs/archive/` es de solo lectura: contiene la línea base v0 y los artefactos de intake procesados. Los originales de `tmp/docs/` se eliminaron; su única copia es `docs/archive/v0-2026-10-24/`.
- El proyecto **no usa git** por ahora: la trazabilidad depende de `changelog.md` y del archivo v0.

## Gestión del trabajo

El trabajo del entorno y del código se gestiona con `bin/pm`: una tarea es un fichero en `work/`. Al arrancar cada sesión, un hook inyecta `bin/pm ready`. No leas `work/` entero ni `work/log.md`: consulta con `bin/pm show ID`.

- **Una tarea = una sesión.** Al terminar, `bin/pm check ID N…` y `bin/pm close ID "resumen de una línea"`; después, `/clear`.
- **Si la sesión acaba a medias,** deja el relevo con `bin/pm next ID "…"`: es lo único que necesita la siguiente.
- **Abre tareas completas en una sola llamada:** `bin/pm new "título" --goal "…" --ac "…" --ac "…"`. Los criterios han de ser observables; sin ellos la tarea no se puede cerrar.
- **Cada hecho, una sola vez.** El detalle vive en la tarea (los hallazgos, con `bin/pm note ID "…"`) y el registro guarda una línea por tarea cerrada. No hay sprints ni ficheros de estado.
- Las cuestiones metodológicas siguen en [open-questions](docs/30-governance/open-questions.md) e [issues](docs/30-governance/issues.md), no en `work/`.
- `bin/pm --help` lista el resto de comandos.
