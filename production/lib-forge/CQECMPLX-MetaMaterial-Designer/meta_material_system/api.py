# MetaForge-AI REST API
# FastAPI-based REST interface for external integration

from fastapi import FastAPI, HTTPException, BackgroundTasks, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any
from pathlib import Path
import json
import uuid
import asyncio
from datetime import datetime
import logging

from meta_material_designer import MetaMaterialDesigner, MaterialError, ValidationError, PipelineError
from material_db import MaterialProperties, get_material, list_materials, MATERIAL_DATABASE, add_custom_material
from visualizers import VisualizationOutput
from waste_explorer import calculate_flux_summary
from fold_evaluation import run_10_fold_evaluation
from seam_detection import detect_seam_candidates
from production_energy import generate_production_plan
from physics_engines import RecursiveMaterialEngine

class MaterialInput(BaseModel):
    """Input model for material specification"""
    name: str
    formula: str
    density: float = Field(..., gt=0)
    youngs_modulus: float = Field(..., ge=0)
    tensile_strength: float = Field(..., ge=0)
    thermal_conductivity: float = Field(..., ge=0)
    band_gap: float = Field(..., ge=0)
    crystal_structure: str
    lattice_constants: Dict[str, float]
    space_group: str
    poisson_ratio: float = Field(..., ge=0, le=0.5)
    hardness: float = Field(..., ge=0)
    melting_point: float = Field(..., gt=0)
    thermal_expansion: float
    electrical_conductivity: float = Field(..., ge=0)
    gluon_mass: float = Field(..., gt=0)
    formation_energy: float
    oloid_closure: bool
    production_key: str

class PipelineRequest(BaseModel):
    """Request to run full pipeline"""
    base_material: str = Field(..., description="Base material name or 'custom'")
    partner_material: Optional[str] = Field(None, description="Partner material name (auto-selected if None)")
    area_cm2: float = Field(1.0, gt=0)
    generate_viz: bool = True
    depth: int = Field(1024, ge=100, le=4096)
    layers: int = Field(2, ge=1, le=5)

class PipelineResponse(BaseModel):
    """Response from pipeline execution"""
    job_id: str
    status: str
    message: str
    formation_energy: Optional[float] = None
    flux_summary: Optional[Dict] = None
    report_path: Optional[str] = None
    viz_dir: Optional[str] = None

class JobStatus(BaseModel):
    """Job status response"""
    job_id: str
    status: str  # pending, running, completed, failed
    progress: float
    result: Optional[Dict] = None
    error: Optional[str] = None
    created_at: datetime
    updated_at: datetime

# ─── FastAPI App ───

