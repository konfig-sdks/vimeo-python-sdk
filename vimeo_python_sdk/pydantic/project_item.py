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

from vimeo_python_sdk.pydantic.live_event_recurring import LiveEventRecurring
from vimeo_python_sdk.pydantic.project import Project
from vimeo_python_sdk.pydantic.video import Video

class ProjectItem(BaseModel):
    # The project item type.  Option descriptions:  * `folder` - The project item is a folder.  * `live_event` - The project item is a live event.  * `video` - The project item is a video. 
    type: Literal["folder", "live_event", "video"] = Field(alias='type')

    # The project item folder.
    folder: typing.Optional[Project] = Field(None, alias='folder')

    # The project item live event.
    live_event: typing.Optional[LiveEventRecurring] = Field(None, alias='live_event')

    # The project item video.
    video: typing.Optional[Video] = Field(None, alias='video')
    class Config:
        arbitrary_types_allowed = True
