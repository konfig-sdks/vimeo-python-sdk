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

from vimeo_python_sdk.pydantic.video_metadata_interactions_watchlater_options import VideoMetadataInteractionsWatchlaterOptions

class VideoMetadataInteractionsWatchlater(BaseModel):
    # Whether the user has added the video to their Watch Later list.
    added: bool = Field(alias='added')

    # The time in ISO 8601 format when the user added the video to their Watch Later list.
    added_time: str = Field(alias='added_time')

    options: VideoMetadataInteractionsWatchlaterOptions = Field(alias='options')

    # The API URI that resolves to the connection data.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
