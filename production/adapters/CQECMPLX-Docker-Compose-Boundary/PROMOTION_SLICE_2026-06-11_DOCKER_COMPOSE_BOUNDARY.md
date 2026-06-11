# Promotion Slice: Docker Compose Boundary

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-Docker-Compose-Boundary.manifest.json`

## Scope

This slice promotes the kernel-level Docker and Compose boundary contracts. It
supports the deployment pattern where the kernel can operate as a sidecar while
external needs are inserted through a constrained boundary adapter.

## Included Roots

- `D:\CQE_CMPLX\CMPLX-Kernel\kernel\deploy\docker`
- `D:\CQE_CMPLX\CMPLX-Kernel\kernel\docs`
- `D:\CQE_CMPLX\CQECMPLX-ProofValidatedSuite\kernel`

## Included Content

- kernel Dockerfile;
- Docker-in-Docker and socket-mounted Compose variants;
- compose insert schema and template;
- Docker boundary and tool-adapter docs;
- proof-validated Compose kernel reference.

## Exclusions

- `D:\CQE_CMPLX\DockerContainers` runtime and workspace payloads;
- `.env` files, volumes, logs, generated data, caches, archives, and database
  payloads;
- arbitrary Compose files not explicitly admitted by the manifest.

## Production Interpretation

This is the adapter package, not a copied Docker workspace. New external needs
should be inserted through the provided schema/template shape so the kernel can
stay above and around the existing lower Compose layers.
