# 📄 Resume to JSON Parser

Welcome to **Resume to JSON Parser**! This tool extracts structured information from resumes in PDF format and converts it into JSON. Perfect for automating resume data extraction!

**[Run the app](https://resume-to-json.streamlit.app/)**

FYI: The app might take some time to show results, so be patient! It is working!

## ✨ Features

- 📂 **PDF to JSON**: Extracts detailed resume information into a JSON format.
- 💬 **Interactive Interface**: Upload PDFs and view extracted data in real-time.
- 🔍 **Detailed Parsing**: Extracts personal information, work experience, education, skills, and more.

## 🚀 Getting Started

### Prerequisites

- **Python 3.7+**: The programming language used for development.
- **Streamlit**: A framework used to create the web application.
- **PyPDF2**: A library to read and extract text from PDF files.
- **OpenAI**: The API used for generating structured data from the resume text.

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/anannya0316/Resume-to-JSON.git
    cd Resume-to-JSON
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Configuration

1. **Add OpenAI API Key**:
    Create a `.streamlit/secrets.toml` file with your OpenAI API key:
    ```toml
    [openai]
    api_key = "YOUR_OPENAI_API_KEY"
    ```

### Run the Application

```sh
streamlit run app.py
