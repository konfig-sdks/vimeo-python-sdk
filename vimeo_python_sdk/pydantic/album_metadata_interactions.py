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

from vimeo_python_sdk.pydantic.album_metadata_interactions_add_custom_thumbnails import AlbumMetadataInteractionsAddCustomThumbnails
from vimeo_python_sdk.pydantic.album_metadata_interactions_add_live_events import AlbumMetadataInteractionsAddLiveEvents
from vimeo_python_sdk.pydantic.album_metadata_interactions_add_logos import AlbumMetadataInteractionsAddLogos
from vimeo_python_sdk.pydantic.album_metadata_interactions_add_to import AlbumMetadataInteractionsAddTo
from vimeo_python_sdk.pydantic.album_metadata_interactions_add_videos import AlbumMetadataInteractionsAddVideos

class AlbumMetadataInteractions(BaseModel):
    add_custom_thumbnails: AlbumMetadataInteractionsAddCustomThumbnails = Field(alias='add_custom_thumbnails')

    add_live_events: AlbumMetadataInteractionsAddLiveEvents = Field(alias='add_live_events')

    add_logos: AlbumMetadataInteractionsAddLogos = Field(alias='add_logos')

    add_to: AlbumMetadataInteractionsAddTo = Field(alias='add_to')

    add_videos: AlbumMetadataInteractionsAddVideos = Field(alias='add_videos')
    class Config:
        arbitrary_types_allowed = True
