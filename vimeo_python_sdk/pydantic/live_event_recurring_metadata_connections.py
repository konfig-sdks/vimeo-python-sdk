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

from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_live_video import LiveEventRecurringMetadataConnectionsLiveVideo
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_pictures import LiveEventRecurringMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_pre_live_video import LiveEventRecurringMetadataConnectionsPreLiveVideo
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_team_member import LiveEventRecurringMetadataConnectionsTeamMember
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_connections_videos import LiveEventRecurringMetadataConnectionsVideos

class LiveEventRecurringMetadataConnections(BaseModel):
    live_video: LiveEventRecurringMetadataConnectionsLiveVideo = Field(alias='live_video')

    pictures: LiveEventRecurringMetadataConnectionsPictures = Field(alias='pictures')

    pre_live_video: LiveEventRecurringMetadataConnectionsPreLiveVideo = Field(alias='pre_live_video')

    team_member: LiveEventRecurringMetadataConnectionsTeamMember = Field(alias='team_member')

    videos: LiveEventRecurringMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
