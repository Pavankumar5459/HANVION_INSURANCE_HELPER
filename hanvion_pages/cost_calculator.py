import streamlit as st
import pandas as pd

def aca_subsidy(income, household_size):
    # 2024 Federal Poverty Level
    fpl_table = {
        1: 14580, 2: 19720, 3: 24860, 4: 30000,
        5: 35140, 6: 40280, 7: 45420, 8: 50560
    }
    fpl = fpl_table.get(household_size, 30000)
    ratio = income / fpl

    # Max % of income a person pays (simplified)
    if ratio < 1.5:
        max_pct = 0.02
    elif ratio < 2:
        max_pct = 0.04
    elif ratio < 3:
        max_pct = 0.065
    elif ratio < 4:
        max_pct = 0.085
    else:
        max_pct = None  # no subsidy

    if max_pct is None:
        return 0

    expected_contribution = income * max_pct
    benchmark_plan_cost = 5400  # ACA national avg
    subsidy = max(0, benchmark_plan_cost - expected_contribution)
    return round(subsidy, 2)


def show_cost_calculator():
    st.title("Insurance Cost Calculator")
    st.write("Estimate premiums, deductibles, coinsurance, and total yearly cost.")

    st.header("1. Premium Calculator")
    col1, col2 = st.columns(2)

    with col1:
        premium = st.number_input("Monthly Premium ($)", min_value=0)

    with col2:
        yearly = premium * 12
        st.metric("Yearly Premium", f"${yearly:,.0f}")

    st.header("2. Deductible Calculator")
    col3, col4 = st.columns(2)

    with col3:
        deductible = st.number_input("Annual Deductible ($)", min_value=0)
        used = st.number_input("Amount already paid this year ($)", min_value=0)

    with col4:
        remaining = max(0, deductible - used)
        st.metric("Remaining Deductible", f"${remaining:,.0f}")

    st.header("3. Coinsurance Calculator")
    col5, col6 = st.columns(2)

    with col5:
        service_cost = st.number_input("Service Cost ($)", min_value=0)
        coins = st.number_input("Coinsurance (%)", min_value=0, max_value=100)

    with col6:
        you_pay = service_cost * (coins / 100)
        insurance_pays = service_cost - you_pay
        st.write(f"You Pay: **${you_pay:,.0f}**")
        st.write(f"Insurance Pays: **${insurance_pays:,.0f}**")

    st.header("4. ACA Marketplace Subsidy Estimator")

    income = st.number_input("Household Income ($)", min_value=0)
    hh_size = st.number_input("Household Size", min_value=1, max_value=10)

    if income > 0:
        subsidy = aca_subsidy(income, hh_size)
        st.success(f"Estimated Yearly Subsidy: **${subsidy:,.0f}**")

    st.header("5. Total Out-of-Pocket Simulator")

    hosp = st.number_input("Hospitalization Count", min_value=0)
    doc = st.number_input("Primary Care Visits", min_value=0)
    spec = st.number_input("Specialist Visits", min_value=0)
    er = st.number_input("ER Visits", min_value=0)

    avg_costs = {
        "hospitalization": 4800,
        "doc": 120,
        "spec": 240,
        "er": 1600
    }

    oop_total = (
        hosp * avg_costs["hospitalization"] +
        doc * avg_costs["doc"] +
        spec * avg_costs["spec"] +
        er * avg_costs["er"]
    )

    st.info(f"Estimated Medical Cost (before insurance): **${oop_total:,.0f}**")

