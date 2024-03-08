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

from vimeo_python_sdk.type.video_metadata_connections_season_options import VideoMetadataConnectionsSeasonOptions

class RequiredVideoMetadataConnectionsSeason(TypedDict):
    # The name of the season.
    name: str

    options: VideoMetadataConnectionsSeasonOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataConnectionsSeason(TypedDict, total=False):
    pass

class VideoMetadataConnectionsSeason(RequiredVideoMetadataConnectionsSeason, OptionalVideoMetadataConnectionsSeason):
    pass
