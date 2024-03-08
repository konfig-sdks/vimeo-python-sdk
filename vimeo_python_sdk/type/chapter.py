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

from vimeo_python_sdk.type.picture import Picture

class RequiredChapter(TypedDict):
    # The title of the chapter.
    title: typing.Optional[str]

    # The thumbnails associated with the video chapter.
    thumbnails: typing.List[Picture]

    # The timecode of the chapter in seconds from the start of the video.
    timecode: typing.Optional[typing.Union[int, float]]

    # The relative URI of the chapter.
    uri: str

class OptionalChapter(TypedDict, total=False):
    # The URI of the active thumbnail.
    active_thumbnail_uri: str

class Chapter(RequiredChapter, OptionalChapter):
    pass
