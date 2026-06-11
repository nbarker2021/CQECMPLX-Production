# Paper 19 - Observer Face-Selection

## Status

Formal refinement draft for peer-review-facing development

## Abstract

This paper states a local transport problem, gives a formal vocabulary for it, binds it to a ForgeFactory/Rhenium tool surface, and supplies an analog workbook sheet. The paper is written as a proof-facing document rather than as a description of how the paper was produced. Build-method details are retained only in appendices, receipts, and the Paper 31 meta-walkthrough.

## Central Thesis

Model observation as face selection with latent alternatives retained as obligations, not deleted.

## Scope Boundary

The paper claims only what its tool, proof tree, citations, and workbook sheet can presently support. Any interpretation that exceeds that support is logged as an obligation rather than silently promoted to proof.

## Definitions

- **C**: the active center of a readout window.
- **L/R**: the two opposed boundary directions read relative to C.
- **Transport row**: a typed record that carries a claim, source, transform, state, and obligation status.
- **Receipt**: a replayable record of an operation, its inputs, outputs, and unresolved obligations.
- **Workbook sheet**: the analog version of the proof state, expressed through color, tokens, string, page, card, and white/black follow-up.
- **Tool binding**: the ForgeFactory module or function family that makes the paper executable or testable.

## Axioms

Axiom 19.1 - Locality: every accepted claim must be readable through a local window before it is lifted to a larger frame.

Axiom 19.2 - Receipt Preservation: no transform is accepted unless its inputs, output, and unresolved residue can be logged.

Axiom 19.3 - Boundary Positivity: failed, partial, or mismatched routes are data. They become obligations or correction surfaces.

Axiom 19.4 - Analog Equivalence: if the claim is part of the main corpus, it must have a physical workbook analogue.

## Lemmas

Lemma 19.1 - If a local state preserves C and records L/R residue, it can be transported into a proof ledger without erasing unresolved alternatives.

Lemma 19.2 - If a tool output and workbook sheet encode the same center, boundary, and obligation state, they are equivalent receipts at different media layers.

Lemma 19.3 - A practical example is valid for this paper only when it demonstrates the same operation in a non-toy domain.

## Formalism / Calculus Sketch

Let a paper state be P = (C, L, R, B, T, O), where C is the center, L and R are boundary readouts, B is the boundary rule, T is the tool transform, and O is the obligation set.

A local transform is accepted when:

```text
T(P_in) -> P_out
receipt(P_in, T, P_out, O) exists
C_out is defined
unresolved residue is in O rather than erased
```

For Paper 19, the tool binding is:

```text
forgefactory.paper19_observer_faces
```

## Proof Tree

```text
claim
-> local window
-> boundary read
-> tool transform
-> practical example
-> workbook analogue
-> receipt
-> proof / obligation split
```

## Practical Solved Example

**Domain:** camera angle in inspection: unseen sides are obligations, not nonexistent.

**Procedure:** define a center, identify left/right or equivalent boundary states, run or simulate the tool transform, record any failed or incomplete path as an obligation, and export a receipt.

**Solved Output:** the example is solved when the operator can reproduce the same state transition from the formal paper, the ForgeFactory tool, and the analog workbook sheet.

## Tool Binding

- Module: `forgefactory.paper19_observer_faces`
- Required outputs: `receipt.json`, `workbook_sheet.json`, `example_result.json`, `obligation_ledger.csv`.
- Minimum test: a smoke test that produces at least one proof-like row and one obligation-like row.

## Analog Workbook Sheet

- Start with grey loose substrate.
- Place C token at the local center.
- Mark active color gradients: red, green, blue minimum.
- Use string to bind the main route.
- Use white follow-up for proof continuation.
- Use black follow-up for obligation or unresolved residue.
- Bind the final sheet into the matching color notebook.

## IRL Citation Anchors

- [Shannon1948] Shannon, C. E. (1948). A Mathematical Theory of Communication. URL: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf Use: information channel, encoding, receiver, noise, state transmission.

## Open Obligations

- Replace citation anchors with final bibliography entries during peer-review preparation.
- Expand the tool binding from stub/registry level to executable tests where not yet implemented.
- Add one domain expert critique pass.
- Add one falsifier case that the tool must reject or defer.

## Back-Propagation Targets

- Paper 00 receives any new contract term needed here.
- ForgeFactory registry receives or updates `forgefactory.paper19_observer_faces`.
- The analog workbook manual receives any new sheet rule required by this paper.
- Paper 31 records how this paper's presentation order demonstrates the same LCR process.


---