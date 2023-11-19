from typing import Any
from enum import Enum
from strawberry import UNSET


def clean_input(obj) -> dict[str, Any]:
    if obj is None or obj == UNSET:
        return {}
    input_cleaned = {}

    obj_items = obj.items() if isinstance(obj, dict) else obj.__dict__.items()

    for key, value in obj_items:
        if value != UNSET:
            input_cleaned[key] = value

    return input_cleaned
