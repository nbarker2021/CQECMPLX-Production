# Paper 08 — Workbook: E8/Niemeier/Leech Closure Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw D1 parity bits | `PARITY_3_GENERATORS` | `Matrix over ℤ/2ℤ` |
| Draw D3 Hamming/Fano | `HAMMING_7_GENERATORS` | `Matrix over ℤ/2ℤ` |
| Draw Fano plane | `FANO_LINES` | `7 points, 7 lines` |
| Draw D4 Extended Hamming | `EXTENDED_HAMMING_8_GENERATORS` | `Matrix over ℤ/2ℤ` |
| Draw E8 (Constr. A) | `Construction_A(extended_hamming_8)` | `E8_root_lattice` |
| Draw D24 Golay | `GOLAY_24_GENERATORS` | `Matrix over ℤ/2ℤ` |
| Draw Leech (Constr. A) | `Construction_A(golay_24)` | `Leech_lattice` |
| Draw D72 Nebe | `NEBE_GENERATORS` | `Nebe_lattice (dim 72)` |

## Human Execution Protocol (Paper 08)
```
1. Draw D1: 3-bit parity check matrix
2. Draw D3: Hamming(7,4) ≡ Fano plane → octonion mult table
3. Draw D4: Extended Hamming(8,4,4) → Construction A → E8
4. Draw D6: Golay(24,12,8) → Construction A → Leech
5. Draw D72: Nebe lattice (A64 inside, K=9 bound)
6. Trace code chain: 1→3→7→8→24→72
6. Verify: A64 (dim 64) strictly inside K=9 shell (72)
```

## Tool Execution Protocol (identical)
```python
# 1. Verify each level
verify_hamming_7_fano()
verify_extended_hamming_8()
verify_golay_24()

# 2. Verify code chain
verify_lattice_code_chain()

# 3. Verify Nebe bound
nebe = NebeLattice()
assert nebe.A64_dim() == 64
assert nebe.K_max() == 9
```

## Receipt (identical)
```
closure-receipt =
  D1: parity_3 ✓
  D3: hamming_7/fano ✓
  D4: ext_hamming_8 → E8 ✓
  D6: golay_24 → Leech ✓
  D72: nebe_gamma72 (K=9) ✓
  A64 ⊂ K=9 shell ✓
  human_verifiable: true (Fano plane = hand-drawable)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
