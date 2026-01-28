import sys
from types import TracebackType
from typing import Optional, Tuple
import logging
from src.logger import logging


def error_message_detail(
    error: Exception,
    error_detail: Tuple[Optional[type],
        Optional[BaseException],
        Optional[TracebackType]]
) -> str:

    _, _, exc_tb = error_detail

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown File"
        line_number = "Unknown Line"

    error_message = (
        f"Error occurred in python script [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{str(error)}]"
    )

    return error_message


class CustomException(Exception):

    def __init__(
        self,
        error,
        error_detail: Tuple[Optional[type],
        Optional[BaseException],
        Optional[TracebackType]]
    ):
        super().__init__(error)

        self.error_message = error_message_detail(error, error_detail)

    def __str__(self) -> str:
        return self.error_message



if __name__ == "__main__":
    try:
        a = 1 / 0

    except Exception as e:

        logging.info("Divided by Zero")

        # Properly raise custom exception
        raise CustomException(e, sys.exc_info())