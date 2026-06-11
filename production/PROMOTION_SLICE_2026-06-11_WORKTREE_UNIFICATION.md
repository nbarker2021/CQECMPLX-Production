# Promotion Slice: Worktree Unification

Date: 2026-06-11

Agent worktrees written to WSL-converted relative paths (`c/`, `d/` literal
directories on C: and D:) are reconciled into the canonical roots and the
resulting unified work is promoted here as one line.

Source binding:

```text
tracking/source-bindings/CQECMPLX-Worktree-Unification.json
```

Promotion manifest:

```text
tracking/promotion-manifests/CQECMPLX-Worktree-Unification.manifest.json
```

## Reconciliation (strays -> canonical, no-clobber)

| Stray root | Recovered | Already merged | Superseded by canonical |
|---|---|---|---|
| `D:\d\CQE_CMPLX\CQECMPLX-Production` | +6 recovered | 58 identical | 6 superseded |
| `C:\d\CQE_CMPLX\CQECMPLX-Production` | +3 recovered | 1 identical | 1 superseded |
| `C:\d\CQECMPLX-Production` | +1 recovered | 0 identical | 3 superseded |
| `C:\d\CQECMPLX-ProofValidatedSuite` | +1 recovered | 0 identical | 0 superseded |
| `D:\CQECMPLX-ProofValidatedSuite` | +20 recovered | 1 identical | 0 superseded |
| `D:\CQE_CMPLX\d\CQECMPLX-ProofValidatedSuite` | +1 recovered | 0 identical | 4 superseded |

Full file-level evidence: `tracking/worktree-unification/reconcile_report.json`.

## Promoted

- `production/lib-forge/engines/` — ChromaForge, GraphStax, PixelForge,
  FridgeForge, LinkForge (the ChromaBlend Studio engine ring; Event Law:
  compute -> save -> validate -> receipt(2 links) -> reuse)
- `production/lib-forge/recovered/` — MASTER_PDF (4 master PDFs), summary
  papers I-X, papers_output set, forgefactory_analog_workbench, build /
  bilateral / dna_construction_kit scripts, FINAL_FORMAL_PAPER.md
- `production/products/PaneForge-Stick/` — the self-contained calendar +
  FridgeForge product payload (83/83 tests, runs from any path)
- `production/operations/ProofKernel-Deploy/` — proof-suite kernel +
  deployment kit (docker/WSL/native paths, opencode integration)

## Counts

- Files promoted: 295
- Strays recovered into canonical: 32
- Stray files confirmed already merged: 60
- Collisions (canonical kept, stray recorded): 14

## Post-conditions

- The stray roots are now safe to archive/delete; nothing unique remains
  outside the canonical roots and this repo.
- `D:\CQECMPLX-Production` (root) is an empty husk — nothing recovered.
