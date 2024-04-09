import os 
import json 
import traceback2
import pandas as pd 
from dotenv import load_dotenv
from src.mcqgen.utils import file_reader, get_table_data
from src.mcqgen.logger import logging
from langchain.callbacks import get_openai_callback
from src.mcqgen.MCQGenerator import final_chain
import streamlit as st 


with open ("Response.json", "r") as file : 
    RESPONSE_JSON = json.load(file)


st.title ("Hello there :) :)  this is an MCQ generator application with LangChain")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a pdf or text file")
    mcq_count = st.number_input("N. of MCQ's", min_value= 2, max_value=10)
    subject = st.text_input("Insert a Subject", max_chars= 20)
    tone= st.text_input("Complexity Level of Questions", max_chars= 20, placeholder= "Simple")
    button = st.form_submit_button("Create MCQ")

    if button and uploaded_file is not None and mcq_count and subject and tone: 
        with st.spinner("loading ...."): 
            try: 
                text = file_reader(uploaded_file)
                with get_openai_callback() as cb :
                    response = final_chain ({
                        "text": text,
                        "number":mcq_count, 
                        "subject": subject, 
                        "tone":tone , 
                        "response_json": json.dumps(RESPONSE_JSON) 
                        }
                    )
                    

            except Exception as e: 
                traceback2.print_exception(type(e), e, e.__traceback__)
                st.error("Error")


            else : 
                print(f'total token is {cb.total_tokens}')
                print(f'prompt tokens is {cb.prompt_tokens}')
                print(f'completion tokens is {cb.completion_tokens}')
                print(f'Total Cost is {cb.total_cost}')

                if isinstance(response,dict): 
                    quiz=response.get("quiz", None)
                    if quiz is not None: 
                        table_data = get_table_data(quiz)
                        if table_data is not None: 
                            df = pd.DataFrame(table_data)
                            df.index= df.index+1 
                            st.table(df)

                            st.text_area(label="review", value=response["review"])
                        else :
                            st.error("Eroor in the Table")
 

                else: 
                    st.write(response)


                











