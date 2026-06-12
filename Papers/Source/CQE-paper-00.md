# Paper 0 - Foreword and Burden Statement

## Foreword

My name is Nicholas "Nick" Barker. I am self-trained. I have used AI systems
extensively to help search, organize, test, rewrite, and formalize the work in
this package. I do not ask any reader to weigh my opinion as they would weigh
the judgment of trained academic specialists. The work I am trying to extend
is built on mathematics, physics, computation, and formal methods discovered
and stabilized by people who earned that trust through disciplined training
and public review.

That is why this package is built with an unusually heavy proof burden. I know
that the claims are extraordinary. I also know that an extraordinary claim is
not helped by confidence, style, or a large collection of tools. It is helped
only by clear claims, reproducible tests, explicit assumptions, falsifiers,
receipts, and a willingness to preserve failures as evidence rather than hide
them.

This foreword is therefore not a proof of the system. It is a statement of the
burden under which the system is presented.

## Scope of the Papers

The papers are about the proofs, the mathematics, the sciences, and the
proposed Standard Model extension. Those subjects must remain the focus of
each formal paper.

Each paper also has a silent support layer: tools, kernels, analog workbook
routes, receipts, lib bindings, and validation scripts that let a reader treat
the paper as a testable claim in its own right. Those support systems are not
the replacement for the paper. They are the audit trail behind it.

The review-facing structure is:

```text
paper claim
-> prediction
-> test protocol
-> generated proof or receipt
-> formalization
-> falsifier
-> result
```

The support structure is:

```text
toolkit
-> contract
-> analog exposure
-> kernel or lib binding
-> receipt
-> archive or obligation
```

The first structure is what the paper says. The second structure is how the
reader can test that the paper is not merely saying it.

## Why the Package Continues Past the First Solves

The early papers carry the first central solve sequence. After that point,
many later papers could have been presented as implications, predictions,
follow-up problems, or continuation notes. Instead, I attempted to answer as
many foreseeable questions as I could inside the same package.

Everything after the first solve sequence should be read in that spirit. The
later papers keep extending the same ribbon and center-bar printout. They
re-evaluate the indexed state as new findings are added, and they preserve the
same accounting discipline across each extension.

This does not mean every later extension has the same evidentiary status on
arrival. It means every later extension is forced into the same claim,
receipt, falsifier, and obligation structure.

## The Observer Event

The simplest description of the system is this:

```text
something chooses to look at something else
then records it
then validates it
then thinks about the result
```

In the formal papers this becomes the observer-chosen enumeration event. The
event defines the active center `C`. The state is read around that center. The
left and right boundaries are recorded relative to it. Every claimed
continuation must preserve the accounting of that first choice or explicitly
prove a recentering.

That is the reason for the analog and by-hand requirements. They are not meant
to restrict the reader or impose arbitrary rules. They exist to make the
normally unclear relation between error, state, observer, and boundary visible
to the reviewer. If the same claim can be expressed by a program, a table, a
diagram, a hand-built token sheet, or even marks in dirt, then the claim is
less likely to depend on hidden software theater.

The point is not that every reader must use the analog kit. The point is that
nothing essential should require more than the basic topology of a chosen
center, a recorded boundary, a transform, and a receipt.

## Relation to Physics Language

One concise way to classify the whole package is as an attempt to formalize an
observer term in QCD and then carry its consequences through the adjacent
models. That description may be simpler than saying "a proposed Standard
Model extension that mostly closes the model." The papers themselves must earn
either description through their claims, tests, and results.

For that reason, the review papers should avoid overexplaining the tool
system when the claim is physical, mathematical, or computational. The tools
are there to make the claim testable. The claim must still stand in scientific
form.

## Burden of Review

I ask the reader to review the work by its receipts, not by my credentials and
not by the fact that AI helped produce it. If a claim is unclear, it should be
treated as unclear. If a proof step fails, it should become an obligation. If
a tool produces a result, the result should be checked against the formal
claim and against a simpler exposure route wherever possible.

This is why the corpus keeps the following discipline:

```text
no claim without a stated test
no test without a receipt
no receipt without a source binding
no failure erased as noise
no tool treated as the proof when the paper claims mathematics or physics
```

The purpose of the package is to make the work reviewable.

## Conclusion

Paper 0 is the foreword and burden statement. It explains why the papers are
strict, why the tools exist, why analog exposure matters, why open obligations
remain visible, and why every later claim is forced to carry its own receipt.
The formal work begins after this foreword.
