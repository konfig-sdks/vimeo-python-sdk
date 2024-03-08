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

from vimeo_python_sdk.type.category_metadata_connections_channels import CategoryMetadataConnectionsChannels
from vimeo_python_sdk.type.category_metadata_connections_groups import CategoryMetadataConnectionsGroups
from vimeo_python_sdk.type.category_metadata_connections_users import CategoryMetadataConnectionsUsers
from vimeo_python_sdk.type.category_metadata_connections_videos import CategoryMetadataConnectionsVideos

class RequiredCategoryMetadataConnections(TypedDict):
    channels: CategoryMetadataConnectionsChannels

    groups: CategoryMetadataConnectionsGroups

    users: CategoryMetadataConnectionsUsers

    videos: CategoryMetadataConnectionsVideos

class OptionalCategoryMetadataConnections(TypedDict, total=False):
    pass

class CategoryMetadataConnections(RequiredCategoryMetadataConnections, OptionalCategoryMetadataConnections):
    pass
