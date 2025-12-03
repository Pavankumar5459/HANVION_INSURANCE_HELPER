import streamlit as st

def show_glossary():
    st.markdown("## Insurance Glossary")

    st.markdown(
        """
        Below are the most important U.S. insurance terms explained in clear,
        simple language.
        """
    )

    glossary_items = {
        "Premium": "The amount you pay every month for your health insurance plan.",
        "Deductible": "The amount you must pay for your care before your insurance starts sharing costs.",
        "Coinsurance": "The percentage of the bill you pay after meeting your deductible.",
        "Copay": "A fixed dollar amount you pay for services like doctor visits or prescriptions.",
        "Out-of-Pocket Maximum": "The most you will pay in one year. After this, insurance pays 100%.",
        "Allowed Amount": "The maximum amount an insurance company considers a service should cost.",
        "EOB (Explanation of Benefits)": "A statement showing what was billed, what insurance paid, and what you owe.",
        "Network": "Doctors, hospitals, and facilities contracted with your insurance plan.",
        "Prior Authorization": "Approval required from insurance before certain services or medications.",
        "Formulary": "A list of medications covered by your insurance plan.",
        "Subsidy (ACA Marketplace Credit)": "Financial help from the government to reduce premiums.",
        "CSR (Cost Sharing Reductions)": "Extra financial help for low-income individuals on Silver plans.",
        "Preventive Care": "Routine checkups, vaccines, and screenings covered at $0 cost under most plans."
    }

    for term, definition in glossary_items.items():
        with st.expander(term):
            st.write(definition)
