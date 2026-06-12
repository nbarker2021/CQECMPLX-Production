# Paper 4.50 - Boundary Repair Claim Contract

## Purpose

Paper 4.50 defines what counts as a valid boundary repair claim. It prevents
failed joins from being erased, and it prevents repair rows from being counted
as proof before the next legal route closes them.

## Admitted Paper 4 Claims

The following claims are admitted from Paper 4:

```text
Paper 2 correction states can become typed boundary constraints
Paper 3 coordinates are preserved in the repair rows
required repair fields are state, axis_sheet, reason, status, next_legal_routes, source_paper, target_paper
repaired rows have status constraint, not proof
repair is idempotent on already repaired rows
untyped failures are rejected
```

## Claim Requirements

Any later paper using a Paper 4 repair row must state:

```text
which correction state is being repaired
which axis/sheet coordinate is preserved
why the row exists
which next route consumes it
which receipt proves the row
whether the row remains a constraint or has been closed by a later theorem
```

## Linked Receipt

The minimum receipt link for Paper 4 is:

```text
paper: CQE-paper-04
theorem: Typed boundary repair
receipt: production/formal-papers/CQE-paper-04/boundary_repair_receipt.json
status: pass
```

The receipt is sufficient for the typed repair theorem. It is not sufficient by
itself for oloid midpoint physics, confinement-scale claims, or downstream
mass-residue claims.

## Boundary Failures

The following are boundary failures:

```text
using a row with status failed as if it were repaired
omitting the source state or axis/sheet coordinate
omitting the next legal route
marking a repair constraint as proof
allowing a payload to rewrite the repair row without a new receipt
```

Boundary failures are routed to obligations or rejected by the consuming paper.

## Hidden-Guess Contract

When hidden-guess diagnostics are enabled, the answer must be recorded before
the receipt is revealed. The guess record should include:

```text
prompt
predicted required fields or repair status
revealed receipt
match/mismatch
next obligation if mismatch
```

The "constraint or proof?" prompt is required because the correct answer is
constraint.

## Conclusion

Paper 4.50 lets later papers import repair rows honestly. It keeps the failure
visible, the repair typed, and the proof status bounded until another theorem
actually closes the route.
