# Paper 8.25 - Toolkit for the Lattice Closure Template

## Purpose

Paper 8.25 describes the tools for reviewing the local lattice closure
template. These tools expose the code/lattice checks and their audit
boundaries; they do not close Leech or Gamma72 landing claims.

## Review Objects

The toolkit works with:

```text
chain rung             = 1, 3, 7, 8, 24
powered terminal       = 72 = 8 x 9
Fano/Hamming check      = dimension 7 incidence
extended Hamming check  = dimension 8 E8 seed
Golay ingredient check  = dimension 24 carrier
Gamma72 transport check = three-sheet round trip
audit boundary          = unproved landing or uniqueness claim
```

## Digital Toolkit

Primary executable files:

```text
production/formal-papers/CQE-paper-08/verify_lattice_closure_template.py
production/formal-papers/CQE-paper-08/lattice_closure_template_receipt.json
```

The verifier imports:

```text
lattice_forge.lattice_codes.verify_lattice_code_chain
lattice_forge.lattice_codes.verify_hamming_7_fano
lattice_forge.lattice_codes.verify_extended_hamming_8
lattice_forge.lattice_codes.verify_golay_24
lattice_forge.lattice_codes.verify_powered_chain
lattice_forge.nebe_gamma72.verify_nebe_gamma72_contract
```

Additional source and kernel files:

```text
production/papers/CQE-paper-08/SOURCE.md
production/papers/CQE-paper-08/01-CQE-formal/FORMAL.md
production/papers/CQE-paper-08/02-CQE-tool/TOOL.md
production/papers/CQE-paper-08/03-CQE-workbook/WORKBOOK.md
production/paper-kernels/papers/CQE-paper-08/PAPER_KERNEL.md
```

The kernel notes currently mark `production/papers/CQE-paper-08/02-CQE-tool/run.py`
as missing, so the promoted verifier is the replayable route for this paper.

## Analog Toolkit

A physical reconstruction can be done as a rung table:

```text
write the rungs 1, 3, 7, 8, 24, 72
record the certified fact for each rung
mark which facts are local and verified
mark which landings are open audit boundaries
draw 24 as three blocks of 8
draw 72 as eight sheets of nine or nine copies of eight
```

The purpose is not to reproduce all code theory by hand. The purpose is to
make the proof boundary visible.

## Hidden-Guess Diagnostics

When training mode is enabled, diagnostic review should ask for a prediction
before revealing the receipt:

```text
What is the powered terminal of 8 x 9?
Does Golay ingredient evidence prove the rootless Leech landing?
Does Gamma72 round-trip transport prove the polarization action?
What is the sheet K bound?
```

Expected answers:

```text
72
no
no
9
```

## Boundary

Paper 8.25 is a toolkit supplement. Any stronger Leech, Gamma72, or uniqueness
claim must pass Paper 8.50's claim contract before it can change the
scientific paper.
