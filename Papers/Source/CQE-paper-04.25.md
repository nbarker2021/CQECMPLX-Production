# Paper 4.25 - Toolkit for Boundary Repair

## Purpose

Paper 4.25 describes the review tools for boundary repair. The tools help a
reader construct and inspect repair rows. They do not add claims beyond the
Paper 4 theorem.

## Review Objects

The toolkit works with:

```text
correction state       = Paper 2 residue state
axis_sheet coordinate  = Paper 3 registration
repair row             = typed boundary constraint
next legal route       = route allowed to consume the constraint
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-04/verify_boundary_repair.py
production/formal-papers/CQE-paper-04/boundary_repair_receipt.json
```

Additional package evidence named by the dyad review:

```text
D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\binary_boundary_adapter.py
D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\transport_obligations.py
```

The verifier checks that Paper 2 correction states are consumed, Paper 3
coordinates are preserved, required fields are present, constraints are not
proofs, next legal routes are nonempty, repair is idempotent, and untyped
failures are rejected.

## Analog Toolkit

A physical reconstruction requires:

- one correction row,
- one coordinate lookup,
- one repair-row template,
- one next-route label,
- one receipt line.

Procedure:

```text
copy the Paper 2 correction state
copy the Paper 3 axis/sheet coordinate
write the reason: correction fired
write status: constraint
write at least one next legal route
write source paper and target paper
repeat the repair operation and confirm the row does not change
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What fields are required for a repaired boundary row?
Does a repaired row count as proof?
Which two states produce repair rows?
Is {"status":"failed"} repairable?
```

Expected answers:

```text
state, axis_sheet, reason, status, next_legal_routes, source_paper, target_paper
no
(0,1,0) and (1,1,0)
no
```

## Boundary

Paper 4.25 is a toolkit supplement. If a new adapter, route, or domain example
is found, it must pass Paper 4.50's claim contract before it changes the
scientific paper.
