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


class RequiredUserUploadQuotaLifetime(TypedDict):
    # The number of bytes or videos remaining in the authenticated user's lifetime maximum.
    free: typing.Optional[typing.Union[int, float]]

    # The total number of bytes or videos that the authenticated user can upload across the lifetime of their account.
    max: typing.Optional[typing.Union[int, float]]

    # The unit that's used to compute quota.  Option descriptions:  * `video_count` - The quota is calculated using the count of the videos.  * `video_size` - The quota is calculated using the byte size of the videos. 
    unit: typing.Optional[str]

    # The number of bytes or videos that the authenticated user has already uploaded against their lifetime limit.
    used: typing.Optional[typing.Union[int, float]]

class OptionalUserUploadQuotaLifetime(TypedDict, total=False):
    pass

class UserUploadQuotaLifetime(RequiredUserUploadQuotaLifetime, OptionalUserUploadQuotaLifetime):
    pass
