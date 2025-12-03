import streamlit as st

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------
st.set_page_config(
    page_title="Hanvion Health – Insurance Intelligence Platform",
    layout="wide"
)

# ------------------------------------------------------------
# Global Styling (Healthcare.gov look)
# ------------------------------------------------------------
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: "Inter", sans-serif;
        color: #222222;
    }

    h1 { font-size: 2rem !important; font-weight: 700 !important; }
    h2 { font-size: 1.4rem !important; font-weight: 600 !important; }
    h3, h4 { font-weight: 600 !important; }

    .stTabs [role="tablist"] button {
        font-size: 1rem !important;
        padding-top: 8px !important;
        padding-bottom: 8px !important;
        color: #0D3B66 !important;
        border-bottom: 2px solid #ddd !important;
    }
    .stTabs [aria-selected="true"] {
        border-bottom: 3px solid #00509E !important;
        font-weight: 600 !important;
    }

    .stButton button {
        background-color: #0D3B66 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 0.5rem 1rem !important;
    }
    .stButton button:hover {
        background-color: #00509E !important;
    }

    .stTextInput input,
    .stNumberInput input,
    .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid #BBB !important;
        padding: 8px !important;
    }

    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------
# IMPORT ALL PAGES
# ------------------------------------------------------------
from hanvion_pages.overview import show_overview
from hanvion_pages.insurance_hub import show_insurance_hub
from hanvion_pages.plan_wizard import show_plan_wizard
from hanvion_pages.cost_calculator import show_cost_calculator
from hanvion_pages.compare_plans import show_compare_plans
from hanvion_pages.nhe_dashboard import show_nhe_dashboard
from hanvion_pages.ai_assistant import show_ai_assistant
from hanvion_pages.ocr_insurance import show_ocr
from hanvion_pages.ocr_plan_pdf import show_pdf_ocr
from hanvion_pages.faq import show_faq
from hanvion_pages.about import show_about

# ------------------------------------------------------------
# HEADER
# ------------------------------------------------------------
st.title("Hanvion Health")
st.subheader("Insurance • Costs • Intelligence Platform")

st.markdown("---")

# ------------------------------------------------------------
# TABS (TOP NAVIGATION)
# ------------------------------------------------------------
tabs = st.tabs([
    "Overview",
    "Insurance Hub",
    "Insurance Wizard",
    "Cost Calculator",
    "Compare Plans",
    "NHE Dashboard",
    "AI Assistant",
    "OCR – Insurance Card",
    "OCR – Plan PDF",
    "FAQ",
    "About"
])

# ------------------------------------------------------------
# ROUTER
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
    show_compare_plans()

with tabs[5]:
    show_nhe_dashboard()

with tabs[6]:
    show_ai_assistant()

with tabs[7]:
    show_ocr()

with tabs[8]:
    show_pdf_ocr()

with tabs[9]:
    show_faq()

with tabs[10]:
    show_about()
