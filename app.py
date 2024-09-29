from transformers import AutoModel, AutoTokenizer,AutoProcessor
import streamlit as st
import os
from PIL import Image
import torch
from torchvision import io
import torchvision.transforms as transforms
import random
import pandas as pd
import easyocr
import numpy as np
import re


def start():
    st.session_state.start = True

def reset():
    del st.session_state['start']
    del st.session_state.language

@st.cache_resource
def model():
    model_path = "D:\IIT-r"
    tokenize = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU',trust_remote_code = True)
    model = AutoModel.from_pretrained('srimanth-d/GOT_CPU',trust_remote_code= True,use_safetensors= True,pad_token_id=tokenize.eos_token_id)
    model = model.eval()
    return model, tokenize

@st.cache_data
def get_text(image_file,_model,_tokenizer):
    res =_model.chat(_tokenizer,image_file,ocr_type= 'ocr')
    return res
    
@st.cache_resource
def highlight_keywords(text, keywords):
    colors = generate_unique_colors(len(keywords))
    highlighted_text = text
    found_keywords = []
    for keyword, color in zip(keywords, colors):
        if keyword.lower() in text.lower():
            highlighted_text = highlighted_text.replace(keyword, f'<mark style="background-color: {color};">{keyword}</mark>')
            found_keywords.append(keyword)
    return highlighted_text, found_keywords

@st.cache_data
def generate_unique_colors(n):
    colors = []
    for i in range(n):
        color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        while color in colors:
            color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
        colors.append(color)
    return colors

@st.cache_data
def extract_text_easyocr(_image):
    reader = easyocr.Reader(['hi'],gpu = False)
    results = reader.readtext(np.array(_image))
    # return results
    return " ".join([result[1] for result in results])


def search():
    st.session_state.search = True

if 'start' not in st.session_state:
    st.session_state.start = False

if 'search' not in st.session_state:
    st.session_state.search = False

if 'reset' not in st.session_state:
    st.session_state.reset = False

if 'language' not in st.session_state:
    st.session_state.language = False
    
with st.sidebar:
    st.header("Instructions")
    st.write("1. Choose a language (English or Hindi).")
    st.write("2. Upload an image in JPG, PNG, or JPEG format.")
    st.write("3. The app will extract text from the image using OCR.")
    st.write("4. Enter keywords to search within the extracted text.")
    st.write("5. If needed, click 'Reset' to upload a new image.")


st.header("Optical Character Recognition ")
col1, col2 = st.columns(2)

with col1:
    if st.button('English'):
        
        st.session_state.language = 'English'
        st.rerun()
        

with col2:
    if st.button('Hindi'):
        
        st.session_state.language = 'Hindi'
        st.rerun()
        

if st.session_state.language == 'English':
        st.title("GOT OCR - Extract Text from Images")
        st.write("Upload an image and let the GOT model extract the text!")

        try:
            MODEL, TOKENIZER = model()
            st.success("GOT model loaded successfully")
        except Exception as e:
            st.error(f"Error loading GOT model: {str(e)}")

        image_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

        if image_file is not None:
            st.image(image_file, caption="Uploaded Image", use_column_width=True)

            if not os.path.exists("images"):
                os.makedirs("images")
            with open(f"images/{image_file.name}", "wb") as f:
                f.write(image_file.getbuffer())

            extracted_text = get_text(f"images/{image_file.name}", MODEL, TOKENIZER)
            # st.session_state.extracted_text = extracted_text
            
            st.subheader("Extracted Text:")
            st.write(extracted_text)

            keywords_input = st.text_input("Enter keywords to search within the extracted text (comma-separated):")
            if keywords_input:
                keywords = [keyword.strip().lower() for keyword in keywords_input.split(',')]  # Convert keywords to lowercase
                lower_extracted_text = extracted_text.lower()  # Convert extracted text to lowercase
                highlighted_text, found_keywords = highlight_keywords(lower_extracted_text, keywords)
                st.button("Search", on_click=search)
                if st.session_state.search:
                    if found_keywords:
                        st.markdown(highlighted_text, unsafe_allow_html=True)
                        st.write(f"Found keywords: {', '.join(found_keywords)}")
                    else:
                        st.warning("No keywords found in the extracted text.")

                    not_found_keywords = set(keywords) - set(found_keywords)
                    if not_found_keywords:
                        st.error(f"Keywords not found: {', '.join(not_found_keywords)}")
            
            st.button("Reset and Upload New Image",on_click=reset)
                


elif st.session_state.language == 'Hindi':
        st.title("HINDI OCR - Extract Text from Images")
        st.write("Upload an image and let EasyOCR extract the text!")
        
        
        image_file_hi = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])
        
        if image_file_hi:
            st.image(image_file_hi, caption="Uploaded Image", use_column_width=True)

            image = Image.open(image_file_hi)
            extracted_text_hindi =extract_text_easyocr(image)
            
            st.subheader("Extracted Text:")
            st.write(extracted_text_hindi)

            keywords_input = st.text_input("Enter keywords to search within the extracted text (comma-separated):")
            if keywords_input:
                keywords = [keyword.strip() for keyword in keywords_input.split(',')]
                highlighted_text, found_keywords = highlight_keywords(extracted_text_hindi, keywords)

                st.subheader("Search Results:")
                if found_keywords:
                    st.markdown(highlighted_text, unsafe_allow_html=True)
                    st.write(f"Found keywords: {', '.join(found_keywords)}")
                else:
                    st.warning("No keywords found in the extracted text.")

                not_found_keywords = set(keywords) - set(found_keywords)
                if not_found_keywords:
                    st.error(f"Keywords not found: {', '.join(not_found_keywords)}")

            st.button("Reset and Upload New Image",on_click=reset)