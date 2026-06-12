# CQECMPLX Review Papers

This top-level directory is the review-facing paper package for the repo.

The production folders hold evidence: source extracts, kernels, receipts,
workbook reconstructions, tool bindings, and package code. The papers here are
the clean scientific artifacts generated from that evidence.

Build the current promoted paper PDFs:

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
