import streamlit as st

def show_insurance_hub():
    st.title("Insurance Education Hub")
    st.write(
        "Learn the most important U.S. health insurance terms and the essential 12-point checklist "
        "that everyone should understand before choosing a plan."
    )

    st.markdown("---")
    st.header("Core U.S. Insurance Terms")

    glossary_items = {
        "Premium": 
        "The amount you pay every month to keep your insurance active. It does not count toward your deductible. "
        "Higher premiums usually mean lower out-of-pocket costs when you receive care.",

        "Deductible":
        "The amount you must pay out of pocket each year before your insurance starts paying. "
        "For example, if your deductible is $2,000, you must spend $2,000 first before most covered services begin "
        "receiving insurance payment.",

        "Coinsurance":
        "The percentage of costs you pay after you meet your deductible. "
        "For example, if your coinsurance is 20%, insurance pays 80% and you pay 20% for covered services.",

        "Copay":
        "A fixed dollar amount you pay for certain services, such as $25 for a primary care visit. "
        "Copays often apply even before the deductible is met depending on the plan.",

        "Out-of-Pocket Maximum":
        "The maximum amount you will pay in a year for covered services. "
        "Once you reach this limit, insurance pays 100% of covered costs for the rest of the year. "
        "This is one of the most important protection features of health insurance.",

        "Allowed Amount":
        "The maximum amount an insurance company deems reasonable for a service. "
        "If a provider charges more than the allowed amount and is out-of-network, "
        "you may be billed for the difference.",

        "Explanation of Benefits (EOB)":
        "A document the insurer sends after a medical service. It explains what was billed, "
        "what the insurer paid, what discounts were applied, and what you owe. "
        "It is not a bill.",

        "Network":
        "A group of hospitals, doctors, and facilities contracted with the insurance plan. "
        "In-network care costs significantly less. Out-of-network providers can lead to very high bills.",

        "Prior Authorization":
        "A requirement where the insurance company must approve a procedure or medication before it is given. "
        "If skipped, the insurer may refuse payment.",

        "Formulary":
        "The official list of drugs covered by an insurance plan. Drugs are grouped into 'tiers' which determine copay/"
        "coinsurance. Higher tiers often cost more.",

        "Subsidy (ACA Marketplace Credit)":
        "A financial discount provided by the government to lower your monthly premium based on income. "
        "Millions of Americans qualify for subsidies and unknowingly overpay for insurance.",

        "Cost Sharing Reductions (CSR)":
        "Special discounts that lower deductibles, copays, and out-of-pocket maximums for qualifying individuals "
        "on Silver Marketplace plans. One of the strongest benefits available for low-to-moderate income groups.",

        "Preventive Care":
        "Certain screenings, vaccinations, and annual checkups covered at 100% without deductible or copays "
        "under federal law, as long as the provider is in-network.",

        "Out-of-Network Billing":
        "When you visit a provider or hospital outside your plan’s network, costs can be much higher. "
        "Some plans do not cover out-of-network services at all, except emergencies.",
    }

    # Render glossary items
    for title, desc in glossary_items.items():
        with st.expander(title):
            st.markdown(f"""
            <div style='background-color:#ffffff; padding:15px; border:1px solid #ddd; border-radius:6px;'>
                {desc}
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")
    st.header("12-Point Smart Insurance Checklist")

    checklist = {
        "1. Identify Your Real Need":
        "Before choosing a plan, assess your family size, ages, medical history, location, and financial stability. "
        "Health needs differ across households, so understanding your own situation is the first step.",

        "2. Do Not Choose Only Based on Premium":
        "Low premium does not mean good coverage. Plans with very low premiums usually have high deductibles, "
        "high out-of-pocket costs, and limited coverage. Focus on total yearly cost.",

        "3. Check Claim Settlement Strength":
        "Instead of only checking the Claim Settlement Ratio, check the average claim amount paid and consistency. "
        "A company that settles many claims but pays only small amounts may not be reliable in real emergencies.",

        "4. Understand Exclusions Clearly":
        "Every policy covers many things — but the exclusions are what cause financial shocks. "
        "Always ask: 'What is NOT covered?' Know this before signing.",

        "5. Avoid Being Forced Into a Policy by Agents":
        "Agents may promote plans with higher commissions. Always compare multiple policies before selecting one. "
        "Never buy the first option you hear.",

        "6. Review Network Hospitals in Your Area":
        "Emergency situations require quick access. Check if nearby hospitals accept your insurance. "
        "This is one of the most practical, real-world checks.",

        "7. Prioritize Long-Term Benefits Over Short-Term Discounts":
        "Temporary offers like 'no-claim bonus' or small cashback should not influence your long-term protection. "
        "Coverage quality matters more.",

        "8. Consider Breadwinner Protection (Term Insurance)":
        "If one person is the only earner, a strong term insurance plan is essential. "
        "Coverage should be at least 10× the annual income after adjusting for inflation.",

        "9. Higher Coverage for Parents or Elderly Members":
        "Older members have higher chances of hospitalization. Plans with 15–20 lakh coverage or more "
        "are suitable to avoid large unexpected expenses.",

        "10. Verify Documentation Carefully":
        "Name, date of birth, ID proofs, KYC, and medical history must be accurate. "
        "Errors can lead to claim rejection later.",

        "11. Check Genuine Customer Feedback":
        "Not all insurers with high claim ratios offer good service. Look at real reviews "
        "about customer support, cashless approval speed, and claim settlement experience.",

        "12. Add Important Riders and Add-Ons":
        "Technology-based add-ons like robotic surgery cover, critical illness riders, maternity cover, "
        "and room-rent waiver can save massive expenses in the future.",
    }

    # Render checklist
    for title, desc in checklist.items():
        with st.expander(title):
            st.markdown(f"""
            <div style='background-color:#ffffff; padding:15px; border:1px solid #ddd; border-radius:6px;'>
                {desc}
            </div>
            """, unsafe_allow_html=True)
