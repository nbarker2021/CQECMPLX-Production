# CQE-E/G8 Adapter Contract

```text
receive_candidate(candidate, context) -> gate_context
read_boundary(gate_context) -> bba_report
seal_result(result_ref) -> sealed_result_id
compute_gate_features(gate_context) -> eg8_features
commit_gate(eg8_features) -> gate_guess
reveal(sealed_result_id) -> result
score(gate_guess, result) -> score
bind_or_new_datum(score, context) -> binding_decision
emit_receipt(binding_decision) -> receipt_id
```
