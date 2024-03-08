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


class RequiredVideoMetadataInteractionsSubscribe(TypedDict):
    pass

class OptionalVideoMetadataInteractionsSubscribe(TypedDict, total=False):
    # Whether the On Demand video has DRM.
    drm: bool

    # The time in ISO 8601 format when the subscription expires.
    expires_time: str

    # The time in ISO 8601 format when the subscription was purchased.
    purchase_time: str

    # The stream type.
    stream: str

class VideoMetadataInteractionsSubscribe(RequiredVideoMetadataInteractionsSubscribe, OptionalVideoMetadataInteractionsSubscribe):
    pass
