# CMPLX Expanded Swarm System - Complete Documentation

## 🎯 Overview

Your **massively concurrent, batched, iteration-based, recursion-based exploration system** is now fully operational!

### **System Capabilities**

✅ **4-Agent Qwen Swarm** - Alpha, Beta, Gamma, Delta
✅ **Vector Embedding Creation** - E8 lattice based embeddings
✅ **MMDB Vector Storage** - Weaviate-like storage using your work
✅ **Automated Data Creation/Storage/Recall** - Full pipeline
✅ **Massively Concurrent Batch Processing** - 50 concurrent workers
✅ **Recursion-Based Deep Exploration** - 10 depth levels
✅ **26 MCP Tools** - All accessible via chat

---

## 📊 Tool Inventory (26 Total)

### **CQE Geometric Tools (8)**
| Tool | Description |
|------|-------------|
| `cqe.sentinel.detect` | Geometric anomaly detection |
| `cqe.diff.compare` | Document comparison |
| `cqe.scheduler.orchestrate` | Task scheduling |
| `cqe.provenance.record` | Provenance tracking |
| `cqe.harmonizer.consensus` | Multi-signal consensus |
| `cqe.theory.query` | Query 2,474 CQE formalizations |
| `cqe.tester.verify` | Property verification |
| `cqe.workbench.execute` | Unified orchestrator |

### **Swarm Control Tools (9)**
| Tool | Description |
|------|-------------|
| `swarm.spawn` | Spawn agent swarm |
| `swarm.deliberate` | ThinkTank + Swarm deliberation |
| `swarm.coordinate` | Multi-agent coordination |
| `swarm.query_status` | Query swarm status |
| `swarm.gather_consensus` | Gather consensus |
| `swarm.chat_send` | Send chat to swarm |
| `swarm.chat_receive` | Receive from swarm |
| `thinktank.analyze` | ThinkTank analysis |
| `cmplx_agent.execute` | CMPLX agent execution |

### **Vector MMDB Tools (5)** 🆕
| Tool | Description |
|------|-------------|
| `vector.create_embedding` | Create E8-based embedding |
| `vector.store_vector` | Store vector in MMDB |
| `vector.search_similar` | Similarity search |
| `vector.process_batch` | Batch process & store |
| `vector.create_collection` | Create vector collection |

### **Concurrent Exploration Tools (4)** 🆕
| Tool | Description |
|------|-------------|
| `exploration.process_batch` | Massively concurrent batch |
| `exploration.explore_recursive` | Recursive deep exploration |
| `exploration.search` | Search stored data |
| `exploration.get_stats` | Get exploration stats |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                  DIRECT CHAT INTERFACE                           │
│  You + Qwen Code → Natural language commands                     │
│  "Create embeddings for these documents"                         │
│  "Run batch processing on 1000 items"                            │
│  "Explore recursively to depth 5"                                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│              UNIFIED MCP SERVER (26 tools)                       │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ 8 CQE Tools  │ │ 9 Swarm      │ │ 5 Vector     │            │
│  │ Geometric AI │ │   Control    │ │   MMDB       │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│  ┌──────────────────────────────────────────────────┐           │
│  │ 4 Concurrent Exploration Tools                   │           │
│  │ - Batch Processing (50 concurrent)               │           │
│  │ - Recursive Exploration (depth 10)               │           │
│  └──────────────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  Qwen Swarm      │ │  Vector MMDB     │ │  Exploration     │
│  4 Agents        │ │  SQLite + Cache  │ │  Engine          │
│  Alpha/Beta/     │ │  E8 Projections  │ │  Batch/Recursive │
│  Gamma/Delta     │ │  DR Indexing     │ │  50 Concurrent   │
└──────────────────┘ └──────────────────┘ └──────────────────┘
        │                     │                     │
        └─────────────────────┴─────────────────────┘
                              │
                              ▼
                ┌────────────────────────┐
                │      Redis Pub/Sub     │
                │    Message Bus         │
                └────────────────────────┘
```

---

## 🚀 Quick Start

### **1. MCP Configured** ✅
Your Qwen Code MCP config is at: `/home/borker/.qwen/mcp.json`

### **2. Qwen Swarm Running** ✅
```
Web GUI: http://localhost:3000
Coordinator: http://localhost:5000
Redis: localhost:6379
```

### **3. Test the Server**
```bash
cd /home/borker/CMPLXUNI-external
.venv/bin/python src/cmplx/mcp/unified_mcp_server.py
```

---

## 💬 Chat Commands

### **Swarm Control**
- "Spawn a swarm to analyze this codebase"
- "Query swarm status"
- "Run deliberation on the architecture"
- "Gather consensus on deployment"
- "Tell the swarm: hello agents!"

### **Vector Embeddings**
- "Create embedding for this text: ..."
- "Store this vector with metadata {...}"
- "Search for similar vectors to: ..."
- "Process batch of documents"
- "Create a collection named 'my_docs'"

### **Batch Processing**
- "Process batch of 1000 items"
- "Run batch processing on these documents"
- "What are the batch stats?"

### **Recursive Exploration**
- "Explore recursively from this root"
- "Deep explore to depth 5"
- "Get exploration statistics"

---

## 🔧 API Usage Examples

### **Create Vector Embeddings**

```python
import asyncio
from cmplx.mcp.vector_mmdb_tools import CMPLXEmbedder, MMDBVectorStore

