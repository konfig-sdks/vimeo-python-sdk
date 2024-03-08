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


class VideoVersionTranscode(BaseModel):
    # The status code for the availability of the video version.  Option descriptions:  * `complete` - Transcoding is complete. The video version is available.  * `error` - There was a transcoding error. The video version isn't available.  * `in_progress` - Transcoding is in progress. The video version isn't available yet. 
    status: typing.Optional[Literal["complete", "error", "in_progress"]] = Field(None, alias='status')
    class Config:
        arbitrary_types_allowed = True
