# CMPLX First Slice Promotion Manifest

Source repo:

```text
https://github.com/nbarker2021/CMPLX
```

Local review clone:

```text
D:\g\CMPLX
```

Decision from intake review:

```text
Core L1-L3 infrastructure candidate. Promote by explicit slices only.
```

## Slice 1 Goal

Promote the baseline MCP/gateway/Docker/deployment contract and selected core
package surfaces without importing vendored sibling repos or generated monoliths.

## Candidate Files

Root identity and operational docs:

- `README.md`
- `AGENTS.md`
- `CMPLX-LOCAL-SETUP-GUIDE.md`
- `DOCKER-CONNECTION-PROTOCOLS.md`
- `EXECUTIVE_SUMMARY.md`
- `ECOSYSTEM_ANALYSIS_REPORT.md`
- `CONTRIBUTING.md`
- `DISCLAIMER.md`
- `LICENSE.md`
- `NOTICE`
- `REUSE.toml`

Deployment contracts:

- `deployment/README.md`
- `deployment/DEPLOYMENT-GUIDE.md`
- `deployment/COMPLETE-DEPLOYMENT.md`
- `deployment/HANDSHAKE-INTEGRATION.md`
- `deployment/docker-compose.production.yml`
- `deployment/docker-compose.handshake.yml`
- `deployment/docker-compose.monitoring.yml`
- `deployment/.env.example`
- `docker-compose.yml`
- `docker-compose.gateway.yml`
- `docker-compose.unified.yml`
- `Dockerfile.mcp`
- `Dockerfile.mcp-gateway`
- `Dockerfile.production`

Core package candidates:

- `core/README.md`
- `core/pyproject.toml`
- `core/src/cmplx/adapters/`
- `core/src/cmplx/mcp/`
- `core/src/cmplx/security/`
- `core/src/cmplx/universal_access/`
- `core/src/cmplx/orchestration/`
- `core/src/cmplx/controllers/`

Tests and validation:

- `tests/`
- `run_tests.py`
- `cmplx_quick_tests.py`
- `pytest.ini`
- `tox.ini`
- `requirements-test.txt`

## Explicit Exclusions For Slice 1

Do not promote in the first slice:

- `cmplx_submodules/**`
- `src/cqe_models/models.py`
- `src/**/unified_cqe_part*.py`
- `core/src/cmplx/misc/models.py`
- `core/src/cmplx/misc/unified_cqe_part*.py`
- `reference/`
- database files
- any `.env` file other than examples
- generated caches or package metadata

## Required Gates Before Copy

- Credential/default secret review.
- Decide source-of-truth for `CMPLXUNI`, `CMPLXMCP`, and DevKit materials.
- Deduplicate generated monolith files.
- Run focused tests for core package and MCP surfaces.
- Replace placeholder project URLs in package metadata before publication.

## Recommended Destination

```text
core/cmplx-baseline/
```

MCP/gateway deployment material may later graduate into:

- `services/mcp/`
- `services/gateway/`
- `deployment/docker/`
- `proof-receipts/runtime/`

