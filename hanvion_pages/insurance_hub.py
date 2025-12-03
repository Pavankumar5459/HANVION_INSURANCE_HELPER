import streamlit as st

def show_insurance_hub():
    st.title("Insurance Education Hub")

    st.write(
        """
        Learn key U.S. health insurance concepts in simple language.
        Expand the topics below to view explanations.
        """
    )

    topics = {
        "Premium": 
            "The amount you pay every month for your health insurance plan.",

        "Deductible": 
            "The amount you must pay before your plan starts sharing costs.",

        "Copay": 
            "A fixed cost you pay for a specific service such as a doctor visit.",

        "Coinsurance": 
            "A percentage of the cost you pay after meeting your deductible.",

        "Out-of-Pocket Maximum": 
            "The most you will pay in a year. After this, your plan pays 100%.",

        "In-Network vs Out-of-Network": 
            "In-network doctors cost less. Out-of-network costs are higher.",

        "Prior Authorization": 
            "Insurance approval required for certain services or medications.",

        "Referrals": 
            "Some plans (like HMOs) require your primary doctor to approve specialist visits.",

        "Formulary": 
            "The list of medications your insurance covers.",

        "HMO vs PPO vs EPO vs HDHP": 
            "The main differences between popular plan types."
    }

    for title, body in topics.items():
        with st.expander(title):
            st.write(body)
