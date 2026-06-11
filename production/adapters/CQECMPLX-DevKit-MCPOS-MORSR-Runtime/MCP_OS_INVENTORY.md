# MCP OS — Comprehensive Inventory

> **Generated**: 2025 | **Package**: `cmplx-mcp-os` v1.0.0 | **Python**: 3.10+
> **Total Source Files**: 35+ Python modules (~12,000+ lines)

---

## 1. Overview

The `mcp_os/` directory implements the **Model Context Protocol (MCP) server and client** for the CMPLX Unified Runtime. It exposes the CQE five-layer architecture as remotely callable tools over stdio transport, following the MCP v1.0 specification.

### Architecture Summary

```text
┌──────────────────────────────────────────────────────────────────────┐
│                        MCP OS Architecture                          │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐    stdio    ┌──────────────────────────────────────┐   │
│  │  Client   │◄──────────►│  CMPLXMCPServer                     │   │
│  │ (client/) │            │  (server/server.py)                 │   │
│  └──────────┘             │                                      │   │
│                           │  ┌────────────────────────────────┐  │   │
│  ┌──────────┐             │  │  Tool Registries               │  │   │
│  │Controller│             │  │  ├─ Layer1Tools (morphonic)    │  │   │
│  │ Proxies  │←────────────│  │  ├─ Layer2Tools (geometric)    │  │   │
│  │(control/)│             │  │  ├─ Layer3Tools (operational)   │  │   │
│  └──────────┘             │  │  ├─ Layer4Tools (governance)    │  │   │
│                           │  │  ├─ Layer5Tools (interface)     │  │   │
│  ┌──────────┐             │  │  ├─ SystemTools                │  │   │
│  │ Universal │             │  │  ├─ UniversalTools (15 tools)  │  │   │
│  │ System   │←────────────│  │  └─ CMPLXToolRegistry (37 tools)│ │   │
│  │(univrsl/)│             │  └────────────────────────────────┘  │   │
│  └──────────┘             └──────────────────────────────────────┘   │
│                                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Pipeline │  │  Codec   │  │ Adapters │  │   AGRM   │            │
│  │(modules/)│  │ (codec/) │  │(adapters)│  │  +MDHG   │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │                  Validation Framework                        │    │
│  │  runner.py → system_validator → mcp_tools_validator          │    │
│  │               → universal_system_validator                   │    │
│  │               → agrm_mdhg_validator → diagnostics            │    │
│  └──────────────────────────────────────────────────────────────┘    │
└──────────────────────────────────────────────────────────────────────┘
```

### Design Principles

| Principle | Implementation |
| ----------- | ---------------- |
| **Handle-based** | Heavy data stays server-side; clients receive lightweight handle references (prefix + hash). 1 KB threshold. |
| **5-Layer Proxy** | Client accesses L1–L5 through typed proxy objects that map to server tool calls |
| **Lazy Init** | Universal tools, AGRM/MDHG, and CMPLX integration components are initialized on first use |
| **Conservation** | All geometric transforms enforce ΔΦ ≤ 0 (conservation law) |
| **Async-First** | All tool handlers are `async`; sync wrappers provided where needed |

### Key Constants

```python
PHI = (1 + sqrt(5)) / 2    # Golden ratio — 1.618…
COUPLING = log(PHI) / 16   # ~0.03
E8_DIM = 8                 # E8 lattice dimensions
LEECH_DIM = 24             # Leech lattice dimensions
LEECH_MINIMAL = 196_560    # Minimal vectors
WEYL_CHAMBERS = 696_729_600
```

---

## 2. Directory Structure

