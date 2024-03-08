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


class SubscriptionPlansPrice(BaseModel):
    # The annual price, charged annually.
    annual: typing.Union[int, float] = Field(alias='annual')

    # The monthly price, charged annually.
    annual_monthly: typing.Union[int, float] = Field(alias='annual_monthly')

    # The monthly price, charged monthly.
    monthly: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthly')
    class Config:
        arbitrary_types_allowed = True
