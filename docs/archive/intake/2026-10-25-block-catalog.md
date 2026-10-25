# Resolución de OQ-44: capa general, identificadores de bloques y denominación

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-011).*

*Fuente comprobada por Claude: artículo 97.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (RDL 1/2007), versión consolidada del BOE a 28/02/2026 (las letras f y p las modificó la Ley 10/2025). Regula la información precontractual de los contratos a distancia.*

## A. Capa general contrastada con el artículo 97.1

Aceptado por el usuario: «1. ok. opiniones como complementaria». Cambios sobre el borrador de D-034:

- **a) Características principales:** cubiertas por «¿qué es y qué incluye?» y por los bloques de clase.
- **b, c, d) Identidad, dirección y contacto del vendedor:** «¿Quién vende?» es principal; el contacto, complementaria.
- **e) Precio total, con impuestos y gastos de transporte o entrega:**
  - Se unen precio y envío en una cuestión crítica: «¿Cuál es el precio total que paga el comprador, con impuestos y envío a España?».
  - Lo que hace variar el envío queda como principal.
  - Resuelve la duda de si el envío es crítico.
- **f) Precio personalizado por decisión automatizada:** nueva cuestión condicionada (si lo está), principal.
- **h) Procedimientos de pago, entrega y fecha de entrega:**
  - Los medios de pago entran como complementaria: es información previa a la compra, aunque la transacción quede fuera del alcance. Resuelve la duda de los medios de pago.
  - El plazo de entrega sigue como principal.
- **j, k, m) Desistimiento:** se reformula la cuestión de devoluciones con las condiciones, el plazo, el coste de devolución y los casos en que no procede (principal).
- **n, ñ) Garantía legal, garantías comerciales y asistencia posventa:** se reformula la cuestión de garantía con esos elementos (principal).
- **p, q, r) Duración, suscripción, depósitos:** cuestiones condicionadas (si es suscripción o hay depósito).
- **s, t) Funcionalidad y compatibilidad de bienes con elementos digitales:** nueva condicionada (si el bien tiene elementos digitales), principal.
- **g, i, o, u)** Coste del medio de comunicación, lengua, códigos de conducta y resolución extrajudicial: fuera de la capa.
- **Opiniones de clientes:**
  - El artículo 97 no las incluye.
  - El usuario decide incluirlas «como complementaria».
  - La propuesta de Claude añadía que, si se publican, se pregunte cómo se garantiza que proceden de compradores reales. Es una obligación de la directiva Omnibus, cuya trasposición está por comprobar.

## B. Identificadores de los bloques

Palabras del usuario: «el formato de id debe ser nuestro, no quiero acoplarme por si en el futuro cambian las referencias. Para mantener trazabilidad con referencia puedes especificar un formato como el propuesto pero no como el campo de id, sino más bien como de referencias o algo del estilo. Lo dejo a tu criterio».

Lo que Claude había propuesto:

- **Identificadores:**
  - `gen` para las cuestiones universales;
  - `gen:<hecho>` para las condicionadas;
  - `shp:<id de categoría de Shopify>`: un único tipo de bloque para sector y categoría, con los atributos propios de cada categoría; sector y categoría solo se distinguen por la posición en la jerarquía;
  - `esp:<nombre>` para las especializaciones.
- **Campos de cada bloque:**
  - identificador, tipo, nombre, disparador, versión y estado;
  - requisitos, cada uno con identificador, pregunta, dimensión, entidad, importancia por defecto, origen (referencias, inferida o normativa), fundamento y aplicabilidad.
- **Cuestiones inferidas:** dentro del bloque de su categoría, con el origen marcado en cada requisito.
- **Ubicación del catálogo:** como datos, en `demand-engine/catalog/`.

El usuario acepta el resto y delega en Claude el formato de los identificadores propios.

## C. Sintaxis de la denominación

Aceptada: «3. si».

Hay dos niveles:

- **Clave, para la máquina (identidad):** la lista ordenada de bloques del modelo más la lista de bloques condicionados activos. Dos ofertas comparten modelo si comparten la primera lista.
- **Nombre, para personas:** «Categorías (alias) · especializaciones — aplicación».
  - Los bloques universales y los de sector no se nombran.
  - Las categorías se unen con «+», en el orden de las piezas.
  - Las especializaciones van en orden fijo: juego, uso, material, función.
  - La aplicación lista solo los bloques condicionados activos.

Ejemplos:

- «Sofás · tapicería de piel — unidad no nueva, con descuento».
- «Sofás cama (dos plazas)».
- «Sábanas planas + Sábanas ajustables + Fundas de almohada · juego, uso invernal, tejido polar — con variantes».

Cierra OQ-44.
