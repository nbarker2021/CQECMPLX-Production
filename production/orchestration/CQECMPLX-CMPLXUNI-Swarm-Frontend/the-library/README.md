# The Library - Complete Documentation

## 🎯 Overview

**The Library** is a dedicated document processing system integrated into your CMPLX MCP server chain. It processes text documents through a comprehensive pipeline with quality validation at every step.

### **Key Features**

✅ **RAG Card Creation** - CMPLX method with E8 embeddings
✅ **Atomic Form Definition** - 10 atomic contracts
✅ **Morphonic Form Generation** - λ-calculus forms
✅ **MDHG Stratification** - 10-layer hierarchy
✅ **Quality Validation** - 6 falsification gates (NO SHITTY WORK)
✅ **Swarm Agent Integration** - 4 agents process documents collaboratively

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP SERVER CHAIN (34 tools)                   │
│  Unified MCP Server                                              │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼ (tool call: library.*)
┌─────────────────────────────────────────────────────────────────┐
│              THE LIBRARY (Document Processing)                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Document → Chunks → RAG Cards → Atomic → Morphonic → MDHG│ │
│  └───────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Quality Gates (F1-F6) - NO SHITTY WORK                    │ │
│  │  F1: Type │ F2: ΔΦ≤0 │ F3: E8 │ F4: Receipt │ F5: Semantic│ │
│  │  F6: MDHG                                                  │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              SWARM AGENTS (4 Agents Processing)                  │
│  Alpha  → Reading & Chunking                                     │
│  Beta   → RAG Cards & Embeddings                                 │
│  Gamma  → Atomic Forms & Receipts                                │
│  Delta  → Morphonic Forms & MDHG                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ MCP Tools (8 New Tools)

| Tool | Description | Example |
|------|-------------|---------|
| `library.ingest` | Ingest document into The Library | `library.ingest(file_path="/docs/my.md")` |
| `library.create_rag_cards` | Create RAG cards with E8 embeddings | `library.create_rag_cards(document_id="doc_123")` |
| `library.define_atomic_forms` | Define 10 atomic contracts | `library.define_atomic_forms(document_id="doc_123")` |
| `library.generate_morphonic_forms` | Generate λ-calculus forms | `library.generate_morphonic_forms(document_id="doc_123")` |
| `library.stratify_mdhg` | Create 10-layer MDHG hierarchy | `library.stratify_mdhg(document_id="doc_123")` |
| `library.validate_quality` | Run 6 quality gates | `library.validate_quality(document_id="doc_123")` |
| `library.search` | Search processed documents | `library.search(query="quantum")` |
| `library.get_report` | Get processing report | `library.get_report(document_id="doc_123")` |

---

## 📋 Document Processing Pipeline

### **Step 1: Document Ingestion (Alpha)**
```python
# Ingest document
document = await library.ingest_document("/docs/my_document.md")

# Returns:
{
  "document_id": "doc_abc123",
  "title": "My Document",
  "word_count": 1500,
  "status": "pending"
}
```

### **Step 2: Chunking (Alpha)**
```python
# Chunk by structure and size
chunks = chunker.chunk(content, method="hybrid")

# Returns: List of chunks
[
  {"chunk_index": 0, "content": "...", "word_count": 256},
  {"chunk_index": 1, "content": "...", "word_count": 312}
]
```

### **Step 3: RAG Card Creation (Beta)**
```python
# Create RAG card with E8 embedding
card = rag_creator.create_card(document_id, chunk, chunk_index)

# Returns RAGCard with:
{
  "card_id": "rag_doc_abc123_0001",
  "embedding": [0.1, -0.2, ...],  # 768D
  "e8_projection": [0.3, -0.1, ...],  # 8D
  "digital_root": 7
}
```

