import streamlit as st

def show_insurance_hub():

    # =====================================================
    # PAGE HEADER
    # =====================================================
    st.markdown(
        """
        <h1 style='color:#0D3B66; font-weight:800; margin-bottom:0px;'>Insurance Education Hub</h1>
        <p style='color:#333; font-size:18px; margin-top:4px;'>
            Learn essential health insurance concepts and follow a smart 12-point checklist before choosing a plan.
        </p>
        <hr style='margin-top:18px; margin-bottom:28px; border:1px solid #E1E5EB;'>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # TEMPLATE FUNCTIONS
    # =====================================================
    def section_title(text):
        st.markdown(
            f"""
            <div style='font-size:22px; font-weight:700; color:#0D3B66; margin-top:10px; margin-bottom:10px;'>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    def card(text):
        st.markdown(
            f"""
            <div style="
                background:#F7FAFC;
                padding:16px 18px;
                border-radius:10px;
                border:1px solid #DFE6EE;
                font-size:16px;
                color:#333;
                line-height:1.55;
                margin-bottom:10px;
            ">
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # MAIN TWO-COLUMN LAYOUT
    # =====================================================
    col1, col2 = st.columns([1, 1.2])

    # =====================================================
    # LEFT COLUMN — CORE TERMS
    # =====================================================
    with col1:
        section_title("Core U.S. Insurance Terms")

        terms = {
            "Premium":
                "The fixed monthly amount you pay to keep your insurance active.",

            "Deductible":
                "The amount you pay each year before insurance starts covering costs.",

            "Coinsurance":
                "The percentage you pay after meeting the deductible (e.g., 20%).",

            "Copay":
                "A fixed fee for specific services (e.g., $30 doctor visit).",

            "Out-of-Pocket Maximum":
                "The maximum amount you pay in a year before insurance covers 100% of covered care.",

            "Allowed Amount":
                "The maximum charge an insurer will pay for a service.",

            "Explanation of Benefits (EOB)":
                "A breakdown of what insurance paid and what you owe for a claim.",

            "Network":
                "Hospitals and doctors contracted with your insurance.",

            "Prior Authorization":
                "Approval required before certain procedures or medications.",

            "Formulary":
                "List of medications covered by the plan, divided into tiers.",

            "Subsidy":
                "Discounts from the government that reduce your premium (ACA Marketplace).",

            "CSR (Cost-Sharing Reductions)":
                "Lower deductibles/copays for eligible income groups.",

            "Preventive Care":
                "Fully covered services such as annual checkups and vaccines.",
        }

        for title, desc in terms.items():
            with st.expander(f"{title}", expanded=False):
                card(desc)

    # =====================================================
    # RIGHT COLUMN — 12-POINT CHECKLIST
    # =====================================================
    with col2:
        section_title("12-Point Smart Insurance Buyer Checklist")

        checklist = {
            "1. Identify Your Needs":
                "Family size, medical history, income, emergency funds, and coverage expectations.",

            "2. Don’t Choose Based Only on Premium":
                "Low premiums often mean high deductibles.",

            "3. Check Claim Settlement Quality":
                "Many insurers settle claims, but the percentage paid matters more.",

            "4. Read Exclusions Carefully":
                "Always ask what is NOT covered — this prevents surprises.",

            "5. Beware of Agent Bias":
                "Agents push high-commission plans. Always compare plans yourself.",

            "6. Check Network Hospitals Near You":
                "More hospitals = better emergency coverage.",

            "7. Choose Long-Term Benefits":
                "Ignore flashy short-term discounts.",

            "8. Adequate Term Coverage":
                "Income × 10 is a safe rule. Adjust for inflation.",

            "9. Senior Coverage for Parents":
                "Older adults need higher limits and good cashless options.",

            "10. Check Documentation Accuracy":
                "Incorrect DOB or KYC can cause claim rejection.",

            "11. Evaluate Real Customer Feedback":
                "Judge based on claim delays and service quality.",

            "12. Add-Ons Matter":
                "Tech-based surgeries (robotic), room rent waivers, etc. must be included.",
        }

        for title, desc in checklist.items():
            with st.expander(f"{title}", expanded=False):
                card(desc)