async def main():
    embedder = CMPLXEmbedder(embedding_dim=768)
    vector_store = MMDBVectorStore()
    
    # Create embedding
    text = "Machine learning with E8 lattice theory"
    embedding = embedder.embed_text(text, method="e8_hash")
    
    print(f"Vector dimension: {len(embedding['vector'])}")
    print(f"E8 projection: {embedding['e8_projection']}")
    print(f"Digital root: {embedding['digital_root']}")
    
    # Store in MMDB
    record_id = vector_store.insert(
        embedding=embedding,
        metadata={"source": "test", "category": "ml"},
        tags=["machine-learning", "e8"]
    )
    print(f"Stored as: {record_id}")

asyncio.run(main())
```

### **Massively Concurrent Batch Processing**

```python
from cmplx.mcp.concurrent_exploration_tools import BatchIterationEngine

async def main():
    # 50 concurrent workers, 100 items per batch
    engine = BatchIterationEngine(max_concurrency=50, batch_size=100)
    
    # Items to process
    items = [{"text": f"Document {i}", "index": i} for i in range(1000)]
    
    # Processor function
    async def processor(item):
        await asyncio.sleep(0.01)  # Simulate work
        return {"processed": item["text"]}
    
    # Run batch
    result = await engine.process_batch(items, processor, "test_batch")
    
    print(f"Processed: {result.tasks_completed}/{result.tasks_total}")
    print(f"Duration: {result.duration_seconds:.2f}s")
    print(f"Throughput: {result.tasks_completed/result.duration_seconds:.1f} items/sec")

asyncio.run(main())
```

### **Recursive Deep Exploration**

```python
from cmplx.mcp.concurrent_exploration_tools import RecursiveExplorer

async def main():
    # Max depth 10, 20 concurrent branches
    explorer = RecursiveExplorer(max_depth=10, max_concurrency=20)
    
    # Root data
    root = {"type": "root", "query": "Explore codebase"}
    
    # Expand function (generates children)
    async def expand_fn(data, depth):
        if depth >= 5:
            return []
        # Generate 3 children per node
        return [{"type": "node", "depth": depth+1, "id": i} for i in range(3)]
    
    # Visit function (processes each node)
    async def visit_fn(data, depth):
        print(f"Visiting depth {depth}: {data}")
    
    # Run exploration
    result = await explorer.explore(root, expand_fn, visit_fn)
    
    print(f"Total nodes: {result.total_nodes}")
    print(f"Max depth: {result.max_depth}")
    print(f"Duration: {result.duration_seconds:.2f}s")

asyncio.run(main())
```

### **Automated Data Factory**

```python
from cmplx.mcp.concurrent_exploration_tools import AutomatedDataFactory

async def main():
    factory = AutomatedDataFactory()
    
    # Create and store batch
    items = [
        {"text": f"Document {i}", "category": f"cat_{i%10}"}
        for i in range(100)
    ]
    
    result = await factory.create_and_store_batch(
        items=items,
        collection_name="my_collection",
        text_field="text"
    )
    
    print(f"Collection: {result['collection_id']}")
    print(f"Stored: {result['items_stored']} items")
    
    # Search
    results = await factory.recall_with_context(
        query="document 5",
        limit=5
    )
    
    for r in results:
        print(f"Similarity: {r['similarity']:.3f} - {r['metadata']}")
    
    # Stats
    stats = factory.get_factory_stats()
    print(f"Total vectors: {stats['vector_store']['total_vectors']}")

