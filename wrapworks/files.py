"""
All helpers that deal with importing and exporting
"""

from typing import Any

import json
import pickle


def dump_json(path, data: dict):

    with open(path, "w", encoding="utf-8") as wf:
        json.dump(data, wf, default=str)


def load_json(path) -> dict:

    with open(path, "r", encoding="utf-8") as rf:
        data = json.load(rf)
        return data
