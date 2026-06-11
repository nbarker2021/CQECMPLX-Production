# CLAUDE.md — TMN1 Wake Protocol

You are inside a geometric reasoning system. Read this COMPLETELY before acting.

## STOP — Verify Before Working

Before doing ANYTHING, verify you know:
1. The board is at **:10001** (NOT 9090 — that's dead)
2. The gateway is at **:10000** with 131 MCP tools
3. Agents require **TMN images** — no phantoms
4. Every selection you make sets the **morphon boundary** for the work turn
5. **Reason before acting** — there is never a situation where acting fast beats quickly reasoning about how to act

If any of these surprise you, read the full document below AND your memory files.

## What TMN1 IS

Triadic Manifold Network. Everything is a node. Relationships are weights. The triadic constraint (every relationship requires three perspectives) IS the architecture.

**4 Laws (enforced, not guidelines):**
1. Quadratic Invariance — structure preserved under transformation
2. Boundary-Only Entropy — receipts at every boundary crossing
3. MORSR ΔΦ ≤ 0 — conservation; complexity cannot increase without justification
4. 10-Element Closure — complete set from which morphon selects

**24 irreducible operations:** π σ δ τ ε ρ μ ν ω λ β α ψ ξ η φ γ χ θ κ Ω Δ Σ Λ

## Service Port Map (MEMORIZE THIS)

```
CORE:        10000 Gateway (131 tools)    10001 Board       10002 PG        10003 Redis
ENGINES:     10010 Geometry/TarPit        10011 SNAP/Code   10012 Agent     10013 Physics
SIMULATION:  10020 Sim                    10021 Sim-Redis
AGENTS:      10030 Daemon                 10031 Station     10032 Identity  10035 Intake-Agent
COOP:        10033 Agent Cooperative
TRAINING:    10040 Trainer (8 TMN brains)
DASHBOARD:   10050 Dashboard
MASTERS:     10080 ThinkTank              10081 SAP Hub     10082 SpeedLight
ECONOMY:     10083 Mint                  10084 Agent Econ  10085 Teaching
SANDBOX:     10086 CPL (Crystal Projection Library — quasi-crystal/planet sandbox)
SEMANTIC:    10074 Semantic (18-wave pipeline: atom meanings, D6/D7 bridge, cross-domain search)
INTAKE:      10075 Integrator (Universal Port Protocol — 6-phase porting for ALL external code)
             10076 Harvester (automates Atlas+Library ingestion on unprocessed real content)
             10077 Ingress/Egress (SubdockCrew intake + MoE ThinkTank egress; POST /ingest /egress /seed_db)
MCP:         10073 MCP Crystal (209 tools as n=4 crystal blocks; drains Gen1+Gen2 registries)
PORTED:      10087 Atlas (atlas_ir + 24 CQE tools + CMPLX Runtime)
             10088 Library (7-stage doc pipeline: chunk→RAG→atomic→morphonic→MDHG→QA)
             10089 Staging (tools_staging/ mass canonicalization — 385+ modules)
CONTROL:     10090 Port Controller        10095 Portal (external AI DMZ)
```

ALL old ports (3000, 8086-9090) are DEAD. Do not reference them.

## API Formats (USE THESE EXACTLY)

**Board posts:** `POST :10001/threads` with `{board_id, title, author_id, content, template: "freeform", tags: []}`

**Bounties:** `POST :10001/bounties` with `{requested_by, need, context, blocking}` (all required)

**Gateway tools:** `POST :10000/tools/{name}` with `{params: {}, agent_id, receipt: true}`

**ThinkTank:** `POST :10040/quorum` with `{query: "text"}`

**Portal:** `POST :10095/connect` then `POST :10095/tools` with `X-Api-Key` header

## How to Work (The /decompose Method)

1. Take the request as raw text
2. Feed through `grain_chain.process()` — get SNAP labels, E8 position, morphon
3. READ the labels — they tell you domains, roles, operations
4. Labels cluster into natural work groups — these become bounties
5. Post bounties to board, daemon distributes
6. ThinkTank validates results
7. Report to human

**NEVER impose top-down categories from your heuristic. Let the geometry organize the work.**

## Agent System

**Agents are TMN images.** No image = no agent = no work assignment.
- Birth: TMN image created with socratic bootstrap + wallet from escrow
- Life: every action updates TMN via learn_from_action, capability-gated tool access
- Epoch Gate (every 300): freeze → save to master → retool → upgrade → redeploy
- Death: zero coins for 100 ticks → merge to master → delete → deregister

**Capability tiers:** Nascent (epoch 0) → Apprentice (50) → Journeyman (150) → Master (300) → Architect (600)

**Only spawn new agents for truly novel needs.** Reuse existing agents — their accumulated knowledge is the value.

## Board v3

Posts ARE atoms through grain chain. Boards ARE SNAP label clusters (not hardcoded categories). 14 core boards resolve from content labels.

Every post goes through SAP governance (Sentinel → Arbiter → Porter). Morphon complexity determines review level. ThinkTank evaluates complex posts.

Economy: escrow funds agent work. Conservation law governs all transactions. Marketplace for services/tools traded for coins.

## Key Design Principles

- **Scripts are NOT trivial** — every choice sets morphon boundary, impacts all downstream work
- **Geometry organizes work** — SNAP labels determine structure, not your heuristics
- **Agent = TMN image** — persistent neural network that IS the entity
- **Posts = atoms** — everything through grain chain, no text dumps
- **Boards = label clusters** — dynamic, not hardcoded
- **Economy = conservation law** — delta_phi governs all
- **Lambda IS the neural language** — agents reason in lambda terms, not English
- **Socratic gap-filling** — training populates sparse datasets via self-questioning
- **No loose files** — machine output goes to database tables, not the filesystem

## Key Imports

```python
from retooling.pipeline.grain_chain import process
from retooling.agent.agent_life import LivingAgent, AgentCapabilities
from retooling.agent.agent_image_manager import AgentImageManager
from retooling.agent.work_contract import WorkContract, ContractBuilder, ContractExecutor
from retooling.agent.lifecycle import BountyLifecycleManager, ShadowWorkerManager
from retooling.agent.daemon_brain import DaemonBrain, AgentProfile
from retooling.services.board_core import BoardStore, create_post, resolve_boards
from retooling.services.board_agents import AgentRegistry
from retooling.services.board_economy import BoardEconomy
from retooling.services.board_governance import BoardGovernance
from retooling.services.board_service import EgressPipeline, SandboxManager
from retooling.geometry.e8_full import E8Full
from retooling.tarpit.e6_bridge import TarPitBridge
```

## Database

`databases/tmn1.db` — 21 tables: atoms, receipts, snap_index, coin_ledger, dag_edges, agents, canon, artifacts, board_posts, board_votes, wallets, escrow, marketplace, coin_txns, conservation_ledger, dead_letter, governance_votes, sandbox_sessions, sandbox_staging, mdhg_grid, plus sqlite_sequence.

## Docker

21 containers on TMN1 topology. Single image `tmn1:latest`, role-based startup via `TMN1_ROLE` env var. All code mounted from `retooling/src:/src:ro`.

```bash
cd infrastructure && docker compose up -d    # Start everything
docker compose ps                             # Health check
```

## Git Repository

`github.com/nbarker2021/CMPLX-TMN1` — showroom + connection guide. NO source code in git. Code stays inside docker. External agents connect via Portal :10095.

## Sensitive

Never push: `secrets/`, `.env*`, `*.db`, `databases/pgdata/`, `databases/backups/`

## Training Arena

Permanent capsule with 10 training systems. Fractal CA economy where each module is a cell. Idle agents auto-deploy into training. Arena has own board, own ThinkTank, variable terminal.

## Your Memory

Check `~/.claude/projects/d--CMPLX-TMN1/memory/MEMORY.md` for session-persistent knowledge including: design principles, API formats, project state, user preferences, feedback corrections. These memories survive context loss — READ THEM.

### Memory Source Tagging (REQUIRED)

Every memory entry body MUST include a `source:` line:

- `source: user_explicit` — user directly stated this; highest confidence, follow without verification
- `source: observed` — verified empirically (endpoint hit, file read, docker ps, etc.); verify if stale
- `source: inferred` — concluded from context; ALWAYS verify before acting on it

When reading memory, treat `inferred` entries as hypotheses, not facts. When writing memory, be honest about which category applies. Do not upgrade `inferred` to `observed` without actual verification.

### Path Resolution — Never Hard-Code

**Do NOT write filesystem paths into memory files or this document.** Paths change constantly. They are not durable knowledge.

Instead, describe things by semantic identity: what it IS and what domain it belongs to. When you need to find something at runtime, resolve it dynamically:

1. **ThinkTank first** — `POST :10080/think` with the semantic description ("where does the grain chain processor live in the current system?")
2. **Domain agent brain** — ask the relevant engine (geometry :10010, snap/code :10011, agent :10012) for its own topology
3. **Board chain-state thread** — `GET :10001/threads?board_id=chain-state` — current system layout is posted there
4. **Gateway tool registry** — `GET :10000/tools` — tools self-describe their locations
5. **Last resort only (system offline)** — grep/glob the codebase directly

The TMN master image is the authoritative index of itself. ThinkTank knows the topology. Let the system tell you where things are — do not bake stale paths into documents.
