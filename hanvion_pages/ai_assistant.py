import streamlit as st
import requests
import os

# Load Perplexity API key
PPLX_KEY = os.getenv("PPLX_API_KEY")


# --------------------------------------------------------
# UNIVERSAL RESPONSE PARSER — never fails
# --------------------------------------------------------
def extract_answer(data):
    """Parses all possible Perplexity API formats."""

    # 1) Standard chat format
    if isinstance(data, dict):
        if "choices" in data:
            try:
                return data["choices"][0]["message"]["content"]
            except:
                pass

        # 2) output_text format
        if "output_text" in data:
            return data["output_text"]

        # 3) text format
        if "text" in data:
            return data["text"]

        # 4) nested data format
        if "data" in data and isinstance(data["data"], dict):
            nested = data["data"]
            if "output_text" in nested:
                return nested["output_text"]
            if "text" in nested:
                return nested["text"]

        # 5) API error
        if "error" in data:
            return f"API Error: {data['error']}"

    # 6) fallback — show everything
    return f"Unexpected API response: {data}"


# --------------------------------------------------------
# MAIN PAGE FUNCTION
# --------------------------------------------------------
def show_ai_assistant():
    st.title("AI Insurance Assistant")
    st.write("Ask questions about health insurance, benefits, costs, and plan types.")

    # Validate Key
    if not PPLX_KEY:
        st.error("Perplexity API key is missing. Add it in Streamlit Secrets.")
        return

    # Chat history storage
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display previous messages
    for msg in st.session_state.messages:
        role = "You" if msg["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {msg['content']}")

    # User input
    user_input = st.text_input("Ask a question:")

    # --------------------------------------------------------
    # SEND MESSAGE
    # --------------------------------------------------------
    if st.button("Send") and user_input:

        # Store user message
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Build API request
        url = "https://api.perplexity.ai/chat/completions"
        headers = {
            "Authorization": f"Bearer {PPLX_KEY}",
            "Content-Type": "application/json"
        }

        # ⭐ Correct and working Perplexity model ⭐
        payload = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [
                {"role": "system", "content": "You are a helpful insurance assistant."},
                {"role": "user", "content": user_input},
            ]
        }

        # API call
        try:
            response = requests.post(url, json=payload, headers=headers)
            data = response.json()
            answer = extract_answer(data)

        except Exception as e:
            answer = f"Error contacting Perplexity: {e}"

        # Store assistant response
        st.session_state.messages.append({"role": "assistant", "content": answer})

        # Update UI
        st.success("Response received. Scroll up to view it.")

    # --------------------------------------------------------
    # CLEAR CHAT
    # --------------------------------------------------------
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.experimental_set_query_params()
        st.success("Chat cleared.")
