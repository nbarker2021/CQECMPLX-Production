# CMPLX-NVEST Adapter Contract

```text
translate_target(target) -> diagnostic_form
read_boundary(diagnostic_form) -> bba_report
decompose(diagnostic_form) -> wave_report
find_candidates(wave_report) -> candidate_points
gate_with_cqe_eg8(candidate_points, context) -> gate_report
bind_to_identity(gate_report, target) -> bound_result
emit_receipt(bound_result) -> receipt_id
```

Adapters must preserve the target identity and must not collapse domain meaning into finance-only labels.
