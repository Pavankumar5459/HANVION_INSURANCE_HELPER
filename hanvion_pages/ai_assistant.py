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

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show chat history
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    # Input box
    user_input = st.text_input("Ask a question:")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

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
                {"role": "user", "content": user_input},
            ]
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            result = response.json()
            answer = result["choices"][0]["message"]["content"]
        except Exception as e:
            answer = f"Error: {e}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.experimental_rerun()
