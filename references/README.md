# references

Sistema de **custodia común de las fuentes externas** de todos los sistemas del proyecto ([D-149](../docs/30-governance/decisions.md#d-149)): un solo registro, un solo almacén de versiones congeladas, una sola versión fijada por fuente, el diff entre versiones y los lectores por formato.

- **Las fuentes se comparten; su interpretación, no.** Lo que una fuente significa para un sistema queda en ese sistema: el catálogo de bloques y las reglas, en [demand-engine](../demand-engine/README.md); las fichas de fuente y los requisitos técnicos (la referencia técnica), en [web-audit/reference/](../web-audit/reference/README.md).
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)). Solo usa la biblioteca estándar.
- **Consumidores:** demand-engine (taxo, blocks, el motor de demanda y PAA) y web-audit (reqs) leen de aquí desde el corte (T-060). Los documentos de Google Search con tablas de propiedades los usan los dos: web-audit para sus requisitos técnicos y demand-engine como apoyo del modelo de demanda (T-056). Las normas que cita el catálogo de demand-engine (T-062) y los códigos ISO de moneda y país, que comprueba web-audit, también están aquí. Sus envoltorios de `bin/` ponen `references/src/` en la ruta; en el contenedor está en `PYTHONPATH`.

## Registro

[sources.json](sources.json):

- `systems`: cada sistema que usa fuentes, con `review`, cómo revisa lo que construyó sobre una versión cuando cambia la fijada.
- `sources`: una entrada por fuente: `id` (kebab-case; es el que nombra una cita), `kind`, `title`, `publisher`, `url` y `uses` (los sistemas que la usan). Opcionales: `inventory` (código en el inventario de partida de web-audit) y `note`. Cada tipo puede pedir campos propios: una norma, `cite` (su código en las citas `ley:`) y `boe` o `celex`; una tabla de EU Vocabularies, `authority` y `file`.

**Tipos de fuente** (`kind`; el detalle, en [kinds/](src/references/kinds/__init__.py)):

| Tipo | Fuentes | Versión |
|---|---|---|
| `shopify-taxonomy`, `shopify-google` | taxonomía de Shopify (ficheros en español) y su mapeo oficial a Google | la release de GitHub, comprobada con su digest |
| `google-taxonomy` | taxonomía de productos de Google es-ES | la cabecera del fichero |
| `amazon-browse-tree`, `amazon-ptd` | árbol de navegación y Product Type Definitions de Amazon.es (SP-API) | la fecha de la extracción |
| `schemaorg` | vocabulario Schema.org en formato máquina | la release, comprobada con el sha de git de cada fichero |
| `document` | un documento publicado: página HTML (se guarda tal cual, `page.html`, y con su texto, `text.md`), PDF o fichero de datos (la lista ISO 4217 de SIX) | la fecha de descarga |
| `law` | una norma por su texto consolidado oficial: el BOE (API de legislación consolidada: `texto.xml` con la historia de cada bloque) o EUR-Lex a través de Cellar, el repositorio de la Oficina de Publicaciones (`page.html`; eur-lex.europa.eu responde con un desafío). Se guarda tal cual y con su `text.md`: un encabezado por artículo (`## Artículo 16`) y una línea por párrafo, que abre su marca (`1.`, `e)`) | la fecha con que la fuente oficial nombra el texto: en el BOE, la de publicación de la última modificación que incluye; en EUR-Lex, la de la versión consolidada o, en el original, la de su publicación en el DO. Por defecto, la última vigente; `--version` congela otra (por ejemplo, el original) |
| `eu-authority` | una tabla de autoridad de EU Vocabularies (la de países, con los códigos ISO 3166-1) | la release de la tabla (`owl:versionInfo`, `20260923-0`) |

## Versiones

- `var/<fuente>/<versión>/`, con sus ficheros y un `MANIFEST.json`: origen, tamaño, sha256, fecha y, si la página la declara, su marca de versión.
- Las versiones **no se sobrescriben**, y una descarga igual a la última **se descarta**. Un `.gz` cuenta por su contenido descomprimido y una página HTML por su texto: un cambio solo de marcado no crea versión. Los errores de una descarga parcial (PTD) quedan en el manifiesto y cuentan como contenido.
- Orden natural de versiones: `9.0` antes que `30.1`.
- **Versión fijada:** `var/pins.json`, una por fuente para todos los sistemas. La primera versión de una fuente se fija sola. Después solo la cambia `refs pin`, que lista los sistemas de `uses` y cómo revisa cada uno lo construido sobre la anterior (`refs diff`).

## Lectores

`references.read` da el contenido de la versión fijada, por formato:

