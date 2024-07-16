# 📄 Resume to JSON Parser

Welcome to **Resume to JSON Parser**! This tool extracts structured information from resumes in PDF format and converts it into JSON. Perfect for automating resume data extraction!


FYI : the app might take some time to show results so be patient! It is working!
 
## ✨ Features

<ul>
  <li><span style="font-size: 1.2em;">📂 PDF to JSON</span>: Extracts detailed resume information into a JSON format.</li>
  <li><span style="font-size: 1.2em;">💬 Interactive Interface</span>: Upload PDFs and view extracted data in real-time.</li>
  <li><span style="font-size: 1.2em;">🔍 Detailed Parsing</span>: Extracts personal information, work experience, education, skills, and more.</li>
</ul>

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Streamlit
- PyPDF2
- OpenAI

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
