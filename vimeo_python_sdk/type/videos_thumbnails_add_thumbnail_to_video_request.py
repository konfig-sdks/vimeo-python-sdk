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


class RequiredVideosThumbnailsAddThumbnailToVideoRequest(TypedDict):
    pass

class OptionalVideosThumbnailsAddThumbnailToVideoRequest(TypedDict, total=False):
    # Whether the image created by the **time** field should be the default thumbnail for the video.
    active: bool

    # The time offset in seconds from which to create the thumbnail.
    time: typing.Union[int, float]

class VideosThumbnailsAddThumbnailToVideoRequest(RequiredVideosThumbnailsAddThumbnailToVideoRequest, OptionalVideosThumbnailsAddThumbnailToVideoRequest):
    pass
