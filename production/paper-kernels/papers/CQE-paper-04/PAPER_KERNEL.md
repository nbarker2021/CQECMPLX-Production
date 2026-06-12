# CQE-paper-04 - Boundary Repair Kernel

Block: `block-00-papers-01-08`

Role: `paper_body_work`

This paper is treated as body work under the Paper 00 operating contract.

Suite edges: `CQE-paper-03` -> `CQE-paper-04` -> `CQE-paper-05`

Block edges: `CQE-paper-03` -> `CQE-paper-04` -> `CQE-paper-05`

Central thesis: Define boundary repair as the transport operation that converts failed joins into typed constraints for the next legal route.

## Claims

Status: `seeded`

Define boundary repair as the transport operation that converts failed joins into typed constraints for the next legal route.

Polished claim: boundary repair converts Paper 02 correction residues plus Paper 03 coordinates into typed, idempotent constraints for the next legal route. A repaired row is a constraint, not proof; untyped failures are rejected.

Required next action: Connect this polished theorem to the installable cqe_engine formal interface and then route constraints into Paper 05 path carriers.

## Math

Status: `source-bound`

Use the paper body axioms, lemmas, and formalism as the math intake.

Required next action: Promote every symbolic statement into a normalized claim row with assumptions and receipts.

## Formal, Normal, Closed-Form Algebra and Calculus

Status: `source-bound`

Use `production/formal-papers/CQE-paper-04/FORMAL_PAPER.md`, `01-CQE-formal/FORMAL.md`, and recovered algebra/PDF evidence.

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

forgefactory.paper04_boundary_repair

Required next action: Resolve this binding into production/lib-forge or mark it as an adapter route.

## Tests and Receipts

Status: `seeded`

Every validation and diagnostic must support hidden-guess ablation when training mode is enabled. Paper 04 now includes `production/formal-papers/CQE-paper-04/boundary_repair_receipt.json`, which verifies typed constraints, idempotent repair, Paper 02/Paper 03 preservation, and rejection of untyped failures.

Required next action: Add positive, negative, boundary, and wrap tests with receipts.

## Deployment Kernel

Status: `seeded`

Deployable individually as CQE-paper-04 and selectable through the master suite.

Required next action: Expose paper, block, and suite selectors with no duplicate routing logic.

## Source Binding

- `body`: `production\papers\CQE-paper-04\PAPER-BODY.md` (present)
- `source`: `production\papers\CQE-paper-04\SOURCE.md` (present)
- `formal`: `production\papers\CQE-paper-04\01-CQE-formal\FORMAL.md` (present)
- `tool`: `production\papers\CQE-paper-04\02-CQE-tool\TOOL.md` (present)
- `tool_runner`: `production\papers\CQE-paper-04\02-CQE-tool\run.py` (present)
- `workbook`: `production\papers\CQE-paper-04\03-CQE-workbook\WORKBOOK.md` (present)
- `recovered_output`: `production\lib-forge\recovered\papers_output\CQE-paper-04.md` (present)
