# CMPLX MCP Configuration - Complete Details

## 🎯 Quick Summary

Your CMPLX system has **8 geometric AI tools** ready to use via MCP. Any AI that supports MCP (Claude Desktop, Cursor, Cline, etc.) can connect and use them.

---

## 📍 Your System Paths

**Windows (Your Setup):**

- Project Root: `D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI`
- MCP Entry: `D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI\src\cmplx\mcp\mcp-server-entry.py`
- Docker Backend: `http://localhost:8000`

**Linux (Current Environment):**

- Project Root: `/home/user/CMPLXUNI`
- MCP Entry: `/home/user/CMPLXUNI/src/cmplx/mcp/mcp-server-entry.py`

---

## 🔧 Configuration for Claude Desktop

**File Location:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "cmplx": {
      "command": "python",
      "args": [
        "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI\\src\\cmplx\\mcp\\mcp-server-entry.py"
      ],
      "env": {
        "CMPLX_ROOT": "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI",
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

---

## 🔧 Configuration for Cursor IDE

**File Location:** `.cursor/mcp.json` in your project or user config

```json
{
  "mcpServers": {
    "cmplx": {
      "command": "python",
      "args": [
        "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI\\src\\cmplx\\mcp\\mcp-server-entry.py"
      ],
      "env": {
        "CMPLX_ROOT": "D:\\Work Files\\CMPLX-Monorepo\\Local AI ToDo\\CMPLXUNI",
        "PYTHONUTF8": "1"
      }
    }
  }
}
```

---

## 🔧 Configuration for HTTP/SSE (Network Mode)

**Use this if your Docker backend is running:**

```json
{
  "mcpServers": {
    "cmplx-http": {
      "url": "http://localhost:8000/sse",
      "transport": "sse"
    }
  }
}
```

---

## 🛠️ The 8 Available Tools

### 1. **cqe.sentinel.detect** (Anomaly Detection)

- **Purpose:** Detect anomalies using E8 lattice geometry
- **Scope:** READ
- **Example:** "Is this log entry anomalous?"

### 2. **cqe.diff.compare** (Document Comparison)

- **Purpose:** Compare documents using dual-lattice fingerprinting
- **Scope:** READ
- **Example:** "How similar are these two code snippets?"

### 3. **cqe.scheduler.orchestrate** (Task Scheduling)

- **Purpose:** Schedule tasks using Conway-frame geometry
- **Scope:** WRITE
- **Example:** "Schedule these 5 tasks with dependencies"

### 4. **cqe.provenance.record** (Audit Trail)

- **Purpose:** Create Merkle-chained provenance records
- **Scope:** WRITE
- **Example:** "Record this action in the audit chain"

### 5. **cqe.harmonizer.consensus** (Multi-Agent Consensus)

- **Purpose:** Find consensus between multiple signals
- **Scope:** READ
- **Example:** "What's the consensus between these 3 opinions?"

### 6. **cqe.theory.query** (Knowledge Base)

- **Purpose:** Query 2,474 CQE formalizations
- **Scope:** READ
- **Example:** "Find formalizations about lattice theory"

### 7. **cqe.tester.verify** (Property Testing)

- **Purpose:** Verify formal properties and invariants
- **Scope:** READ
- **Example:** "Run all property tests"

### 8. **cqe.workbench.execute** (Unified Orchestrator)

- **Purpose:** Run pipeline/analysis/audit workflows
- **Scope:** WRITE
- **Example:** "Run audit mode on the system"

---

## 🧪 Testing Your Setup

### Step 1: Verify Python

```bash
python --version
# Should show Python 3.10 or higher
```

### Step 2: Test MCP Server Directly

```bash
cd "D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI"
python src\cmplx\mcp\cmplx_cqe_mcp_server.py
```

Expected output: Self-test showing all 8 tools operational.

### Step 3: Configure Your AI Client

1. Copy the appropriate JSON config above
2. Paste into your AI client's MCP config file
3. Restart the AI client
4. Look for "cmplx" in available tools/servers

### Step 4: Test a Tool

Ask your AI:

```
Use the cmplx cqe.sentinel.detect tool to check if this text is anomalous:
"ERROR: Unexpected null pointer exception at memory address 0x00000000"
```

---

## 🔍 How It Works

1. **Your AI Client** (Claude, Cursor, etc.) reads the MCP config
2. **Spawns the MCP Server** as a subprocess using Python
3. **Communicates via STDIO** (standard input/output)
4. **Tools are invoked** when you ask the AI to use them
5. **Results are returned** with cryptographic receipts

---

## 🎯 Key Features

- ✅ **Conservation Law:** All operations enforce ΔΦ ≤ 0
- ✅ **Receipt Tracking:** Every invocation generates a Merkle receipt
- ✅ **Tier System:** Tools respect agent tier permissions
- ✅ **Geometric AI:** Uses E8 lattice for embeddings and comparisons
- ✅ **Provenance Chain:** Immutable audit trail
- ✅ **Formal Verification:** Property-based testing built-in

---

## 🚨 Troubleshooting

### "Server not found"

- ✓ Check Python is installed: `python --version`
- ✓ Verify the path to `mcp-server-entry.py` is correct
- ✓ Ensure `CMPLX_ROOT` points to project root

### "UTF-8 encoding error" (Windows)

- ✓ Add `"PYTHONUTF8": "1"` to env
- ✓ Add `"PYTHONIOENCODING": "utf-8"` to env

### "Import error"

- ✓ The server has fallback implementations
- ✓ Check if dependencies are installed: `pip install -e .`

### "Connection refused" (HTTP mode)

- ✓ Verify Docker is running: `docker ps`
- ✓ Check port 8000: `curl http://localhost:8000/health`

---

## 📚 Architecture

```
┌─────────────────┐
│   AI Client     │  (Claude Desktop, Cursor, etc.)
│  (MCP Client)   │
└────────┬────────┘
         │ STDIO/HTTP
         ▼
┌─────────────────┐
│  MCP Server     │  (mcp-server-entry.py)
│  cmplx-toolkit  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  8 CQE Tools    │  (cmplx_cqe_mcp_server.py)
│  E8 Lattice     │
│  Provenance     │
│  ThinkTank      │
└─────────────────┘
```

---

## 🎓 Example Conversations

**Anomaly Detection:**

```
You: "Use cmplx to detect if this is anomalous: 'System crashed with code 0xDEADBEEF'"
AI: [Uses cqe.sentinel.detect] "Yes, z-score of 3.2 indicates anomaly"
```

**Document Comparison:**

```
You: "Compare these two API responses using cmplx"
AI: [Uses cqe.diff.compare] "Similarity: 0.87, verdict: similar"
```

**Consensus Building:**

```
You: "Find consensus between these 3 team opinions using cmplx"
AI: [Uses cqe.harmonizer.consensus] "Consensus: majority, agreement: 0.73"
```

---

## 📝 Notes

- **Server ID:** `cmplx-toolkit`
- **Version:** 1.0.0
- **Protocol:** MCP (Model Context Protocol)
- **Transport:** STDIO (default) or HTTP/SSE
- **License:** MIT

---

## ✅ Checklist

- [ ] Python 3.10+ installed
- [ ] CMPLX project cloned/downloaded
- [ ] MCP config file created for your AI client
- [ ] AI client restarted
- [ ] "cmplx" appears in available tools
- [ ] Test tool invocation successful

---

**You're ready to use CMPLX geometric AI tools with any MCP-compatible AI!** 🚀
