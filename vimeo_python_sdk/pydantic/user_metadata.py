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

from vimeo_python_sdk.pydantic.user_metadata_connections import UserMetadataConnections
from vimeo_python_sdk.pydantic.user_metadata_interactions import UserMetadataInteractions
from vimeo_python_sdk.pydantic.user_metadata_public_videos import UserMetadataPublicVideos

class UserMetadata(BaseModel):
    connections: UserMetadataConnections = Field(alias='connections')

    interactions: UserMetadataInteractions = Field(alias='interactions')

    public_videos: UserMetadataPublicVideos = Field(alias='public_videos')
    class Config:
        arbitrary_types_allowed = True
