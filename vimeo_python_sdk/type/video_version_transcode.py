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


class RequiredVideoVersionTranscode(TypedDict):
    pass

class OptionalVideoVersionTranscode(TypedDict, total=False):
    # The status code for the availability of the video version.  Option descriptions:  * `complete` - Transcoding is complete. The video version is available.  * `error` - There was a transcoding error. The video version isn't available.  * `in_progress` - Transcoding is in progress. The video version isn't available yet. 
    status: str

class VideoVersionTranscode(RequiredVideoVersionTranscode, OptionalVideoVersionTranscode):
    pass
