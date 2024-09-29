---
title: GOT OCR Web App  # Title of your app
emoji: 📄  # You can choose any emoji that represents your app
colorFrom: blue  # Start color for the gradient background
colorTo: green  # End color for the gradient background
sdk: streamlit  # Your app uses Streamlit
sdk_version: "1.21.0"  # Version of Streamlit you are using
app_file: app.py  # Entry point of your application
pinned: false  # Whether this Space should be pinned on your profile
---



# OCR Web Application

## Project Overview
This is a **web-based Optical Character Recognition (OCR) application** built using Streamlit. The app supports both English and Hindi languages, allowing users to upload images and extract text using advanced OCR models.

## How the Application Works
1. Choose Language: Select either English or Hindi using the sidebar instructions.
2. Upload Image: Use the file uploader to input an image in JPG, PNG, or JPEG format.
3. Text Extraction: For English, the app uses the GOT OCR 2.0 model to extract text, while for Hindi, it leverages EasyOCR.
4. Keyword Search: After text extraction, you can search for specific keywords within the extracted text. Matching keywords will be highlighted, and any missing keywords will be displayed in a warning message.
5. Reset: If needed, reset the session and upload a new image to start over.

## Installation and Setup

### Prerequisites:
- **Python 3.8 or higher**
- Required libraries listed in `requirements.txt`

### Installation Steps:
1. **Clone the repository**:
   ```bash
   git clone https://github.com/Trisandhyadevi/OCR.git

2. **Navigate to the project directory**
   ```bash
    cd OCR

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

4. **Run the application:**
    ```bash
    streamlit run app.py


# Description

This web application supports converting images to text using the GOT OCR 2.0 Model. Below are some key features of the GOT OCR 2.0 model

# GOT OCR 2.0 Model Overview

The GOT OCR 2.0 Model is a state-of-the-art OCR system designed for accurate text extraction from images. Key features include:

- **Multi-task Learning**: The model supports various tasks beyond OCR, including layout analysis and object detection, making it versatile for diverse text recognition needs.
- **End-to-End Pipeline**: It efficiently processes entire images, identifying and extracting text without the need for additional preprocessing steps.

Note: Currently, the model does not support all languages. Fine-tuning is required for languages not included in the pre-trained model. For more information on fine-tuning, visit the [GOT OCR 2.0 Fine-tuning Guide](https://github.com/Ucas-HaoranWei/GOT-OCR2.0/?tab=readme-ov-file#fine-tune).

For more technical details about the model architecture and usage, visit the [GOT OCR 2.0 Model Documentation](https://github.com/Ucas-HaoranWei/GOT-OCR2.0/?tab=readme-ov-file#general-ocr-theory-towards-ocr-20-via-a-unified-end-to-end-model).


## Deployment
To deploy the application to a cloud platform(Hugging Face)

## Folder Structure
```bash
.
├── app.py                # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Projectdocumentation


