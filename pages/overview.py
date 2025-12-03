import streamlit as st

def show_overview():
    # Hero section
    st.markdown(
        """
        <div style="
            padding: 30px 0;
            border-bottom: 1px solid #E2E8F0;
        ">
            <h1 style="color:#0D3B66; margin-bottom:6px;">Hanvion Health</h1>
            <h4 style="color:#00509E; margin-top:0; font-weight:400;">
                Insurance • Costs • Intelligence Platform
            </h4>
            <p style="color:#444; font-size:1.05rem; width:75%; line-height:1.6;">
                A clean and simple way to understand U.S. health insurance — compare 
                plans, estimate costs, explore national healthcare spending, and get 
                instant answers from AI. Built for patients, providers, and learners.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

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
                box-shadow:0px 2px 4px rgba(0,0,0,0.05);
                height:190px;
            ">
                <h4 style="color:#0D3B66;">Insurance Wizard</h4>
                <p style="color:#444;">Find which type of plan fits your situation based on age, income, job status, and state.</p>
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
                box-shadow:0px 2px 4px rgba(0,0,0,0.05);
                height:190px;
            ">
                <h4 style="color:#0D3B66;">Cost Calculator</h4>
                <p style="color:#444;">Estimate premiums, deductibles, and your expected annual spending.</p>
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
                box-shadow:0px 2px 4px rgba(0,0,0,0.05);
                height:190px;
            ">
                <h4 style="color:#0D3B66;">AI Assistant</h4>
                <p style="color:#444;">Ask any health insurance question and get instant, clear answers.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

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
                box-shadow:0px 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">Insurance Hub</h4>
                <p style="color:#444;">Learn insurance fundamentals — deductible, copay, coinsurance, networks, and more.</p>
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
                box-shadow:0px 2px 4px rgba(0,0,0,0.05);
            ">
                <h4 style="color:#0D3B66;">NHE Dashboard</h4>
                <p style="color:#444;">Explore U.S. healthcare spending trends from official NHE datasets.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
