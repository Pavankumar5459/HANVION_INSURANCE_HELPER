import streamlit as st

def show_overview():
    # Hero Section
    st.markdown(
        """
        <div style="
            padding: 32px 0;
            border-bottom: 1px solid #E2E8F0;
        ">
            <h1 style="color:#0D3B66; margin-bottom:6px;">Hanvion Health</h1>
            <h4 style="color:#00509E; margin-top:0; font-weight:400;">
                Insurance • Costs • Intelligence Platform
            </h4>
            <p style="color:#444; font-size:1.05rem; width:75%; line-height:1.6;">
                Understand U.S. health insurance with clarity — compare plans, estimate out-of-pocket costs, 
                check eligibility, explore national healthcare spending, and access personalized AI explanations.
                Built for patients, families, providers, and learners.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Start Here Section
    st.markdown("### Start Here")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style="
                border:1px solid #E0E0E0;
                padding:18px;
                border-radius:12px;
                background:white;
                box-shadow:0 2px 4px rgba(0,0,0,0.05);
                height:200px;
            ">
                <h4 style="color:#0D3B66;">Insurance Wizard</h4>
                <p style="color:#444;">
                    A guided flow that identifies the best insurance path based on age, job status, income, 
                    state, and family information.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div style="
                border:1px solid #E0E0E0;
                padding:18px;
                border-radius:12px;
                background:white;
                box-shadow:0 2px 4px rgba(0,0,0,0.05);
                height:200px;
            ">
                <h4 style="color:#0D3B66;">Cost Calculator</h4>
                <p style="color:#444;">
                    Estimate yearly premium, deductible exposure, OOP maximum risk, and subsidy impact based 
                    on Marketplace rules.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        st.markdown(
            """
            <div style="
                border:1px solid #E0E0E0;
                padding:18px;
                border-radius:12px;
                background:white;
                box-shadow:0 2px 4px rgba(0,0,0,0.05);
                height:200px;
            ">
                <h4 style="color:#0D3B66;">AI Assistant</h4>
                <p style="color:#444;">
                    Ask any insurance-related question — plan types, deductibles, OOP rules, CPT billing, 
                    allowed amount, prior authorization, and more.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # Explore More Section
    st.markdown("### Explore More")

    col4, col5 = st.columns(2)

    with col4:
        st.markdown(
            """
            <div style="
                border:1px solid #E0E0E0;
                padding:18px;
                border-radius:12px;
                background:white;
                box-shadow:0 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">Insurance Hub</h4>
                <p style="color:#444;">
                    Learn essential insurance basics — deductible, copay, coinsurance, provider networks, 
                    OOP maximums, allowed amounts, preventive care, and formulary rules.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col5:
        st.markdown(
            """
            <div style="
                border:1px solid #E0E0E0;
                padding:18px;
                border-radius:12px;
                background:white;
                box-shadow:0 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">NHE Dashboard</h4>
                <p style="color:#444;">
                    Explore U.S. National Health Expenditure (NHE) data — hospital, physician, outpatient, 
                    prescription drugs, Medicare, Medicaid, and private spending trends.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
