# Block 01 Dyad Brief - Papers 04 and 05

Source: Dyad Agent D, read-only synthesis. No files edited by the agent.

## Repository State

Top-level `Papers/Source` only contains Paper 0/quarter papers and Paper 1/quarter papers. Papers 4 and 5 are still being generated from lower production sources/PDFs, so the main agent should create new top-level:

- `Papers/Source/CQE-paper-04.md`
- `Papers/Source/CQE-paper-04.25.md`
- `Papers/Source/CQE-paper-04.50.md`
- `Papers/Source/CQE-paper-04.75.md`
- `Papers/Source/CQE-paper-05.md`
- `Papers/Source/CQE-paper-05.25.md`
- `Papers/Source/CQE-paper-05.50.md`
- `Papers/Source/CQE-paper-05.75.md`

## Paper 04 - Boundary Repair

Final scientific claim focus:

Paper 4 should prove that a failed join/correction residue is not discarded and not promoted directly to proof. It becomes a typed, idempotent, replayable boundary constraint. The strict theorem already promoted is:

```text
T_BOUNDARY_REPAIR: failed joins become typed constraints for the next legal route.
```

The clean formal version should center on:

```text
Paper 02 correction residue + Paper 03 coordinate
-> typed boundary repair constraint
-> legal intake for Paper 05 path carrier
```

Verified finite form:

```text
Correction states:
(0,1,0) -> axis/sheet (2,0)
(1,1,0) -> axis/sheet (3,1)

Required repair fields:
state
axis_sheet
reason
status
next_legal_routes
source_paper
target_paper
```

Important polish:

Do not let the integer paper become a workbook/toolkit essay. The integer paper should prove the boundary repair operation. The analog circle-strip, tokens, "draw red X," and human sheet protocols belong in `.25/.50/.75`.

Proof/evidence files:

- `production/formal-papers/CQE-paper-04/FORMAL_PAPER.md`
- `production/formal-papers/CQE-paper-04/verify_boundary_repair.py`
- `production/formal-papers/CQE-paper-04/boundary_repair_receipt.json`
- `production/papers/CQE-paper-04/SOURCE.md`
- `production/papers/CQE-paper-04/01-CQE-formal/FORMAL.md`
- `production/papers/CQE-paper-04/02-CQE-tool/TOOL.md`
- `production/papers/CQE-paper-04/03-CQE-workbook/WORKBOOK.md`
- `production/paper-kernels/papers/CQE-paper-04/PAPER_KERNEL.md`
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\binary_boundary_adapter.py`
- `D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\transport_obligations.py`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-V-32-Theorems-Registry.md`
- `D:\CQE_CMPLX\Claude-Codex-Memory\Claude work\CL-AirLock-Survey\CL_airlock-formal-md-p00-p05.md`

Verifier/receipt status:

`boundary_repair_receipt.json` is `pass`.

Checks verified:

- consumes two Paper 02 correction states
- preserves Paper 03 axis/sheet coordinates
- all required fields present
- repaired rows are constraints, not proofs
- next legal routes nonempty
- repair is idempotent
- untyped failure rejected

Integer vs companions:

- Paper 4 integer paper:
  - abstract
  - definitions
  - theorem
  - proof of typed/idempotent repair
  - worked finite example using the two correction states
  - falsifier: `{"status":"failed"}` is rejected
  - explicit link to Paper 5 as next-route carrier
  - scope note: repair is constraint, not proof
- Paper 4.25 toolkit:
  - Binary Boundary Adapter
  - circle labels, head/tail, matching tail
  - `adapt(window)` concept
  - transport obligation ledger
  - local modules and verifier commands
- Paper 4.50 contract:
  - validation contract for a repair row
  - required fields
  - hidden-guess diagnostics
  - rejection rules for untyped failures
  - positive/negative/boundary/wrap tests
- Paper 4.75 application:
  - how repaired constraints precondition Paper 5
  - boundary repair as oloid midpoint / Dust pair introduced cautiously
  - forward links to Paper 6 causal code, Paper 14 curvature, Paper 15 mass-residue

Special cross-evidence:

Claude-side C-form material says Paper 4's deeper center is the boundary repair gluon / oloid repair midpoint:

```text
s* = (pole+ + pole-)/2
Dust(N,-N)
repair complete when orbit wraps to Lie conjugate L=R in <=3 S3 steps
```

This is important, but should stay a forward-linked strengthened interpretation unless the rewrite also pulls in the actual `verify_boundary_repair(N=4096)`/Dust implementation. The current production verifier proves the typed constraint version.

## Paper 05 - Oloid Path Carrier

Final scientific claim focus:

Paper 5 should prove that once Paper 4 has repaired a failure into a typed constraint, that constraint can be transported along a legal non-straight path. The strict theorem already promoted is:

```text
T_OLOID_PATH: curved/rolling carriers preserve continuity without straight-line transport.
```

Verified finite form:

```text
state q = (sheet, phase, parity)

sheet in {0,1}
phase in {0,1,2,3}
parity in {0,1}

roll(q,b) = ((sheet+1) mod 2, (phase+1) mod 4, parity xor b)
```

