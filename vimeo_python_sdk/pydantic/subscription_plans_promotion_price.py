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


class SubscriptionPlansPromotionPrice(BaseModel):
    # The promotional annual price, charged annually.
    annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='annual')

    # The promotional monthly price, charged annually.
    annual_monthly: typing.Optional[typing.Union[int, float]] = Field(None, alias='annual_monthly')

    # The promotional monthly price, charged monthly.
    monthly: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthly')
    class Config:
        arbitrary_types_allowed = True
