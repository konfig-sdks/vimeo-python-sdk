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


class RequiredSegmentWords(TypedDict):
    # The end time of the word in milliseconds.
    end_time: typing.Optional[typing.Union[int, float]]

    # The start time of the word in milliseconds.
    start_time: typing.Optional[typing.Union[int, float]]

    # The word text.
    word: str

class OptionalSegmentWords(TypedDict, total=False):
    pass

class SegmentWords(RequiredSegmentWords, OptionalSegmentWords):
    pass
