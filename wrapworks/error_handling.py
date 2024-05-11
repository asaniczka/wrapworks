"""
Contains helpers related to error handling
"""

from typing import Any, Callable
import traceback

from rich import print


def eprint(e: Exception, func: Callable):
    """
    Prints an error with traceback and type
    """
    print(f"Error on '{func.__name__}'. {type(e).__name__} - {e}.")
    traceback.print_tb(e.__traceback__, limit=5)
