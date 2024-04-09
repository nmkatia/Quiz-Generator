import logging 
import os 
from datetime import datetime  ## Its okay, it is working


### But what is the thought process here? 
### Why create this string int he first place ? 

LOG_FILE = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log" ### fuck it, this is just to add it to thepath later
#print(LOG_FILE) ### which is a string. 


## Now create what ? a path for a directroy ? 

log_path = os.path.join(os.getcwd(),"logs")
#print(log_path)

## First, you create the path, then you create the directory
dir = os.makedirs(log_path, exist_ok=True)


LOG_FILEPATH = os.path.join(log_path,LOG_FILE)
#print(LOG_FILEPATH)


logging.basicConfig(filename=LOG_FILEPATH, level=logging.INFO, format= "[%(asctime)s] : %(lineno)d : %(name)s : %(levelname)s : %(message)s")

