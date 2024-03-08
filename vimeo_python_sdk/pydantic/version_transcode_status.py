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


class VersionTranscodeStatus(BaseModel):
    # Whether the video has finished transcoding.
    is_complete: bool = Field(alias='is_complete')

    # Whether the video is playable in all resolutions, up to either the source quality or 4K, whichever is lower, at standard definition.
    is_fully_playable: bool = Field(alias='is_fully_playable')

    # Whether the video is playable.
    is_playable: bool = Field(alias='is_playable')
    class Config:
        arbitrary_types_allowed = True
