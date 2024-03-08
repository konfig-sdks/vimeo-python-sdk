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


class RequiredVideosTextTracksAddTextTrackRequest(TypedDict):
    # The language of the text track. For a full list of supported languages, use the [`/languages?filter=texttracks`](https://developer.vimeo.com/api/reference/videos#get_languages) endpoint.
    language: str

    # The name of the text track.
    name: str

    # The type of text track.  Option descriptions:  * `captions` - The text track is the captions type.  * `chapters` - The text track is the chapters type.  * `descriptions` - The text track is the descriptions type.  * `metadata` - The text track is the metadata type.  * `subtitles` - The text track is the subtitles type. 
    type: str

class OptionalVideosTextTracksAddTextTrackRequest(TypedDict, total=False):
    # Whether the current text track is the *active text track,* or the one that appears in the player. Only one text track per language and type can be active.
    active: bool

    # Whether the text track was uploaded automatically by the Seshat audio annotation management platform.
    is_auto_generated: bool

    # Whether the text track was uploaded by the Seshat audio annotation management platform after the user edited their transcript.
    is_edited: bool

class VideosTextTracksAddTextTrackRequest(RequiredVideosTextTracksAddTextTrackRequest, OptionalVideosTextTracksAddTextTrackRequest):
    pass
