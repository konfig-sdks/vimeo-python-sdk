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

from vimeo_python_sdk.pydantic.trimmed_video_metadata_connections_created_version import TrimmedVideoMetadataConnectionsCreatedVersion
from vimeo_python_sdk.pydantic.trimmed_video_metadata_connections_root_version import TrimmedVideoMetadataConnectionsRootVersion
from vimeo_python_sdk.pydantic.trimmed_video_metadata_connections_video import TrimmedVideoMetadataConnectionsVideo

class TrimmedVideoMetadataConnections(BaseModel):
    created_version: TrimmedVideoMetadataConnectionsCreatedVersion = Field(alias='created_version')

    root_version: TrimmedVideoMetadataConnectionsRootVersion = Field(alias='root_version')

    video: TrimmedVideoMetadataConnectionsVideo = Field(alias='video')
    class Config:
        arbitrary_types_allowed = True
