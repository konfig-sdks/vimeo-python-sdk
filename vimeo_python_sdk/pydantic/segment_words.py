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


class SegmentWords(BaseModel):
    # The end time of the word in milliseconds.
    end_time: typing.Optional[typing.Union[int, float]] = Field(alias='end_time')

    # The start time of the word in milliseconds.
    start_time: typing.Optional[typing.Union[int, float]] = Field(alias='start_time')

    # The word text.
    word: str = Field(alias='word')
    class Config:
        arbitrary_types_allowed = True
