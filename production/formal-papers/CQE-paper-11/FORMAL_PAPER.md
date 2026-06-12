# Paper 11 - Theory Admission Gate

## Abstract

Paper 11 proves the admission rule for importing an external theory into the
CQECMPLX stack. An outside theory is not accepted because it is rhetorically
similar to the framework, and it is not discarded because a first transport
attempt fails. It is tested as a candidate against the carried observer center,
the Paper 10 master receipt, the trusted Gluon spectrum, and the `K=9` sheet
boundary inherited from the lattice closure layer.

The proof-carrying result is `T_ADMISSION`: the admission Gluon is a Gluon
mass filter at `K=9`, anchored by the Paper 10 master receipt. A candidate is
admitted only when its mass matches the trusted spectrum and remains inside the
`K_max = 9` window. A trusted match outside that window is a boundary receipt,
not an admission. A nonmatching candidate is rejected as a datum, not erased.

The Pariah/Happy-Family case is included as a worked boundary receipt. The
local Lattice Forge ledger already carries the Monster/Pariah structure: the
Monster metadata records the 20 Monster-involved group bulk, the six Pariah
objects are ledger objects, and the Pariah routes are materialized as
admissibility/morphism paths. Under the declared bit-length-parity encoder,
the Pariah set closes while the Happy Family set remains open. That worked
case shows how Paper 11 converts failure, closure, and boundary collision into
typed receipts.

## Proof/Exposure Hierarchy

The primary proof is the admission theorem. Paper 00 supplies the inherited
minimum contract and the original requested enumeration event. Paper 10 binds
that event into the master receipt. Paper 11 then proves the next operation:
how a new theory is tested against the already carried center without silently
moving the center or importing unreceipted claims.

Workbook routes, analog reconstructions, and open-obligation ledgers are
validation and exposure layers. They are valuable because they make the proof
inspectable and reproducible, but the result of this paper is not that a human
can do the system by hand. The result is the formal gate:

```text
candidate theory -> T10 anchor -> trusted spectrum -> K=9 boundary
                 -> admitted | boundary | rejected-as-datum
```

## Definitions

The **observer center `C00`** is the center encoded by the requested
enumeration event at the Paper 00 to Paper 01 transition. Paper 11 inherits
this center through the Paper 10 master receipt unless a later paper explicitly
proves a recentering.

The **step `00 -> 1` encoding event** is the first active encoding of the
Paper 00 burden contract into the paper stack. Paper 11 does not restart the
stack; it reads candidates as consequences of that original encoded request.

The **Paper 10 trust anchor** is the receipt:

```text
T10 = (C00, E00->1, P00, P01..P09, R, L, V, O)
```

where `R` is the transport table, `L` is the lookup cache, `V` is the verifier
verdict, and `O` is the visible open-boundary set.

An **admission Gluon** is the Paper 11 carrier that evaluates a candidate
theory by Gluon mass against a trusted spectrum. In the local corpus this is
registered as:

```text
T_ADMISSION: Admission Gluon = Gluon mass filter at K=9; T10 = trust anchor
```

The **trusted spectrum** is the finite mass set exposed by the receipt-bearing
stack available to Paper 11. The production verifier binds the current Paper
11 spectrum to the Paper 00 through Paper 10 receipt indices:

```text
S_T10 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

The **sheet boundary** is:

```text
K_max = 9
```

This is the Nebe/lattice window used throughout the corpus as the maximum
sheet depth expressible from one anchor event before the candidate must be
reported as a boundary crossing.

A **candidate theory** is any external theory, model, proof object, package,
or tool claim being tested for import into the CQECMPLX stack.

An **admission receipt** is the typed verdict produced by the gate:

```text
(candidate_id, mass, trusted_match, K_max, T10_anchor, verdict)
```

The verdict set is:

```text
admitted
boundary
rejected
rejected_as_datum
```

## Main Claim

**Theorem 11.1, T_ADMISSION.** Let `T` be a candidate theory with Gluon mass
`m(T)`. Let `S_T10` be the trusted spectrum exposed by the Paper 10 master
receipt, and let `K_max = 9`. Paper 11 admits `T` if and only if:

```text
T10 signs the admission context
m(T) in S_T10
m(T) <= K_max
```

If `T10` signs the context and `m(T) in S_T10` but `m(T) > K_max`, then `T`
is routed to a boundary receipt. If `m(T) notin S_T10`, or if the candidate is
not bound to the T10 context, the candidate is rejected or rejected as a datum
according to the declared test.

### Proof

Paper 10 proves that `C00`, the `00 -> 1` encoding event, and the receipts for
Papers 00-09 are present in one replayable master object. Therefore Paper 11
has a stable observer center and a stable receipt anchor before it evaluates
any external theory. Admission without that anchor would be a center move with
no accounting, so it is rejected by construction.

The admission Gluon is defined as a filter over candidate mass. Its acceptance
predicate is:

```text
A(T) = signed_T10(T) and m(T) in S_T10 and m(T) <= 9
```

These three clauses are necessary. Without `signed_T10(T)`, the candidate is
not being evaluated inside the carried paper stack. Without `m(T) in S_T10`,
the candidate has no trusted spectrum match. Without `m(T) <= 9`, the
candidate crosses the sheet boundary and cannot be admitted from the same
anchor event.

They are also sufficient for Paper 11 admission: a candidate with the T10
anchor, a trusted-spectrum mass, and a mass inside `K=9` is exactly the object
the admission Gluon is defined to pass. Therefore the gate is closed under the
three predicates.

The remaining cases are exhaustive and disjoint:

```text
signed_T10(T) and m(T) in S_T10 and m(T) <= 9  -> admitted
signed_T10(T) and m(T) in S_T10 and m(T) > 9   -> boundary
m(T) notin S_T10 or no T10 context             -> rejected/rejected_as_datum
```

Thus Paper 11 proves a real admission rule rather than a narrative preference.
QED.

## Worked Boundary Receipt: Pariah and Happy Family

The Pariah/Happy-Family case supplies the concrete boundary example. It does
not replace the theorem above; it demonstrates how the theorem treats a named
mathematical partition when the candidate data already exists locally.

The local Lattice Forge ledger contains:

```text
Monster:M metadata:
  sporadic_partition = "20 Monster-involved + 4 structural pariahs + 2 hard pariahs"

