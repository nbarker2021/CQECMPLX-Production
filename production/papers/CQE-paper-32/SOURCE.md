# Paper 32 - Superpermutation Dimensional Schedule

## Status

Applied-layer paper opening the 32+ series. Proof-facing draft with explicit obligations.

## Abstract

This paper states a local transport problem, gives a formal vocabulary for it, binds it to a ForgeFactory/GraphStax tool surface, and supplies an analog workbook sheet. The paper is written as a proof-facing document rather than as a description of how the paper was produced. Build-method details are retained only in appendices, receipts, and the Paper 31 meta-walkthrough.

## Central Thesis

Read the shortest string that contains every permutation of n symbols (the minimal superpermutation) as the minimal schedule for enumerating an n-dimensional reading, and show that solving each successive n carries the complexity into the local length-n charts.

## Scope Boundary

The paper claims only what its tool, proof tree, citations, and workbook sheet can presently support. The minimal lengths for n less than or equal to 5 are cited as established results; the n greater than or equal to 6 statements are bounds and construction records, not minimality proofs. Any interpretation that exceeds that support is logged as an obligation rather than silently promoted to proof.

## Definitions

- **C**: the active center of a readout window.
- **L/R**: the two opposed boundary directions read relative to C.
- **Enumeration request**: a cursor position on the superpermutation string; the act that asks for one ordering of the n symbols to be read now.
- **Local chart**: a length-n window of the superpermutation string — the ordering currently visible at the cursor.
- **Transport row**: a typed record that carries a claim, source, transform, state, and obligation status.
- **Receipt**: a replayable record of an operation, its inputs, outputs, and unresolved obligations.
- **Workbook sheet**: the analog version of the proof state, expressed through color, tokens, string, page, card, and white/black follow-up.
- **Tool binding**: the GraphStax module that makes the paper executable or testable.

## Axioms

Axiom 32.1 - Locality: every accepted claim about the schedule must be readable through a single length-n window before it is lifted to a larger frame.

Axiom 32.2 - Receipt Preservation: no construction step is accepted unless its inputs, output string, and coverage residue can be logged.

Axiom 32.3 - Boundary Positivity: a length below the best known construction is not a failure; it is an open corridor recorded as an obligation.

Axiom 32.4 - Analog Equivalence: the schedule must have a physical workbook analogue — a string drawn on a sheet with a sliding window.

## Lemmas

Lemma 32.1 - Coverage is local: a string is a superpermutation for n iff every length-n window, read across the whole string, collectively realizes all n! orderings. Coverage is checked window by window.

Lemma 32.2 - The N to N+1 lift is chart-threaded: threading the symbol n+1 through every length-n chart in visit order, with maximal overlap, yields a superpermutation of length the sum of k! for k = 1..n+1.

Lemma 32.3 - The example is valid only in a non-toy domain: the n=4 service-wiring schedule and the n=8 ribbon-slot schedule are the required demonstrations, not a symbolic toy.

## Formalism / Calculus Sketch

Let a schedule state be P = (C, L, R, B, T, O), where C is the symbol at the cursor, L and R are the neighboring window content, B is the coverage rule, T is the lift transform, and O is the obligation set (the open corridor).

A lift is accepted when:

```text
T(P_in) -> P_out                         lift scale n to n+1
receipt(P_in, T, P_out, O) exists        construction logged
coverage_check(P_out, n+1) is true       every permutation appears
open corridor recorded in O              floor-to-ceiling gap, not erased
```

The dimensional reading: an ordering of n symbols is one way to read n slots off the tape; the set of all orderings is the action graph at dimension n (n! vertices); the minimal superpermutation is that graph serialized onto one tape with maximal overlap. For Paper 32, the tool binding is:

```text
graphstax.permforge
```

## Proof Tree

```text
claim (minimal schedule at scale n)
-> local window (length-n chart)
-> coverage read (all n! orderings appear)
-> lift transform (n -> n+1, chart-threaded)
-> practical example (n=4 services, n=8 ribbon)
-> workbook analogue (string + sliding window on a sheet)
-> receipt (lengths, coverage, corridor)
-> proof / obligation split (minimal for n<=5; corridor open for n>=6)
```

