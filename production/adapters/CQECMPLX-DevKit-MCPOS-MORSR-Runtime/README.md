# CMPLX MCP OS

A Model Context Protocol (MCP) based operating system for the CMPLX framework.

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      LOCAL RUNTIME                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │  Client  │  │ Adapters │  │ Proxies  │  │ Pipeline │    │
│  │ (thin)   │  │(light)   │  │(handles) │  │(metadata)│    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│       │             │             │             │           │
│       └─────────────┴─────────────┴─────────────┘           │
│                         │                                   │
│                    [MCP Protocol]                           │
│                         │                                   │
└─────────────────────────┼───────────────────────────────────┘
                          │
┌─────────────────────────┼───────────────────────────────────┐
│                         ▼                                   │
│                    MCP SERVER                               │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                   TOOL REGISTRY                      │   │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐     │   │
│  │  │  L1  │ │  L2  │ │  L3  │ │  L4  │ │  L5  │     │   │
│  │  │Morph │ │Geom  │ │Oper  │ │Gov   │ │Inter │     │   │
│  │  └──────┘ └──────┘ └──────┘ └──────┘ └──────┘     │   │
│  └─────────────────────────────────────────────────────┘   │
│                          │                                  │
│  ┌───────────────────────┼──────────────────────────────┐  │
│  │               HEAVY DATA (Server-side)               │  │
│  │  • E8 Lattice (240 roots)                           │  │
│  │  • Leech Lattice (196,560 vectors)                  │  │
│  │  • 24 Niemeier Lattices                             │  │
│  │  • Weyl Chambers (696,729,600)                      │  │
│  │  • Large embeddings                                 │  │
│  └─────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### 1. Install

```bash
cd mcp_os
pip install -r requirements.txt
```

### 2. Run Server

```bash
python -m mcp_os server
```

### 3. Run Client (in another terminal)

```bash
python -m mcp_os client
```

## Usage

### Basic Client Usage

```python
import asyncio
from mcp_os import create_client, ProxyRegistry

async def main():
    async with create_client() as client:
        # Create proxy registry
        registry = ProxyRegistry(client)

        # Layer 1: Morphonic Foundation
        morphon = await registry.l1.generate_morphon("7")

        # Layer 2: Geometric Engine
        e8_result = await registry.l2.project_e8([1,2,3,4,5,6,7,8])

        # Layer 3: Operational Systems
        optimized = await registry.l3.morsr_optimize([1.0, 0.5, -0.3, 0.7], iterations=100)

        # Layer 4: Governance
        dr = await registry.l4.digital_root(432)

        # Layer 5: Interface
        embedding = await registry.l5.embed("Your text here", domain="text")

asyncio.run(main())
```

### Pipeline Usage

```python
from mcp_os.modules import Pipeline, DatabaseManager

async with create_client() as client:
    db = DatabaseManager()
    pipeline = Pipeline(client=client, db_manager=db)

    # Process data through pipeline
    result = await pipeline.process("Your content here")

    # Result contains handles, not heavy data
    print(result.handles)  # {'embedding': 'emb_abc123...'}
    print(result.metadata)  # Validation, timestamps, etc.
```

## Design Principles

1. **Heavy Data Stays Server-Side**: E8 roots, Leech lattice, etc. never leave the server
2. **Handles Are Lightweight**: Only handles and metadata travel between client/server
3. **Lazy Loading**: Data only fetched when explicitly requested
4. **Cache Locally**: Client caches handles; server caches full data
5. **Pipeline Flow**: Work → Intake → Geometric → Validation → Storage

## Layer Organization

| Layer | Name | Heavy Data | Local Proxy |
| ------- | ------ | ------------ | ------------- |
| L1 | Morphonic | None | Full capability |
| L2 | Geometric | E8, Leech, Niemeier, Weyl | Handle-only |
| L3 | Operational | MORSR state | Small states local |
| L4 | Governance | Policy DB | Cache policies |
| L5 | Interface | Embeddings | Handle-only |

## API Reference

### Client Methods

All methods are async and return lightweight handles/metadata.

- `generate_morphon(seed: str)` → `{handle, summary, dr}`

- `project_e8(vector: list[float])` → `{handle, lattice, norm}`

- `nearest_leech(vector: list[float])` → `{handle, lattice, distance}`

- `morsr_optimize(initial_state, iterations)` → `{handle, iterations, final_norm}`

- `digital_root(number)` → `{digital_root, meaning}`

- `embed(content, domain)` → `{handle, domain, content_hash}`

## License

MIT
