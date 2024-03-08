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


class RequiredVersionTranscodeStatus(TypedDict):
    # Whether the video has finished transcoding.
    is_complete: bool

    # Whether the video is playable in all resolutions, up to either the source quality or 4K, whichever is lower, at standard definition.
    is_fully_playable: bool

    # Whether the video is playable.
    is_playable: bool

class OptionalVersionTranscodeStatus(TypedDict, total=False):
    pass

class VersionTranscodeStatus(RequiredVersionTranscodeStatus, OptionalVersionTranscodeStatus):
    pass