```text
mcp_os/                              # Root package
├── __init__.py                      # Exports: CMPLXClient, create_client, ProxyRegistry
├── __main__.py                      # CLI entry: python -m mcp_os [server|client]
├── setup.py                         # Package metadata (cmplx-mcp-os v1.0.0)
├── requirements.txt                 # numpy>=1.21.0, mcp>=1.0.0, uvicorn>=0.24.0, anyio>=4.0.0
│
├── server/                          # MCP Server
│   ├── __init__.py                  # Exports: CMPLXMCPServer, create_server
│   ├── server.py          (517 ln)  # MCP server core — list_tools, call_tool, stdio transport
│   ├── tools.py           (589 ln)  # Layer 1–5 + System tool handlers, handle registry
│   └── universal_tools.py (362 ln)  # Universal tool handlers (15 tools)
│
├── client/                          # MCP Client
│   ├── __init__.py                  # Exports: CMPLXClient, create_client
│   └── client.py          (380 ln)  # Async MCP client, typed proxy methods
│
├── controllers/                     # Client-side controller proxies
│   ├── __init__.py                  # Exports: ProxyRegistry + all proxies
│   ├── registry.py        (108 ln)  # ProxyRegistry — assembles L1–L5 + FamilyManager
│   ├── proxy.py           (321 ln)  # ControllerProxy ABC + Layer1–5 Proxy classes
│   └── family_manager.py  (408 ln)  # FamilyControllerManager — 18 family profiles
│
├── universal/                       # Universal System (content → geometry)
│   ├── __init__.py                  # Exports: all universal classes
│   ├── translator.py      (480 ln)  # UniversalTranslator — 13 content types → GeometricForm
│   ├── crystal.py         (499 ln)  # Crystal + CrystalLattice (SQLite-backed storage)
│   ├── snap_atom.py       (299 ln)  # SNAPAtom, SNAPBond, SNAPTransaction, SNAPChain
│   ├── temporal.py        (523 ln)  # TemporalLayer, HypothesisEngine, Memory
│   └── identity_family.py (421 ln)  # IdentityFamily, SpeedlightReceipt, Identity
│
├── cmplx_integration/              # CMPLX toolkit tool registry
│   ├── __init__.py                  # Exports: CMPLXToolRegistry, get_cmplx_registry, register_cmplx_tools
│   ├── registry.py       (1163 ln) # CMPLXToolRegistry — 37 tools across 10 categories
│   ├── advanced_tools.py (1001 ln) # 3 advanced tools: Resonance Cascade, Knowledge Synthesis, Entropy Scan
│   └── adapters.py        (293 ln) # High-level adapters: Quorum, ThinkTank, PlanetaryDB, etc.
│
├── adapters/                        # MCP data-transfer adapters
│   ├── __init__.py                  # Exports: AdapterRegistry + all adapters
│   ├── base.py            (150 ln)  # MCPAdapter ABC + AdapterRegistry
│   ├── geometric.py       (180 ln)  # GeometricAdapter (Layer 2) — server-mandatory for Leech/Weyl
│   ├── morphonic.py       (140 ln)  # MorphonicAdapter (Layer 1) — pre-caches 10 morphons
│   └── operational.py     (140 ln)  # OperationalAdapter (Layer 3) — local MORSR for ≤8D
│
├── codec/                           # Wire-format encoding
│   ├── __init__.py                  # Exports: CMPLXEncoder, CMPLXDecoder
│   └── encoder.py         (220 ln)  # Handle-based encode/decode, 1KB threshold
│
├── modules/                         # Pipeline & storage
│   ├── __init__.py                  # Exports: Pipeline, DatabaseManager
│   ├── pipeline.py        (290 ln)  # 4-stage pipeline: Intake → Geometric → Validation → Storage
│   └── database.py        (190 ln)  # SQLite manager: handles, pipelines, audit_log tables
│
├── agrm_mdhg_integration/          # AGRM + MDHG subsystem
│   ├── __init__.py                  # Exports: all AGRM/MDHG classes
│   ├── agrm_router.py    (435 ln)  # Golden-ratio sweep scanner, zone classifier, path builder
│   ├── mdhg_ca.py         (615 ln)  # MDHGCache, CAField, cellular automata, multi-scale
│   ├── planet.py          (360 ln)  # Planet (MDHG+CA+AGRM unit), PlanetConfig, Receipt
│   └── network.py         (380 ln)  # PlanetNetwork, Ribbon (inter-planet), NetworkQuery
│
└── validation/                      # Validation framework
    ├── __init__.py                   # Exports: ValidationRunner, ValidationResult, etc.
    ├── runner.py          (200 ln)   # CLI runner (--all, --universal, --agrm, --json)
    ├── system_validator.py(351 ln)   # SystemValidator orchestrator + ValidationSuite/Result
    ├── mcp_tools_validator.py(381 ln)# MCPToolsValidator — tests every MCP tool
    ├── universal_system_validator.py(530 ln) # UniversalSystemValidator — translator/crystal/snap/temporal
    ├── agrm_mdhg_validator.py(752 ln)# AGRMMDHGValidator — MDHG/CA/AGRM/Planet/Network tests
    ├── diagnostics.py     (296 ln)   # SystemDiagnostics — real-time health + resource checks
    ├── README.md                     # Validation documentation
    ├── benchmarks/                   # (empty — reserved for perf benchmarks)
    ├── diagnostics/                  # (empty — reserved for diagnostic reports)
    └── tests/                        # (empty — reserved for test data)
```

---

## 3. Tool Registry — Complete Inventory

### 3a. MCP Server Tools (server/tools.py + server/universal_tools.py)

These are the tools exposed via the MCP protocol through `CMPLXMCPServer`. Total: **33 tools**.

#### Layer 1 — Morphonic Foundation (3 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 1 | `l1_morphon_generate` | `seed: str` | `{handle, dr, phi_quality}` | Generate a Universal Morphon (M₀) from a single-digit seed |
| 2 | `l1_mglc_execute` | `expression: str, context: dict` | `{handle, result_type, reduction_steps}` | Execute a Morphonic Lambda Calculus expression |
| 3 | `l1_seed_expand` | `digit: int, dimensions: int=24` | `{handle, dimensions, norm, dr}` | Expand a single digit into a 24D substrate vector |

#### Layer 2 — Geometric Engine (4 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 4 | `l2_e8_project` | `vector: list[float](8D), return_format: str` | `{handle, lattice, nearest_root, distance, dr}` | Project vector onto E8 lattice (240 roots) |
| 5 | `l2_leech_nearest` | `vector: list[float](24D), return_format: str` | `{handle, lattice, distance, shell}` | Find nearest Leech lattice point (196,560 minimal vectors) |
| 6 | `l2_weyl_navigate` | `position: list[float](8D)` | `{handle, chamber, reflections}` | Navigate E8 Weyl chambers (696,729,600 chambers) |
| 7 | `l2_niemeier_classify` | `vector: list[float](24D)` | `{handle, top_lattice, all_scores}` | Classify vector across all 24 Niemeier lattices |

#### Layer 3 — Operational Systems (2 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 8 | `l3_morsr_optimize` | `initial_state: list[float], iterations: int=100` | `{handle, final_norm, phi_quality, iterations}` | Run MORSR geometric optimization |
| 9 | `l3_conservation_check` | `before: list[float], after: list[float]` | `{delta_phi, conserved, phi_before, phi_after}` | Check conservation law compliance (ΔΦ ≤ 0) |

#### Layer 4 — Governance (3 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 10 | `l4_digital_root` | `number: int, modulus: int=9` | `{digital_root, meaning, sequence}` | Calculate digital root (DR 0–9) with semantic meaning |
| 11 | `l4_seven_witness` | `artifact: dict` | `{witnesses, all_valid, confidence}` | Multi-perspective validation via 7 witness types |
| 12 | `l4_policy_check` | `artifact_id: str, policy_tier: int` | `{tier_name, compliant, violations}` | Check compliance against policy hierarchy |

