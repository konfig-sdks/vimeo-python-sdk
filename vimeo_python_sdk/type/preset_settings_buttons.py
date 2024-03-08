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


class RequiredPresetSettingsButtons(TypedDict):
    # Whether the preset includes `Embed` button settings.
    embed: bool

    # Whether the preset includes `Fullscreen` button settings.
    fullscreen: bool

    # Whether the preset includes `HD` button settings.
    hd: bool

    # Whether the preset includes `Like` button settings.
    like: bool

    # Whether the preset includes `Reaction` button settings.
    reaction: typing.Optional[bool]

    # Whether the present includes `Share` button settings.
    share: bool

    # Whether the preset includes `Vote` button settings.
    vote: bool

    # Whether the preset includes `Watch Later` button settings.
    watchlater: bool

class OptionalPresetSettingsButtons(TypedDict, total=False):
    pass

class PresetSettingsButtons(RequiredPresetSettingsButtons, OptionalPresetSettingsButtons):
    pass
