### Hello, I ma ver very very excited to work on you : ) : ) Hi Hi Hi

import json 
import os 
import PyPDF2
import traceback2 


###1 : File reading fiunction 


def file_reader(file): 
    if file.name.endswith(".pdf"): 
        try:
            pdf_reader =PyPDF2.PdfFileReader(file) 
            text = ""
            for page in pdf_reader.pages: 
                text+= page.extract_text()
                return text 
        except Exception as e: 
            raise Exception("Error Reading the Pdf file") ### You basically want ot read a pdf file into a big string, otherwise, error  
        
    elif file.name.endswith(".txt"): 
        return file.read().decode("utf-8") 
    else: 
        raise Exception(
            "Unsupported file format"
            )       
    


def get_table_data(quiz_str): 
    try: 
        quiz_dict = json.loads(quiz_str)
        quiz_data_table = []


        for key, value in quiz_dict.items():
            mcq = value["mcq"]
            options = "|".join(
                [
                    f" {option}:{option_value}"  
                    for option, option_value in value["options"].items()
                    ])
            
            correct = value["correct"]
            quiz_data_table.append({"MCQ":mcq, "Choices": options, "Correct": correct })

    except Exception as e : 
        traceback2.print_exception(type(e),e,e.__traceback__)
        return False
        