#### Layer 5 — Interface (3 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 13 | `l5_embed` | `content: str, domain: str` | `{handle, content_hash, e8_projection_norm}` | Embed arbitrary content into E8 geometric space |
| 14 | `l5_query_similar` | `handle: str, top_k: int=10` | `{results, total_candidates, query_handle}` | Find similar overlays by geometric resonance |
| 15 | `l5_transform` | `handle: str, operator: str` | `{handle, operator, delta_phi, conserved}` | Apply geometric transform (rotation, reflection, etc.) |

#### System Tools (3 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 16 | `sys_info` | (none) | `{system, version, layers, constants}` | System information and configuration |
| 17 | `sys_cache_stats` | (none) | `{handles_cached, memory_estimate}` | Handle cache statistics |
| 18 | `sys_resolve_handle` | `handle: str` | `{data}` or error | Resolve handle to full server-side data |

#### Universal Tools (15 tools)

| # | Tool Name | Parameters | Returns | Description |
| --- | ----------- | ----------- | --------- | ------------- |
| 19 | `universal_translate` | `content: any, content_type: str, identity: str` | `{handle, atom_count, bond_count, symmetry}` | Translate any content to GeometricForm via UniversalTranslator |
| 20 | `crystal_store` | `geometric_form_handle: str, name: str, tags: list` | `{crystal_id, name, atom_count}` | Store a GeometricForm as a Crystal in CrystalLattice |
| 21 | `crystal_retrieve` | `crystal_id: str` | `{crystal, found}` | Retrieve a Crystal by ID |
| 22 | `crystal_resonance_query` | `crystal_id: str, threshold: float, max_results: int` | `{matches, query_crystal}` | Find crystals with resonance above threshold |
| 23 | `crystal_merge` | `crystal_ids: list[str], name: str` | `{merged_crystal}` | Merge multiple crystals into one |
| 24 | `temporal_query` | `time_range: str, phase: str` | `{events, count}` | Query temporal layer by time range and phase |
| 25 | `temporal_remember` | `content: str, identity: str, tags: list` | `{memory_id, stored}` | Store a memory in the temporal layer |
| 26 | `hypothesis_generate` | `question: str, context: dict` | `{hypothesis_id, prior, description}` | Generate a hypothesis with prior probability |
| 27 | `hypothesis_validate` | `hypothesis_id: str, evidence: dict` | `{posterior, status, evidence_count}` | Validate hypothesis against evidence (Bayesian update) |
| 28 | `temporal_counterfactual` | `hypothesis_id: str, changes: dict` | `{counterfactual, original}` | Generate counterfactual scenario |
| 29 | `identity_register` | `name: str, role: str` | `{identity_id, public_key}` | Register a new identity with cryptographic keys |
| 30 | `identity_history` | `identity_id: str` | `{actions, reputation}` | Get identity action history and reputation |
| 31 | `audit_provenance` | `crystal_id: str` | `{provenance_chain, creator, receipts}` | Full provenance audit trail for a crystal |
| 32 | `verify_receipt` | `receipt_hash: str` | `{valid, receipt, timestamp}` | Verify a SpeedlightReceipt by hash |
| 33 | `universal_stats` | (none) | `{crystals, identities, hypotheses, memories}` | Aggregate statistics across all universal subsystems |

---

### 3b. CMPLX Integration Registry (cmplx_integration/registry.py)

These are the tools registered via `CMPLXToolRegistry` and connected to the `cmplx_toolkit` backend. Total: **37 tools** across 10 categories.

#### Quorum (3 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 1 | `quorum_deliberate` | quorum | `question: str, context: dict, min_confidence: float` | Run multi-agent quorum deliberation on a question |
| 2 | `quorum_check_cache` | quorum | `question: str` | Check if a quorum result is cached |
| 3 | `quorum_clear_cache` | quorum | (none) | Clear the quorum deliberation cache |

#### Think Tank (8 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 4 | `think_tank_status` | think_tank | (none) | Get Think Tank status (running, circuit breaker, pending proposals) |
| 5 | `think_tank_start` | think_tank | (none) | Start the Think Tank background loop |
| 6 | `think_tank_stop` | think_tank | (none) | Stop the Think Tank background loop |
| 7 | `think_tank_run_session` | think_tank | `focus_area: str` | Run a single Think Tank session with optional focus area |
| 8 | `think_tank_get_proposals` | think_tank | `status: str` | Get Think Tank proposals filtered by status |
| 9 | `think_tank_approve_proposal` | think_tank | `proposal_id: str` | Approve a pending proposal |
| 10 | `think_tank_reject_proposal` | think_tank | `proposal_id: str, reason: str` | Reject a pending proposal with reason |
| 11 | `think_tank_get_history` | think_tank | `limit: int` | Get Think Tank session history |

#### Agent Orchestration (4 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 12 | `agent_list_profiles` | agent_orchestration | (none) | List available sub-agent profiles |
| 13 | `agent_start` | agent_orchestration | `profile_name: str, task: str` | Start a sub-agent with a task |
| 14 | `agent_status` | agent_orchestration | `agent_id: str` | Check status of a running agent |
| 15 | `agent_stop` | agent_orchestration | `agent_id: str` | Stop a running agent |

#### Planetary Database (4 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 16 | `planetary_admit` | planetary_db | `content: str, metadata: dict, tags: list` | Admit content to Planetary Database with geometric embedding |
| 17 | `planetary_query` | planetary_db | `query: str, threshold: float, limit: int` | Query Planetary Database by semantic/geometric similarity |
| 18 | `planetary_store_crystal` | planetary_db | `crystal_data: dict, tags: list` | Store a pre-formed crystal directly |
| 19 | `planetary_get_stats` | planetary_db | (none) | Get Planetary Database statistics |

