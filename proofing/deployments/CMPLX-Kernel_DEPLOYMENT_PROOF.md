# CMPLX-Kernel Deployment Proof

## Identity

- Root: `CMPLX-Kernel`
- Local path: `D:\CMPLX-Kernel`
- Claimed role: deployable AI sidecar kernel.
- Production interpretation: file-fed, repo-clonable sidecar runtime plus full
  corpus package builder.

## Deployment Surfaces

- Runtime: `D:\CMPLX-Kernel\kernel`
- Services: none by default.
- Docker/K8s: none by default.
- MCP/API: future wrapper; current protocol is CLI/file/stdin/request JSON.
- File-fed/sidecar: primary deployment surface.
- Data/corpus: production archive
  `CMPLX-Kernel_Production_20260607T223706.tar.gz`

## Proof Artifacts

- `kernel/KERNEL_MANIFEST.json`
- `kernel/AI_LOAD_FIRST.md`
- `kernel/docs/SIDECAR_PROTOCOL.md`
- `PACKAGE_MANIFEST.csv` inside production package.
- `PORTABILITY_REVIEW.md` inside production package.
- `PRODUCTION_REPO_MAP.md`

## Adapter Boundary

- Binary Boundary Adapter: implemented in `kernel/cmplx_kernel/adapters.py`.
- Universal Adapter: implemented in `kernel/cmplx_kernel/adapters.py`.
- Network/API handshakes: not primary yet.
- Hidden Guess Result mode: quiet by default; enabled by `training_mode`;
  required by `--local-full-program`.

## Production Split

Reusable lib behavior:

- token sidecar runtime;
- boundary/adapters;
- kernel receipt schema;
- optional training diagnostics.

Product/source/corpus material:

- full production package archive;
- root deployment docs.

Excluded or airlocked:

- generated caches;
- corrupt zip removed;
- giant source corpus remains archive/provenance material, not direct git body.

## Risks

- Full archive is multi-GB and should not be committed directly to normal git.
- Runtime is new and stdlib-only but still needs broader host integration tests.

## Promotion Decision

State: `slice-ready`

First safe slice:

- `kernel/` runtime folder;
- root `README.md`, `DEPLOYMENT.md`, `PRODUCTION_REPO_MAP.md`;
- package manifest references, not the full tarball.

Required gates:

- keep guess mode quiet by default;
- add API/MCP wrapper only after Universal Adapter contract is preserved.

