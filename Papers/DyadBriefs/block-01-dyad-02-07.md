# Block 01 Dyad Brief - Papers 2 and 7

Source: Dyad Agent B, read-only synthesis. Agent inspected files and ran
verifiers. No edits made by agent.

## Paper 2

Final scientific focus:

Paper 2 is the first rigorous residue theorem. The integer paper should center
on the exact GF(2) decomposition:

```text
Rule30(L,C,R) = Rule90(L,R) xor corr(L,C,R)
corr(L,C,R) = C and not R
```

The claim is not "failure proves the route"; it is "failure becomes typed,
replayable correction data." The firing surface is exactly:

```text
{(0,1,0), (1,1,0)}
```

with D4 chart projections:

```text
(2,0), (3,1)
```

Evidence files:

```text
production/formal-papers/CQE-paper-02/FORMAL_PAPER.md
production/formal-papers/CQE-paper-02/verify_correction_surface.py
production/formal-papers/CQE-paper-02/correction_surface_receipt.json
production/papers/CQE-paper-02/SOURCE.md
production/papers/CQE-paper-02/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-02/02-CQE-tool/TOOL.md
production/papers/CQE-paper-02/02-CQE-tool/run.py
production/papers/CQE-paper-02/03-CQE-workbook/WORKBOOK.md
production/lib-forge/recovered/papers_output/CQE-paper-02.md
production/paper-kernels/papers/CQE-paper-02/PAPER_KERNEL.md
```

Verifier status:

`verify_correction_surface.py` passes. Checks prove:

```text
8-state enumeration
identity for all states
exact firing set
D4 projection
residue is obligation, not proof
```

Integer paper vs supplements:

- Integer Paper 2: abstract, definitions, theorem, proof by Boolean algebra,
  full truth-table receipt, D4 projection as checked codec output, falsifier
  that residue alone is not proof.
- Paper 2.25: correction toolkit: correction token, clear overlay, black
  obligation row, `verify_correction_surface`.
- Paper 2.50: admissible correction row contract: state, source rule, residue
  value, route, next obligation.
- Paper 2.75: residue feeds Paper 3 triality intake, Paper 4 boundary repair,
  and Paper 6 causal edges.

## Paper 7

Final scientific focus:

Paper 7 is a narrow sample-preserving interpolation theorem. Every finite
indexed numeric trace admits a continuous piecewise-linear interpolant that
exactly preserves all integer samples. This lets the suite draw
continuous-looking fields without deleting discrete receipts. It does not
prove unique physical dynamics between samples.

Evidence files:

```text
production/formal-papers/CQE-paper-07/FORMAL_PAPER.md
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json
production/papers/CQE-paper-07/SOURCE.md
production/papers/CQE-paper-07/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-07/02-CQE-tool/TOOL.md
production/papers/CQE-paper-07/03-CQE-workbook/WORKBOOK.md
production/lib-forge/recovered/papers_output/CQE-paper-07.md
production/paper-kernels/papers/CQE-paper-07/PAPER_KERNEL.md
```

Verifier status:

`verify_discrete_continuous_bridge.py` passes. Checks prove:

```text
integer samples preserved
max sample error zero
adjacent segment endpoint agreement
Rule30/Rule90 correction identity still holds
between-sample physics remains an obligation
```

Paper 7 tool runner is missing in the kernel manifest, so the rewrite should
cite the promoted verifier, not an absent `run.py`.

Integer paper vs supplements:

- Integer Paper 7: theorem of sample-preserving interpolation, proof by
  piecewise-linear construction, exact receipt, falsifier rejecting
  "interpolation proves all between-sample physics."
- Paper 7.25: plotting indexed samples, drawing segments, bridge receipt,
  optional correction overlay.
- Paper 7.50: encoder/sampling declaration required; sample preservation is
  admissible, physical dynamics requires a separate theorem.
- Paper 7.75: feeds Paper 8 lattice closure and Paper 9 Hamiltonian windows
  only as sampled receipts unless later dynamics are proved.

## Dyad Cross-Link

The clean bridge is:

```text
correction surface
-> indexed residue trace
-> sample-preserving bridge
-> continuous presentation with original discrete receipt preserved
```

Paper 2 supplies the nonlinear residue `C and not R`. Paper 7 can interpolate
a trace containing those correction bits, but the correction proof remains
discrete at the indexed samples. Paper 7 does not smooth away correction; it
visualizes and transports it while preserving the exact sample ledger.

Important rewrite caution:

Older Paper 7 source contains broader indexed-discretization, CMB/Hawking/Wow,
`n=3` closure, and bridge Gluon language. Keep that material as extension
evidence or companion content unless the final integer paper includes matching
receipts. The current verified integer claim is sample preservation, plus the
correction identity inherited from Paper 2.
