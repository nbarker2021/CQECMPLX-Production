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

1. `CMPLX-1T`
2. `CMPLX-Monorepo`
3. `CMPLX`
4. `CMPLXUNI`
5. `CMPLXMCP`
6. `CMPLXDevKit`

This order starts with the broad identity root, then compares it against the
existing monorepo and core/runtime surfaces.

