# Paper 07 - Discrete-Continuous Bridge

## Abstract

Paper 07 defines the bridge between discrete state changes and continuous
presentation. The polished theorem is deliberately exact but limited: a finite
or indexed discrete sequence can be embedded into a continuous interpolant that
matches every discrete sample point exactly. This gives the suite a way to draw
and transport continuous-looking fields without losing the discrete receipts.

This paper does not prove that the interpolant is the unique physical dynamics
between samples. It proves sample-preserving interpolation and records
between-sample dynamics as a separate obligation.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed result. Paper 00, hand routes, analog tools, workbook language, and obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. The hand route is not the purpose of the paper; it is a way to expose the same state transitions with ordinary marks, tokens, lines, or any equivalent physical substitute.

## Definitions

A **discrete trace** is a list of indexed values:

```text
D = [(0,x0), (1,x1), ..., (n,xn)]
```

A **sample-preserving bridge** is a continuous function `F` on `[0,n]` such
that:

```text
F(k) = xk for every integer sample k.
```

The verifier uses piecewise-linear interpolation:

```text
F(t) = (1-a) * x_floor(t) + a * x_ceil(t)
where a = t - floor(t)
```

At integer points, `a=0`, so `F(k)=xk`.

## Main Claim

**Theorem 7.1, Sample-Preserving Bridge.** Every finite discrete trace over
numeric values admits a continuous piecewise-linear bridge that exactly
preserves all indexed samples.

### Proof

Between each adjacent pair `(k,xk)` and `(k+1,xk+1)`, draw the straight segment
joining the two values. The resulting piecewise-linear function is continuous
because adjacent segments share the same endpoint at every integer index.
At each sample index `k`, the function evaluates to the stored value `xk`.
Thus the bridge preserves every discrete sample exactly. QED.

## Relation to Earlier Papers

Paper 06 gives typed causal edges. Paper 07 gives a presentation bridge from
indexed edge states to continuous fields. The bridge is a view of the discrete
receipt structure, not a replacement for it.

Paper 02's Rule 30 / Rule 90 correction identity can provide one family of
discrete values:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Those discrete values can be drawn as a continuous interpolant, but the exact
proof remains at the sample points unless a separate theorem proves the
between-sample dynamics.

## Falsifier

The verifier rejects this overclaim:

```text
"sample-preserving interpolation proves all between-sample physics"
```

That statement is false. Sample preservation is not physical uniqueness.

## Hand Reconstruction

1. Choose a finite indexed trace.
2. Plot each sample as a point.
3. Connect adjacent samples with straight line segments.
4. Check that the curve passes through every original sample.
5. Mark all between-sample interpretation as model-dependent.
6. Preserve the original discrete receipt next to the drawing.

## Code Reconstruction

The production verifier is:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
```

It verifies:

```text
1. The interpolant preserves every integer sample.
2. Adjacent linear segments agree at shared endpoints.
3. The Rule 30 / Rule 90 correction identity still holds on all LCR states.
4. The between-sample physical-dynamics overclaim is rejected.
```

## Open Obligations

1. Wire `verify_discrete_continuous_bridge` into `cqe_engine.formal`.
2. Decide which later papers require more than sample-preserving interpolation.
3. Add a separate theorem for any claimed Hamiltonian or physical dynamics
   between samples.
4. Carry bridge residuals into Paper 16 only as obligations until verified.

## Conclusion

Paper 07 supplies a safe bridge: it lets discrete receipts be drawn as
continuous fields while preserving every indexed sample. It does not erase the
discrete proof, and it does not claim more between samples than the verifier
can support.
