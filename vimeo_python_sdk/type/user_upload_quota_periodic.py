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


class RequiredUserUploadQuotaPeriodic(TypedDict):
    # The number of bytes or video count remaining in the authenticated user's upload quota for the current period.
    free: typing.Optional[typing.Union[int, float]]

    # The total number of bytes or videos that the authenticated user can upload per period.
    max: typing.Optional[typing.Union[int, float]]

    # The renewal frequency of the quota.  Option descriptions:  * `lifetime` - The user doesn't have a periodic quota.  * `month` - The quota renews monthly.  * `week` - The quota renews weekly.  * `year` - The quota renews yearly. 
    period: typing.Optional[str]

    # The time in ISO 8601 format when the authenticated user's upload quota resets.
    reset_date: typing.Optional[str]

    # The unit that's used to compute quota.  Option descriptions:  * `video_count` - The quota is calculated using the count of the videos.  * `video_size` - The quota is calculated using the byte size of the videos. 
    unit: typing.Optional[str]

    # The number of bytes or video count that the authenticated user has already uploaded against their quota in the current period.
    used: typing.Optional[typing.Union[int, float]]

class OptionalUserUploadQuotaPeriodic(TypedDict, total=False):
    pass

class UserUploadQuotaPeriodic(RequiredUserUploadQuotaPeriodic, OptionalUserUploadQuotaPeriodic):
    pass
