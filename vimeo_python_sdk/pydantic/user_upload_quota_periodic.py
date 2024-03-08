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
from pydantic import BaseModel, Field, RootModel


class UserUploadQuotaPeriodic(BaseModel):
    # The number of bytes or video count remaining in the authenticated user's upload quota for the current period.
    free: typing.Optional[typing.Union[int, float]] = Field(alias='free')

    # The total number of bytes or videos that the authenticated user can upload per period.
    max: typing.Optional[typing.Union[int, float]] = Field(alias='max')

    # The renewal frequency of the quota.  Option descriptions:  * `lifetime` - The user doesn't have a periodic quota.  * `month` - The quota renews monthly.  * `week` - The quota renews weekly.  * `year` - The quota renews yearly. 
    period: Literal["lifetime", "month", "week", "year"] = Field(alias='period')

    # The time in ISO 8601 format when the authenticated user's upload quota resets.
    reset_date: typing.Optional[str] = Field(alias='reset_date')

    # The unit that's used to compute quota.  Option descriptions:  * `video_count` - The quota is calculated using the count of the videos.  * `video_size` - The quota is calculated using the byte size of the videos. 
    unit: Literal["video_count", "video_size"] = Field(alias='unit')

    # The number of bytes or video count that the authenticated user has already uploaded against their quota in the current period.
    used: typing.Optional[typing.Union[int, float]] = Field(alias='used')
    class Config:
        arbitrary_types_allowed = True
