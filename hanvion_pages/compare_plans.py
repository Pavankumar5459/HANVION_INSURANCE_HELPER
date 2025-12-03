import streamlit as st
import pandas as pd


# ------------------------------------------------------------
# NORMALIZED SCORING FUNCTION (Based on User Weights)
# ------------------------------------------------------------
def calculate_plan_score(plan, weights):
    # Normalize weights to sum to 1.0
    total_weight = sum(weights.values())
    w = {k: v / total_weight for k, v in weights.items()}

    score = 0

    # Premium (lower = better)
    score += w["premium"] * max(0, 100 - (plan["premium"] / 10))

    # Deductible
    score += w["deductible"] * max(0, 100 - (plan["deductible"] / 100))

    # OOP Max
    score += w["oop_max"] * max(0, 100 - (plan["oop_max"] / 100))

    # Coinsurance
    score += w["coinsurance"] * max(0, 100 - (plan["coinsurance"] * 2))

    # Network Size
    score += w["network"] * min(100, plan["network_size"] / 100)

    # Extra Benefits
    score += w["benefits"] * min(100, plan["extra_benefits"] * 20)

    return round(score, 2)



# ------------------------------------------------------------
# MAIN PAGE
# ------------------------------------------------------------
def show_compare_plans():
    st.title("Compare Health Insurance Plans")

    st.write("Adjust scoring weights and compare how different plans rank based on your preferences.")

    # ------------------------------------------------------------
    # WEIGHT ADJUSTMENT SECTION
    # ------------------------------------------------------------
    st.header("Customize Scoring Weights")

    col1, col2, col3 = st.columns(3)

    with col1:
        premium_w = st.slider("Premium Weight (%)", 0, 30, 25)
        deductible_w = st.slider("Deductible Weight (%)", 0, 25, 20)

    with col2:
        oop_w = st.slider("OOP Max Weight (%)", 0, 25, 20)
        coins_w = st.slider("Coinsurance Weight (%)", 0, 20, 15)

    with col3:
        network_w = st.slider("Network Size Weight (%)", 0, 15, 10)
        benefits_w = st.slider("Extra Benefits Weight (%)", 0, 15, 10)

    weights = {
        "premium": premium_w,
        "deductible": deductible_w,
        "oop_max": oop_w,
        "coinsurance": coins_w,
        "network": network_w,
        "benefits": benefits_w,
    }

    st.markdown("---")

    # ------------------------------------------------------------
    # SAMPLE PLANS (If No Upload)
    # ------------------------------------------------------------
    st.subheader("Plan Dataset")

    sample_data = pd.DataFrame([
        {
            "plan_name": "SilverCare Advantage",
            "premium": 420,
            "deductible": 2500,
            "oop_max": 9000,
            "coinsurance": 20,
            "network_size": 5400,
            "extra_benefits": 3,
        },
        {
            "plan_name": "HealthyPlus Bronze",
            "premium": 310,
            "deductible": 6000,
            "oop_max": 8700,
            "coinsurance": 40,
            "network_size": 3500,
            "extra_benefits": 1,
        },
        {
            "plan_name": "FamilyCare Gold",
            "premium": 560,
            "deductible": 1500,
            "oop_max": 6500,
            "coinsurance": 10,
            "network_size": 6200,
            "extra_benefits": 4,
        }
    ])

    uploaded_file = st.file_uploader("Upload CSV file with plan data", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = sample_data.copy()

    # ------------------------------------------------------------
    # APPLY NEW SCORING
    # ------------------------------------------------------------
    st.subheader("Plan Rankings (Based on Your Weight Preferences)")

    df["score"] = df.apply(lambda row: calculate_plan_score(row, weights), axis=1)

    st.dataframe(df.sort_values("score", ascending=False), use_container_width=True)

    st.markdown("---")

    # ------------------------------------------------------------
    # RECOMMENDATIONS
    # ------------------------------------------------------------
    st.subheader("Personalized Recommendations")

    best_overall = df.loc[df["score"].idxmax()]

    st.info(
        f"**Best Overall Plan:** {best_overall['plan_name']} "
        f"(Score: {best_overall['score']}) \n\n"
        "Selected based on your scoring weights."
    )

    # ------------------------------------------------------------
    # EXPANDABLE PLAN DETAILS
    # ------------------------------------------------------------
    st.subheader("Detailed Plan Insights")

    for _, row in df.iterrows():
        with st.expander(f"{row['plan_name']} — Score {row['score']}"):
            st.write(f"Monthly Premium: ${row['premium']}")
            st.write(f"Deductible: ${row['deductible']}")
            st.write(f"Out-of-Pocket Max: ${row['oop_max']}")
            st.write(f"Coinsurance: {row['coinsurance']}%")
            st.write(f"Network Size: {row['network_size']}")
            st.write(f"Extra Benefits Count: {row['extra_benefits']}")
