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

from vimeo_python_sdk.type.live_event_recurring_metadata_connections import LiveEventRecurringMetadataConnections
from vimeo_python_sdk.type.live_event_recurring_metadata_interactions import LiveEventRecurringMetadataInteractions

class RequiredLiveEventRecurringMetadata(TypedDict):
    connections: LiveEventRecurringMetadataConnections

    interactions: LiveEventRecurringMetadataInteractions

class OptionalLiveEventRecurringMetadata(TypedDict, total=False):
    pass

class LiveEventRecurringMetadata(RequiredLiveEventRecurringMetadata, OptionalLiveEventRecurringMetadata):
    pass
