import streamlit as st
import requests
import base64
import os
from pdf2image import convert_from_bytes

PPLX_KEY = os.getenv("PPLX_API_KEY")


# ------------------------------------------------------------
# Helper: Convert image to Base64
# ------------------------------------------------------------
def encode_image(uploaded_file):
    return base64.b64encode(uploaded_file.read()).decode("utf-8")


# ------------------------------------------------------------
# Helper: Convert PDF → First Page PNG → Base64
# ------------------------------------------------------------
def pdf_to_image_base64(uploaded_pdf):
    pages = convert_from_bytes(uploaded_pdf.read(), dpi=200)
    first_page = pages[0]

    import io
    buf = io.BytesIO()
    first_page.save(buf, format="PNG")
    img_bytes = buf.getvalue()
    return base64.b64encode(img_bytes).decode("utf-8")


# ------------------------------------------------------------
# Main OCR Page
# ------------------------------------------------------------
def show_ocr_documents():
    st.title("OCR – Insurance & Plan Documents")

    if not PPLX_KEY:
        st.error("Missing Perplexity API key.")
        return

    st.write("Choose the type of document you want to extract:")

    mode = st.radio(
        "Select Document Type",
        ["Insurance Card (Image)", "Insurance Plan (PDF)"],
    )

    st.markdown("---")

    # ------------------------------------------------------------
    # MODE 1: INSURANCE CARD IMAGE OCR
    # ------------------------------------------------------------
    if mode == "Insurance Card (Image)":
        st.header("Insurance Card OCR")

        uploaded = st.file_uploader("Upload Insurance Card (JPG/PNG)", type=["jpg", "jpeg", "png"])

        if uploaded:
            st.image(uploaded, caption="Uploaded Insurance Card", use_column_width=True)

            if st.button("Extract Insurance Card Details"):
                with st.spinner("Extracting with AI..."):

                    img_b64 = encode_image(uploaded)

                    url = "https://api.perplexity.ai/chat/completions"
                    headers = {
                        "Authorization": f"Bearer {PPLX_KEY}",
                        "Content-Type": "application/json"
                    }

                    system_prompt = """
                    Extract all fields from the insurance card image in CLEAN JSON format.
                    If you cannot find a specific field, return "Not provided".
                    
                    Return JSON with:
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
                                    {"type": "text", "text": "Extract structured JSON only."}
                                ]
                            }
                        ]
                    }

                    response = requests.post(url, json=payload, headers=headers)
                    data = response.json()

                    if "choices" in data:
                        result = data["choices"][0]["message"]["content"]
                    else:
                        result = str(data)

                st.subheader("Extracted Insurance Card Data")
                st.code(result)
                st.success("Extraction completed.")


    # ------------------------------------------------------------
    # MODE 2: PLAN PDF OCR
    # ------------------------------------------------------------
    if mode == "Insurance Plan (PDF)":
        st.header("Insurance Plan PDF OCR")

        pdf = st.file_uploader("Upload Plan PDF", type=["pdf"])

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
                    Extract all insurance plan fields from this PDF (first page only).
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

                    If any field is missing, return "Not provided".
                    """

                    payload = {
                        "model": "mixtral-8x7b-instruct",
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {
                                "role": "user",
                                "content": [
                                    {"type": "input_image", "image": img_b64},
                                    {"type": "text", "text": "Extract JSON only."}
                                ]
                            }
                        ]
                    }

                    response = requests.post(url, json=payload, headers=headers)
                    data = response.json()

                    if "choices" in data:
                        result = data["choices"][0]["message"]["content"]
                    else:
                        result = str(data)

                st.subheader("Extracted Plan Data")
                st.code(result)
                st.success("Plan extraction completed.")
