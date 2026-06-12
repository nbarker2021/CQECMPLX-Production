# CQE-paper-07 - Discrete-Continuous Bridge Kernel

Block: `block-00-papers-01-08`

Role: `paper_body_work`

This paper is treated as body work under the Paper 00 operating contract.

Suite edges: `CQE-paper-06` -> `CQE-paper-07` -> `CQE-paper-08`

Block edges: `CQE-paper-06` -> `CQE-paper-07` -> `CQE-paper-08`

Central thesis: Define the bridge where discrete state changes approximate continuous dynamics through indexed windows.

## Claims

Status: `polished`

Polished claim: a discrete indexed trace can be embedded into a continuous
piecewise-linear bridge that preserves every sample exactly. This proves sample
preservation, not between-sample physical dynamics.

Required next action: Connect this polished theorem to cqe_engine.formal and add
separate theorems for any claimed Hamiltonian or physical dynamics between
samples.

## Math

Status: `polished`

Use the paper body axioms, lemmas, and formalism as the math intake.

Required next action: Promote every symbolic statement into a normalized claim row with assumptions and receipts.

## Formal, Normal, Closed-Form Algebra and Calculus

Status: `source-bound`

Use `production/formal-papers/CQE-paper-07/FORMAL_PAPER.md`,
`01-CQE-formal/FORMAL.md`, and recovered algebra/PDF evidence.

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

Status: `verified`

forgefactory.paper07_discrete_continuous_bridge

Required next action: Resolve this binding into production/lib-forge or mark it as an adapter route.

## Tests and Receipts

Status: `seeded`

Every validation and diagnostic must support hidden-guess ablation when training mode is enabled.

Paper 07 now includes
`production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json`,
which verifies exact indexed sample preservation, adjacent endpoint agreement,
the Rule 30 / Rule 90 correction identity, and the rejection of the
between-sample physics overclaim.

Required next action: Add broader positive, negative, boundary, and wrap tests
when later papers claim more than sample preservation.

## Deployment Kernel

Status: `seeded`

Deployable individually as CQE-paper-07 and selectable through the master suite.

Required next action: Expose paper, block, and suite selectors with no duplicate routing logic.

## Source Binding

- `body`: `production\papers\CQE-paper-07\PAPER-BODY.md` (present)
- `source`: `production\papers\CQE-paper-07\SOURCE.md` (present)
- `formal`: `production\papers\CQE-paper-07\01-CQE-formal\FORMAL.md` (present)
- `tool`: `production\papers\CQE-paper-07\02-CQE-tool\TOOL.md` (present)
- `tool_runner`: `production\papers\CQE-paper-07\02-CQE-tool\run.py` (missing)
- `workbook`: `production\papers\CQE-paper-07\03-CQE-workbook\WORKBOOK.md` (present)
- `recovered_output`: `production\lib-forge\recovered\papers_output\CQE-paper-07.md` (present)