### **Step 4: Atomic Form Definition (Gamma)**
```python
# Define 10 atomic contracts
forms = atomic_definer.define_atomic_forms(card)

# Returns 10 forms:
[
  {"contract": "dim_adapt", "input_dim": 768, "output_dim": 8},
  {"contract": "typed_bridge", "input_type": "text", "output_type": "vector"},
  {"contract": "receipt_wrapper", "receipt_id": "rcpt_abc123"},
  {"contract": "lattice_type_cast", "src": "text", "dst": "E8"},
  {"contract": "graph_to_causal", ...},
  {"contract": "term_to_graph", ...},
  {"contract": "seal_and_fingerprint", ...},
  {"contract": "orbit_expand", ...},
  {"contract": "delta_phi_decorator", "delta_phi": -0.05},
  {"contract": "dual_rail_inverse", ...}
]
```

### **Step 5: Morphonic Form Generation (Delta)**
```python
# Generate λ-calculus forms
forms = morphonic_generator.generate_forms(card)

# Returns 3 forms:
[
  {"form": "M0_universal_morphon", "lambda_expr": "λx...."},
  {"form": "MGLC_morphonic_lambda", "lambda_term": "λabc.body"},
  {"form": "observation_functor", "maps_to": "E8_7"}
]
```

### **Step 6: MDHG Stratification (All Agents)**
```python
# Create 10-layer hierarchy
address = mdhg_stratifier.stratify(card, document)

# Returns MDHG address:
{
  "atom": "rag_doc_abc123_0001",
  "room": "room_doc_abc123_0",
  "floor": "floor_my_document",
  "building": "building_my_doc",
  "city": "city_library",
  "planet": "planet_documents",
  "velocity": 0.5,
  "dimension": 7,
  "lattice": "E8",
  "universe": "CMPLX_Library",
  "hamiltonian_path": ["atom:...", "room:...", ...]
}
```

### **Step 7: Quality Validation (6 Gates)**
```python
# Run all 6 quality gates
report = quality_gates.validate(card, document)

# Returns:
{
  "passed": True,
  "gates": {
    "f1_type_validation": (True, "Type validation passed"),
    "f2_conservation_law": (True, "ΔΦ ≤ 0 satisfied"),
    "f3_lattice_snap": (True, "E8 lattice snap valid"),
    "f4_receipt_chain": (True, "Receipt chain intact"),
    "f5_semantic_coherence": (True, "Semantic coherence valid"),
    "f6_mdhg_address": (True, "MDHG address valid")
  },
  "overall_score": 1.0,
  "issues": []
}
```

---

## 🚫 Quality Gates (NO SHITTY WORK)

### **Automatic Rejection Criteria**

Any output is **REJECTED** if:

| Gate | Check | Rejection Criteria |
|------|-------|-------------------|
| **F1: Type Validation** | Types match schemas | Empty content, missing embedding, < 10 atomic forms |
| **F2: Conservation Law** | ΔΦ ≤ 0 | Energy increases (ΔΦ > 0) |
| **F3: Lattice Snap** | E8 projection valid | Missing or invalid E8 projection |
| **F4: Receipt Chain** | Merkle chain intact | Missing receipt ID |
| **F5: Semantic Coherence** | Chunks coherent | < 10 words, no complete sentences |
| **F6: MDHG Address** | All layers present | < 10 layers populated |

### **Retry Logic**

1. **1st failure**: Agent retries with adjusted parameters
2. **2nd failure**: Escalates to different agent
3. **3rd failure**: Marks as FAILED, logs issue, queues for human review

---

## 💬 Chat Commands

### **Full Pipeline**
```
"Process this document through The Library: /docs/my_doc.md"
→ Ingests, chunks, creates RAG cards, defines atomic forms,
  generates morphonic forms, stratifies MDHG, validates quality
```

### **Specific Tasks**
```
"Beta, create RAG cards for document doc_123"
→ Creates E8 embeddings and stores in MMDB

"Gamma, define atomic forms for doc_123"
→ Defines all 10 atomic contracts with receipts

"Delta, generate morphonic forms for doc_123"
→ Generates λ-calculus forms

"Validate quality for doc_123 - no shitty work"
→ Runs all 6 quality gates
```

