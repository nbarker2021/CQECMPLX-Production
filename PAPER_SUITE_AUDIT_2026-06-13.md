# CQECMPLX Paper Suite Audit - 2026-06-13

This audit records the production state after the proof-first rewrite pass through
Paper 32. It separates paper evidence from supplemental tooling, and it keeps
package obligations visible without promoting them as closed proof.

## Current Production State

- Review PDFs: 132 files checked from `Papers/PDF/review_pdf_manifest.json`.
- PDF openability check: 132 checked, 0 failures.
- Formal paper directories: 32 directories for `CQE-paper-01` through
  `CQE-paper-32`.
- Formal verifier coverage: every `CQE-paper-01` through `CQE-paper-32`
  directory has at least one `verify*.py` script and at least one receipt JSON.
- Foreword/contract set: `CQE-paper-00`, `00.25`, `00.50`, and `00.75` exist
  as `Papers/Source` markdown and review PDFs. Paper 00 is the burden/contract
  preface, not one of the 32 proof-bearing formal paper directories.
- Companion coverage: all tracked intervals have `.25`, `.50`, and `.75`
  companion drafts built into the review PDF manifest.

## Recent Proof-First Commits

- `d5af062` - Paper 29, Monster horizon package.
- `58cb1ba` - Paper 30, Grand Ribbon meta-framer package.
- `87bfcea` - Paper 31, Meta LCR readout package.
- `8b4d781` - Paper 32, Supervisor Cursor package.

## Paper 29-32 Findings

Paper 29 proves only the finite and receipt-bound Monster/VOA adjacency facts it
can verify: `47 * 59 * 71 = 196883`, `196884 = 1 + 196883`,
`Z(q) = 2q^0 + 6q^5`, and the local centroid-chain profile with two fixed
points and six period-4 states. Physical energy, universal energy ceiling, and
Pariah boundary claims are quarantined hypotheses.

Paper 30 packages the suite as an eight-slot ribbon schema:
`C, L, R, B, T, O, W, A`. It verifies the 30-position sweep through
`CQE-paper-00` to `CQE-paper-29`, the terminal route `Niemeier:A2^12`, and the
transport-obligation ledger. It also records that the reusable ribbon code
exists in nearby kernel/lib copies and should be promoted into the tracked
production root rather than silently assumed.

Paper 31 is a retrospective LCR readout, not an upstream dependency. It verifies
the gluon/LCR invariant, the Rule 30 truth table with ANF
`L xor C xor R xor (C and R)`, and the Paper 30 receipt link. It preserves Paper
32 as the forward package/deployment target.

Paper 32 is the supervisor cursor. It verifies PermForge coverage records for
`n = 4..8`, claims minimality only where established for `n = 4` and `n = 5`,
records `n = 8` with length `46205`, keeps the `120`-unit open corridor to the
lower bound visible, and wraps the suite selector from Paper 32 back to Paper 01.
Cursor success is schedule coverage, not proof of the selected item.

## Source Mirror Gap

`Papers/Source` currently has 124 markdown files. The review PDF set has 132
PDFs because Papers 25-32 use `production/formal-papers/*/FORMAL_PAPER.md` as
their main body source while their `.25`, `.50`, and `.75` companions live in
`Papers/Source`.

Missing main-source mirrors:

- `Papers/Source/CQE-paper-25.md`
- `Papers/Source/CQE-paper-26.md`
- `Papers/Source/CQE-paper-27.md`
- `Papers/Source/CQE-paper-28.md`
- `Papers/Source/CQE-paper-29.md`
- `Papers/Source/CQE-paper-30.md`
- `Papers/Source/CQE-paper-31.md`
- `Papers/Source/CQE-paper-32.md`

This is an organization gap, not a proof gap. The formal bodies, receipts, and
PDFs exist. The next cleanup pass should mirror these formal bodies into
`Papers/Source` or update the repository convention so formal main bodies are
declared canonical.

## Package And Lib Promotion Obligations

The installable surface is split between:

- `production/packages/cqekernel`: kernel, adapters, binary boundary carrier,
  ribbon modules, ledger, verification, workbook, storage, and firmware bridges.
- `production/packages/cqecmplx-forge`: LatticeForge, GraphStax/PermForge,
  PixelForge, FridgeForge, ChromaForge, SceneForge, Rhenium, ReForge contracts,
  and related Forge engines.
- `production/lib-forge`: curated engine mirrors, recovered summary papers,
  recovered scripts, and product sources such as the metamaterial designer.

Known promotion items:

- Promote a stable formal-paper verifier interface so standalone
  `production/formal-papers/CQE-paper-*/verify*.py` scripts can be invoked
  through the kernel/API.
- Reconcile the ribbon implementation noted by Paper 30 with the tracked
  `cqekernel.ribbon` package and any nearby `cqe_engine.ribbon` copies.
- Decide whether Papers 25-32 main bodies should be mirrored into
  `Papers/Source` or whether `production/formal-papers/*/FORMAL_PAPER.md`
  remains the canonical main-body source.
- Preserve hidden guess/honesty mode as a validation layer, with mandatory use
  only when kernel training mode is enabled.
- Keep Cursor/SuperPerm scheduling separate from proof receipts: Paper 32 may
  route work, but the selected paper/package/product must still expose its own
  receipt and obligation status.
- Integrate the Forge registry with the paper receipt map so each named Forge
  can be traced from paper claim to package module to verifier command.

## Do Not Overclaim

The current production package should not claim that every open scientific,
physical, biological, CAD, game, market, or deployment interpretation is closed.
It should claim the verified formal rows, finite receipts, exact package
registrations, and explicitly named hypothesis corridors. That distinction is
the strength of the suite: proof rows become stronger when obligation rows are
kept visible.
