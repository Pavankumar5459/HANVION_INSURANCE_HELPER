import streamlit as st
import pandas as pd
import numpy as np


# ------------------------------------------------------------
# Federal Poverty Level Table (2024)
# ------------------------------------------------------------
def get_fpl(household_size):
    fpl_base = {
        1: 14580,
        2: 19720,
        3: 24860,
        4: 30000,
    }
    if household_size <= 4:
        return fpl_base[household_size]
    else:
        extra = household_size - 4
        return 30000 + extra * 5140


# ------------------------------------------------------------
# Premium variation by ZIP (approximate regional factor)
# ------------------------------------------------------------
def zip_factor(zip_code):
    if not zip_code:
        return 1.0

    z = str(zip_code).strip()

    northeast = ["0", "1"]
    south = ["2", "3"]
    midwest = ["4", "5"]
    west = ["8", "9"]

    if z[0] in northeast:
        return 1.15
    if z[0] in south:
        return 0.95
    if z[0] in midwest:
        return 1.00
    if z[0] in west:
        return 1.20
    return 1.0


# ------------------------------------------------------------
# Age → Benchmark Premium Multiplier
# ------------------------------------------------------------
def age_factor(age):
    if age < 21:
        return 0.85
    if 21 <= age <= 27:
        return 1.00
    if 28 <= age <= 36:
        return 1.16
    if 37 <= age <= 45:
        return 1.36
    if 46 <= age <= 50:
        return 1.58
    if 51 <= age <= 55:
        return 1.78
    return 2.00


# ------------------------------------------------------------
# ACA Expected Contribution Percentage (2024)
# ------------------------------------------------------------
def expected_contribution_ratio(fpl_ratio):
    if fpl_ratio < 1.0:
        return 0.0
    if 1.0 <= fpl_ratio < 1.5:
        return 0.02
    if 1.5 <= fpl_ratio < 2.0:
        return 0.04
    if 2.0 <= fpl_ratio < 2.5:
        return 0.06
    if 2.5 <= fpl_ratio < 3.0:
        return 0.085
    if 3.0 <= fpl_ratio <= 4.0:
        return 0.085
    return 0.085


# ------------------------------------------------------------
# CSR Level
# ------------------------------------------------------------
def csr_level(fpl_ratio):
    if fpl_ratio <= 1.5:
        return "CSR 94"
    if fpl_ratio <= 2.0:
        return "CSR 87"
    if fpl_ratio <= 2.5:
        return "CSR 73"
    return "None"


# ------------------------------------------------------------
# Employer Insurance Expected Annual Cost
# ------------------------------------------------------------
def employer_cost(plan_type, employer_share, visits, specialist_visits, meds):
    # average numbers
    if plan_type == "PPO":
        premium = 7500
        ded = 1500
        coins = 0.20
    elif plan_type == "HMO":
        premium = 6500
        ded = 1000
        coins = 0.20
    elif plan_type == "EPO":
        premium = 7000
        ded = 1200
        coins = 0.20
    else:  # HDHP
        premium = 5000
        ded = 3500
        coins = 0.0

    employee_premium = premium * (1 - employer_share / 100)

    expected_oop = ded + visits * 40 + specialist_visits * 60 + meds * 15

    return employee_premium + expected_oop


# ------------------------------------------------------------
# Marketplace Annual Cost
# ------------------------------------------------------------
def marketplace_cost(age, zip_code, income, household_size, visits, specialist_visits, meds):
    fpl = get_fpl(household_size)
    ratio = income / fpl

    benchmark_silver = 5000 * age_factor(age) * zip_factor(zip_code)

    expected_contrib = expected_contribution_ratio(ratio) * income
    subsidy = max(0, benchmark_silver - expected_contrib)

    actual_premium = benchmark_silver - subsidy

    ded = 4500
    oop_cost = ded + visits * 40 + specialist_visits * 60 + meds * 20

    total = actual_premium + oop_cost

    return total, subsidy, csr_level(ratio), actual_premium


# ------------------------------------------------------------
# Final Comparison Logic
# ------------------------------------------------------------
def recommend_plan(market_cost, employer_cost_val, csr):
    if market_cost < employer_cost_val:
        return f"Marketplace Plan ({csr})", market_cost
    else:
        return "Employer Plan", employer_cost_val


