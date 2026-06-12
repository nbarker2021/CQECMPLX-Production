# Paper 3 - D4/J3 Triality Surface

## Abstract

Paper 3 proves the first multi-language registration theorem in the CQECMPLX
sequence. Paper 1 defines the local LCR carrier. Paper 2 identifies the first
correction residue. Paper 3 proves that the same eight local states can be read
without loss in three linked languages:

```text
LCR state <-> D4-style axis/sheet code <-> diagonal J3 carrier
```

The theorem is intentionally local and finite. It does not claim the full D4
triality automorphism theorem, nor a full exceptional Jordan algebra action.
It proves the registration surface needed by the next papers: a bijective
axis/sheet encoding of `{0,1}^3`, trace preservation by `diag(L,C,R)`, and
trace-2 diagonal idempotents for the shell-2 states.

## Claims

**Claim 3.1.** The eight binary LCR states admit a bijective D4-style
axis/sheet chart.

**Claim 3.2.** The diagonal carrier `phi(L,C,R)=diag(L,C,R)` preserves the
LCR shell as trace.

**Claim 3.3.** The shell-2 states map to trace-2 diagonal idempotents under
coordinate-wise diagonal product.

**Claim 3.4.** The Paper 2 correction states are preserved as registered
coordinates `(2,0)` and `(3,1)`.

## Definitions

Let:

```text
S = {0,1}^3
s = (L,C,R) in S
shell(s) = L + C + R
```

Define the axis map:

```text
axis(0,0,0) = 0    axis(1,1,1) = 0
axis(1,0,0) = 1    axis(0,1,1) = 1
axis(0,1,0) = 2    axis(1,0,1) = 2
axis(0,0,1) = 3    axis(1,1,0) = 3
```

Define the sheet map:

```text
sheet(L,C,R) = 0 if L+C+R <= 1
sheet(L,C,R) = 1 if L+C+R >= 2
```

Define the diagonal carrier:

```text
phi(L,C,R) = diag(L,C,R)
```

On diagonal carriers, use coordinate-wise diagonal product:

```text
diag(a,b,c) o diag(a,b,c) = diag(a*a,b*b,c*c)
```

## Theorem 3.1 - Local Triality Surface

The map

```text
tau(L,C,R) = (axis(L,C,R), sheet(L,C,R), diag(L,C,R))
```

is a faithful three-language presentation of the eight binary LCR states. The
axis/sheet component is a bijection from `S` to `{0,1,2,3} x {0,1}`. The
diagonal component preserves shell as trace. The shell-2 states map to
trace-2 diagonal idempotents.

## Proof

The axis map partitions the eight states into four complement pairs:

```text
axis 0: (0,0,0), (1,1,1)
axis 1: (1,0,0), (0,1,1)
axis 2: (0,1,0), (1,0,1)
axis 3: (0,0,1), (1,1,0)
```

Within each axis pair, one state has shell `0` or `1`, and the complement has
shell `2` or `3`. The sheet bit therefore selects exactly one state inside
each pair. Hence `(axis, sheet)` names exactly one state, and every state is
named once.

For the diagonal carrier:

```text
trace(phi(L,C,R)) = trace(diag(L,C,R)) = L + C + R = shell(L,C,R)
```

If `shell(s)=2`, then `phi(s)` has two diagonal `1` entries and one diagonal
`0` entry. Since every binary entry is idempotent,

```text
phi(s) o phi(s) = phi(s)
```

Thus shell-2 states become trace-2 diagonal idempotents. The Paper 2 correction
states are among the enumerated states, and their registered coordinates are
read directly from the axis/sheet chart:

```text
(0,1,0) -> (2,0)
(1,1,0) -> (3,1)
```

This proves the local registration theorem.

## Receipt

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-03/verify_triality_surface.py
production/formal-papers/CQE-paper-03/triality_surface_receipt.json
```

The receipt status is `pass`. It verifies:

```text
axis_sheet_bijection                    = true
axis_pairs_are_antipodal                = true
trace_equals_shell                      = true
shell2_states_are_diagonal_idempotents  = true
paper02_correction_coordinates_preserved = true
strong_triality_left_as_obligation      = true
```

## Scope Boundary

This paper proves a local triality surface. It does not, by itself, prove:

```text
full D4 triality automorphism
full F4 action on J3(O)
off-diagonal octonionic dynamics
S3 group-ring closure of a Rule 30 trace-2 transition matrix
```

Those claims may be imported only when their own receipts are attached.

## Falsifiers

The paper fails if any of the following occur:

```text
two different LCR states share the same axis/sheet coordinate
any LCR state lacks an axis/sheet coordinate
trace(diag(L,C,R)) differs from L+C+R
a shell-2 diagonal carrier is not idempotent
the Paper 2 correction states do not map to (2,0) and (3,1)
full D4/F4/J3(O) claims are counted as closed by this receipt alone
```

## Role in the Suite

Paper 3 supplies registered object transport. Paper 2 gives the correction
residue, Paper 3 gives that residue a second coordinate language, and Paper 4
uses the registered residue as a boundary repair input.

The transfer is:

```text
correction residue -> registered coordinate -> boundary repair constraint
```

## Open Obligations

1. Wire `verify_triality_surface` into the installable kernel/API interface.
2. Add the stronger group-action proof as a separate theorem if full D4/F4
   language is used as proof rather than orientation.
3. Reconcile all D-drive copies of the axis/sheet codec against this receipt.
4. Ensure Paper 4 consumes the exact Paper 2 coordinates preserved here.

## Conclusion

Paper 3 proves that the local event can be registered without losing its
state. The same `(L,C,R)` carrier can be read as an axis/sheet chart entry and
as a diagonal trace carrier. That is the object-level registration discipline
that later papers generalize into repair, path transport, and causal proof
edges.
