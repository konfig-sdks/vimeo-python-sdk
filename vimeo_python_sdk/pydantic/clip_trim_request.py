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


class ClipTrimRequest(BaseModel):
    # The end position in seconds of the trim in the video.
    trim_end: typing.Optional[str] = Field(None, alias='trim_end')

    # The start position in seconds of the trim in the video.
    trim_start: typing.Optional[str] = Field(None, alias='trim_start')
    class Config:
        arbitrary_types_allowed = True
