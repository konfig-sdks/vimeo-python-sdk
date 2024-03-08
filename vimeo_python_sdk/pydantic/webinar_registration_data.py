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


class WebinarRegistrationData(BaseModel):
    # The maximum number of registrants permitted to attend the webinar.
    capping: typing.Union[int, float] = Field(alias='capping')

    # Whether the number of registrants is unlimited.
    is_unlimited: bool = Field(alias='is_unlimited')

    # The minimum number of registrants to trigger the 80% capping email.
    lower_limit: typing.Union[int, float] = Field(alias='lower_limit')

    # The number of registrants who have signed up for the webinar.
    total: typing.Union[int, float] = Field(alias='total')

    # The maximum number of registrants to trigger the 100% capping email.
    upper_limit: typing.Union[int, float] = Field(alias='upper_limit')
    class Config:
        arbitrary_types_allowed = True
