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
# Global UI Styling
# ------------------------------------------------------------
st.markdown(
    """
    <style>

    /* Global font */
    html, body, [class*="css"]  {
        font-family: "Inter", sans-serif;
        color: #222222;
    }

    /* Titles */
    h1 {
        font-size: 1.9rem !important;
        font-weight: 700 !important;
    }
    h2 {
        font-size: 1.4rem !important;
        font-weight: 600 !important;
    }
    h3, h4 {
        font-weight: 600 !important;
    }

    /* Tabs */
    .stTabs [role="tablist"] button {
        font-size: 1rem !important;
        padding-top: 8px !important;
        padding-bottom: 8px !important;
        color: #0D3B66 !important;
        border-bottom: 2px solid #ddd;
    }

    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #00509E !important;
        font-weight: 600 !important;
    }

    /* Cards used in Hub */
    div[data-testid="stMarkdownContainer"] > div {
        border-radius: 10px;
    }

    /* Buttons */
    .stButton button {
        background-color: #0D3B66 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
        border: none !important;
    }
    .stButton button:hover {
        background-color: #00509E !important;
    }

    /* Input fields */
    .stTextInput input, .stNumberInput input, .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid #BBB !important;
        padding: 8px !important;
    }

    /* Section spacing */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }

    </style>
    """,
    unsafe_allow_html=True,
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
