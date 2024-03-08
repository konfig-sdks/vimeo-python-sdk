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


class RequiredVideosAnimatedThumbnailsCreateSetRequest(TypedDict):
    # The duration of the animation in seconds. The maximum value is 6.
    duration: typing.Union[int, float]

class OptionalVideosAnimatedThumbnailsCreateSetRequest(TypedDict, total=False):
    # The time in seconds corresponding to the start of the animation in the video. The default value is 0.
    start_time: typing.Union[int, float]

class VideosAnimatedThumbnailsCreateSetRequest(RequiredVideosAnimatedThumbnailsCreateSetRequest, OptionalVideosAnimatedThumbnailsCreateSetRequest):
    pass