#### Receipts (2 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 20 | `receipt_verify_chain` | receipts | (none) | Verify the entire receipt hash chain integrity |
| 21 | `receipt_get_recent` | receipts | `limit: int` | Get most recent receipts |

#### Health (2 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 22 | `health_check` | health | (none) | Full system health check |
| 23 | `health_component` | health | `component: str` | Check health of a specific component |

#### TMN — Thalamic Matching Network (4 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 24 | `tmn_learn` | tmn | `input_data: list[float], target: list[float]` | Train TMN on an input→target pair |
| 25 | `tmn_state` | tmn | (none) | Get TMN state: epoch, mutual information, dimensions |
| 26 | `tmn_save` | tmn | `path: str` | Save TMN weights to file |
| 27 | `tmn_load` | tmn | `path: str` | Load TMN weights from file |

#### Geometric (3 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 28 | `l2_project_e8` | geometric | `vector: list[float]` | Project vector to E8 lattice |
| 29 | `l2_nearest_leech` | geometric | `vector: list[float]` | Find nearest Leech lattice point |
| 30 | `l2_digital_root` | geometric | `number: int` | Calculate digital root (DR 0–9) |

#### Governance (2 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 31 | `governance_validate` | governance | `artifact: dict` | Validate artifact against governance framework |
| 32 | `governance_meaning` | governance | `number: int` | Get governance meaning of a digital root |

#### Advanced (3 tools)

| # | Tool Name | Category | Parameters | Description |
| --- | ----------- | ---------- | ----------- | ------------- |
| 33 | `resonance_cascade_query` | advanced | `query: str, min_resonance: float, max_results: int, include_harmonics: bool` | E8 geometric resonance search with harmonic octaves across crystals |
| 34 | `autonomous_knowledge_synthesis` | advanced | `source_crystal_ids: list, query: str, synthesis_depth: int, create_proposal: bool, tags: list` | Multi-crystal → quorum deliberation → TMN learning → synthesis crystal pipeline |
| 35 | `system_entropy_scan` | advanced | `scan_depth: str, include_predictions: bool` | Deep geometric conservation law diagnostics with anomaly detection and future issue prediction |

#### Reserved Registration Slots

Tools 36–37 are reserved registration slots in the registry for additional geometric/governance helpers.

---

## 4. Tool Detail — Per Tool

### 4.1 Server-Side Tool Classes

All server tools inherit from `ToolRegistry` base class which provides:

```python
class ToolRegistry:
    """Base tool registry with routing and handle management."""
    PREFIX: str              # Tool name prefix for routing
    _HANDLE_REGISTRY: dict   # In-memory handle → data store (global)

    def _generate_handle(prefix, data) -> str   # SHA256-based handle
    def _resolve_handle(handle) -> dict | None  # Lookup server-side data
    async def handle(name, arguments, data_root) -> dict  # Route to handler
```

| Class | File | Prefix | Layer | Tools |
| ------- | ------ | -------- | ------- | ------- |
| `Layer1Tools` | server/tools.py | `l1_` | Morphonic | 3 |
| `Layer2Tools` | server/tools.py | `l2_` | Geometric | 4 |
| `Layer3Tools` | server/tools.py | `l3_` | Operational | 2 |
| `Layer4Tools` | server/tools.py | `l4_` | Governance | 3 |
| `Layer5Tools` | server/tools.py | `l5_` | Interface | 3 |
| `SystemTools` | server/tools.py | `sys_` | System | 3 |
| `UniversalTools` | server/universal_tools.py | (exact match) | Universal | 15 |

Global singletons: `LAYER1_TOOLS`, `LAYER2_TOOLS`, `LAYER3_TOOLS`, `LAYER4_TOOLS`, `LAYER5_TOOLS`, `SYSTEM_TOOLS`, `UNIVERSAL_TOOLS`.

### 4.2 CMPLXToolRegistry Pattern

```python
@dataclass
class ToolDefinition:
    name: str                # Unique tool name
    description: str         # Human/agent-readable description
    handler: Callable        # async handler(args, registry) → dict
    parameters: dict         # JSON Schema for input parameters
    returns: dict            # JSON Schema for return value
    category: str            # Category grouping
```

Registration: `self.register(ToolDefinition(...))`.
Lookup: `registry.get_tool(name)`, `registry.list_tools(category=...)`.
MCP binding: `register_cmplx_tools(server)` iterates all tools and registers with `server.tool(name, description)`.

### 4.3 Advanced Tools — Deep Dive

#### `resonance_cascade_query` (ResonanceCascadeQuery)

**Purpose**: Finds crystals whose E8 geometric resonance exceeds a threshold, then computes harmonic octaves (PHI^n scaling).

**Flow**:

1. Convert query text to 8D E8 embedding
2. Scan all crystals in Planetary DB
3. Compute resonance score = cosine_similarity × phi_correction
4. For matches ≥ `min_resonance`, generate harmonic octaves at PHI^1, PHI^2, PHI^3 scales
5. Return ranked results with geometric metadata

**Classes**: `ResonanceCascadeQuery`, `E8ProjectionCache`, `HarmonicOctave`

#### `autonomous_knowledge_synthesis` (AutonomousKnowledgeSynthesis)

**Purpose**: Fully automated knowledge pipeline that reads crystals, runs quorum deliberation, trains TMN, and stores a synthesis crystal.

**Flow**:

1. Identify source crystals (by IDs or query)
2. Build synthesis prompt from crystal contents
3. Run quorum multi-agent deliberation on the prompt
4. Extract TMN training pairs from synthesis
5. Feed training pairs into TMN
6. Store synthesis result as a new crystal
7. (Optional) Create a Think Tank proposal

