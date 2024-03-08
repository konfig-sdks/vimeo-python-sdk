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

from vimeo_python_sdk.type.live_event_metadata_connections import LiveEventMetadataConnections
from vimeo_python_sdk.type.live_event_metadata_interactions import LiveEventMetadataInteractions

class RequiredLiveEventMetadata(TypedDict):
    connections: LiveEventMetadataConnections

    interactions: LiveEventMetadataInteractions

class OptionalLiveEventMetadata(TypedDict, total=False):
    pass

class LiveEventMetadata(RequiredLiveEventMetadata, OptionalLiveEventMetadata):
    pass
