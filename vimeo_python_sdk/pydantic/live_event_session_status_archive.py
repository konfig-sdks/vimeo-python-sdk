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


class LiveEventSessionStatusArchive(BaseModel):
    # The ID of the archived video.
    clip_id: typing.Union[int, float] = Field(alias='clip_id')

    # The status of the archive data.
    status: typing.Optional[typing.Union[int, float]] = Field(alias='status')
    class Config:
        arbitrary_types_allowed = True
