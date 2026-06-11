# CMPLX Next.js Application - Complete Documentation

## 🎯 Overview

A full-stack Next.js application providing:
- **LLM-style chat interface** with 4-agent swarm support
- **Tool manipulation suite** with tabs for different tool categories
- **Master Memory Layer** - Persistent, stateful memory for all agents
- **Onboarding Loops** - Agent teaching system with phased tests
- **Morphon Shell Integration** - Live parsable database from repo + ToDo folders

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd /home/borker/CMPLXUNI-external/cmplx-nextjs
npm install
```

### 2. Set Environment Variables

Create `.env.local`:
```bash
MCP_SERVER_URL=http://localhost:8900
LIBRARY_URL=http://localhost:8902
SWARM_COORDINATOR_URL=http://localhost:5000
SWARM_GUI_URL=http://localhost:3000
REDIS_HOST=localhost
REDIS_PORT=6379
REPO_PATH=/home/borker/CMPLXUNI-external
TODO_PATH=/home/borker/.qwen/todos
MEMORY_PATH=/home/borker/CMPLXUNI-external/cmplx-nextjs/memory
```

### 3. Start Development Server

```bash
npm run dev
```

Open **http://localhost:3000**

---

## 🏗️ Architecture

### Frontend Components

```
src/components/
├── chat/
│   ├── ChatInterface.tsx      # Main chat UI with swarm
│   ├── MessageList.tsx        # Message rendering
│   ├── MessageInput.tsx       # Input with suggestions
│   ├── AgentStatus.tsx        # Agent status indicators
│   └── SwarmView.tsx          # Multi-agent view
├── tools/
│   ├── ToolSuite.tsx          # Tabbed tool interface
│   ├── LibraryTools.tsx       # Library tool controls
│   ├── VectorTools.tsx        # Vector MMDB controls
│   ├── SwarmTools.tsx         # Swarm control panel
│   ├── CqeTools.tsx           # CQE tool controls
│   └── ExplorationTools.tsx   # Exploration tools
├── memory/
│   ├── MemoryLayer.tsx        # Master memory visualization
│   ├── MemoryVisualizer.tsx   # Graph view of memory
│   └── RecallHistory.tsx      # Recall history
└── onboarding/
    ├── OnboardingLoops.tsx    # Onboarding interface
    └── ProgressTracker.tsx    # Progress tracking
```

### Backend API Routes

```
src/app/api/
├── chat/
│   └── route.ts               # Chat with swarm
├── tools/
│   ├── route.ts               # List tools
│   └── [toolName]/
│       └── call/
│           └── route.ts       # Call specific tool
├── memory/
│   ├── [agentId]/
│   │   └── route.ts           # Agent memory CRUD
│   └── recall/
│       └── route.ts           # Memory recall
├── onboarding/
│   ├── start/
│   │   └── route.ts           # Start onboarding
│   └── [loopId]/
│       └── test/
│           └── route.ts       # Run onboarding test
└── agents/
    └── route.ts               # Agent management
```

---

## 💬 Chat Interface Features

### Multi-Agent Support

The chat interface supports all 4 swarm agents:

| Agent | Role | Color | Status |
|-------|------|-------|--------|
| **Alpha** | Document Reader | Green | Idle/Busy |
| **Beta** | RAG Card Creator | Blue | Idle/Busy |
| **Gamma** | Atomic Form Definer | Purple | Idle/Busy |
| **Delta** | Morphonic Generator | Cyan | Idle/Busy |

### Chat Commands

```
# Document Processing
"Process /docs/test.md through The Library"
"Create RAG cards for document doc_123"
"Define atomic forms for doc_123"
"Validate quality - no shitty work"

# Swarm Control
"Spawn a swarm to analyze the codebase"
"Query swarm status"
"Run deliberation on the architecture"

# Memory & Recall
"Recall what we discussed about E8 lattice"
"What did Alpha say about the documents?"
"Show me learnings about atomic forms"

# Onboarding
"Onboarding Loops Enabled"
"Start agent onboarding"
"Show onboarding progress"
```

---

## 🧠 Master Memory Layer

### Three-Tier Architecture

```
┌─────────────────────────────────────────┐
│  Short-term (In-Memory)                 │
│  - Chat history (last 100 messages)     │
│  - Current task                         │
│  - Session context                      │
│  - Expires after session                │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Long-term (JSON Files)                 │
│  - Agent learnings                      │
│  - Tool usage history                   │
│  - Agent relationships                  │
│  - Persistent across sessions           │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  Semantic (Vector Embeddings)           │
│  - Concepts and definitions             │
│  - Semantic relationships               │
│  - Embedding vectors                    │
│  - Similarity search                    │
└─────────────────────────────────────────┘
```

### Memory API

```typescript
// Get agent memory
GET /api/memory/:agentId

// Update memory
POST /api/memory/:agentId
Body: { session_id, memory: {...} }

// Recall from memory
POST /api/memory/recall
Body: { agent_id, query, limit }

