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


class ChannelsVideosAddMultipleToChannelRequest(BaseModel):
    # A member of an array representing the URIs of the videos to add. For each member in the array, use the format `{\"video_uri\":\"x\"}` where **x** is a video URI. For more information on batch requests like this, see [Using Common Formats and Parameters](https://developer.vimeo.com/api/common-formats#working-with-batch-requests).
    video_uri: str = Field(alias='video_uri')
    class Config:
        arbitrary_types_allowed = True
