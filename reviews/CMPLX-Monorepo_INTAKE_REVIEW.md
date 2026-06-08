# CMPLX-Monorepo Intake Review

Source repo:

```text
https://github.com/nbarker2021/CMPLX-Monorepo
```

Local clone:

```text
D:\g\CMPLX-Monorepo
```

Review branch created in source clone:

```text
intake/review-for-cqecmplx-production
```

## Repository State

- Current branch at intake: `main`
- Review branch created: `intake/review-for-cqecmplx-production`
- Head commit observed: `c56c785 feat: Add unified code from docker/unified - cqe_website`
- Clone path: short-path lane `D:\g`
- `core.longpaths=true`

## Inventory

- Files: `683`
- Directories: `141`
- Size including `.git`: about `88 MB`
- Dominant extensions:
  - `.py`: `495`
  - `.md`: `81`
  - `.toml`: `20`
  - `.json`: `17`

Largest notable files:

- `docs/inventory_raw.txt`: `28,898,630` bytes
- `mmdb/receipts_23k.json`: `7,588,831` bytes
- `mmdb/atoms_23k.json`: `5,608,531` bytes
- `docs/phase0/artifacts/catchall_code_index.jsonl`: `5,500,317` bytes
- repeated `cqe_website/cqe_core_system*.py`: about `3,138,817` bytes each
- `cqe_website/CQE_CORE_MONOLITH_fixed.py`: about `3,121,182` bytes

Top-level weight:

- `cqe_website`: `385` files, about `25 MB`
- `projects`: `150` files, about `193 KB`
- `docs`: `67` files, about `36 MB`
- `mmdb`: `6` files, about `13.6 MB`

## Identity Read

`CMPLX-Monorepo` presents itself as the public portal and installation guide for
the L1-L10 CMPLX stack. It is more production-shaped than `CMPLX-1T`: smaller,
more structured, and centered around services, project roots, orchestration,
and documentation.

Production interpretation:

- It should become a high-priority production intake source.
- It appears to encode service registry/runtime truth for CMPLXNEXT.
- It references submodules for CMPLX, DevKit, MCP, and UNI, but this checkout
  did not populate a `cmplx_submodules` directory and `git submodule status`
  returned no entries. Treat `.gitmodules` as intent that needs validation.

## Production-Candidate Slices

Promote after focused review:

- `README.md`, `NAVIGATION.md`, `AGENTS.md`, `TODO.md`
- `.env.example` as a template only, not secrets
- `.gitmodules` as intended cross-repo map
- `projects/CMPLXNEXT/`
- `projects/QwenCoderWrapper/`
- `projects/physics-lab/`
- `services/`
- `product/infra/`
- `scripts/`
- `tests/`
- selected `docs/phase0/` artifacts after size review

## Staged Or Airlock-Only Slices

Keep indexed and gated:

- `docs/inventory_raw.txt`
- `docs/phase0/artifacts/catchall_code_index.jsonl`
- `mmdb/*.json` until ownership and runtime use are confirmed
- repeated `cqe_website/cqe_core_system*.py` copies
- `cqe_website/*monolith*` files until deduplicated or source-of-truth chosen
- any generated website/runtime files that duplicate CMPLX-1T `docker/unified`

## Risks Before Promotion

1. `.gitmodules` and README describe submodules, but the checkout does not show
   populated submodule directories. Production needs a confirmed submodule
   strategy.
2. `.env.example` and docs include placeholder/default credentials. These are
   acceptable as templates only; production deployment must require environment
   injection.
3. `cqe_website` has repeated large monolith/core files. Choose one source of
   truth before promotion.
4. `mmdb` JSON files are sizable runtime/corpus assets. Treat them as data
   artifacts unless code requires them directly.
5. Test execution was not attempted during intake; review is structural.

## Production Decision

`CMPLX-Monorepo` is a stronger near-term production candidate than `CMPLX-1T`
for portal/service/runtime structure.

Do not merge wholesale yet. Promote:

- repo identity and navigation;
- CMPLXNEXT service/runtime contracts;
- Qwen wrapper only after secret handling review;
- services/product infra after tests and dependency checks;
- docs only after excluding generated raw inventories.

## Next Actions

1. Build a first-slice promotion manifest for `CMPLX-Monorepo`.
2. Validate whether submodules should be active git submodules or explicit
   sibling repos in production.
3. Deduplicate `cqe_website` monolith/core files.
4. Run focused tests for `projects/CMPLXNEXT` and `projects/QwenCoderWrapper`
   after dependency inspection.

