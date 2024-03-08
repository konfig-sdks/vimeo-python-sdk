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

from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_comments import OnDemandPageMetadataConnectionsMetadataConnectionsComments
from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_genres import OnDemandPageMetadataConnectionsMetadataConnectionsGenres
from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_likes import OnDemandPageMetadataConnectionsMetadataConnectionsLikes
from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_pictures import OnDemandPageMetadataConnectionsMetadataConnectionsPictures
from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_seasons import OnDemandPageMetadataConnectionsMetadataConnectionsSeasons
from vimeo_python_sdk.pydantic.on_demand_page_metadata_connections_metadata_connections_videos import OnDemandPageMetadataConnectionsMetadataConnectionsVideos

class OnDemandPageMetadataConnectionsMetadataConnections(BaseModel):
    comments: OnDemandPageMetadataConnectionsMetadataConnectionsComments = Field(alias='comments')

    genres: OnDemandPageMetadataConnectionsMetadataConnectionsGenres = Field(alias='genres')

    likes: OnDemandPageMetadataConnectionsMetadataConnectionsLikes = Field(alias='likes')

    pictures: OnDemandPageMetadataConnectionsMetadataConnectionsPictures = Field(alias='pictures')

    seasons: OnDemandPageMetadataConnectionsMetadataConnectionsSeasons = Field(alias='seasons')

    videos: OnDemandPageMetadataConnectionsMetadataConnectionsVideos = Field(alias='videos')
    class Config:
        arbitrary_types_allowed = True
