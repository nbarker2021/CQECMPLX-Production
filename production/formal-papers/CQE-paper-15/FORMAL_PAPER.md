# Paper 15 - QFT/Higgs Mass-Residue Carrier

## Abstract

This paper defines the CQECMPLX substrate meaning of a mass-residue carrier. The
closed result is finite and local: Rule 30 splits over `F2` into a linear part
and a bilinear obstruction, the obstruction has Arf invariant `0`, Arf-matching
gluing admits while Arf-mismatch gluing rejects, the chart states split into
`2q^0 + 6q^5` under the VOA weight, and the local correction residue
`C AND NOT R` identifies the states that carry surviving residue.

This is not a derivation of the Higgs mechanism, a particle mass spectrum, or
quantum field theory. The physical reading "mass equals surviving residue
weight" is a candidate interpretation held behind an explicit obligation gate.

## Claims

**Claim 15.1.** Rule 30 decomposes over `F2` as:

```text
Rule30(L,C,R) = (L xor C xor R) xor (C and R)
```

**Claim 15.2.** The bilinear obstruction has Arf invariant `0`, and Arf
matching supplies a finite gluing rule.

**Claim 15.3.** The VOA sector decomposition of the eight chart states is:

```text
Z(q) = 2q^0 + 6q^5
```

**Claim 15.4.** The local correction-residue states are exactly:

```text
(0,1,0), (1,1,0)
```

because those are the states where `C AND NOT R` fires.

**Claim 15.5.** The nth-bit layer passes only as a local/oracle-backed and
partially open layer; McKay-Thompson correction parity remains open.

**Claim 15.6.** Physical Higgs and particle-mass claims remain obligations.

## Definitions

A **carrier effect** is a quantity accepted only when it is witnessed by local
readout and receipt.

The **linear part** of the local Rule 30 formula is `L xor C xor R`.

The **obstruction** is the bilinear term `C and R`.

The **correction residue** is `C and not R`.

A **mass-residue carrier** is the substrate object that survives cancellation,
has a receipt, and carries a weight. It is not a physical rest mass unless a
separate calibrated physical derivation is supplied.

## Theorem 15

The CQECMPLX mass-residue carrier is a finite substrate layer consisting of:

```text
F2 obstruction
-> Arf gluing receipt
-> correction-residue local states
-> VOA weight split
-> open physical obligation
```

## Proof

Exhaust the eight local chart states. For every `(L,C,R)`, the verifier checks:

```text
Rule30(L,C,R) = (L xor C xor R) xor (C and R)
```

This proves Claim 15.1.

The `f2_majorana` verifier reports:

```text
q_zero_arf = 0
q_hyperbolic_arf = 0
q_elliptic_arf = 1
rule30_correction_arf = 0
zero_vs_hyperbolic_can_glue = true
zero_vs_elliptic_can_glue = false
```

Thus the obstruction has Arf invariant `0`; matching Arf classes glue, and
mismatched classes reject. This proves Claim 15.2.

The `centroid_voa` verifier reports exactly two true vacua of weight `0` and
six excited states of weight `5`. Therefore the seed partition function is
`Z(q) = 2q^0 + 6q^5`. This proves Claim 15.3.

The correction-residue function is `C AND NOT R`. Exhausting the eight states
shows that it fires only at `(0,1,0)` and `(1,1,0)`. This proves Claim 15.4.

The nth-bit layer passes at the tested local/oracle level with `oracle_accuracy
= 1.0`, while the receipt still names McKay-Thompson correction parity as an
open step. Therefore the local residue evidence is admitted and the closed-form
parity theorem remains open. This proves Claim 15.5.

No verifier computes the Higgs mechanism, electroweak symmetry breaking,
Yukawa couplings, or measured particle masses. The verifier explicitly keeps
physical Higgs mass as an obligation. This proves Claim 15.6.

Combining the admitted claims proves the theorem.

## Receipt

Promoted verifier:

```text
production/formal-papers/CQE-paper-15/verify_mass_residue_carrier.py
```

Receipt:

```text
production/formal-papers/CQE-paper-15/mass_residue_carrier_receipt.json
```

Closed layers:

```text
Rule 30 splits into linear part xor C*R obstruction over F2
Rule 30 obstruction has Arf invariant 0
Arf-matching gluing admits and Arf-mismatch gluing rejects
VOA sector decomposition is 2q^0 + 6q^5
correction residue C and not R identifies the local surviving-residue states
nth-bit local/oracle layer passes while McKay-Thompson parity remains open
```

Open layers:

```text
physical Higgs mechanism
particle mass spectrum or numerical mass prediction
electroweak symmetry breaking/Yukawa coupling derivation
closed-form McKay-Thompson correction parity
```

## Falsifiers

The paper fails if the Rule 30 split fails on any local state.

It fails if Arf mismatch glues losslessly.

It fails if the VOA split is not two weight-0 vacua and six weight-5 excited
states.

It fails if the correction residue fires anywhere other than `(0,1,0)` and
`(1,1,0)`.

It fails if this receipt is used as a physical Higgs-mass proof.

## Role in the Suite

Paper 14 exports repair score and open physical boundary. Paper 15 receives
that discipline and defines the local residue/weight object that later papers
may carry into continuum, lattice-tower, or energy-bound work.

## Conclusion

Paper 15 closes the substrate mass-residue carrier. It proves obstruction,
Arf gluing, residue firing, and VOA weight. It does not prove the Higgs
mechanism. The result is the necessary carrier layer for later physical
comparison.
