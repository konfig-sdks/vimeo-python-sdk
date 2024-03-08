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

from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_request_add import VideosShowcasesAddToMultipleShowcasesRequestAdd
from vimeo_python_sdk.type.videos_showcases_add_to_multiple_showcases_request_remove import VideosShowcasesAddToMultipleShowcasesRequestRemove

class RequiredVideosShowcasesAddToMultipleShowcasesRequest(TypedDict):
    pass

class OptionalVideosShowcasesAddToMultipleShowcasesRequest(TypedDict, total=False):
    add: VideosShowcasesAddToMultipleShowcasesRequestAdd

    remove: VideosShowcasesAddToMultipleShowcasesRequestRemove

class VideosShowcasesAddToMultipleShowcasesRequest(RequiredVideosShowcasesAddToMultipleShowcasesRequest, OptionalVideosShowcasesAddToMultipleShowcasesRequest):
    pass