import streamlit as st

def show_insurance_hub():

    # =====================================================
    # PAGE HEADER
    # =====================================================
    st.markdown(
        """
        <h1 style='color:#0D3B66; font-weight:800; margin-bottom:0px;'>Insurance Education Hub</h1>
        <p style='color:#333; font-size:18px; margin-top:4px;'>
            Learn essential health insurance concepts and follow a smart 12-point checklist before choosing a plan.
        </p>
        <hr style='margin-top:18px; margin-bottom:28px; border:1px solid #E1E5EB;'>
        """,
        unsafe_allow_html=True,
    )

    # =====================================================
    # TEMPLATE FUNCTIONS
    # =====================================================
    def section_title(text):
        st.markdown(
            f"""
            <div style='font-size:22px; font-weight:700; color:#0D3B66; margin-top:10px; margin-bottom:10px;'>
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    def card(text):
        st.markdown(
            f"""
            <div style="
                background:#F7FAFC;
                padding:16px 18px;
                border-radius:10px;
                border:1px solid #DFE6EE;
                font-size:16px;
                color:#333;
                line-height:1.55;
                margin-bottom:10px;
            ">
                {text}
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # MAIN TWO-COLUMN LAYOUT
    # =====================================================
    col1, col2 = st.columns([1, 1.2])

    # =====================================================
    # LEFT COLUMN — CORE TERMS
    # =====================================================
    with col1:
        section_title("Core U.S. Insurance Terms")

        terms = {
            "Premium":
                "The fixed monthly amount you pay to keep your insurance active.",

            "Deductible":
                "The amount you pay each year before insurance starts covering costs.",

            "Coinsurance":
                "The percentage you pay after meeting the deductible (e.g., 20%).",

            "Copay":
                "A fixed fee for specific services (e.g., $30 doctor visit).",

            "Out-of-Pocket Maximum":
                "The maximum amount you pay in a year before insurance covers 100% of covered care.",

            "Allowed Amount":
                "The maximum charge an insurer will pay for a service.",

            "Explanation of Benefits (EOB)":
                "A breakdown of what insurance paid and what you owe for a claim.",

            "Network":
                "Hospitals and doctors contracted with your insurance.",

            "Prior Authorization":
                "Approval required before certain procedures or medications.",

            "Formulary":
                "List of medications covered by the plan, divided into tiers.",

            "Subsidy":
                "Discounts from the government that reduce your premium (ACA Marketplace).",

            "CSR (Cost-Sharing Reductions)":
                "Lower deductibles/copays for eligible income groups.",

            "Preventive Care":
                "Fully covered services such as annual checkups and vaccines.",
        }

        for title, desc in terms.items():
            with st.expander(f"{title}", expanded=False):
                card(desc)

    # =====================================================
    # RIGHT COLUMN — 12-POINT CHECKLIST
    # =====================================================
    with col2:
        section_title("12-Point Smart Insurance Buyer Checklist")

        checklist = {
            "1. Identify Your Needs":
                "Family size, medical history, income, emergency funds, and coverage expectations.",

            "2. Don’t Choose Based Only on Premium":
                "Low premiums often mean high deductibles.",

            "3. Check Claim Settlement Quality":
                "Many insurers settle claims, but the percentage paid matters more.",

            "4. Read Exclusions Carefully":
                "Always ask what is NOT covered — this prevents surprises.",

            "5. Beware of Agent Bias":
                "Agents push high-commission plans. Always compare plans yourself.",

            "6. Check Network Hospitals Near You":
                "More hospitals = better emergency coverage.",

            "7. Choose Long-Term Benefits":
                "Ignore flashy short-term discounts.",

            "8. Adequate Term Coverage":
                "Income × 10 is a safe rule. Adjust for inflation.",

            "9. Senior Coverage for Parents":
                "Older adults need higher limits and good cashless options.",

            "10. Check Documentation Accuracy":
                "Incorrect DOB or KYC can cause claim rejection.",

            "11. Evaluate Real Customer Feedback":
                "Judge based on claim delays and service quality.",

            "12. Add-Ons Matter":
                "Tech-based surgeries (robotic), room rent waivers, etc. must be included.",
        }

        for title, desc in checklist.items():
            with st.expander(f"{title}", expanded=False):
                card(desc)
# =====================================================
# PREMIUM QUIZ UI — Modern Interactive Design
# =====================================================

st.markdown("<hr style='margin-top:40px;'>", unsafe_allow_html=True)

st.markdown(
    """
    <div style='font-size:26px; font-weight:800; color:#0D3B66; margin-bottom:6px;'>
        Insurance Knowledge Quiz
    </div>
    <p style='font-size:16px; color:#444; margin-bottom:20px;'>
        Test your understanding of key U.S. health insurance concepts.
    </p>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Quiz Questions
# -----------------------------
quiz_questions = [
    {
        "question": "What is a deductible?",
        "options": [
            "A fixed amount you pay for every doctor visit",
            "The amount you pay before insurance begins covering costs",
            "The most your insurance will pay in a year"
        ],
        "answer": 1,
        "explanation": "A deductible is the amount you pay before insurance coverage starts."
    },
    {
        "question": "What happens after you reach your out-of-pocket maximum?",
        "options": [
            "Insurance covers 100% of covered services for the rest of the year",
            "Your plan resets immediately",
            "Preventive care becomes paid"
        ],
        "answer": 0,
        "explanation": "When you hit OOP max, insurance pays 100% of covered costs."
    },
    {
        "question": "Which is typically NOT fully covered under preventive care?",
        "options": [
            "Annual wellness visit",
            "Vaccinations",
            "Emergency room visit"
        ],
        "answer": 2,
        "explanation": "ER visits are not preventive care and have cost-sharing."
    }
]

# -----------------------------
# Answer Storage
# -----------------------------
user_answers = []

st.markdown("<div style='margin-bottom:10px;'></div>", unsafe_allow_html=True)

for index, q in enumerate(quiz_questions):
    st.markdown(
        f"""
        <div style='
            background:#F6FAFF; 
            border:1px solid #D6E4F2;
            padding:18px;
            border-radius:12px;
            margin-bottom:18px;
            box-shadow:0px 1px 3px rgba(0,0,0,0.05);
        '>
            <div style='font-size:18px; font-weight:700; color:#0D3B66; margin-bottom:10px;'>
                Q{index + 1}. {q['question']}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    user_choice = st.radio(
        "Choose one:",
        q["options"],
        key=f"quiz_{index}"
    )
    user_answers.append(user_choice)


# -----------------------------
# Show Results Button
# -----------------------------
if st.button("Show Results"):
    score = 0

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:24px; font-weight:700; color:#0D3B66;'>Your Quiz Results</div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='margin-bottom:14px;'></div>", unsafe_allow_html=True)

    for i, q in enumerate(quiz_questions):
        correct = q["options"][q["answer"]]
        user = user_answers[i]

        # Result Card
        if user == correct:
            score += 1
            st.success(f"Correct! ✔ {q['explanation']}")
        else:
            st.error(f"Incorrect ❌ — {q['explanation']}")

        st.markdown("---")

    # -----------------------------
    # Score Bar
    # -----------------------------
    st.markdown(
        f"""
        <div style='font-size:20px; font-weight:700; color:#0D3B66; margin-bottom:10px;'>
            Final Score: {score} / {len(quiz_questions)}
        </div>
        """,
        unsafe_allow_html=True,
    )

    progress = score / len(quiz_questions)
    st.progress(progress)

    # Badge
    if score == len(quiz_questions):
        st.success("Excellent! You mastered the fundamentals.")
    elif score >= len(quiz_questions) * 0.6:
        st.info("Good job! You understand most concepts.")
    else:
        st.warning("Keep practicing! Review the terms and try again.")

    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    st.button("Retry Quiz")
