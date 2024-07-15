import streamlit as st
import PyPDF2
import openai
import json

# Initialize OpenAI with your API key
openai.api_key = 'sk-proj-zDl7PgYHSwsMpb4Ty9VxT3BlbkFJ6Dg07gYLKYGuQ10vHdYG'

def parse_resume_gpt(text):
    prompt = f"""
    Extract the following information from the resume text provided:
    - Name
    - Contact Information
    - Professional Summary
    - Work Experience
    - Education
    - Skills

    Resume Text:
    {text}

    Extracted Information (in JSON format):
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return response.choices[0].text.strip()

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfFileReader(file)
    text = ""
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text += page.extract_text()
    return text

st.title("Resume Parser with GPT")
st.write("Upload your resume to parse it into JSON format using GPT.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    resume_text = extract_text_from_pdf(uploaded_file)
    parsed_data = parse_resume_gpt(resume_text)
    st.write("Parsed Resume Data:")
    st.json(json.loads(parsed_data))

    # Download JSON
    st.download_button("Download JSON", parsed_data, file_name="resume.json")
