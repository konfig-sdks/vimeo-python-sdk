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


class RequiredHlsDashVideoFile(TypedDict):
    # The direct link to the video file.
    link: typing.Optional[str]

    # The time in ISO 8601 format when the link to the video file expires.
    link_expiration_time: str

class OptionalHlsDashVideoFile(TypedDict, total=False):
    # The URL for logging events.
    log: typing.Optional[str]

class HlsDashVideoFile(RequiredHlsDashVideoFile, OptionalHlsDashVideoFile):
    pass
