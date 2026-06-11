# CQE Pipeline Bindings

CQE_MORSR binds to the CQE pipeline as a validation executor.

## Pipeline Placement

```text
CQE context
  -> embed/adapt into C centroid
  -> MORSR pulse
  -> hidden guess commit
  -> reveal and score
  -> confirmed node
  -> recenter x3
  -> receipt and map update
```

## Required Interfaces

- `derive_centroid(context) -> centroid`
- `seal_expected_result(result) -> sealed_result_id`
- `pulse(centroid) -> active_nodes`
- `commit_guess(active_nodes, context) -> guess_record`
- `reveal(sealed_result_id) -> expected_result`
- `score(guess_record, expected_result) -> score_record`
- `confirm(score_record, active_nodes) -> confirmed_node`
- `recenter(confirmed_node) -> centroid`
- `write_receipt(trace) -> receipt_id`

## Market/Wave Tool Role

The market and wave engines are diagnostic sniffers, not finance-only tools. Under CQE_MORSR, their job is to locate:

- exact error points
- failure points
- success points
- phase shifts
- centroid tension
- wave/shape mismatch
- hidden-result prediction deltas

Any market-specific labels are surface vocabulary only.
