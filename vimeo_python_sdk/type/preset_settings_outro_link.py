# coding: utf-8

"""
    Vimeo API

    Build something great. Vimeo's API supports flexible, high-quality video integration with your custom apps.

    The version of the OpenAPI document: 3.4
    Created by: https://developer.vimeo.com/help
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredPresetSettingsOutroLink(TypedDict):
    pass

class OptionalPresetSettingsOutroLink(TypedDict, total=False):
    # The name of the outro link.
    name: str

    # The URL of the outro link.
    url: str

class PresetSettingsOutroLink(RequiredPresetSettingsOutroLink, OptionalPresetSettingsOutroLink):
    pass
