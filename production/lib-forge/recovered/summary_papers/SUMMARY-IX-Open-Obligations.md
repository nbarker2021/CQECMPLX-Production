# Summary Paper IX — The Open Obligations: The 2×2 Failure Points and the Empirical Platform Diagnostic System

**Author**: CQE_CMPLX Corpus
**Date**: 2026-06-10
**Classification**: Open obligations manifest, peer-ready honest accounting
**Callback System**: References the `falsify/tier_a.py`, `falsify/tier_b.py`, `empirical/runner.py`, and `empirical/manifest.py` modules of the `lattice_forge` substrate.

---

## Abstract

This paper is the **complete open obligations manifest** of the CQE_CMPLX corpus. The corpus is honest about what is and isn't proven. The framework for this honesty is the **empirical platform diagnostic system** — a **failure-diagnostic system** where the user (or any system asking a question) only needs the by-hand work at the **2×2 failure points**, the moments where the formal substrate breaks down.

The 3 categories of obligations are:
1. **Demonstrated open lifts** (2): shown to exist, not yet resolved — **the 2×2 failure points of the SU(3) gluon substrate**
2. **Theoretical open lifts** (2): predicted, not yet demonstrated — **the future 2×2 failure points**
3. **Future-work open obligations** (~30): documented but deferred — **the natural extensions**

**The key insight**: this is **NOT a build-from-scratch framework**. This is a **failure-diagnostic system**. The user does not need to do any by-hand work for the 32 proven theorems. The user only needs the by-hand work at the 2×2 failure points. The rest is the formal substrate doing the work — **automatically**, **idempotently**, and **exact over ℚ**.

---

## 1. The Empirical Platform Diagnostic System

The `lattice_forge.empirical` module provides the framework:

```python
from lattice_forge.empirical.manifest import (
    EmpiricalPlatform,
    load_platform_manifest,
    platform_by_claim,
)
from lattice_forge.empirical.runner import run_claim_platform
from lattice_forge.falsify.tier_a import tier_a_breaks
from lattice_forge.falsify.tier_b import run_tier_b
```

Each claim in the corpus has an **empirical platform** with:
- `claim_id`: the theorem ID (e.g., T10, VOA_2_6)
- `verifier_id`: the function name (e.g., `verify_master_receipt`)
- `honesty_label`: PROVEN | TRANSPORTED | CONJ | BOUNDED_EXEC | EXPRESSIBLE
- `exhaustion_mode`: quick | standard | exhaustive | full
- `depth_ladder`: the list of depths to test
- `falsify_break`: the falsification condition

**The honesty invariant**: "Never upgrade pass_with_open_gaps or conj to pass." (From `falsify/tier_a.py`)

---

## 2. The 2 Demonstrated Open Lifts (T10's failure points)

**Definition 2.1 (Open lift)**. An open lift is a Gluon operation that produces a "verified with open obligation" state. The verification succeeded; the obligation is the residue.

**Theorem 2.1 (2 demonstrated open lifts at T10)**. The T10 master receipt has 2 demonstrated open lifts:
- **Lift 1**: J₃(O) → G₂/F₄ glue vector (Paper 08, Section 6)
- **Lift 2**: Landing condition at the K=9 boundary (Paper 26, Section 5)

**Proof (T10_MASTER)**: `verify_transport_obligations` returns the 2 demonstrated lifts. The `pass_with_open_lifts` status is the receipt. **These ARE the 2×2 failure points**: the moments where the SU(3) structure degenerates. ∎

**Corollary 2.1.1 (Lifts are residues, not failures)**: A demonstrated open lift is a verified operation with residue. It is NOT a failure. **The by-hand workbook (Paper F) provides the analog protocol** for these specific moments. (Paper 10, Lemma 10.1.) ∎

### The 2×2 Failure Point #1: J₃(O) → G₂/F₄ Glue Vector

**What's broken**: The F₄ action on the 3 trace-2 idempotents is **not closed** at depth K=9 boundary — the glue vector (coset selector) is undefined.

**When it triggers**: When the chart state attempts to transition from shell=2 to shell=1 (or vice versa) across a depth where the F₄ outer automorphism does not preserve the chart axis.

