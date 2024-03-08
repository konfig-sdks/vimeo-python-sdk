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


class RequiredVideoSpatialDirectorTimelineItem(TypedDict):
    pass

class OptionalVideoSpatialDirectorTimelineItem(TypedDict, total=False):
    # The timeline pitch value, ranging from a minimum of `-90` to a maximum of `90`.
    pitch: typing.Union[int, float]

    # The timeline roll value.
    roll: typing.Union[int, float]

    # The timeline time code.
    time_code: typing.Union[int, float]

    # The timeline yaw value, ranging from a minimum of `0` to a maximum of `360`.
    yaw: typing.Union[int, float]

class VideoSpatialDirectorTimelineItem(RequiredVideoSpatialDirectorTimelineItem, OptionalVideoSpatialDirectorTimelineItem):
    pass
