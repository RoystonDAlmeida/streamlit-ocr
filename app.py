import time
from pdf2image import convert_from_bytes
from ocr_function import get_ocr_result
import streamlit as st
from PIL import Image
import io

# Set the page window document title
st.set_page_config(
    page_title="Extracting Text using OCR",
    page_icon="📝",
    layout="wide"
)

st.title("Extracting Text from Image/PDF using OCR")
st.write("This app extracts text from scanned images and PDFs using Pytesseract OCR.")

uploaded_file = st.file_uploader("Choose a File:", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    start_time = time.time()

    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        single_img_doc = convert_from_bytes(pdf_bytes)  # Convert PDF to images
        result, json_output = get_ocr_result(single_img_doc)  # Pass list of images to OCR function
    else:
        image_bytes = uploaded_file.read()
        img = Image.open(io.BytesIO(image_bytes))  # Open image from bytes
        result, json_output = get_ocr_result(img)  # Pass the image directly

    st.write(result, json_output)