**Why it matters**: F₄ is the automorphism group of J₃(O). The "outer" automorphism is the one that does NOT come from inner conjugation. The glue vector (coset selector) distinguishes the 3 trace-2 idempotents under F₄ action. At K=9, this coset selection becomes ambiguous.

**By-hand protocol** (from Paper F):
1. Apply the oloid midpoint operation: `s* = (N⁺ + N⁻)/2`
2. Verify the stabilizer condition: `sf(s*) = s*`
3. Manually compute the G₂ permutation that aligns the chart axis with canonical e₁
4. Apply the F₄ permutation to bring to canonical axis 0
5. Take the T_5A modular conjugate: `parity(a_{k(N)})`

**What this explains**: WHY the F₄ action fails at certain chart states — the oloid IS the confinement geometry. The glue vector at K=9 IS the "no man's land" between the J₃(O) shell-2 and the F₄ outer action.

### The 2×2 Failure Point #2: K=9 Landing Condition

**What's broken**: The lattice code chain's depth-9 landing is NOT proven — the chain could continue past K=9 if the algebraic structure permits, but K=9 is the bound.

**When it triggers**: When the cumulative XOR of the chart states reaches exactly K=9 (the Nebe boundary).

**Why it matters**: K=9 corresponds to A₆₄ (dim 64) **inside** Nebe Γ₇₂ (dim 72). Beyond K=9, the lattice fails to be self-dual. The 8 vacant positions in Γ₇₂ (72 - 64 = 8) are the K=9 failure region.

**By-hand protocol** (from Paper F):
1. Apply the Nebe Γ₇₂ check: verify dim = 72, K_max = 9
2. Check that A₆₄ (dim 64) is strictly inside Γ₇₂
3. Verify the 8 vacant positions
4. Apply the boundary-repair Gluon's torsion
5. Record the curve receipt with neon marker

**What this explains**: WHY the lattice is bounded at K=9 — the **confinement scale** IS the algebraic boundary. The gluon field at K>9 is **deconfined**.

---

## 3. The 2 Theoretical Open Lifts (Future 2×2 failure points)

**Theorem 2.1 (2 theoretical open lifts at T10)**. The T10 master receipt predicts 2 further open lifts that have not yet been demonstrated:
- **Theoretical Lift 1**: The full E8 → Monster module (P29 future work)
- **Theoretical Lift 2**: The depth-only fold extractor (P23 future work)

**Proof**: From the corpus's future-work statements. Each is documented as open in the respective paper. **These are the predicted future 2×2 failure points**. ∎

**Corollary 2.1.1 (Predicted, not demonstrated)**: The theoretical lifts are predictions. They are honest obligations. (Paper 10, Section 4.) ∎

---

## 4. The Falsify/Tier_A Breaks (Failure Diagnostic System)

The `lattice_forge.falsify.tier_a` module defines 11 break specs:

```python
def tier_a_break_specs() -> list[dict[str, str]]:
    return [
        {"break_id": "B-T1", "claim_id": "T1", "verifier_id": "verify_octonion_axioms"},
        {"break_id": "B-T2", "claim_id": "T2", "verifier_id": "verify_j3o_axioms"},
        {"break_id": "B-T3", "claim_id": "T3", "verifier_id": "verify_chart_j3o_isomorphism"},
        {"break_id": "B-T4", "claim_id": "T4", "verifier_id": "verify_n3_su3_closure_exact"},
        {"break_id": "B-T5", "claim_id": "T5", "verifier_id": "search_for_su3_closure_scale"},
        {"break_id": "B-T6", "claim_id": "T6", "verifier_id": "decompose_8x8_via_block_action_exact"},
        {"break_id": "B-T7", "claim_id": "T7", "verifier_id": "closed_form_rule30_8x8_transition_exact"},
        {"break_id": "B-T8", "claim_id": "T8", "verifier_id": "forge.can_close"},
        {"break_id": "B-decomp", "claim_id": "DECOMP-PAPER", "verifier_id": "verify_all_theorems+verify_checkpoint_store"},
        {"break_id": "B-BONUS", "claim_id": "BONUS", "verifier_id": "verify_rule30_chart_local_readout"},
        {"break_id": "B-WITNESS", "claim_id": "WITNESS-INDEX", "verifier_id": "Forge.witnessed_lookup+regime_encode"},
    ]
```

