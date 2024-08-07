import streamlit as st
import PyPDF2
import openai
import json

openai.api_key = st.secrets["openai"]["api_key"]

def parse_resume_gpt(text):
    messages = [
        {"role": "system", "content": "You are an expert resume analyst with a keen eye for detail."},
        {"role": "user", "content": f"""
        You are an expert resume analyst. Your task is to meticulously extract structured information from resumes.
        If any information is missing, do not fill in the information with something else. Only take information that is already provided.
        Please extract the following information from the resume text provided below and return it in JSON format:

        1. Personal Information:
           - Full Name
           - Contact Information (Phone, Email, Address)
           - All social profiles links with their names (if available)

        2. Work Experience:
           - Job Title
           - Company Name
           - Location
           - Dates of Employment (Start Date - End Date)
           - Detailed Responsibilities and Achievements

        3. Education:
           - Degree
           - University/College Name
           - Graduation Year
           - Major/Field of Study

        4. Skills:
           - A comprehensive list of professional skills

        5. Certifications:
           - Certification Name
           - Issuing Organization
           - Date of Issuance

        6. Projects:
           - Project Title
           - Description
           - Technologies Used
           - Role in the Project

        7. Awards and Honors:
           - Award Title
           - Issuing Organization
           - Date Received
           - Description

        8. Languages:
           - List of languages spoken with proficiency levels

        Resume Text:
        {text}

        Extracted Information (in JSON format):
        """}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    return response.choices[0].message['content']

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text() + "\n"
    return text

st.title("Resume Parser with GPT")
st.write("Upload your resume to parse it into JSON format using GPT-3.5-turbo.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner('Extracting text from PDF...'):
        resume_text = extract_text_from_pdf(uploaded_file)
        st.success('Text extracted successfully.')
    
        with st.spinner('Processing resume with GPT...'):
            parsed_data = parse_resume_gpt(resume_text)
            st.success('Resume processed successfully.')
    
            # Attempt to clean and load the response as JSON
            try:
                # Clean the response to ensure it's valid JSON
                start_idx = parsed_data.find('{')
                end_idx = parsed_data.rfind('}') + 1
                cleaned_data = parsed_data[start_idx:end_idx]
                parsed_data_json = json.loads(cleaned_data)
                # Print the parsed data
                st.json(parsed_data_json)
            except json.JSONDecodeError as e:
                st.error("Failed to decode JSON response")
                st.text(f"Error: {e}")
                # Print the cleaned data for further debugging
                st.text(cleaned_data)
