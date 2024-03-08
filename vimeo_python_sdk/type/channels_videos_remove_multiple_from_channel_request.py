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


class RequiredChannelsVideosRemoveMultipleFromChannelRequest(TypedDict):
    # The URI of a video to remove.
    video_uri: str

class OptionalChannelsVideosRemoveMultipleFromChannelRequest(TypedDict, total=False):
    pass

class ChannelsVideosRemoveMultipleFromChannelRequest(RequiredChannelsVideosRemoveMultipleFromChannelRequest, OptionalChannelsVideosRemoveMultipleFromChannelRequest):
    pass
