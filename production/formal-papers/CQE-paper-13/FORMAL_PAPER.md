# Paper 13 - Standard-Model Quark-Face Transport

## Abstract

This paper promotes the Standard-Model quark-face layer only to the extent
currently supported by finite algebraic receipts. The closed result is not a
derivation of physical quarks. It is the disciplined transport statement beneath
that proposed reading: the shell-2 `LCR` chart has exactly three states, those
states correspond to the three trace-2 idempotents of `J_3(O)`, the six-element
`S_3` Weyl action closes on that triple, and the `n=3` shell-2 transition is an
exact element of the `SU(3)` Weyl group ring over the rationals. A bounded
`G2/F4/T5A` route classifies already-enumerated bits in at most three stages
while explicitly refusing to become a cold-start depth-only derivation.

The six-face color/anticolor workbook model is retained as an analog exposure
surface. It is useful because it makes the algebraic transport inspectable, but
it does not by itself prove physical color charge, CKM phase, weak parity, or a
complete Standard Model extension.

## Claims

**Claim 13.1.** The shell-2 chart stratum is the three-element set
`{(1,1,0), (1,0,1), (0,1,1)}`.

**Claim 13.2.** The three shell-2 states map bijectively to the three trace-2
idempotents `{E11+E22, E11+E33, E22+E33}` in `J_3(O)`.

**Claim 13.3.** The six permutations of diagonal indices in `S_3` close on the
trace-2 triple.

**Claim 13.4.** The `n=3` shell-2 transition is an exact `SU(3)` Weyl group-ring
element with residual squared equal to `0` over `Q`.

**Claim 13.5.** The bounded `G2/F4/T5A` route is a route classifier for an
already-enumerated bit. It is not a depth-only derivation of that bit.

**Claim 13.6.** The color/anticolor six-face model is admitted as an analog
transport model, not as a physical derivation.

## Definitions

An **LCR chart state** is a triple `(L,C,R)` in `{0,1}^3`.

The **shell** of a chart state is `L + C + R`.

The **shell-2 stratum** is the set of chart states with shell value `2`.

A **quark face** in this paper is an algebraic face: one member of the trace-2
idempotent triple of `J_3(O)`. The word "quark" names the intended Standard
Model analogy, not a completed physical identification.

The **color Weyl action** is the `S_3` action induced by permuting diagonal
indices `(1,2,3)` and then reading the induced permutation of trace-2
idempotent pairs.

A **bounded route classifier** is a route that may classify an already-supplied
enumeration value while preserving a visible boundary that it did not derive the
value from depth alone.

## Theorem 13

The CQECMPLX quark-face layer is a closed algebraic transport layer:

```text
shell-2 LCR triple
-> trace-2 J_3(O) idempotent triple
-> closed S_3 Weyl action
-> exact n=3 SU(3) group-ring closure
-> bounded exceptional route classification
```

and the physical Standard Model reading remains an explicit obligation unless
and until a separate calibrated derivation is supplied.

## Proof

First enumerate all binary chart states with shell value `2`. There are exactly
three:

```text
C- = (1,1,0)
C0 = (1,0,1)
C+ = (0,1,1)
```

This proves Claim 13.1 by exhaustion.

Next map these states to the trace-2 idempotents:

```text
C- -> E11 + E22
C0 -> E11 + E33
C+ -> E22 + E33
```

`verify_j3o_axioms` verifies that the diagonal idempotents are idempotent and
Jordan-orthogonal, that they sum to the identity, and that the three trace-2
objects have trace `2` and are idempotent. This proves Claim 13.2 at the
algebraic layer.

Now let a permutation `sigma` in `S_3` act on diagonal indices. For any trace-2
pair `{i,j}`, the image is `{sigma(i), sigma(j)}`, again one of the three
two-element diagonal pairs. Since all six permutations are enumerated and every
image lands inside the same three-element set, the Weyl action closes on the
quark-face triple. This proves Claim 13.3.

The exact transition check is stronger than a floating-point fit. The verifier
`verify_n3_su3_closure_exact` computes the `n=3` shell-2 conditional matrix and
decomposes it over the `S_3` permutation matrices using rational arithmetic. The
receipt reports residual squared equal to `0` and `is_exact_group_ring_element =
true`. This proves Claim 13.4.

The exceptional route layer is then admitted with its honesty boundary intact.
`verify_conjugate_triple(max_depth=256)` reports a passing bounded classifier:
the route is oracle-backed, all tested routes resolve in at most three stages,
and `depth_only_bridge` is false. Therefore it classifies supplied bits but does
not claim to derive them cold-start from depth. This proves Claim 13.5 while
also limiting it.

Finally, the six-face model has three color faces, three conjugate faces,
involutive conjugation, and a closed `Z3` cycle on the three color faces. That
is a valid analog model of the algebraic transport surface. It is not a
derivation of physical color charge. This proves Claim 13.6 with the required
boundary.

Combining the five closed algebraic layers and the explicit physical boundary
proves the theorem.

## Receipt

The promoted verifier is:

```text
production/formal-papers/CQE-paper-13/verify_quark_face_transport.py
```

It writes:

```text
production/formal-papers/CQE-paper-13/quark_face_transport_receipt.json
```

The closed layers are:

```text
three shell-2 chart states
three trace-2 J_3(O) idempotents
six S3 Weyl actions close on the trace-2 triple
n=3 shell-2 transition is exact over the SU(3) Weyl group ring
bounded G2/F4/T5A route classifies oracle-enumerated bits in <=3 stages
six-face color/anticolor analog model is internally consistent
```

The open layers are:

```text
derivation of physical quark color charge
derivation of measured CKM phase or V-A weak structure
cold-start depth-only derivation through the G2/F4/T5A route
```

## Falsifiers

This paper fails if the shell-2 stratum does not contain exactly three states.

It fails if any trace-2 idempotent check in `J_3(O)` fails.

It fails if any `S_3` action leaves the trace-2 triple.

It fails if exact `n=3` closure has nonzero residual.

It fails if the bounded route is presented as a cold-start derivation.

It fails if the analog color-face model is used as a physical Standard Model
proof without a separate calibrated derivation.

## Role in the Suite

Paper 12 supplies a local CA prediction surface. Paper 13 receives one of its
correction/transport fields and shows how it can be read through a three-face
`J_3(O)` and `SU(3)`-Weyl closure. Paper 14 may use this as boundary-curvature
input only if it cites the receipt and preserves the physical-obligation
boundary.

## Conclusion

Paper 13 closes a real algebraic layer: shell-2 chart states, trace-2
idempotents, `S_3` transport, exact rational `SU(3)` closure, and bounded
exceptional-route classification. It does not yet close the physical Standard
Model derivation. That separation is the point of the paper: the transport
surface is proved; the physics identification remains a named target rather
than an implied result.
