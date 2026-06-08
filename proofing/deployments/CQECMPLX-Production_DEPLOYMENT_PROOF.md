# CQECMPLX-Production Deployment Proof

## Identity

- Root: `CQECMPLX-Production`
- Canonical remote: `https://github.com/nbarker2021/CQECMPLX-Production`
- Local reviewed clone: `D:\CQE_CMPLX\git-hosted-roots\CQECMPLX-Production`
- Existing local production body: `D:\CQECMPLX-Production`
- Claimed role: canonical production repo.
- Production interpretation: clean proof-backed assembly body for the full
  CQE/CMPLX family.

## Deployment Surfaces

- Runtime: none yet in repo root; runtime arrives through approved slices.
- Services: staged through future promotion.
- Docker/K8s: staged through future promotion.
- MCP/API: staged through future promotion.
- File-fed/sidecar: CMPLX-Kernel runtime candidate.
- Data/corpus: referenced by proof docs, not blindly committed.

## Proof Artifacts

- `README.md`
- `PRODUCTION_REPO_MAP.md`
- `INTAKE_REGISTRY.json`
- `INTAKE_REVIEW.md`
- `reviews/*.md`
- `promotions/*.md`
- `proofing/DEPLOYMENT_PROOF_INDEX.md`

## Adapter Boundary

- Binary Boundary Adapter: required for sidecar/kernel/file-fed runtime slices.
- Universal Adapter: required for host/tool handshakes.
- Network/API handshakes: must be named by each promoted service.
- Hidden Guess Result mode: quiet by default; enabled by `training_mode`.

## Production Split

Reusable lib behavior:

- Not yet promoted.

Product/source/corpus material:

- Admitted only by exact promotion manifests.

Excluded or airlocked:

- Raw workspaces.
- Giant generated corpus files.
- Archives and databases unless explicitly routed to release/LFS/corpus storage.

## Risks

- Empty canonical repo can become a dumping ground if promotion gates are not
  enforced.
- Multiple local roots have overlapping identities and duplicated runtime code.

## Promotion Decision

State: `production-shaped`

First safe slice:

- proofing spine;
- repo map;
- intake registry;
- deployment proof docs.

Required gates:

- Every incoming root must receive a deployment proof.
- Every promoted slice must have a manifest and portability review.

