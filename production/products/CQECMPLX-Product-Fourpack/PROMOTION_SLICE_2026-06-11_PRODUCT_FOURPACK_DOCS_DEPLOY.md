# Promotion Slice: Product Fourpack Docs and Deploy Metadata

Date: 2026-06-11

Manifest:
`tracking/promotion-manifests/CQECMPLX-Product-Fourpack.manifest.json`

## Scope

This slice promotes the first production-shaped accounting surface for the four
historical product packages. It includes product docs, pitch notes, Docker
metadata, package metadata, SDK metadata, and monitoring config where present.

## Included Source Roots

- `D:\CQE_CMPLX\historical_pastworks\product_authentica`
- `D:\CQE_CMPLX\historical_pastworks\product_converge`
- `D:\CQE_CMPLX\historical_pastworks\product_entropy`
- `D:\CQE_CMPLX\historical_pastworks\product_sentinel`

## Included Products

- `product_authentica`
- `product_converge`
- `product_entropy`
- `product_sentinel`

## Included Content

- README and PITCH files;
- Dockerfiles and Compose files;
- Python package metadata where present;
- TypeScript SDK package metadata for EntropyCore;
- Prometheus/Grafana monitoring config for Sentinel.

## Normalization Applied

- `AUTHENTICA_SECRET` in the promoted Compose file now requires an explicit
  environment value.
- the Authentica Dockerfile example uses `<set-secret>` instead of a local
  placeholder secret.
- Sentinel Grafana admin password now requires
  `GF_SECURITY_ADMIN_PASSWORD`.

## Exclusions

- runtime logs, databases, generated metrics, caches, archives, virtual
  environments, generated builds, and local secrets;
- product source code pending claim/proof and import review.

## Production Interpretation

This slice records that the products are real deployable candidates. Public
claim language remains gated until product claims are bound to paper/proof
receipts and validation evidence.
