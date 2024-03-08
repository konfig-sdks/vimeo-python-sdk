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

from vimeo_python_sdk.type.channel_metadata_connections import ChannelMetadataConnections
from vimeo_python_sdk.type.channel_metadata_interactions import ChannelMetadataInteractions

class RequiredChannelMetadata(TypedDict):
    connections: ChannelMetadataConnections

    interactions: ChannelMetadataInteractions

class OptionalChannelMetadata(TypedDict, total=False):
    pass

class ChannelMetadata(RequiredChannelMetadata, OptionalChannelMetadata):
    pass
