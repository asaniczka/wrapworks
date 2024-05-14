"""
All helpers that deal with importing and exporting
"""

from typing import Any

import json
import pickle


def dump_json(path, data: dict):

    with open(path, "w", encoding="utf-8") as wf:
        json.dump(data, wf, default=str)


def load_json(path, data: dict):

    with open(path, "r", encoding="utf-8") as rf:
        data = json.load(rf)
        return data


def dump_pickle(path, data: Any):

    with open(path, "w") as wf:
        pickle.dump(
            data,
            wf,
        )


def load_pickle(path, data: Any):

    with open(path, "r") as rf:
        data = pickle.load(rf)
        return data
