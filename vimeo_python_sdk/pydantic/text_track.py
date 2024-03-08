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


class TextTrack(BaseModel):
    # Whether the text track is active.
    active: bool = Field(alias='active')

    # The name of the language.
    display_language: str = Field(alias='display_language')

    # The read-only URL of the text track file, intended for use with HLS playback.
    hls_link: str = Field(alias='hls_link')

    # The time in ISO 8601 format when the read-only HLS playback text track file expires.
    hls_link_expires_time: str = Field(alias='hls_link_expires_time')

    # The text track identifier.
    id: typing.Union[int, float] = Field(alias='id')

    # The language code for the text track. To see a full list, request `/languages?filter=texttrack`.
    language: typing.Optional[str] = Field(alias='language')

    # The read-only URL of the text track file. You can upload to this link when you create it for the first time.
    link: str = Field(alias='link')

    # The time in ISO 8601 format when the text track link expires.
    link_expires_time: str = Field(alias='link_expires_time')

    # The descriptive name of the text track.
    name: typing.Optional[str] = Field(alias='name')

    # The type of text track.  Option descriptions:  * `captions` - The text track is for captions.  * `subtitles` - The text track is for subtitles. 
    type: Literal["captions", "subtitles"] = Field(alias='type')

    # The relative URI of the text track.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
