import sys
import logging 
from src.logger import logging
def error_message_detail(error, error_detail:sys):
    exc_type,exc_obj,exc_tb = error_detail.exc_info()
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"Error occured in script:[{file_name}] at line {line_number} with message {str(error)}"
    else:
        return f"Error without traceback[{str(error)}]"
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_detail)
        self.error_message = error_message_detail(error_message,error_detail = error_detail)
        logging.error(self.error_message)

    def __str__(self):
        return self.error_message
    

if __name__ == "__main__":
    try:
        a = 1 / 0
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)

