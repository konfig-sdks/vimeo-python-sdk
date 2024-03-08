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

from vimeo_python_sdk.type.preset_settings_outro_link import PresetSettingsOutroLink

class RequiredPresetSettingsOutro(TypedDict):
    # The preset outro type.  Option descriptions:  * `link` - The outro includes a link.  * `no idea` - The outro type is `no idea`. The outro includes uploaded videos.  * `text` - The outro includes text.  * `uploaded_clips` - The outro includes uploaded videos.  * `uploaded_videos` - The outro includes uploaded videos. 
    type: str

class OptionalPresetSettingsOutro(TypedDict, total=False):
    # A comma-separated list of video URIs. This field appears only when **type** is `uploaded_clips`.
    clips: typing.Optional[str]

    link: PresetSettingsOutroLink

    # The outro text. This appears only when **type** is `text`.
    text: typing.Optional[str]

    # A comma-separated list of video URIs. This field appears only when **type** is `no idea`.
    videos: typing.Optional[str]

class PresetSettingsOutro(RequiredPresetSettingsOutro, OptionalPresetSettingsOutro):
    pass
