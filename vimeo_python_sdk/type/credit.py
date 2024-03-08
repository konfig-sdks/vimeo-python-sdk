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

from vimeo_python_sdk.type.user import User
from vimeo_python_sdk.type.video import Video

class RequiredCredit(TypedDict):
    # The name of the person credited.
    name: str

    # The character that the person portrayed, or the job that the person performed.
    role: str

    # The unique identifier to access the credit resource.
    uri: str

class OptionalCredit(TypedDict, total=False):
    # The Vimeo user associated with the credit.
    user: User

    # The video associated with the credit.
    video: Video

class Credit(RequiredCredit, OptionalCredit):
    pass
