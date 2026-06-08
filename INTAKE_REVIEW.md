# Intake Review

## Repository State

The remote cloned successfully but had no commits at intake time. This makes it
a clean production anchor.

## First Local Branch

`intake/production-kernel-map`

Purpose:

- record the canonical production repo identity;
- map local staging roots into the production family;
- list public git roots pending review;
- define promotion gates before moving code or corpus material.

## Next Review Order

1. `CMPLX-1T` - reviewed; see `reviews/CMPLX-1T_INTAKE_REVIEW.md`
2. `CMPLX-Monorepo` - reviewed; see `reviews/CMPLX-Monorepo_INTAKE_REVIEW.md`
3. `CMPLX` - reviewed; see `reviews/CMPLX_INTAKE_REVIEW.md`
4. `CMPLXUNI` - poised next
5. `CMPLXMCP`
6. `CMPLXDevKit`

This order starts with the broad identity root, then compares it against the
existing monorepo and core/runtime surfaces.

## Current Poised Repo

```text
https://github.com/nbarker2021/CMPLXUNI
```

Expected next branch:

```text
intake/review-for-cqecmplx-production
```