**Depth levels**: 1 = common themes, 2 = emergent insights, 3 = deep synthesis (contradictions + higher-order principles)

#### `system_entropy_scan` (SystemEntropyScanner)

**Purpose**: Treat the CMPLX system as a geometric manifold and detect conservation law violations indicating problems.

**Scans**:

1. PlanetaryDB health (crystal/planet ratio → entropy)
2. Think Tank health (circuit breaker, proposal backlog)
3. TMN health (epoch, mutual information, learning efficiency)
4. Receipt chain integrity
5. Geometric conservation (component energy vectors, imbalances)
6. Cross-component energy flow analysis
7. Anomaly detection
8. Future issue prediction

**Conservation checks**: ΔΦ ≤ 0 (Law 1), receipt chain valid (Law 2), TMN coherence > 0 (Law 3).

---

## 5. Universal Modules

### 5.1 UniversalTranslator (`universal/translator.py` — 480 lines)

Converts **any content** into a `GeometricForm` (atoms + bonds) for geometric processing.

**Supported Content Types** (13):

| Content Type | Input | Translation Method |
| ------------- | ------- | ------------------- |
| `text` | String | Character/word-level tokenization → atoms |
| `code` | String | AST parsing → structural atoms + dependency bonds |
| `math` | String | Symbol extraction → mathematical atoms |
| `audio` | Array | Spectral decomposition → frequency atoms |
| `image` | Array | Patch extraction → pixel-region atoms |
| `video` | Array | Frame extraction → temporal atoms |
| `mesh` | Dict | Vertex/edge extraction → mesh atoms |
| `json` | Dict/List | Recursive key/value → structural atoms |
| `filesystem` | Path | File/directory → hierarchical atoms |
| `process` | Dict | Step/stage → process atoms |
| `concept` | String | Word tokenization → concept atoms |
| `hypothesis` | String | Claim decomposition → hypothesis atoms |
| `memory` | String | Recall decomposition → memory atoms |

**Key Classes**:

- `GeometricForm`: atoms (list[SNAPAtom]), bonds (list[SNAPBond]), envelope (dict), symmetry_signature (str)

- Auto-detection: `_detect_content_type(content)` — examines input type and structure

### 5.2 Crystal + CrystalLattice (`universal/crystal.py` — 499 lines)

**Crystal** — Immutable geometric data unit:

```python
@dataclass
class Crystal:
    crystal_id: str           # Unique ID (cryst_<hash>)
    name: str                 # Human-readable name
    atoms: list[SNAPAtom]     # Geometric atoms
    bonds: list[SNAPBond]     # Inter-atom bonds
    resonance_signature: list[float]  # Fixed-length resonance vector
    temporal_phase: str       # "past" | "present" | "future"
    provenance: list[str]     # Chain of creator IDs
    tags: list[str]           # Searchable tags
    created_at: str           # ISO timestamp
```

**Methods**: `vibrate(frequency) → Crystal` (phase-shift), `resonance_with(other) → float` (cosine similarity of resonance signatures)

**CrystalLattice** — SQLite-backed holographic storage:

- `store(crystal)` → persist

- `retrieve(crystal_id)` → Crystal

- `query_by_resonance(signature, threshold)` → list[Crystal]

- `query_by_phase(phase)` → list[Crystal]

- `query_by_tags(tags)` → list[Crystal]

- `merge(crystals, name)` → Crystal (combine atoms/bonds)

### 5.3 SNAP Atom System (`universal/snap_atom.py` — 299 lines)

**SNAPAtom** — Minimal geometric information unit:

```python
@dataclass
class SNAPAtom:
    identity: str        # Creator/owner identity hash
    morphon_seed: int    # Single-digit morphonic seed (0–9)
    position: list[float]  # 24D coordinate in Leech space
    charge: float        # Energy charge (-1.0 to 1.0)
    content: Any         # Payload
    atom_type: str       # Classification tag
```

**SNAPBond** — Directional connection: `source_id → target_id` with `strength` (0–1) and `bond_type`.

**SNAPTransaction** — Immutable record: `tx_id`, `atoms`, `bonds`, `receipt_hash`, `digital_root`, `parent_tx`, `timestamp`.

**SNAPChain** — DAG of transactions:

- `submit(tx)` → validate + append

- `get_by_identity(identity)` → list[tx]

- `get_by_signature(sig)` → list[tx]

- `verify_integrity()` → bool

### 5.4 Temporal Layer (`universal/temporal.py` — 523 lines)

**TemporalCoordinate**: `phase` (past/present/future), `certainty` (0–1), `branch_id`, `entropy`.

**Hypothesis**: Prior/posterior probability, evidence list, `confirm(evidence)` / `refute(evidence)` → Bayesian update.

**Memory**: `content`, `decay_rate`, `reliability`, `reinforcement_count`, `recall()` → reinforce + return.

**HypothesisEngine**: Create, validate, list hypotheses. Tracks active/confirmed/refuted.

**TemporalLayer**:

- `query(time_range, phase)` → events in temporal window

- `remember(content, identity)` → create Memory

- `generate_hypothesis(question, context)` → new Hypothesis

- `counterfactual(hypothesis_id, changes)` → alternate-timeline result

### 5.5 Identity Family (`universal/identity_family.py` — 421 lines)

**SpeedlightReceipt**: Cryptographic proof of action:

```python
@dataclass
class SpeedlightReceipt:
    receipt_hash: str    # SHA256 of action
    actor_id: str        # Who performed
    action: str          # What was done
    target: str          # What was affected
    timestamp: str       # When (ISO)
    digital_root: int    # DR of the action
    signature: str       # Cryptographic signature
```

