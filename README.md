<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume to JSON Parser</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        ul li {
            margin: 10px 0;
        }
        .feature {
            font-size: 1.2em;
        }
        pre {
            background: #333;
            color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>📄 Resume to JSON Parser</h1>
    <p>Welcome to <strong>Resume to JSON Parser</strong>! This tool extracts structured information from resumes in PDF format and converts it into JSON. Perfect for automating resume data extraction!</p>

    <p><strong><a href="https://resume-to-json.streamlit.app/">Run the app</a></strong></p>

    <p>FYI: The app might take some time to show results, so be patient! It is working!</p>

    <h2>✨ Features</h2>
    <ul>
        <li class="feature">📂 PDF to JSON: Extracts detailed resume information into a JSON format.</li>
        <li class="feature">💬 Interactive Interface: Upload PDFs and view extracted data in real-time.</li>
        <li class="feature">🔍 Detailed Parsing: Extracts personal information, work experience, education, skills, and more.</li>
    </ul>

    <h2>🚀 Getting Started</h2>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.7+</li>
        <li>Streamlit</li>
        <li>PyPDF2</li>
        <li>OpenAI</li>
    </ul>

    <h3>Installation</h3>
    <p>1. <strong>Clone the repository</strong>:</p>
    <pre>
        git clone https://github.com/anannya0316/Resume-to-JSON.git
        cd Resume-to-JSON
    </pre>

    <p>2. <strong>Install dependencies</strong>:</p>
    <pre>pip install -r requirements.txt</pre>

    <h3>Configuration</h3>
    <p>1. <strong>Add OpenAI API Key</strong>:</p>
    <p>Create a <code>.streamlit/secrets.toml</code> file with your OpenAI API key:</p>
    <pre>
        [openai]
        api_key = "YOUR_OPENAI_API_KEY"
    </pre>

    <h3>Run the Application</h3>
    <pre>streamlit run app.py</pre>
</body>
</html>
