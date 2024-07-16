import streamlit as st
import PyPDF2
import openai
import json

# Load OpenAI API key from secrets
openai.api_key = st.secrets["openai"]["api_key"]

def parse_resume_gpt(text):
    prompt = f"""
    You are an expert resume analyst. Your task is to meticulously extract structured information from resumes. If any information is missing, do not fill in the information with something else. Only take information that is already provided. Please extract the following information from the resume text provided below and return it in JSON format:
    
    1. Personal Information:
       - Full Name
       - Contact Information (Phone, Email, Address)
       - all social profiles links with their names(if available)

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
    """

    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1500,
        temperature=0.7
    )

    return response.choices[0].text.strip()

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
        st.write("Extracted Text from PDF:")
        st.text(resume_text)  # Display the extracted text
    
        with st.spinner('Processing resume with GPT...'):
            parsed_data = parse_resume_gpt(resume_text)
            st.success('Resume processed successfully.')
    
            # Print the raw GPT response for debugging
            st.write("Raw GPT Response:")
            st.text(parsed_data)
    
            # Attempt to clean and load the response as JSON
            try:
                # Clean the response to ensure it's valid JSON
                start_idx = parsed_data.find('{')
                end_idx = parsed_data.rfind('}') + 1
                cleaned_data = parsed_data[start_idx:end_idx]
                parsed_data_json = json.loads(cleaned_data)
                # Print the parsed data
                st.write("This is the JSON format of the resume:")
                st.json(parsed_data_json)
            except json.JSONDecodeError as e:
                st.error("Failed to decode JSON response")
                st.text(f"Error: {e}")
                # Print the cleaned data for further debugging
                st.write("Cleaned GPT Response:")
                st.text(cleaned_data)