**Identity**: `identity_id`, `name`, `role`, `public_key`, `reputation` (0–1), `crystal_ids` (owned), `created_at`.

**IdentityFamily** — orchestrator:

- `register(name, role)` → new Identity

- `get_history(identity_id)` → actions + reputation

- `audit_provenance(crystal_id)` → full chain from creation

- `verify_receipt(receipt_hash)` → bool + receipt details

- Integrates SNAP, Speedlight, Crystal, Temporal subsystems

---

## 6. Pipeline

### Module: `modules/pipeline.py` (290 lines)

Four-stage processing pipeline for content entering the MCP OS:

```text
 Input Content
      │
      ▼
┌────────────┐
│   Intake   │  Validate input, detect type, create PipelineContext
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Geometric  │  Translate content → GeometricForm via UniversalTranslator
└─────┬──────┘
      │
      ▼
┌────────────┐
│ Validation │  Conservation check (ΔΦ ≤ 0), governance, digital root
└─────┬──────┘
      │
      ▼
┌────────────┐
│  Storage   │  Store as Crystal in CrystalLattice + handle generation
└────────────┘
```

**Key Classes**:

- `PipelineContext`: data, metadata dict, handles dict, errors list, timestamps dict

- `PipelineStage(ABC)`: `async process(context) → context`

- `IntakeStage`: Input validation + type detection

- `GeometricStage`: Universal translation to GeometricForm

- `ValidationStage`: Conservation + governance checks

- `StorageStage`: Crystal storage + handle generation

- `Pipeline`: Composes stages sequentially, supports `add_stage()` for custom stages

### Module: `modules/database.py` (190 lines)

**DatabaseManager** — lightweight SQLite storage for metadata (NOT heavy data):

| Table | Purpose | Columns |
| ------- | --------- | --------- |
| `handles` | Handle → metadata mapping | handle_id, handle_type, metadata_json, created_at |
| `pipelines` | Pipeline execution records | pipeline_id, status, context_json, started_at, completed_at |
| `audit_log` | All actions for compliance | action_id, actor, action_type, target, details_json, timestamp |

---

## 7. Adapters

### MCP Data-Transfer Adapters (`adapters/`)

Determine when to use local computation vs. server-side MCP calls.

| Adapter | Layer | Local Capability | Server Mandatory For |
| --------- | ------- | ------------------- | --------------------- |
| `MorphonicAdapter` | L1 | Pre-caches 10 morphons, basic seed expansion | Distributed morphon operations |
| `GeometricAdapter` | L2 | E8 projection (local approximation) | Leech lattice (196,560 vectors), Weyl chambers (696M) |
| `OperationalAdapter` | L3 | MORSR for small states (≤8D, ≤1000 iterations) | Large-state MORSR, cross-layer conservation |

**Base**: `MCPAdapter(ABC)` — `layer` property, `initialize()`, local result cache.
**Registry**: `AdapterRegistry` — maps layer number → adapter instance. `get(layer)`, `register(layer, adapter)`.

### CMPLX Integration Adapters (`cmplx_integration/adapters.py`)

High-level adapters bridging MCP tools to `cmplx_toolkit` backends:

| Adapter | Wraps | Key Methods |
| --------- | ------- | ------------- |
| `QuorumAdapter` | `QuorumEngine` | `deliberate()`, `check_cache()`, `clear_cache()` |
| `ThinkTankAdapter` | `ThinkTankLoop` | `start()`, `stop()`, `run_session()`, `approve/reject()` |
| `PlanetaryDBAdapter` | `PlanetaryDatabase` | `admit()`, `query()`, `store_crystal()`, `get_stats()` |
| `ReceiptAdapter` | `ReceiptLedger` | `verify_chain()`, `get_recent()` |
| `HealthAdapter` | `HealthChecker` | `full_check()`, `component_check()` |
| `TMNAdapter` | `TMN` | `learn()`, `state()`, `save()`, `load()` |
| `FamilyAdapter` | `FamilyControllerManager` | `list_families()`, `discover()` |

**`CMPLXAdapterBundle`**: Bundles all adapters into a single object for convenience.

---

## 8. Codec

### Module: `codec/encoder.py` (220 lines)

Handle-based wire-format encoding for MCP communication.

**Classes**:

- `HandleMetadata`: type_hint, byte_size, content_hash, created_at

- `HandleReference`: handle string + HandleMetadata

- `CMPLXEncoder`: Encodes data → `HandleReference` or inline content

- `CMPLXDecoder`: Decodes `HandleReference` → data (server lookup)

**Threshold**: 1 KB

- Below 1 KB → content sent inline

- Above 1 KB → handle-only mode (data stays server-side)

---

## 9. AGRM + MDHG Integration

### 9.1 MDHG Cache (`agrm_mdhg_integration/mdhg_ca.py` — 615 lines)

**MDHGCache**: Maps 24D vectors to a 2D slot grid via double hashing.

```python
MDHGCache(grid_side=64, cap_per_slot=16)
  .admit(v24, meta) → {"admit": bool, "slot": (r,c), "key": str}
  .query(v24, radius) → list[matches]
  .evict_lru(slot)
  .get_stats() → {"total_items", "evictions", "grid_side", ...}
```

**Quantization**: `quantize(v24, bins=64)` → list[int] (24 integers in [0, bins)).

**MDHGMultiScale**: Three cache layers with different resolutions:

- `fast` (grid_side=32, cap=8) — hot data

- `med` (grid_side=64, cap=16) — warm data

- `slow` (grid_side=128, cap=32) — cold data

### 9.2 Cellular Automata (`agrm_mdhg_integration/mdhg_ca.py`)

**CACell**: `state` (float), 4 channels (`c0`–`c3`), `last_update`.
**CAField**: 2D grid of CACells with kernel-based updating.

