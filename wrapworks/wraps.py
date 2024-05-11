"""
For now, this contains all the wrappers
"""

from functools import wraps
from typing import Any
import time

from rich import print


def timeit():
    """Prints the execution duration of the function"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_duration = end_time - start_time
            print(f"'{func.__name__}' took {total_duration} seconds to execute")
            return result

        return wrapper

    return decorator


def add_try_except(default_return: Any = None):
    """Adds a try except block around the function saving to a bunch of keystrokes"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                print( f"An exception occurred in function '{func.__name__}': {type(e).__name__} - {e}")  # fmt:skip
                return default_return
            return result

        return wrapper

    return decorator


def retry_on_exception(max_retries=5, delay=1, default_return: Any = None):
    """Automatically retry the function"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print( f"An exception occurred in function '{func.__name__}': {type(e).__name__} - {e}")  # fmt:skip
                    retries += 1
                    time.sleep(delay)
                    continue
            print( f"Function '{func.__name__}' failed to execute succesfully even after {retries} retries")  # fmt:skip
            return default_return

        return wrapper

    return decorator
