import streamlit as st
import requests
import os

# Load Perplexity API key
PPLX_KEY = os.getenv("PPLX_API_KEY")

# -----------------------------
# UNIVERSAL RESPONSE PARSER
# -----------------------------
def extract_answer(data):
    if isinstance(data, dict):
        # Standard chat format
        if "choices" in data:
            try:
                return data["choices"][0]["message"]["content"]
            except:
                pass

        # Some models return "output_text"
        if "output_text" in data:
            return data["output_text"]

        # Some return simple "text"
        if "text" in data:
            return data["text"]

        # Nested data section
        if "data" in data and isinstance(data["data"], dict):
            nested = data["data"]
            if "output_text" in nested:
                return nested["output_text"]
            if "text" in nested:
                return nested["text"]

        # API error
        if "error" in data:
            return f"API Error: {data['error']}"

    return f"Unexpected API response: {data}"


# -----------------------------
# MAIN PAGE FUNCTION
# -----------------------------
def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    if not PPLX_KEY:
        st.error("Perplexity API key is missing. Add it in Streamlit Secrets.")
        return

    # Chat memory
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show previous msgs
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    # User input
    user_input = st.text_input("Ask a question:")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {PPLX_KEY}",
            "Content-Type": "application/json"
        }

        # ⭐ WORKING MODEL ⭐
        payload = {
            "model": "sonar-small-chat",
            "messages": [
                {"role": "system", "content": "You are a helpful insurance assistant."},
                {"role": "user", "content": user_input},
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

    # Clear chat
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.success("Chat cleared.")
