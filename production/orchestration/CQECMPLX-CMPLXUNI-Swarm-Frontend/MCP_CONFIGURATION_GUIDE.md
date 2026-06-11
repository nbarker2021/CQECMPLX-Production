# CMPLX MCP Server Configuration Guide

## Overview

Your CMPLX system exposes **8 geometric AI tools** via Model Context Protocol (MCP) that can be used by any MCP-compatible AI client (Claude Desktop, Cursor, Cline, etc.).

## Available Tools

| Tool                        | Description                                          | Scope |
| --------------------------- | ---------------------------------------------------- | ----- |
| `cqe.sentinel.detect`       | Geometric anomaly detection via E8 lattice           | READ  |
| `cqe.diff.compare`          | Document comparison with dual-lattice fingerprinting | READ  |
| `cqe.scheduler.orchestrate` | Conway-frame task scheduling                         | WRITE |
| `cqe.provenance.record`     | Merkle-chained provenance tracking                   | WRITE |
| `cqe.harmonizer.consensus`  | Multi-signal consensus via E8 alignment              | READ  |
| `cqe.theory.query`          | Query 2,474 CQE formalizations                       | READ  |
| `cqe.tester.verify`         | Formal property verification                         | READ  |
| `cqe.workbench.execute`     | Unified orchestrator (pipeline/analysis/audit)       | WRITE |

## Configuration Methods

### Method 1: STDIO (Local Process) - RECOMMENDED

**For Claude Desktop** (`%APPDATA%\Claude\claude_desktop_config.json`):

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

**For Cursor/Cline** (`.cursor/mcp.json` or `.cline/mcp.json`):

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

### Method 2: HTTP/SSE (Network Access)

**If your Docker backend is running on port 8000:**

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

**For remote access (from another machine):**

```json
{
  "mcpServers": {
    "cmplx-remote": {
      "url": "http://YOUR_IP:8000/sse",
      "transport": "sse"
    }
  }
}
```

## Linux/macOS Configuration

**For Unix-based systems** (adjust paths):

```json
{
  "mcpServers": {
    "cmplx": {
      "command": "python3",
      "args": ["/home/user/CMPLXUNI/src/cmplx/mcp/mcp-server-entry.py"],
      "env": {
        "CMPLX_ROOT": "/home/user/CMPLXUNI"
      }
    }
  }
}
```

## Testing Your Configuration

### 1. Test the MCP Server Directly

```bash
# Windows
python "D:\Work Files\CMPLX-Monorepo\Local AI ToDo\CMPLXUNI\src\cmplx\mcp\cmplx_cqe_mcp_server.py"

# Linux/macOS
python3 /home/user/CMPLXUNI/src/cmplx/mcp/cmplx_cqe_mcp_server.py
```

Expected output: Self-test showing all 8 tools operational.

### 2. Verify MCP Client Connection

After configuring your AI client:

1. Restart the client application
2. Look for "cmplx" in the available tools/servers list
3. Try invoking a tool: "Use the cmplx sentinel to detect anomalies in this text: [your text]"

## Tool Usage Examples

### Anomaly Detection

```
Use cqe.sentinel.detect to check if this log entry is anomalous:
"ERROR: Unexpected null pointer at 0x7fff5fbff8a0"
```

### Document Comparison

```
Use cqe.diff.compare to find the similarity between:
Text A: "Deploy to production immediately"
Text B: "Deploy to production after testing"
```

### Task Scheduling

```
Use cqe.scheduler.orchestrate to schedule these tasks:
- init_database
- load_models
- start_api_server
```

### Consensus Building

```
Use cqe.harmonizer.consensus to find agreement between:
- "We should refactor the codebase"
- "We should refactor the code structure"
- "We should rewrite everything from scratch"
```

## Troubleshooting

### Issue: "Server not found"

- Verify Python 3.10+ is installed: `python --version`
- Check the path to `mcp-server-entry.py` is correct
- Ensure `CMPLX_ROOT` points to the project root

### Issue: "UTF-8 encoding error" (Windows)

- Add `"PYTHONUTF8": "1"` to env
- Add `"PYTHONIOENCODING": "utf-8"` to env

### Issue: "Import error: mcp_os not found"

- The server will fall back to built-in CQE tools
- Check if `mcp_os` directory exists in your project

### Issue: "Connection refused" (HTTP mode)

- Verify Docker container is running: `docker ps`
- Check port 8000 is accessible: `curl http://localhost:8000/health`
- Ensure firewall allows connections

## Architecture Notes

- **Server ID**: `cmplx-toolkit`
- **Version**: 1.0.0
- **Transport**: STDIO (default) or HTTP/SSE
- **Conservation Law**: All tools enforce ΔΦ ≤ 0
- **Receipt Tracking**: Every invocation generates a cryptographic receipt
- **Tier System**: Tools are restricted by agent tier (Full Model, Agent/PLEX, SubAgent, etc.)

## Advanced: Custom Tool Registration

To add your own tools to the MCP server, edit:

```
src/cmplx/mcp/cmplx_cqe_mcp_server.py
```

Follow the pattern of existing tools with:

1. `MCPToolContract` definition
2. Tool class implementation
3. Registration in `CQEMCPServer.__init__`
4. Handler in `_make_handler`

## Support

For issues or questions:

- Check logs in your AI client's console
- Run the self-test: `python cmplx_cqe_mcp_server.py`
- Verify environment variables are set correctly
