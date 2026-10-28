# Contexto de la petición del perfil de consumo y datos en scripts que no son marcado

Decisión del usuario del 2026-10-28, tomada en sesión, que cierra OQ-78 y OQ-79 con las recomendaciones de Claude. Recogida por Claude el mismo día.

## Contexto

Al analizarlo, Claude vio que el motor de captura está hecho para parecer un Chrome corriente y evitar bloqueos: perfil persistente, user agent real, `--lang=es-ES`, `--accept-lang=es-ES,es`, sin banderas de automatización (políticas de D-042/D-046). Propuso separar cómo se obtiene la ficha (el motor) de qué contexto de petición define la representación, y corregir solo lo que sesga el resultado y es barato.

## OQ-78 · Contexto de la petición (recomendaciones de Claude)

| Punto | Recomendación | Por qué |
|---|---|---|
| a · Estado | Estado limpio por ficha: antes de cada captura se borran cookies y almacenamiento del dominio; nunca se acepta un banner. | Es el sesgo más claro (consentimiento heredado que ninguna IA recibe); todas las IA llegan sin estado. Riesgo: más desafíos antibot; se mide en el piloto, y un desafío es incidencia, no ausencia. |
| b · Accept-Language | `es-ES`, registrado en la ficha. | Perímetro: el comprador español; los navegadores agénticos envían el del usuario; omitirlo exige interceptar peticiones y es señal de bot; una tienda .es suele servir español. |
| c · IP de origen | España, registrando país y ASN; sin proxies. | Perímetro España; ChatGPT-User tiene subredes en Madrid y los agentes salen con la IP del usuario; una IP de EE. UU. exige proxy y podría auditar otra tienda. |
| d · User agent | El real de Chrome; no se reabre D-042/D-046. | Un token propio aumenta bloqueos; suplantar un bot desde una IP ajena es un bot falso para el WAF. |
| e · robots.txt por bot | Registrarlo en la ficha (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Googlebot, Google-Extended, Bingbot, Meta, Amazon). No afecta al GSC. | El motor ya lee robots.txt; es un hecho técnico útil para el informe y web-audit, sin efecto en la disponibilidad bajo el perfil (invariante 8). |
| f · Sondas desde EE. UU. o con en-US | No. | Contradice el perfil único; si un cliente vende fuera, perfil nuevo más adelante. |

## OQ-79 · Datos en scripts que no son marcado (opción B de Claude)

No cuentan como información: no dan disponibilidad ni sirven de base a los AC. Solo diagnóstico: si el auditor ve que el dato existe en el estado de la aplicación pero no en el HTML ni en el marcado, lo registra como hallazgo («el dato existe en el estado de la aplicación pero no se publica»).

Frontera: cuentan el texto del HTML (también el oculto), los atributos y el marcado; de los scripts, solo `application/ld+json`; los demás scripts, no. Coherente con el caso C de calibración («contenedor vacío → disponibilidad 0»).

Motivos: son estructuras internas pensadas para que las consuma JavaScript, con claves sin significado publicado; las lecturas en vivo las descartan; y contradiría el fundamento de D-156 (que la información no dependa de JavaScript). Descartadas: A (cuentan como información) y C (caso a caso, contra M10).

## Respuesta del usuario

> si. matiz sobre el perfil. Mantenemos el navegador real para evitar bloqueos. pero es un navegador que no ejecuta js.

(Texto original: «si. matiz sobre el perfil. Mantenemos el navegador real para evitar bloqueos. pero es un navegador que o ejecuta js.»)
