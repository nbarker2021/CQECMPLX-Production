# CQE-paper-02 - Correction Surface Kernel

Block: `block-00-papers-01-08`

Role: `paper_body_work`

This paper is treated as body work under the Paper 00 operating contract.

Suite edges: `CQE-paper-01` -> `CQE-paper-02` -> `CQE-paper-03`

Block edges: `CQE-paper-01` -> `CQE-paper-02` -> `CQE-paper-03`

Central thesis: Treat failure, mismatch, and nonlinear residue as positive correction data rather than dismissal.

## Claims

Status: `seeded`

Treat failure, mismatch, and nonlinear residue as positive correction data rather than dismissal.

Polished claim: the correction surface is the typed residue map `corr(L,C,R) = C and not R`, and for the Rule 30 / Rule 90 split it fires exactly on `(0,1,0)` and `(1,1,0)`. A correction is positive data only when recorded as a replayable obligation, not when promoted directly to proof.

Required next action: Connect this polished theorem to the installable cqe_engine formal interface.

## Math

Status: `source-bound`

Use the paper body axioms, lemmas, and formalism as the math intake.

Required next action: Promote every symbolic statement into a normalized claim row with assumptions and receipts.

## Formal, Normal, Closed-Form Algebra and Calculus

Status: `source-bound`

Use `production/formal-papers/CQE-paper-02/FORMAL_PAPER.md`, `01-CQE-formal/FORMAL.md`, and recovered algebra/PDF evidence.

Required next action: Split normal form, closed form, algebraic operators, calculus/window operators, and open obligations.

## By-Hand Reconstruction

Status: `source-bound`

Use 03-CQE-workbook/WORKBOOK.md plus the analog toolkit guides.

Required next action: Write the physical reconstruction steps and boundary-collision handling for the paper.

## Code Rebuild

Status: `source-bound`

Use 02-CQE-tool/TOOL.md and run.py when present.

Required next action: Bind a replayable command or mark the missing executable as an obligation.

## Installable Lib Bindings

Status: `seeded`

forgefactory.paper02_correction_surface

Required next action: Resolve this binding into production/lib-forge or mark it as an adapter route.

## Tests and Receipts

Status: `seeded`

Every validation and diagnostic must support hidden-guess ablation when training mode is enabled. Paper 02 now includes `production/formal-papers/CQE-paper-02/correction_surface_receipt.json`, which verifies the finite correction identity, exact firing set, D4 projection, and obligation rule.

Required next action: Add positive, negative, boundary, and wrap tests with receipts.

## Deployment Kernel

Status: `seeded`

Deployable individually as CQE-paper-02 and selectable through the master suite.

Required next action: Expose paper, block, and suite selectors with no duplicate routing logic.

## Source Binding

- `body`: `production\papers\CQE-paper-02\PAPER-BODY.md` (present)
- `source`: `production\papers\CQE-paper-02\SOURCE.md` (present)
- `formal`: `production\papers\CQE-paper-02\01-CQE-formal\FORMAL.md` (present)
- `tool`: `production\papers\CQE-paper-02\02-CQE-tool\TOOL.md` (present)
- `tool_runner`: `production\papers\CQE-paper-02\02-CQE-tool\run.py` (present)
- `workbook`: `production\papers\CQE-paper-02\03-CQE-workbook\WORKBOOK.md` (present)
- `recovered_output`: `production\lib-forge\recovered\papers_output\CQE-paper-02.md` (present)
