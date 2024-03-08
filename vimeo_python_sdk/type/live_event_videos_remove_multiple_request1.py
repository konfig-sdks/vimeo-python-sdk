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

from vimeo_python_sdk.type.live_event_videos_remove_multiple_request1_videos import LiveEventVideosRemoveMultipleRequest1Videos

class RequiredLiveEventVideosRemoveMultipleRequest1(TypedDict):
    pass

class OptionalLiveEventVideosRemoveMultipleRequest1(TypedDict, total=False):
    videos: LiveEventVideosRemoveMultipleRequest1Videos

class LiveEventVideosRemoveMultipleRequest1(RequiredLiveEventVideosRemoveMultipleRequest1, OptionalLiveEventVideosRemoveMultipleRequest1):
    pass
