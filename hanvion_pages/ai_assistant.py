import streamlit as st
import requests
import os

# Load Perplexity API key
PPLX_KEY = os.getenv("PPLX_API_KEY")

def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    if not PPLX_KEY:
        st.error("Perplexity API key is missing. Add it in your Streamlit Secrets.")
        return

    # Chat history storage
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display prior messages
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    # User input
    user_input = st.text_input("Ask a question:")

    if st.button("Send") and user_input:
        # Save user message
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        # Perplexity API call
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {PPLX_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.1-8b-instruct",
            "messages": [
                {"role": "system", "content": "You are a helpful insurance assistant."},
                {"role": "user", "content": user_input}
            ],
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            answer = data["choices"][0]["message"]["content"]
        except Exception as e:
            answer = f"Error from Perplexity: {e}"

        # Append assistant response
        st.session_state.messages.append(
            {"role": "assistant", "content": answer}
        )

        # Instead of rerun, simply clear input via empty container
        st.success("Response received. Scroll up to view it.")

    # Button to clear chat
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_set_query_params()  # Safe page refresh
        st.success("Chat cleared.")
