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


class RequiredPresetSettingsLogos(TypedDict):
    # Whether the preset includes custom logo settings.
    custom: bool

    # Whether the present includes sticky custom logo settings.
    sticky_custom: bool

    # Whether the preset includes Vimeo logo settings.
    vimeo: bool

class OptionalPresetSettingsLogos(TypedDict, total=False):
    pass

class PresetSettingsLogos(RequiredPresetSettingsLogos, OptionalPresetSettingsLogos):
    pass
