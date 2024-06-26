import json
import traceback
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file,get_table_data
from src.mcqgenerator.MCQgenerator import generate_evaluate_chain
from src.mcqgenerator.logger import logging
from langchain_community.callbacks.manager import get_openai_callback


with open(r'C:\Users\Dell\mcqgenproj\Response.json','r') as file:
    RESPONSE_JSON = json.load(file)

#create a form my st.form
with st.form("user_inputs"):

    st.title("Welcome to the Langchain MCQGen App!")
    #file upload
    uploaded_file=st.file_uploader("Upload a PDF or TXT File")

    #input fields
    mcq_count=st.number_input("No. of MCQs",min_value=3,max_value=50)

    subject=st.text_input("Subject",max_chars=20)

    tone=st.text_input("Complexity level of Questoins",max_chars=20,placeholder='Simple')

    # add button 
    button=st.form_submit_button("Create MCQs")

    # check if the button is clicked and all fields have inputs

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Loading..."):
            try:
                text=read_file(uploaded_file)
                #count token and the cost of API call
                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            "text": text,
                            "number": mcq_count,
                            "subject": subject,
                            "tone": tone,
                            "response_json": json.dumps(RESPONSE_JSON)
                        }
                    )

            except Exception as e:
                traceback.print_exception(type(e),e,e.__traceback__)
                st.error("Error")

            else:
               print(f"Total Tokens: {cb.total_tokens}")
               print(f"Prompt Tokens: {cb.prompt_tokens}")
               print(f"Completion Tokens: {cb.completion_tokens}")
               print(f"Total Cost: {cb.total_cost}")

               if isinstance(response,dict):
                   #extract the quiz data from the response
                   quiz=response.get("quiz",None)
                   if quiz is not None:
                       table_data=get_table_data(quiz)
                       if table_data is not None:
                           df=pd.DataFrame(table_data)
                           df.index=df.index+1
                           st.table(df)
                            #display review in text box as well
                           st.text_area(label="Review",value=response["review"])
                       else:
                           st.error("Error in the table data")
                   else:
                       st.write(response)
                       



