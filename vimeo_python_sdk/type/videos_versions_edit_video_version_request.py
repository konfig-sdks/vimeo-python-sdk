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


class RequiredVideosVersionsEditVideoVersionRequest(TypedDict):
    pass

class OptionalVideosVersionsEditVideoVersionRequest(TypedDict, total=False):
    # A description of the video version. This description can make use of the full unicode character set.
    description: str

    # Whether the video version is active.
    is_current: bool

class VideosVersionsEditVideoVersionRequest(RequiredVideosVersionsEditVideoVersionRequest, OptionalVideosVersionsEditVideoVersionRequest):
    pass
