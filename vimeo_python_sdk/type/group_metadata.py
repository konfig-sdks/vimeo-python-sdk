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

from vimeo_python_sdk.type.group_metadata_connections import GroupMetadataConnections
from vimeo_python_sdk.type.group_metadata_interactions import GroupMetadataInteractions

class RequiredGroupMetadata(TypedDict):
    connections: GroupMetadataConnections

    interactions: GroupMetadataInteractions

class OptionalGroupMetadata(TypedDict, total=False):
    pass

class GroupMetadata(RequiredGroupMetadata, OptionalGroupMetadata):
    pass
