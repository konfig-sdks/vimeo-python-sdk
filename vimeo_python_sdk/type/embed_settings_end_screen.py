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


class RequiredEmbedSettingsEndScreen(TypedDict):
    # How the embeddable player handles the end screen.  Option descriptions:  * `empty` - The end screen is empty.  * `loop` - The end screen loops the video playback.  * `share` - The end screen includes sharing options.  * `thumbnail` - The end screen includes the thumbnail of the video. 
    type: str

class OptionalEmbedSettingsEndScreen(TypedDict, total=False):
    pass

class EmbedSettingsEndScreen(RequiredEmbedSettingsEndScreen, OptionalEmbedSettingsEndScreen):
    pass
