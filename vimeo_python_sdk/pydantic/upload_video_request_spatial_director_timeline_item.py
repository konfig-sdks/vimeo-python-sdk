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


class UploadVideoRequestSpatialDirectorTimelineItem(BaseModel):
    # The 360 director timeline pitch. This value must be between `−90` and `90`, and it's required only when **spatial.director_timeline** is defined.
    pitch: typing.Union[int, float] = Field(alias='pitch')

    # The 360 director timeline time code. This field is required only when **spatial.director_timeline** is defined.
    time_code: typing.Union[int, float] = Field(alias='time_code')

    # The 360 director timeline yaw. This value must be between `0` and `360`, and it's required only when **spatial.director_timeline** is defined.
    yaw: typing.Union[int, float] = Field(alias='yaw')

    # The 360 director timeline roll.
    roll: typing.Optional[typing.Union[int, float]] = Field(None, alias='roll')
    class Config:
        arbitrary_types_allowed = True
