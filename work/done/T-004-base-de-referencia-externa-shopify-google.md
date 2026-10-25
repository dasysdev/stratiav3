---
id: T-004
title: Base de referencia externa (Shopify, Google, Amazon) con actualización manual
status: hecha
depends:
milestone: taxonomia
created: 2026-10-24
closed: 2026-10-24
---

## Objetivo

Descargar y conservar, versionado e inmutable, el material de referencia de la taxonomía (Shopify es, Google es-ES, Amazon.es browse tree y PTD) con bin/refs status/check/fetch/diff/pin

## Criterios de aceptación

- [x] bin/refs fetch descarga cada fuente a refs/<fuente>/<versión>/ con MANIFEST.json (URL, sha256, tamaño, fecha) y nunca sobrescribe una versión existente
- [x] bin/refs check informa si hay versión nueva sin descargar nada
- [x] bin/refs diff lista categorías añadidas, eliminadas, renombradas o movidas entre dos versiones
- [x] Shopify v2026-08 (es), Google es-ES y Amazon.es descargados y verificados por sha256
- [x] Credenciales SP-API solo en .env no versionado

## Resultado

bin/refs: Shopify es v2026-08, Google es-ES 2021-09-21, árbol Amazon.es y 1877 PTD congelados por versión, con check/fetch/diff/pin

## Notas

- 2026-10-24 Amazon: credenciales LWA de vendedor (región UE) copiadas de amazonconnectorv2/app/www/.env.local a .env (ignorado). Los valores venían entre comillas: load_env las quita. La cuenta participa en Amazon.es (A1RKKUPIHCS9HS).
- 2026-10-24 Medido: Shopify es 12,6 MB/versión; Google es-ES 0,6 MB (sigue en 2021-09-21); árbol Amazon.es 1,5 MB gz (27.753 nodos, 2242 con varias rutas); PTD 1877 tipos, unos 90 KB gz por esquema; páginas R1–R16 14,4 MB.
- 2026-10-24 R08 de sources.md (lang-es_es) redirige a 404; funciona con lang-es_ES. R06a/b (Seller Central) solo devuelven la portada pública: la ayuda exige login.
- 2026-10-24 PTD Amazon.es: 1877 definiciones y 1877 esquemas (122 MB), verificados por el MD5 publicado; sin enlaces firmados guardados. Shopify verificado contra el sha256 que publica GitHub; Google y el árbol de Amazon no publican hash: su sha256 queda registrado en el manifiesto.
- 2026-10-24 Fuente docs (páginas R1–R16) eliminada a petición del usuario. Gestión de las actualizaciones (changelog, notas de release) aplazada por el usuario.
