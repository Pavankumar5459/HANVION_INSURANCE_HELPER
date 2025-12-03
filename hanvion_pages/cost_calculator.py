import streamlit as st

def show_cost_calculator():
    st.title("Insurance Cost Calculator")
    st.write(
        "Estimate your yearly healthcare spending based on plan details and expected usage."
    )

    st.markdown("### 1. Plan Information")

    col1, col2 = st.columns(2)

    with col1:
        monthly_premium = st.number_input(
            "Monthly Premium ($)", min_value=0, value=350
        )
        deductible = st.number_input(
            "Annual Deductible ($)", min_value=0, value=2000
        )
        oop_max = st.number_input(
            "Out-of-Pocket Maximum ($)", min_value=0, value=6500
        )

    with col2:
        copay = st.number_input(
            "Average Copay per Visit ($)", min_value=0, value=30
        )
        coinsurance = st.slider(
            "Coinsurance (%)",
            min_value=0,
            max_value=50,
            value=20
        )
        network = st.selectbox("Network Type", ["HMO", "PPO", "EPO", "HDHP + HSA"])

    st.markdown("### 2. Expected Healthcare Usage")

    col3, col4 = st.columns(2)

    with col3:
        doctor_visits = st.number_input(
            "Expected Doctor Visits per Year", min_value=0, value=4
        )
        specialist_visits = st.number_input(
            "Specialist Visits per Year", min_value=0, value=2
        )

    with col4:
        labs = st.number_input("Lab Tests per Year", min_value=0, value=2)
        emergency_visits = st.number_input(
            "Emergency Room Visits per Year", min_value=0, value=0
        )

    st.markdown("---")

    # ---------------------------------------------
    # COST CALCULATION
    # ---------------------------------------------
    # Premiums
    yearly_premium = monthly_premium * 12

    # Medical costs estimate (simple average model)
    avg_doctor_cost = 150
    avg_specialist_cost = 250
    avg_lab_cost = 80
    avg_er_cost = 1200

    total_raw_cost = (
        doctor_visits * avg_doctor_cost
        + specialist_visits * avg_specialist_cost
        + labs * avg_lab_cost
        + emergency_visits * avg_er_cost
    )

    # Apply deductible
    if total_raw_cost <= deductible:
        medical_cost_after_deductible = total_raw_cost
        deductible_met = False
    else:
        medical_cost_after_deductible = deductible + (
            (total_raw_cost - deductible) * (coinsurance / 100)
        )
        deductible_met = True

    # Cap at Out-of-Pocket Maximum
    final_medical_cost = min(medical_cost_after_deductible, oop_max)

    # Total yearly cost
    total_yearly_cost = yearly_premium + final_medical_cost

    # ---------------------------------------------
    # OUTPUT
    # ---------------------------------------------
    st.subheader("Estimated Total Yearly Cost")
    st.success(f"${total_yearly_cost:,.2f}")

    st.markdown("### Breakdown")
    st.write(f"**Yearly Premium:** ${yearly_premium:,.2f}")
    st.write(f"**Medical Spending (after deductible & coinsurance):** ${final_medical_cost:,.2f}")

    if deductible_met:
        st.info("Your deductible is fully met this year.")
    else:
        st.info("Your deductible is NOT fully met this year.")

    st.markdown("---")
    st.caption("Estimates based on typical national averages. Actual costs vary by provider, region, and plan details.")
