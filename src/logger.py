import logging 
import os 
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

log_dirs = os.path.join(os.getcwd(),"logs")
os.makedirs(log_dirs,exist_ok=True)

LOG_FILE_PATH = os.path.join(log_dirs,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
)

if __name__ == "__main__":
    logging.info("Logging has started")