"""Helpers functionalities."""
# flake8: noqa=E501, pylint: disable=C0301
import logging
import json

from typing import Any, Dict, List, Optional

LOGGER = logging.getLogger(__name__)


def load_settings(
    config_values: Dict[str, Any],
    config_keys: List[str]
):
    """
    Extract configurations from a given config dictionary.

    config_values: dict
        JSON Dump of the configuration file.

    config_keys: list
        List of configuration keys.

    """
    return [config_values.get(key, None) for key in config_keys]


def read_json(filename):
    """Read JSON file."""
    with open(filename, "r") as fp:
        return json.load(fp)