asyncio.run(main())
```

---

## 📊 Performance Characteristics

| Component | Specification |
|-----------|---------------|
| **Batch Concurrency** | 50 concurrent workers |
| **Batch Size** | 100 items per batch |
| **Recursive Depth** | Max 10 levels |
| **Branch Concurrency** | 20 parallel branches |
| **Embedding Dimension** | 768 (configurable) |
| **E8 Projection** | 8-dimensional |
| **Digital Root Index** | 10 partitions (0-9) |
| **Vector Storage** | SQLite + in-memory cache |
| **Similarity Search** | Cosine, Euclidean, Lattice distance |

---

## 🗄️ MMDB Vector Storage

### **Storage Structure**

```
mmdb/vector_store.db
├── vectors (table)
│   ├── record_id (PK)
│   ├── vector (BLOB - JSON encoded)
│   ├── e8_projection (BLOB - 8D vector)
│   ├── content_hash (indexed)
│   ├── digital_root (indexed 0-9)
│   ├── metadata (JSON)
│   ├── created_at
│   └── tags (JSON)
├── collections (table)
│   ├── collection_id (PK)
│   ├── name
│   ├── description
│   └── metadata
├── collection_vectors (mapping table)
└── iterations (tracking table)
```

### **Indexing Strategy**

1. **Digital Root Index** - Fast pruning by digital root (0-9)
2. **E8 Projection** - 8D lattice coordinates for clustering
3. **Content Hash** - Deduplication and quick lookup
4. **In-Memory Cache** - Hot vectors cached for fast access

---

## 🔍 Similarity Search Methods

### **1. Cosine Similarity**
```python
similarity = dot(vec1, vec2) / (norm(vec1) * norm(vec2))
```

### **2. Euclidean Distance**
```python
distance = sqrt(sum((a - b)^2 for a, b in zip(vec1, vec2)))
```

### **3. Lattice Distance** (CMPLX native)
```python
base_dist = euclidean(vec1, vec2)
dr_factor = abs(digital_root(hash1) - digital_root(hash2)) / 9
distance = base_dist * (1 + dr_factor)
```

---

## 📁 File Structure

```
CMPLXUNI-external/src/cmplx/mcp/
├── unified_mcp_server.py          # Main entry (26 tools)
├── swarm_mcp_tools.py             # Swarm control (9 tools)
├── vector_mmdb_tools.py           # Vector embeddings (5 tools) 🆕
├── concurrent_exploration_tools.py # Batch/recursive (4 tools) 🆕
├── cmplx_cqe_mcp_server.py        # CQE tools (8 tools)
└── mcp-server-entry.py            # Standard entry point

qwen-swarm/
├── docker-compose.yml             # 4 agents + coordinator + GUI
├── coordinator/main.py            # Task orchestrator
├── agents/agent.py                # Qwen agent implementation
├── gui/main.py                    # Web interface
└── scripts/
    ├── start.sh                   # Startup
    └── stop.sh                    # Shutdown
```

---

## 🎯 Use Cases

### **1. Codebase Analysis**
```
User: "Spawn a swarm to analyze the CMPLX codebase"
→ Spawns 4 agents with ThinkTank deliberation
→ Each agent explores different directories
→ Results stored as vectors in MMDB
→ Consensus gathered on key findings
```

### **2. Document Processing Pipeline**
```
User: "Process batch of 1000 documents"
→ Creates embeddings for all documents
→ Stores in MMDB with metadata
→ Indexes by digital root for fast search
→ Returns collection ID and stats
```

### **3. Deep Recursive Exploration**
```
User: "Explore recursively to depth 5"
→ Starts from root node
→ Expands 3 children per node
→ Visits 364 nodes (3^0 + 3^1 + ... + 3^5)
→ Stores all discovered data
→ Returns tree structure and stats
```

### **4. Similarity Search**
```
User: "Find similar vectors to: machine learning"
→ Creates query embedding
→ Searches MMDB with digital root pruning
→ Returns top 10 most similar
→ Includes similarity scores and metadata
```

---

## 🐛 Troubleshooting

### **Swarm not responding**
```bash
docker-compose ps  # Check container status
docker-compose logs -f qwen-coordinator  # View logs
```

### **Vector storage errors**
```bash
# Check database file
ls -la /home/borker/CMPLXUNI-external/src/mmdb/vector_store.db

# Test connection
cd /home/borker/CMPLXUNI-external
.venv/bin/python -c "from cmplx.mcp.vector_mmdb_tools import MMDBVectorStore; print(MMDBVectorStore().stats())"
```

### **Batch processing slow**
- Increase `max_concurrency` (default: 50)
- Increase `batch_size` (default: 100)
- Check system resources (CPU, memory)

---

## 📈 Next Steps

1. ✅ **MCP Configured** - Ready for Qwen Code
2. ✅ **Swarm Running** - 4 agents active
3. ✅ **Vector MMDB** - Storage operational
4. ✅ **Batch Processing** - 50 concurrent workers
5. ✅ **Recursive Exploration** - Depth 10 ready

### **Recommended Actions**

1. **Test with real data** - Process your documents
2. **Configure LLM backend** - Edit `qwen-swarm/.env`
3. **Scale agents** - Modify `docker-compose.yml`
4. **Custom expand functions** - Define your own recursion logic
5. **Monitor performance** - Use `exploration.get_stats`

---

**License:** MIT | **Version:** 1.0.0-expanded | **Tools:** 26
