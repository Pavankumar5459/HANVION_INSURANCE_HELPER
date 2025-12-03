import streamlit as st

# --------------------------------------------------------
# Basic actuarial assumptions for ACA tiers (national avg)
# --------------------------------------------------------
PLAN_DATA = {
    "Bronze": {
        "premium": 4200,
        "deductible": 7000,
        "oop_max": 9100,
        "coverage": "60% actuarial value",
        "ideal": "Good for healthy individuals who rarely visit doctors and want a lower premium.",
    },
    "Silver": {
        "premium": 6000,
        "deductible": 4500,
        "oop_max": 8500,
        "coverage": "70% actuarial value",
        "ideal": "Best overall value. Eligible for CSR discounts based on income.",
    },
    "Gold": {
        "premium": 7200,
        "deductible": 1500,
        "oop_max": 6000,
        "coverage": "80% actuarial value",
        "ideal": "Good for individuals who frequently use healthcare services.",
    },
    "Platinum": {
        "premium": 9000,
        "deductible": 500,
        "oop_max": 4500,
        "coverage": "90% actuarial value",
        "ideal": "Best for people with chronic conditions and predictable, high yearly usage.",
    },
}


def render_plan_card(name, data):
    """Healthcare.gov style plan card."""
    st.markdown(
        f"""
        <div style="
            border:1px solid #E0E0E0;
            padding:18px;
            border-radius:12px;
            background:white;
            box-shadow:0px 2px 4px rgba(0,0,0,0.06);
            height: 300px;
        ">
            <h3 style="color:#0D3B66; margin-bottom:6px;">{name} Plan</h3>

            <p style="margin:4px 0; color:#333;">
                <strong>Premium:</strong> ${data['premium']:,}/year
            </p>
            <p style="margin:4px 0; color:#333;">
                <strong>Deductible:</strong> ${data['deductible']:,}
            </p>
            <p style="margin:4px 0; color:#333;">
                <strong>Out-of-Pocket Max:</strong> ${data['oop_max']:,}
            </p>
            <p style="margin:4px 0; color:#333;">
                <strong>Coverage Level:</strong> {data['coverage']}
            </p>

            <p style="margin-top:10px; color:#444; line-height:1.4;">
                {data['ideal']}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# --------------------------------------------------------
# CSR Adjustment Logic
# --------------------------------------------------------
def csr_adjustments(fpl_ratio):
    """Return CSR-adjusted Silver plan values."""
    if fpl_ratio <= 1.5:  # CSR 94
        return {
            "premium": 6000,
            "deductible": 500,
            "oop_max": 2000,
            "coverage": "94% actuarial value",
            "ideal": "Best for low-income enrollees; extremely strong financial assistance.",
        }
    if fpl_ratio <= 2.0:  # CSR 87
        return {
            "premium": 6000,
            "deductible": 1500,
            "oop_max": 3000,
            "coverage": "87% actuarial value",
            "ideal": "Excellent coverage for moderate-income enrollees.",
        }
    if fpl_ratio <= 2.5:  # CSR 73
        return {
            "premium": 6000,
            "deductible": 2500,
            "oop_max": 5500,
            "coverage": "73% actuarial value",
            "ideal": "Lower deductible compared to standard Silver.",
        }

    return PLAN_DATA["Silver"]


# --------------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------------
def show_compare_plans():

    st.title("Compare Marketplace Metal Plans")

    st.write(
        "Compare Bronze, Silver, Gold, and Platinum plans side-by-side to understand differences "
        "in premiums, deductibles, and expected coverage levels."
    )

    st.markdown("### Step 1: Enter Income Information (optional)")

    income = st.number_input("Household Income ($)", 0, 300000, 45000)
    household = st.number_input("Household Size", 1, 10, 1)

    # FPL table
    fpl_table = {
        1: 14580,
        2: 19720,
        3: 24860,
        4: 30000,
    }

    if household <= 4:
        fpl = fpl_table[household]
    else:
        fpl = 30000 + (household - 4) * 5140

    fpl_ratio = income / fpl if fpl > 0 else 10

    # CSR Silver plan logic
    if fpl_ratio <= 2.5:
        silver_data = csr_adjustments(fpl_ratio)
    else:
        silver_data = PLAN_DATA["Silver"]

    st.markdown("### Step 2: Plan Comparison")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_plan_card("Bronze", PLAN_DATA["Bronze"])

    with col2:
        render_plan_card("Silver", silver_data)

    with col3:
        render_plan_card("Gold", PLAN_DATA["Gold"])

    with col4:
        render_plan_card("Platinum", PLAN_DATA["Platinum"])

    st.markdown("### How to Choose")

    st.write(
        """
        **Bronze:** Good for low-usage individuals who want the lowest premiums.  
        **Silver:** Best overall value. If your income qualifies, CSR benefits make Silver extremely strong.  
        **Gold:** Good for people with frequent doctor visits or ongoing treatment.  
        **Platinum:** Best protection, but high premium.  
        """
    )

    if fpl_ratio <= 2.5:
        st.info(
            "Based on your income, you qualify for **Cost Sharing Reductions**, making Silver much stronger "
            "than Bronze or Gold."
        )
