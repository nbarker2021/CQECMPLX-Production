"""
Waste Material Exploration System — Flux/Transition Materials
=============================================================
Core Principle: Waste streams become FLUX or TRANSITION LAYERS in the metamaterial stack
instead of requiring separate recovery plants. Direct in-situ reuse.
"""

from __future__ import annotations
from typing import Dict, List, Any
import json


# ─── Flux/Transition Pathways: Waste → In-Situ Reuse ───

FLUX_PATHWAYS = [
    # ─── PMMA Residue → Carbon Interlayer Flux ───
    {
        "waste_source": "PMMA Transfer",
        "waste_name": "PMMA Polymer Residue",
        "flux_role": "Carbon Interlayer / Graphitization Seed",
        "application": "Insert between 2D layers as amorphous carbon flux that graphitizes during annealing",
        "mechanism": "PMMA pyrolyzes → amorphous carbon → catalyzes layer alignment / reduces interfacial resistance",
        "benefit": "Eliminates separate transfer polymer removal step; carbon residue becomes functional interlayer",
        "processing": "None - residue remains in situ, annealed with stack",
        "compatible_stacks": ["graphene/hbn", "graphene/mos2", "tmd/metal", "any vdW stack"],
        "cost_savings": "Eliminates PMMA etch step ($5-10/cm²), acetone recovery",
        "environmental": "Zero polymer waste discharge",
    },
    {
        "waste_source": "PMMA Transfer",
        "waste_name": "Acetone Solvent (contaminated)",
        "flux_role": "Solvent Vapor Annealing Agent",
        "application": "Controlled acetone vapor during assembly improves layer adhesion / removes bubbles",
        "mechanism": "Acetone vapor plasticizes residual polymer, enables self-healing of wrinkles",
        "benefit": "Turns waste solvent into process gas; closed-loop vapor system",
        "processing": "Condenser trap on assembly chamber exhaust",
        "compatible_stacks": ["All polymer-assisted transfers"],
        "cost_savings": "Eliminates fresh acetone purchase for vapor annealing",
        "environmental": "Closed solvent loop, zero VOC emission",
    },

    # ─── Etchant Waste → Transition Metal Flux ───
    {
        "waste_source": "Selective Etching",
        "waste_name": "Spent Etchant (FeCl3/HCl)",
        "flux_role": "Iron Chloride Flux for TMD Growth",
        "application": "FeCl3 vapor as flux agent in CVD of MoS2/WS2 - enhances nucleation, controls domain size",
        "mechanism": "FeCl3 lowers nucleation barrier, promotes lateral growth; incorporates as controlled dopant",
        "benefit": "Etchant waste becomes high-value CVD flux ($50/kg as reagent vs $0.30 as waste)",
        "processing": "Concentrate by evaporation, purify via sublimation, dose into CVD carrier gas",
        "compatible_stacks": ["mos2", "ws2", "mose2", "wse2", "tmd alloys"],
        "cost_savings": "Replaces purchased FeCl3 flux; eliminates etchant disposal cost",
        "environmental": "Zero liquid discharge; Fe cycles in-process",
    },
    {
        "waste_source": "Selective Etching",
        "waste_name": "Etched Metal Hydroxide Sludge (Cu, Fe, Ti)",
        "flux_role": "Metal Oxide Nucleation Seeds",
        "application": "Ultra-thin (sub-nm) metal oxide interfacial layer for band alignment / Schottky contact tuning",
        "mechanism": "Sludge calcined → nanoparticles → spin-coated as monolayer before 2D transfer",
        "benefit": "Converts toxic metal waste into precision band-engineering layer",
        "processing": "Calcine 500°C → disperse in IPA → spin coat 0.5 nm → anneal",
        "compatible_stacks": ["metal/TMD contacts", "graphene/metal", "vdW heterojunctions"],
        "cost_savings": "Eliminates sludge disposal ($500/kg); creates high-value contact layer",
        "environmental": "Heavy metals immobilized in functional device layer",
    },

    # ─── CVD Exhaust → Chalcogen Flux Loop ───
    {
        "waste_source": "Co-CVD / CVD Growth",
        "waste_name": "Exhaust Gas (H2S, H2Se, unreacted Mo/W carbonyls)",
        "flux_role": "In-Situ Chalcogen / Metal Carbonyl Recycle Loop",
        "application": "Direct recycle of exhaust into CVD precursor bubbler via cold trap",
        "mechanism": "Cold finger at -80°C condenses H2S/H2Se/Mo(CO)6 → repressurized into carrier gas",
        "benefit": "95% precursor recovery; near-zero chemical consumption",
        "processing": "Cryogenic trap on reactor exhaust → periodic warm-up → repressurization",
        "compatible_stacks": ["All CVD-grown TMDs", "Co-CVD alloys"],
        "cost_savings": "Precursor cost reduction >90% (Mo(CO)6 $200/g, H2Se $500/g)",
        "environmental": "Zero toxic gas emission; closed chemical loop",
    },

    # ─── MBE Residue → Perovskite Flux / Substrate Treatment ───
    {
        "waste_source": "Molecular Beam Epitaxy",
        "waste_name": "Effusion Cell Residue (Sr, Ti, Ba, Pb oxides)",
        "flux_role": "Perovskite Surface Flux / Termination Control",
        "application": "SrO/TiO2/BaO flux during oxide MBE controls surface stoichiometry, prevents cation intermixing",
        "mechanism": "Controlled flux of excess A-site cation creates atomically flat, single-terminated surface",
        "benefit": "Waste oxide becomes essential flux for high-quality oxide growth",
        "processing": "Residue scraped, ground, loaded into dedicated flux cell",
        "compatible_stacks": ["sto", "btio3", "pbtio3", "knbo3", "oxide/2D interfaces"],
        "cost_savings": "Eliminates separate flux purchase; residue is flux-grade purity",
        "environmental": "Pb/Sr/Ti retained in-process, zero aqueous discharge",
    },

    # ─── Amorphous Carbon Soot → Interfacial Engineering ───
    {
        "waste_source": "CVD Growth",
        "waste_name": "Amorphous Carbon / Soot Deposits",
        "flux_role": "Tunable Work Function Interlayer",
        "application": "Sub-nm amorphous carbon between metal contact and 2D semiconductor tunes Schottky barrier",
        "mechanism": "Carbon dipole layer shifts vacuum level; thickness controls barrier height continuously",
        "benefit": "Replaces complex Fermi-level pinning mitigation schemes; waste becomes contact engineer tool",
        "processing": "Soot collected → dispersed → spin coat controlled thickness → anneal",
        "compatible_stacks": ["metal/TMD contacts", "graphene/metal", "vertical transistors"],
        "cost_savings": "Eliminates separate interfacial layer deposition; soot is free",
        "environmental": "Carbon retained in device, not emitted",
    },

    # ─── Inert Gas → Direct Reuse Loop ───
    {
        "waste_source": "Post-Assembly Annealing",
        "waste_name": "Inert Gas Purge (Ar, N2, forming gas)",
        "flux_role": "Process Gas Recycle Loop",
        "application": "Direct recompression and purification of Ar/N2/H2 for reuse in same furnace",
        "mechanism": "Membrane separation (H2) + getter (O2/H2O) → 99.999% purity restoration",
        "benefit": "Zero gas purchase for annealing; only electricity for compression",
        "processing": "Integrated gas handling skid on furnace exhaust",
        "compatible_stacks": ["All annealing steps"],
        "cost_savings": "Ar $5/L → recovered at $0.10/L electricity; 98% cost reduction",
        "environmental": "Zero gas cylinder logistics/emissions",
    },

    # ─── Failed Devices → Metrology Standards / Reference Layers ───
    {
        "waste_source": "Quality Control",
        "waste_name": "Failed/Scrapped Devices",
        "flux_role": "Reference Standards / Process Metrology Layers",
        "application": "Delaminated layers become reference samples for Raman/PL/TEM calibration",
        "mechanism": "Known defect / twist angle / thickness stacks used to calibrate inline metrology",
        "benefit": "Converts scrap into QA assets; each failed device = $500 metrology value",
        "processing": "Automated delamination → characterization → catalog → deploy as standard",
        "compatible_stacks": ["All production lines"],
        "cost_savings": "Eliminates purchase of reference standards; turns scrap into asset",
        "environmental": "Maximizes material utilization before final recycling",
    },

    # ─── Generic Synthesis Byproduct → Flux for Next Batch ───
    {
        "waste_source": "Generic Synthesis",
        "waste_name": "Reaction Byproducts (mixed oxides, chlorides)",
        "flux_role": "Mineralizing Flux for Hydrothermal / Solvothermal Growth",
        "application": "Mixed oxide/chloride waste lowers eutectic temperature for next crystal growth batch",
        "mechanism": "Flux modifies solubility, enables lower-temperature growth, incorporates as controlled impurity",
        "benefit": "Waste becomes process enabler for next batch; zero precursor waste",
        "processing": "Blend waste with fresh precursors at 5-10 wt% flux ratio",
        "compatible_stacks": ["oxide single crystals", "perovskite epitaxy", "hydrothermal TMDs"],
        "cost_savings": "Reduces fresh flux purchase; waste disposal eliminated",
        "environmental": "Closed precursor loop; zero solid waste",
    },

    # ─── New: ALD/CVD Trimethyl Metal → Carbon-Free Metal Flux ───
    {
        "waste_source": "CVD Growth / ALD",
        "waste_name": "Trimethyl Metal Residue (TMA, TEG, TMIn, etc.)",
        "flux_role": "Carbon-Free Metal Source via Pyrolysis",
        "application": "Pyrolyze TMA → Al metal + CH4; use Al as flux for III-V/oxide growth",
        "mechanism": "Controlled pyrolysis cracks organometallic → pure metal flux + captured hydrocarbon",
        "benefit": "Eliminates carbon incorporation from organometallics; captures CH4 for fuel",
        "processing": "Heated pyrolysis chamber (600°C) on exhaust line",
        "compatible_stacks": ["III-V semiconductors", "oxide MBE", "ALD"],
        "cost_savings": "Reduces high-purity metal source cost; CH4 credit",
        "environmental": "Carbon captured as CH4 not CO2; metal recycled",
    },

    # ─── New: Photoresist / E-beam Resist → Carbon Nanotube Seed ───
    {
        "waste_source": "Lithography / Patterning",
        "waste_name": "Exposed/Developed Photoresist (PMMA, HSQ, ZEP)",
        "flux_role": "CNT / Graphene Nucleation Seed Layer",
        "application": "Patterned resist pyrolyzed → ordered carbon dots → seed aligned CNT growth",
        "mechanism": "Resist carbon structure templates sp2 nucleation; patterning transfers to CNT array",
        "benefit": "Lithography waste becomes template for 1D material integration",
        "processing": "Pyrolysis at 800°C inert on patterned substrate",
        "compatible_stacks": ["CNT interconnects", "CNT transistors", "vertical integration"],
        "cost_savings": "Eliminates e-beam resist disposal ($200/kg); creates high-value CNT template",
        "environmental": "Resist carbon → functional nanostructure, not waste",
    },
]


