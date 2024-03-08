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

from vimeo_python_sdk.pydantic.picture import Picture

class Chapter(BaseModel):
    # The title of the chapter.
    title: typing.Optional[str] = Field(alias='title')

    # The thumbnails associated with the video chapter.
    thumbnails: typing.List[Picture] = Field(alias='thumbnails')

    # The timecode of the chapter in seconds from the start of the video.
    timecode: typing.Optional[typing.Union[int, float]] = Field(alias='timecode')

    # The relative URI of the chapter.
    uri: str = Field(alias='uri')

    # The URI of the active thumbnail.
    active_thumbnail_uri: typing.Optional[str] = Field(None, alias='active_thumbnail_uri')
    class Config:
        arbitrary_types_allowed = True
