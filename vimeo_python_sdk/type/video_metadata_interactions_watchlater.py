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

from vimeo_python_sdk.type.video_metadata_interactions_watchlater_options import VideoMetadataInteractionsWatchlaterOptions

class RequiredVideoMetadataInteractionsWatchlater(TypedDict):
    # Whether the user has added the video to their Watch Later list.
    added: bool

    # The time in ISO 8601 format when the user added the video to their Watch Later list.
    added_time: str

    options: VideoMetadataInteractionsWatchlaterOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsWatchlater(TypedDict, total=False):
    pass

class VideoMetadataInteractionsWatchlater(RequiredVideoMetadataInteractionsWatchlater, OptionalVideoMetadataInteractionsWatchlater):
    pass
