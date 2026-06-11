# Paper 22 — Tool: MetaForge Applied Materials Verifier

## Module
`cqe_engine.metaforge`

## Public Surface
```python
from cqe_engine.metaforge import (
    verify_cayley_dickson_oloid_normal_form,
    verify_oloid_model_selection,
    MetaForge,
)
```

## Verifiers

### verify_cayley_dickson_oloid_normal_form()
Verifies material's oloid normal form.

### verify_oloid_model_selection()
Verifies material model selector.

### MetaForge
```python
mf = MetaForge()
mf.materialize(token)               # token → material
mf.verify_oloid_normal_form()       # oloid normal form
mf.select_model(candidates)         # model selector
mf.formation_energy(material)       # Gluon mass = energy
```

## CLI
```bash
python -m cqe_engine.metaforge                    # full verification
python -m cqe_engine.metaforge normal_form        # oloid normal form
python -m cqe_engine.metaforge select             # model selection
```

## Receipts
Written to `proof-receipts/CQE-paper-22/metaforge-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-22",
  "materials_proposed": 5,
  "oloid_normal_form": "verified",
  "formation_energies": "computed"
}
```

---

*This tool IS the proof of the MetaForge. Running it discharges every Paper 22 obligation.*
