import streamlit as st

def evaluate_plan(age, income, family, health_conditions, medications, hospital_visits, prefer_low_premium):
    """Core logic: decides plan tier + checklist flags."""

    # ---- Risk Tier ----
    risk = "Low"
    if age > 50 or len(health_conditions) > 0 or hospital_visits > 1:
        risk = "Moderate"
    if age > 60 or "cancer" in health_conditions or "diabetes" in health_conditions:
        risk = "High"

    # ---- Income Category ----
    if income < 30000:
        income_level = "Low Income"
    elif income < 70000:
        income_level = "Middle Income"
    else:
        income_level = "High Income"

    # ---- Plan Recommendation ----
    if income < 35000 and risk == "Low":
        plan = "Silver (with Cost Sharing Reductions)"
    elif risk == "Low":
        plan = "Bronze"
    elif risk == "Moderate":
        plan = "Silver"
    elif risk == "High":
        plan = "Gold"
    else:
        plan = "Silver"

    # ---- Checklist Flags ----
    flags = []

    # Checkpoint #2: low premium bias
    if prefer_low_premium:
        flags.append("Checkpoint #2: Choosing based only on premium increases deductible/out-of-pocket risk.")

    # Checkpoint #6: network
    flags.append("Checkpoint #6: Verify local network hospitals before finalizing this plan.")

    # Checkpoint #8: breadwinner protection
    if family > 1 and income > 0:
        flags.append("Checkpoint #8: Since others depend on your income, consider term insurance coverage.")

    # Checkpoint #9: elderly risk
    if age > 55:
        flags.append("Checkpoint #9: Age above 55 — ensure your health plan provides 15–20 lakh (or $20k–$30k) coverage.")

    # Checkpoint #12: add-ons
    if "surgery" in health_conditions or risk == "High":
        flags.append("Checkpoint #12: Add important riders (e.g., critical illness, robotic surgery cover).")

    return plan, risk, income_level, flags


def show_plan_wizard():
    st.title("Insurance Plan Wizard")
    st.write("Answer a few questions and get a personalized insurance recommendation based on your profile.")

    st.markdown("---")
    st.header("Basic Details")

    age = st.number_input("Your Age", min_value=1, max_value=99)
    income = st.number_input("Household Annual Income ($)", min_value=0)
    family = st.number_input("Total Number of Family Members (including you)", min_value=1)

    st.markdown("---")
    st.header("Health and Usage")

    health_conditions = st.multiselect(
        "Select any existing health conditions",
        ["none", "diabetes", "hypertension", "asthma", "heart disease", "cancer", "pregnancy", "surgery needed"]
    )

    medications = st.number_input("Number of long-term medications you take", min_value=0)
    hospital_visits = st.number_input("Expected Hospital Visits per Year", min_value=0, max_value=10)

    st.markdown("---")
    st.header("Preferences")

    prefer_low_premium = st.checkbox("I prefer the lowest monthly premium")

    if st.button("Get Recommendation"):
        plan, risk, income_level, flags = evaluate_plan(
            age, income, family, health_conditions, medications, hospital_visits, prefer_low_premium
        )

        st.markdown("---")
        st.subheader("Your Recommended Plan Tier")
        st.success(plan)

        st.subheader("Your Risk Profile")
        st.info(risk)

        st.subheader("Your Income Category")
        st.write(income_level)

        st.subheader("Important Notes (From 12-Point Checklist)")
        for f in flags:
            st.write(f"- {f}")

        st.markdown("---")
        st.subheader("Why This Plan Is Recommended")

        if plan.startswith("Silver") and income < 35000:
            st.write(
                "You may qualify for Cost Sharing Reductions (CSR). This lowers your deductible and out-of-pocket "
                "expenses significantly while keeping premiums affordable. Silver with CSR is usually the best choice "
                "for low-income but healthy individuals."
            )
        elif plan == "Bronze":
            st.write(
                "Since your risk profile is low and income allows for risk-sharing, a Bronze plan minimizes premiums "
                "while covering major emergencies. Ideal for individuals with few health conditions."
            )
        elif plan == "Silver":
            st.write(
                "Silver plans provide a strong balance between premiums and coverage, especially for moderate health "
                "service usage or families needing predictable costs."
            )
        elif plan == "Gold":
            st.write(
                "Gold plans offer low deductibles and strong coverage. Recommended for older individuals, people with "
                "chronic conditions, or those expecting higher healthcare usage."
            )
