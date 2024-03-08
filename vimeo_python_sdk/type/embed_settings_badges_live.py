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


class RequiredEmbedSettingsBadgesLive(TypedDict):
    # Whether the video was streamed live.
    archived: bool

    # Whether the video is currently streaming live.
    streaming: bool

class OptionalEmbedSettingsBadgesLive(TypedDict, total=False):
    pass

class EmbedSettingsBadgesLive(RequiredEmbedSettingsBadgesLive, OptionalEmbedSettingsBadgesLive):
    pass