Pariah objects:
  Pariah:J1
  Pariah:J3
  Pariah:J4
  Pariah:Ru
  Pariah:ON
  Pariah:Ly
```

It also carries route evidence:

```text
Monster:M -> Pariah:J1
Monster:M -> Pariah:J3
Monster:M -> Pariah:ON
Monster:M -> Pariah:Ru

Pariah:{J1,J3,ON,Ru} -> Pariah:{J4,Ly}
```

Those are the local conjugation/admissibility paths used by the verifier. The
Monster record supplies the Happy-Family bulk as the 20 Monster-involved
portion of the partition; the six Pariah groups are separate ledger nodes with
prime profiles and construction status rows.

Under the declared bit-length-parity encoder:

```text
bit(G) = bit_length(|G|) mod 2
```

the R30 theorem registry records `T_D4_5`:

```text
Pariah groups      -> res^2 = 0,     dominant chain e -> e -> e, closed
Happy Family groups -> res^2 = 4/9,  open, non-idempotent
```

The Paper 11 reading is therefore:

```text
Pariah closure while surrounding Monster expansion opens -> boundary receipt
Happy-Family open behavior under this encoder             -> datum/obligation
Native closing control with surrounding closure            -> admitted
```

This proves the boundary mechanism used by the admission gate. It does not
need to reprove the classification of finite simple groups; that
classification is an imported mathematical input. What Paper 11 proves is the
CQECMPLX role of the partition under the declared encoder and the T10-anchored
admission rule.

## Relation to C and the Enumeration Event

Paper 11 is one of the first places where it becomes easy to lose the center.
The candidate theory has its own internal identity, but the admission question
is not asked from inside that candidate. It is asked from the already encoded
CQECMPLX observer state:

```text
requested enumeration -> C00 -> E00_to_1 -> T10 -> Paper 11 gate
```

Every admission verdict is an effect of that chain. A candidate may later
prove a new center, but until it does, the admission gate evaluates it against
the carried center. This is both accounting and mathematics: the observer
request is the encoded event that defines which spectrum, boundary, and receipt
context the candidate is allowed to touch.

## Falsifiers

The verifier rejects these overclaims:

```text
"A theory may enter without the T10 trust anchor"
"A trusted mass above K=9 is admitted without a boundary receipt"
"A nonmatching candidate is deleted rather than receipted"
"A verdict from one declared encoder may be generalized without a new receipt"
"The Pariah boundary reading is a new finite-group classification theorem"
"Paper 11 can ignore C00/E00_to_1"
```

The theorem passes because it admits only the T10-signed, spectrum-matched,
inside-window case and records every other case as a typed receipt.

## Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py
```

It emits:

```text
production/formal-papers/CQE-paper-11/theory_admission_gate_receipt.json
```

The verifier checks:

```text
1. Paper 11 inherits C00/E00_to_1 through the Paper 10 master receipt.
2. The T10 receipt passes.
3. The trusted spectrum binds Paper 00 through Paper 10.
4. K_max is 9.
5. The mass gate exercises admitted, boundary, and rejected outcomes.
6. The local Lattice Forge ledger carries six Pariah objects.
7. The local Monster metadata records the 20 Monster-involved + 6 Pariah split.
8. Structural Pariah exit routes and hard-wall routes are present locally.
9. The Pariah signature closes under the declared encoder.
10. The Happy-Family signature remains open under the declared encoder.
11. Boundary failures are retained as receipts instead of being erased.
```

## Open Audit Boundaries

1. Candidate-specific Gluon mass functions must be declared before admission.
2. A candidate that claims a new center must prove the recentering and handoff.
3. The Pariah/Happy-Family result is bound to the declared encoder unless a
   later paper supplies a broader encoder-invariance proof.
4. The local ledger records the Monster-involved Happy-Family bulk through
   Monster metadata; individual Happy-Family object nodes can be promoted
   later without changing the gate theorem.
5. Paper 11 does not reprove finite simple group classification. It imports
   that classification as mathematical input and proves the CQECMPLX admission
   and boundary role.

## Conclusion

Paper 11 closes the admission problem for this stage of the stack. A candidate
theory enters only through the T10-anchored Gluon mass filter, inside the
`K=9` boundary, against the trusted spectrum. Boundary crossings and failed
encoder tests are not discarded; they become receipt-bearing data. The result
is therefore proof-first: the observer center, the T10 anchor, the mass
predicate, the K-boundary, the local Lattice Forge Pariah routes, and the
boundary receipt logic all appear in one replayable formal object.
