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

from vimeo_python_sdk.type.channel_metadata_connections_privacy_users import ChannelMetadataConnectionsPrivacyUsers
from vimeo_python_sdk.type.channel_metadata_connections_users import ChannelMetadataConnectionsUsers
from vimeo_python_sdk.type.channel_metadata_connections_videos import ChannelMetadataConnectionsVideos

class RequiredChannelMetadataConnections(TypedDict):
    privacy_users: ChannelMetadataConnectionsPrivacyUsers

    users: ChannelMetadataConnectionsUsers

    videos: ChannelMetadataConnectionsVideos

class OptionalChannelMetadataConnections(TypedDict, total=False):
    pass

class ChannelMetadataConnections(RequiredChannelMetadataConnections, OptionalChannelMetadataConnections):
    pass
