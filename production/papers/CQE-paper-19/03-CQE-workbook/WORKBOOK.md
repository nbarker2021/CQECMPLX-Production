# Paper 19 — Workbook: Observer Face-Selection Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw 4 frames | `ObserverGluon().frames()` | `4 frames` |
| Select face | `ObserverGluon().select_face(n)` | `face 0|1|2|3` |
| Mark latent | `ObserverGluon().latent_faces()` | `3 faces` |
| Draw Z4 cycle | `verify_z4_face_cycle()` | `0→1→2→3→0` |

## Human Execution Protocol (Paper 19)

```
1. Draw 4 frames in Z4 cycle: 0(C) → 1(R) → 2(C') → 3(L) → 0
2. Select active face (observed center)
3. Mark 3 latent faces = obligations (O slot)
4. Rotate: Frame 0→1→2→3→0 (Z4 cycle)
```

## Tool Execution Protocol (identical)

```python
og = ObserverGluon()
og.select_face(0)  # Frame 0

assert len(og.latent_faces()) == 3

verify_z4_face_cycle()
# 0→1→2→3→0 verified

```

## Receipt (identical)

```
observer-receipt =
  frames: 4
  z4_cycle: verified
  selected_face: 1
  latent_obligations: 3
  human_verifiable: true
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
