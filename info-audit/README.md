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

- **`alfa/1`:** la salida del filtro Alfa (`filter`, `version`, `ficha`, `title`, `text`, `fragments`). Un contenido original está en `title` o en `text`; `posicion` es [inicio, fin) en `text`. Ver *Filtro Alfa*.
- **`markup/1`:** el marcado Schema.org de la respuesta (JSON-LD, microdatos y RDFa): `reader` (`markup`), `version` (1), `ficha` y `blocks`, cada uno con su `text` literal. Su lector está pendiente (T-098).

## Filtro Alfa (`alfa/1`)

`audit alfa` aplica el filtro de lectura de Contenido a una ficha que capture congeló con `audit-es` ([D-221](../docs/30-governance/decisions.md#d-221)). La especificación es [filter-alfa](../docs/20-methods/audit-gsc/filter-alfa.md) y prevalece; esta sección dice cómo la aplica el código.

- **Entrada:** el page-ID de una ficha de `capture/var/pages/`. El filtro lee con el lector del almacén (`capture.pages`) la ficha y los bytes originales de su respuesta (`response.html.gz` de la instantánea).
  - Rechaza una ficha `reader`, una instantánea sin los bytes originales y una respuesta cuyo sha256 no es el de su `meta.json`.
- **Codificación** (`encoding.py`): el BOM; si no hay, el `charset` del `Content-Type` de la respuesta; si no hay, `<meta charset>` o `<meta http-equiv>` en los primeros 1024 bytes. Las etiquetas son las del Encoding Standard.
  - Sin ninguna declaración, el filtro usa UTF-8 si los bytes son UTF-8 válido, y si no, windows-1252. `encoding_from` lo dice: `detectada`.
- **Análisis** (`htmltree.py`): el tokenizador de `html.parser`, con los scripts desactivados, y las reglas de construcción del árbol del HTML Living Standard que deciden dónde va cada nodo. El docstring del módulo da las reglas y las dos simplificaciones, que no cambian el texto ni su orden.
- **Texto** (`alfa.py`): lo que entra y lo que no entra son las listas de la especificación. Cada bloque de su lista empieza una línea, y el texto que sigue a un bloque, otra.
  - Un título lleva `#` a `######`; un elemento de lista, `- `; una fila, sus celdas separadas por ` | ` (una celda vacía deja su separador: `A | | C`).
  - `<pre>` conserva sus espacios. En lo demás, los espacios ASCII se colapsan y el espacio duro (U+00A0) se conserva.
  - Una imagen se sustituye por su `alt`, con un espacio colapsable a cada lado.

| Campo | Contenido |
|---|---|
| `filter`, `version` | `alfa`, `1` |
| `ficha` | El page-ID de la ficha |
| `source` | Perfil, URL final, fecha de captura, instantánea, sha256 de la respuesta, codificación (`encoding`, `encoding_from`) y analizador (con la versión de Python) |
| `title` | El título del documento: el primer `<title>` que no es de `<svg>`, con los espacios colapsados |
| `text` | El contenido textual del cuerpo, en el orden del documento y sin corte |
| `fragments` | Un fragmento por nodo de texto y por `alt`, en el orden del texto |

Cada fragmento lleva `start` y `end` (su `posicion`: [inicio, fin) en `text`), `text` (igual a `text[start:end]`) y `ruta`. Las demás anotaciones solo aparecen si se dan:

| Anotación | Valor |
|---|---|
| `ruta` | La ruta del elemento: `/html/body/div[2]/p`. El número va si hay hermanos con la misma etiqueta. |
| `oculto` | Lo que lo oculta, de fuera a dentro: `hidden`, `aria-hidden`, `inert`, `display:none`, `visibility:hidden` (del atributo `style`), `dialog` (sin `open`) o `details` (cerrado, fuera de su `<summary>`). |
| `region` | `header`, `nav`, `footer`, `aside`, `role=banner`, `role=navigation`, `role=contentinfo` o `role=complementary`, de fuera a dentro. |
| `control` | `form`, `select`, `button`, `textarea` o `label`, de fuera a dentro. |
| `alt` | `true`: el fragmento es el `alt` de un `<img>`. |
| `enlace` | La URL absoluta del enlace (`<a href>`), contra la `<base href>` o la URL final de la ficha. |

- **Salida:** `info-audit/var/representations/PAGE-ID.alfa-1.json` (fuera de git), con un fragmento por línea. Es el `representation.file` de los registros de Contenido.
- **No se sustituye:** si la salida ya existe y es igual, no cambia. Si existe y es distinta, `alfa` termina con error, porque los registros citan sus posiciones. Para escribirla de nuevo, bórrala.
- **Versión:** el filtro solo cambia de versión si cambia su definición o su lectura de la norma ([reading-filters](../docs/10-model/reading-filters.md)). Una corrección del código que cambia la salida es `alfa/2`.

## Uso

```
info-audit/bin/audit validate RECORD.json [RECORD.json …]
info-audit/bin/audit alfa PAGE-ID [PAGE-ID …]
```

- `validate` escribe «válido» o los errores de cada registro. Si un registro tiene errores, termina con código 1.
- `alfa` escribe, para cada ficha, los caracteres de `text`, los fragmentos, los fragmentos con `oculto` y la ruta de la salida. Si una ficha falla, termina con código 1.

## Estructura

```
info-audit/
├── pyproject.toml     miembro del workspace (solo biblioteca estándar)
├── bin/audit          envoltorio de línea de comandos (el código está en src/)
├── schemas/           esquemas JSON de los registros, versionados (D-199)
├── src/info_audit/    schema (validador del subconjunto), records (reglas), audit (CLI),
│                      alfa (filtro Alfa), htmltree (árbol del documento), encoding (codificación)
├── tests/             pruebas
└── var/
    ├── audits/AUDIT/  registros de cada auditoría (fuera de git)
    └── representations/  salida de alfa/1 de cada ficha (fuera de git)
```

## Qué entra en git

Todo lo de info-audit salvo `var/`: código, esquemas, pruebas y `pyproject.toml`. `var/` es desechable.

## Ejecución

- **`audit validate`** se ejecuta en el host (`info-audit/bin/audit …`) y solo usa la biblioteca estándar.
- **`audit alfa`** se ejecuta con Python 3.13, en el contenedor: el tokenizador de `html.parser` cambia entre versiones de Python. Desde el host, con un Python anterior, delega en el contenedor. Solo usa la biblioteca estándar y el lector del almacén de capture.
- **Pruebas:** `bin/run dev test info-audit/tests` (todas las del proyecto: `bin/run dev test`).
