# CMPLX Next.js Application Architecture

## Overview

A full-stack Next.js application providing:
- **LLM-style chat interface** with swarm agent support
- **Tool manipulation suite** (tabs/windows for different tool categories)
- **Master Memory Layer** for all agents (persistent, stateful)
- **Onboarding Loops** (agent teaching system)
- **Live parsable database** (repo + ToDo folders as morphon shell)
- **ML loops** with local memory integration

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    NEXT.JS APPLICATION                           │
│  Port: 3000 (frontend + API)                                     │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  FRONTEND (React + TypeScript)                             │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Chat Interface                                      │ │ │
│  │  │  - Multi-agent swarm chat                            │ │ │
│  │  │  - Message threads per agent                         │ │ │
│  │  │  - Real-time status indicators                       │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Tool Suite (Tabs/Windows)                           │ │ │
│  │  │  - Library Tools Tab                                 │ │ │
│  │  │  - Vector MMDB Tab                                   │ │ │
│  │  │  - Swarm Control Tab                                 │ │ │
│  │  │  - CQE Tools Tab                                     │ │ │
│  │  │  - Exploration Tab                                   │ │ │
│  │  │  - Memory Layer Tab                                  │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  │  ┌─────────────────────────────────────────────────────┐ │ │
│  │  │  Master Memory Layer UI                              │ │ │
│  │  │  - Agent memory visualization                        │ │ │
│  │  │  - Onboarding progress                               │ │ │
│  │  │  - Recall history                                    │ │ │
│  │  └─────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  BACKEND API (Next.js API Routes)                          │ │
│  │  /api/chat              - Chat with swarm                  │ │
│  │  /api/tools/*           - Tool manipulation                │ │
│  │  /api/memory/*          - Master memory layer              │ │
│  │  /api/onboarding/*      - Onboarding loops                 │ │
│  │  /api/agents/*          - Agent management                  │ │
│  │  /api/morphon/*         - Morphon shell integration         │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    EXTERNAL SERVICES                             │
├─────────────────────────────────────────────────────────────────┤
│  MCP Server (Port 8900) - 34 tools                               │
│  The Library (Port 8902) - Document processing                   │
│  Qwen Swarm (Port 3000/5000) - 4 agents                          │
│  Redis (Port 6379) - Pub/Sub messaging                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## File Structure

```
cmplx-nextjs/
├── package.json
├── next.config.js
├── tsconfig.json
├── src/
│   ├── app/                      # Next.js 14 App Router
│   │   ├── layout.tsx            # Root layout
│   │   ├── page.tsx              # Main chat page
│   │   ├── tools/
│   │   │   ├── page.tsx          # Tools suite page
│   │   │   ├── library/          # Library tools
│   │   │   ├── vector/           # Vector MMDB
│   │   │   ├── swarm/            # Swarm control
│   │   │   ├── cqe/              # CQE tools
│   │   │   └── memory/           # Memory layer
│   │   ├── memory/
│   │   │   └── page.tsx          # Master memory view
│   │   ├── onboarding/
│   │   │   └── page.tsx          # Onboarding loops
│   │   └── api/                  # API routes
│   │       ├── chat/
│   │       ├── tools/
│   │       ├── memory/
│   │       ├── onboarding/
│   │       └── agents/
│   ├── components/               # React components
│   │   ├── chat/
│   │   │   ├── ChatInterface.tsx
│   │   │   ├── MessageList.tsx
│   │   │   ├── MessageInput.tsx
│   │   │   ├── AgentStatus.tsx
│   │   │   └── SwarmView.tsx
│   │   ├── tools/
│   │   │   ├── ToolSuite.tsx
│   │   │   ├── ToolTab.tsx
│   │   │   ├── LibraryTools.tsx
│   │   │   ├── VectorTools.tsx
│   │   │   └── ...
│   │   ├── memory/
│   │   │   ├── MemoryLayer.tsx
│   │   │   ├── MemoryVisualizer.tsx
│   │   │   └── RecallHistory.tsx
│   │   └── onboarding/
│   │       ├── OnboardingLoops.tsx
│   │       └── ProgressTracker.tsx
│   ├── lib/                      # Utilities
│   │   ├── mcp-client.ts         # MCP client
│   │   ├── memory-store.ts       # Memory layer
│   │   ├── onboarding-engine.ts  # Onboarding system
│   │   └── morphon-shell.ts      # Morphon shell
│   └── types/                    # TypeScript types
│       ├── chat.ts
│       ├── tools.ts
│       ├── memory.ts
│       └── agents.ts
├── public/
└── .env.local
```

---

## Master Memory Layer

### Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    MASTER MEMORY LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  Short-term     │  │  Long-term      │  │  Semantic       │ │
│  │  (Redis)        │  │  (PostgreSQL)   │  │  (Vector DB)    │ │
│  │  - Chat history │  │  - Agent memory │  │  - Concepts     │ │
│  │  - Agent state  │  │  - Tool usage   │  │  - Relationships│ │
│  │  - Session data │  │  - Learnings    │  │  - Embeddings   │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
│                              │                                   │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │  Memory API                                                │ │
│  │  - get(agent_id, key)                                     │ │
│  │  - set(agent_id, key, value)                              │ │
│  │  - recall(agent_id, query, limit)                         │ │
│  │  - embed(text) → vector                                   │ │
│  │  - search_similar(vector, threshold)                      │ │
│  └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### Memory Schema

```typescript
interface AgentMemory {
  agent_id: string;
  session_id: string;
  short_term: {
    chat_history: Message[];
    current_task: Task | null;
    context: Record<string, any>;
  };
  long_term: {
    learnings: Learning[];
    tool_usage: ToolUsage[];
    relationships: Relationship[];
  };
  semantic: {
    concepts: Concept[];
    embeddings: number[][];
  };
}

interface OnboardingLoop {
  loop_id: string;
  agent_id: string;
  phase: 'orientation' | 'tool_training' | 'system_learning' | 'integration';
  tests: OnboardingTest[];
  progress: number;
  completed_at?: string;
}
```

---

## Onboarding Loops System

### Phases

**Phase 1: Orientation**
- System overview
- Agent role assignment
- Basic tool introduction

**Phase 2: Tool Training**
- Library tools (8 tools)
- Vector MMDB tools (5 tools)
- Swarm tools (9 tools)
- CQE tools (8 tools)
- Exploration tools (4 tools)

**Phase 3: System Learning**
- Repo folder structure
- ToDo folder integration
- Morphon shell operations
- MDHG navigation

**Phase 4: Integration**
- Full pipeline execution
- Quality gate validation
- Multi-agent coordination

### Tests Per Phase

```typescript
const onboardingTests = {
  orientation: [
    "What is the CMPLX system?",
    "Name the 4 swarm agents",
    "What is the MCP server?"
  ],
  tool_training: [
    "Create a RAG card",
    "Define atomic forms",
    "Run quality validation"
  ],
  system_learning: [
    "Navigate to repo folder",
    "Process ToDo item",
    "Use morphon shell"
  ],
  integration: [
    "Full document pipeline",
    "Swarm coordination task",
    "Quality gate validation"
  ]
};
```

---

## Morphon Shell Integration

### Wrapped Shell

```typescript
class MorphonShell {
  // Wraps repo and ToDo folders as live parsable database
  repoPath: string;
  todoPath: string;
  
  // Operations
  async parse(): Promise<ParsedDocument[]>;
  async index(): Promise<void>;
  async search(query: string): Promise<SearchResult[]>;
  async updateMemory(agent_id: string): Promise<void>;
}
```

### Live Parsing

- Watch file changes (chokidar)
- Auto-index new documents
- Update vector embeddings
- Sync with memory layer

---

## API Endpoints

### Chat
- `POST /api/chat` - Send message to swarm
- `GET /api/chat/:session_id` - Get chat history
- `POST /api/chat/:session_id/agents` - Assign agents

### Tools
- `GET /api/tools` - List all tools
- `POST /api/tools/:tool_name/call` - Call tool
- `GET /api/tools/:tool_name/schema` - Get tool schema

### Memory
- `GET /api/memory/:agent_id` - Get agent memory
- `POST /api/memory/:agent_id` - Update memory
- `POST /api/memory/:agent_id/recall` - Recall with query
- `GET /api/memory/:agent_id/onboarding` - Get onboarding status

### Onboarding
- `POST /api/onboarding/start` - Start onboarding
- `POST /api/onboarding/:loop_id/test` - Run test
- `GET /api/onboarding/:loop_id/progress` - Get progress

### Agents
- `GET /api/agents` - List agents
- `GET /api/agents/:agent_id/status` - Get status
- `POST /api/agents/:agent_id/assign` - Assign task

---

## Technology Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | Next.js 14, React 18, TypeScript |
| **UI Components** | Radix UI, Tailwind CSS |
| **State Management** | Zustand, React Query |
| **Backend** | Next.js API Routes |
| **Database** | PostgreSQL (long-term memory) |
| **Cache** | Redis (short-term memory) |
| **Vector DB** | MMDB (integrated) |
| **Real-time** | Server-Sent Events (SSE) |
| **MCP Client** | Custom HTTP client |

---

**Status:** Ready for implementation
