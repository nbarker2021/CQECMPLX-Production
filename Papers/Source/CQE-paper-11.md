# Paper 11 - Theory Admission Gate

## Abstract

Paper 11 proves the theory admission gate for the CQECMPLX suite. An external
theory is not admitted because it sounds compatible with the framework, and it
is not discarded because a first transport attempt fails. It is evaluated as a
candidate against the carried observer center, the Paper 10 master receipt, a
trusted spectrum, and the `K=9` sheet boundary inherited from the lattice
closure layer.

The admission theorem is:

```text
candidate theory -> T10 anchor -> trusted spectrum -> K=9 boundary
                 -> admitted | boundary | rejected_as_datum
```

The paper also records the Pariah/Happy-Family case as a worked boundary
receipt under the declared bit-length-parity encoder. That worked case is not
a new finite-group classification theorem. It is an encoder-bound admission
and boundary test inside the CQECMPLX receipt system.

## Claims

**Claim 11.1.** A candidate theory is admitted only when it is signed by the
T10 context, its Gluon mass matches the trusted spectrum, and its mass remains
inside `K_max = 9`.

**Claim 11.2.** A trusted match above `K=9` is routed to a boundary receipt,
not admitted.

**Claim 11.3.** A nonmatching candidate is rejected or rejected as datum
according to the declared test. It is not erased.

**Claim 11.4.** The Pariah/Happy-Family worked case is bound to its declared
encoder and cannot be generalized without a new receipt.

## Definitions

The **observer center `C00`** is the center encoded by the requested
enumeration event at the Paper 00 to Paper 01 transition.

The **Paper 10 trust anchor** is:

```text
T10 = (C00, E00->1, P00, P01..P09, R, L, V, O)
```

An **admission Gluon** is the Paper 11 carrier that evaluates a candidate
theory by Gluon mass against a trusted spectrum:

```text
T_ADMISSION = Gluon mass filter at K=9, anchored by T10
```

The **trusted spectrum** for the production verifier is:

```text
S_T10 = {0,1,2,3,4,5,6,7,8,9,10}
```

The **sheet boundary** is:

```text
K_max = 9
```

A **candidate theory** is an external theory, model, proof object, package, or
tool claim being tested for import into the CQECMPLX stack.

An **admission receipt** is:

```text
candidate_id
mass
trusted_match
K_max
T10_anchor
verdict
```

The verdict set is:

```text
admitted
boundary
rejected
rejected_as_datum
```

## Theorem 11.1 - T_ADMISSION

Let `T` be a candidate theory with Gluon mass `m(T)`. Let `S_T10` be the
trusted spectrum exposed by the Paper 10 master receipt, and let `K_max = 9`.
Paper 11 admits `T` if and only if:

```text
T10 signs the admission context
m(T) in S_T10
m(T) <= K_max
```

If the context is T10-signed and `m(T) in S_T10` but `m(T) > K_max`, then `T`
is routed to a boundary receipt. If `m(T) notin S_T10`, or the candidate is
not bound to T10, the candidate is rejected or rejected as datum.

## Proof

Paper 10 proves that `C00`, the `00 -> 1` encoding event, and the receipts for
Papers 00-09 are present in one replayable master object. Therefore Paper 11
has a stable observer center and a stable receipt anchor before evaluating any
external theory.

The admission predicate is:

```text
A(T) = signed_T10(T) and m(T) in S_T10 and m(T) <= 9
```

Each clause is necessary. Without `signed_T10(T)`, the candidate is not being
evaluated inside the carried paper stack. Without `m(T) in S_T10`, the
candidate has no trusted spectrum match. Without `m(T) <= 9`, the candidate
crosses the sheet boundary from the same anchor event.

The three outlets are exhaustive:

```text
signed_T10 and spectrum match and m <= 9 -> admitted
signed_T10 and spectrum match and m > 9  -> boundary
no spectrum match or no T10 context      -> rejected/rejected_as_datum
```

Thus Paper 11 proves an admission gate rather than a narrative preference.

## Worked Boundary Receipt: Pariah and Happy Family

The Pariah/Happy-Family case demonstrates how the gate treats a named
mathematical partition when the candidate data already exists locally.

The local Lattice Forge ledger contains six Pariah objects:

```text
Pariah:J1
Pariah:J3
Pariah:J4
Pariah:Ru
Pariah:ON
Pariah:Ly
```

It also records Monster metadata and local admissibility routes from
`Monster:M` to Pariah nodes. Under the declared encoder:

```text
bit(G) = bit_length(|G|) mod 2
```

the receipt records:

```text
Pariah groups       -> closed signature
Happy Family groups -> open signature
```

The Paper 11 reading is:

```text
Pariah closure while surrounding Monster expansion opens -> boundary receipt
Happy-Family open behavior under this encoder            -> datum/obligation
native closing control with surrounding closure           -> admitted
```

This proves the gate behavior for the declared encoder. It does not reprove
finite simple group classification, and it does not claim encoder
independence.

## Receipt

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py
production/formal-papers/CQE-paper-11/theory_admission_gate_receipt.json
```

The receipt status is `pass`. It verifies:

```text
inherits_t10_observer_center       = true
t10_master_receipt_passes          = true
trusted_spectrum_binds_p00_to_p10  = true
k_max_is_nebe_bound                = true
mass_gate_admits_inside_window     = true
mass_gate_routes_trusted_k10_to_boundary = true
mass_gate_rejects_untrusted_mass   = true
encoder_declared                   = true
pariah_count_is_six                = true
happy_family_count_is_twenty       = true
pariah_signature_closed            = true
happy_family_signature_open        = true
three_outlet_gate_exercised        = true
boundary_receipt_outlets_exercised = true
```

## Falsifiers

The verifier rejects:

```text
a verdict from one declared encoder may be generalized without a new receipt
a theory may enter without T10 trust-anchor receipt
a trusted mass above K=9 is admitted without a boundary receipt
a non-closing candidate is dismissed rather than receipted
the Pariah boundary reading is a new theorem of finite-group classification
Paper 11 can admit external theories without inheriting C00/E00_to_1
```

## Relation to C and the Enumeration Event

Paper 11 evaluates candidates from the already encoded CQECMPLX observer
state:

```text
requested enumeration -> C00 -> E00_to_1 -> T10 -> Paper 11 gate
```

A candidate may later prove a new center, but until it does, the admission gate
evaluates it against the carried center and its inherited receipt context.

## Open Audit Boundaries

1. Candidate-specific Gluon mass functions must be declared before admission.
2. A candidate that claims a new center must prove the recentering and handoff.
3. The Pariah/Happy-Family result is bound to the declared encoder unless a
   later paper supplies encoder-invariance proof.
4. Paper 11 does not reprove finite simple group classification.
5. Individual Happy-Family ledger nodes can be promoted later without changing
   the admission theorem.

## Conclusion

Paper 11 proves the suite's theory admission gate. A candidate enters only
through the T10-anchored Gluon mass filter, inside the `K=9` boundary, against
the trusted spectrum. Boundary crossings and failed encoder tests become
receipt-bearing data rather than erased failures.
