# Paper 07 - Tool: Discrete-Continuous Bridge Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module

`cqe_engine.bridge`

## Public Surface

```python
from cqe_engine.bridge import (
    verify_bridge_exactness,
    interpolate_discrete_to_continuous,
    verify_rule90_linearization,
    BridgeInterpolator,
)
```

## Verifiers

### verify_bridge_exactness(max_depth=4096)

Verifies that the discrete-to-continuous bridge preserves every indexed sample
point exactly. This is a sample-preservation theorem, not a proof of the unique
physical dynamics between samples.

Returns:

```python
{
    "status": "pass" | "fail",
    "max_sample_error": Fraction,
    "between_sample_dynamics_closed": bool,
    "claim": str,
}
```

At indexed samples, `max_sample_error = 0`. Between-sample dynamics remain an
explicit obligation unless a later theorem closes them.

### verify_rule90_linearization()

Verifies the local identity:

```text
Rule30(L,C,R) = Rule90(L,R) xor (C and not R)
```

Returns:

```python
{"status": "pass", "identity_holds": True}
```

### BridgeInterpolator

Interpolates indexed discrete edge states to a continuous presentation field.

```python
interp = BridgeInterpolator()
field = interp.interpolate(causal_edge, resolution=0.001)
```

The field is a view of the discrete receipt structure, not a replacement for
the discrete proof.

## CLI

```bash
python -m cqe_engine.bridge
python -m cqe_engine.bridge interpolate 128
python -m cqe_engine.bridge l90
```

## Receipts

Current polished receipt:

```text
production/formal-papers/CQE-paper-07/discrete_continuous_bridge_receipt.json
```

## Example Result

```json
{
  "paper_id": "CQE-paper-07",
  "theorems": ["T_SAMPLE_PRESERVING_BRIDGE", "T_R30_DECOMP"],
  "all_passed": true,
  "max_sample_error": 0,
  "rule30_rule90_correction_identity_holds": true,
  "between_sample_dynamics_closed": false
}
```

---

*This tool proves the indexed sample bridge and preserves the Rule 30 / Rule 90
correction identity. It does not discharge every Paper 07 obligation.*
