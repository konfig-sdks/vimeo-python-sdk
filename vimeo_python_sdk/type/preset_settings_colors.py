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


class RequiredPresetSettingsColors(TypedDict):
    # The fourth player color, which controls the player background color.
    color_four: str

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color_one: str

    # The third player color, which controls the color of text and icons.
    color_three: str

    # The second player color, which controls the player accent color.
    color_two: str

class OptionalPresetSettingsColors(TypedDict, total=False):
    pass

class PresetSettingsColors(RequiredPresetSettingsColors, OptionalPresetSettingsColors):
    pass
