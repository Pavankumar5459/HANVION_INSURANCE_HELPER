import streamlit as st

# Import pages
from pages.overview import show_overview
from pages.insurance_hub import show_insurance_hub
from pages.plan_wizard import show_plan_wizard
from pages.cost_calculator import show_cost_calculator
from pages.ai_assistant import show_ai_assistant
from pages.nhe_dashboard import show_nhe_dashboard

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Hanvion Health – Insurance Intelligence",
    layout="wide"
)

# ------------------------------------------------------------
# Header (clean, Healthcare.gov style)
# ------------------------------------------------------------
st.markdown(
    """
    <div style='padding: 15px 0 5px 0;'>
        <h1 style='color:#0D3B66; margin-bottom: 2px;'>Hanvion Health</h1>
        <h4 style='color:#00509E; margin-top:0; font-weight:400;'>Insurance • Costs • Intelligence Platform</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# Top Navigation Tabs
# ------------------------------------------------------------
tabs = st.tabs([
    "Overview",
    "Insurance Hub",
    "Insurance Wizard",
    "Cost Calculator",
    "NHE Dashboard",
    "AI Assistant",
])

# ------------------------------------------------------------
# Content Routing
# ------------------------------------------------------------
with tabs[0]:
    show_overview()

with tabs[1]:
    show_insurance_hub()

with tabs[2]:
    show_plan_wizard()

with tabs[3]:
    show_cost_calculator()

with tabs[4]:
    show_nhe_dashboard()

with tabs[5]:
    show_ai_assistant()
