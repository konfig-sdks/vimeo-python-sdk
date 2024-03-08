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


class RequiredLiveEventActivationCreateRtmpLinksRequest(TypedDict):
    pass

class OptionalLiveEventActivationCreateRtmpLinksRequest(TypedDict, total=False):
    # Whether the stream activates from the cloud composer. _This field is deprecated._
    cloud_composing_streaming: bool

    # Whether the stream activates from the cloud composer.
    streaming_start_requested: bool

class LiveEventActivationCreateRtmpLinksRequest(RequiredLiveEventActivationCreateRtmpLinksRequest, OptionalLiveEventActivationCreateRtmpLinksRequest):
    pass
