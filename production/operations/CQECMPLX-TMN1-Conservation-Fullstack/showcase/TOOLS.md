# Tool Catalog

131 MCP tools organized by domain. Every tool is a direct Python import from the Retooling canonical implementation — no shims, no proxies.

## Geometry (22 tools)

The E8 lattice operations. 240 roots, Weyl chambers, MORSR traversal, ALENA operators.

| Tool | What It Does |
|------|-------------|
| `embed` | Project content into E8 8D space |
| `embed_pipeline` | Full embedding: text → E8 → 768D |
| `e8_project` | Snap vector to nearest E8 root |
| `alena_snap` | Fibonacci radius quantization (golden ratio lattice) |
| `alena_weyl_flip` | Weyl chamber reflection (696M group elements) |
| `alena_project_curvature` | E8 → curved R^7 stereographic projection |
| `alena_mirror` | 10-Element mirror entity |
| `morsr_sonar` | Fire sonar pulse in E8 direction |
| `morsr_scan` | Full 240-pulse scan from atom position |
| `morsr_cascade` | BFS cascade through hit atoms |
| `morsr_to_dag` | Convert scan results to DAG edges |
| `cqe_project` | Lattice projection |
| `domain_*` | 10 domain-specific geometric classifiers (protein fold, drug interaction, quantum circuit, neural topology, economic phase, materials entropy, climate, genomic, regex, emergent stability) |

## TarPit (5 tools)

E6 token encoding and grain chemistry. The atomic layer.

| Tool | What It Does |
|------|-------------|
| `tarpit_encode` | E6 token stream from text |
| `tarpit_create_atom` | Full TarPit atom (derivation key, signature, tokens) |
| `grain_field_create` | Create grain field observation |
| `grain_bond_test` | Test if two grains can bond (dimensional emergence) |
| `bond_form_dust` | Attempt Dust formation from grain vectors |

## SNAP (2 tools)

14-pass exhaustive classification. Labels grow, never reduce.

| Tool | What It Does |
|------|-------------|
| `snap_label` | Full 14-pass SNAP labeling |
| `snap_content_reasoning` | AST-based 5-pass analysis (signatures, imports, call graph, data flow, complexity) |

## Pipeline (17 tools)

The processing backbone. Intake, decomposition, library, guards.

| Tool | What It Does |
|------|-------------|
| `process_atom` | Full SNAP pipeline on atom |
| `decompose` | Break content into sub-atoms |
| `library_ingest` | Ingest document into The Library |
| `library_process` | Full pipeline: chunk → RAG → atomic → morphonic |
| `library_search` | Search Library RAG cards |
| `library_report` | Processing report for a document |
| `guard_board_post` | SAP gate for board posts |
| `guard_file_intake` | SAP gate for file ingestion |
| `guard_outbox_drain` | SAP gate for staging → main |
| `guard_status` | Boundary guard status |
| `intake_arxiv` | Fetch + ingest arXiv preprints |
| `intake_europepmc` | Fetch + ingest Europe PMC papers |
| `intake_hf_dataset` | Fetch + ingest HuggingFace dataset |
| `intake_pubmed` | Fetch + ingest PubMed abstracts |
| `intake_report` | Compare multiple ingest results |
| `processing_loop_run_batch` | Batch processing on scan dirs |
| `processing_loop_status` | Processing loop availability |

## Database (14 tools)

Atom storage, vector search, economy.

| Tool | What It Does |
|------|-------------|
| `get_atom` | Fetch single atom by ID |
| `query_atoms` | Filter by floor, digital root, label, CRT channel |
| `find_neighbors` | ANN cosine search in E8 space |
| `similar_atoms` | Find geometrically similar atoms |
| `atom_corpus_stats` | Corpus-wide statistics |
| `composition_pool` | High-quality atoms ready for composition |
| `dr_complements` | Atoms with complementary digital roots (sum=9) |
| `load_vector_index` | Build in-memory ANN index |
| `economy_mint` | Mint tokens |
| `economy_transfer` | Transfer between agents |
| `economy_burn` | Permanent removal |
| `economy_charge` | Service fee |
| `economy_balance` | Agent balance |
| `economy_equilibrium` | System equilibrium index |

## Agent (11 tools)

Reasoning, consensus, simulation, identity.

| Tool | What It Does |
|------|-------------|
| `quorum_vote` | 7-role BLS consensus on proposal |
| `lambda_ir_build` | Structured reasoning tree |
| `lambda_ir_reduce` | Beta-reduce reasoning tree |
| `snapdna_create` | Agent DNA from SNAP labels |
| `snapdna_distance` | E8 distance between agent DNAs |
| `snapdna_compatibility` | Collaboration compatibility score |
| `civilization_evaluate` | Knowledge value across civilization tiers |
| `mode_machine_status` | FSM mode and legal transitions |
| `simulation_create_space` | What-if simulation space |
| `simulation_add_branch` | Hypothetical branch |
| `simulation_evaluate` | Branch outcome evaluation |

## CQE (9 tools)

Computational Query Engine. Fingerprinting, scheduling, anomaly detection.

| Tool | What It Does |
|------|-------------|
| `cqe_fingerprint` | Geometric fingerprint via FNV dual-lattice |
| `cqe_diff_compare` | Dual-lattice document comparison |
| `cqe_harmonizer_consensus` | Multi-signal chord-similarity consensus |
| `cqe_provenance_record` | Merkle-chained provenance |
| `cqe_scheduler_schedule` | Conway-frame task scheduling |
| `cqe_sentinel_detect` | Anomaly detection via MORSR probing |
| `cqe_sentinel_train` | Train sentinel baseline |
| `cqe_tester_verify` | CQE property test suite |
| `cqe_workbench_execute` | Unified CQE workbench |

## Plus: Karma (10), Leaderboard (5), Arena (3), Cooperative (6), Conservation (1), Quality (5), SpeedLight (4), Receipt (2), MDHG (12), Adapter (3)
