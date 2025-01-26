"""
Functions that help with importing
"""

import os
import sys


def cwdtoenv():
    """Adds current dir to system path and loads envs from dotenv"""

    sys.path.append(os.getcwd())
