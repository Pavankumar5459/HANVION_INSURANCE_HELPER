import streamlit as st
import openai
import os

def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    # Set API key (must be set in Streamlit Cloud secrets or environment variable)
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error("OpenAI API key is missing. Add it in your environment or secrets.")
        return

    client = openai.OpenAI(api_key=api_key)

    # Initialize session state for chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for msg in st.session_state.messages:
        st.write(f"**You:** {msg['user']}")
        st.write(f"**Assistant:** {msg['assistant']}")

    # User input
    query = st.text_input("Your question", "")

    if st.button("Ask"):
        if not query.strip():
            st.warning("Please enter a question.")
            return

        # System instructions for insurance expert
        system_prompt = (
            "You are an expert health insurance assistant. "
            "Explain things clearly, professionally, and with correct U.S. insurance terminology. "
            "Do not use emojis. "
            "Topics include: deductibles, copays, coinsurance, networks, Marketplace plans, "
            "Medicare, Medicaid, HDHP, PPO, HMO, EPO, OOP maximums, prior authorization, "
            "EOBs, allowed amounts, and CPT billing."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
            )

            answer = response.choices[0].message["content"]

            # Save to history
            st.session_state.messages.append(
                {"user": query, "assistant": answer}
            )

            # Display response
            st.write(f"**You:** {query}")
            st.write(f"**Assistant:** {answer}")

        except Exception as e:
            st.error(f"Error: {e}")

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.success("Conversation reset.")
