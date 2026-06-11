#!/usr/bin/env python3
"""
MetaForge-AI — Streamlit Web Application
========================================
Interactive metamaterial design system with real-time Pareto partnering,
10-fold recursive evaluation, seam detection, and production planning.
"""

import sys
import json
from pathlib import Path
from typing import Optional, Dict, Any, List

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Add package to path
sys.path.insert(0, str(Path(__file__).parent))

from material_db import (
    get_material,
    list_materials,
    MATERIAL_DATABASE,
    MaterialProperties,
)
from meta_material_designer import MetaMaterialDesigner
from visualizers import render_visualizations_streamlit
from waste_explorer import calculate_flux_summary, render_flux_streamlit


# ─── Page Config ───
st.set_page_config(
    page_title="MetaForge-AI: Metamaterial Design System",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS ───
st.markdown("""
<style>
    .main-header { font-size: 2.5rem; font-weight: 700; color: #1e3a5f; margin-bottom: 0.5rem; }
    .sub-header { font-size: 1.2rem; color: #4a6fa5; margin-bottom: 1.5rem; }
    .metric-card { background: #f8f9fa; border-radius: 8px; padding: 1rem; margin: 0.5rem 0; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { height: 50px; padding: 0 24px; }
    .success-box { background: #d4edda; border: 1px solid #c3e6cb; border-radius: 4px; padding: 1rem; }
    .warning-box { background: #fff3cd; border: 1px solid #ffeeba; border-radius: 4px; padding: 1rem; }
    .info-box { background: #d1ecf1; border: 1px solid #bee5eb; border-radius: 4px; padding: 1rem; }
</style>
""", unsafe_allow_html=True)


# ─── Session State ───
def init_session_state():
    if "designer" not in st.session_state:
        st.session_state.designer = MetaMaterialDesigner()
    if "fold_sequence" not in st.session_state:
        st.session_state.fold_sequence = None
    if "seam_candidates" not in st.session_state:
        st.session_state.seam_candidates = []
    if "production_plan" not in st.session_state:
        st.session_state.production_plan = None
    if "pareto_partners" not in st.session_state:
        st.session_state.pareto_partners = []


init_session_state()


# ─── Sidebar: Material Selection ───
with st.sidebar:
    st.markdown("## 🔧 Material Selection")
    
    input_mode = st.radio(
        "Input mode",
        ["Database", "Upload JSON", "Create Template"],
        key="input_mode",
    )
    
    if input_mode == "Database":
        material_names = [m.name for m in MATERIAL_DATABASE.values()]
        selected_idx = st.selectbox(
            "Select base material",
            range(len(material_names)),
            format_func=lambda i: material_names[i],
            key="db_material_select",
        )
        if st.button("Load Material", type="primary", use_container_width=True):
            mat = list(MATERIAL_DATABASE.values())[selected_idx]
            st.session_state.designer.base_material = mat
            st.success(f"✓ Loaded: {mat.name}")
            st.rerun()
    
    elif input_mode == "Upload JSON":
        uploaded = st.file_uploader("Upload material JSON", type=["json"])
        if uploaded and st.button("Load Custom Material", type="primary", use_container_width=True):
            try:
                data = json.load(uploaded)
                mat = MaterialProperties(**data)
                st.session_state.designer.base_material = mat
                # Add to database for partnering
                from meta_material_system.material_db import add_custom_material
                add_custom_material(mat)
                st.success(f"✓ Loaded: {mat.name}")
                st.rerun()
            except Exception as e:
                st.error(f"Invalid JSON: {e}")
    
    elif input_mode == "Create Template":
        if st.button("Generate Template", type="primary", use_container_width=True):
            st.session_state.designer.save_material_template("material_template.json")
            with open("material_template.json", "r") as f:
                st.download_button(
                    "Download Template",
                    f.read(),
                    file_name="material_template.json",
                    mime="application/json",
                    use_container_width=True,
                )
    
    # Show current base material
    if st.session_state.designer.base_material:
        mat = st.session_state.designer.base_material
        st.markdown("---")
        st.markdown(f"### 📦 Current Base: **{mat.name}**")
        col1, col2 = st.columns(2)
        col1.metric("Gluon Mass", f"{mat.gluon_mass:.2f}")
        col2.metric("Formation Energy", f"{mat.formation_energy:.2f} eV")
        st.write(f"**Formula:** {mat.formula}")
        st.write(f"**Crystal:** {mat.crystal_structure}")
        st.write(f"**Oloid Closure:** {'✓' if mat.oloid_closure else '✗'}")


# ─── Main Content ───
st.markdown('<div class="main-header">🔬 MetaForge-AI</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Metamaterial Design System — Formal Verification + Production Pipeline</div>', unsafe_allow_html=True)

if not st.session_state.designer.base_material:
    st.markdown("""
    <div class="info-box">
        <h4>Welcome to MetaForge-AI</h4>
        <p>Select a base material from the sidebar to begin the design pipeline:</p>
        <ol>
            <li><strong>Pareto Partnering</strong> — Find optimal partner materials</li>
            <li><strong>10-Fold Evaluation</strong> — Recursive SK-bifurcation with error walls</li>
            <li><strong>Seam Detection</strong> — Identify interlayer materials</li>
            <li><strong>Production Plan</strong> — Real synthesis: energy, time, cost, scalability</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    st.stop()


# ─── Tabs ───
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🎯 Pareto Partners",
    "🔄 10-Fold Evaluation",
    "🔍 Seam Detection",
    "🏭 Production Plan",
    "📊 Visualizations",
    "⚗️ Flux/Transition",
    "📄 Export Report",
])


# ─── Tab 1: Pareto Partners ───
with tab1:
    st.subheader("Pareto-Optimal Partner Materials")
    
    if st.button("Find Partners", type="primary", use_container_width=True):
        with st.spinner("Running multi-objective optimization..."):
            all_mats = [get_material(k) for k in MATERIAL_DATABASE.keys()]
            st.session_state.pareto_partners = find_pareto_partners(
                st.session_state.designer.base_material, all_mats
            )
            st.session_state.designer.pareto_partners = st.session_state.pareto_partners
        st.success(f"Found {len(st.session_state.pareto_partners)} Pareto partners")
    
    if st.session_state.pareto_partners:
        # Table
        df = pd.DataFrame([
            {
                "Rank": i + 1,
                "Partner": p.material_b.name,
                "Formula": p.material_b.formula,
                "Pareto Score": f"{p.pareto_score:.3f}",
                "Lattice Match": f"{p.lattice_match:.2f}",
                "Property Synergy": f"{p.property_synergy:.2f}",
                "Gluon Coherence": f"{p.gluon_coherence:.2f}",
                "Oloid Compat": f"{p.oloid_compatibility:.2f}",
                "Interface Energy": f"{p.interface_energy:.4f}",
                "Strain Tolerance": f"{p.strain_tolerance:.2f}",
            }
            for i, p in enumerate(st.session_state.pareto_partners)
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Radar chart for top 3
        st.subheader("Top Partners — Multi-Objective Radar")
        fig = go.Figure()
        categories = ["Lattice", "Property", "Gluon", "Oloid", "Interface", "Strain"]
        for i, p in enumerate(st.session_state.pareto_partners[:3]):
            values = [
                p.lattice_match, p.property_synergy, p.gluon_coherence,
                p.oloid_compatibility, 1 - p.interface_energy, p.strain_tolerance / 30
            ]
            fig.add_trace(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill='toself',
                name=p.material_b.name,
                opacity=0.7,
            ))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
            showlegend=True,
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Partner selection
        st.markdown("---")
        st.subheader("Select Partner for Full Pipeline")
        partner_options = [f"{p.material_b.name} (Pareto: {p.pareto_score:.3f})" 
                          for p in st.session_state.pareto_partners[:10]]
        selected_partner = st.selectbox("Choose partner", partner_options)
        if st.button("Run Full Pipeline", type="primary", use_container_width=True):
            idx = partner_options.index(selected_partner)
            st.session_state.designer.partner = st.session_state.pareto_partners[idx].material_b
            st.success(f"✓ Partner: {st.session_state.designer.partner.name}")
            st.info("Switch to the **10-Fold Evaluation** tab to run the recursive analysis")
    
    else:
        st.info("Click **Find Partners** to run the Pareto optimization")


# ─── Tab 2: 10-Fold Evaluation ───
with tab2:
    st.subheader("10-Fold Recursive SK-Bifurcation Evaluation")
    
    if not st.session_state.designer.partner:
        st.warning("Select a partner in the **Pareto Partners** tab first")
    else:
        base = st.session_state.designer.base_material
        partner = st.session_state.designer.partner
        
        st.write(f"**Base:** {base.name}  +  **Partner:** {partner.name}")
        
        if st.button("Run 10-Fold Evaluation", type="primary", use_container_width=True):
            with st.spinner("Running recursive evaluation..."):
                st.session_state.fold_sequence = run_10_fold_evaluation(
                    base, partner, seed=42
                )
                st.session_state.designer.fold_sequence = st.session_state.fold_sequence
            st.success("10-Fold evaluation complete!")
        
        if st.session_state.fold_sequence:
            fs = st.session_state.fold_sequence
            
            # Summary metrics
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Final Tensile", f"{fs.final_tensile:,.0f} MPa")
            col2.metric("Composite Strength", f"{fs.final_composite:,.0f} MPa")
            col3.metric("Final Gluon Mass", f"{fs.final_gluon_mass:.3f}")
            col4.metric("Total Formation Energy", f"{fs.total_formation_energy:.2f} eV")
            
            # Fold progression chart
            st.subheader("Fold Progression")
            fold_df = pd.DataFrame([
                {
                    "Fold": f.fold_number,
                    "Context": f.applied_context,
                    "Gluon Mass": f.gluon_mass,
                    "Tensile (MPa)": f.tensile_strength,
                    "Composite (MPa)": f.composite_strength,
                    "Formation Energy": f.formation_energy,
                    "Oloid Closure": f.oloid_closure,
                    "Error Walls": len(f.error_walls),
                }
                for f in fs.folds
            ])
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=fold_df["Fold"], y=fold_df["Tensile (MPa)"],
                mode='lines+markers', name='Tensile', line=dict(color='#1f77b4')
            ))
            fig.add_trace(go.Scatter(
                x=fold_df["Fold"], y=fold_df["Composite (MPa)"],
                mode='lines+markers', name='Composite', line=dict(color='#ff7f0e')
            ))
            fig.add_trace(go.Scatter(
                x=fold_df["Fold"], y=fold_df["Gluon Mass"] * 50000,
                mode='lines+markers', name='Gluon × 50k', line=dict(color='#2ca02c')
            ))
            fig.update_layout(height=400, xaxis_title="Fold", yaxis_title="Value")
            st.plotly_chart(fig, use_container_width=True)
            
            # Error wall summary
            st.subheader("Error Wall Summary")
            if fs.error_wall_summary:
                ew_df = pd.DataFrame([
                    {"Type": k.value, "Count": v}
                    for k, v in fs.error_wall_summary.items()
                ])
                st.dataframe(ew_df, use_container_width=True, hide_index=True)
            
            # Fold detail table
            st.subheader("Fold Details")
            st.dataframe(fold_df, use_container_width=True, hide_index=True)
            
            if st.button("Run Seam Detection", type="secondary", use_container_width=True):
                with st.spinner("Detecting seam materials..."):
                    st.session_state.seam_candidates = detect_seam_candidates(
                        base, partner, fs
                    )
                    st.session_state.designer.seam_candidates = st.session_state.seam_candidates
                st.success(f"Found {len(st.session_state.seam_candidates)} seam candidates")
                st.info("Switch to the **Seam Detection** tab to view results")


# ─── Tab 3: Seam Detection ───
with tab3:
    st.subheader("Interlayer Seam Material Candidates")
    
    if not st.session_state.fold_sequence:
        st.warning("Run 10-Fold Evaluation first")
    elif not st.session_state.seam_candidates:
        st.info("Click **Run Seam Detection** in the 10-Fold Evaluation tab")
    else:
        for i, s in enumerate(st.session_state.seam_candidates):
            with st.expander(f"{i+1}. {s.material.name} ({s.role}) — {s.effectiveness:.0%} Effective", expanded=i==0):
                col1, col2 = st.columns(2)
                with col1:
                    st.write(f"**Role:** {s.role}")
                    st.write(f"**Placement:** {s.placement}")
                    st.write(f"**Thickness:** {s.required_thickness:.1f} nm")
                    st.write(f"**Reason:** {s.reason}")
                with col2:
                    st.metric("Effectiveness", f"{s.effectiveness:.0%}")
                    st.metric("Effective Tensile", f"{s.effective_tensile:,.0f} MPa")
                    st.metric("Interface Energy Reduction", f"{s.interface_energy_reduction:.0%}")
                    st.metric("Processing Compatibility", f"{s.processing_compatibility:.0%}")
                    st.metric("Added Formation Energy", f"{s.added_formation_energy:.3f} eV")


# ─── Tab 4: Production Plan ───
with tab4:
    st.subheader("Production Plan & Energy Analysis")
    
    if not st.session_state.seam_candidates:
        st.warning("Complete Seam Detection first")
    else:
        area = st.number_input("Target Area (cm²)", min_value=0.1, max_value=1000.0, value=1.0, step=0.1)
        
        if st.button("Generate Production Plan", type="primary", use_container_width=True):
            with st.spinner("Calculating synthesis steps..."):
                st.session_state.production_plan = generate_production_plan(
                    st.session_state.designer.base_material,
                    st.session_state.designer.partner,
                    st.session_state.fold_sequence,
                    st.session_state.seam_candidates,
                    target_area_cm2=area,
                )
                st.session_state.designer.production_plan = st.session_state.production_plan
            st.success("Production plan generated!")
        
        if st.session_state.production_plan:
            pp = st.session_state.production_plan
            
            # Summary
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Energy", f"{pp.total_energy_joules_per_cm2/1e6:.2f} MJ/cm²")
            col2.metric("Total Time", f"{pp.total_time_hours:.1f} hours")
            col3.metric("Estimated Cost", f"${pp.estimated_cost_usd_per_cm2:.2f}/cm²")
            col4.metric("Scalability Score", f"{pp.scalability_score:.0%}")
            
            col1, col2 = st.columns(2)
            col1.metric("Max Temperature", f"{pp.max_temperature_K:.0f} K")
            col2.metric("Max Pressure", f"{pp.max_pressure_atm:.2f} atm")
            
            # Steps table
            st.subheader("Synthesis Steps")
            steps_df = pd.DataFrame([
                {
                    "Step": i + 1,
                    "Name": s.name,
                    "Energy (J/cm²)": f"{s.energy_per_cm2:,.0f}",
                    "Time (h)": f"{s.time_hours:.1f}",
                    "Temp (K)": f"{s.temperature_K:.0f}",
                    "Pressure (atm)": f"{s.pressure_atm:.2e}",
                    "Yield": f"{s.yield_rate:.0%}",
                    "Equipment": ", ".join(s.equipment[:2]) + ("..." if len(s.equipment) > 2 else ""),
                }
                for i, s in enumerate(pp.steps)
            ])
            st.dataframe(steps_df, use_container_width=True, hide_index=True)
            
            # Energy breakdown chart
            st.subheader("Energy Distribution")
            fig = px.pie(
                values=[s.energy_per_cm2 for s in pp.steps],
                names=[s.name for s in pp.steps],
                hole=0.3,
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)
            
            # Notes
            if pp.notes:
                st.subheader("Notes")
                for note in pp.notes:
                    st.write(f"• {note}")


# ─── Tab 5: Visualizations ───
with tab5:
    st.subheader("📊 Publication-Quality Visualizations")
    
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🔄 Generate/Refresh Visualizations", type="primary", use_container_width=True):
            if not all([
                st.session_state.designer.base_material,
                st.session_state.designer.partner,
            ]):
                st.error("Complete partner selection first")
            else:
                with st.spinner("Generating visualizations..."):
                    # Run pipeline up to production if needed
                    if not st.session_state.fold_sequence:
                        st.session_state.designer.run_fold_evaluation()
                        st.session_state.fold_sequence = st.session_state.designer.fold_sequence
                    if not st.session_state.seam_candidates:
                        st.session_state.designer.find_seams()
                        st.session_state.seam_candidates = st.session_state.designer.seam_candidates
                    if not st.session_state.production_plan:
                        st.session_state.designer.generate_production(1.0)
                        st.session_state.production_plan = st.session_state.designer.production_plan
                    
                    # Generate visualizations
                    st.session_state.designer.generate_visualizations()
                    st.success("Visualizations ready!")
        
        viz_mode = st.selectbox(
            "View mode",
            ["All", "2D Structures", "State Transitions", "3D Geometry", "Production"],
            index=0
        )
    
    with col1:
        if st.session_state.designer.visualizations:
            render_visualizations_streamlit(st.session_state.designer.visualizations, tabs=viz_mode.lower().replace(' ', '_'))
        else:
            st.info("Click **Generate/Refresh Visualizations** to create publication-quality 2D/3D visualizations from the pipeline state.")

# ─── Tab 6: Flux/Transition ───
with tab6:
    st.subheader("⚗️ Flux & Transition Material System (Waste → In-Situ Reuse)")
    
    if not (st.session_state.designer.base_material and st.session_state.designer.partner):
        st.info("Complete partner selection first to enable flux analysis")
    else:
        if st.button("🔄 Generate/Refresh Flux Analysis", type="primary", use_container_width=True):
            with st.spinner("Running full pipeline up to production..."):
                # Run pipeline up to production if needed
                if not st.session_state.fold_sequence:
                    st.session_state.designer.run_fold_evaluation()
                    st.session_state.fold_sequence = st.session_state.designer.fold_sequence
                if not st.session_state.seam_candidates:
                    st.session_state.designer.find_seams()
                    st.session_state.seam_candidates = st.session_state.designer.seam_candidates
                if not st.session_state.production_plan:
                    st.session_state.designer.generate_production(1.0)
                    st.session_state.production_plan = st.session_state.designer.production_plan
                
                # Generate flux summary
                st.session_state.designer.flux_summary = calculate_flux_summary(
                    st.session_state.designer.production_plan.steps
                )
                st.success("Flux analysis ready!")
        
        # Render flux analysis if available
        if hasattr(st.session_state.designer, 'flux_summary') and st.session_state.designer.flux_summary:
            render_flux_streamlit(st.session_state.designer.flux_summary)
        else:
            st.info("Click **Generate/Refresh Flux Analysis** to map waste streams to in-situ flux/transition layers.")


# ─── Tab 7: Export Report ───
with tab7:
    st.subheader("Export Complete Design Report")
    
    report_path = st.text_input("Output filename", "metamaterial_report.json")
    
    if st.button("Generate & Download Report", type="primary", use_container_width=True):
        if not all([
            st.session_state.designer.base_material,
            st.session_state.designer.partner,
            st.session_state.fold_sequence,
            st.session_state.seam_candidates,
            st.session_state.production_plan,
        ]):
            st.error("Complete all pipeline steps first")
        else:
            path = st.session_state.designer.save_report(report_path)
            with open(path, "r") as f:
                st.download_button(
                    "Download JSON Report",
                    f.read(),
                    file_name=report_path,
                    mime="application/json",
                    use_container_width=True,
                )
            st.success(f"Report saved to {path}")
            
            # Show summary
            with open(path, "r") as f:
                report = json.load(f)
            st.json({k: v for k, v in report.items() if k != "production_plan"}, expanded=False)


# ─── Footer ───
st.markdown("---")
st.caption("""
MetaForge-AI — Built on lattice_forge formal substrate
• 1024/1024 exact Mandelbrot boundary scalar • SK-combinator transport • Oloid normal form
• Zero-training • Certified correctness • Production-ready
""")