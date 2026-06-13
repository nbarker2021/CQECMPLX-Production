# Paper 12 - CA Prediction Surface

## Abstract

Paper 12 defines the prediction surface for deterministic binary cellular
automata. A prediction surface is not a single magic predictor. It is a typed
layer stack in which each layer reports its input, output, cost class, defect,
and receipt.

The closed result in this paper is finite and local. For Rule 30, the local
truth table agrees with:

```text
Rule30(L,C,R) = L xor (C or R)
```

and with the local readout law:

```text
T_EMISSION(L,C,R) = not L if C=1 else L xor R
```

The same local rule decomposes as:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

The paper also verifies that exactly 64 of the 256 elementary cellular
automata have silent boundary values `f(000)=0` and `f(111)=0`. The paper does
not prove a cold-start full `O(log N)` Rule 30 extractor and does not prove the
spectral next-state layer.

EntropyForge is admitted as a bounded extension of the same surface. It
verifies the canonical Rule 30 center-column implementation, the finite
VOA-sector partition `Z(q) = 2q^0 + 6q^5`, the arithmetic identity
`196883 = 47 * 59 * 71`, a finite non-periodicity window, and repeatable seeded
stream behavior. Infinite center-column non-periodicity and product-level
statistical certification remain obligations.

## Claims

**Claim 12.1.** The Rule 30 local truth table matches `L xor (C or R)` on all
eight LCR states.

**Claim 12.2.** The `T_EMISSION` formula matches Rule 30 on all eight LCR
states.

**Claim 12.3.** Rule 30 decomposes as `Rule90 xor (C and not R)` on all eight
LCR states.

**Claim 12.4.** Exactly 64 of the 256 elementary cellular automata are
silent-boundary rules.

**Claim 12.5.** A prediction surface must preserve layer, cost, defect, and
receipt metadata; empirical or open layers cannot be counted as closed.

**Claim 12.6.** EntropyForge may be treated as a finite, receipt-bound product
extension of Paper 12 when it preserves the canonical Rule 30 column, the
finite VOA-sector partition, deterministic syndrome behavior, and explicit open
obligations.

## Definitions

An **elementary cellular automaton** is a radius-1 binary rule:

```text
f : {0,1}^3 -> {0,1}
```

For rule number `r`, the local emission is:

```text
emit_r(L,C,R) = (r >> (4L + 2C + R)) & 1
```

A **prediction surface** is:

```text
surface(system, N) -> (bit, layer, cost, defect, receipt)
```

For Rule 30:

```text
Rule30(L,C,R) = L xor (C or R)
Rule90(L,R)   = L xor R
correction    = C and not R
```

A **silent-boundary rule** is an ECA satisfying:

```text
emit_r(0,0,0) = 0
emit_r(1,1,1) = 0
```

The **canonical center column** is the single-cell Rule 30 evolution read at
the center position across a finite depth. Product seeded streams may wrap this
surface, but they do not replace the paper-bound canonical object.

## Theorem 12.1 - CA Prediction Surface Finite Local Layers

The Rule 30 local readout, `T_EMISSION`, and Rule90-correction decomposition
are exact on the eight binary LCR states. The 256-rule ECA space contains
exactly 64 silent-boundary rules. These facts form the closed finite layer of
the CA prediction surface.

## Proof

Enumerate all states:

```text
(L,C,R) in {0,1}^3
```

For each state, compute `emit_30(L,C,R)` from the ECA rule number and compute
`L xor (C or R)`. The verifier checks equality on all eight rows.

For `T_EMISSION`, if `C=1` then:

```text
L xor (C or R) = L xor 1 = not L
```

If `C=0` then:

```text
L xor (C or R) = L xor R
```

Therefore `T_EMISSION` matches Rule 30 on every local state.

For the correction decomposition:

```text
C or R = C xor R xor (C and R)
```

so:

```text
Rule30 = L xor C xor R xor (C and R)
       = (L xor R) xor (C xor (C and R))
       = Rule90 xor (C and not R)
```

The silent-boundary count is finite. Two of the eight truth-table entries are
fixed to zero. The remaining six entries are free, giving:

```text
2^6 = 64
```

silent-boundary rules.

## Theorem 12.2 - Bounded EntropyForge Extension

EntropyForge is a valid Paper 12 product extension when it remains finite,
receipt-bound, and explicit about its obligations.

The verifier checks ten finite rows:

```text
Rule 30 formula matches Wolfram code 30
VOA partition is Z(q) = 2q^0 + 6q^5
Monster scalar is 47 * 59 * 71 = 196883
D4 antipodal axes partition the eight states
two center-column implementations agree on 512 bits
no period p <= 256 appears within the first 2048 canonical bits
XOR-debiased density stays within tolerance
VOA syndrome is deterministic and window-sensitive
seeded streams repeat for equal seeds and separate for distinct seeds
entropy block round-trips and verifies client-side
```

The non-periodicity row is finite. It proves only the stated checked window.
The infinite-column statement remains an obligation.

## Receipts

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-12/verify_ca_prediction_surface.py
production/formal-papers/CQE-paper-12/ca_prediction_surface_receipt.json
```

The receipt status is `pass`. It verifies:

```text
rule30_truth_table_matches_formula        = true
t_emission_matches_rule30                 = true
rule30_rule90_correction_identity_holds   = true
local_state_count_is_8                    = true
silent_boundary_rule_count_is_64          = true
cold_start_rule30_extractor_left_as_obligation = true
spectral_prediction_left_as_empirical     = true
```

The EntropyForge extension receipt is:

```text
production/formal-papers/CQE-paper-12/verify_center_column_entropy.py
production/formal-papers/CQE-paper-12/center_column_entropy_receipt.json
```

The receipt status is `pass`, with `10/10` finite checks passing. It records
two open obligations:

```text
infinite-column non-periodicity remains a conjecture
statistical-suite certification is product-layer work, not a paper claim
```

## Falsifiers

The verifier rejects:

```text
the spectral layer is a proved cold-start Rule 30 predictor
a local T_EMISSION receipt proves between-depth dynamics without the local state
a layer may omit its cost and defect receipt
finite center-column evidence proves infinite non-periodicity
seeded product streams replace the canonical paper-bound object
```

## Role in the Suite

Paper 11 admits candidate theories through a receipt gate. Paper 12 turns an
admitted cellular automaton candidate into a prediction surface:

```text
admission receipt
-> local CA rule
-> layer stack
-> closed local readout
-> open extraction or empirical layers where required
```

Paper 13 may use the CA correction field as a quark-face transport input, but
must preserve which layer produced the bit and which obligations remain open.
Paper 18 and Paper 29 may reuse the `2 + 6` VOA partition and the Monster
scalar only as finite arithmetic/sector receipts unless a stronger theorem is
supplied.

## Open Audit Boundaries

1. A full cold-start `O(log N)` Rule 30 extractor remains open.
2. The spectral next-state layer is empirical until an accuracy theorem is
   supplied.
3. Case-by-case closure of every silent-boundary rule requires additional
   receipts beyond the count.
4. Any use of a prediction surface must preserve layer, cost, defect, and
   receipt metadata.
5. Infinite center-column non-periodicity remains unproved by this paper.
6. Product-level randomness certification remains outside the paper claim until
   a separate statistical receipt is supplied.

## Conclusion

Paper 12 proves the finite local layer of the cellular-automaton prediction
surface. It gives Rule 30 an exact local readout and correction decomposition,
counts the silent-boundary ECA subset, and keeps cold-start, spectral
prediction, infinite-periodicity, and product-certification claims visible as
open layers rather than hidden conclusions.
