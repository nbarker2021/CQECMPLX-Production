# CMPLXUNI - Unified Enterprise AI System

> **CMPLXUNI: Enterprise AI & Unified Families**  
> *Layer L8: Families, E8/Leech Lattice, MMDB*

**Parent Navigation:** [CMPLX-1T NAVIGATION.md](../NAVIGATION.md) | **Ecosystem Hub:** [CMPLX-1T Root](../../README.md)  
**You Are Here:** `repos/cmplx-uni/README.md` → L8 Enterprise layer

---

**Version:** 1.0.0 | **Date:** 2026-02-28  
**Repository:** https://github.com/nbarker2021/CMPLXUNI

---

## 🎯 Quick Navigation

**For AI Agents:** [AGENTS.md](AGENTS.md) → Coding standards & integration  
**For Navigation:** [NAVIGATION.md](NAVIGATION.md) → Internal module traversal  
**For Architecture:** See docs in repository root

---

## 📋 Overview

CMPLXUNI is the enterprise-grade AI layer of the CMPLX ecosystem, built on geometric first principles using E8 lattice theory. It provides:

1. **Unified Families** - Family-based computation system
2. **Geometric Intelligence** - E8/Leech lattice operations
3. **Multi-Modal Database (MMDB)** - Unified data storage
4. **ThinkTank** - Multi-perspective deliberation
5. **Next.js Interface** - Web-based chat system

---

## 🗺️ Module Navigation

```
cmplx-uni/
├── README.md                 ← You are here
├── AGENTS.md                 ← AI agent guide
├── NAVIGATION.md             ← Internal navigation
│
├── src/cmplx/               ← Source code
│   ├── core/                → [Core abstractions](src/cmplx/core/)
│   ├── lattice/             → [E8/Leech lattice](src/cmplx/lattice/)
│   ├── unified_families/    → [Family system](src/cmplx/unified_families/)
│   ├── mcp/                 → [MCP OS integration](src/cmplx/mcp/)
│   ├── hub/                 → [Agent runtime](src/cmplx/hub/)
│   ├── thinktank/           → [Deliberation](src/cmplx/thinktank/)
│   └── cli/                 → [Command line](src/cmplx/cli/)
│
├── mmdb/                    ← Multi-modal database
├── cmplx-nextjs/            ← Next.js chat interface
└── The Library/             ← Document system
```

---

## 🚀 Quick Start

### Installation

```bash
# Install CMPLXUNI
pip install -e .

# Install with all dependencies
pip install -e .[all]
```

### Basic Usage

```python
from cmplx.lattice import E8Lattice
from cmplx.unified_families import FamilyManager
from cmplx.thinktank import ThinkTank

# Initialize E8 lattice
lattice = E8Lattice()
root = lattice.snap_to_e8([1.0] * 8)

# Create a family
manager = FamilyManager()
family = manager.create_family("research_family")

# Use ThinkTank for deliberation
tank = ThinkTank()
result = tank.deliberate("Complex question here")
```

### Running the Chat Interface

```bash
# Navigate to Next.js app
cd cmplx-nextjs

# Install dependencies
npm install

# Run development server
npm run dev
# Access at http://localhost:3000
```

---

## 🔗 Cross-Repository Navigation

### Up to Parent
- **[CMPLX-1T Root](../../README.md)** - Master showroom
- **[CMPLX-1T NAVIGATION.md](../NAVIGATION.md)** - Ecosystem navigation
- **[CMPLX-1T AGENTS.md](../AGENTS.md)** - Root agent guide

### Related Repositories
- **[CMPLX-Baseline](../cmplx-baseline/)** ← L1-L3 Infrastructure
- **[CMPLXDevKit](../cmplx-devkit/)** ← L5-L6 MDHG/Morphons
- **[CMPLXMCP](../cmplx-mcp/)** ← L7 Composables (sibling layer)
- **[CMPLX-Monorepo](../cmplx-monorepo/)** ← Full stack portal

---

## 🧩 Component Details

### Core (`src/cmplx/core/`)
Base abstractions and interfaces:
- Base classes for all components
- Common interfaces
- Utility functions

### Lattice (`src/cmplx/lattice/`)
Geometric computing on E8/Leech:
- **E8Lattice** - E8 root system operations
- **LeechLattice** - Leech lattice (24D)
- **NiemeierLattices** - Niemeier classifications
- **SNAP** - SNAP coordinate system

