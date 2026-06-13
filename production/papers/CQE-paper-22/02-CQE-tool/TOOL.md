# Paper 22 — Tool: MetaForge Applied Materials Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

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

*This tool is a supplemental verifier and exposure route. The formal paper and receipt carry the proof; running the tool can reproduce evidence and may leave obligations open when the receipt says so.*
