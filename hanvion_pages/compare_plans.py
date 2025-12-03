import streamlit as st
import pandas as pd

# ------------------------------------------------------------
# Scoring Function
# ------------------------------------------------------------
def score_plan(plan):
    score = 0

    # Premium (lower = better)
    score += max(0, 25 - (plan["premium"] / 10))

    # Deductible
    score += max(0, 20 - (plan["deductible"] / 500))

    # Out-of-pocket max
    score += max(0, 20 - (plan["oop_max"] / 750))

    # Coinsurance logic
    score += max(0, 15 - (plan["coinsurance"] / 5))

    # Network size
    score += min(10, (plan["network_size"] / 1000) * 10)

    # Extra benefits
    benefits_count = plan["extra_benefits"]
    score += min(10, benefits_count * 2)

    return round(score, 2)


# ------------------------------------------------------------
# Compare Plans Main Page
# ------------------------------------------------------------
def show_compare_plans():
    st.title("Compare Health Insurance Plans")

    st.write("Upload plan data or use sample marketplace plans to compare costs, coverage, and benefits.")

    # ------------------------------------------------------------
    # Sample Demo Dataset
    # ------------------------------------------------------------
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

    uploaded_file = st.file_uploader("Upload plan CSV", type=["csv"])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
    else:
        df = sample_data.copy()

    # ------------------------------------------------------------
    # Compute Scores
    # ------------------------------------------------------------
    df["score"] = df.apply(score_plan, axis=1)

    st.subheader("Plan Comparison Table")
    st.dataframe(df, use_container_width=True)

    # ------------------------------------------------------------
    # Best Plan Recommendations
    # ------------------------------------------------------------
    st.subheader("Recommended Plans")

    best_overall = df.loc[df["score"].idxmax()]
    best_low_cost = df.loc[df["premium"].idxmin()]
    best_low_deductible = df.loc[df["deductible"].idxmin()]
    best_family = df.loc[df["extra_benefits"].idxmax()]

    st.markdown("### Best Overall")
    st.info(f"{best_overall['plan_name']} — Score: {best_overall['score']}")

    st.markdown("### Best for Low Monthly Premium")
    st.info(f"{best_low_cost['plan_name']} — ${best_low_cost['premium']}")

    st.markdown("### Best for Low Deductible")
    st.info(f"{best_low_deductible['plan_name']} — ${best_low_deductible['deductible']}")

    st.markdown("### Best for Families (More Benefits)")
    st.info(f"{best_family['plan_name']} — {best_family['extra_benefits']} added benefits")

    # ------------------------------------------------------------
    # Detailed Plan Cards
    # ------------------------------------------------------------
    st.subheader("Detailed Plan Insights")

    for _, row in df.iterrows():
        with st.expander(f"{row['plan_name']} – Score {row['score']}"):
            st.write(f"Premium: ${row['premium']}")
            st.write(f"Deductible: ${row['deductible']}")
            st.write(f"Out-of-Pocket Max: ${row['oop_max']}")
            st.write(f"Coinsurance: {row['coinsurance']}%")
            st.write(f"Network Size: {row['network_size']} providers")
            st.write(f"Extra Benefits: {row['extra_benefits']} services")
