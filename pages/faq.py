import streamlit as st

def show_faq():
    st.markdown("## Frequently Asked Questions")

    faq_items = {
        "Do I need health insurance?":
        "Yes. Without insurance, emergency care or hospital bills can be extremely expensive.",

        "What is the difference between PPO, HMO, EPO, and HDHP?":
        "PPO: Most flexible network. HMO: Requires referrals. EPO: No out-of-network coverage. HDHP: High deductible, lower premium.",

        "Can I get insurance if I am not employed?":
        "Yes. You can apply through the ACA Marketplace and possibly qualify for subsidies.",

        "What if I am a student?":
        "Students may qualify for Marketplace plans, university plans, or remain on a parent’s plan until age 26.",

        "How do subsidies work?":
        "They lower your monthly premium based on household income and family size.",

        "What is Open Enrollment?":
        "A yearly window when anyone can sign up or change plans—usually November 1 to January 15.",

        "What if I miss Open Enrollment?":
        "You may still qualify through a Special Enrollment Period (move, job loss, marriage, etc.)."
    }

    for q, a in faq_items.items():
        with st.expander(q):
            st.write(a)
