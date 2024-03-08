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

from vimeo_python_sdk.pydantic.live_event_metadata_connections_live_video import LiveEventMetadataConnectionsLiveVideo
from vimeo_python_sdk.pydantic.live_event_metadata_connections_pictures import LiveEventMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.live_event_metadata_connections_pre_live_video import LiveEventMetadataConnectionsPreLiveVideo
from vimeo_python_sdk.pydantic.live_event_metadata_connections_team_member import LiveEventMetadataConnectionsTeamMember
from vimeo_python_sdk.pydantic.live_event_metadata_connections_videos import LiveEventMetadataConnectionsVideos

class LiveEventMetadataConnections(BaseModel):
    live_video: LiveEventMetadataConnectionsLiveVideo = Field(alias='live_video')

    pictures: LiveEventMetadataConnectionsPictures = Field(alias='pictures')

    pre_live_video: LiveEventMetadataConnectionsPreLiveVideo = Field(alias='pre_live_video')

    team_member: LiveEventMetadataConnectionsTeamMember = Field(alias='team_member')

    videos: LiveEventMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
