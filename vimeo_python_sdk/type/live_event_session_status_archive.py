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


class RequiredLiveEventSessionStatusArchive(TypedDict):
    # The ID of the archived video.
    clip_id: typing.Union[int, float]

    # The status of the archive data.
    status: typing.Optional[typing.Union[int, float]]

class OptionalLiveEventSessionStatusArchive(TypedDict, total=False):
    pass

class LiveEventSessionStatusArchive(RequiredLiveEventSessionStatusArchive, OptionalLiveEventSessionStatusArchive):
    pass
