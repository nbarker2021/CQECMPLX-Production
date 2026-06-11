# CQE_MORSR Validation Loop

CQE_MORSR wraps MORSR as a validation executor.

## Loop

```text
derive C centroid from CQE context
seal expected result
emit 240-direction E8 pulse
collect active validation nodes
commit hidden guess
reveal expected result
score guess against result
confirm or reject reading
if confirmed:
    set reading as pode/node
    recenter
repeat until 3 recenter confirmations or stop condition
emit diagnostic receipt and delta map
```

## CQE Inputs

- source context
- validation question
- expected result source, sealed
- available evidence
- allowed tools
- forbidden leakage rules
- scoring rubric

## CQE Outputs

- prediction
- confidence
- reasoning snapshot before reveal
- revealed result
- score
- failure mode
- confirmed node
- recenter trace
- map update
- receipt

## Failure Modes

- `hit`: prediction matches result.
- `near_miss`: prediction partially matches but misses key structure.
- `false_positive`: prediction asserts success where result says failure.
- `false_negative`: prediction rejects success.
- `leakage`: result was visible before guess.
- `invalid_context`: context was insufficient or malformed.
- `unscored`: result was never revealed.