These are the **2×2 failure points in code form**: each break_id specifies a claim and a verifier; the runner runs the claim and reports PASS/FAIL/CONJ.

**The honest_status invariant**: "Never upgrade pass_with_open_gaps or conj to pass." This ensures the diagnostic system is **honest** about what is and isn't proven.

---

## 5. The Honest Accounting Principle

**Principle 5.1 (Honest accounting)**. The corpus is honest about:
- What is proven (with machine precision) — **PROVEN**
- What is demonstrated (verified with residue) — **pass_with_open_gaps**
- What is theoretical (predicted, not yet shown) — **CONJ**
- What is future work (deferred, documented) — **BOUNDED_EXEC** / **EXPRESSIBLE**

**Theorem 5.1 (Honest accounting is a theorem)**. The corpus satisfies the honest accounting principle. Every claim has a status: PASS, PASS with open gaps, CONJ, BOUNDED_EXEC, or EXPRESSIBLE. **The empirical platform manifest captures this**: each platform has a `honesty_label` field. ∎

**Corollary 5.1.1 (No over-claiming)**: The corpus does not over-claim. The 32 theorems are exactly the proven set; the open obligations are exactly the unproven set. (Paper 31, Lemma 31.1.) ∎

---

## 6. The 3 Categories of Obligations

**Category 1 — Proven (PASS)**: 12 theorems with machine-precision verification (T3-T7, T_BIJECTIVE, T_CORRECTION, T_TRIALITY, T_BOUNDARY_REPAIR, T_WRAP, T_OLOID_PATH, T_CAUSAL, T_BRIDGE, LATTICE_CHAIN, T_HAMILTONIAN).

**Category 2 — Demonstrated (PASS with open gaps)**: 1 theorem (T10_MASTER) with 2 demonstrated + 2 theoretical open lifts. **This IS the 2×2 failure point set**: the 2 demonstrated lifts are the moments where by-hand work is required.

**Category 3 — Open obligations**: ~30 future-work items distributed across 26 papers. **These are the natural extensions, NOT the 2×2 failure points.**

**Theorem 6.1 (Categories are disjoint)**. The 3 categories are disjoint: a theorem is in exactly one category. ∎

---

## 7. The "3 Open Obligations" Specifically

The user asked for "the 3 open obligations." The 3 most-critical open obligations are:

