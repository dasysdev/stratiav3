---
id: T-002
title: Esqueleto de ejecución dockerizado (Python) a partir de stratia.rpa
status: pendiente
depends:
milestone: codigo
created: 2026-10-24
---

## Objetivo

Cuando empiece el código de producto: Dockerfile base/dev/prod con uv, compose de dev, bin/run <entorno> <comando> autodocumentado y pytest dentro del contenedor, tomados de stratia.rpa.

## Criterios de aceptación

- [ ] bin/run dev up levanta el servicio Python con el código montado
- [ ] bin/run dev test ejecuta pytest dentro del contenedor y termina en verde
- [ ] Puertos publicados solo en 127.0.0.1 y ficheros creados con el UID del host

## Notas

- 2026-10-24 Sin base de datos de momento (decisión del usuario, 2026-10-24). Cuando haga falta, la recomendación es PostgreSQL.
- 2026-10-24 Medición de coste por tarea (agent-cost, a partir de rpa-cost) aplazada por el usuario.
