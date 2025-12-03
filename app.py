import streamlit as st

st.set_page_config(page_title="Hanvion Health – Insurance Intelligence", layout="wide")

from pages.overview import show_overview
from pages.insurance_hub import show_insurance_hub
from pages.plan_wizard import show_plan_wizard
from pages.cost_calculator import show_cost_calculator
from pages.ai_assistant import show_ai_assistant
from pages.nhe_dashboard import show_nhe_dashboard

# Header
st.markdown(
    """
    <div style='background: linear-gradient(90deg, #0D3B66, #00509E);
                padding: 22px; border-radius: 0px 0px 16px 16px;
                margin-bottom: 25px; color: white;'>
        <h2 style='margin:0;'>Hanvion Health</h2>
        <p style='margin-top:4px; opacity:0.9;'>Insurance • Costs • Insights</p>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.sidebar:
    st.markdown("### Navigate")
    page = st.radio(
        "",
        [
            "Overview",
            "Insurance Hub",
            "Insurance Wizard",
            "Cost Calculator",
            "AI Assistant",
            "NHE Dashboard"
        ],
    )

if page == "Overview":
    show_overview()
elif page == "Insurance Hub":
    show_insurance_hub()
elif page == "Insurance Wizard":
    show_plan_wizard()
elif page == "Cost Calculator":
    show_cost_calculator()
elif page == "AI Assistant":
    show_ai_assistant()
elif page == "NHE Dashboard":
    show_nhe_dashboard()
