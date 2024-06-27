import json
import os
import PyPDF2
import traceback

def read_file(file):
    if file.name.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
    else:
        raise Exception("Unsupported file format, only PDF and TXT files are supported")

def get_table_data(quiz_str):
    try:
        # Remove prefix if present
        if quiz_str.startswith("### RESPONSE_JSON"):
            quiz_str = quiz_str[len("### RESPONSE_JSON"):].strip()
        
        quiz_dict = json.loads(quiz_str)
        quiz_table_data = []

        # iterate over the quiz dictionary and extract the required info
        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = " || ".join(
                [
                    f"{option}->{option_value}" 
                    for option, option_value in value["options"].items()
                ]
            )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})

        return quiz_table_data
    
    except json.JSONDecodeError as json_error:
        raise Exception(f"Invalid JSON format in quiz data: {json_error}")

    except Exception as e:
        raise Exception(f"An error occurred while processing the quiz data: {e}")

