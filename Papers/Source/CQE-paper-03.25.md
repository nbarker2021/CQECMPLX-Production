# Paper 3.25 - Toolkit for the D4/J3 Triality Surface

## Purpose

Paper 3.25 describes the tools for reviewing Paper 3's local registration
theorem. The tools expose the finite chart and diagonal carrier; they do not
prove additional exceptional-algebra claims.

## Review Objects

The toolkit works with:

```text
LCR state        = (L,C,R)
axis             = complement-pair label in {0,1,2,3}
sheet            = low-shell or high-shell selector
diagonal carrier = diag(L,C,R)
trace            = L + C + R
idempotent test  = diag(L,C,R) o diag(L,C,R) = diag(L,C,R)
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-03/verify_triality_surface.py
production/formal-papers/CQE-paper-03/triality_surface_receipt.json
```

Additional source and kernel files:

```text
production/papers/CQE-paper-03/SOURCE.md
production/papers/CQE-paper-03/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-03/02-CQE-tool/TOOL.md
production/papers/CQE-paper-03/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-03/PAPER_KERNEL.md
```

The verifier checks the axis/sheet bijection, antipodal axis pairs, trace
preservation, trace-2 idempotency, and Paper 2 correction-coordinate
preservation.

## Analog Toolkit

A physical reconstruction requires:

- eight LCR cards,
- four axis labels,
- two sheet labels,
- a diagonal trace column,
- a receipt row.

Procedure:

```text
list all eight LCR states
pair each state with its bitwise complement
assign pairs to axes 0,1,2,3
mark sheet 0 for shell <= 1
mark sheet 1 for shell >= 2
confirm every axis/sheet coordinate is used once
write diag(L,C,R)
check trace = shell
check trace-2 diagonals are idempotent
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What axis/sheet coordinate does (0,1,0) receive?
What axis/sheet coordinate does (1,1,0) receive?
Does this receipt prove full D4 triality?
Which shell states become trace-2 diagonal idempotents?
```

Expected answers:

```text
(2,0)
(3,1)
no
the shell-2 states
```

## Boundary

Paper 3.25 is a toolkit supplement. Any claim about full triality, F4 action,
or off-diagonal octonionic dynamics must enter through Paper 3.50's claim
contract before it can be used as a proof claim.
