"""
For now, this contains all the wrappers
"""

from functools import wraps
import os
from typing import Any
import time

from rich import print


def timeit(level: int = 1):
    """
    Prints the execution duration of the function.

    This is a decorator factory

    ## Args:
    - `level`: An arbitary int assigned to the wrapper. Use this combined with `WRAPWORKSLEVEL` env to control whether this wrapper uses print
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                print(f"'{func.__name__}' starting")  # fmt:skip
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                end_time = time.perf_counter()
                total_duration = end_time - start_time

                if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                    print(f"'{func.__name__}' took {total_duration} seconds to execute!")  # fmt:skip

        return wrapper

    return decorator


def tryexcept(default_return: Any = None, level: int = 1):
    """
    Adds a try except block around the function saving to a bunch of keystrokes.

    This is a decorator factory.

    ## Args:
    - `default_return`: What to return when the function fails
    - `level`: An arbitary int assigned to the wrapper. Use this combined with `WRAPWORKSLEVEL` env to control whether this wrapper uses print
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                    print( f"Exception in function '{func.__name__}': {type(e).__name__} - {e}")  # fmt:skip
                return default_return
            return result

        return wrapper

    return decorator


def retry(max_retries=5, delay=1, default_return: Any = None, level=1):
    """
    Automatically retry the function.

    This is a decorator factory.

    ## Args:
    - `max_retries`: Maximum number of retires
    - `delay`: Delay in seconds between retries
    - `default_return`: What to return when the function fails
    - `level`: An arbitary int assigned to the wrapper. Use this combined with `WRAPWORKSLEVEL` env to control whether this wrapper uses print
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                        print( f"Cxception in function '{func.__name__}': {type(e).__name__} - {e}")  # fmt:skip
                    retries += 1
                    time.sleep(delay)
                    continue
            if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                print( f"Function '{func.__name__}' failed to execute successfully even after {retries} retries")  # fmt:skip
            return default_return

        return wrapper

    return decorator


def debug(level: int = 1):
    """
    This wrapper prints the arguments and return values
    """

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            result_set = False
            start_time = time.perf_counter()
            if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                print(f"'{func.__name__}' starting")  # fmt:skip
                print("args=", args)
                print("kwargs=", kwargs)
            try:
                result = func(*args, **kwargs)
                result_set = True
                return result
            finally:
                end_time = time.perf_counter()
                total_duration = end_time - start_time

                if level >= int(os.getenv("WRAPWORKSLEVEL", "1")):
                    print(f"'{func.__name__}' took {total_duration} seconds to execute!")  # fmt:skip
                    if result_set:
                        print(result)

        return wrapper

    return decorator
