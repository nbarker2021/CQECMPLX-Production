# CQE-paper-01 - LCR Chain Carrier Kernel

Block: `block-00-papers-01-08`

Role: `paper_body_work`

This paper is treated as body work under the Paper 00 operating contract.

Suite edges: `CQE-paper-32` -> `CQE-paper-01` -> `CQE-paper-02`

Block edges: `CQE-paper-08` -> `CQE-paper-01` -> `CQE-paper-02`

Central thesis: Formalize Left-Center-Right readout as the smallest chain carrier that preserves a center while allowing two opposed boundary directions.

## Claims

Status: `seeded`

Formalize Left-Center-Right readout as the smallest chain carrier that preserves a center while allowing two opposed boundary directions.

Polished claim: LCR is the minimal ordered carrier preserving one center and two addressable boundary directions. Directional opposition is structural; boundary-value inequality is not guaranteed.

Required next action: Connect this polished theorem to the installable cqe_engine formal interface.

## Math

Status: `source-bound`

Use the paper body axioms, lemmas, and formalism as the math intake.

Required next action: Promote every symbolic statement into a normalized claim row with assumptions and receipts.

## Formal, Normal, Closed-Form Algebra and Calculus

Status: `source-bound`

Use `production/formal-papers/CQE-paper-01/FORMAL_PAPER.md`, `01-CQE-formal/FORMAL.md`, and recovered algebra/PDF evidence.

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

forgefactory.paper01_lcr_chain_carrier

Required next action: Resolve this binding into production/lib-forge or mark it as an adapter route.

## Tests and Receipts

Status: `seeded`

Every validation and diagnostic must support hidden-guess ablation when training mode is enabled. Paper 01 now includes `production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json`, which verifies the finite carrier claims and rejects the false shell-2 value-inequality overclaim.

Required next action: Add positive, negative, boundary, and wrap tests with receipts.

## Deployment Kernel

Status: `seeded`

Deployable individually as CQE-paper-01 and selectable through the master suite.

Required next action: Expose paper, block, and suite selectors with no duplicate routing logic.

## Source Binding

- `body`: `production\papers\CQE-paper-01\PAPER-BODY.md` (present)
- `source`: `production\papers\CQE-paper-01\SOURCE.md` (present)
- `formal`: `production\papers\CQE-paper-01\01-CQE-formal\FORMAL.md` (present)
- `tool`: `production\papers\CQE-paper-01\02-CQE-tool\TOOL.md` (present)
- `tool_runner`: `production\papers\CQE-paper-01\02-CQE-tool\run.py` (present)
- `workbook`: `production\papers\CQE-paper-01\03-CQE-workbook\WORKBOOK.md` (present)
- `recovered_output`: `production\lib-forge\recovered\papers_output\CQE-paper-01.md` (present)
