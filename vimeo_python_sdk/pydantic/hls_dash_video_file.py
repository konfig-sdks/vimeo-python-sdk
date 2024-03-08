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


class HlsDashVideoFile(BaseModel):
    # The direct link to the video file.
    link: typing.Optional[str] = Field(alias='link')

    # The time in ISO 8601 format when the link to the video file expires.
    link_expiration_time: str = Field(alias='link_expiration_time')

    # The URL for logging events.
    log: typing.Optional[typing.Optional[str]] = Field(None, alias='log')
    class Config:
        arbitrary_types_allowed = True
