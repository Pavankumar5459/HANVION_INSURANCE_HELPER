import streamlit as st
import pandas as pd

def show_compare_plans():
    st.title("Compare Health Insurance Plans")
    st.write("Compare plan costs, deductibles, and out-of-pocket expenses.")

    # -----------------------------------------
    # TYPICAL ACA PLAN DATASET (No HTML)
    # -----------------------------------------
    plan_data = {
        "Plan Type": ["Bronze", "Silver", "Gold", "Platinum", "HDHP"],
        "Monthly Premium": [350, 480, 620, 750, 310],
        "Deductible": [6000, 4500, 1500, 500, 7000],
        "Out-of-Pocket Max": [9000, 8500, 6000, 4000, 9000],
        "Coinsurance (%)": [40, 30, 20, 10, 0],
        "Typical Use Case": [
            "Healthy individuals, low premiums",
            "Balanced cost-sharing (most popular)",
            "Frequent care and specialist visits",
            "High usage, predictable costs",
            "Low premiums + HSA eligibility"
        ]
    }

    df = pd.DataFrame(plan_data)

    # -----------------------------------------
    # SELECT PLANS
    # -----------------------------------------
    st.subheader("Select Plans to Compare")

    selected = st.multiselect(
        "Choose at least two plans:",
        df["Plan Type"].tolist(),
        default=["Bronze", "Silver"]
    )

    if len(selected) < 2:
        st.warning("Please select at least two plans to continue.")
        return

    compare_df = df[df["Plan Type"].isin(selected)]

    st.subheader("Plan Comparison Table")
    st.dataframe(compare_df, use_container_width=True)

    # -----------------------------------------
    # USAGE INPUT
    # -----------------------------------------
    st.subheader("Expected Medical Usage")

    visits = st.slider("Yearly doctor/specialist visits", 0, 20, 4)
    rx = st.slider("Monthly prescriptions", 0, 10, 1)
    er_visits = st.slider("Emergency room visits per year", 0, 3, 0)

    # -----------------------------------------
    # COST CALCULATION
    # -----------------------------------------
    st.subheader("Estimated Yearly Cost")

    avg_visit_cost = 150
    avg_rx_cost = 60
    avg_er_cost = 1200

    usage_cost = (
        visits * avg_visit_cost +
        rx * avg_rx_cost * 12 +
        er_visits * avg_er_cost
    )

    results = []

    for _, row in compare_df.iterrows():
        premium_annual = row["Monthly Premium"] * 12
        deductible = row["Deductible"]
        oop_max = row["Out-of-Pocket Max"]
        coins_rate = row["Coinsurance (%)"] / 100

        # Apply deductible logic
        if usage_cost <= deductible:
            medical_cost = usage_cost
        else:
            medical_cost = deductible + (usage_cost - deductible) * coins_rate

        final_cost = min(medical_cost, oop_max) + premium_annual

        results.append({
            "Plan Type": row["Plan Type"],
            "Yearly Premium": premium_annual,
            "Medical Spending": min(medical_cost, oop_max),
            "Total Estimated Cost": final_cost
        })

    result_df = pd.DataFrame(results)

    st.dataframe(result_df, use_container_width=True)

    # -----------------------------------------
    # Recommendation
    # -----------------------------------------
    best = result_df.loc[result_df["Total Estimated Cost"].idxmin()]

    st.subheader("Best Plan Based on Your Usage")
    st.success(
        f"**{best['Plan Type']}** is estimated to be the most cost-effective.\n\n"
        f"Estimated yearly cost: **${best['Total Estimated Cost']:,.2f}**"
    )