Head/tail dyad:

```text
head = sheet
tail = (phase mod 2) xor sheet xor parity
```

The core proof is that legal rolling steps produce a continuous trace, every adjacent pair is generated by one valid `roll`, dyads remain binary, and Paper 4 payloads do not alter the path rule.

Proof/evidence files:

- `production/formal-papers/CQE-paper-05/FORMAL_PAPER.md`
- `production/formal-papers/CQE-paper-05/verify_oloid_path_carrier.py`
- `production/formal-papers/CQE-paper-05/oloid_path_carrier_receipt.json`
- `production/papers/CQE-paper-05/SOURCE.md`
- `production/papers/CQE-paper-05/01-CQE-formal/FORMAL.md`
- `production/papers/CQE-paper-05/02-CQE-tool/TOOL.md`
- `production/papers/CQE-paper-05/03-CQE-workbook/WORKBOOK.md`
- `production/paper-kernels/papers/CQE-paper-05/PAPER_KERNEL.md`
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_rolling.py`
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_octonionic.py`
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\oloid_dual_path.py`
- `D:\CQE_CMPLX\CMPLX-PartsFactory-main\packages\lattice-forge\src\lattice_forge\quad_oloid.py`
- `D:\CQE_CMPLX\CMPLX-R30-main\FORMALIZATION\CAYLEY_DICKSON_OLOID_NORMAL_FORM.md`
- `D:\CQE_CMPLX\CMPLX-Kernel\lib-forge\summary_papers\SUMMARY-V-32-Theorems-Registry.md`
- `D:\CQE_CMPLX\Claude-Codex-Memory\Claude work\CL-AirLock-Survey\CL_airlock-formal-md-p00-p05.md`

Verifier/receipt status:

`oloid_path_carrier_receipt.json` is `pass`.

Checks verified:

- trace length is input length plus one
- adjacent pairs are legal rolls
- head/tail dyads are binary
- payload does not alter path rule
- invalid bit rejected
- discontinuous jump rejected
- prediction claim left out of scope

Example receipt:

Input bits:

```text
[1,0,1,1,0,0,1,0]
```

Trace returns to `(0,0,0)` after eight steps, with Paper 4 payload attached at state `(1,3,0)` without changing the rolling rule.

Integer vs companions:

- Paper 5 integer paper:
  - abstract
  - definitions of rolling carrier, legal step, dyad, trace, payload
  - theorem and proof of rolling continuity
  - worked finite trace
  - falsifiers: invalid bit, discontinuous jump, payload trying to alter path
  - explicit scope note: proves carrier continuity, not standalone Rule 30 prediction
  - link forward to Paper 6 causal edge and Paper 9/15 accumulated C
- Paper 5.25 toolkit:
  - oloid rolling modules
  - Cayley-Dickson oloid normal form
  - dual-path oloid modules
  - octonionic grounding
  - how to run or inspect verifier outputs
- Paper 5.50 contract:
  - what counts as valid path-carrier claim
  - every adjacent pair must be a legal roll
  - payload cannot mutate the path rule
  - prediction claims require separate verifier
  - hidden-guess prompts for continuity, dyads, invalid jumps
- Paper 5.75 application:
  - Paper 4 constraint becomes payload
  - path carrier becomes `C_accumulated`
  - forward links:
    - Paper 6: causal code
    - Paper 7: bridge
    - Paper 8: K=9 / lattice boundary
    - Paper 9: Hamiltonian time as `C_accumulated`
    - Paper 15: Higgs/mass-residue carrier

## Cross-Link: Paper 04 -> Paper 05

This dyad should be presented as one tight transition:

```text
Paper 4 repairs a failed boundary into a typed constraint.
Paper 5 transports that typed constraint along a legal rolling path.
```

Better formal bridge:

```text
repair_boundary(s) = constraint row r
attach_payload(q_t, r) = carried receipt at path state q_t
payload_alters_path_rule = false
```

This is the key conceptual connection. Paper 4 produces the object Paper 5 is allowed to carry.

The deeper C-form chain from local evidence is:

```text
P04: C = boundary repair midpoint / mediator
P05: C_accumulated = XOR of repair center bits along the carrier path
```

Use this as the polished connection:

"Boundary repair produces a conserved center-bearing payload. The path carrier transports that payload without erasing or rewriting it. When repeated over a trajectory, the transported centers accumulate as `C_accumulated`, which later papers reuse as Hamiltonian and mass-residue evidence."

Caution:

There are stronger local claims in `CMPLX-Kernel\lib-forge\summary_papers`, especially:

- oloid midpoint as confinement scale
- Wilson loop holonomy
- Higgs field/mass from `C_accumulated`
- Hamiltonian time from `C_accumulated`

Those should not dominate Papers 4 and 5. In Papers 4/5, mention them as downstream implications or linked future uses. The integer papers should prove the substrate operations first. The physics interpretation belongs later unless the relevant verifier is brought into the same paper's proof body.
