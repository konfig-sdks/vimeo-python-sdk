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


class VideoStats(BaseModel):
    # The current total number of times that the video has been played.
    plays: typing.Optional[typing.Union[int, float]] = Field(alias='plays')
    class Config:
        arbitrary_types_allowed = True
