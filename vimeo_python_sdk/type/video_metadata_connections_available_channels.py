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

from vimeo_python_sdk.type.video_metadata_connections_available_channels_options import VideoMetadataConnectionsAvailableChannelsOptions

class RequiredVideoMetadataConnectionsAvailableChannels(TypedDict):
    options: VideoMetadataConnectionsAvailableChannelsOptions

    # The total number of channels on this connection. This data requires a bearer token with the `private` scope.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data. This data requires a bearer token with the `private` scope.
    uri: str

class OptionalVideoMetadataConnectionsAvailableChannels(TypedDict, total=False):
    pass

class VideoMetadataConnectionsAvailableChannels(RequiredVideoMetadataConnectionsAvailableChannels, OptionalVideoMetadataConnectionsAvailableChannels):
    pass
