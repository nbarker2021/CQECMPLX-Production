# Paper 14 - GR Boundary-Repair Curvature

## Abstract

This paper defines the CQECMPLX substrate meaning of curvature as a
boundary-repair demand. The closed result is a transport-ledger theorem: every
route has a typed status, demonstrated rows carry zero repair score, non-closed
lifts carry nonzero repair score, and the exact Paper 13 `SU(3)` closure
supplies the zero-repair reference. The oloid modules supply a curved carrier:
the Cayley-Dickson/Oloid normal form verifies the repeating `1,8,8,1` pattern,
and the dual-path oloid verifies three-dyad involution coherence.

This is not a derivation of General Relativity. Riemann curvature, Ricci
curvature, Einstein tensors, and measured gravitational effects remain physical
obligations. The paper proves the boundary-repair accounting layer that later
work may compare to curvature.

## Claims

**Claim 14.1.** The transport ledger is a finite typed repair ledger whose rows
carry explicit proof boundaries.

**Claim 14.2.** Demonstrated rows define zero repair in this ledger.

**Claim 14.3.** Open or lifted rows define positive repair demand.

**Claim 14.4.** Exact `n=3` `SU(3)` closure from Paper 13 is a zero-repair
reference because its residual squared is exactly `0`.

**Claim 14.5.** The Cayley-Dickson/Oloid carrier verifies a repeating
`1,8,8,1` normal-form pattern while explicitly refusing to prove nth-bit
extraction by itself.

**Claim 14.6.** General Relativity curvature is a candidate interpretation of
repair demand, not a closed theorem in this paper.

## Definitions

A **repair demand** is unresolved transport residue preserved as an obligation
instead of erased.

A **repair score** is the scalar proxy:

```text
demonstrated -> 0
bounded_local -> 1
bounded_external -> 2
registered_landing_forms -> 3
open -> 4
```

A **flat reference** is a closed transport whose exact residual is `0`.

A **curved carrier** is a carrier that transports a state through a non-flat or
multi-dyad route while preserving a receipt and an honesty boundary.

## Theorem 14

For the currently promoted transport ledger, boundary-repair curvature is a
well-defined substrate quantity:

```text
curvature_CQE(route) = repair_score(route.classification)
```

with zero value exactly on demonstrated rows and positive value on visible
non-closed lifts. This quantity is a CQECMPLX repair ledger, not a physical
Riemann tensor.

## Proof

The verifier reads the four transport obligation rows. Each row has a source
object, target object, map, preserved quantity, failure condition, witness,
classification, and proof boundary. This proves Claim 14.1.

The verifier assigns repair score `0` to `demonstrated` rows. It checks that all
demonstrated rows have score `0`. This proves Claim 14.2.

The verifier assigns positive score to all lifted or open classifications. The
current ledger has two demonstrated rows and two open lifts; the two open lifts
are exactly the rows with nonzero repair score. This proves Claim 14.3.

Paper 13 supplies the flat reference. Its exact `n=3` shell-2 `SU(3)` closure
has residual squared `0` over the rationals. A zero residual requires no repair
row at that closure layer. This proves Claim 14.4.

The Cayley-Dickson/Oloid verifier checks the normal form across the tested
range and confirms the `1,8,8,1` pattern. The generated form carries an honesty
string stating that the normal form does not by itself prove nth-bit extraction.
The dual-path oloid verifier also passes, including the three-dyad involution
coherence checks. This proves Claim 14.5.

No computation in the receipt constructs Riemann, Ricci, or Einstein tensors.
The verifier explicitly rejects the claim that Einstein field equations are
verified by this receipt. This proves Claim 14.6.

Together these results prove the theorem.

## Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-14/verify_boundary_repair_curvature.py
```

Receipt:

```text
production/formal-papers/CQE-paper-14/boundary_repair_curvature_receipt.json
```

Closed layers:

```text
transport obligations are typed and boundary-bearing
demonstrated rows score zero repair
open lifts score nonzero repair
Paper 13 exact SU3 closure supplies zero-repair reference
Cayley-Dickson/Oloid normal form verifies 1,8,8,1 carrier pattern
dual-path oloid verifies three-dyad involution coherence
```

Open layers:

```text
Riemann/Ricci/Einstein tensor derivation
calibrated gravitational measurement
nth-bit extraction from the oloid normal form alone
```

## Falsifiers

The paper fails if any transport row lacks a proof boundary.

It fails if a demonstrated row receives nonzero repair score.

It fails if a non-closed lift is treated as zero repair.

It fails if the Paper 13 flat reference has nonzero exact residual.

It fails if the oloid normal form is presented as nth-bit extraction.

It fails if this receipt is used as a derivation of Einstein's field equations.

## Role in the Suite

Paper 13 proves the exact zero-repair reference. Paper 14 defines how visible
residue becomes repair magnitude. Paper 15 may use this repair magnitude as
mass-residue input only if it preserves the open physical boundary.

## Conclusion

Paper 14 closes the substrate theorem for boundary-repair curvature: repair is
typed, scored, receipt-bearing, and carried on verified non-flat support. It
does not close General Relativity. The result is useful because it makes the
curvature analogy testable instead of rhetorical.
