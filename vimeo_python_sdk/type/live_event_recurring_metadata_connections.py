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

from vimeo_python_sdk.type.live_event_recurring_metadata_connections_live_video import LiveEventRecurringMetadataConnectionsLiveVideo
from vimeo_python_sdk.type.live_event_recurring_metadata_connections_pictures import LiveEventRecurringMetadataConnectionsPictures
from vimeo_python_sdk.type.live_event_recurring_metadata_connections_pre_live_video import LiveEventRecurringMetadataConnectionsPreLiveVideo
from vimeo_python_sdk.type.live_event_recurring_metadata_connections_team_member import LiveEventRecurringMetadataConnectionsTeamMember
from vimeo_python_sdk.type.live_event_recurring_metadata_connections_videos import LiveEventRecurringMetadataConnectionsVideos

class RequiredLiveEventRecurringMetadataConnections(TypedDict):
    live_video: LiveEventRecurringMetadataConnectionsLiveVideo

    pictures: LiveEventRecurringMetadataConnectionsPictures

    pre_live_video: LiveEventRecurringMetadataConnectionsPreLiveVideo

    team_member: LiveEventRecurringMetadataConnectionsTeamMember

    videos: LiveEventRecurringMetadataConnectionsVideos

class OptionalLiveEventRecurringMetadataConnections(TypedDict, total=False):
    pass

class LiveEventRecurringMetadataConnections(RequiredLiveEventRecurringMetadataConnections, OptionalLiveEventRecurringMetadataConnections):
    pass
