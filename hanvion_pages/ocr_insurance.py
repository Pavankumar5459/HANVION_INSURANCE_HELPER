import streamlit as st
import requests
import base64
import os

PPLX_KEY = os.getenv("PPLX_API_KEY")

def encode_image(uploaded_file):
    """Convert uploaded JPG/PNG to Base64."""
    return base64.b64encode(uploaded_file.read()).decode("utf-8")


def show_ocr():
    st.title("Insurance Card OCR")
    st.write("Upload the front/back of an insurance card to extract structured details.")

    if not PPLX_KEY:
        st.error("Missing Perplexity API key.")
        return

    uploaded = st.file_uploader("Upload Insurance Card (JPG or PNG)", type=["jpg", "jpeg", "png"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Insurance Card", use_column_width=True)

        if st.button("Extract Insurance Details"):

            with st.spinner("Extracting with AI..."):

                img_b64 = encode_image(uploaded)

                url = "https://api.perplexity.ai/chat/completions"
                headers = {
                    "Authorization": f"Bearer {PPLX_KEY}",
                    "Content-Type": "application/json"
                }

                system_prompt = """
                You are an insurance card OCR assistant. Extract all fields in clean JSON format.
                If a field is missing, return "Not provided".

                Required fields:
                - member_name
                - member_id
                - group_number
                - plan_type
                - insurance_company
                - phone_numbers
                - copay_pcp
                - copay_specialist
                - copay_er
                - copay_urgent
                - deductible
                - rx_tier1
                - rx_tier2
                - rx_tier3
                """

                payload = {
                    "model": "mixtral-8x7b-instruct",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_image", "image": img_b64},
                                {"type": "text", "text": "Extract all fields in JSON."}
                            ]
                        }
                    ]
                }

                try:
                    response = requests.post(url, headers=headers, json=payload)
                    data = response.json()

                    # Parse safely
                    if "choices" in data:
                        raw_text = data["choices"][0]["message"]["content"]
                    else:
                        raw_text = str(data)

                except Exception as e:
                    raw_text = f"Error: {e}"

                st.subheader("Extracted Insurance Data")
                st.code(raw_text)

                st.success("Extraction complete.")
