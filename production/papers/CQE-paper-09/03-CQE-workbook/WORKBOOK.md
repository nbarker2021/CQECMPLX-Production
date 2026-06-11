# Paper 09 — Workbook: Hamiltonian Window Sheet

## Sheet ⇄ Tool Isomorphism

| Analog Operation | Tool Function | Data Structure |
|------------------|---------------|----------------|
| Draw 1-3 bar windows | `iterative_hamiltonian(order=2)` | `List[WindowRead]` |
| Draw 1-5 bar windows | `iterative_hamiltonian(order=3)` | `List[WindowRead]` |
| Draw 1-7 bar windows | `iterative_hamiltonian(order=4)` | `List[WindowRead]` |
| Carry C forward | `C_accumulated = XOR(correction_bits)` | `int` |
| Read backward validate | `hamiltonian_read()` | `{"validated": bool}` |
| Mark Z4 MORSR cycle | `OBS/REF/SYN/REC` | `Z4 cycle` |

## Human Execution Protocol (Paper 09)
```
1. Write C-forms 0-5 as sequence: [C0, C1, C2, C3, C4, C5]
2. For 1-3 bar: slide 3-frame window, carry forward, read back
3. For 1-5 bar: slide 5-frame window, carry forward, read back  
4. For 1-7 bar: use all 7 C-forms, carry forward, read back
4. Verify: each window's backward read = forward carry
5. Record: surviving global C at each order
```

## Tool Execution Protocol (identical)
```python
# 1. Load base C-forms
c_forms = BASE_C_FORMS  # Papers 0-5

# 2. Run 2nd order (1-3 bar)
r2 = iterative_hamiltonian(c_forms, order=2)
# → 4 windows, each produces surviving C

# 3. Run 3rd order (1-5 bar) 
r3 = iterative_hamiltonian(c_forms, order=3)
# → 2 windows

# 4. Run 4th order (1-7 bar)
r4 = iterative_hamiltonian(c_forms, order=4)
# → 1 window

# 5. Validate all
assert all(r["validated"] for r in r2+r3+r4)
```

## Receipt (identical)
```
hamiltonian-receipt =
  2nd_order: 4 windows, C_survives: [C0⋯C2, C1⋯C3, C2⋯C4, C3⋯C5]
  3rd_order: 2 windows, C_survives: [C0⋯C4, C1⋯C5]
  4th_order: 1 window,  C_survives: [C0⋯C6]
  all_backward_validated: true
  human_verifiable: true (sliding window = hand-simulatable)
```

---

*This IS the algorithm. The workbook IS the code spec. Every analog operation has its exact digital twin.*
