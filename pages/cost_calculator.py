import streamlit as st


def calculate_cost(allowed_amount, deductible, deductible_met, copay, coinsurance, oop_max, oop_spent):
    """Core insurance cost-sharing calculation."""

    # Remaining ded / oop
    ded_remaining = max(0, deductible - deductible_met)
    oop_remaining = max(0, oop_max - oop_spent)

    # If OOP max already reached
    if oop_remaining <= 0:
        return 0, allowed_amount, ded_remaining, 0  # you pay 0, insurance pays all

    # SCENARIO 1 — Entire allowed amount falls within deductible
    if allowed_amount <= ded_remaining:
        you_pay = allowed_amount
        insurance_pays = 0
        return min(you_pay, oop_remaining), insurance_pays, ded_remaining - allowed_amount, oop_remaining - you_pay

    # SCENARIO 2 — Part goes to deductible, remaining is coinsurance
    amount_after_ded = allowed_amount - ded_remaining

    coins_part = amount_after_ded * (coinsurance / 100)
    ins_part = amount_after_ded - coins_part

    you_pay = ded_remaining + coins_part + copay
    insurance_pays = ins_part

    # Apply OOP max
    if you_pay >= oop_remaining:
        you_pay = oop_remaining
        insurance_pays = allowed_amount - you_pay

    return you_pay, insurance_pays, 0, oop_remaining - you_pay



def show_cost_calculator():

    st.title("Cost Calculator")

    st.write(
        "Estimate your out-of-pocket cost for a medical service based on your plan’s deductible, "
        "copay, coinsurance, and out-of-pocket maximum."
    )

    st.subheader("Service Details")

    allowed = st.number_input("Allowed Amount ($)", 0, 50000, 500)
    copay = st.number_input("Copay ($)", 0, 500, 30)
    coins = st.number_input("Coinsurance (%)", 0, 100, 20)

    st.subheader("Your Plan Details")

    deductible = st.number_input("Annual Deductible ($)", 0, 20000, 2000)
    ded_met = st.number_input("Deductible Met So Far ($)", 0, deductible, 0)

    oop_max = st.number_input("Out-of-Pocket Maximum ($)", 0, 30000, 8000)
    oop_spent = st.number_input("OOP Spent So Far ($)", 0, oop_max, 0)

    if st.button("Calculate Cost"):
        you_pay, ins_pay, ded_remain, oop_remain = calculate_cost(
            allowed, deductible, ded_met, copay, coins, oop_max, oop_spent
        )

        st.subheader("Your Cost Summary")

        st.write(f"**You Pay:** ${you_pay:,.2f}")
        st.write(f"**Insurance Pays:** ${ins_pay:,.2f}")

        st.subheader("Remaining Balance")
        st.write(f"Remaining Deductible: ${ded_remain:,.2f}")
        st.write(f"Remaining OOP Max: ${oop_remain:,.2f}")


