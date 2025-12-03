import streamlit as st

def show_overview():
    # Header Section (Hero)
    st.markdown(
        """
        <div style="
            padding: 18px 0 10px 0;
            border-bottom: 1px solid #E2E8F0;
        ">
            <h2 style="color:#0D3B66; margin-bottom:4px;">Welcome to Hanvion Health</h2>
            <p style="color:#444; font-size:1.05rem; margin-top:0;">
                A clear and simple way to understand U.S. health insurance — eligibility, plans, costs, and national trends.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### Start Here")

    col1, col2, col3 = st.columns(3)

    # Card 1 — Wizard
    with col1:
        st.markdown(
            """
            <div style="
                border: 1px solid #E0E0E0;
                padding: 18px;
                border-radius: 12px;
                background: white;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
                height: 190px;
            ">
                <h4 style="color:#0D3B66; margin-bottom:8px;">Insurance Wizard</h4>
                <p style="color:#444; line-height:1.45;">
                    A step-by-step guide to help you determine which insurance category fits your situation.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Card 2 — Cost Calculator
    with col2:
        st.markdown(
            """
            <div style="
                border: 1px solid #E0E0E0;
                padding: 18px;
                border-radius: 12px;
                background: white;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
                height: 190px;
            ">
                <h4 style="color:#0D3B66; margin-bottom:8px;">Cost Calculator</h4>
                <p style="color:#444; line-height:1.45;">
                    Estimate premiums, deductibles, and expected yearly healthcare costs based on real plan rules.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Card 3 — AI Assistant
    with col3:
        st.markdown(
            """
            <div style="
                border: 1px solid #E0E0E0;
                padding: 18px;
                border-radius: 12px;
                background: white;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
                height: 190px;
            ">
                <h4 style="color:#0D3B66; margin-bottom:8px;">AI Insurance Assistant</h4>
                <p style="color:#444; line-height:1.45;">
                    Ask any insurance-related question in clear language — coverage, eligibility, costs, and more.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("### Explore More")

    col4, col5 = st.columns([1, 1])

    with col4:
        st.markdown(
            """
            <div style="
                border: 1px solid #E0E0E0;
                padding: 18px;
                border-radius: 12px;
                background: white;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">Insurance Hub</h4>
                <p style="color:#444; line-height:1.45;">
                    Understand key insurance terms: deductible, copay, coinsurance, out-of-pocket max, subsidies,
                    allowed amount, and coverage rules.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            """
            <div style="
                border: 1px solid #E0E0E0;
                padding: 18px;
                border-radius: 12px;
                background: white;
                box-shadow: 0px 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">NHE Dashboard</h4>
                <p style="color:#444; line-height:1.45;">
                    View national healthcare expenditure trends — hospital, physician, prescription, Medicare,
                    Medicaid, private health insurance, and out-of-pocket spending.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
