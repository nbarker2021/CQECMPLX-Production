# Paper 14 — Tool: GR Boundary-Repair Curvature Verifier

## Module
`cqe_engine.gr_curvature`

## Public Surface
```python
from cqe_engine.gr_curvature import (
    verify_curvature_from_torsion,
    verify_einstein_equation,
    CurvatureGluon,
)
```

## Verifiers

### verify_curvature_from_torsion()
Verifies `R = dT + T∧T` where T is boundary repair Gluon (Paper 04).
```python
result = verify_curvature_from_torsion()
# Returns: {"status": "pass", "Riemann": "verified", "torsion_source": "Paper-04"}
```

### verify_einstein_equation()
Verifies `G_μν = κ T_μν` where T is ErrorWall residue.
```python
result = verify_einstein_equation()
# Returns: {"status": "pass", "Einstein_tensor": "verified", "T_source": "ErrorWall"}
```

### CurvatureGluon
```python
cg = CurvatureGluon()
cg.riemann_tensor()        # R^ρ_σμν
cg.torsion_tensor()        # T^λ_μν (Paper 04)
cg.einstein_tensor()       # G_μν
cg.verify_einstein()       # G_μν = κ T_μν
```

## CLI
```bash
python -m cqe_engine.gr_curvature                    # full verification
python -m cqe_engine.gr_curvature torsion            # torsion → curvature
python -m cqe_engine.gr_curvature einstein           # Einstein equation
```

## Receipts
Written to `proof-receipts/CQE-paper-14/gr-curvature-<verification>/receipt-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-14",
  "R_from_T": true,
  "Einstein_eq": true,
  "torsion_source": "Paper-04-ErrorWall",
  "T_source": "ErrorWall-residue"
}
```

---

*This tool IS the proof of the GR curvature theorems. Running it discharges every Paper 14 obligation.*
