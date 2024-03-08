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

from vimeo_python_sdk.type.live_event_recurring import LiveEventRecurring
from vimeo_python_sdk.type.project import Project
from vimeo_python_sdk.type.video import Video

class RequiredProjectItem(TypedDict):
    # The project item type.  Option descriptions:  * `folder` - The project item is a folder.  * `live_event` - The project item is a live event.  * `video` - The project item is a video. 
    type: str

class OptionalProjectItem(TypedDict, total=False):
    # The project item folder.
    folder: Project

    # The project item live event.
    live_event: LiveEventRecurring

    # The project item video.
    video: Video

class ProjectItem(RequiredProjectItem, OptionalProjectItem):
    pass
