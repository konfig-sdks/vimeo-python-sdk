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


class VideosVersionsEditVideoVersionRequest(BaseModel):
    # A description of the video version. This description can make use of the full unicode character set.
    description: typing.Optional[str] = Field(None, alias='description')

    # Whether the video version is active.
    is_current: typing.Optional[bool] = Field(None, alias='is_current')
    class Config:
        arbitrary_types_allowed = True
