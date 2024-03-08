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

from vimeo_python_sdk.type.trimmed_video_metadata_connections_created_version import TrimmedVideoMetadataConnectionsCreatedVersion
from vimeo_python_sdk.type.trimmed_video_metadata_connections_root_version import TrimmedVideoMetadataConnectionsRootVersion
from vimeo_python_sdk.type.trimmed_video_metadata_connections_video import TrimmedVideoMetadataConnectionsVideo

class RequiredTrimmedVideoMetadataConnections(TypedDict):
    created_version: TrimmedVideoMetadataConnectionsCreatedVersion

    root_version: TrimmedVideoMetadataConnectionsRootVersion

    video: TrimmedVideoMetadataConnectionsVideo

class OptionalTrimmedVideoMetadataConnections(TypedDict, total=False):
    pass

class TrimmedVideoMetadataConnections(RequiredTrimmedVideoMetadataConnections, OptionalTrimmedVideoMetadataConnections):
    pass
