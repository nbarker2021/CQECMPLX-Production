# Paper 12.25 - Toolkit for the CA Prediction Surface

## Purpose

Paper 12.25 describes the tools for reviewing the cellular-automaton
prediction surface. These tools expose local readout, correction
decomposition, silent-boundary counting, and layer receipts.

## Review Objects

The toolkit works with:

```text
ECA rule number
LCR state
local emission
T_EMISSION
Rule90 base
correction field
silent-boundary flag
prediction surface layer receipt
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-12/verify_ca_prediction_surface.py
production/formal-papers/CQE-paper-12/ca_prediction_surface_receipt.json
```

Related historical and package evidence:

```text
D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\rule30_nth_bit.py
D:\CQE_CMPLX\CMPLX-R30-main\PROOF\src\lattice_forge\rule30_predictor.py
production/papers/CQE-paper-12/02-CQE-tool/TOOL.md
production/papers/CQE-paper-12/03-CQE-workbook/WORKBOOK.md
```

The promoted verifier in this repo is the authority for the closed Paper 12
claim.

## Analog Toolkit

A physical reconstruction requires:

- eight LCR rows,
- one ECA truth table,
- one correction column,
- one layer receipt row.

Procedure:

```text
write all eight LCR states
compute Rule30 = L xor (C or R)
compute T_EMISSION
compute Rule90 = L xor R
compute correction = C and not R
check Rule30 = Rule90 xor correction
count silent-boundary rules by fixing f(000)=0 and f(111)=0
mark cold-start and spectral layers as open unless separately verified
```

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
How many LCR states are checked?
How many silent-boundary ECAs exist?
Does T_EMISSION prove cold-start depth-N extraction?
Is the spectral layer proved or empirical here?
```

Expected answers:

```text
8
64
no
empirical
```

## Boundary

Paper 12.25 is a toolkit supplement. Any cold-start extractor, spectral
accuracy theorem, or universal closure theorem must pass Paper 12.50's claim
contract before changing the scientific paper.
