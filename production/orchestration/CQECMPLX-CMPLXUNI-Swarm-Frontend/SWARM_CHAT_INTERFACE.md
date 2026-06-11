# CMPLX Swarm - Chat-Controlled Multi-Agent System

## 🎯 Overview

This system integrates:

- **Qwen Swarm** (4 agents: Alpha, Beta, Gamma, Delta)
- **CMPLX MCP Tools** (8 CQE geometric tools)
- **ThinkTank** (Deliberation engine)
- **Direct Chat Interface** (You + Qwen Code control)

All accessible via **MCP protocol** and **natural language chat**.

---

## 🚀 Quick Start

### 1. Test the Unified Server

```bash
cd "D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI"
.venv\Scripts\python src\cmplx\mcp\unified_mcp_server.py
```

Expected output:

```
======================================================================
  CMPLX Unified MCP Server
  Swarm + ThinkTank + CQE Tools + Chat Interface
======================================================================

✅ Server Status: healthy
✅ Total Tools: 17
   - CQE Tools: 8
   - Swarm Tools: 9
```

### 2. Start the Qwen Swarm (Optional)

```bash
cd "D:\Work Files\CMPLX-Monorepo\Local AI ToDo\qwen-swarm"
.\scripts\start.sh
```

Access GUI at: http://localhost:3000

---

## 💬 Chat Commands

You can control the swarm via **natural language chat**. Just say:

### Swarm Control

| Command                                  | What it does                                |
| ---------------------------------------- | ------------------------------------------- |
| "Spawn a swarm to analyze this codebase" | Spawns 4 agents with ThinkTank deliberation |
| "Query swarm status"                     | Shows agent status and active sessions      |
| "Run deliberation on the architecture"   | ThinkTank + Swarm deliberate on question    |
| "Gather consensus on deployment"         | Collects consensus from all agents          |
| "Coordinate this task across agents"     | Distributes subtasks to agents              |
| "Tell the swarm: hello agents!"          | Sends chat message to swarm                 |

### ThinkTank

| Command                            | What it does                  |
| ---------------------------------- | ----------------------------- |
| "Analyze this code with ThinkTank" | Runs ThinkTank analysis       |
| "Review the architecture"          | ThinkTank architecture review |
| "Think about this design"          | ThinkTank deliberation        |

### CQE Tools

| Command                        | What it does                     |
| ------------------------------ | -------------------------------- |
| "Detect anomalies in this log" | Uses `cqe.sentinel.detect`       |
| "Compare these two documents"  | Uses `cqe.diff.compare`          |
| "Schedule these tasks"         | Uses `cqe.scheduler.orchestrate` |

---

## 🔧 MCP Tool Reference

### Swarm Tools (9)

| Tool                     | Description                           | Scope |
| ------------------------ | ------------------------------------- | ----- |
| `swarm.spawn`            | Spawn agent swarm for task            | WRITE |
| `swarm.deliberate`       | Run ThinkTank + Swarm deliberation    | READ  |
| `swarm.coordinate`       | Coordinate multi-agent task execution | WRITE |
| `swarm.query_status`     | Query swarm and agent status          | READ  |
| `swarm.gather_consensus` | Gather consensus from swarm           | READ  |
| `swarm.chat_send`        | Send direct chat message to swarm     | WRITE |
| `swarm.chat_receive`     | Receive messages from swarm           | READ  |
| `thinktank.analyze`      | Run ThinkTank analysis on topic       | READ  |
| `cmplx_agent.execute`    | Execute CMPLX agent task              | WRITE |

### CQE Tools (8)

| Tool                        | Description                 |
| --------------------------- | --------------------------- |
| `cqe.sentinel.detect`       | Geometric anomaly detection |
| `cqe.diff.compare`          | Document comparison         |
| `cqe.scheduler.orchestrate` | Task scheduling             |
| `cqe.provenance.record`     | Provenance tracking         |
| `cqe.harmonizer.consensus`  | Multi-signal consensus      |
| `cqe.theory.query`          | Query CQE formalizations    |
| `cqe.tester.verify`         | Property verification       |
| `cqe.workbench.execute`     | Unified orchestrator        |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              DIRECT CHAT INTERFACE                           │
│  You + Qwen Code → Natural language commands                 │
│  "Spawn a swarm to analyze this"                             │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              UNIFIED MCP SERVER (Port 8900)                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Chat Interface → Intent Detection → Tool Router     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                            │
            ┌───────────────┼───────────────┐
            ▼               ▼               ▼
