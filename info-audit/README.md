# info-audit

Sistema de la **auditoría informativa** de los ámbitos Contenido y Marcado: disponibilidad efectiva y GSC por AC de cada unidad RI × ámbito. Sigue el método [audit-gsc](../docs/20-methods/audit-gsc/README.md) (propuesta V1). La evaluación técnica es de [web-audit](../web-audit/README.md) y es independiente: info-audit no depende de ella en el piloto (T-097).

- **Canon:** [docs/10-model/](../docs/10-model/evaluation-architecture.md). Prevalece sobre el método y sobre lo de aquí.
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Ejecución en dos fases

La ejecución es la de [D-153](../docs/30-governance/decisions.md#d-153) y [D-223](../docs/30-governance/decisions.md#d-223) ([execution](../docs/20-methods/audit-gsc/execution.md#ejecución-en-dos-fases)):

1. **Fase 1:** un agente por ficha × ámbito decide la disponibilidad efectiva de todos los RI pertinentes. Escribe un registro de disponibilidad.
2. **Validación:** `bin/audit validate` comprueba el registro. Lo que no pasa no va a la fase 2 (QA-15).
3. **Fase 2:** un agente por lote de RI con disponibilidad 1 valora los seis AC. Escribe un registro de valoración por lote.
4. **Validación:** `bin/audit validate` comprueba cada registro de valoración contra el de su fase 1.

Cada agente lee solo la representación de su ámbito: en Contenido, la salida del [filtro Alfa](../docs/20-methods/audit-gsc/filter-alfa.md) (`alfa/1`); en Marcado, el marcado (`markup/1`).

## Registros

Los registros son JSON validado y versionado ([D-199](../docs/30-governance/decisions.md#d-199)). Los esquemas están en `schemas/`, con la versión en el nombre del fichero. El validador solo usa la biblioteca estándar y admite un subconjunto de JSON Schema: una palabra fuera del subconjunto es un error del esquema.

| Esquema | Registro | Qué contiene |
|---|---|---|
| `common.v1.json` | — | Definiciones comunes: evidencia con localizador y contenido original ([evidence](../docs/20-methods/audit-gsc/evidence.md)), cobertura de una ausencia ([availability-coverage](../docs/20-methods/audit-gsc/availability-coverage.md#registro-de-cobertura)), comprobación fallida de una NE o de una comprobación inconclusa, representación y modelo. |
| `availability.v1.json` | `info-audit/availability` | Fase 1: universo examinable, evidencias y la disponibilidad de cada RI pertinente (0, 1, o `null` con estado `inconclusa`). |
| `assessment.v1.json` | `info-audit/assessment` | Fase 2: evidencias de la reapertura, hallazgos y los seis AC de cada RI del lote ([gsc-decision](../docs/20-methods/audit-gsc/gsc-decision.md)), con las propiedades consideradas y su efecto ([D-198](../docs/30-governance/decisions.md#d-198)). |

Los nombres de los campos son los de las plantillas del método (`contenido_original`, `localizador`, `disponibilidad_efectiva`…). Las rutas de un registro (`representation.file`, `model.file`, `availability`) son relativas a la raíz del repositorio. Ningún esquema tiene pesos, medias, GSC global ni fórmula de IR; una prueba lo comprueba. `ir` solo aparece con disponibilidad 0, con valor 0.

### Qué rechaza `bin/audit validate`

- Un campo que el esquema no prevé, un tipo erróneo o un valor fuera de su lista: disponibilidad distinta de 0, 1 o `null`; GSC distinto de 0, 1, 2 o `null`.
- Un contenido original que no está literal en la representación del ámbito, o que no está en su `posicion` (QA-15). Las evidencias de tipo `ausencia` y `limitacion_acceso` no citan texto y no se comprueban.
- Una lectura que no es la del ámbito: Contenido con otra cosa que `alfa/1`, Marcado con otra cosa que `markup/1`.
- En la fase 1:
  - una disponibilidad 0 sin registro de cobertura o sin `ir` = 0 (CO-08);
  - una comprobación inconclusa sin la comprobación que falló;
  - un RI que no es pertinente en el modelo del ámbito, o un RI pertinente sin disponibilidad.
- En la fase 2:
  - AC valorados en un RI con disponibilidad 0 o inconclusa en la fase 1 (GSC-01);
  - un RI sin los seis AC, cada uno una vez;
  - un GSC sin evidencias (GSC-12);
  - una NE sin la comprobación que falló;
  - un NA de criterio, salvo el de Comparabilidad en un requisito que el modelo marca como no dimensión de comparación ([D-126](../docs/30-governance/decisions.md#d-126)).
- Una evidencia, un hallazgo o un id citado que no existe, o un id repetido.

### Representaciones

- **`alfa/1`:** la salida del filtro Alfa (`filter`, `version`, `ficha`, `title`, `text`, `fragments`). Un contenido original está en `title` o en `text`; `posicion` es [inicio, fin) en `text`. El filtro es T-103.
- **`markup/1`:** el marcado Schema.org de la respuesta (JSON-LD, microdatos y RDFa): `reader` (`markup`), `version` (1), `ficha` y `blocks`, cada uno con su `text` literal. Su lector está pendiente (T-098).

## Uso

```
info-audit/bin/audit validate RECORD.json [RECORD.json …]
```

El comando escribe «válido» o los errores de cada registro. Si un registro tiene errores, termina con código 1.

## Estructura

```
info-audit/
├── pyproject.toml     miembro del workspace (solo biblioteca estándar)
├── bin/audit          envoltorio de línea de comandos (el código está en src/)
├── schemas/           esquemas JSON de los registros, versionados (D-199)
├── src/info_audit/    schema (validador del subconjunto), records (reglas), audit (CLI)
├── tests/             pruebas
└── var/audits/AUDIT/  registros de cada auditoría (fuera de git)
```

## Qué entra en git

Todo lo de info-audit salvo `var/`: código, esquemas, pruebas y `pyproject.toml`. `var/` es desechable.

## Ejecución

- **`audit`** se ejecuta en el host (`info-audit/bin/audit …`) y solo usa la biblioteca estándar.
- **Pruebas:** `bin/run dev test info-audit/tests` (todas las del proyecto: `bin/run dev test`).
