# CQECMPLX Paper Rewrite Status

## Meaning

Every paper belongs in the top-level review package. The current PDF build
covers the full visible suite, but not every paper has been rewritten into the
new final review form yet.

Status meanings:

- `review-source`: top-level source exists in `Papers/Source/`.
- `promoted-formal`: current PDF comes from `production/formal-papers`.
- `fallback-body`: current PDF comes from `production/papers/*/PAPER-BODY.md`
  and still needs a strict rewrite.
- `companion-needed`: `.25`, `.50`, and `.75` support papers still need to be
  written for that interval.

## Current Status

| Paper | Build Source | Rewrite Need |
|---|---|---|
| 0 | review-source | Foreword draft present; polish as corpus front matter. |
| 0.25 | review-source | Toolkit draft present; expand as first-section support. |
| 0.50 | review-source | Claim contract draft present; expand Merkle/link review rules. |
| 0.75 | review-source | Application/precondition draft present; expand examples. |
| 1 | review-source | Strict scientific rewrite present; companion supports drafted. |
| 1.25 | review-source | LCR toolkit supplement present. |
| 1.50 | review-source | LCR claim contract supplement present. |
| 1.75 | review-source | LCR next-state precondition supplement present. |
| 2 | review-source | Strict scientific rewrite present; companion supports drafted. |
| 2.25 | review-source | Correction toolkit supplement present. |
| 2.50 | review-source | Correction claim contract supplement present. |
| 2.75 | review-source | Correction next-state precondition supplement present. |
| 3 | review-source | Strict scientific rewrite present; companion supports drafted. |
| 3.25 | review-source | Triality-surface toolkit supplement present. |
| 3.50 | review-source | Triality-surface claim contract supplement present. |
| 3.75 | review-source | Triality-surface next-state precondition supplement present. |
| 4 | review-source | Strict scientific rewrite present; companion supports drafted. |
| 4.25 | review-source | Boundary-repair toolkit supplement present. |
| 4.50 | review-source | Boundary-repair claim contract supplement present. |
| 4.75 | review-source | Boundary-repair next-state precondition supplement present. |
| 5 | promoted-formal | Rewrite to strict scientific paper form. |
| 6 | promoted-formal | Rewrite to strict scientific paper form. |
| 7 | promoted-formal | Rewrite to strict scientific paper form. |
| 8 | promoted-formal | Rewrite to strict scientific paper form. |
| 9 | promoted-formal | Rewrite to strict scientific paper form. |
| 10 | promoted-formal | Rewrite to strict scientific paper form. |
| 11 | promoted-formal | Rewrite to strict scientific paper form. |
| 12 | fallback-body | Promote from production body into strict scientific paper. |
| 13 | fallback-body | Promote from production body into strict scientific paper. |
| 14 | fallback-body | Promote from production body into strict scientific paper. |
| 15 | fallback-body | Promote from production body into strict scientific paper. |
| 16 | fallback-body | Promote from production body into strict scientific paper. |
| 17 | fallback-body | Promote from production body into strict scientific paper. |
| 18 | fallback-body | Promote from production body into strict scientific paper. |
| 19 | fallback-body | Promote from production body into strict scientific paper. |
| 20 | fallback-body | Promote from production body into strict scientific paper. |
| 21 | fallback-body | Promote from production body into strict scientific paper. |
| 22 | fallback-body | Promote from production body into strict scientific paper. |
| 23 | fallback-body | Promote from production body into strict scientific paper. |
| 24 | fallback-body | Promote from production body into strict scientific paper. |
| 25 | fallback-body | Promote from production body into strict scientific paper. |
| 26 | fallback-body | Promote from production body into strict scientific paper. |
| 27 | fallback-body | Promote from production body into strict scientific paper. |
| 28 | fallback-body | Promote from production body into strict scientific paper. |
| 29 | fallback-body | Promote from production body into strict scientific paper. |
| 30 | fallback-body | Promote from production body into strict scientific paper. |
| 31 | fallback-body | Promote from production body into strict scientific paper. |
| 32 | fallback-body | Promote from production body into strict scientific paper. |

## Companion Paper Requirement

Every interval needs companion support:

```text
N.25 toolkit
N.50 claim contract / linked review
N.75 application as next-state precondition
```

The first interval has drafts for `0.25`, `0.50`, `0.75`, `1.25`, `1.50`,
and `1.75`. Future interval companions remain `companion-needed` until
drafted and built.