def get_flux_pathways_for_step(step_name: str) -> List[Dict]:
    """Get flux pathways applicable to a production step."""
    matches = []
    for pathway in FLUX_PATHWAYS:
        if pathway["waste_source"].lower() in step_name.lower() or step_name.lower() in pathway["waste_source"].lower():
            matches.append(pathway)
    return matches


def calculate_flux_summary(plan_steps: List[Any]) -> Dict:
    """Calculate flux/transition material summary for a production plan."""
    total_waste_eliminated = 0.0
    total_cost_savings = 0.0
    step_fluxes = []

    for step in plan_steps:
        pathways = get_flux_pathways_for_step(step.name)
        if not pathways:
            continue

        step_mass = 0.0
        step_savings = 0.0
        for p in pathways:
            if "PMMA" in p["waste_source"] or "Transfer" in p["waste_source"]:
                step_mass += 3.0e-3
                step_savings += 10.0
            elif "Etch" in p["waste_source"]:
                step_mass += 0.02
                step_savings += 50.0
            elif "CVD" in p["waste_source"] or "Growth" in p["waste_source"]:
                step_mass += 0.01
                step_savings += 100.0
            elif "MBE" in p["waste_source"]:
                step_mass += 5e-4
                step_savings += 200.0
            elif "Anneal" in p["waste_source"]:
                step_mass += 1e-3
                step_savings += 5.0
            elif "Quality" in p["waste_source"]:
                step_mass += 5e-3
                step_savings += 500.0
            elif "Litho" in p["waste_source"]:
                step_mass += 1e-4
                step_savings += 50.0

        step_fluxes.append({
            "step": step.name,
            "applicable_pathways": len(pathways),
            "pathways": [
                {
                    "waste": p["waste_name"],
                    "flux_role": p["flux_role"],
                    "application": p["application"],
                    "mechanism": p["mechanism"],
                    "benefit": p["benefit"],
                    "compatible_stacks": p["compatible_stacks"],
                    "cost_savings_est": p["cost_savings"],
                    "environmental": p["environmental"],
                }
                for p in pathways
            ],
            "estimated_waste_mass_kg_per_cm2": step_mass,
            "estimated_cost_savings_usd_per_cm2": step_savings,
        })

        total_waste_eliminated += step_mass
        total_cost_savings += step_savings

    return {
        "total_steps_with_flux": len(step_fluxes),
        "total_waste_eliminated_kg_per_cm2": total_waste_eliminated,
        "total_estimated_savings_usd_per_cm2": total_cost_savings,
        "step_details": step_fluxes,
        "summary": {
            "waste_to_flux_conversion_rate": "100% (all identified waste streams have flux pathway)",
            "net_cost_per_cm2": total_cost_savings,
            "key_principle": "Waste is not discarded — it becomes the next process's flux, seed, or transition layer",
        }
    }


