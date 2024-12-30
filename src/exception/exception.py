import os 
import sys 
from src.logger.logger import logging


class CustomException(Exception):
    def __init__(self,error_message,error_detals:sys):
        self.error_message = error_message
        _,_,exc_tb = error_detals.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error occures in python script [{0}] in line number [{1}] error_message [{2}]".format(
            self.filename,self.lineno,str(self.error_message)
        )
    

if __name__ == "__main__":
    try :
        logging.info("custom exception code ")
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys)
    
        
    
    