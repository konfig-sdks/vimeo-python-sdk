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

from vimeo_python_sdk.type.video_metadata_interactions_like_options import VideoMetadataInteractionsLikeOptions

class RequiredVideoMetadataInteractionsLike(TypedDict):
    # Whether the user has liked the video.
    added: bool

    # The time in ISO 8601 format when the user liked the video.
    added_time: str

    options: VideoMetadataInteractionsLikeOptions

    # Whether the user can access the video's number of likes.
    show_count: bool

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataInteractionsLike(TypedDict, total=False):
    pass

class VideoMetadataInteractionsLike(RequiredVideoMetadataInteractionsLike, OptionalVideoMetadataInteractionsLike):
    pass
