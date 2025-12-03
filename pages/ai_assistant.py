import streamlit as st
import openai
import os

# -------------------------------------------------------
# Safe instruction wrapper for insurance-only AI
# -------------------------------------------------------
SYSTEM_PROMPT = """
You are Hanvion Health's Insurance Intelligence Assistant.
You explain insurance concepts clearly, professionally, and accurately.

Rules:
- Do not provide medical advice.
- Do not diagnose diseases.
- Keep all responses within health insurance, billing, financial assistance, ACA Marketplace regulations, employer plans, deductibles, copays, coinsurance, networks, prior authorization, and coverage rules.
- Be factual, concise, and neutral.
- No emojis.
- No emotional tone.
- Do not fabricate plan details.
- If unsure, ask the user for more information.
"""


def call_openai(user_input):
    """Safe wrapper for OpenAI API calls."""
    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
            max_tokens=500,
            temperature=0.2,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {e}. Please check your API key."


def show_ai_assistant():
    st.title("Hanvion Insurance Assistant")

    st.write(
        "This assistant helps explain insurance rules, bills, deductibles, coinsurance, "
        "plan types, Marketplace options, employer coverage, and related topics."
    )

    api_status = os.getenv("OPENAI_API_KEY")
    if not api_status:
        st.warning("API key not found. Please set the OPENAI_API_KEY environment variable.")

    user_input = st.text_area("Ask a question about health insurance:", height=150)

    if st.button("Get Answer"):
        if not user_input.strip():
            st.info("Please enter a question.")
            return

        with st.spinner("Generating explanation..."):
            answer = call_openai(user_input)

        st.subheader("Response")
        st.write(answer)
