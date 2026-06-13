# Paper 13 — Workbook: Quark-Face Transport Sheet

## Workbook Role

This workbook is supplemental validation and exposure material. It is not the paper's primary proof. It shows how the paper's mathematical state can be reconstructed with ordinary marks, tokens, strings, cards, or any equivalent physical substitute so that the proof remains inspectable even without software.

## Proof/Exposure Hierarchy

The proof-carrying content of this paper is the mathematics: the definitions, lemmas, constructions, examples, and receipts that establish the claimed transport. Paper 00, workbook sheets, analog tools, and open-obligation ledgers are supplemental validation and exposure layers. They exist to make the math inspectable, reproducible, and accessible without requiring a particular software stack. In the simplest case, the same state transitions can be marked with ordinary physical tokens, lines, or dirt; the point is not the material, but the preserved center, boundary, transform, residue, and receipt structure.

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw 6 quark faces | `QuarkFaceTransport().faces()` | `6 faces` |
| Color each face | `transport.color_charge(face)` | `+1 (R,G,B) | -1 (anti)` |
| Draw gluon mediator | `transport.transport_face("R", "G")` | `gluon` |
| Draw SU(3) cycle | `transport.verify_su3_cycle()` | `R→G→B→R` |
| Verify chirality | `verify_chirality_cipher()` | `cipher verified` |

## Human Execution Protocol (Paper 13)

```
1. Draw 6 faces: R, G, B, anti-R, anti-G, anti-B
2. Color: R/G/B = +1; anti-R/anti-G/anti-B = -1
3. Draw gluon mediators: R→G, G→B, B→R (gluons)
4. Verify SU(3) cycle: R → G → B → R (Z3)
5. Note: 2 true vacua = leptons (color neutral)
```

## Tool Execution Protocol (identical)

```python
transport = QuarkFaceTransport()
transport.verify_su3_cycle()
# R→G→B→R verified

verify_color_transport()
# 6 faces, all gluon-mediated ✓

verify_chirality_cipher()
# chirality cipher verified ✓

```

## Receipt (identical)

```
quark-face-receipt =
  faces: 6 (R,G,B, anti-R,anti-G,anti-B)
  su3_cycle: R→G→B→R ✓
  color_charge: +1/-1 conserved ✓
  gluon_mediated: true ✓
  true_vacua: 2 (leptons) ✓
  human_verifiable: true (6 faces = hand-drawable)
```

---

*This workbook is a supplemental exposure route. The formal paper and receipt carry the proof; the workbook preserves an analog twin for review and boundary-collision practice.*
