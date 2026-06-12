# Paper 7 - Discrete-Continuous Bridge

## Abstract

Paper 7 proves the sample-preserving bridge used by the CQECMPLX suite. The
previous papers produce discrete receipts: correction rows, registered
coordinates, repair constraints, path states, and causal edges. Paper 7 proves
that a finite indexed numeric trace can be embedded in a continuous
piecewise-linear presentation without losing any original sample.

The theorem is exact and limited:

```text
finite indexed trace -> continuous bridge
continuous bridge -> exact agreement at every indexed sample
```

It does not prove that the interpolant is the unique physical dynamics between
samples. Between-sample dynamics require a separate theorem.

## Claims

**Claim 7.1.** Every finite numeric discrete trace admits a continuous
piecewise-linear interpolant.

**Claim 7.2.** The interpolant preserves every indexed sample exactly.

**Claim 7.3.** Adjacent segments agree at shared endpoints.

**Claim 7.4.** Sample preservation does not prove between-sample physical
dynamics.

## Definitions

A **discrete trace** is:

```text
D = [(0,x0), (1,x1), ..., (n,xn)]
```

A **sample-preserving bridge** is a continuous function `F` on `[0,n]` such
that:

```text
F(k) = xk
```

for every integer sample index `k`.

For `t in [k,k+1]`, define the piecewise-linear bridge:

```text
a = t - k
F(t) = (1-a) * xk + a * x(k+1)
```

## Theorem 7.1 - Sample-Preserving Bridge

Every finite discrete trace over numeric values admits a continuous
piecewise-linear bridge that exactly preserves all indexed samples.

## Proof

Between each adjacent pair `(k,xk)` and `(k+1,x(k+1))`, draw the straight
segment joining the two values:

```text
F(t) = (1-a) * xk + a * x(k+1)
```

where `a = t-k`. At the left endpoint, `a=0`, so `F(k)=xk`. At the right
endpoint, `a=1`, so `F(k+1)=x(k+1)`. Adjacent segments therefore agree at the
shared integer sample, and the full piecewise function is continuous.

Since each integer sample is an endpoint of one or two adjacent segments and
all such segments agree at that endpoint, every original sample is preserved
exactly.

## Receipt

The primary executable receipt is:

```text
production/formal-papers/CQE-paper-07/verify_discrete_continuous_bridge.py
production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json
```

The receipt status is `pass`. It verifies:

```text
integer_samples_preserved                 = true
max_sample_error_is_zero                  = true
adjacent_segments_share_endpoints         = true
rule30_rule90_correction_identity_holds   = true
between_sample_physics_left_as_obligation = true
```

The receipt trace is:

```text
[0,1,1,0,1,0,0,1]
```

All sample errors are zero.

## Falsifier

The verifier rejects this claim:

```text
sample-preserving interpolation proves all between-sample physics
```

That claim is false. Sample preservation proves exact agreement at indexed
samples only.

## Relation to Earlier Papers

Paper 6 gives typed causal edges. Paper 7 gives a continuous presentation of
indexed proof data while preserving the discrete receipt.

Paper 2's correction identity remains discrete:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Paper 7 may draw those values as a continuous curve, but the proof remains at
the indexed samples unless another theorem closes the between-sample dynamics.

## Role in the Suite

The bridge rule is:

```text
discrete receipt -> indexed trace -> continuous presentation
```

The forbidden move is:

```text
continuous presentation -> erased discrete receipt
```

This lets later papers use continuous-looking fields without losing the
original finite proof.

## Open Obligations

1. Expose `verify_discrete_continuous_bridge` through the installable
   kernel/API interface.
2. Add separate theorems for Hamiltonian or physical dynamics between samples.
3. Preserve causal receipt links whenever interpolated traces are used.
4. Carry bridge residuals into later continuum papers only as obligations until
   verified.

## Conclusion

Paper 7 proves a safe bridge from discrete receipts to continuous
presentation. It preserves every indexed sample exactly and refuses to convert
visual smoothness into unsupported physical dynamics.
