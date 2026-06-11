# CQECMPLX-Payload-Ledger

Status: `trackable-ledger`

Route: `production/payload-ledger`

## Composite Identity

`CQECMPLX-Payload-Ledger` is the metadata-first route for binary payloads and
nested archives found across repo accounting.

## Known Payload Families

- CMPLX-1T training/document/simulation databases.
- MMDB SQLite databases.
- E8 database payloads.
- vector store databases.
- Manny memory and instruction databases.
- PartsFactory lattice-forge morphism ledger.
- nested archive candidates.

## Production Rule

Payload metadata may enter production before payload bodies.

Binary payloads may not enter production until:

1. database introspection is complete;
2. nested archive expansion is complete;
3. artifact storage policy is chosen;
4. source lineage remains exact;
5. no dedupe has contaminated literal accounting.

## Source Bindings

- `tracking/source-bindings/CQECMPLX-Payload-Ledger.json`
- `tracking/promotion-manifests/CQECMPLX-Payload-Ledger.manifest.json`
