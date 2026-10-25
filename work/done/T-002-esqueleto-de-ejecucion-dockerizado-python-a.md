---
id: T-002
title: Esqueleto de ejecución dockerizado (Python) a partir de stratia.rpa
status: hecha
depends:
milestone: codigo
created: 2026-10-24
closed: 2026-10-25
---

## Objetivo

Cuando empiece el código de producto: Dockerfile base/dev/prod con uv, compose de dev, bin/run <entorno> <comando> autodocumentado y pytest dentro del contenedor, tomados de stratia.rpa.

## Criterios de aceptación

- [x] bin/run dev up levanta el servicio Python con el código montado
- [x] bin/run dev test ejecuta pytest dentro del contenedor y termina en verde
- [x] Puertos publicados solo en 127.0.0.1 y ficheros creados con el UID del host

## Resultado

Esqueleto dockerizado: Python 3.13 + uv + Chrome sobre Xvfb, bin/run dev up|test|shell|lock|mpir, pytest en verde dentro del contenedor, sin puertos publicados

## Notas

- 2026-10-24 Sin base de datos de momento (decisión del usuario, 2026-10-24). Cuando haga falta, la recomendación es PostgreSQL.
- 2026-10-24 Medición de coste por tarea (agent-cost, a partir de rpa-cost) aplazada por el usuario.
- 2026-10-25 Ampliada (2026-10-25, decisión del usuario): la imagen lleva Chrome estable con ventana sobre Xvfb para el motor de captura del MPIR. No se publica ningún puerto: el CDP de Chrome no debe salir del contenedor.
- 2026-10-25 uv 0.12.24 fijado en la imagen; bin/run dev lock regenera uv.lock con la etapa base. Sin puertos publicados (el CDP no sale del contenedor). Ficheros de mpir/var con el UID del host. Imagen prod verificada: solo código, pyproject y uv.lock.
