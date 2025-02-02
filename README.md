# OCR Application Using Streamlit

This is an Optical Character Recognition (OCR) application built with Streamlit, designed to extract text from images and PDF documents using the Tesseract OCR engine. The application provides a user-friendly interface for uploading files and viewing extracted text.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)

## Features

- Upload images (JPEG, PNG) and PDF documents for text extraction.
- Extract text using Tesseract OCR.
- Display extracted text in a clean and readable format.
- Support for multiple file uploads.
- Simple and intuitive user interface built with Streamlit.

## Requirements

Before running the application, ensure you have the following installed:

- Python 3.7 or higher
- Tesseract OCR
- Required Python packages listed in `requirements.txt`

### Tesseract Installation

#### On Ubuntu:
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

#### On macOS:
```bash
brew install tesseract
```

#### On Windows:
```bash
Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions.
```

## Installation

1. Clone this repository to your local machine:
```bash
git clone https://github.com/RoystonDAlmeida/streamlit-ocr.git
cd streamlit-ocr/
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```

3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Use the file uploader to select images or PDF documents from your local machine.

4. Click on the "Extract Text" button to process the uploaded files.

5. The extracted text will be displayed on the page.

## How It Works

This application uses the following libraries:

- **Streamlit**: For creating the web interface.
- **Pillow**: For image processing.
- **Pytesseract**: For performing OCR on images and PDFs.
- **pdf2image**: For converting PDF pages into images before applying OCR.

The workflow of the application is as follows:

1. The user uploads an image or PDF document.
2. If a PDF is uploaded, it is converted into images using `pdf2image`.
3. The images are processed by Pytesseract to extract text.
4. The extracted text is displayed in the web interface.