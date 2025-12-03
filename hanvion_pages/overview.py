import streamlit as st

def show_overview():

    # =====================================================
    # Page Title & Intro
    # =====================================================
    st.markdown(
        """
        <h1 style='color:#0D3B66; font-weight:800; margin-bottom:4px;'>Welcome to Hanvion Health</h1>
        <p style='color:#333; font-size:18px; margin-top:0px;'>
            Your gateway to understanding U.S. health insurance, costs, and plan selection.
        </p>
        <hr style='margin-top:18px; margin-bottom:28px; border:1px solid #E1E5EB;'>
        """,
        unsafe_allow_html=True
    )

    # YOU CAN ADD YOUR OVERVIEW TEXT HERE
    st.write(
        """
        The Hanvion platform provides tools to help you understand insurance,
        compare plans, estimate costs, and decode your insurance cards using AI.
        """
    )

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
        "explanation": "ER visits have cost-sharing—preventive care is fully covered only for routine services."
    }
]

user_answers = []

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
        key=f"overview_quiz_{index}"   # FIXED KEY
    )
    user_answers.append(user_choice)

if st.button("Show Results", key="overview_show_results"):
    score = 0

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(
        "<div style='font-size:24px; font-weight:700; color:#0D3B66;'>Your Quiz Results</div>",
        unsafe_allow_html=True,
    )

    for i, q in enumerate(quiz_questions):
        correct = q["options"][q["answer"]]
        user = user_answers[i]

        if user == correct:
            score += 1
            st.success(f"Correct! ✔ {q['explanation']}")
        else:
            st.error(f"Incorrect ❌ — {q['explanation']}")

        st.markdown("---")

    progress = score / len(quiz_questions)
    st.subheader(f"Final Score: {score} / {len(quiz_questions)}")
    st.progress(progress)

    st.button("Retry Quiz", key="overview_retry")
