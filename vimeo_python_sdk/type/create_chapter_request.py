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

from vimeo_python_sdk.type.create_chapter_request_thumbnail_uris import CreateChapterRequestThumbnailUris

class RequiredCreateChapterRequest(TypedDict):
    pass

class OptionalCreateChapterRequest(TypedDict, total=False):
    # The title of the chapter.
    title: typing.Optional[str]

    # The URI of the chapter's active thumbnail.
    active_thumbnail_uri: str

    thumbnail_uris: CreateChapterRequestThumbnailUris

    # The timecode of the chapter in seconds from the start of the video.
    timecode: typing.Optional[typing.Union[int, float]]

class CreateChapterRequest(RequiredCreateChapterRequest, OptionalCreateChapterRequest):
    pass