// Add learning
POST /api/memory/:agentId/learning
Body: { content, source }

// Add concept
POST /api/memory/:agentId/concept
Body: { name, definition, related_concepts }
```

---

## 📚 Onboarding Loops System

### Phases

**Phase 1: Orientation (2 tests)**
- System overview
- Agent identification
- Basic concepts

**Phase 2: Tool Training (5 tests)**
- Library tools (8 tools)
- Vector MMDB (5 tools)
- Swarm control (9 tools)
- CQE tools (8 tools)
- Exploration (4 tools)

**Phase 3: System Learning (3 tests)**
- Repo folder navigation
- ToDo folder integration
- Morphon shell operations

**Phase 4: Integration (2 tests)**
- Full pipeline execution
- Multi-agent coordination

### Starting Onboarding

```
User: "Onboarding Loops Enabled"

System: 
🎓 Onboarding Started for Agent Alpha
Phase 1: Orientation (0/2 complete)

Test 1: What is the CMPLX system?
[Type your answer or ask for hint]
```

### Onboarding API

```typescript
// Start onboarding
POST /api/onboarding/start
Body: { agent_id }

// Run test
POST /api/onboarding/:loopId/test
Body: { test_id, answer }

// Get progress
GET /api/onboarding/:loopId/progress
```

---

## 🛠️ Tool Suite Interface

### Tabs

1. **Library Tools** (8 tools)
   - Ingest Document
   - Create RAG Cards
   - Define Atomic Forms
   - Generate Morphonic Forms
   - Stratify MDHG
   - Validate Quality
   - Search
   - Get Report

2. **Vector MMDB** (5 tools)
   - Create Embedding
   - Store Vector
   - Search Similar
   - Process Batch
   - Create Collection

3. **Swarm Control** (9 tools)
   - Spawn Swarm
   - Deliberate
   - Coordinate
   - Query Status
   - Gather Consensus
   - Chat Send/Receive
   - ThinkTank Analyze
   - Agent Execute

4. **CQE Tools** (8 tools)
   - Sentinel Detect
   - Diff Compare
   - Scheduler Orchestrate
   - Provenance Record
   - Harmonizer Consensus
   - Theory Query
   - Tester Verify
   - Workbench Execute

5. **Exploration** (4 tools)
   - Process Batch
   - Explore Recursive
   - Search
   - Get Stats

6. **Memory Layer**
   - View Agent Memory
   - Recall
   - Add Learning
   - Add Concept
   - Onboarding Progress

---

## 🔗 Integration with Existing Systems

### MCP Server (34 Tools)

The Next.js app connects to your unified MCP server:
- All 34 tools available via API
- Automatic intent detection
- Tool call tracking in chat

### The Library

Document processing integration:
- Direct API calls to Library (port 8902)
- RAG card creation from chat
- Quality validation reports

### Qwen Swarm

4-agent swarm integration:
- Agent status in real-time
- Task assignment via chat
- Inter-agent messaging

### Redis

Pub/Sub for real-time updates:
- Agent state changes
- Tool execution status
- Chat message delivery

---

## 📊 Memory Schema

```typescript
interface AgentMemory {
  agent_id: string;
  session_id: string;
  
  // Short-term (session)
  short_term: {
    chat_history: Message[];      // Last 100 messages
    current_task: Task | null;
    context: Record<string, any>;
  };
  
  // Long-term (persistent)
  long_term: {
    learnings: Learning[];         // Acquired knowledge
    tool_usage: ToolUsage[];       // Tool call history
    relationships: Relationship[]; // Entity relationships
  };
  
  // Semantic (vector)
  semantic: {
    concepts: Concept[];           // Known concepts
    embeddings: number[][];        // Vector embeddings
  };
}
```

---

## 🎯 Key Features

### 1. Persistent Stateful Memory

- Memory persists across sessions (JSON files)
- Agents remember previous conversations
- Learnings accumulate over time
- Concepts build semantic network

### 2. Onboarding Loops Enabled

When user says **"Onboarding Loops Enabled"**:
- System creates onboarding loop for agent
- Runs through 4 phases of tests
- Tracks progress and completion
- Certifies agent when complete

### 3. Live Parsable Database

- Repo folder watched for changes
- ToDo folder integrated
- Auto-indexing of new documents
- Vector embeddings updated

### 4. ML Loops Integration

- Tool usage patterns learned
- Success rates tracked
- Recommendations based on history
- Continuous improvement

---

## 🐛 Troubleshooting

### Chat not connecting
```bash
# Check MCP server
curl http://localhost:8900/health

# Check Next.js API
curl http://localhost:3000/api/chat
```

### Memory not persisting
```bash
# Check memory directory exists
ls -la /home/borker/CMPLXUNI-external/cmplx-nextjs/memory/agents/

# Check permissions
chmod 755 memory/agents/
```

### Onboarding not starting
```bash
# Check agent_id is provided
# Verify memory store initialized
```

---

**License:** MIT | **Version:** 1.0.0 | **Port:** 3000
