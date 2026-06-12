# CQECMPLX Review Papers

This top-level directory is the review-facing paper package for the repo.

The papers are the thing being shown. The production folders hold evidence:
source extracts, kernels, receipts, workbook reconstructions, tool bindings,
and package code. Those materials are used to build, validate, and reproduce
the papers, but they are not the review-facing substitute for the papers.

Canonical review sources live in:

```text
Papers/Source/
```

Generated review PDFs live in:

```text
Papers/PDF/
```

## Paper Sequence

The sequence uses main papers and companion quarter papers.

```text
Paper 0     Foreword and burden statement
Paper 0.25  Toolkit for the upcoming section
Paper 0.50  Claim-validation contract and Merkle/link review layer
Paper 0.75  Application of prior tools/results as next-state preconditions
Paper 1     First strict scientific paper
Paper 1.25  Paper 1 toolkit supplement
Paper 1.50  Paper 1 contract/review supplement
Paper 1.75  Paper 1 application/precondition supplement
Paper 2     Next strict scientific paper
```

The quarter papers are not filler. They are where toolkits, analog methods,
kernels, lib-forge data, narrative aids, and reader-facing review support are
allowed to live. The integer papers should remain scientific papers: abstract,
claims, predictions, tests, proof generation, formalization, falsifiers,
results, and references.

## Production Rule

No source material is discarded until its value has been extracted. Scattered
workspace material is first inventoried, then promoted into either:

- a review paper,
- a quarter-paper supplement,
- an evidence receipt,
- a tool/lib binding,
- an archive record,
- or an explicit obligation.

The goal is not to hide the tools. The goal is to keep the papers themselves
focused on the math, sciences, proofs, and Standard Model extension claims,
while making every claim testable through visible supporting machinery.

Build the current paper PDFs. The builder uses `Papers/Source/` first, then
falls back to promoted formal papers and production paper bodies so the full
0-32 suite stays visible while rewrites continue:

```powershell
python Papers/build_review_pdfs.py
```

Build one paper:

```powershell
python Papers/build_review_pdfs.py --paper CQE-paper-11
```

Outputs are written to:

```text
Papers/PDF/
```
