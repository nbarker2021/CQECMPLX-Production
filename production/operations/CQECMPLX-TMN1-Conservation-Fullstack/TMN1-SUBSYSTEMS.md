# TMN1 Subsystems

Internal design of the major system components. See [TMN1-ARCHITECTURE.md](TMN1-ARCHITECTURE.md) for the overall structure and [TMN1-DOCKER.md](TMN1-DOCKER.md) for the full port map.

---

## Grain Chain

The core pipeline. Every atom passes through exactly once.

**Entry:** `retooling/src/retooling/pipeline/grain_chain.py` — `process(content) → Atom`

**Stages:**

1. **TarPit (E6 bridge)** — morphon tokenization, chemical reactions. `GlyphTarPit` + `EvolvingTarPit` both active. Jot bits (APPLY=0, NEST=1) determine bonding rules. 20-60 bonds per atom.
2. **SNAP (14-pass labeling)** — `SNAPEnricher` applies 19-family taxonomy × layer labels. Family detection from path + content keywords. Content-hash dedup before insert.
3. **E8 (240 roots, Bourbaki form)** — `E8Full` positions atom in the E8 lattice. Simple roots: α₁–α₆ = eᵢ − eᵢ₊₁, α₇ = e₅+e₆, α₈ = (−½)⁷×(+½). DO NOT normalize — E8 simple roots have norm √2.
4. **MDHG (6-layer hash fabric)** — `MDHGHashFabric` assigns 10-level address: Universe→Galaxies→Systems→Planets→Cities→Locals→Neighborhoods→Buildings→Rooms→Atoms. Hash algorithms per level (SHA3-512 at Universe, SHA256 at Atoms).
5. **Morphon** — computes (z, φ, ΔΦ, R). ΔΦ must be ≤ 0. Complexity measure gates all downstream work.
6. **Walls** — boundary conditions, conservation check.
7. **Receipt (SHA3-256)** — Merkle chain receipt, MORSR ΔΦ ≤ 0 enforced. Coin mint triggered.

---

## Agent System

**Core file:** `retooling/src/retooling/agent/agent_life.py` — `LivingAgent`

Every `LivingAgent` gets at birth (fail-silent on ImportError):

- **Claw stack** — `OpenClawFramer(agent_id=...)`, policy gate, Lambda IR
- **Julia Set positioning** — `CValue` derived from SNAP labels + tier + E8 position; `AgentKernelLoop` ticks every 15s (boundary detection, drift correction)
- **Board URL** — `_claw_board_url` for posting Claw messages to Board

**Per-action flow:**

```text
learn_from_action(tool, content)
  → _claw.validate_policy({action: tool})   [blocks policy violations]
  → _claw.to_lambda_ir({action: tool})      [Lambda IR before execution]
  → tool execution
  → epoch++
  → if epoch % 300 == 0: freeze + save .pt + retool
  → _julia_tick()                           [boundary/drift handling]
  → _claw_post(MORSR_PULSE, ...)           [broadcast to board]
```

**Agent image:** `.pt` file in `databases/agent_images/`. Agent identity = grain mass history. The `.pt` file IS the agent — not a config, a neural network.

---

## Board v4

**Core file:** `infrastructure/board/board.py`

Posts are atoms through the grain chain. 39 boards resolve from content SNAP labels — not hardcoded categories. 14 core board IDs recognized.

**Per-post flow:**

```text
POST /threads
  → grain_chain.process(content)   [labels, E8, MDHG, receipt]
  → SAP governance check
  → _save_atom() to board.db
  → if template in {bounty, vote, fulfillment}: fire MINT webhook (non-blocking)
```

**Economy integration:** `MINT_URL` env var enables webhooks. Empty = disabled. Board never blocks on Mint.

---

## ThinkTank

**Core file:** `infrastructure/thinktank/thinktank.py` (the live service at `:10080`)

8 KarpathyFleet nanoGPT bots in quorum. Each bot has `block_size=128` (128-char context). Bots emit structured glyph directives, decoded via `BotGlyphCodec`.

**Endpoints:**

- `POST /ask {question, top_k}` → `{synthesis: "..."}` — corpus hits + brain context + quorum answer (best for conversational queries)
- `POST /reason {query, content}` → `{glyph: "λ₂ε...", thinktank: {...}}` — glyph sequence + bot directives
- `POST /think {query}` → single-call invocation

**Glyph encoding:** `/reason` response includes `glyph` field — GNLC wire format encoding the bot directives. `BotGlyphCodec.summarize_thinktank()` decodes to English.

