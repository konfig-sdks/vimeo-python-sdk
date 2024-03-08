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


class RequiredVideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimelineItem(TypedDict):
    # The 360 director timeline pitch. This value must be between `−90` and `90`, and it's required only when **spatial.director_timeline** is defined.
    pitch: typing.Union[int, float]

    # The 360 director timeline time code. This field is required only when **spatial.director_timeline** is defined.
    time_code: typing.Union[int, float]

    # The 360 director timeline yaw. This value must be between `0` and `360`, and it's required only when **spatial.director_timeline** is defined.
    yaw: typing.Union[int, float]

class OptionalVideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimelineItem(TypedDict, total=False):
    # The 360 director timeline roll.
    roll: typing.Union[int, float]

class VideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimelineItem(RequiredVideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimelineItem, OptionalVideosUploadsBeginVideoUploadProcessRequestSpatialDirectorTimelineItem):
    pass
