import logging 
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y,%H,%M,%S')}.log" #This helps to watch at which time your pipeline is executed

# Saving logs

log_path = os.path.join(os.getcwd(),"logs") #folder along with the path
os.makedirs(log_path,exist_ok=True) #creating that particular folder

LOG_FILEPATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    filename = LOG_FILEPATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)