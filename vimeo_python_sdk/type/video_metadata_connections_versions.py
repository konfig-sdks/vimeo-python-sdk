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

from vimeo_python_sdk.type.video_metadata_connections_versions_options import VideoMetadataConnectionsVersionsOptions

class RequiredVideoMetadataConnectionsVersions(TypedDict):
    # Whether the video has interactive capability.
    has_interactive: bool

    options: VideoMetadataConnectionsVersionsOptions

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool

    # The total number of versions on this connection.
    total: typing.Union[int, float]

    # The API URI that resolves to the connection data.
    uri: str

class OptionalVideoMetadataConnectionsVersions(TypedDict, total=False):
    # The URI of the current version of the video.
    current_uri: str

    # The resource key string of the current version of the video.
    resource_key: str

class VideoMetadataConnectionsVersions(RequiredVideoMetadataConnectionsVersions, OptionalVideoMetadataConnectionsVersions):
    pass