┌──────────────────┐ ┌──────────────────┐ ┌──────────────────┐
│  Swarm Controller│ │  CQE Server      │ │  ThinkTank       │
│  - 4 Agents      │ │  - 8 Tools       │ │  - Deliberation  │
│  - Redis Bus     │ │  - Geometric AI  │ │  - Analysis      │
└──────────────────┘ └──────────────────┘ └──────────────────┘
```

---

## 📋 Configuration

### For Claude Desktop

Add to `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "cmplx-unified": {
      "command": "python",
      "args": [
        "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI\\src\\cmplx\\mcp\\unified_mcp_server.py"
      ],
      "env": {
        "CMPLX_ROOT": "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI",
        "PYTHONUTF8": "1"
      }
    }
  }
}
```

### For Cursor IDE

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "cmplx-unified": {
      "command": "python",
      "args": [
        "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI\\src\\cmplx\\mcp\\unified_mcp_server.py"
      ],
      "env": {
        "CMPLX_ROOT": "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI"
      }
    }
  }
}
```

---

## 🧪 Usage Examples

### Example 1: Spawn Swarm for Code Analysis

**User:** "Spawn a swarm to analyze the CMPLX codebase"

**System:**

```json
{
  "session_id": "swarm_a1b2c3d4",
  "agents_spawned": ["alpha", "beta", "gamma", "delta"],
  "thinktank_deliberation": {
    "status": "completed",
    "recommendations": ["...", "..."]
  },
  "status": "active"
}
```

### Example 2: Run Deliberation

**User:** "Should we deploy to production today?"

**System:**

```json
{
  "question": "Should we deploy to production today?",
  "thinktank_result": {...},
  "swarm_result": {
    "agent_responses": {
      "architect": "...",
      "analyst": "...",
      "critic": "...",
      "implementer": "..."
    }
  },
  "consensus": {
    "summary": "ThinkTank + Swarm consensus",
    "confidence": 0.85
  }
}
```

### Example 3: Query Status

**User:** "What's the swarm status?"

**System:**

```json
{
  "agents": {
    "alpha": {"name": "Qwen-Alpha", "status": "active"},
    "beta": {"name": "Qwen-Beta", "status": "active"},
    "gamma": {"name": "Qwen-Gamma", "status": "active"},
    "delta": {"name": "Qwen-Delta", "status": "active"}
  },
  "active_sessions": [...],
  "session_count": 1
}
```

---

## 🔍 Programmatic Usage

### Python API

```python
import asyncio
from cmplx.mcp.unified_mcp_server import UnifiedMCPServer, ChatInterface

async def main():
    # Create server
    server = UnifiedMCPServer()

    # Create chat interface
    chat = ChatInterface(server)

    # Send chat message
    result = await chat.process_message(
        "Spawn a swarm to analyze the codebase",
        sender="user"
    )
    print(result)

    # Direct tool call
    result = await server.call_tool(
        name="swarm.query_status",
        arguments={},
        caller="user"
    )
    print(result)

asyncio.run(main())
```

### MCP Client

```python
from mcp import Client

async with Client() as client:
    # List tools
    tools = await client.list_tools()
    print(tools)  # 17 tools available

    # Call tool
    result = await client.call_tool(
        name="swarm.deliberate",
        arguments={"question": "What's the best approach?"}
    )
```

---

## 📁 File Structure

```
CMPLXUNI-external/src/cmplx/mcp/
├── unified_mcp_server.py       # Main entry point
├── swarm_mcp_tools.py          # Swarm MCP tools
├── cmplx_cqe_mcp_server.py     # CQE tools (existing)
├── mcp-server-entry.py         # Standard entry point
└── ...

qwen-swarm/
├── docker-compose.yml          # Swarm Docker config
├── coordinator/main.py         # Coordinator service
├── agents/agent.py             # Agent implementation
├── gui/main.py                 # Web GUI
└── scripts/
    ├── start.sh                # Startup script
    └── stop.sh                 # Shutdown script
```

---

## 🐛 Troubleshooting

### Swarm not starting

```bash
# Check Docker
docker ps | grep qwen

# Check logs
docker-compose logs -f qwen-coordinator
```

### MCP tools not showing

```bash
# Test server directly
cd "D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI"
.venv\Scripts\python src\cmplx\mcp\unified_mcp_server.py
```

### Chat commands not working

- Ensure intent detection keywords are used
- Check conversation history with `swarm.chat_receive`

---

## 🎓 Best Practices

1. **Always use ThinkTank first** for complex decisions
2. **Query status** before spawning new swarms
3. **Gather consensus** for important decisions
4. **Use chat interface** for natural interaction
5. **Monitor agent status** during long-running tasks

---

## 📝 Next Steps

1. ✅ **Test unified server** - Run `unified_mcp_server.py`
2. 🔲 **Start Qwen Swarm** - Run `./scripts/start.sh` in qwen-swarm
3. 🔲 **Configure MCP client** - Add to Claude/Cursor config
4. 🔲 **Test chat commands** - Try "spawn a swarm"
5. 🔲 **Integrate with Qwen Code** - Use via chat interface

---

## 🚀 Advanced: Custom Agent Roles

You can define custom agent roles for specific tasks:

```python
await server.call_tool(
    name="swarm.deliberate",
    arguments={
        "question": "How should we architect the new feature?",
        "roles": ["architect", "security_expert", "performance_expert"]
    }
)
```

---

**License:** MIT | **Version:** 1.0.0-unified
