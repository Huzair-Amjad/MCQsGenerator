# Langchain MCQGen App

Welcome to the Langchain MCQGen App! This application uses Langchain to generate and evaluate multiple-choice questions (MCQs) based on the text provided by the user. It leverages OpenAI's API for text processing and question generation.

## Features

- Upload a PDF or TXT file containing text
- Specify the number of MCQs to generate
- Provide the subject and complexity level for the questions
- Display generated MCQs in a table format
- Review the generated questions

## Prerequisites

- Python 3.7 or higher
- OpenAI API key

## Installation

1. Clone the repository:
   
   git clone https://github.com/yourusername/mcqgenproj.git
   cd mcqgenproj

2. Create a virtual environment and activate it:

   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:

   pip install -r requirements.txt

4. Create a '.env' file in the project directory and add your OpenAI API key:

   OPENAI_API_KEY=your_openai_api_key

5. Project Structure:

   mcqgenproj/
├── src/
│   ├── mcqgenerator/
│   │   ├── utils.py
│   │   ├── MCQgenerator.py
│   │   └── logger.py
│   └── ...
├── Response.json
├── StreamlitAPP.py
└── requirements.txt


Usage:

1. Run the streamlit app:

   streamlit run StreamlitAPP.py

2. Open the URL provided by Streamlit (usually 'http://localhost:8501') in your web browser.

3. Follow the instructions in the app:

   * Upload a PDF or TXT file.
   * Enter the number of MCQs you want to generate.
   * Provide the subject of the questions.
   * Specify the complexity level of the questions.
   * Click the "Create MCQs" button.

4. View the generated MCQs in the table and review the questions.


