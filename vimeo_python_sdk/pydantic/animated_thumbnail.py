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


class AnimatedThumbnail(BaseModel):
    # The duration of the animated thumbnail in seconds.
    duration: typing.Union[int, float] = Field(alias='duration')

    # The file format of the animated thumbnail.
    file_format: str = Field(alias='file_format')

    # The file size of the animated thumbnail in bytes.
    file_size: typing.Union[int, float] = Field(alias='file_size')

    # The height of the animated thumbnail in pixels.
    height: typing.Union[int, float] = Field(alias='height')

    # Whether the animated thumbnail can be downloaded.
    is_downloadable: bool = Field(alias='is_downloadable')

    # The URL of the animated thumbnail file.
    link: str = Field(alias='link')

    # The URL of the animated thumbnail file with a play button overlay.
    link_with_play_button: str = Field(alias='link_with_play_button')

    # The profile ID of the animated thumbnail.
    profile_id: str = Field(alias='profile_id')

    # The time in the video, in seconds, corresponding to the start of the animation.
    start_time: typing.Union[int, float] = Field(alias='start_time')

    # The ID of the animated thumbnail.
    uuid: str = Field(alias='uuid')

    # The width of the animated thumbnail in pixels.
    width: typing.Union[int, float] = Field(alias='width')
    class Config:
        arbitrary_types_allowed = True
