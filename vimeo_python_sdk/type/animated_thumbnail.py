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


class RequiredAnimatedThumbnail(TypedDict):
    # The duration of the animated thumbnail in seconds.
    duration: typing.Union[int, float]

    # The file format of the animated thumbnail.
    file_format: str

    # The file size of the animated thumbnail in bytes.
    file_size: typing.Union[int, float]

    # The height of the animated thumbnail in pixels.
    height: typing.Union[int, float]

    # Whether the animated thumbnail can be downloaded.
    is_downloadable: bool

    # The URL of the animated thumbnail file.
    link: str

    # The URL of the animated thumbnail file with a play button overlay.
    link_with_play_button: str

    # The profile ID of the animated thumbnail.
    profile_id: str

    # The time in the video, in seconds, corresponding to the start of the animation.
    start_time: typing.Union[int, float]

    # The ID of the animated thumbnail.
    uuid: str

    # The width of the animated thumbnail in pixels.
    width: typing.Union[int, float]

class OptionalAnimatedThumbnail(TypedDict, total=False):
    pass

class AnimatedThumbnail(RequiredAnimatedThumbnail, OptionalAnimatedThumbnail):
    pass
