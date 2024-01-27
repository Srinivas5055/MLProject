import sys
import logging

def error_message(msg,sys):
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = 'This is the error in python file name [{0}] from line no [{1}] error message [{2}]'.format(
        file_name,
        exc_tb.tb_lineno,
        str(msg)
    )
    return error_message    

class CustomException(Exception):
    def __init__(self,msg,sys):
        super().__init__(msg)
        self.msg = error_message(msg,sys)

    def __str__(self):
        return self.msg

