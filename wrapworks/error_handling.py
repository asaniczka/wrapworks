"""
Contains helpers related to error handling
"""

from typing import Callable
import traceback

from rich import print


def eprint(e: Exception, func: Callable, no_tracebacks: bool = True):
    """
    Prints an error with traceback and type

    ## Args:
    - `e` : The exception
    - `func` : The funcation callable
    - `no_tracebacks`: Whether to include traceback
    """
    print(f"Error on '{func.__name__}'. {type(e).__name__} - {e}.")
    if not no_tracebacks:
        traceback.print_tb(e.__traceback__, limit=5)
