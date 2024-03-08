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


class RequiredChannelsModeratorsReplaceModeratorsRequest(TypedDict):
    # The URI of the user to add as a moderator.
    user_uri: str

class OptionalChannelsModeratorsReplaceModeratorsRequest(TypedDict, total=False):
    pass

class ChannelsModeratorsReplaceModeratorsRequest(RequiredChannelsModeratorsReplaceModeratorsRequest, OptionalChannelsModeratorsReplaceModeratorsRequest):
    pass
