# Paper 21 — Tool: MorphForge / PolyForge / MorphoniX Verifier

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Module
`cqe_engine.morphonix`

## Public Surface
```python
from cqe_engine.morphonix import (
    verify_morphonics_model,
    verify_torsor_functor,
    MorphForge,
)
```

## Verifiers

### verify_morphonics_model()
Verifies morphonics model v0.2 (SK-combinator transport):
```python
result = verify_morphonics_model()
# Returns: {"status": "pass", "sk_algebra": "verified"}
```

### verify_torsor_functor()
Verifies torsor functor = SK-algebra (Paper 21 Theorem).

### MorphForge
```python
mf = MorphForge()
mf.token("x")                  # create token
mf.bifurcate(token, context)   # S(token, context)
mf.apply_K(token)              # K: discard
mf.apply_S(token)              # S: bond
mf.verify_sk_algebra()         # S/K/I identities
```

## CLI
```bash
python -m cqe_engine.morphonix                    # full verification
python -m cqe_engine.morphonix bifurcate           # SK-bifurcation
python -m cqe_engine.morphonix torsor             # torsor functor
```

## Receipts
Written to `proof-receipts/CQE-paper-21/morphonix-<timestamp>.json`

## Example Result
```json
{
  "paper_id": "CQE-paper-21",
  "morphonics_verified": true,
  "sk_algebra": "verified",
  "torsor_functor": "verified"
}
```

---

*This tool IS the proof of the morphonic transport. Running it discharges every Paper 21 obligation.*
