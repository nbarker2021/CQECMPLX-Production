# CMPLX-Monorepo Deployment Proof

## Identity

- Root: `CMPLX-Monorepo`
- Canonical remote: `https://github.com/nbarker2021/CMPLX-Monorepo`
- Local path: `D:\g\CMPLX-Monorepo`
- Claimed role: public portal and installation guide for the L1-L10 stack.
- Production interpretation: high-priority portal/runtime/service orchestration
  source.

## Deployment Surfaces

- Runtime: `projects/CMPLXNEXT/`, `projects/QwenCoderWrapper/`,
  `projects/physics-lab/`
- Services: `services/`, `projects/CMPLXNEXT/service_registry.json`
- Docker/K8s: Qwen wrapper Docker and product infra compose files.
- MCP/API: CMPLXNEXT and Qwen API surfaces; submodule intent points to MCP repo.
- File-fed/sidecar: not primary; can connect through Universal Adapter.
- Data/corpus: `mmdb/*.json`, docs phase0 artifacts, CQE website monoliths.

## Proof Artifacts

- Review: `reviews/CMPLX-Monorepo_INTAKE_REVIEW.md`
- Promotion manifest: `promotions/CMPLX-Monorepo_FIRST_SLICE_MANIFEST.md`
- Source docs: `README.md`, `AGENTS.md`, `.gitmodules`, `.env.example`

## Adapter Boundary

- Binary Boundary Adapter: useful for file/corpus ingestion but not primary.
- Universal Adapter: required for API/service registration.
- Network/API handshakes: Qwen wrapper, MCP gateway/server, service registry.
- Hidden Guess Result mode: quiet by default; training mode only for diagnostic
  learning.

## Production Split

Reusable lib behavior:

- service registry/orchestration patterns;
- product infra code after focused review;
- Qwen wrapper interface after secret handling review.

Product/source/corpus material:

- portal docs;
- CMPLXNEXT project structure;
- selected service docs and tests.

Excluded or airlocked:

- `docs/inventory_raw.txt`
- large `mmdb/*.json` until ownership/use is clear.
- repeated `cqe_website/cqe_core_system*.py`.
- CQE website monolith/core duplicates until deduplicated.
- populated secret files.

## Risks

- `.gitmodules` declares submodules, but checkout did not show populated
  submodule directories.
- Placeholder/default credentials exist in docs/templates.
- CQE website source-of-truth is unclear due repeated monolith files.
- Tests not yet run.

## Promotion Decision

State: `slice-ready`

First safe slice:

- portal identity/navigation;
- CMPLXNEXT service/runtime contracts;
- Qwen wrapper after secret review;
- services/product infra after focused tests.

Required gates:

- submodule strategy decision;
- secret handling review;
- monolith deduplication;
- destination: `portal/cmplx-monorepo/`.

