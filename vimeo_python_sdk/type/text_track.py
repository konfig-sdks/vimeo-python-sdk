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


class RequiredTextTrack(TypedDict):
    # Whether the text track is active.
    active: bool

    # The name of the language.
    display_language: str

    # The read-only URL of the text track file, intended for use with HLS playback.
    hls_link: str

    # The time in ISO 8601 format when the read-only HLS playback text track file expires.
    hls_link_expires_time: str

    # The text track identifier.
    id: typing.Union[int, float]

    # The language code for the text track. To see a full list, request `/languages?filter=texttrack`.
    language: typing.Optional[str]

    # The read-only URL of the text track file. You can upload to this link when you create it for the first time.
    link: str

    # The time in ISO 8601 format when the text track link expires.
    link_expires_time: str

    # The descriptive name of the text track.
    name: typing.Optional[str]

    # The type of text track.  Option descriptions:  * `captions` - The text track is for captions.  * `subtitles` - The text track is for subtitles. 
    type: typing.Optional[str]

    # The relative URI of the text track.
    uri: str

class OptionalTextTrack(TypedDict, total=False):
    pass

class TextTrack(RequiredTextTrack, OptionalTextTrack):
    pass
