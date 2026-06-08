# CMPLX-1T First Slice Promotion Manifest

Source repo:

```text
https://github.com/nbarker2021/CMPLX-1T
```

Local review clone:

```text
D:\g\CMPLX-1T
```

Decision from intake review:

```text
Promote by explicit slices. Do not merge wholesale.
```

## Slice 1 Goal

Bring over the smallest production-useful layer from `CMPLX-1T`: identity,
navigation, architecture, agent guidance, and the compact runtime/source
candidates needed to understand the showroom without importing the full staged
corpus.

## Candidate Files

Identity and navigation:

- `README.md`
- `NAVIGATION.md`
- `AGENTS.md`
- `INDEX-V5.md`
- `QUICKSTART-V5.md`
- `CONTRIBUTING.md`
- `DISCLAIMER.md`
- `LICENSE.md`
- `NOTICE`
- `REUSE.toml`

Architecture:

- `ARCHITECTURE-V5.md`
- `README-DOCKER.md`
- `REORGANIZATION_PLAN.md`
- `docker-compose.master.yml`
- `docker-compose.task-template.yml`
- `Dockerfile`
- `Dockerfile.polyglot`
- `k8s-deployment.yaml`

Source/runtime candidates:

- `src/`
- `scripts/`
- `pipeline/`
- `intake-system/`
- `toolkit/`
- `cmplx-1t-hook/`

Showroom and product-facing docs:

- `SHOWROOM/`
- `reports/`
- `security-reports/`
- `plans/`
- `TODO/README.md`
- `TODO/completed/README.md`

## Explicit Exclusions For Slice 1

Do not promote in the first slice:

- `docs/3_staged/**`
- `docs/1_intake/inventory_raw.txt`
- `docs/directory_manifest*.csv`
- `docs/tree_dump.txt`
- `data/*.db`
- `Wolfram study/*.tar.gz`
- giant generated files under `docker/unified/**`
- copied legacy family builds under `docs/3_staged/family_exemplar_starters/**`
- archives, generated checkpoints, and bundled release payloads

## Required Gates Before Copy

- Long-path note added to production docs.
- Docker/default credential review.
- Manifest of exact copied files generated.
- Hidden Guess Result remains optional by default; training mode required for
  diagnostic-learning runs.
- Destination path chosen inside `CQECMPLX-Production` before copying.

## Recommended Destination

```text
showroom/cmplx-1t/
```

Keep source/runtime candidates grouped under that destination until CQE decides
which pieces become shared lib, proof receipts, service runtime, or papers.

