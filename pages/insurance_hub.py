import streamlit as st


def card(title, body):
    st.markdown(
        f"""
        <div style="
            border:1px solid #E5E7EB;
            padding:18px;
            border-radius:12px;
            background:white;
            margin-bottom:15px;">
            <h4 style="margin:0; color:#0D3B66;">{title}</h4>
            <p style="color:#333; margin-top:6px;">{body}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_insurance_hub():
    st.title("Insurance Education Hub")

    st.write(
        "Understand key insurance concepts in simple, clear language. "
        "These definitions follow official Marketplace and employer-plan rules."
    )

    st.subheader("Core Cost Concepts")

    card("Deductible",
         "The amount you pay for covered health services before your insurance begins paying. "
         "Example: If your deductible is $2,000, you pay the first $2,000 of covered services yourself.")

    card("Copay",
         "A fixed amount you pay for certain services (e.g., $30 for a doctor visit). "
         "Copays typically do not count toward the deductible but do count toward your out-of-pocket maximum.")

    card("Coinsurance",
         "Your share of costs after you meet your deductible. "
         "Example: If the allowed amount is $200 and your coinsurance is 20%, you pay $40.")

    card("Out-of-Pocket Maximum (OOP Max)",
         "The most you will pay in a coverage year for covered services. "
         "After reaching this amount, insurance pays 100% of covered services.")

    st.subheader("Plan Network Types")

    card("HMO (Health Maintenance Organization)",
         "Lower cost, requires referrals, limited to in-network doctors. Best for predictable care within a single network.")

    card("PPO (Preferred Provider Organization)",
         "More expensive, but flexible. No referrals needed and out-of-network coverage included at higher cost.")

    card("EPO (Exclusive Provider Organization)",
         "A mix of HMO and PPO. No out-of-network coverage, but no referrals needed. Lower cost than PPO.")

    card("HDHP (High Deductible Health Plan)",
         "Lower premiums but high deductible. HSA eligible. Best for people who want to save tax-free or rarely use care.")

    st.subheader("Marketplace Metal Tiers")

    card("Bronze",
         "Lowest premiums, highest deductibles. Good for people who rarely use care.")

    card("Silver",
         "Moderate premiums and moderate deductibles. Eligible for CSR discounts if income qualifies.")

    card("Gold",
         "Higher premiums but lower deductibles and better coverage. Best for people who use care frequently.")

    card("Platinum",
         "Highest premiums but lowest out-of-pocket costs. Rare in many states.")

    st.subheader("Additional Terms")

    card("Preventive Care",
         "Screenings and vaccines covered at no cost under most plans.")

    card("Prior Authorization",
         "Some procedures require insurance approval before they are covered.")

    card("Referral",
         "Some plans require a referral from your primary doctor to see a specialist.")