```python
CAField(grid_side=64)
  .step(kernel)            # Apply 3×3 kernel convolution
  .inject(r, c, value)     # Inject value at position
  .snapshot() → 2D array   # Get current field state
  .energy() → float        # Total field energy
```

**CAFieldMultiScale**: Multiple overlapping CA fields at different resolutions.
**WolframAssignment**: Maps digital roots (0–9) to Wolfram CA rules for governance-driven evolution.

### 9.3 AGRM Router (`agrm_mdhg_integration/agrm_router.py` — 435 lines)

**Golden-Ratio Spiral Sweep**:

```python
AGRMSweepScanner(slots, max_radius)
  .sweep(origin, direction) → list[AGRMNode]  # PHI-spiral scan
```

Scans slots along a golden-ratio spiral: each step at angle `2π/PHI²` and radius `r × PHI^step`.

**AGRMZoneClassifier**: Classifies MDHG slots into zones:

- `hot`: frequently accessed

- `warm`: moderate access

- `cold`: rarely accessed

- `archive`: near-zero access

**AGRMPathBuilder**: Builds optimal paths between two MDHG slots using zone-weighted A* search.

**AGRMRouter**: Combines Scanner + Classifier + PathBuilder for full routing.

### 9.4 Planet (`agrm_mdhg_integration/planet.py` — 360 lines)

A **Planet** is an MDHG + CA + AGRM unit — a self-contained geometric compute node.

```python
Planet(config: PlanetConfig)
  .admit(v24, meta) → Receipt     # Admit vector, update CA, generate receipt
  .query(v24, radius) → list      # AGRM-routed query
  .step_dynamics() → dict         # Advance CA field by one step
  .get_state() → dict             # Full planet state
  .get_receipt(receipt_id) → Receipt
```

**PlanetConfig**: `planet_id`, `grid_side`, `cap_per_slot`, `ca_kernel`, `agrm_max_radius`.

**Receipt**: Immutable proof of admission: `receipt_id`, `planet_id`, `slot`, `timestamp`, `digital_root`.

### 9.5 Network (`agrm_mdhg_integration/network.py` — 380 lines)

**PlanetNetwork**: Multi-planet coordination layer.

```python
PlanetNetwork()
  .add_planet(planet) → str           # Register planet
  .connect(p1_id, p2_id, ribbon) → str  # Create inter-planet link
  .route(query_v24, origin_planet) → list[results]  # Cross-planet query
  .global_stats() → dict              # Aggregate network stats
```

**Ribbon**: Bidirectional communication channel between planets:

- `ribbon_id`, `source_planet`, `target_planet`, `bandwidth`, `latency`

- `transfer(data)` → Receipt

**NetworkQuery**: Orchestrates cross-planet queries with hop limits and bandwidth constraints.

---

## 10. Controllers (Client-Side Proxies)

### ProxyRegistry (`controllers/registry.py`)

Central access point for all controller proxies:

```python
registry = ProxyRegistry(client)
registry.l1   # → Layer1Proxy (morphonic operations)
registry.l2   # → Layer2Proxy (geometric operations)
registry.l3   # → Layer3Proxy (operational systems)
registry.l4   # → Layer4Proxy (governance)
registry.l5   # → Layer5Proxy (interface)
registry.families  # → FamilyControllerManager
```

### Layer Proxies (`controllers/proxy.py`)

| Proxy | Methods |
| ------- | --------- |
| `Layer1Proxy` | `generate_morphon(seed)`, `execute_mglc(expression, context)`, `expand_seed(digit, dims)` |
| `Layer2Proxy` | `project_e8(vector)`, `nearest_leech(vector)`, `navigate_weyl(position)`, `classify_niemeier(vector)` |
| `Layer3Proxy` | `morsr_optimize(state, iters)`, `check_conservation(before, after)` |
| `Layer4Proxy` | `digital_root(number)`, `seven_witness(artifact)`, `policy_check(artifact_id, tier)` |
| `Layer5Proxy` | `embed(content, domain)`, `query_similar(handle, top_k)`, `transform(handle, operator)` |

### FamilyControllerManager (`controllers/family_manager.py` — 408 lines)

Discovers and manages **18 family profiles** from donor code builds:

| Family | Controller Layer | Adapter Type | Keywords |
| -------- | ----------------- | -------------- | ---------- |
| `agrm_mdhg` | L2 (geometric) | geometric | AGRM, MDHG, cache |
| `aletheia` | L5 (interface) | interface | consciousness, AI |
| `cmplx` | L1 (morphonic) | morphonic | runtime, core |
| `complex_t` | L2 (geometric) | geometric | complex numbers |
| `cqe` | L1 (morphonic) | morphonic | CQE, unified |
| `e8` | L2 (geometric) | geometric | E8, lattice, roots |
| `eqai` | L5 (interface) | interface | equitable AI |
| `lattice` | L2 (geometric) | geometric | lattice, vectors |
| `lfai` | L4 (governance) | governance | LFAI, ethics |
| `lsdt` | L3 (operational) | operational | LSDT, transform |
| `morphonic` | L1 (morphonic) | morphonic | morphon, seed |
| `promutate_construct` | L3 (operational) | operational | promutate |
| `quadratic_frame` | L2 (geometric) | geometric | quadratic, frame |
| `quorum` | L4 (governance) | governance | quorum, consensus |
| `snap` | L1 (morphonic) | morphonic | SNAP, atom |
| `snaplat` | L2 (geometric) | geometric | SNAP lattice |
| `tarpit` | L3 (operational) | operational | tarpit, Turing |
| `uhp` | L4 (governance) | governance | UHP, protocol |

---

## 11. Validation Framework

