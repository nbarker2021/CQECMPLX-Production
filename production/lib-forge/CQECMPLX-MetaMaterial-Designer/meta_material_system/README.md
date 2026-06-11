# MetaForge-AI: Recursive Physics Engine for Metamaterial Design

> **The map IS the computation. Every traversal re-fires the entire formalism.**

A recursive physics engine stack that generates publication-quality metamaterial designs with in-situ flux/transition waste-to-resource pathways. Built on a recursive physics engine where every call re-fires the complete formalism stack.

## 🎯 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run CLI (with flux analysis)
python meta_material_designer.py --material graphene --auto-partner --area 1 --output report.json --viz-dir viz_out

# Run web app
streamlit run streamlit_app.py

# Or run with Docker (recommended)
docker-compose up -d
```

## 🏗️ Architecture: The Recursive Physics Engine

```
┌─────────────────────────────────────────────────────────────────┐
│                    META-FORGE-AI PIPELINE                       │
├─────────────────────────────────────────────────────────────────┤
│  NEW MATERIAL PAIR INSERTS                                      │
│        │                                                         │
│        ▼                                                         │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ RUN ALL 6 ENGINES FRESH (no caching, no shortcuts)        │  │
│  ├───────────────────────────────────────────────────────────┤  │
│  │ Rule 30 Lattice     │ Causal (L,C,R) readout               │  │
│  │ Mandelbrot Boundary │ 4 locked-CR schedules (stability)   │  │
│  │ E8 Root Lattice     │ Glue vectors, mass reduction        │  │
│  │ VOA / Moonshine     │ j-coefficients (modular)            │  │
│  │ Oloid / Cayley-Dick │ Winding, closure (geometry)         │  │
│  │ SK-Hopf Algebra     │ Reads ALL readouts, generates SK    │  │
│  └───────────────────────────────────────────────────────────┘  │
│        │                                                         │
│        ▼                                                         │
│  Formation Energy = Σ weighted action paths                     │
│        │                                                         │
│        ▼                                                         │
│  10-Fold SK-Bifurcation Evaluation                              │
│        │                                                         │
│        ▼                                                         │
│  Seam Detection → Production Plan → Flux/Transition             │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Option 1: Local (Python 3.11+)

```bash
git clone <repo>
cd meta_material_system
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Option 2: Docker (Recommended)

```bash
# Build and run web app
docker-compose up -d

# Run CLI
docker-compose run --rm metaforge-cli --material graphene --auto-partner --area 1
```

## 🚀 Usage

### CLI (Full Pipeline)

```bash
# Basic usage with auto-selected partner
python meta_material_designer.py --material graphene --auto-partner --area 1 --output report.json --viz-dir viz_out

# Custom material
python meta_material_designer.py --material-file my_material.json --auto-partner --area 10

# Skip visualizations for speed
python meta_material_designer.py --material graphene --auto-partner --no-viz

# Complex material combo
python meta_material_designer.py --material tbg --partner 1 --area 1 --output tbg_report.json
```

### Web App

```bash
streamlit run streamlit_app.py
# Opens at http://localhost:8501
```

### Docker

```bash
# Production
docker-compose up -d

# CLI inside container
docker-compose run --rm metaforge-cli --material graphene --auto-partner

