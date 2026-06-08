# CMPLX Intake Review

Source repo:

```text
https://github.com/nbarker2021/CMPLX
```

Local clone:

```text
D:\g\CMPLX
```

Review branch created in source clone:

```text
intake/review-for-cqecmplx-production
```

## Repository State

- Current branch at intake: `main`
- Review branch created: `intake/review-for-cqecmplx-production`
- Head commit observed: `51ff9c2 Stop tracking Python cache artifacts`
- Clone path: short-path lane `D:\g`
- `core.longpaths=true`

## Inventory

- Files: `12,927`
- Directories: `318`
- Size including `.git`: about `1.04 GB`
- Dominant extensions:
  - `.py`: `12,348`
  - `.md`: `259`
  - `.json`: `56`
  - `.yml`: `29`
  - `.ts`: `28`

Largest notable files are repeated generated/runtime Python bundles:

- `cmplx_submodules/CMPLXUNI/src/cmplx/misc/models.py`: about `30.8 MB`
- `cmplx_submodules/CMPLX/core/src/cmplx/misc/models.py`: about `30.8 MB`
- `src/cqe_models/models.py`: about `30.8 MB`
- `core/src/cmplx/misc/models.py`: about `30.8 MB`
- repeated `unified_cqe_part1.py` and `unified_cqe_part2.py` copies around
  `26-28 MB`

Top-level weight:

- `cmplx_submodules`: `6,119` files, about `570 MB`
- `src`: `3,434` files, about `113 MB`
- `core`: `2,876` files, about `281 MB`
- `reference`: `327` files, about `24 MB`
- `deployment`: `29` files, about `161 KB`
- `tests`: `14` files, about `80 KB`

## Identity Read

`CMPLX` presents itself as the public open-source baseline for L1-L3:

- MCP infrastructure;
- Docker orchestration;
- gateway;
- Redis/Postgres/MMDB integration;
- local setup;
- core `cmplx` package;
- test harness.

Production interpretation:

- It is a core infrastructure/runtime candidate.
- It is more operational than `CMPLX-1T`.
- It overlaps heavily with `CMPLX-Monorepo` and contains embedded submodule
  copies of CMPLX, CMPLXUNI, CMPLXMCP, and DevKit-like materials.

## Production-Candidate Slices

Promote after focused review:

- `README.md`, `AGENTS.md`, `CMPLX-LOCAL-SETUP-GUIDE.md`
- `DOCKER-CONNECTION-PROTOCOLS.md`
- `deployment/`
- `docker-compose*.yml`
- `Dockerfile.*`
- `core/README.md`
- `core/pyproject.toml`
- `core/src/cmplx/adapters/`
- `core/src/cmplx/mcp/`
- `core/src/cmplx/security/`
- `core/src/cmplx/universal_access/`
- `core/src/cmplx/orchestration/`
- `tests/`
- `run_tests.py`, `cmplx_quick_tests.py`

## Staged Or Airlock-Only Slices

Keep indexed and gated:

- `cmplx_submodules/**` until source-of-truth is resolved.
- repeated `models.py`, `unified_cqe_part1.py`, `unified_cqe_part2.py`.
- `src/*` generated unified-family bundles until deduplicated.
- `.env.example` and deployment env examples until credential review.
- `reference/` until provenance is assigned.
- database files.

## Risks Before Promotion

1. Default/demo credentials appear in docs/config examples, including gateway
   API keys, Postgres passwords, Grafana defaults, and sample bearer tokens.
2. Multiple nested copies of sibling repos exist under `cmplx_submodules`.
   Production must decide whether those are vendored snapshots, historical
   references, or should be replaced by sibling repo links.
3. Large generated Python monoliths duplicate across `src`, `core`, and
   `cmplx_submodules`.
4. The package metadata still uses placeholder project URLs such as
   `github.com/yourusername/cmplx`.
5. Tests were inventoried but not run during intake.

## Production Decision

Do not merge `CMPLX` wholesale.

Use it as the core L1-L3 infrastructure source for:

- MCP server/gateway contracts;
- Docker and deployment guides;
- core package adapter/security/orchestration code;
- test harness.

Promote by explicit slices only after credential review and duplicate-source
resolution.

## Next Actions

1. Build `CMPLX` first-slice promotion manifest.
2. Compare `core/src/cmplx` against `CMPLXUNI` and `CMPLXMCP` once those repos
   are reviewed.
3. Run focused tests after dependency inspection.
4. Add credential-hardening gate for all Docker/MCP deployment slices.

