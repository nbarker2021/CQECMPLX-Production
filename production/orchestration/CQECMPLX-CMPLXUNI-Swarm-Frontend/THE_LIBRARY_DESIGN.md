# The Library - Document Processing System

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP SERVER CHAIN                              │
│  Unified MCP Server (26 tools)                                   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (tool call: library.ingest)
┌─────────────────────────────────────────────────────────────────┐
│              THE LIBRARY (Docker Container)                      │
│  Port: 8902                                                      │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Document Ingestion Pipeline                               │ │
│  │  1. Document Reader (.md, .txt, .docx, .pdf)               │ │
│  │  2. Chunking Engine (semantic + structural)                │ │
│  │  3. RAG Card Creator (CMPLX method)                        │ │
│  │  4. Atomic Form Definer (10 contracts)                     │ │
│  │  5. Morphonic Form Generator (λ-calculus)                  │ │
│  │  6. MDHG Stratification (10-layer hierarchy)               │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Quality Validation Gates (6 falsifiers)                   │ │
│  │  F1: Type validation                                       │ │
│  │  F2: Conservation law (ΔΦ ≤ 0)                             │ │
│  │  F3: Lattice snap verification                             │ │
│  │  F4: Receipt chain integrity                               │ │
│  │  F5: Semantic coherence                                    │ │
│  │  F6: MDHG address validity                                 │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Storage Layer                                             │ │
│  │  - Raw documents (/library/documents)                      │ │
│  │  - RAG cards (/library/rag_cards)                          │ │
│  │  - Atomic forms (/library/atomic_forms)                    │ │
│  │  - Morphonic forms (/library/morphonic_forms)              │ │
│  │  - MDHG database (/library/mdhg.db)                        │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              SWARM AGENT ASSIGNMENTS                             │
│  Alpha  → Document reading & chunking                            │
│  Beta   → RAG card creation                                      │
│  Gamma  → Atomic form definition                                 │
│  Delta  → Morphonic form generation                              │
│  All    → MDHG stratification & quality validation               │
└─────────────────────────────────────────────────────────────────┘
```

---

## MCP Tools (New)

| Tool | Description |
|------|-------------|
| `library.ingest` | Ingest document into Library |
| `library.create_rag_cards` | Create RAG cards from document |
| `library.define_atomic_forms` | Define atomic forms (10 contracts) |
| `library.generate_morphonic_forms` | Generate morphonic λ-forms |
| `library.stratify_mdhg` | MDHG 10-layer stratification |
| `library.validate_quality` | Run 6 quality gates |
| `library.search` | Search processed documents |
| `library.get_report` | Get analysis report |

---

## File Structure

```
the-library/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── library_server.py          # FastAPI server
│   ├── document_reader.py         # Document ingestion
│   ├── chunking_engine.py         # Semantic chunking
│   ├── rag_card_creator.py        # RAG card creation
│   ├── atomic_form_definer.py     # 10 atomic contracts
│   ├── morphonic_form_generator.py # λ-calculus forms
│   ├── mdhg_stratifier.py         # 10-layer MDHG
│   ├── quality_gates.py           # 6 falsification gates
│   └── storage.py                 # Document storage
├── library/
│   ├── documents/                 # Raw documents
│   ├── rag_cards/                 # RAG cards
│   ├── atomic_forms/              # Atomic forms
│   ├── morphonic_forms/           # Morphonic forms
│   └── mdhg.db                    # MDHG SQLite database
└── scripts/
    └── start.sh                   # Startup script
```

---

## Quality Gates (No Shitty Work)

### F1: Type Validation
- Verify all type contracts match
- Check input/output schemas

### F2: Conservation Law (ΔΦ ≤ 0)
- Energy must not increase
- Verify geometric conservation

### F3: Lattice Snap Verification
- E8 lattice projection valid
- Digital root correct

### F4: Receipt Chain Integrity
- Merkle chain unbroken
- All receipts present

### F5: Semantic Coherence
- Chunks semantically coherent
- No fragmentation

### F6: MDHG Address Validity
- All 10 layers populated
- Hamiltonian path valid

---

## Usage

### Ingest Document
```bash
curl -X POST http://localhost:8902/library/ingest \
  -H "Content-Type: application/json" \
  -d '{"path": "/docs/my_document.md", "collection": "my_docs"}'
```

### Create RAG Cards
```bash
curl -X POST http://localhost:8902/library/rag_cards \
  -H "Content-Type: application/json" \
  -d '{"document_id": "doc_123", "chunk_size": 512}'
```

### Validate Quality
```bash
curl -X POST http://localhost:8902/library/validate \
  -H "Content-Type: application/json" \
  -d '{"document_id": "doc_123"}'
```

---

**Status:** Ready for implementation
