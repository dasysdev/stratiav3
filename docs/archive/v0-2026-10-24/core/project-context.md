# Contexto y marco del estudio

## 1. Punto de partida: la información comercial en el comercio digital

La **información comercial** comprende los contenidos, datos, afirmaciones y relaciones mediante los que un ecommerce describe sus productos, variantes, ofertas, vendedores y condiciones de comercialización. Esta información se representa y expone a través de distintos recursos e interfaces, entre ellos páginas HTML, datos estructurados y catálogos o feeds comerciales.

Los buscadores, las plataformas publicitarias, los sistemas de recomendación y los agentes de inteligencia artificial utilizan la información comercial para descubrir, interpretar, seleccionar, comparar y evaluar productos y ofertas. Su mera publicación no garantiza, por sí sola, que estos sistemas puedan utilizarla adecuadamente. También es necesario que resulte accesible, suficientemente detallada, comprensible, atribuible a las entidades y condiciones correctas, coherente y capaz de fundamentar conclusiones.

El problema que motiva el estudio es, por tanto, **en qué medida la información comercial y sus condiciones de representación y exposición permiten resolver las cuestiones informativas relevantes para evaluar una oferta**, más allá de la cantidad de datos publicados o del cumplimiento formal de un formato.

## 2. Marco funcional: Agentic Commerce

El estudio se sitúa en el contexto del **Agentic Commerce**, entendido como un modelo de comercio en el que agentes de inteligencia artificial pueden intervenir en distintas fases del proceso de compra, desde la búsqueda y valoración de alternativas hasta, cuando estén habilitadas, determinadas operaciones comerciales.

Las capacidades que un ecommerce puede ofrecer a estos agentes son de distinta naturaleza. Algunas permiten **descubrir, acceder, identificar, comprender, comparar y evaluar información comercial, así como justificar las respuestas obtenidas**; otras facilitan preparar o ejecutar operaciones de compra. Las interfaces son los medios técnicos mediante los que el comercio expone la información o habilita esas operaciones. La calidad de la información comercial y de su exposición condiciona el ejercicio efectivo de las capacidades informativas.

A efectos de delimitación, se distinguen cuatro fases del ciclo de compra:

| Fase | Finalidad | Relación con este estudio |
|---|---|---|
| **Descubrimiento y decisión de compra** | Encontrar ofertas, interpretar sus características y condiciones, contrastar alternativas y valorar su adecuación a una necesidad. | **Dentro del alcance.** |
| Preparación de la compra | Seleccionar o configurar productos y preparar una operación de compra. | Fuera del alcance. |
| Transacción | Autorizar y formalizar el pedido y el pago. | Fuera del alcance. |
| Postcompra | Consultar o gestionar pedidos, entregas, cancelaciones, devoluciones y reembolsos. | Fuera del alcance. |

En este contexto, la *Agentic Commerce Readiness* designa, en sentido amplio, el grado de preparación de un ecommerce para atender las capacidades que requieren los agentes. El estudio se centra en **las condiciones informativas y técnicas que favorecen el descubrimiento y la decisión de compra**, dentro del perímetro definido.

## 3. Objeto del estudio

El objeto del estudio es **la calidad de la información comercial y de sus condiciones de representación y exposición**, entendida como el grado en que la información publicada por un ecommerce y las interfaces que la presentan permiten **determinar y fundamentar respuestas suficientes a las cuestiones informativas relevantes para la demanda** de una clase de producto u oferta.

La evaluación comprende dos dimensiones complementarias:

- **Técnica:** condiciones de publicación, acceso, legibilidad, estructura, conformidad y distribución que permiten localizar, recuperar y consumir la información comercial mediante las interfaces pertinentes.
- **Informativa y semántica:** suficiencia, detalle, significado, relaciones, atribución, vigencia, coherencia y fundamento de la información necesaria para resolver las cuestiones relevantes.

Ambas dimensiones están relacionadas, pero expresan condiciones distintas. Una interfaz técnicamente conforme puede exponer información insuficiente para responder una cuestión de compra; a su vez, que una respuesta pueda fundamentarse mediante una interfaz no elimina necesariamente una limitación técnica o informativa de otra.

La calidad examinada se refiere a **la información comercial expuesta y su utilidad para la evaluación**, no a la calidad intrínseca de un producto ni a su conveniencia para un comprador particular. Una respuesta suficientemente fundada puede establecer tanto la adecuación como la incompatibilidad de una oferta con una necesidad de compra.