# Development with Jupyter
docker-compose --profile dev up -d jupyter
```

## 📊 Output

Every run produces:

| Output | Description |
|--------|-------------|
| `report.json` | Complete pipeline state (materials, folds, seams, production, flux) |
| `viz_out/` | 10 publication-quality HTML visualizations |
| `flux_summary` | In-situ waste-to-flux pathways with $/cm² savings |

### Example Output

```json
{
  "base_material": {"name": "Graphene", "gluon_mass": 0.98, ...},
  "partner_material": {"name": "Hexagonal Boron Nitride", ...},
  "fold_sequence": {"final_tensile": 77154, "final_composite": 43873, ...},
  "seam_materials": [{"material": "MXene", "role": "HEALING", ...}],
  "production_plan": {"cost_usd_per_cm2": 105.00, "energy_MJ_per_cm2": 0.08, ...},
  "flux_summary": {
    "total_steps_with_flux": 8,
    "total_waste_eliminated_kg_per_cm2": 0.074,
    "total_estimated_savings_usd_per_cm2": 765.0
  },
  "formation_energy": 40.35
}
```

## 🔬 Physics Engines (The Map)

| Engine | Purpose | Key Feature |
|--------|---------|-------------|
| **Rule 30 Lattice** | Causal (L,C,R) light-cone | Full light-cone reconstruction per step |
| **SK-Hopf Algebra** | Combinator action on data readouts | SK operates on Rule 30, Mandelbrot, VOA, E8 readouts |
| **Oloid / Cayley-Dickson** | Geometric phase | Full octonion multiplication, winding, closure |
| **Mandelbrot Boundary** | Stability verification | 4 locked-CR external rays, 1024-depth exact |
| **E8 Root Lattice** | Symmetry reduction | 240 roots, glue vectors, mass reduction |
| **VOA / Moonshine** | Modular invariance | j-function coefficients, Monster group |

**Key Principle**: The map IS the computation. Every call re-fires the entire formalism stack — no caching, no shortcuts. The SK-combinator operates on ACTUAL data readouts from other engines.

## ♻️ Flux/Transition System (Waste → In-Situ Reuse)

| Waste Stream | Becomes Flux/Transition Layer For | Savings |
|--------------|-----------------------------------|---------|
| PMMA residue | Carbon interlayer / graphitization seed | $5-10/cm² |
| Acetone solvent | Vapor annealing agent | Eliminates fresh acetone |
| Spent FeCl₃ etchant | FeCl₃ flux for TMD CVD | >90% precursor recovery |
| Metal hydroxide sludge | Sub-nm oxide nucleation seeds | $500/kg waste → asset |
| CVD exhaust (H₂S, H₂Se, Mo/W) | 95% precursor recycle loop | >90% chemical cost reduction |
| MBE cell residue | Perovskite surface flux | Eliminates separate flux purchase |
| Amorphous carbon soot | Tunable work-function interlayer | Free contact engineering |
| Inert gas purge | Direct gas recycle loop | 98% cost reduction |
| Failed devices | Metrology reference standards | $500/device value |

## 🧪 Testing

```bash
# Run all tests
pytest -v

# With coverage
pytest --cov=meta_material_system --cov-report=html

# Run specific test
pytest tests/test_physics_engines.py -v
```

## 📁 Project Structure

```
meta_material_system/
├── meta_material_designer.py    # CLI + Pipeline orchestrator
├── streamlit_app.py             # Web app (7 tabs)
├── material_db.py               # 23 real materials database
├── physics_engines.py           # 7 recursive physics engines
├── waste_explorer.py            # 15 flux pathways
├── visualizers.py               # 10 publication-quality plots
├── pareto_partnering.py         # Multi-objective optimization
├── fold_evaluation.py           # 10-fold SK-bifurcation
├── seam_detection.py            # 5 seam roles
├── production_energy.py         # Real synthesis steps
├── visualizers.py               # 2D/3D plotly visualizations
├── physics_engines.py           # Recursive physics engine stack
├── config.yaml                  # All runtime configuration
├── requirements.txt             # Pinned dependencies
├── pyproject.toml               # Build system config
├── Dockerfile                   # Multi-stage Docker build
├── docker-compose.yml           # Orchestration
├── config.yaml                  # Runtime configuration
├── tests/                       # Test suite
│   ├── test_physics_engines.py
│   ├── test_material_db.py
│   ├── test_pipeline.py
│   └── test_integration.py
└── meta_material_system/        # Package
    ├── __init__.py
    └── ...
```

## ⚙️ Configuration

All runtime configuration in `config.yaml`:

```yaml
app:
  debug: false
  log_level: "INFO"

pipeline:
  default_depth: 1024
  max_folds: 10
  validate_materials: true

engines:
  rule30:
    max_width: 4096
  mandelbrot:
    depth: 1024
    verify_exact: true
```

## 🐳 Docker Deployment

```bash
# Production
docker-compose up -d

# View logs
docker-compose logs -f metaforge-api

# Scale
docker-compose up -d --scale metaforge-api=3
```

## 🧪 Testing Strategy

- **Unit tests**: Each physics engine tested in isolation
- **Integration tests**: Full pipeline runs
- **Validation tests**: Against known heterostructures (Gr/hBN, MoS₂/WS₂, TBG/hBN)
- **Edge cases**: Invalid materials, missing files, invalid parameters

## 📚 Citation

If you use this work, please cite:

```bibtex
@software{metaforge_ai,
  title = {MetaForge-AI: Recursive Physics Engine for Metamaterial Design},
  author = {MetaForge-AI Team},
  year = {2024},
  url = {https://github.com/metaforge-ai/metaforge-ai}
}
```

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Run tests (`pytest -v`)
4. Commit changes (`git commit -m 'Add amazing feature'`)
5. Push to branch (`git push origin feature/amazing-feature`)
6. Open Pull Request

---

**Built with formal methods. Every call re-fires the map.**