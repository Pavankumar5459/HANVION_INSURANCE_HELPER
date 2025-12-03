import streamlit as st

def show_overview():

    # ---------------------------------------------------
    # HEADER
    # ---------------------------------------------------
    st.title("Welcome to Hanvion Health")
    st.write(
        "Your gateway to understanding U.S. health insurance, costs, and plan selection."
    )

    st.markdown("""<hr style='margin-top:20px;'>""", unsafe_allow_html=True)

    st.write(
        "The Hanvion platform provides tools to help you understand insurance, "
        "compare plans, estimate costs, and decode your insurance cards using AI."
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------------------------------------------------
    # MAIN CONTENT (BEFORE QUIZ)
    # ---------------------------------------------------

    st.subheader("Why Learn Health Insurance Basics?")
    st.write(
        """
        Understanding insurance fundamentals helps you avoid major financial risks,
        choose the right plan, and ensure your family gets proper coverage.
        """
    )

    st.markdown("<hr style='margin-top:30px;'>", unsafe_allow_html=True)

    # ---------------------------------------------------
    # INSURANCE QUIZ TITLE
    # ---------------------------------------------------
    st.markdown(
        """
        <div style='font-size:28px; font-weight:800; color:#0D3B66; margin-top:35px;'>
            📝 Insurance Knowledge Quiz
        </div>
        <p style='font-size:16px; color:#444; margin-bottom:20px;'>
            Test your understanding of essential U.S. health insurance terms.
        </p>
        """,
        unsafe_allow_html=True,
    )

    # ---------------------------------------------------
    # QUIZ QUESTIONS
    # ---------------------------------------------------
    quiz_questions = [
        {
            "question": "What is a deductible?",
            "options": [
                "A fixed amount you pay for each doctor visit",
                "The amount you pay before insurance starts covering costs",
                "The most insurance will pay in a single year"
            ],
            "answer": 1,
            "explanation": "A deductible is the amount you must pay out of pocket before insurance begins covering costs."
        },
        {
            "question": "What happens after you reach your out-of-pocket maximum?",
            "options": [
                "Insurance pays 100% of covered medical costs for the rest of the year",
                "Your plan resets immediately",
                "Premiums increase automatically"
            ],
            "answer": 0,
            "explanation": "After reaching the OOP max, insurance covers 100% of covered care."
        },
        {
            "question": "Which service is NOT considered preventive care?",
            "options": [
                "Vaccinations",
                "Annual wellness visit",
                "Emergency room visit"
            ],
            "answer": 2,
            "explanation": "Emergency room visits involve cost-sharing and are not part of preventive care."
        },
    ]

    user_answers = []

    # ---------------------------------------------------
    # DISPLAY QUESTIONS
    # ---------------------------------------------------
    for i, q in enumerate(quiz_questions):

        st.markdown(
            f"""
            <div style='
                background:#F6FAFF; 
                border:1px solid #D6E4F2;
                padding:18px;
                border-radius:12px;
                margin-bottom:18px;
            '>
                <div style='font-size:18px; font-weight:700; color:#0D3B66; margin-bottom:10px;'>
                    Q{i+1}. {q["question"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # IMPORTANT — UNIQUE KEYS
        answer = st.radio(
            "Choose one:",
            q["options"],
            key=f"overview_quiz_q{i}"
        )

        user_answers.append(answer)

    # ---------------------------------------------------
    # RESULTS BUTTON
    # ---------------------------------------------------
    if st.button("Show Results", key="overview_quiz_results"):

        score = 0
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Your Quiz Results")

        for idx, q in enumerate(quiz_questions):
            correct = q["options"][q["answer"]]
            user = user_answers[idx]

            if user == correct:
                score += 1
                st.success(f"Correct! ✔ {q['explanation']}")
            else:
                st.error(f"Incorrect ❌ — {q['explanation']}")

        progress = score / len(quiz_questions)
        st.subheader(f"Final Score: {score} / {len(quiz_questions)}")
        st.progress(progress)

    st.markdown("<br><br>", unsafe_allow_html=True)
