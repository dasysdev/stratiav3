---
id: changelog
title: Registro de cambios de la documentación
layer: governance
status: vigente
version: 1.0
updated: 2026-10-24
sources: []
---

# Registro de cambios

Entradas en orden cronológico inverso. Cada entrada indica la fecha, los módulos afectados, el tipo de cambio y la decisión que lo motiva.

**Tipos:** `estructura` · `canon` (cambia una definición, regla, escala o indicador) · `método` · `editorial` (sin cambio de significado) · `gobernanza`.

## 2026-10-24 — Intake «prominencia informativa» · aplicado

- **gobernanza** — El intake prevalece sobre el contenido existente y se aplica sin aprobación previa ([D-016](decisions.md#d-016)). Skill `docs-update` reescrita.
- **canon** — `scoring-systems` 1.1: escala del IR fijada en **0–10** ([D-017](decisions.md#d-017)) y nuevo **estado binario de resolución** (propuesta, [D-019](decisions.md#d-019)).
- **canon** — Nuevo módulo `informative-prominence` 1.0 (propuesta): prominencia informativa, IP y calidad ajustada ([D-018](decisions.md#d-018)). Se reformula la invariante 7 del `CLAUDE.md` raíz.
- **gobernanza** — Nuevas OQ-31 a OQ-36 (sección G). OQ-28 anotada. Artefacto archivado en `archive/intake/2026-10-24-prominencia-informativa.md`.

## 2026-10-24 — Intake y skill docs-update

- **estructura** — Nueva bandeja `docs/intake/` y nueva skill `/docs-update` para procesar updates ([D-015](decisions.md#d-015)). El validador admite la clave de fuente `INTAKE <stem>` (comprueba que exista en `archive/intake/`) e ignora `intake/`.

## 2026-10-24 — Resolución de I-01, I-04, I-07, I-09 e I-10

- **canon** — `scope` 1.1: CTX §5 enumera los tres ámbitos ([D-013](decisions.md#d-013)). `quality-properties` 1.2: P07 entra en las asociaciones orientativas de Aplicabilidad ([D-014](decisions.md#d-014)).
- **editorial** — Denominaciones confirmadas: TRI y Tasa de cumplimiento técnico, con los alias de FUND ([D-003](decisions.md#d-003)); «Taxonomía de clases de producto» ([D-012](decisions.md#d-012)). Nombre del proyecto: **stratia.cic** ([D-011](decisions.md#d-011)).
- **gobernanza** — Todas las incidencias I-01 a I-10 quedan resueltas.

## 2026-10-24 — Resolución de I-02 e I-03

- **canon** — `demand-model` 1.1: el modelo de demanda tiene dos vías de construcción, la taxonomía de clases de producto y el MPIR (BASE §4.2 enmendada, [D-009](decisions.md#d-009)).
- **canon** — «Interfaz» y «ámbito» son sinónimos en la unidad de evaluación ([D-010](decisions.md#d-010), sustituye a D-004). Se retiran las marcas ⚠ I-03 de `evaluation-scopes`, `evaluation-architecture`, `scoring-systems`, `acceptance-criteria`, `inputs-outputs`, `integration` e `interpretation-transfer`.
- **gobernanza** — I-02 e I-03 resueltas. Se reformula la propuesta de I-04.

## 2026-10-24 — Resolución de I-05, I-06 e I-08

- **canon** — `quality-properties` 1.1: la definición de propiedades (BASE §5.3) queda enmendada y se elimina «y los requisitos técnicos generales». Las propiedades son exclusivamente informativas y P01–P05 quedan retirados ([D-007](decisions.md#d-007)).
- **gobernanza** — I-05 e I-08 resueltas por D-007; I-06 resuelta por [D-008](decisions.md#d-008): antecedentes no incorporados y documentos de apoyo no disponibles.

## 2026-10-24 — Línea base 1.0

- **estructura** — Reorganización del corpus v0 en capas y módulos ([D-001](decisions.md#d-001)). Originales archivados en `archive/v0-2026-10-24/` ([D-002](decisions.md#d-002)).
- **estructura** — Nuevos: `CLAUDE.md` raíz, `docs/CLAUDE.md`, `docs/README.md`, `docs/glossary.md` y `tools/check_docs.py`.
- **canon** — Sin cambios de significado. Definiciones normativas trasladadas literalmente desde CTX/BASE; interpretación condensada desde FUND.
- **editorial** — Correcciones tras la revisión independiente de fidelidad. Se restituyen citas literales de CTX/BASE en `scope`, `scoring-systems` y `demand-model`. Se corrige la «conformidad técnica como requisito necesario» (`commercial-information`). Se retira «no hay compensación entre criterios» como regla vigente y se remite a M09 (propuesta). Se restituyen matices de FUND §3.6, §4.1, §4.3, §6.2, §7.3 y §12. Se marca la procedencia GSC0 donde correspondía. En `20-methods/`: se restituyen las condiciones de los casos de calibración G, H, J, K y L, la tabla de dimensiones del registro de FUND §9.4 (`evidence`) y GSC0 §18.1–18.2 (`open-questions`); se marcan los bloques vigentes de FUND; se unifica la definición de evidencia y hallazgo. La matriz de cobertura de GSC0 §19 es metadocumentación del borrador v0 y **no se traslada**: se consulta en el archivo.
- **gobernanza** — Incidencias I-01 a I-10 registradas; cuestiones abiertas consolidadas (OQ-01 a OQ-30); decisiones provisionales D-003 y D-004.
- **método** — GSC0, TAX y MPIR divididos en módulos de `20-methods/`, con los IDs de reglas originales.
