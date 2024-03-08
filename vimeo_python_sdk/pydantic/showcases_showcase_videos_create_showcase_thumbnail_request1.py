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


class ShowcasesShowcaseVideosCreateShowcaseThumbnailRequest1(BaseModel):
    # The time in seconds of the video frame to use as the thumbnail image.
    time_code: typing.Optional[typing.Union[int, float]] = Field(None, alias='time_code')
    class Config:
        arbitrary_types_allowed = True