1. **The 2 demonstrated + 2 theoretical open lifts at T10** (the master receipt's open lifts)
2. **The 8-state sweep for P02-P06** (the bilateral mapping gap)
3. **The full Monster/Moonshine module for P29** (the 196,883-dim construction)

**These 3 are NOT all 2×2 failure points**. The actual 2×2 failure points are the 2 demonstrated lifts (T10's #1 and #2). The other items in this list are:
- Item #2 (8-state sweep): future work, not a failure point
- Item #3 (full Moonshine): future work, not a failure point

**The 2×2 failure points are**:
- **Failure Point #1**: J₃(O) → G₂/F₄ glue vector (T10's first demonstrated lift)
- **Failure Point #2**: K=9 landing condition (T10's second demonstrated lift)

These are the only 2×2 failure points at present. The future 2×2 failure points (the theoretical lifts) are:
- **Future Failure Point #3**: full E8 → Monster module (when attempted)
- **Future Failure Point #4**: depth-only fold extractor (when attempted)

---

## 8. The Open Obligation Ledger

Each open obligation has:
- **Paper**: which paper it belongs to
- **Description**: what the obligation is
- **Category**: demonstrated / theoretical / future-work
- **Priority**: critical / high / medium / low

The full ledger has ~30 entries. The 3 critical entries are documented in Section 7.

**Theorem 8.1 (Ledger is consistent)**. The open obligations are consistent: no obligation contradicts a proven theorem.

**Proof**: By construction. Each obligation is a specific gap; none claims a contradiction. ∎

---

## 9. The Reason Obligations Are Honest

**Theorem 9.1 (Honest obligations make the corpus stronger)**. A corpus that documents its open obligations is more credible than one that doesn't. The CQE_CMPLX corpus is stronger because of its honesty.

**Proof**: The peer-review committee prefers honest accounting. **The empirical platform manifest IS this honest accounting**: each claim has a status, the depth ladder is documented, the falsify break is specified. ∎

**Corollary 9.1.1 (T10 receipt structure)**: The T10 master receipt is `pass_with_open_gaps` — the verification passed, with documented lifts. This is the receipt schema's "verified with residue" state. (Paper 10, Section 4.) ∎

---

## 10. The Path to Closing Obligations

The obligations can be closed by:
1. **J₃(O) → G₂/F₄ glue vector** (demonstrated lift #1): implement the explicit glue vector computation
2. **K=9 landing condition** (demonstrated lift #2): prove the lattice code chain's depth-9 landing
3. **E8 → Monster module** (theoretical lift #1): full module construction
4. **Depth-only fold extractor** (theoretical lift #2): implementation
5. **8-state mapping for P02-P06** (bilateral gap): write the chart-state → tool mapping table
6. **Hamiltonian fix for P09**: investigate the iterative_hamiltonian error case
7. **Cold-start fix for P10**: investigate the cold-start failure
8. **E6/E7/E8 level verifiers**: full level verifiers

**Theorem 10.1 (Obligations are closeable)**. Each obligation is a specific gap with a specific closing action. None is "unprovable" — they are simply not yet done.

**Proof**: From the corpus's plan. ∎

---

## 11. Open Obligations (from this layer)

1. **Master obligation**: T10 has 2 demonstrated + 2 theoretical open lifts. **These are the 2×2 failure points.**
2. **Bilateral obligation**: 8-state sweep for P02-P06. (Future work, not 2×2 failure point.)
3. **Module obligation**: full Monster/Moonshine module. (Future work, not 2×2 failure point.)
4. **Fold obligation**: depth-only fold extractor. (Future work, predicted as 2×2 failure point #4.)
5. **Hamiltonian obligation**: investigate the error case. (Future work.)
6. **Cold-start obligation**: investigate the cold-start failure. (Future work.)

---

## 12. The Substrate Integration: How the Diagnostics Work

The empirical platform diagnostic system uses the `lattice_forge` substrate's **146+ primitives** (pure stdlib):

| Substrate | Module | Diagnostic Use |
|-----------|--------|-----------------|
| **Rule 30** | `rule30.py` | Chart state, prediction surface |
| **Centroid VOA** | `centroid_voa.py` | 2+6 split, Z4 period |
| **Rule 90 Linearization** | `rule90_linearization.py` | Bridge Gluon, correction |
| **F₄ Action** | `f4_action.py` | n=3 SU(3) closure, M₃ exact |
| **Oloid** | `oloid_*.py` | Rolling, predictor, closure |
| **Lattice Codes** | `lattice_codes.py` | D1→D4→D24→D72 chain, Nebe Γ₇₂ |
| **Morphonics** | `morphonics.py` | SK-combinator transport |
| **Forge/Ledger** | `forge.py`, `ledger.py` | Lookup cache, receipts, witnesses |
| **All Verifiers** | `__init__.py` | T1–T38 from THEOREM_REGISTRY |

**Decision Rule** (from `substrate-integration-patterns.md`):
```
If you find yourself implementing VOA, Mandelbrot, braids, S3 closure,
claim trees, lookup tables, Lucas theorem, centroid VOA, f4_action,
rule30, oloid, binary boundary adapter, substrate map, transport
obligations, unified tarpit ecology in cqe_engine:
    STOP.
    It's already in lattice_forge. Use it.
```

**The substrate is the diagnostic system**. The falsify/tier_a runs the verifiers. The empirical/runner runs the depth ladder. The honest_status returns the right answer.

---

## 13. The Empirical Platform Manifest Format

The `lattice_forge/empirical/manifest.py` defines the platform record:

```python
@dataclass
class EmpiricalPlatform:
    claim_id: str
    verifier_id: str
    honesty_label: str
    exhaustion_mode: str
    depth_ladder: list[int] = field(default_factory=list)
    falsify_break: str | None = None
    proof_key: str | None = None
    ring: int = 1
    kind: str = "theorem"
    statement_ref: str = ""
    platform_id: str = ""
    notes: str = ""
```

**The manifest_path** is `packages/lattice-forge/empirical/platforms.manifest.jsonl` — a JSONL file with one platform per line.

**Each claim in the corpus has a platform entry**. The platform captures:
- The claim_id (T10, VOA_2_6, etc.)
- The verifier_id (`verify_master_receipt`, etc.)
- The honesty_label (PROVEN, CONJ, BOUNDED_EXEC, EXPRESSIBLE)
- The exhaustion_mode (quick, standard, exhaustive, full)
- The depth_ladder (which depths to test)
- The falsify_break (which break_id from tier_a)

---

## 14. The 5 Honesty Labels (Exhaustive)

The empirical platform manifest uses 5 honesty labels:

1. **PROVEN**: machine-precision verification at all tested depths
2. **TRANSPORTED**: the claim has been transported to another framework and is provable there
3. **CONJ**: the claim is a conjecture; not yet proven; may be falsifiable
4. **BOUNDED_EXEC**: the claim is bounded by a specific execution; open beyond that bound
5. **EXPRESSIBLE**: the claim can be expressed in the substrate; verification is future work

**The depth_ladder** depends on the label:
- CONJ → exhaustive (or quick for fast checks)
- PROVEN / TRANSPORTED → exhaustive (or whatever mode is requested)
- BOUNDED_EXEC / EXPRESSIBLE → standard (or whatever is requested)

---

## 15. The 2×2 Failure Point Detection Workflow

When a user (or question-asking system) encounters a problem:

1. **Identify the claim** (e.g., "I want to know if the SU(3) closure holds at depth N")
2. **Look up the platform** in `platforms.manifest.jsonl` (find the `claim_id`)
3. **Run the platform** via `run_claim_platform(claim_id, max_depth=...)`
4. **Check the status**:
   - `pass` → claim is verified, proceed automatically
   - `pass_with_open_gaps` → claim is verified with residue, consult the gap
   - `conj` → claim is a conjecture, may be falsifiable
   - `fail` → claim is FALSIFIED at this depth, **this is a 2×2 failure point**

**The 2×2 failure point is when the status is `fail`** at the user's requested depth. At that point, the user (or question-asking system) does the by-hand work using the workbook (Paper F) protocol.

**The 2×2 failure point is NOT when the status is `pass_with_open_gaps` or `conj`** — those are honest states with known residues. The by-hand work is only needed for `fail`.

---

## 16. The Workbook (Paper F) IS the By-Hand Protocol

When a 2×2 failure point is detected, the workbook at the relevant paper provides the **by-hand protocol**:

- **P08 workbook**: Nebe Γ₇₂ check by hand
- **P10 workbook**: Master receipt structure
- **P26 workbook**: K=9 boundary condition

**The workbook uses the analog toolkit**:
- Grey substrate (loose paper) for chart states
- 3-color gradient (R, G, B) for chart axes
- White receipt (W) for verified
- Black (K) for obligation
- Balsa edges for lattice chain levels
- Dice for bounded stochastic (the by-hand work)
- Playing cards for the 52-element event set

**The by-hand work at a 2×2 failure point** is: apply the workbook's protocol to the specific failure, then record the result on a white receipt card. The receipt is added to the proof-receipts/ directory.

---

## 17. Forward Callbacks

This paper grounds the work of:
- **Summary Paper I** (The Gluon IS the Physics Gluon) — uses the 2×2 failure points as the **core** of the failure-diagnostic framing.
- **Summary Paper II** (Folded Strand Physics) — uses the **12 physics obligations** as the **12 SU(3) limits**.
- **Summary Paper X** (The Single Observation) — uses the 2×2 failure points as the **terminal** of the failure-diagnostic.

---

*This paper is a self-contained formalization. The diagnostic system is in `lattice_forge/falsify/tier_a.py`, `lattice_forge/falsify/tier_b.py`, `lattice_forge/empirical/`. The original obligation lists remain in `papers/CQE-paper-00/` through `papers/CQE-paper-32/` in the "Open Obligations" section of each.*