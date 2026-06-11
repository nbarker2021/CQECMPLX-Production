# Promotion Slice: TMN1 Operations and Docker Docs

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-TMN1-Conservation-Fullstack.manifest.json`

## Scope

This slice promotes TMN1 operational documentation, showcase material, and
Docker metadata. It records TMN1 as a fullstack conservation/MORSR/E8 operations
candidate without promoting large formalization payloads or runtime state.

## Included Source Root

- `D:\CQE_CMPLX\g\CMPLX-TMN1`

## Included Content

- architecture, channels, Docker, economy, ecosystem, fullstack, operations,
  playbooks, and subsystem docs;
- portal/API and connection docs;
- showcase system/tool docs;
- infrastructure Compose and Dockerfiles.

## Normalization Applied

- `POSTGRES_PASSWORD` in the promoted Compose file now requires an explicit
  environment value.
- concrete-looking API key examples in `PORTAL-API.md` were replaced with
  `<api_key>`.

## Exclusions

- `formalizations\CQE_Classified_Formalizations.json`, which is large enough to
  require payload-ledger handling before body promotion;
- runtime databases, `.env` files, logs, generated service data, archives,
  caches, virtual environments, and local secrets.

## Production Interpretation

TMN1 is now tracked as an operations layer, not only a role family. Future work
should bind MORSR conservation claims to receipts and align Docker services with
the Docker Compose Boundary adapter.
