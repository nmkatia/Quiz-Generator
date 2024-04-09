from dotenv import load_dotenv
import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain 
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
 
import json
from src.mcqgen.logger import logging
from src.mcqgen.utils import file_reader, get_table_data



load_dotenv()

### Acccesing the env variables using os.environ.get()

key = os.environ.get("OPENAI_API_KEY")

### Instantinating my LLM

llm = OpenAI(openai_api_key = key)

## My Template

TEMPLATE1 = """
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to\
create a quiz of {number} multiple choice questions for {subject} students in tone {tone}.
Make sure that the questions are not repeated and check all the questions to be conforming the text as well.
Make sure to format your responses like RESPONSE _JSON below and use it as a guide. \
### RESPONSE_JSON
{response_json}
"""
### My Prompt

prompt1 = PromptTemplate(
    input_variables = ["text", "number", "subject", "tone", "response_json"],
    template = TEMPLATE1)

### My LLMchain (llm+prompt)
quiz_chain = LLMChain(llm= llm, prompt = prompt1, output_key= "quiz", verbose= True)


### My template 2 : For review which takes the output prompt as an input varibale to the review prompt
TEMPLATE2 = """
You are an expert english grammmarian and writer. Given a multiple choice quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity. \
If the quiz is not at per with the cognitive and analytical capabilities of teh students.\
Update the quiz questions that need to be changed and change the tone such that it matches the student capabilities.
QUIZ_MCQ:
{quiz}
Check from an expert English Writer of the above quiz
"""

### My Review Prompt
prompt2= PromptTemplate(
    input_variables= ["subject", "quiz"], 
    template=TEMPLATE2
)
### My Review Chain, llm already instantiated
review_chain= LLMChain(llm=llm, prompt= prompt2, output_key="review", verbose =True)

### My final SequentialChain: wich takes in a chains list and input variables as parameters 
final_chain = SequentialChain (chains = [quiz_chain, review_chain],input_variables=["text","number", "subject", "tone","response_json" ],
                               output_variables = ["quiz", "review"], verbose = True)