- **taxonomía:** categorías y atributos de Shopify, mapeo a Google, nombres de Google y el árbol de Amazon;
- **PTD de Amazon:** propiedades y definición de un tipo de producto, valores de sus enumeraciones;
- **vocabulario en JSON-LD:** la definición de cada término (Schema.org, GS1);
- **documentos:** encabezados y secciones de un `text.md` (un encabezado y todo lo que cuelga de él, o `#`, el preámbulo: el texto antes del primer encabezado), y el texto citable de una fuente.
- **normas:** el pasaje que nombra una cita `ley:CÓDIGO-artículo.apartado.letra@versión` (`ley:TRLGDCU-97.1.e@2026-02-28`): el texto entero, un artículo o, dentro de él, la línea que abre la marca del apartado o la letra y las que la siguen hasta la siguiente marca del mismo tipo. El código es el `cite` de la norma (gana el más largo); sin versión, la fijada. Error si la norma no está registrada, la versión no está congelada o el pasaje no existe. También, los artículos que cambian entre dos versiones.
- **códigos:** los alfabéticos de ISO 4217 (lista uno de SIX: nombre, número, decimales y entidades) y los alfa-2 de ISO 3166-1 (tabla de países de EU Vocabularies, sin los retirados; incluye algunos que ISO reserva excepcionalmente, como EU o IC).
- **tablas de propiedades** (documentos de Google Search): en la sección de definiciones de tipos, cada fila con su tipo (el del encabezado, el del encabezado superior que lo nombre o el único del título), sus nombres (`price or priceSpecification.price`, `gtin | gtin8`), su tabla (`required` o `recommended`) y grupo (`Option A`), su encabezado, el tipo esperado y el texto de la celda, en la versión fijada o en otra. Una fila de prosa («Choose either…») no tiene nombres. Una cita `fuente:Tipo.propiedad@versión` (`google-search-merchant-listing:Product.audience@2026-10-27`) se resuelve en esa versión, o da error. La tabla da la naturaleza incondicional: una obligación condicional («only required if…») queda en el texto.

`references.store.pins(sistema)` da solo las versiones fijadas de las fuentes que usa ese sistema: es lo que registra un resultado de ese sistema.

## Uso

`references/bin/refs status | check | fetch | diff | pin` (`--help`). Se ejecuta en el host.

- `refs props FUENTE [TIPO]` muestra las tablas de propiedades de un documento y `refs props FUENTE:Tipo.propiedad@VERSIÓN` resuelve una cita.
- `refs law ley:CÓDIGO-ARTÍCULO.APARTADO@VERSIÓN` muestra el pasaje que cita y `refs law FUENTE [ANTIGUA NUEVA]` los artículos que cambian entre dos versiones (por defecto, de la fijada a la última).
- `check` no guarda nada; `fetch` descarga una versión nueva (puntual y a petición, con un segundo entre documentos); `--version` solo para las fuentes con release (Shopify, Schema.org, EU Vocabularies) y las normas.
- **Credenciales de SP-API** (fuentes de Amazon): `SPAPI_LWA_ID`, `SPAPI_LWA_SECRET` y `SPAPI_REFRESH_TOKEN`, en `references/.env` (fuera de git y de las imágenes; los nombres, en `.env.example`) o en el entorno.
- `REFS_DIR` cambia el directorio de las versiones y `SOURCES_FILE` el registro (pruebas).

## Estructura

```
references/
├── pyproject.toml          miembro del workspace (solo biblioteca estándar)
├── bin/refs                envoltorio de línea de comandos (el código está en src/)
├── sources.json            registro de fuentes y sistemas
├── src/references/         store (custodia), net (HTTP y SP-API), html (texto de una página),
│                           kinds/ (comprobar, descargar y comparar por tipo: taxonomías, Amazon,
│                           Schema.org, documentos, normas, tablas de EU Vocabularies), read (lectores), cli
├── tests/                  pruebas
├── .env.example            variables de .env (las credenciales de SP-API, solo en .env)
└── var/                    desechable: las versiones y pins.json
```

## Qué entra en git

En git va **lo que gobierna el sistema**: código, pruebas y `sources.json`. `var/` es desechable y no tiene copia; git no es una copia de seguridad. Si se pierde, se regenera con `refs fetch`, pero la versión de un documento o de una extracción de Amazon lleva la fecha de su descarga: la nueva tendrá otra fecha y, si cambió en origen, otro contenido. Las citas, los modelos y las reglas que nombran la versión perdida habrá que revisarlos. Las releases de Shopify y Schema.org sí se recuperan iguales.

## Pruebas

`bin/run dev test references/tests` (todas las del proyecto: `bin/run dev test`).
