# Paper 23.50 - FoldForge Claim Contract

## Admission Rule

A Paper 23 claim is admitted only when it is framed as a fold descriptor unless
PDB, experimental, or validated simulation evidence is attached. A descriptor
must include a residue chart, contact-map receipt, candidate bifurcation list,
winding evidence, open obligations, and a falsifier.

## Required Fields

Each admitted descriptor must provide:

- protein or peptide identifier,
- residue sequence,
- residue encoding rule,
- complete local-window count,
- contact predicate,
- contact-map receipt,
- candidate bifurcation list,
- winding or topology descriptor,
- substrate verifier status,
- open biological obligations,
- falsification rule.

## Rejected Promotions

The following promotions are not allowed:

- contact map to native structure,
- candidate bifurcation to real turn without structure comparison,
- bounded winding trace to all-depth extractor,
- hydrophobic encoding to full physicochemical model,
- descriptor receipt to fold-rate proof,
- descriptor receipt to AlphaFold parity,
- workbook bead model to biological validation.

## Falsifiers

The descriptor is falsified if its contact map cannot be replayed, if symmetry or
zero-diagonal conditions fail, if its local-window count is wrong, if the winding
receipt loses its open-gap label, or if PDB comparison shows no correlation
between the claimed descriptor and the target topology under a representative
test set.

## Carry Rule

Later papers may import FoldForge as a descriptor pattern. They inherit its open
obligations unless they provide a stronger domain receipt.
