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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.video_metadata_connections_versions_options import VideoMetadataConnectionsVersionsOptions

class VideoMetadataConnectionsVersions(BaseModel):
    # Whether the video has interactive capability.
    has_interactive: bool = Field(alias='has_interactive')

    options: VideoMetadataConnectionsVersionsOptions = Field(alias='options')

    # Whether the video has unified resolution. If the value of this field is `false`, the video requires transcoding.
    origin_variable_frame_resolution: bool = Field(alias='origin_variable_frame_resolution')

    # The total number of versions on this connection.
    total: typing.Union[int, float] = Field(alias='total')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')

    # The URI of the current version of the video.
    current_uri: typing.Optional[str] = Field(None, alias='current_uri')

    # The resource key string of the current version of the video.
    resource_key: typing.Optional[str] = Field(None, alias='resource_key')
    class Config:
        arbitrary_types_allowed = True
