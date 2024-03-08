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

class RequiredVideoUploader(TypedDict):
    # The profile link of the user who uploaded the video.
    link: str

    # The display name of the user who uploaded the video.
    name: str

    # The active portrait of the user who uploaded the video.
    pictures: Picture

class OptionalVideoUploader(TypedDict, total=False):
    pass

class VideoUploader(RequiredVideoUploader, OptionalVideoUploader):
    pass
