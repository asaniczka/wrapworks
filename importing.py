"""
Functions that help with importing
"""

import os
import sys
import dotenv


def load_env_cwd():

    sys.path.append(os.getcwd())
    dotenv.load_dotenv()
