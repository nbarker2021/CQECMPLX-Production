# Paper 11.25 - Toolkit for the Theory Admission Gate

## Purpose

Paper 11.25 describes the tools for reviewing the theory admission gate. These
tools expose candidate admission, boundary routing, rejected-as-datum behavior,
and the Pariah/Happy-Family worked boundary receipt.

## Review Objects

The toolkit works with:

```text
candidate theory
T10 trust anchor
Gluon mass
trusted spectrum
K_max = 9
declared encoder
admission receipt
verdict
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-11/verify_theory_admission_gate.py
production/formal-papers/CQE-paper-11/theory_admission_gate_receipt.json
```

Primary bindings:

```text
T_ADMISSION
lattice_forge.ledger.build_seed_database
CMPLX-Kernel/lib-forge/part1_constants.py
CMPLX-Kernel/lib-forge/part2_steps.py
```

The promoted verifier is the replayable route for this paper. The kernel notes
currently mark `production/papers/CQE-paper-11/02-CQE-tool/run.py` as missing.

## Analog Toolkit

A physical reconstruction can be done as a three-outlet sorter:

```text
write the candidate on a card
write the declared encoder
write the candidate mass
check T10 anchor
check trusted spectrum membership
check K <= 9
place the card in admitted, boundary, or rejected-as-datum
write a receipt for the outlet
```

Rejected-as-datum cards are not thrown away. They are routed to an obligation
folder with the encoder and failed condition recorded.

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
Does a candidate enter without T10?
What happens to a trusted mass at K=10?
Can a non-closing candidate be erased?
Can the Pariah encoder result be generalized without a new receipt?
```

Expected answers:

```text
no
boundary
no
no
```

## Boundary

Paper 11.25 is a toolkit supplement. Any new admitted theory family,
candidate-specific mass function, or encoder-invariance claim must pass Paper
11.50's claim contract before changing the scientific paper.
