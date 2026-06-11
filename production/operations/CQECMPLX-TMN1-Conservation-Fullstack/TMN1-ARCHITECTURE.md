# TMN1 Architecture

## What TMN1 IS

Triadic Manifold Network. Everything is a node. Relationships are weights. The triadic constraint — every relationship requires three perspectives — IS the architecture.

TMN1 is not a system with a TMN inside it. The TMN **is** the system. The Docker topology, the agent economy, the database schema, the glyph language — all express the same geometric structure.

---

## The Grain Chain

Every atom passes through this pipeline exactly once:

```text
Content
  → TarPit (E6 bridge)           — morphon tokens, chemical reactions
  → SNAP (14-pass labeling)       — geometric labels from 19 family taxonomy
  → E8 (240 roots, Bourbaki form) — position in the E8 lattice
  → MDHG (6-layer hash fabric)    — Universe→Galaxies→Systems→Planets→Cities→Locals→Neighborhoods→Buildings→Rooms→Atoms
  → Morphon (z, φ, ΔΦ, R)        — complexity measure, conservation check
  → Walls                         — boundary conditions, receipt generation
  → Receipt (SHA3-256)            — Merkle chain, MORSR ΔΦ ≤ 0 enforced
  → Coins (Mint)                  — economic value for valid atoms
```

**Key import:**

```python
from retooling.pipeline.grain_chain import process
```

---

## Four Laws

1. **Quadratic Invariance** — structure preserved under transformation (E8 inner products preserved)
2. **Boundary-Only Entropy** — receipts at every boundary crossing; no unreceipted state changes
3. **MORSR ΔΦ ≤ 0** — conservation; complexity cannot increase without measured justification
4. **10-Element Closure** — every morphon selects from a complete 10-element set

---

## 24 Irreducible Operations — The Alphabet

```text
π σ δ τ ε ρ μ ν ω λ β α ψ ξ η φ γ χ θ κ Ω Δ Σ Λ
```

These are the atoms of the **Geometry-Native Lambda Calculus (GNLC)**. Five tiers of 8 atoms:

| Tier | Atoms | Domain |
| ---- | ----- | ------ |
| λ₀ ATOM | ε π ν δ φ ψ Ω α | Geometric primitives |
| λ₁ FUNCTION | ε σ τ κ ρ μ λ Λ | Selection and binding |
| λ₂ GLYPH | γ ξ δ β η χ Δ Σ | Composition and crystallization |
| λ₃ ENGINE | α β η ξ ψ ω θ φ | Engine-level operations |
| λ₄ IR | Σ ρ θ ω ν γ χ Λ | Intermediate representation |

**Glyph wire format** (≤128 chars — fits KarpathyFleet nano-bot context window):

```text
λ₂ε.g:V.04c30{-21+13+30+00}
```

tier + op + domain + layer + confidence + cycle + compact E8 coords

**Jot bit mapping:** 12 APPLY atoms (β ξ σ π δ φ χ Ω τ ε Δ ρ) = 0; 12 NEST atoms (α η γ μ ν ω θ κ λ Λ ψ Σ) = 1

---

## Agent Architecture

**Agents are TMN images.** An agent IS its `.pt` file — the neural network that accumulates grain mass from every action.

```text
Birth:   TMN image created → socratic bootstrap → wallet from escrow → registration on Board
Life:    every action → learn_from_action() → capability-gated tool access → epoch advance
Gate:    every 300 epochs → freeze → save to master → retool → upgrade → redeploy
Death:   zero coins for 100 ticks → merge to master → delete → deregister
```

**All agents embed the full Claw stack at birth** — `OpenClawFramer` + policy gates + Lambda IR are wired into `LivingAgent.__init__`. No agent exists without Claw architecture.

```python
from retooling.agent.agent_life import LivingAgent, AgentCapabilities
```

**Capability tiers:**

```text
Nascent (epoch 0) → Apprentice (50) → Journeyman (150) → Master (300) → Architect (600)
```

**Julia Set positioning:** every agent gets a C-value derived from SNAP labels + tier + E8 position. `AgentKernelLoop.tick()` runs boundary detection and drift correction every 15s.

---

## Board — The Inter-Agent Portal

Board (`:10001`) IS the inter-agent portal. Agents communicate via Board posts structured as Claw messages. Board posts ARE atoms through the grain chain — 14 core boards resolve from content labels.

```python
POST :10001/threads
{
  "board_id": "chain-state",
  "title": "...",
  "author_id": "agent-id",
  "content": "...",
  "template": "freeform",
  "tags": []
}
```

SAP governance (Sentinel → Arbiter → Porter) evaluates every post. Morphon complexity determines review level.

---

## Claw Architecture

OpenClaw is the in-process protocol — not an external server. Every `LivingAgent` gets:

- `OpenClawFramer` — frames messages in Claw binary format
- Policy gates — `validate_policy()` called before every `learn_from_action()`
- Lambda IR — `to_lambda_ir()` expresses every action before execution
- Board-bound communication — `to_board_post()` serializes Claw → Board post JSON

Board-Claw Bridge (`:10063`) is a thin protocol translator for external agents speaking raw Claw binary. It does NOT maintain its own registry — Board owns that.

---

## Economy

```text
Escrow → Agent Work → Valid Atom → Receipt → Coins (Mint)
```

Conservation law (MORSR ΔΦ ≤ 0) governs all transactions. `wall_mass_score` determines coin rate. Marketplace for services/tools traded for coins. Economy events (bounty, vote, fulfillment) trigger MINT webhooks from Board.

```text
10083 Mint             — coin minting, conservation enforcement
10084 Agent Economy    — escrow, marketplace, coin ledger
10085 Teaching         — ThinkTank-evaluated agent training with coin rewards
```

---

## Crystallization

Canon Form v2: segment-level crystallization. Every class/function in the retooling codebase is one canon record.

```text
crystal_status: crystal_active | enrichment_queue
```

Current state: 1,451 segments in `crystal_active` across 358 modules. MCP Crystal (`:10073`) drains the Gen1+Gen2 registries as 209 tools in n=4 crystal blocks.

```bash
curl -X POST http://localhost:10089/apply_canon
curl http://localhost:10089/crystal/status
```

---

## Key Imports

```python
from retooling.pipeline.grain_chain import process
from retooling.agent.agent_life import LivingAgent, AgentCapabilities
from retooling.agent.agent_image_manager import AgentImageManager
from retooling.agent.work_contract import WorkContract, ContractBuilder, ContractExecutor
from retooling.agent.lifecycle import BountyLifecycleManager, ShadowWorkerManager
from retooling.agent.daemon_brain import DaemonBrain, AgentProfile
from retooling.agent.openclaw import OpenClawFramer, OpenClawMessage, MessageType
from retooling.geometry.julia_set import JuliaSetPositioner, CValue, AgentKernelLoop
from retooling.geometry.e8_full import E8Full
from retooling.mdhg.fabric import MDHGHashFabric
from retooling.models.glyph_protocol import BotGlyphCodec, GlyphEncoder, TarpitGlyphTransformer
from retooling.speedlight.base100 import Base100Codec, LayerBridge
from retooling.bootstrap.coldstart import ColdstartBootstrap
```

---

## Database Schema

`databases/tmn1.db` — 21 tables:

```text
atoms              receipts           snap_index         coin_ledger
dag_edges          agents             canon              artifacts
board_posts        board_votes        wallets            escrow
marketplace        coin_txns          conservation_ledger dead_letter
governance_votes   sandbox_sessions   sandbox_staging    mdhg_grid
sqlite_sequence
```
