# wrapworks

## Introduction

The `wrapworks` package provides decorators and helper functions for various functionalities such as timing function execution, handling exceptions, and automatic function retries.

## Installation

You can install `wrapworks` using pip:

```bash
pip install wrapworks
```

## Features

- `timeit`: Decorator to print the execution duration of a function.
- `tryexcept`: Decorator to add a try-except block around a function.
- `retry`: Decorator to automatically retry a function.

## Usage

### Timing Function Execution

```python
from wrapworks import timeit

@timeit()
def my_function():
    pass
```

### Handling Exceptions

```python
from wrapworks import tryexcept

@tryexcept(default_return=None)
def another_function():
    pass
```

### Automatic Function Retries

```python
from wrapworks import retry

@retry(max_retries=3, delay=1, default_return=None)
def some_function():
    pass

```

### Easy printing of exceptions

```python
from wrapworks import eprint

def some_function():
    try:
        raise ValueError()
    except Exception as e:
        eprint(e , some_function)

```

### Add current directory to system path and load environment variables

```python
from wrapworks import cwdtoenv
cwdtoenv()
```

## Customizing Output

You can customize the output behavior of the `wrapworks` decorators by specifying a `level` parameter when using them.

Additionally, you can further control the display of print statements based on the `WRAPWORKSLEVEL` environment variable as follows:

- If the `level` parameter in a decorator is higher than the `WRAPWORKSLEVEL` environment variable, the print statement from that decorator will be displayed.
- Set `WRAPWORKSLEVEL` to a specific level (e.g., `1`, `2`, `3`, etc.) to control which decorators' print statements are shown based on their respective levels.
- Print statements from decorators with a level lower than the `WRAPWORKSLEVEL` will be suppressed, providing a cleaner output in the console or log files.
