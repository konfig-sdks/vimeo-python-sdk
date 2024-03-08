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

from vimeo_python_sdk.pydantic.live_event_videos_add_multiple_videos_request_videos_item_video import LiveEventVideosAddMultipleVideosRequestVideosItemVideo

class LiveEventVideosAddMultipleVideosRequestVideosItem(BaseModel):
    video: typing.Optional[LiveEventVideosAddMultipleVideosRequestVideosItemVideo] = Field(None, alias='video')
    class Config:
        arbitrary_types_allowed = True
