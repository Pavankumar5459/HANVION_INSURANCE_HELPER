import streamlit as st
import requests
import base64
import os

PPLX_KEY = os.getenv("PPLX_API_KEY")

def encode_image(uploaded_file):
    """Convert uploaded image to Base64."""
    return base64.b64encode(uploaded_file.read()).decode("utf-8")


def show_ocr():
    st.title("Insurance Card OCR")
    st.write("Upload the front or back of an insurance card to extract ID, group number, copays, plan details, and phone numbers.")

    if not PPLX_KEY:
        st.error("Perplexity API key missing. Add PPLX_API_KEY to Streamlit Secrets.")
        return

    uploaded = st.file_uploader("Upload insurance card image", type=["jpg", "jpeg", "png"])

    if uploaded:
        st.image(uploaded, caption="Uploaded Insurance Card", use_column_width=True)

        if st.button("Extract Insurance Information"):
            with st.spinner("Extracting information..."):

                # Convert to base64
                image_b64 = encode_image(uploaded)

                url = "https://api.perplexity.ai/chat/completions"
                headers = {
                    "Authorization": f"Bearer {PPLX_KEY}",
                    "Content-Type": "application/json"
                }

                # Vision prompt
                prompt = (
                    "Extract the following fields from this insurance card image. "
                    "If any field is missing, return 'Not found'. "
                    "Fields:\n"
                    "- Member Name\n"
                    "- Member ID\n"
                    "- Group Number\n"
                    "- Plan Name\n"
                    "- Insurance Company\n"
                    "- Phone Numbers\n"
                    "- Copay Information (PCP, Specialist, ER, Urgent Care)\n"
                    "- Deductible Information\n"
                    "- Prescription (Rx) Benefits\n"
                    "- Plan Type (HMO, PPO, EPO, HDHP)\n"
                )

                payload = {
                    "model": "sonar-small-chat",
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are an insurance card OCR assistant. Extract structured insurance fields clearly."
                        },
                        {
                            "role": "user",
                            "content": prompt,
                        },
                        {
                            "role": "user",
                            "content": [
                                {
                                    "type": "input_image",
                                    "image": image_b64
                                }
                            ]
                        }
                    ]
                }

                try:
                    response = requests.post(url, headers=headers, json=payload)
                    data = response.json()

                    # Try parsing all possible formats
                    if "choices" in data:
                        extracted = data["choices"][0]["message"]["content"]
                    elif "output_text" in data:
                        extracted = data["output_text"]
                    else:
                        extracted = f"Unexpected response format: {data}"

                except Exception as e:
                    extracted = f"Error contacting Perplexity: {e}"

                st.subheader("Extracted Insurance Information")
                st.write(extracted)

    st.caption("This OCR tool uses AI to extract fields from insurance cards. Accuracy may vary depending on image quality.")
