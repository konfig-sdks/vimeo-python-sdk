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


class RequiredLiveEventLowLatencyToggleOptionRequest1(TypedDict):
    pass

class OptionalLiveEventLowLatencyToggleOptionRequest1(TypedDict, total=False):
    # Whether the event is low latency.
    low_latency: bool

class LiveEventLowLatencyToggleOptionRequest1(RequiredLiveEventLowLatencyToggleOptionRequest1, OptionalLiveEventLowLatencyToggleOptionRequest1):
    pass
