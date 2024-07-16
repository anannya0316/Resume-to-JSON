📄 Resume to JSON Parser
Welcome to Resume to JSON Parser! This tool extracts structured information from resumes in PDF format and converts it into JSON. Perfect for automating resume data extraction!

✨ Features
📂 PDF to JSON: Extracts detailed resume information into a JSON format.
💬 Interactive Interface: Upload PDFs and view extracted data in real-time.
🔍 Detailed Parsing: Extracts personal information, work experience, education, skills, and more.
🚀 Getting Started
Prerequisites
Python 3.7+
Streamlit
PyPDF2
OpenAI
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/anannya0316/Resume-to-JSON.git
cd Resume-to-JSON
Install dependencies:

sh
Copy code
pip install -r requirements.txt
Configuration
Add OpenAI API Key:
Create a .streamlit/secrets.toml file with your OpenAI API key:
toml
Copy code
[openai]
api_key = "YOUR_OPENAI_API_KEY"
Run the Application
sh
Copy code
streamlit run app.py
Usage
Upload PDF: Upload your resume in PDF format.
View JSON: See the extracted JSON data in real-time.
🛠️ Technology Stack
Frontend: Streamlit
Backend: Python, OpenAI GPT-3.5-turbo
PDF Processing: PyPDF2
