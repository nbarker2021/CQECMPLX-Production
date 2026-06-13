# Paper 1 - LCR Chain Carrier

## Abstract

This paper defines the first active object in the CQECMPLX sequence after the
foreword and claim contract: the local Left-Center-Right carrier. The carrier
is the ordered triple

```text
(L, C, R)
```

where `C` is the active center selected by the observer's enumeration event,
and `L` and `R` are the two boundary addresses read relative to that center.

The main theorem is deliberately small and foundational. Any local carrier
that preserves one distinguished center and records two addressable boundary
directions requires at least three positions. The ordered LCR triple realizes
that lower bound. This proves that the LCR chart is the minimal carrier for
the later papers' transport, correction, triality, boundary, and observer
claims.

The paper also records the first physical bridge used by the suite: the
`shell = 2` subspace of the binary LCR chart contains the three states

```text
(1,1,0), (1,0,1), (0,1,1)
```

and the left-right side flip exchanges the two chiral states while fixing the
middle state. This is the local structure later papers use as the
single-forward-tape doublet carrier. Paper 1 proves the finite carrier facts
directly and binds the stronger doublet interpretation to the downstream
trace-2/Jordan and closure papers where its larger algebraic claims are
completed.

## Claims

**Claim 1.1.** The LCR carrier is the minimal ordered local carrier that
preserves one center and two boundary addresses.

**Claim 1.2.** For the binary chart, there are exactly eight local states, and
left-right reversal preserves `C`, is an involution, and partitions the states
into four fixed states and two two-state reversal orbits.

**Claim 1.3.** Directional opposition is address-based, not value-based.
Therefore the statement "opposed boundaries must have unequal values" is
false. The counterexample is `(1,0,1)`, where `L = R = 1` while `L` and `R`
remain distinct boundary addresses.

**Claim 1.4.** The `shell = 2` stratum supplies the first carried doublet
interface: `(1,1,0)` and `(0,1,1)` are exchanged by left-right reversal, while
`(1,0,1)` is fixed. The full physical reading of this interface is carried
forward to the trace-2 and closure results in Papers 3 and later.

**Claim 1.5.** The O8 spinor double-cover obligation is closed at the local
carrier interface: frame inversion `F` has `F^2 = -1` at `2*pi` and `F^4 = +1`
at `4*pi`, as verified by the oloid kinematic receipts.

## Predictions

The finite verifier for Paper 1 must return:

```text
state count                         = 8
shell multiplicities                = 1, 3, 3, 1
left-right reversal preserves C      = true
left-right reversal is involutive    = true
fixed reversal states                = 4
two-state reversal orbits            = 2
counterexample to value inequality   = (1,0,1)
minimal address count                = 3
```

A verifier or reviewer that reports every `shell = 2` state as having unequal
boundary values must fail.

## Definitions

Let `A` be a finite alphabet. For the binary examples in this paper,
`A = {0,1}`.

An **LCR state** over `A` is an ordered triple:

```text
s = (L, C, R) in A^3
```

`C` is the distinguished center. `L` is the left boundary address read relative
to `C`. `R` is the right boundary address read relative to `C`.

The **center projection** is:

```text
pi_C(L,C,R) = C
```

The **left-right reversal** is:

```text
rho(L,C,R) = (R,C,L)
```

The **binary shell** is:

```text
shell(L,C,R) = L + C + R
```

The binary shell grades have multiplicity:

```text
shell 0: 1 state
shell 1: 3 states
shell 2: 3 states
shell 3: 1 state
```

Directional opposition means:

```text
address(L) != address(R)
```

Value inequality means:

```text
value(L) != value(R)
```

Paper 1 requires directional opposition. It does not require value inequality
in every state.

## Test Protocol

The test is finite.

1. Enumerate all triples in `{0,1}^3`.
2. Compute `rho(s)` for every state.
3. Check that `pi_C(rho(s)) = pi_C(s)` for every state.
4. Check that `rho(rho(s)) = s` for every state.
5. Count shell multiplicities.
6. Count fixed states and two-state orbits under `rho`.
7. Test the false boundary-value claim against `(1,0,1)`.
8. Check that the address roles `{left_boundary, center, right_boundary}` have
   cardinality three.

The production verifier is:

```text
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
production/formal-papers/CQE-paper-01/verify_o8_spinor_double_cover_closed.py
```

It emits:

```text
production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json
production/formal-papers/CQE-paper-01/o8_spinor_double_cover_closed_receipt.json
```

## Results

The verifier returns `status = pass`.

The eight binary LCR states are:

```text
(0,0,0) shell 0
(0,0,1) shell 1
(0,1,0) shell 1
(0,1,1) shell 2
(1,0,0) shell 1
(1,0,1) shell 2
(1,1,0) shell 2
(1,1,1) shell 3
```

The fixed states under left-right reversal are:

```text
(0,0,0)
(0,1,0)
(1,0,1)
(1,1,1)
```

The two nontrivial reversal pairs are:

```text
(0,0,1) <-> (1,0,0)
(0,1,1) <-> (1,1,0)
```

