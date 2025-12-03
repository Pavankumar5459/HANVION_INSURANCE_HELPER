import streamlit as st
import requests
import os

PPLX_KEY = os.getenv("PPLX_API_KEY")

def extract_answer(data):
    """Universal parser for ALL Perplexity response formats."""

    # 1) Standard completion format → choices
    if isinstance(data, dict):
        if "choices" in data:
            try:
                return data["choices"][0]["message"]["content"]
            except:
                pass

        # 2) Some models return → output_text
        if "output_text" in data:
            return data["output_text"]

        # 3) Sometimes wrapped inside `data`
        if "data" in data and isinstance(data["data"], dict):
            inner = data["data"]
            if "output_text" in inner:
                return inner["output_text"]
            if "text" in inner:
                return inner["text"]

        # 4) Some responses put text in plain "text"
        if "text" in data:
            return data["text"]

        # 5) API error message
        if "error" in data:
            return f"API Error: {data['error']}"

    # 6) If everything fails → show raw data
    return f"Unexpected API response: {data}"


def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    if not PPLX_KEY:
        st.error("Perplexity API key is missing. Add it in Streamlit Secrets.")
        return

    # Chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display old messages
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    # Input box
    user_input = st.text_input("Ask a question:")

    if st.button("Send") and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Build request
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
            ]
        }

        # Send request
        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()

            # Extract answer (handles all formats)
            answer = extract_answer(data)

        except Exception as e:
            answer = f"Error contacting Perplexity: {e}"

        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.success("Response received. Scroll up to read it.")

    # Clear chat
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_set_query_params()
        st.success("Chat cleared.")
