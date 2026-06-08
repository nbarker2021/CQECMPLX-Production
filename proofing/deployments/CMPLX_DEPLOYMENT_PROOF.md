# CMPLX Deployment Proof

## Identity

- Root: `CMPLX`
- Canonical remote: `https://github.com/nbarker2021/CMPLX`
- Local path: `D:\g\CMPLX`
- Claimed role: CMPLX baseline, L1-L3 infrastructure, MCP/Docker/DevKit layer.
- Production interpretation: core infrastructure/runtime candidate, but not a
  wholesale merge candidate due vendored sibling repos and generated monoliths.

## Deployment Surfaces

- Runtime: `core/src/cmplx`, `src/*` generated/runtime bundles.
- Services: MCP server, MCP gateway, Redis/Postgres/MMDB integration.
- Docker/K8s: root compose files, deployment compose files, Dockerfiles,
  Kubernetes templates.
- MCP/API: primary surface; ports 8900/8901 in docs.
- File-fed/sidecar: not primary; can integrate through Universal Adapter.
- Data/corpus: possible DBs and generated reference/source bundles.

## Proof Artifacts

- Review: `reviews/CMPLX_INTAKE_REVIEW.md`
- Promotion manifest: `promotions/CMPLX_FIRST_SLICE_MANIFEST.md`
- Source docs: `README.md`, `AGENTS.md`, deployment guides, pyproject.
- Tests: `tests/`, `run_tests.py`, `cmplx_quick_tests.py`

## Adapter Boundary

- Binary Boundary Adapter: needed for file/data ingress.
- Universal Adapter: required for MCP/gateway host handshakes.
- Network/API handshakes: MCP server, gateway, Postgres, Redis, Grafana.
- Hidden Guess Result mode: quiet by default; training mode only for diagnostic
  learning.

## Production Split

Reusable lib behavior:

- core adapters;
- MCP/gateway contracts;
- security/orchestration modules;
- tests/harnesses.

Product/source/corpus material:

- setup/deployment docs;
- Docker and K8s specs;
- local setup guides.

Excluded or airlocked:

- `cmplx_submodules/**` until source-of-truth is decided.
- repeated generated `models.py` and `unified_cqe_part*.py` files.
- `reference/` until provenance is assigned.
- DB files and env files.

## Risks

- Default/demo credentials appear in docs and compose examples.
- Sibling repos are vendored/nested, creating source-of-truth ambiguity.
- Large generated Python bundles duplicate across directories.
- Package metadata includes placeholder URLs.
- Tests not yet run.

## Promotion Decision

State: `slice-ready`

First safe slice:

- root operational docs;
- deployment contracts after credential review;
- selected `core/src/cmplx` adapter/MCP/security/orchestration surfaces;
- tests.

Required gates:

- credential review;
- duplicate-source decision;
- focused test run;
- destination: `core/cmplx-baseline/`.
