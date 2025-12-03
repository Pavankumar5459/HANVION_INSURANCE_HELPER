import streamlit as st

def show_plan_wizard():
    st.title("Insurance Plan Wizard")
    st.write("Answer a few quick questions to find the best insurance plan for your needs.")

    # -----------------------------
    # Step 1: Age Group
    # -----------------------------
    age = st.selectbox(
        "What is your age group?",
        ["Under 18", "18–29", "30–45", "46–64", "65 and older"]
    )

    # -----------------------------
    # Step 2: Medical Usage
    # -----------------------------
    usage = st.selectbox(
        "How often do you expect to use healthcare?",
        [
            "Very rarely (1–2 visits a year)", 
            "Occasionally (3–6 visits a year)",
            "Frequently (monthly visits)",
            "Chronic conditions requiring regular care"
        ]
    )

    # -----------------------------
    # Step 3: Budget Preference
    # -----------------------------
    budget = st.selectbox(
        "What is your monthly premium preference?",
        ["Lowest cost", "Moderate cost", "Higher cost for best coverage"]
    )

    # -----------------------------
    # Step 4: Deductible Preference
    # -----------------------------
    deductible_pref = st.selectbox(
        "Preferred deductible style:",
        ["Low deductible", "Medium deductible", "High deductible (okay with HDHP)"]
    )

    # -----------------------------
    # Step 5: Network Flexibility
    # -----------------------------
    network = st.selectbox(
        "Do you need out-of-network coverage?",
        ["No", "Yes", "Not sure"]
    )

    # -----------------------------
    # Step 6: Medication Needs
    # -----------------------------
    meds = st.selectbox(
        "Do you take medications regularly?",
        ["No", "Occasionally", "Monthly", "Multiple medications monthly"]
    )

    # -----------------------------
    # Step 7: Travel Frequency
    # -----------------------------
    travel = st.selectbox(
        "Do you travel frequently (out of state)?",
        ["No", "Yes"]
    )

    st.markdown("---")

    # -----------------------------
    # Recommendation Logic
    # -----------------------------
    result = ""
    reasoning = []

    # HDHP Recommendation Logic
    if budget == "Lowest cost" and deductible_pref == "High deductible (okay with HDHP)":
        result = "High Deductible Health Plan (HDHP) + HSA"
        reasoning.append("You prefer the lowest premiums and are okay with a high deductible.")
        reasoning.append("You can also save money tax-free using an HSA.")

    # HMO Recommendation
    elif network == "No" and budget != "Higher cost for best coverage":
        result = "HMO (Health Maintenance Organization)"
        reasoning.append("HMO plans have lower monthly premiums.")
        reasoning.append("You prefer to stay in-network and don't require flexibility.")

    # PPO Recommendation
    elif network == "Yes" or travel == "Yes":
        result = "PPO (Preferred Provider Organization)"
        reasoning.append("PPO plans offer out-of-network coverage and more flexibility.")
        reasoning.append("Ideal for frequent travelers or those seeing multiple specialists.")

    # EPO Recommendation
    elif network == "Not sure" and budget == "Moderate cost":
        result = "EPO (Exclusive Provider Organization)"
        reasoning.append("EPO plans offer moderate premiums without referrals.")
        reasoning.append("A good balance between HMO and PPO.")

    # Chronic Conditions
    if usage == "Chronic conditions requiring regular care":
        result = "Low Deductible PPO or Gold Tier Plan"
        reasoning.append("You need predictable costs and regular access to specialists.")

    # Medicaid
    if age == "Under 18" and budget == "Lowest cost":
        result = "Medicaid (Child Health Program)"
        reasoning.append("Children with low-income households often qualify for Medicaid.")

    # Medicare
    if age == "65 and older":
        result = "Medicare Advantage (Part C)"
        reasoning.append("This includes hospital, doctor, and prescription coverage.")

    # If still empty → default
    if result == "":
        result = "Silver Tier Marketplace Plan"
        reasoning.append("You fit a broad usage and budget category suitable for Silver-level plans.")

    # -----------------------------
    # Output
    # -----------------------------
    st.subheader("Recommended Plan Type")
    st.success(result)

    st.subheader("Why this plan fits you")
    for reason in reasoning:
        st.write("- " + reason)

    st.markdown("---")
    st.info("This tool provides educational guidance only. For exact eligibility and pricing, refer to Healthcare.gov.")
