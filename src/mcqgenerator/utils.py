import json
import os
import PyPDF2
import traceback

def read_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except Exception as e:
            print(f"Error: {e}")
            raise Exception("Error reading the PDF file") from e
        
    elif file.name.endswith('.txt'):
        try:
            return file.read().decode('utf-8')
        except Exception as e:
            print(f"Error: {e}")
            raise Exception("Error reading the TXT file") from e
    else:
        raise Exception("Unsupported file format, only PDF and TXT files are supported")


def get_table_data(quiz_str):
    try:
        # convert the quiz from str to dictionary
        quiz_dict = json.loads(quiz_str)
        quiz_table_data=[]

        # iterate over the quiz dictionary and extract the required info
        for key,value in quiz_dict.items():
            mcq=value["mcq"]
            options=" || ".join(
                [
                    f"{option}->{option_value}" 
                    for option,option_value in value["options"].items()
                ]
            )

            correct=value["correct"]
            quiz_table_data.append({"MCQ":mcq,"Choices":options,"Correct":correct})

        return quiz_table_data
    
    except Exception as e:
        traceback.print_exception(type(e),e,e.__traceback__)
        return False