---

## Staging / Crystallization

**Core file:** `retooling/src/retooling/tools_staging/staging_service.py` at `:10089`

Canon Form v2: segment-level crystallization. `SegmentExtractor` splits each module into class/function segments. Each segment → one `CanonSegment` record with `snap_key` (from Atlas or SHA256 fallback, 2s timeout).

**Crystal states:** `enrichment_queue` → `crystal_active`

**Endpoints:**

- `POST /apply_canon` — run full crystallization pass
- `GET /crystal/status` — `{modules_crystallized, total_active_logged}`
- `GET /partition/status` — partition stats

**MCP Crystal (`:10073`)** drains `crystal_active` records into 209 tools as n=4 crystal blocks.

---

## MDHG Hash Fabric

**Core file:** `retooling/src/retooling/mdhg/fabric.py` — `MDHGHashFabric`

10-level hierarchical hash addressing. Hash algorithms:

```text
Universe:       SHA3-512 (64B)
Galaxies:       BLAKE2b-256 (32B)
Systems:        SHA3-256 (32B)
Planets:        SHA3-256 (32B)
Cities:         BLAKE2b-256 (32B)
Locals:         SHA256 (32B)
Neighborhoods:  SHA256 (32B)
Buildings:      SHA256 (16B)
Rooms:          SHA256 (16B)
Atoms:          SHA256 (8B)
```

Note: `hashlib.blake2b` used as BLAKE3 substitute (blake3 not in stdlib).

**Key methods:** `hash_at_level(level, label, e8_pos, metadata)`, `hash_receipt(prev, op, inputs, outputs, ts)`, `detect_interference(h1, h2)`, `compute_interference_product(h1, h2)`

**MDHG Sandbox (`:10062`)** provides isolated scratchpad sessions with 30-min idle TTL.

---

## OpenClaw Protocol

**Core file:** `retooling/src/retooling/agent/openclaw.py` — single file, merged from 4 source files.

Key classes: `MessageType` (enum), `OpenClawMessage`, `OpenClawFramer`, `OpenClawServer`, `OpenClawClient`, `ResourceManager`

CQE-specific message types: `LATTICE_SYNC`, `MORSR_PULSE`, `E8_TRANSFORM`

`OpenClawMessage.to_board_post()` — serializes Claw message → Board post JSON for `POST :10001/threads`

`OpenClawServer` is used ONLY by the Board-Claw Bridge (`:10063`). Not the agent registry.

---

## Julia Set Positioning

**Core file:** `retooling/src/retooling/geometry/julia_set.py`

`CValue.from_snap_labels(labels, tier, e8_position)` → deterministic C-value from context

`AgentKernelLoop.tick()` per-tick flow: sample state → label spray → drift check → boundary/expand/mirror → emit receipt

Every agent gets a C-value and kernel loop at birth. The Julia Set IS the agent's geometric identity in the complex plane.

---

## Base100 / Layer Bridge

**Core file:** `retooling/src/retooling/speedlight/base100.py`

`Base100Codec`: encode/decode bytes and text in Base100 encoding.

`LayerBridge`: cross-layer encoding pipeline:

```text
L1 (JSON) ↔ L2 (Base100 + SHA256 checksum) ↔ L3 (binary struct) ↔ L4 (E8-native snap-hash + Base100)
```

Token IR service (`:10064`) exposes the full 4-layer pipeline as REST endpoints.

Gateway exposes `POST /snap/process` (tool #132) — returns `base100_layer2` field + optional `?layer=4` for E8-native encoding.

---

## Coldstart Bootstrap

**Core file:** `retooling/src/retooling/bootstrap/coldstart.py` — `ColdstartBootstrap`

7-phase bootstrap sequence. Each phase emits a `PhaseReceipt` via `MDHGHashFabric.hash_receipt()`. Module name mapping handles `cmplx_*` → `retooling.*` namespace translation. Missing modules produce partial results, not failures.

---

## CA Simulation

**Core file:** `retooling/src/retooling/simulation/ca_sim_service.py` at `:10061`

`WolframCA`: 10 independent CA channels, rules 30/54/90/110/etc.
`NiemeierPanel`: 24 panels (one per Niemeier lattice), each wrapping a CA channel.
Per-step MDHG receipt via `MDHGHashFabric.hash_at_level("Atom", panel_state_bytes)`.
MINT webhook on Wolfram Class IV (complex/interesting) pattern detection.
