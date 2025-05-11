"""
All helpers that deal with importing and exporting
"""

from typing import Any

import json
import pickle


def dump_json(path: str, data: dict):

    assert isinstance(
        data, (dict, list)
    ), f"Expected data to be of type dict or list, got {type(data).__name__} instead!"

    with open(path, "w", encoding="utf-8") as wf:
        json.dump(data, wf, default=str)


def load_json(path) -> dict:

    with open(path, "r", encoding="utf-8") as rf:
        data = json.load(rf)
        return data


def dump_text(path: str, data: str):

    assert isinstance(
        data, str
    ), f"Expected data to be of type str, got {type(data).__name__} instead!"
    with open(path, "w", encoding="utf-8") as wf:
        wf.write(data)


def load_test(path: str) -> str:

    with open(path, "r", encoding="utf-8") as rf:
        return rf.read()
