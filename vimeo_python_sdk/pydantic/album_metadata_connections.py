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

from vimeo_python_sdk.pydantic.album_metadata_connections_available_videos import AlbumMetadataConnectionsAvailableVideos
from vimeo_python_sdk.pydantic.album_metadata_connections_requested_clip import AlbumMetadataConnectionsRequestedClip
from vimeo_python_sdk.pydantic.album_metadata_connections_videos import AlbumMetadataConnectionsVideos

class AlbumMetadataConnections(BaseModel):
    available_videos: AlbumMetadataConnectionsAvailableVideos = Field(alias='available_videos')

    requested_clip: AlbumMetadataConnectionsRequestedClip = Field(alias='requested_clip')

    videos: AlbumMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
