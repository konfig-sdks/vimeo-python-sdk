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


class VideoSpatialDirectorTimelineItem(BaseModel):
    # The timeline pitch value, ranging from a minimum of `-90` to a maximum of `90`.
    pitch: typing.Optional[typing.Union[int, float]] = Field(None, alias='pitch')

    # The timeline roll value.
    roll: typing.Optional[typing.Union[int, float]] = Field(None, alias='roll')

    # The timeline time code.
    time_code: typing.Optional[typing.Union[int, float]] = Field(None, alias='time_code')

    # The timeline yaw value, ranging from a minimum of `0` to a maximum of `360`.
    yaw: typing.Optional[typing.Union[int, float]] = Field(None, alias='yaw')
    class Config:
        arbitrary_types_allowed = True
