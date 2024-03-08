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

from vimeo_python_sdk.pydantic.channel_metadata_connections_privacy_users import ChannelMetadataConnectionsPrivacyUsers
from vimeo_python_sdk.pydantic.channel_metadata_connections_users import ChannelMetadataConnectionsUsers
from vimeo_python_sdk.pydantic.channel_metadata_connections_videos import ChannelMetadataConnectionsVideos

class ChannelMetadataConnections(BaseModel):
    privacy_users: ChannelMetadataConnectionsPrivacyUsers = Field(alias='privacy_users')

    users: ChannelMetadataConnectionsUsers = Field(alias='users')

    videos: ChannelMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