### Runner (`validation/runner.py`)

CLI for running validation suites:

```bash
python -m mcp_os.validation.runner --all              # Run everything
python -m mcp_os.validation.runner --universal         # Universal System only
python -m mcp_os.validation.runner --agrm --mdhg       # AGRM+MDHG only
python -m mcp_os.validation.runner --all --json --output results.json
```

### Validators

| Validator | File | Tests | Components Covered |
| ----------- | ------ | ------- | -------------------- |
| `SystemValidator` | system_validator.py | Orchestrator | MCP, Universal, AGRM/MDHG, Integration, Performance |
| `MCPToolsValidator` | mcp_tools_validator.py | 24 tests | All 33 MCP server tools (L1–L5, System, Universal, Planet) |
| `UniversalSystemValidator` | universal_system_validator.py | 15 tests | Translator (4 types), Crystal (3), SNAP (2), Temporal (3), Identity (3) |
| `AGRMMDHGValidator` | agrm_mdhg_validator.py | 19 tests | MDHG (4), CA Field (4), AGRM (4), Planet (4), Network (3) |

### Diagnostics (`validation/diagnostics.py`)

Real-time health monitoring:

```python
diag = SystemDiagnostics()
report = diag.run_full_diagnostics()
# → HealthReport with components: system_resources, python_env, dependencies,
#   filesystem, mcp_server, universal_system, agrm_mdhg
```

Checks:

- CPU/memory/disk via `psutil`

- Python version and environment

- Required dependencies (`numpy`, `mcp`) and optional (`psutil`, `matplotlib`)

- Filesystem structure verification

- MCP server module loading

- Universal System component loading

- AGRM+MDHG module loading

---

## 12. Integration Points

### CMPLX Toolkit ↔ MCP OS

| MCP OS Component | CMPLX Toolkit Module | Integration |
| ------------------ | --------------------- | ------------- |
| `CMPLXToolRegistry` | `cmplx_toolkit.quorum.engine` | Quorum deliberation engine |
| `CMPLXToolRegistry` | `cmplx_toolkit.autonomy.think_tank` | Think Tank loop + proposals |
| `CMPLXToolRegistry` | `cmplx_toolkit.autonomy.receipts` | Receipt ledger + chain verification |
| `CMPLXToolRegistry` | `cmplx_toolkit.autonomy.snap_roles` | SNAP role definitions |
| `CMPLXToolRegistry` | `cmplx_toolkit.autonomy.llm_bridge` | LLM execution bridge |
| `CMPLXToolRegistry` | `cmplx_toolkit.utils.health` | Health checker |
| `CMPLXToolRegistry` | `cmplx_toolkit.config` | ToolkitConfig |
| `PersistentMemory` | `mcp_os.universal.crystal` | CrystalLattice storage backend |
| `CMPLXAgent` | `mcp_os.cmplx_integration.registry` | Tool binding via registry |

### CQE Runtime ↔ MCP OS

| MCP OS Tool | CQE Runtime Module | Purpose |
| ------------- | ------------------- | --------- |
| `l1_morphon_generate` | `layer1_morphonic/morphon.py` | Universal Morphon generation |
| `l1_mglc_execute` | `layer1_morphonic/mglc.py` | Lambda calculus execution |
| `l1_seed_expand` | `layer1_morphonic/seed_generator.py` | Seed → 24D substrate |
| `l2_e8_project` | `layer2_geometric/e8/` | E8 lattice operations |
| `l2_leech_nearest` | `layer2_geometric/leech/` | Leech lattice operations |
| `l2_weyl_navigate` | `layer2_geometric/weyl/` | Weyl chamber navigation |
| `l2_niemeier_classify` | `layer2_geometric/niemeier/` | Niemeier lattice classification |
| `l3_morsr_optimize` | `layer3_operational/morsr.py` | MORSR optimization |
| `l3_conservation_check` | `layer3_operational/conservation.py` | Conservation law enforcement |
| `l4_digital_root` | `layer4_governance/gravitational.py` | Digital root system |
| `l4_seven_witness` | `layer4_governance/seven_witness.py` | Multi-witness validation |
| `l4_policy_check` | `layer4_governance/policy_hierarchy.py` | Policy enforcement |
| `l5_embed` | `layer5_interface/sdk.py` | Content embedding |
| `l5_query_similar` | `layer5_interface/sdk.py` | Similarity search |
| `l5_transform` | `layer5_interface/sdk.py` | Geometric transform |

### External Dependencies

| Dependency | Version | Required | Purpose |
| ----------- | --------- | ---------- | --------- |
| `numpy` | ≥1.21.0 | Yes | All numerical/geometric operations |
| `mcp` | ≥1.0.0 | Yes | MCP protocol implementation |
| `uvicorn` | ≥0.24.0 | Yes | ASGI server |
| `anyio` | ≥4.0.0 | Yes | Async I/O |
| `aiosqlite` | any | Optional | Async SQLite for CrystalLattice |
| `psutil` | any | Optional | System diagnostics |
| `matplotlib` | any | Optional | Visualization |

---

## 13. Summary Statistics

| Metric | Count |
| -------- | ------- |
| **Total Python source files** | 35+ |
| **Total lines of code** | ~12,000+ |
| **MCP Server tools** | 33 |
| **CMPLX Integration tools** | 37 |
| **Combined unique tool surface** | ~55 (some intentional overlap in geometric/governance) |
| **Universal content types** | 13 |
| **Supported family profiles** | 18 |
| **Validation test cases** | 58+ |
| **Pipeline stages** | 4 |
| **Database tables** | 3 |
| **AGRM/MDHG components** | 12 classes |
| **Adapter types** | 10 (3 MCP + 7 CMPLX integration) |

---

*End of MCP OS Inventory.*
