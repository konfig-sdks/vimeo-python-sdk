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


class RequiredVideosCreditsAddUserCreditInVideoRequest(TypedDict):
    # The email address of the credited person.
    email: str

    # The name of the credited person.
    name: str

    # The role of the credited person.
    role: str

    # The Vimeo URI of the credited person.
    user_uri: str

class OptionalVideosCreditsAddUserCreditInVideoRequest(TypedDict, total=False):
    pass

class VideosCreditsAddUserCreditInVideoRequest(RequiredVideosCreditsAddUserCreditInVideoRequest, OptionalVideosCreditsAddUserCreditInVideoRequest):
    pass
