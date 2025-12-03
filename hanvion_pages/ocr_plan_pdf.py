import streamlit as st
import requests
import base64
import os
from pdf2image import convert_from_bytes

PPLX_KEY = os.getenv("PPLX_API_KEY")

def pdf_to_image_base64(uploaded_pdf):
    pages = convert_from_bytes(uploaded_pdf.read(), dpi=200)
    first_page = pages[0]

    # Convert to PNG base64
    import io
    buf = io.BytesIO()
    first_page.save(buf, format="PNG")
    img_bytes = buf.getvalue()
    return base64.b64encode(img_bytes).decode("utf-8")


def show_pdf_ocr():
    st.title("Plan PDF OCR")
    st.write("Upload a plan PDF to extract deductible, premium, OOP max, copays, and plan type.")

    if not PPLX_KEY:
        st.error("Missing API key.")
        return

    pdf = st.file_uploader("Upload Insurance Plan PDF", type=["pdf"])

    if pdf:
        if st.button("Extract Plan Details"):
            with st.spinner("Processing PDF..."):
                img_b64 = pdf_to_image_base64(pdf)

                url = "https://api.perplexity.ai/chat/completions"
                headers = {
                    "Authorization": f"Bearer {PPLX_KEY}",
                    "Content-Type": "application/json"
                }

                system_prompt = """
                Extract the following fields from this insurance PDF (first page only):

                Return CLEAN JSON with:
                - plan_name
                - premium
                - deductible
                - oop_max
                - coinsurance
                - copay_pcp
                - copay_specialist
                - copay_er
                - copay_urgent
                - rx_tier1
                - rx_tier2
                - rx_tier3
                - plan_type
                - extra_benefits_count

                If any value is missing, return "Not provided".
                """

                payload = {
                    "model": "mixtral-8x7b-instruct",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_image", "image": img_b64},
                                {"type": "text", "text": "Extract as JSON only."},
                            ]
                        }
                    ]
                }

                try:
                    response = requests.post(url, headers=headers, json=payload)
                    data = response.json()

                    if "choices" in data:
                        extracted = data["choices"][0]["message"]["content"]
                    else:
                        extracted = str(data)

                except Exception as e:
                    extracted = f"Error: {e}"

                st.subheader("Extracted Plan Data")
                st.code(extracted)
                st.success("Plan details extracted successfully.")