### **Search**
```
"Search The Library for 'quantum computing'"
→ Returns matching RAG cards with similarity scores
```

---

## 📁 File Structure

```
the-library/
├── docker-compose.yml          # Docker configuration
├── Dockerfile                   # Container definition
├── requirements.txt             # Python dependencies
├── src/
│   └── library_server.py        # Main library implementation
├── library/
│   ├── documents/               # Raw documents
│   ├── rag_cards/               # RAG cards (JSON)
│   ├── atomic_forms/            # Atomic forms (JSON)
│   ├── morphonic_forms/         # Morphonic forms (JSON)
│   └── mdhg.db                  # MDHG SQLite database
└── scripts/
    └── start.sh                 # Startup script
```

---

## 🔧 Usage Examples

### **Python API**
```python
from library_server import TheLibrary

library = TheLibrary()

# Ingest document
doc = await library.ingest_document("/docs/my_doc.md")

# Process full pipeline
results = await library.process_document(doc.document_id)

# Get report
report = library.get_report(doc.document_id)

# Search
matches = library.search("quantum computing", limit=10)
```

### **MCP Tool Calls**
```python
# Via unified MCP server
result = await server.call_tool(
    name="library.process_full_pipeline",
    arguments={"file_path": "/docs/my_doc.md"}
)
```

### **REST API** (when Docker is running)
```bash
# Ingest document
curl -X POST http://localhost:8902/library/ingest \
  -H "Content-Type: application/json" \
  -d '{"file_path": "/docs/my_doc.md"}'

# Get report
curl http://localhost:8902/library/report/doc_abc123

# Search
curl "http://localhost:8902/library/search?query=quantum&limit=10"
```

---

## 📊 Performance Targets

| Metric | Target | Description |
|--------|--------|-------------|
| Documents/hour | 100 | Processing throughput |
| RAG cards/second | 50 | Card creation rate |
| Quality pass rate | ≥ 95% | Must pass 6 gates |
| Atomic forms/card | 10 | All contracts defined |
| Morphonic forms/card | 3 | All forms generated |
| MDHG layers | 10 | Full stratification |
| Hamiltonian path | Valid | Navigation valid |

---

## 🐛 Troubleshooting

### **Document fails quality validation**
```
Issue: Document fails F5 (semantic coherence)
Solution: Check chunk size - ensure > 10 words and complete sentences
```

### **Missing atomic forms**
```
Issue: < 10 atomic forms defined
Solution: Check atomic_definer - all 10 contracts must be defined
```

### **MDHG address incomplete**
```
Issue: < 10 layers in MDHG address
Solution: Check mdhg_stratifier - all layers must be populated
```

### **ΔΦ > 0 (conservation violation)**
```
Issue: Energy increases (ΔΦ > 0)
Solution: Review delta_phi_decorator - must ensure ΔΦ ≤ 0
```

---

## 🔗 Integration Points

| System | Integration |
|--------|-------------|
| **MCP Server** | 8 library.* tools added |
| **Swarm Agents** | Alpha/Beta/Gamma/Delta assignments |
| **Vector MMDB** | RAG cards stored with E8 embeddings |
| **ThinkTank** | Analysis of morphonic forms |
| **Quality Gates** | 6 falsifiers enforced |

---

## 📝 Next Steps

1. **Start Docker container**
   ```bash
   cd /home/borker/CMPLXUNI-external/the-library
   docker-compose up -d
   ```

2. **Test document processing**
   ```bash
   curl -X POST http://localhost:8902/library/ingest \
     -d '{"file_path": "/docs/test.md"}'
   ```

3. **Assign swarm agents**
   - Alpha: Reading/chunking
   - Beta: RAG cards
   - Gamma: Atomic forms
   - Delta: Morphonic + MDHG

4. **Monitor quality**
   ```bash
   curl http://localhost:8902/library/report/doc_abc123
   ```

---

**License:** MIT | **Version:** 1.0.0-library | **Tools:** 8 (library.*) | **Quality Gates:** 6 (F1-F6)
