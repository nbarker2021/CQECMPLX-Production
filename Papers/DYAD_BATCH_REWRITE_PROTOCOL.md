# CQECMPLX Dyad Batch Rewrite Protocol

## Purpose

The paper rewrite is a batch synthesis task. Each block is reviewed through
mirrored dyads so that edge, wrap, and back-propagation relationships stay
visible while the final papers are rewritten.

The agents produce evidence briefs. The final review-facing papers are written
from those briefs plus the current repo evidence, receipts, verifiers, and
source bodies.

## Block Pattern

Each 8-paper block is assigned to four dyad reviews:

```text
first with last
second with seventh
third with sixth
fourth with fifth
```

For the four active paper windows:

```text
Block 01:  1/8,   2/7,   3/6,   4/5
Block 02:  9/16, 10/15, 11/14, 12/13
Block 03: 17/24, 18/23, 19/22, 20/21
Block 04: 25/32, 26/31, 27/30, 28/29
```

This ordering is intentional. It forces each paper to be read with the paper
that closes, reflects, or pressure-tests its role inside the block.

## Agent Brief Requirements

Each dyad agent must produce a brief with:

```text
1. Integer-paper claim focus for each paper.
2. Proof and evidence files.
3. Verifier and receipt status.
4. What belongs in the integer paper.
5. What belongs in .25 toolkit companion material.
6. What belongs in .50 claim-contract / linked-review material.
7. What belongs in .75 next-state / precondition material.
8. Cross-links between the dyad papers.
9. Open obligations and falsifiers that must not be hidden.
10. Recommended final-paper structure.
```

Agents do not decide final wording. They identify evidence and rewrite
requirements. The main paper pass synthesizes the final paper.

Agents may draft structure, claim focus, and suggested language, but their
output is not the paper format. The user's instructions and the agent briefs
are design constraints and evidence maps. The final review papers must be
assembled by the main synthesis pass using scientific judgment, logical
ordering, proof discipline, and formal writing.

## Main Rewrite Pass

For each paper, the main pass writes:

```text
Papers/Source/CQE-paper-NN.md
```

as a strict scientific paper:

```text
abstract
claims
predictions
definitions
test protocol
results
theorems and proofs
falsifiers
scope boundary
evidence bindings
conclusion
```

The main pass must not paste a dyad brief into a paper as if aggregation were
authorship. It must decide:

```text
what the paper actually proves
what is only support material
what is an implication or cross-link
what is an open obligation
what wording is professionally review-facing
```

For each interval needing support, the main pass writes:

```text
Papers/Source/CQE-paper-NN.25.md
Papers/Source/CQE-paper-NN.50.md
Papers/Source/CQE-paper-NN.75.md
```

as companion supports:

```text
.25 = toolkit
.50 = claim contract / Merkle-style linked review
.75 = next-state precondition / application of prior results
```

## Separation Rule

Integer papers carry the scientific claim. They must not be crowded by
toolkit narration, analog kit explanation, process backstory, or construction
diary.

Companion papers carry the support layer: analog tools, kernels, lib-forge
bindings, hidden-guess diagnostics, reader-facing review methods, and
cross-paper usage rules.

## Evidence Rule

No source material is discarded. Evidence is classified as:

```text
paper claim material
companion support material
proof/verifier/receipt
tool/lib/kernel binding
archive-only historical record
duplicate/composite candidate
open obligation
```

If two sources say the same thing, the final paper should synthesize a
composite claim and retain source traceability.

## Review Pass

After each block is rewritten, a final review pass checks:

```text
1. Each integer paper is proof-first and scientifically readable.
2. Each companion paper holds support material instead of polluting the integer paper.
3. Dyad cross-links are named but not overclaimed.
4. Falsifiers and obligations remain visible.
5. Verifier receipts still pass or are marked as missing/needed.
6. PDFs rebuild and open successfully.
```

## Current Batch

Active first batch:

```text
Agent A: Papers 1/8
Agent B: Papers 2/7
Agent C: Papers 3/6
Agent D: Papers 4/5
```

Next batches use the same pattern for the remaining blocks.

Returned briefs are stored in:

```text
Papers/DyadBriefs/
```
