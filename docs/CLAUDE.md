# Reglas de mantenimiento de la documentación

Este fichero se carga al trabajar en `docs/`. Define cómo se escribe, se modifica y se valida la base conceptual.

## Capas y precedencia

| Capa | Carpeta | Contenido | Estado típico |
|---|---|---|---|
| Contexto | `00-context/` | Problema, objeto, alcance, encaje de negocio. | `vigente` |
| Modelo | `10-model/` | **Canon conceptual**: definiciones, reglas, escalas e indicadores. | `vigente` |
| Métodos | `20-methods/` | Procedimientos operativos (taxonomía, MPIR, auditoría GSC). | `propuesta` |
| Gobernanza | `30-governance/` | Decisiones, cuestiones abiertas, incidencias, changelog. | — |
| Archivo | `archive/` | Originales v0 y artefactos de intake procesados (`archive/intake/`), **inmutables**. | `historico` |
| Intake | `intake/` | Artefactos de update **pendientes de procesar**. No es canon; el validador no la revisa. | — |

**Precedencia:** un artefacto de `intake/` procesado prevalece sobre todo lo existente ([D-016](30-governance/decisions.md#d-016)). Entre capas, `00-context` y `10-model` prevalecen sobre `20-methods`. Un método **no puede** introducir conceptos, criterios, propiedades, escalas, pesos ni indicadores nuevos; si lo necesita, se registra como decisión pendiente en `30-governance/decisions.md`.

## Frontmatter obligatorio (todo `.md` salvo `archive/` y este fichero)

```yaml
---
id: acceptance-criteria        # único en docs/; por defecto el nombre del fichero (README → nombre de carpeta)
title: Criterios de aceptación
layer: model                   # context | model | method | governance | meta
status: vigente                # vigente | propuesta | pendiente | historico
version: 1.0
updated: 2026-10-24
sources: [BASE §5.2, FUND §6]  # trazabilidad al archivo v0 (claves abajo); [] si es contenido nuevo
---
```

**Claves de fuentes v0** (`archive/v0-2026-10-24/`):

| Clave | Fichero v0 | Ref. interna original |
|---|---|---|
| `CTX` | `core/project-context.md` — Contexto y marco del estudio | M1 (rector) |
| `BASE` | `core/base-concepts.md` — Conceptos base del sistema de estudio | M2 (rector) |
| `FUND` | `core/fundamentals.md` — Fundamentos consolidados | M3 |
| `TAX` | `demand-model/Marco_metodologico_taxonomia_modelos_demanda.md` | M4 |
| `MPIR` | `demand-model/Marco_metodologico_MPIR.md` | — |
| `GSC0` | `evaluation-systems/draft_0-0-0.md` — Marco operativo GSC v0.1 | — |
| `INTAKE <stem>` | `archive/intake/<stem>.<ext>` — artefacto de update procesado (p. ej. `INTAKE 2026-10-24-prominencia-informativa`) | — |

## Estados

- `vigente` — definido en los documentos rectores (CTX, BASE), en FUND o en un intake procesado que lo formule como vigente ([D-016](30-governance/decisions.md#d-016), [D-070](30-governance/decisions.md#d-070)); forma parte del canon.
- `propuesta` — propuesta operativa V1 o diseño metodológico pendiente de calibración (GSC0, MPIR, TAX).
- `pendiente` — identificado pero sin especificar.
- `historico` — superado; solo consulta.

Si un módulo mezcla estados, el frontmatter indica el predominante y cada bloque distinto se marca al inicio con
`> **Estado: propuesta V1**` (o `pendiente`).

## Plantilla de módulo del modelo (`10-model/`)

Secciones, en este orden, omitiendo las que no apliquen:

1. **Definición** — texto normativo **literal** de la fuente rectora.
2. **Reglas e invariantes** — lo que siempre se cumple.
3. **Distinciones** — «X frente a Y».
4. **Interpretación** — desarrollo de FUND, condensado sin alterar el significado.
5. **Ejemplo mínimo**.
6. **Pendiente** — con enlace a `30-governance/open-questions.md`.
7. **Relacionado** — enlaces a otros módulos.

Los métodos (`20-methods/`) conservan los identificadores de reglas originales (`M01`, `RI-01`, `L-01`, `PF-01`, `CT-01`, `CO-01`, `EV-01`, `PR-01`, `GSC-01`, `OP-01`, `QA-01`, `SI-01`…).

## Reglas de redacción

- Contenido en **español**; nombres de fichero e `id` en inglés, en kebab-case.
- Módulos de **80–250 líneas**. Si se supera, dividir por subtema.
- **Una sola fuente de verdad por concepto.** Fuera de su módulo canónico, un concepto se enlaza; no se redefine. Se admite una frase de contexto.
- Definiciones normativas: literales. Interpretaciones: pueden condensarse, **nunca** añadir conceptos, escalas, pesos ni cambiar el sentido.
- Divergencias entre fuentes: **no resolverlas en silencio**. Registrar en `30-governance/issues.md` y marcar en el texto `⚠ Ver [I-NN](../30-governance/issues.md#i-nn)`.
- Enlaces relativos markdown. Anclas con slug estilo GitHub (minúsculas, sin puntuación, espacios → `-`).
- Ejemplos hipotéticos: indicarlo expresamente.

## Flujo de cambio

Los updates se procesan con la skill **`/docs-update`** (`.claude/skills/docs-update/`). Los artefactos se depositan en `intake/`; la skill analiza el impacto, decide y aplica sin aprobación previa los pasos siguientes, archiva el artefacto en `archive/intake/` e informa al terminar. **El intake prevalece sobre el contenido existente y lo sobrescribe**, incluidas las invariantes y las decisiones aceptadas; cada sobrescritura queda registrada como decisión ([D-016](30-governance/decisions.md#d-016)). Todo artefacto procesado se archiva; `intake/` solo contiene lo pendiente o lo aplazado. Pasos que aplica:

1. Registrar la decisión en `30-governance/decisions.md` (contexto, decisión, consecuencias, estado).
2. Editar el módulo canónico y subir `version` + `updated`.
3. Actualizar `glossary.md` si cambia un término, su definición breve o su ubicación.
4. Añadir entrada en `30-governance/changelog.md`.
5. Ejecutar `python3 tools/check_docs.py` y corregir errores.

**Versionado de módulos:** +0.1 por cada cambio; +1.0 solo si se reestructura o redefine el módulo.

El archivo `archive/` **no se edita nunca**; solo se le añaden artefactos de intake procesados. Una nueva línea base se archiva como carpeta nueva (`archive/vN-AAAA-MM-DD/`).