# ------------------------------------------------------------
# UI — Multi-step Wizard
# ------------------------------------------------------------
def show_plan_wizard():
    st.title("Insurance Plan Wizard")

    st.write("A 4-step guided tool to recommend the best insurance plan for your profile.")

    step = st.session_state.get("wizard_step", 1)

    # --------------------------------------------------------
    # STEP 1 — Personal Info
    # --------------------------------------------------------
    if step == 1:
        st.subheader("Step 1 — Personal Details")

        age = st.number_input("Age", 18, 64, 30)
        zip_code = st.text_input("ZIP Code (optional)", "")
        household_size = st.number_input("Household Size", 1, 10, 1)
        income = st.number_input("Household Income ($)", 0, 500000, 45000)
        employment = st.selectbox("Employment Status", ["Employed", "Self-employed", "Unemployed"])
        employer_contrib = 0

        if employment == "Employed":
            employer_contrib = st.slider("Employer Premium Contribution (%)", 0, 100, 70)

        if st.button("Next"):
            st.session_state.age = age
            st.session_state.zip_code = zip_code
            st.session_state.household_size = household_size
            st.session_state.income = income
            st.session_state.employed = employment == "Employed"
            st.session_state.employer_contrib = employer_contrib
            st.session_state.wizard_step = 2
            st.experimental_rerun()

    # --------------------------------------------------------
    # STEP 2 — Usage
    # --------------------------------------------------------
    if step == 2:
        st.subheader("Step 2 — Healthcare Usage")

        visits = st.slider("Primary Care Visits per Year", 0, 20, 2)
        specialist = st.slider("Specialist Visits per Year", 0, 20, 1)
        meds = st.slider("Monthly Medications", 0, 10, 1)

        if st.button("Next"):
            st.session_state.visits = visits
            st.session_state.specialist = specialist
            st.session_state.meds = meds
            st.session_state.wizard_step = 3
            st.experimental_rerun()

        if st.button("Back"):
            st.session_state.wizard_step = 1
            st.experimental_rerun()

    # --------------------------------------------------------
    # STEP 3 — Employer Plan
    # --------------------------------------------------------
    if step == 3:
        st.subheader("Step 3 — Employer Plan Environment")

        if st.session_state.employed:
            plan_type = st.selectbox("Employer Plan Type", ["PPO", "HMO", "EPO", "HDHP"])
        else:
            st.info("Skipping employer plan — you are not currently employed.")
            plan_type = None

        if st.button("Next"):
            st.session_state.plan_type = plan_type
            st.session_state.wizard_step = 4
            st.experimental_rerun()

        if st.button("Back"):
            st.session_state.wizard_step = 2
            st.experimental_rerun()

    # --------------------------------------------------------
    # STEP 4 — Results
    # --------------------------------------------------------
    if step == 4:
        st.subheader("Step 4 — Final Recommendation")

        age = st.session_state.age
        zip_code = st.session_state.zip_code
        household_size = st.session_state.household_size
        income = st.session_state.income

        visits = st.session_state.visits
        specialist = st.session_state.specialist
        meds = st.session_state.meds

        employer_contrib = st.session_state.employer_contrib
        plan_type = st.session_state.plan_type

        market_cost, subsidy, csr, mpremium = marketplace_cost(
            age, zip_code, income, household_size, visits, specialist, meds
        )

        if st.session_state.employed:
            emp_cost = employer_cost(plan_type, employer_contrib, visits, specialist, meds)
        else:
            emp_cost = float("inf")

        best_plan, best_cost = recommend_plan(market_cost, emp_cost, csr)

        st.markdown("### Recommended Plan")
        st.write(best_plan)
        st.markdown("### Estimated Annual Cost")
        st.write(f"${best_cost:,.2f}")

        st.markdown("### Cost Breakdown")
        st.write(f"Marketplace Annual Cost: ${market_cost:,.2f}")
        st.write(f"Employer Annual Cost: ${emp_cost:,.2f if emp_cost != float('inf') else 'Not Applicable'}")
        st.write(f"Subsidy Estimate (ACA): ${subsidy:,.2f}")

        if st.button("Start Over"):
            st.session_state.wizard_step = 1
            st.experimental_rerun()
