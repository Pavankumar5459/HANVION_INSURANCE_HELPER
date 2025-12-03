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
