import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # name of the file

logs_path = os.path.join(
    os.getcwd(), "logs", LOG_FILE
)  ## path where save all the logs files
os.makedirs(logs_path, exist_ok=True)  ## make folder in which add log files


LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



