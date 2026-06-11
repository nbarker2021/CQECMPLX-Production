# Paper 08 — Tool: E8/Niemeier/Leech Closure Verifier

## Module
`cqe_engine.closure`

## Public Surface
```python
from cqe_engine.closure import (
    verify_lattice_code_chain,
    verify_golay_24,
    verify_hamming_7_fano,
    verify_extended_hamming_8,
    verify_powered_chain,
    NebeLattice,
)
```

## Verifiers

### verify_lattice_code_chain()
Verifies the full D1→D4→D24→D72 chain:
- D1: parity 3 (repetition) → D3: Hamming(7,4) → D4: Extended Hamming(8,4)→E8
- D24: Golay(24,12,8) → Leech → Nebe dim 72
Returns: `{"status": "pass", "levels_verified": 5, "glue_vectors_valid": True}`

### verify_golay_24()
Verifies Golay(24,12,8) generator matrix properties.

### verify_hamming_7_fano()
Verifies Hamming(7,4,3) ↔ Fano plane octonion multiplication.

### verify_extended_hamming_8()
Verifies Extended Hamming(8,4,4) ⟹ Construction A → E8 lattice.

### verify_powered_chain()
Verifies shortcut chain: 1→9→49→72

### NebeLattice
```python
nebe = NebeLattice()
nebe.A64_dim()      # 64
nebe.K_max()        # 9
nebe.glue_vectors() # glue cosets
```

## CLI
```bash
python -m cqe_engine.closure                          # full chain verification
python -m cqe_engine.closure golay                    # golay-24 only
python -m cqe_engine.closure nebe                     # Nebe Γ72 verification
```

## Receipts
Written to `proof-receipts/CQE-paper-08/closure-<level>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-08",
  "chain_verified": ["D1","D3","D4","D24","D72"],
  "golay_verified": true,
  "fano_verified": true,
  "E8_construction_A": true,
  "nebe_K9_bound": true
}
```

---

*This tool IS the proof of the closure theorems. Running it discharges every Paper 08 obligation.*