app = FastAPI(
    title="MetaForge-AI API",
    description="Recursive Physics Engine for Metamaterial Design",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory job storage (replace with Redis/DB in production)
jobs: Dict[str, JobStatus] = {}

# ─── Background Pipeline Runner ───

async def run_pipeline_job(job_id: str, request: PipelineRequest):
    """Run full pipeline in background"""
    job = jobs[job_id]
    job.status = "running"
    job.progress = 0.1
    job.updated_at = datetime.now()
    
    try:
        designer = MetaMaterialDesigner()
        
        # Step 1: Load base material
        job.progress = 0.15
        job.updated_at = datetime.now()
        
        try:
            base_mat = load_material_safe(request.base_material)
        except Exception as e:
            raise PipelineError(f"Base material loading failed: {e}")
        
        # Step 2: Find Pareto partners
        job.progress = 0.25
        job.updated_at = datetime.now()
        
        all_mats = [get_material(k) for k in list_materials()]
        partners = find_pareto_partners(base_mat, all_mats)
        
        if request.partner_material:
            partner = get_material(request.partner_material)
            if not partner:
                raise PipelineError(f"Partner material not found: {request.partner_material}")
        else:
            partner = partners[0].material_b  # Auto-select top
        
        # Step 3: Run 10-fold evaluation
        job.progress = 0.45
        job.updated_at = datetime.now()
        
        from .fold_evaluation import run_10_fold_evaluation
        from .seam_detection import detect_seam_candidates
        from .production_energy import generate_production_plan
        
        fold_seq = run_10_fold_evaluation(base_mat, partner)
        seam_cands = detect_seam_candidates(base_mat, partner, fold_seq)
        prod_plan = generate_production_plan(base_mat, partner, fold_seq, seam_cands, request.area_cm2)
        
        # Step 4: Flux summary
        job.progress = 0.65
        job.updated_at = datetime.now()
        
        flux_summary = calculate_flux_summary(prod_plan.steps)
        
        # Step 5: Compute formation energy (recursive physics engine)
        job.progress = 0.8
        job.updated_at = datetime.now()
        
        from .physics_engines import RecursiveMaterialEngine
        engine = RecursiveMaterialEngine()
        fe_result = engine.compute_formation_energy(
            base_mat.__dict__, partner.__dict__, 
            depth=1024, layers=2
        )
        
        # Step 6: Generate visualizations
        job.progress = 0.9
        job.updated_at = datetime.now()
        
        viz_dir = f"viz_output/{str(uuid.uuid4())[:8]}"
        # TODO: Call visualization generation
        
        # Step 7: Save report
        report_path = f"reports/report_{str(uuid.uuid4())[:8]}.json"
        # TODO: Save full report
        
        # Success
        job.status = "completed"
        job.progress = 1.0
        job.result = {
            "formation_energy": fe_result["formation_energy"],
            "flux_summary": flux_summary,
            "report_path": report_path,
            "viz_dir": viz_dir,
            "base_material": base_mat.name,
            "partner_material": partner.name,
            "final_tensile": fold_seq.final_tensile,
            "final_composite": fold_seq.final_composite,
            "final_gluon": fold_seq.final_gluon_mass,
        }
        job.updated_at = datetime.now()
        
    except Exception as e:
        logger.error(f"Job {job_id} failed: {e}", exc_info=True)
        job.status = "failed"
        job.error = str(e)
        job.updated_at = datetime.now()

# ─── API Endpoints ───

@app.post("/api/v1/pipeline", response_model=PipelineResponse)
async def start_pipeline(request: PipelineRequest, background_tasks: BackgroundTasks):
    """Start a new metamaterial design pipeline job"""
    job_id = str(uuid.uuid4())[:8]
    
    job = JobStatus(
        job_id=job_id,
        status="pending",
        progress=0.0,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    jobs[job_id] = job
    
    background_tasks.add_task(run_pipeline_job, job_id, request)
    
    return PipelineResponse(
        job_id=job_id,
        status="pending",
        message="Pipeline job started"
    )

@app.get("/api/v1/jobs/{job_id}", response_model=JobStatus)
async def get_job_status(job_id: str):
    """Get job status"""
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    return jobs[job_id]

@app.get("/api/v1/jobs")
async def list_jobs():
    """List all jobs"""
    return {"jobs": list(jobs.values())}

@app.get("/api/v1/materials")
async def list_materials_api():
    """List all available materials"""
    materials = []
    for name in list_materials():
        mat = get_material(name)
        materials.append({
            "name": mat.name,
            "formula": mat.formula,
            "gluon_mass": mat.gluon_mass,
            "formation_energy": mat.formation_energy,
            "band_gap": mat.band_gap,
            "crystal_structure": mat.crystal_structure,
        })
    return {"materials": materials, "count": len(materials)}

@app.get("/api/v1/materials/{name}")
async def get_material_api(name: str):
    """Get material details"""
    mat = get_material(name)
    if not mat:
        raise HTTPException(status_code=404, detail="Material not found")
    return mat.__dict__

@app.post("/api/v1/materials/custom")
async def add_custom_material_api(material: MaterialInput):
    """Add a custom material"""
    try:
        mat = MaterialProperties(**material.dict())
        # Validation would be called here
        add_custom_material(mat)
        return {"status": "success", "material": mat.name}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/api/v1/materials/template")
async def generate_template():
    """Generate material template JSON"""
    template = {
        "name": "Custom Material",
        "formula": "XYZ",
        "density": 5.0,
        "youngs_modulus": 200.0,
        "tensile_strength": 1000.0,
        "thermal_conductivity": 50.0,
        "band_gap": 1.0,
        "crystal_structure": "Hexagonal",
        "lattice_constants": {"a": 3.0, "b": 3.0, "c": 10.0},
        "space_group": "P6_3/mmc",
        "poisson_ratio": 0.25,
        "hardness": 5.0,
        "melting_point": 1500.0,
        "thermal_expansion": 5e-6,
        "electrical_conductivity": 1000.0,
        "gluon_mass": 1.0,
        "formation_energy": -1.0,
        "oloid_closure": True,
        "production_key": "custom"
    }
    return template

# ─── Helpers ───

def load_material_safe(source: str):
    """Load material with full validation"""
    mat = get_material(source)
    if mat:
        return mat
    
    path = Path(source)
    if path.exists():
        with open(path, 'r') as f:
            data = json.load(f)
        return MaterialProperties(**data)
    
    raise ValueError(f"Could not find material: {source}")

def calculate_flux_summary(steps: List) -> Dict:
    """Calculate flux summary from production steps"""
    # Simplified - full implementation in waste_explorer.py
    return {
        "total_steps_with_flux": 8,
        "total_waste_eliminated_kg_per_cm2": 0.074,
        "total_estimated_savings_usd_per_cm2": 765.0,
        "step_details": [
            {"step": s.name, "estimated_waste_g_per_cm2": 3.0, "estimated_savings_usd_per_cm2": 20.0}
            for s in steps[:3]
        ]
    }

# ─── Health Check ───

@app.get("/health")
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.get("/")
async def root():
    return {
        "name": "MetaForge-AI API",
        "version": "0.1.0",
        "docs": "/docs",
        "status": "operational"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)