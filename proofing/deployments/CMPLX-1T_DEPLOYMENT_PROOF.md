# CMPLX-1T Deployment Proof

## Identity

- Root: `CMPLX-1T`
- Canonical remote: `https://github.com/nbarker2021/CMPLX-1T`
- Local path: `D:\g\CMPLX-1T`
- Claimed role: flagship showroom/display floor.
- Production interpretation: identity, architecture, showroom, source-candidate,
  and corpus index. Not a wholesale production merge candidate.

## Deployment Surfaces

- Runtime: `src/`, `scripts/`, `pipeline/`, `intake-system/`, `toolkit/`
- Services: Docker compose service families and controller/task architecture.
- Docker/K8s: `docker-compose.master.yml`, `docker-compose.task-template.yml`,
  `Dockerfile`, `Dockerfile.polyglot`, `k8s-deployment.yaml`
- MCP/API: described in docs; related MCP roots should be reviewed separately.
- File-fed/sidecar: indirect, through kernel and intake systems.
- Data/corpus: huge staged corpus under `docs/`, generated manifests, DBs,
  archives, legacy family builds.

## Proof Artifacts

- Review: `reviews/CMPLX-1T_INTAKE_REVIEW.md`
- Promotion manifest: `promotions/CMPLX-1T_FIRST_SLICE_MANIFEST.md`
- Source docs: `README.md`, `AGENTS.md`, `ARCHITECTURE-V5.md`, `NAVIGATION.md`

## Adapter Boundary

- Binary Boundary Adapter: needed if any runtime slice becomes a sidecar/file
  interface.
- Universal Adapter: needed for AI-agent integration surfaces.
- Network/API handshakes: Docker/MCP surfaces must declare ports and credentials.
- Hidden Guess Result mode: optional by default; required only in training/local
  diagnostic mode.

## Production Split

Reusable lib behavior:

- `src/` engine candidates.
- controller/decomposer/agent modules after focused review.

Product/source/corpus material:

- `SHOWROOM/`
- reports/security-reports/plans.
- architecture and navigation docs.

Excluded or airlocked:

- `docs/3_staged/**`
- generated directory manifests/tree dumps.
- `data/*.db`
- archives and tarballs.
- giant generated files under `docker/unified/**`.
- deep legacy family exemplar builds.

## Risks

- Deep Windows paths break normal checkout unless short clone path and long paths
  are enabled.
- Default credentials appear in Docker/docs.
- Huge generated files and copied legacy corpora blur source-of-truth.
- Test execution not yet performed.

## Promotion Decision

State: `slice-ready`

First safe slice:

- identity/navigation/architecture;
- source/runtime candidates;
- showroom/report docs;
- Docker/runtime contracts after credential review.

Required gates:

- long-path production note;
- credential review;
- exact file manifest;
- destination: `showroom/cmplx-1t/`.

