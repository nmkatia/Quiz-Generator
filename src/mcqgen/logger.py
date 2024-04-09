import logging 
import os 
from datetime import datetime  


LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log" ### fuck it, this is just to add it to thepath later
log_path = os.path.join(os.getcwd(),"logs")
dir = os.makedirs(log_path, exist_ok=True)
LOG_FILEPATH = os.path.join(log_path,LOG_FILE)
logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO, format= "[%(asctime)s] : %(lineno)d : %(name)s : %(levelname)s : %(message)s")