### Unified Families (`src/cmplx/unified_families/`)
Family-based computation:
- **FamilyManager** - Family lifecycle
- **FamilyRegistry** - Service discovery
- **SNAP Labels** - Type-agnostic tagging

### ThinkTank (`src/cmplx/thinktank/`)
Multi-perspective deliberation:
- **DeliberationEngine** - Core deliberation
- **PerspectiveSystem** - Multiple viewpoints
- **ConsensusBuilding** - Agreement algorithms

### MCP (`src/cmplx/mcp/`)
Model Context Protocol integration:
- **MCPClient** - Protocol client
- **MCPOS** - Operating system layer

### Hub (`src/cmplx/hub/`)
Agent runtime environment:
- **AgentRuntime** - Execution environment
- **TaskScheduler** - Job scheduling

### CLI (`src/cmplx/cli/`)
Command-line interface:
- Interactive shell
- Batch processing
- Admin tools

---

## 📊 Integration Points

| Component | Protocol | Port/Path |
|-----------|----------|-----------|
| Next.js UI | HTTP | 3000 |
| MMDB | TCP | Configurable |
| ThinkTank | Internal | Module call |
| MCP Client | HTTP/SSE | 8900 |

---

## 🛠️ Development

### Code Structure

```python
# Lattice example
from cmplx.lattice import E8Lattice

lattice = E8Lattice()
coords = lattice.generate_root_system()

# Family example
from cmplx.unified_families import FamilyManager

manager = FamilyManager()
family = manager.get_family("research")

# ThinkTank example
from cmplx.thinktank import ThinkTank

tank = ThinkTank()
result = tank.deliberate(query, perspectives=["analyst", "critic", "synthesist"])
```

### Testing

```bash
# Run tests
pytest tests/

# Run specific test
pytest tests/test_lattice.py
pytest tests/test_families.py
pytest tests/test_thinktank.py
```

---

## 📝 Documentation

| Document | Purpose | Location |
|----------|---------|----------|
| **Root README** | Overview (you are here) | [README.md](README.md) |
| **Agent Guide** | AI coding standards | [AGENTS.md](AGENTS.md) |
| **Navigation** | Internal module map | [NAVIGATION.md](NAVIGATION.md) |
| **Architecture** | CMPLX_NEXTJS_ARCHITECTURE.md | [CMPLX_NEXTJS_ARCHITECTURE.md](CMPLX_NEXTJS_ARCHITECTURE.md) |
| **MCP Config** | MCP_CONFIGURATION_GUIDE.md | [MCP_CONFIGURATION_GUIDE.md](MCP_CONFIGURATION_GUIDE.md) |
| **Swarm Docs** | EXPANDED_SWARM_DOCUMENTATION.md | [EXPANDED_SWARM_DOCUMENTATION.md](EXPANDED_SWARM_DOCUMENTATION.md) |

---

## 🔄 CMPLX-1T Layer Mapping

| Layer | Name | CMPLXUNI Component |
|-------|------|-------------------|
| L8 | Families | `unified_families/` |
| L8 | Geometric AI | `lattice/` |
| L8 | MMDB | `mmdb/` |
| L8 | ThinkTank | `thinktank/` |
| L8 | Interface | `cmplx-nextjs/` |

---

## 📞 Support

- **Documentation:** See docs above
- **Agent Help:** [AGENTS.md](AGENTS.md)
- **Navigation:** [NAVIGATION.md](NAVIGATION.md)
- **Parent Context:** [CMPLX-1T NAVIGATION.md](../NAVIGATION.md)

---

## CMPLX-1T Status

### Architecture Layer
- **CMPLX-1T Layer:** L8 (Families)
- **Repository:** https://github.com/nbarker2021/CMPLXUNI

### To Do
- [ ] Complete Families L8 system implementation
- [ ] Tag all families with SNAP labels
- [ ] Implement binary chains system

### In Progress
- [ ] Maintain unified families with SNAP labels
- [ ] Develop geometric foundations (E8, Leech lattice)

### Completed
- [x] Geometric AI framework on E8 lattice theory
- [x] Multi-modal database (mmdb) integration
- [x] Next.js chat interface (cmplx-nextjs)
- [x] The Library document system

---

**Version:** 1.0.0 | **Layer:** L8 Families | **Parent:** [CMPLX-1T](../)

*"Where geometric intelligence meets enterprise AI."*