def render_flux_streamlit(flux_summary: Dict):
    """Render flux/transition analysis in Streamlit."""
    import streamlit as st
    import pandas as pd

    st.subheader("⚗️ Flux & Transition Material System (Waste → In-Situ Reuse)")

    st.caption("**Core Principle**: Every waste stream is a flux/transition layer for the next process step. No external recovery plant needed — reuse happens in-situ.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Steps with Flux Pathways", flux_summary["total_steps_with_flux"])
    col2.metric("Waste Eliminated", f"{flux_summary['total_waste_eliminated_kg_per_cm2']*1000:.1f} g/cm²")
    col3.metric("Est. Cost Savings", f"${flux_summary['total_estimated_savings_usd_per_cm2']:.0f}/cm²")

    for sf in flux_summary["step_details"]:
        with st.expander(f"🔬 {sf['step']} — {sf['applicable_pathways']} flux pathways | Waste: {sf['estimated_waste_mass_kg_per_cm2']*1000:.1f} g/cm² | Savings: ${sf['estimated_cost_savings_usd_per_cm2']:.0f}/cm²"):
            for p in sf["pathways"]:
                st.markdown(f"**{p['flux_role']}** (`{p['waste']}`)")
                st.markdown(f"> **Application**: {p['application']}")
                st.markdown(f"> **Mechanism**: {p['mechanism']}")
                st.markdown(f"> **✅ Benefit**: {p['benefit']}")
                st.markdown(f"> **♻️ Environmental**: {p['environmental']}")
                st.markdown(f"> **💰 Cost Impact**: {p['cost_savings_est']}")
                st.markdown(f"> **🧪 Compatible**: {', '.join(p['compatible_stacks'])}")
                st.markdown("---")


if __name__ == "__main__":
    from meta_material_designer import MetaMaterialDesigner

    designer = MetaMaterialDesigner()
    designer.base_material = designer.load_material("graphene")
    designer.partner = designer.load_material("hbn")
    designer.find_partners()
    designer.select_partner(0)
    designer.run_fold_evaluation()
    designer.find_seams()
    designer.generate_production(1.0)

    flux = calculate_flux_summary(designer.production_plan.steps)
    print(json.dumps(flux, indent=2, default=str))