from typing import Any

import pydash as py_


def hide_nulls(mongo_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Hide null attributes from mongo dict.

    :param mongo_dict: The mongo dict to clean
    :return: The mongo dict clean
    """
    return {k: v for k, v in mongo_dict.items() if v is not None}


def hide_privates(mongo_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Hide private attributes from mongo dict.

    :param mongo_dict: The mongo dict to clean
    :return: The mongo dict clean
    """
    return {k: v for k, v in mongo_dict.items() if not k.startswith("_")}


def hide_empty_lists(mongo_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Hide empty lists from mongo dict.

    :param mongo_dict: The mongo dict to clean
    :return: The mongo dict clean
    """
    return {k: v for k, v in mongo_dict.items() if not isinstance(v, list) or len(v) != 0}


def clean_dict(mongo_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Clean mongo dict.

    :param mongo_dict: The mongo dict to clean
    :return: The mongo dict clean
    """
    if not mongo_dict or len(mongo_dict) == 0:
        return {}

    mongo_dict_clean: dict[str, Any] = py_.flow(
        hide_nulls,
        hide_privates,
        hide_empty_lists,
    )(mongo_dict)
    return mongo_dict_clean
