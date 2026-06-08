# CMPLX-Monorepo First Slice Promotion Manifest

Source repo:

```text
https://github.com/nbarker2021/CMPLX-Monorepo
```

Local review clone:

```text
D:\g\CMPLX-Monorepo
```

Decision from intake review:

```text
High-priority portal/runtime candidate. Promote by explicit slices.
```

## Slice 1 Goal

Promote the production portal and service/runtime contract layer without
importing generated inventory dumps, MMDB data payloads, or duplicated CQE
website monoliths.

## Candidate Files

Root production identity:

- `README.md`
- `NAVIGATION.md`
- `AGENTS.md`
- `TODO.md`
- `CONTRIBUTING.md`
- `DISCLAIMER.md`
- `LICENSE.md`
- `NOTICE`
- `REUSE.toml`
- `.env.example`
- `.gitmodules`

Service/runtime contracts:

- `projects/CMPLXNEXT/README.md`
- `projects/CMPLXNEXT/service_registry.json`
- `projects/CMPLXNEXT/orchestrate.ps1`
- `projects/CMPLXNEXT/subprojects/**/pyproject.toml`
- `projects/CMPLXNEXT/subprojects/**/README.md`
- `services/**/requirements.txt`
- `product/infra/docker-compose.snap.yml`
- `product/infra/snap_schema.py`
- `product/infra/embedding_pipeline.py`

Qwen wrapper candidate:

- `projects/QwenCoderWrapper/README.md`
- `projects/QwenCoderWrapper/requirements.txt`
- `projects/QwenCoderWrapper/config.py`
- `projects/QwenCoderWrapper/src/`
- `projects/QwenCoderWrapper/docker/`
- `projects/QwenCoderWrapper/.env.example`

Docs:

- `docs/phase0/README.md`
- selected `docs/plans/`
- `plans/`

Tests:

- `tests/`

## Explicit Exclusions For Slice 1

Do not promote in the first slice:

- `docs/inventory_raw.txt`
- `docs/phase0/artifacts/catchall_code_index.jsonl`
- `mmdb/*.json`
- repeated `cqe_website/cqe_core_system*.py`
- `cqe_website/*MONOLITH*`
- duplicated `cqe_website/lattice*.py` files until source-of-truth is selected
- any populated secret file other than `.env.example`

## Required Gates Before Copy

- Confirm whether `.gitmodules` is active source-of-truth or historical intent.
- Ensure `.env.example` contains placeholders only.
- Deduplicate CQE website monolith/core files.
- Run focused tests for CMPLXNEXT/Qwen wrapper once dependencies are confirmed.
- Add adapter/receipt notes for any service promoted into production.

## Recommended Destination

```text
portal/cmplx-monorepo/
```

Runtime/service slices may later graduate from `portal/cmplx-monorepo/` into:

- `services/`
- `product/infra/`
- `shared-memory/service-registry/`
- `proof-receipts/runtime/`

