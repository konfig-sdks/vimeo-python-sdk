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

from vimeo_python_sdk.pydantic.webinar_event_metadata_connections_live_video import WebinarEventMetadataConnectionsLiveVideo
from vimeo_python_sdk.pydantic.webinar_event_metadata_connections_pictures import WebinarEventMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.webinar_event_metadata_connections_pre_live_video import WebinarEventMetadataConnectionsPreLiveVideo
from vimeo_python_sdk.pydantic.webinar_event_metadata_connections_team_member import WebinarEventMetadataConnectionsTeamMember
from vimeo_python_sdk.pydantic.webinar_event_metadata_connections_videos import WebinarEventMetadataConnectionsVideos

class WebinarEventMetadataConnections(BaseModel):
    live_video: WebinarEventMetadataConnectionsLiveVideo = Field(alias='live_video')

    pictures: WebinarEventMetadataConnectionsPictures = Field(alias='pictures')

    pre_live_video: WebinarEventMetadataConnectionsPreLiveVideo = Field(alias='pre_live_video')

    team_member: WebinarEventMetadataConnectionsTeamMember = Field(alias='team_member')

    videos: WebinarEventMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
