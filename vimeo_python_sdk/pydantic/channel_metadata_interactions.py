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

from vimeo_python_sdk.pydantic.channel_metadata_interactions_add_moderators import ChannelMetadataInteractionsAddModerators
from vimeo_python_sdk.pydantic.channel_metadata_interactions_add_to import ChannelMetadataInteractionsAddTo
from vimeo_python_sdk.pydantic.channel_metadata_interactions_follow import ChannelMetadataInteractionsFollow
from vimeo_python_sdk.pydantic.channel_metadata_interactions_moderate_videos import ChannelMetadataInteractionsModerateVideos

class ChannelMetadataInteractions(BaseModel):
    add_moderators: ChannelMetadataInteractionsAddModerators = Field(alias='add_moderators')

    add_to: ChannelMetadataInteractionsAddTo = Field(alias='add_to')

    follow: ChannelMetadataInteractionsFollow = Field(alias='follow')

    moderate_videos: ChannelMetadataInteractionsModerateVideos = Field(alias='moderate_videos')
    class Config:
        arbitrary_types_allowed = True