## Practical Solved Example

**Domain:** the 8-slot ribbon (C, L, R, B, T, O, W, A) whose every read-ordering must be scheduled, and the n=4 block of four services wired by the unique minimal n=4 schedule.

**Procedure:** build the schedule from a single symbol by the chart-threaded lift, verify coverage at each scale, and compare the result against the established bounds.

**Solved Output:**

- The chart-walk construction, built live from "1", gives lengths 1, 3, 9, 33, 153, 873, 5913, 46233 — the sum of k! at each rung — with full coverage verified at every rung.
- At n=4 the minimal schedule is unique and palindromic, length 33, covering all 24 orderings (the wiring pattern for a block of four services).
- At n=5 there are exactly 8 minimal schedules of length 153 (one palindrome, seven trees).
- At n=8 the best known schedule has length 46205, covering all 40320 orderings — verified against the field record — and equals the Egan construction formula exactly. The proven floor is 46085; the open corridor is 120 = 5! symbols wide.

The example is solved when the operator can reproduce each length and each coverage result from the formal paper, the GraphStax tool, and the analog workbook sheet.

## Tool Binding

- Module: `graphstax.permforge`
- Required outputs: `receipt.json` (lengths + coverage + corridor), `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: `coverage_check` passes for n=4..8 against the shipped strings, and `recursive_construction(8)` reproduces length 46233 with full coverage.

## Analog Workbook Sheet

- Start with grey loose substrate.
- Write the schedule string left to right; the C token is whatever symbol the cursor sits on.
- Slide a length-n cutout window along the string; each placement is one local chart.
- Mark active color gradients: red, green, blue minimum — one per newly seen ordering.
- Use string to bind the main route (the schedule).
- Use white follow-up for a covered ordering (proof continuation).
- Use black follow-up for the open corridor (obligation or unresolved residue).
- Bind the final sheet into the matching color notebook.

## IRL Citation Anchors

- [Chaffin2014] B. Chaffin, reported by N. Johnston: minimal superpermutations on 5 symbols (length 153, eight solutions). URL: https://www.njohnston.ca/2014/08/all-minimal-superpermutations-on-five-symbols-have-been-found/ Use: n=5 minimality and the octad.
- [Houston2014] R. Houston: a superpermutation on 6 symbols shorter than the recursive construction (872 < 873). Use: the recursive construction is not minimal for n >= 6.
- [HPV2018] R. Houston, J. Pantone, V. Vatter: a lower bound on the length of the shortest superpermutation. URL: https://oeis.org/A180632/a180632.pdf Use: the floor n! + (n-1)! + (n-2)! + n - 3.
- [Egan2018] G. Egan: superpermutations (upper-bound construction). URL: https://www.gregegan.net/SCIENCE/Superpermutations/Superpermutations.html Use: the ceiling n! + (n-1)! + (n-2)! + (n-3)! + n - 3 and search records.

## Open Obligations

- The n=8 corridor: 120 symbols between the floor 46085 and the construction 46205. Transport Egan's n=7 search methods (kernel graphs over the 2-cycle/3-cycle quotient) to n=8 inside this format and record any string below 46205 with a coverage receipt.
- Ship the sub-formula search records at n=6 (872) and n=7 (5906) as field data alongside the construction records, each with a coverage receipt.
- Add one falsifier case the tool must reject (a string that misses at least one ordering) and confirm `coverage_check` defers it.
- Replace citation anchors with final bibliography entries during peer-review preparation.

## Back-Propagation Targets

- Paper 00 receives any new contract term needed here (the enumeration-request reading of C).
- Paper 16 (Continuum Edge Residuals) receives the power-of-ten ladder framing of the factorial walk.
- ForgeFactory / GraphStax registry receives or updates `graphstax.permforge`.
- The analog workbook manual receives the sliding-window sheet rule.
- Paper 31 records how this paper's presentation order demonstrates the same LCR process.
