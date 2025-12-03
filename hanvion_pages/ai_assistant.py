import streamlit as st
import requests
import os

PPLX_KEY = os.getenv("PPLX_API_KEY")


def extract_answer(data):
    """Universal fallback parser."""
    if "choices" in data:
        try:
            return data["choices"][0]["message"]["content"]
        except:
            pass

    if "output_text" in data:
        return data["output_text"]

    if "text" in data:
        return data["text"]

    if "error" in data:
        return f"API Error: {data['error']}"

    return f"Unexpected API response: {data}"


def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    if not PPLX_KEY:
        st.error("Perplexity API key is missing.")
        return

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show history
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    user_input = st.text_input("Ask a question:")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {PPLX_KEY}",
            "Content-Type": "application/json"
        }

        # ⭐ The ONLY VALID MODELS for your key ⭐
        payload = {
            "model": "sonar-small",
            "messages": [
                {"role": "system", "content": "You are a helpful insurance assistant."},
                {"role": "user", "content": user_input}
            ]
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            answer = extract_answer(data)
        except Exception as e:
            answer = f"Error contacting Perplexity: {e}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.success("Response received. Scroll up to view it.")

    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.success("Chat cleared.")