En la evaluación de calidad informativa, la disponibilidad efectiva constituye un requerimiento previo para examinar la resolución de cada requisito informativo en una interfaz pertinente. Se determina a partir de la existencia de información pertinente que pueda obtenerse y leerse bajo las condiciones de consumo previstas. Su comprobación se distingue de la evaluación de los requisitos técnicos de implementación de la interfaz.

## 4. Finalidad del modelo de auditoría

El estudio proporciona el marco para construir un **sistema de auditoría** que examine, mediante criterios explícitos y evidencias, la capacidad de la información comercial expuesta por un ecommerce para resolver las cuestiones relevantes de su demanda.

La auditoría permite identificar limitaciones de acceso, comprensión, atribución, contraste y fundamentación; distinguir las condiciones técnicas, informativas y semánticas que las explican; y orientar recomendaciones de mejora verificables.

La referencia de evaluación es **la posibilidad de determinar y justificar suficientemente la respuesta que corresponda** a cada cuestión, según la entidad, el alcance y las condiciones examinadas. La calidad no depende de acumular el mayor número posible de atributos ni de que una oferta satisfaga necesariamente las preferencias de un comprador.

El sistema evalúa las condiciones que ofrece el ecommerce para utilizar su información comercial. Sus resultados se refieren a esa capacidad informativa y técnica, diferenciada del comportamiento de un agente de IA específico y de los resultados comerciales de visibilidad o conversión.

## 5. Alcance y límites del estudio

El perímetro de trabajo corresponde al **contexto relevante para España desde octubre de 2026, con horizonte hasta, al menos, el primer trimestre de 2027**.

La delimitación funcional y técnica es la siguiente:

- **Fase examinada:** descubrimiento y decisión de compra.
- **Modalidad de interacción:** comercio agéntico **sin navegación interactiva**; se consideran vías de acceso y consumo de información que no requieren operar interactivamente las páginas o procesos de compra.
- **Información examinada:** características de productos y variantes, ofertas, vendedores y condiciones comerciales, según su pertinencia para las cuestiones evaluadas.
- **Interfaces y ámbitos de evaluación:**
    - **Catálogos distribuidos:** información comercial distribuida mediante feeds y catálogos destinados a plataformas comerciales.
    - **Web:** información comercial del recurso web considerado en su conjunto, incluyendo contenido HTML y marcado estructurado Schema.org.
- **Ámbito de las comprobaciones:** información publicada, sus representaciones y las condiciones técnicas de su exposición y distribución; no se auditan las operaciones de preparación, transacción o postcompra ni la infraestructura completa del ecommerce.

Las comprobaciones responden a la función y especificaciones de cada interfaz. Las distintas representaciones de una misma realidad comercial pueden aportar información complementaria; su interpretación debe preservar la atribución, el alcance y las condiciones de cada afirmación, así como reconocer discrepancias entre datos referidos a la misma entidad y a momentos comparables.

## 6. Encaje en el modelo de trabajo y sus ámbitos de aplicación

La auditoría forma parte de una iniciativa más amplia de **consultoría, enriquecimiento y optimización de información comercial** orientada a mejorar el rendimiento de productos y ofertas en canales orgánicos, canales de pago y entornos mediados por inteligencia artificial. La mejora de la calidad informativa y de sus condiciones de representación y exposición constituye una palanca para favorecer el descubrimiento, la visibilidad y la conversión cualificada.

El modelo de trabajo comprende cuatro ámbitos conectados:

1. **Auditoría y diagnóstico:** evaluar la información comercial y sus condiciones de exposición, documentar hallazgos e identificar oportunidades de mejora.
2. **Consultoría y planificación:** interpretar los resultados y priorizar actuaciones de enriquecimiento, normalización, estructuración, contextualización, coherencia, actualización y distribución.
3. **Implementación y transformación:** introducir mejoras en contenidos, datos, plataformas, integraciones y procesos comerciales.
4. **Medición y optimización continua:** verificar los cambios y evaluar sus efectos sobre la calidad informativa, la presencia en los canales y el rendimiento comercial, mediante métricas pertinentes.

El ámbito de aplicación es transversal e incluye **SEO, AI SEO y GEO; publicidad digital; recomendación y personalización; AI Commerce; PIM, PXM y gestión de feeds; ecommerce y CRO; y tecnología y operaciones**.
