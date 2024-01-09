"""Configuration file for ada."""
# flake8: noqa=B006, E501, pylint: disable=C0301, W0101, W0102, W4901
import logging
import os
from os.path import abspath, dirname, join
from typing import Dict, List

from ada.utils.helpers import load_settings, read_json

LOGGER = logging.getLogger(__name__)

SAMPLE_PATH: str = abspath(join(dirname(__file__), "./"))

TELEGRAM, DISCORD = load_settings(
    config_values=read_json(f"{SAMPLE_PATH}/settings.json"),
    config_keys=["telegram", "discord"]
)
