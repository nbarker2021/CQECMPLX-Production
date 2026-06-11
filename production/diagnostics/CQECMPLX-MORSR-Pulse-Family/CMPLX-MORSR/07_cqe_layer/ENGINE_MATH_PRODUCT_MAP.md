# CMPLX-MORSR Engine Math Product Map

| Layer | CMPLX-MORSR Meaning |
|---|---|
| Engine | C centroid pulse, active-node trigger, confirmed reading, recenter x3 |
| Math | E8 240-root pulse, centroid/pode relation, quadratically confirmed extension |
| Product | diagnostic scan, failure/success point finder, active-node report |
| Library | `cmplx.morsr`, `cmplx.nsl`, `cmplx.receipt`, `cmplx.morphon`, `lattice_forge` |
| Datum | only a confirmed reading that cannot bind to an existing morphon/receipt/trace |

## Binding Priority

1. Existing morphon identity.
2. Existing diagnostic trace.
3. Existing receipt chain.
4. Existing MORSR/CQE adapter.
5. New datum only after all bindings fail.