The counterexample to the false boundary-value claim is:

```text
(1,0,1)
```

It has shell 2 and equal boundary values, but its left and right boundary
addresses remain distinct.

## Theorem 1.1 - Minimal LCR Carrier

Any ordered local carrier that preserves one distinguished center and records
two addressable boundary directions requires at least three positions. The
ordered triple `(L,C,R)` realizes this lower bound and is therefore minimal.

### Proof

A carrier that preserves a distinguished center must contain an address for
the center. A carrier that records two boundary directions relative to that
center must contain one address for the left boundary and one address for the
right boundary.

These three addresses cannot be identified. If the center address is identified
with a boundary address, the center is no longer distinguished. If the two
boundary addresses are identified, the carrier cannot distinguish left from
right. Therefore any such carrier has at least three addresses.

The ordered triple `(L,C,R)` has exactly these three addresses. It preserves
the center by `pi_C`, records both boundary directions, and admits the reversal
operation `rho`. Therefore it attains the lower bound. QED.

## Theorem 1.2 - Binary Reversal Inventory

In the binary LCR chart, left-right reversal preserves the center, is an
involution, has four fixed states, and has two nontrivial two-state orbits.

### Proof

For any state `(L,C,R)`:

```text
pi_C(rho(L,C,R)) = pi_C(R,C,L) = C = pi_C(L,C,R)
```

and:

```text
rho(rho(L,C,R)) = rho(R,C,L) = (L,C,R)
```

Thus reversal preserves the center and is an involution.

The fixed states satisfy `L = R`, giving:

```text
(0,0,0), (0,1,0), (1,0,1), (1,1,1)
```

The remaining four states form two reversal pairs:

```text
(0,0,1) <-> (1,0,0)
(0,1,1) <-> (1,1,0)
```

This exhausts the eight binary states. QED.

## Theorem 1.3 - O8 Spinor Double-Cover Closure

The frame-inversion operator `F` carried by the oloid kinematic layer realizes
the local SU(2) to SO(3) double-cover semantics required by O8. In the verified
carrier, `F^2` gives the spinor sign at `2*pi`, and `F^4` returns to the origin
at `4*pi`.

### Proof

The verifier composes the existing oloid kinematic checks. Bit complement is
verified as frame inversion. The two-period check verifies the `pi` phase
advance corresponding to `-1` at `2*pi`. The four-period check verifies return
to origin, corresponding to `+1` at `4*pi`. The alternating-bit and oloid
kinematic checks confirm consistency of the rolling double-cover carrier.
Together these checks close O8 for the local carrier interface. QED.

## Doublet Interface

The `shell = 2` stratum is:

```text
(1,1,0), (1,0,1), (0,1,1)
```

Left-right reversal maps:

```text
(1,1,0) <-> (0,1,1)
(1,0,1) -> (1,0,1)
```

This gives the first local doublet interface used by the suite: two chiral
states exchanged by side flip and one fixed pivot. The stronger statement that
this interface is the single-forward-tape carrier for the SU(2)-style doublet
is carried as `T_BIJECTIVE` in the surrounding evidence corpus and depends on
the trace-2/Jordan registration and later closure papers. Paper 1 supplies the
finite carrier and reversal facts those later claims require.

## Falsifiers

The paper fails if any of the following occurs:

```text
the binary state count is not 8
rho fails to preserve C
rho is not an involution
shell counts differ from 1,3,3,1
the fixed-state count is not 4
the nontrivial reversal-pair count is not 2
(1,0,1) is not recognized as a shell-2 equal-boundary counterexample
a two-address object is claimed to preserve one center and two distinct boundaries
```

## Scope Boundary

Paper 1 proves the minimal carrier and the finite binary reversal inventory.
It does not by itself prove the full Standard Model extension, the full
`J_3(O)` registration, or the full Rule 30 solve. It does close the local O8
spinor double-cover semantics through the oloid kinematic frame-inversion
receipt, and it supplies the first finite doublet interface that later papers
must preserve.

## Evidence Bindings

Primary executable evidence:

```text
production/formal-papers/CQE-paper-01/verify_lcr_carrier.py
production/formal-papers/CQE-paper-01/lcr_carrier_receipt.json
```

Supporting source evidence:

```text
production/papers/CQE-paper-01/SOURCE.md
production/papers/CQE-paper-01/PAPER-BODY.md
D:/CQE_CMPLX/Claude-Codex-Memory/Claude work/CL-Paper-Evidence-DB/CL-CQE-Papers-01-05-C-Form-Chain.md
D:/CQE_CMPLX/CMPLX-R30-main/CATALOG/distilled_claims.json
```

## Conclusion

Paper 1 establishes the local carrier that every later paper must respect.
The result is not a metaphor and not a tool description. It is a finite
structural theorem: one center plus two distinguishable boundary directions
requires three ordered addresses, and the binary chart over those addresses
has a fully enumerated reversal structure. Later papers may lift, repair,
curve, or reinterpret that carrier, but they must preserve the accounting of
`L`, `C`, `R`, and the observer-chosen center.
