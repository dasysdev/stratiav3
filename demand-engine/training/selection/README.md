# Selección del catálogo de entrenamiento

El catálogo de entrenamiento son las fichas de producto de tiendas reales que el entrenamiento clasifica y de las que induce reglas ([model-training](../../../docs/10-model/model-training.md#casos-alcance-y-ejecución), [OQ-48](../../../docs/30-governance/open-questions.md)). Cada selección se describe en un `STORE.spec.json` y se genera de forma determinista en `STORE-FECHA.json`.

## Criterio

**Amplitud antes que profundidad.** Pocas fichas de cada tipo de producto y tantos tipos como sea posible, para que el entrenamiento vea muchas clases.

1. **Tienda.** Generalista y con muchos departamentos. Amazon.es no se captura.
2. **Legitimidad.** `check_site` del motor de captura con veredicto `ok` (robots.txt, reserva TDM, portada). Ninguna ficha excluida por robots.txt.
3. **Universo.** Las fichas de producto de los sitemaps de la tienda (los que sigue `follow_products` de la especificación), leídos desde la ventana del propio sitio con el motor de captura. Quedan fuera los departamentos que no venden productos: entradas, tarifas planas, tarjetas regalo y cajas de experiencias.
4. **Un producto, una ficha.** Las variantes (talla, color) comparten el identificador del producto y cuentan una sola vez.
5. **Tipo de producto.** Es la primera palabra del nombre del producto en la URL, en singular y sin las palabras vacías de la especificación («juego de 2 vasos» → vaso), dentro de cada departamento. En los departamentos cuyos nombres son títulos (libros, cine, música), el tipo es el departamento. Es una aproximación previa a la captura. La clase de cada ficha es la que le da el clasificador.
6. **Tipos elegibles.** Los que tienen al menos `min_products` productos y, con `require_store_category`, una categoría de la tienda que los nombre: así quedan fuera las marcas y las palabras sueltas que encabezan algunos nombres. `exclude_types` quita tipos que no son productos (tarjetas regalo).
7. **Sorteo con semilla fija.** Los departamentos se ordenan al azar y los tipos se toman por rondas, uno de cada departamento por ronda, hasta `categories` tipos. Un tipo no se repite en otro departamento. De cada tipo se toman `per_category` fichas al azar y `reserves` reservas, que sustituyen a las que ya no existan al capturar.
8. **Piloto.** Los primeros `pilot` tipos, de departamentos distintos, validan la cadena completa antes de escalar.

`store_category` es la categoría de la tienda cuya última parte nombra el tipo (la más general). Es orientativa: a veces la coincidencia es solo de prefijo («medias» → medidor).

## Órdenes

```
bin/train discover training/selection/STORE.spec.json   # en el contenedor (desde el host delega)
bin/train select training/selection/STORE.spec.json [DESCUBRIMIENTO]
bin/train capture training/selection/STORE-FECHA.json [--pilot] [--max N] [--ignore-hours]
bin/train capture training/selection/STORE-FECHA.json [--pilot] --status
```

**Captura.** Un lote del motor de captura al ritmo de `pacing` de la especificación (en ECI: pausa de 10–30 s, pausa larga de 1–3 min cada 20–30 fichas, tope de 300 al día y `scroll: false`, la primera carga, D-053). Cada ficha capturada queda en `var/pages/ID.html` con su instantánea, como en `taxo page fetch`. Si una ficha ya no existe (404/410), o la excluyen robots.txt o una reserva TDM, la sustituye una reserva de su tipo. El registro `var/training/STORE/capture-SELECCIÓN.jsonl` hace el lote reanudable: lo capturado o descartado no se vuelve a visitar, y un bloqueo o un fallo se reintenta en la siguiente ejecución. Ante un desafío, el lote se para.

El descubrimiento queda en `var/training/STORE/discovery-FECHA/`: la comprobación del sitio, robots.txt y las URL de producto y de categoría. Es desechable: la selección guarda la carpeta y la fecha de la que sale.

## Selecciones

| Selección | Tienda | Tipos | Fichas | Piloto |
|---|---|---|---|---|
| [eci-2026-10-25](eci-2026-10-25.json) | El Corte Inglés ([spec](eci.spec.json)) | 100 de 26 departamentos (1.057 elegibles) | 300 + 200 reservas | 10 tipos de 10 departamentos, 30 fichas |

### El Corte Inglés (2026-10-25)

- **Comprobación del sitio:** veredicto `ok`. robots.txt excluye a Bytespider y Amazonbot (no nos aplica); hay antibot de Akamai.
- **Universo:** 48 sitemaps de producto del índice de variantes (propios y de marketplace; de libros, solo el primero de nueve): 501.645 URL, 397.810 productos tras quitar 102.715 variantes. Fuera: entradas, tarifa plana, tarjetas y cajas regalo, y sneaker-room (sus nombres empiezan por la marca).
- **Formas de URL:** `/{departamento}/{id}-{variante}-pr-{nombre}/` con variantes y `/{departamento}/{id}-{nombre}/` sin ellas; el id es `A…` o `MP_…` (marketplace).
- **Piloto:** mermelada, sopera, bolso de viaje, música (vinilo y CD), piercing, deportiva infantil, mochila escolar, lijadora, botella térmica y aceite de motor.

