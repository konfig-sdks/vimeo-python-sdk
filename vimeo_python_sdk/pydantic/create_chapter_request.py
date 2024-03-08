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

from vimeo_python_sdk.pydantic.create_chapter_request_thumbnail_uris import CreateChapterRequestThumbnailUris

class CreateChapterRequest(BaseModel):
    # The title of the chapter.
    title: typing.Optional[typing.Optional[str]] = Field(None, alias='title')

    # The URI of the chapter's active thumbnail.
    active_thumbnail_uri: typing.Optional[str] = Field(None, alias='active_thumbnail_uri')

    thumbnail_uris: typing.Optional[CreateChapterRequestThumbnailUris] = Field(None, alias='thumbnail_uris')

    # The timecode of the chapter in seconds from the start of the video.
    timecode: typing.Optional[typing.Optional[typing.Union[int, float]]] = Field(None, alias='timecode')
    class Config:
        arbitrary_types_allowed = True
