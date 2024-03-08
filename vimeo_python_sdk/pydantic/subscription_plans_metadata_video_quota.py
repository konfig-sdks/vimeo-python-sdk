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


class SubscriptionPlansMetadataVideoQuota(BaseModel):
    # The total video upload quota associated with the product.
    lifetime: typing.Optional[typing.Union[int, float]] = Field(alias='lifetime')

    # The monthly video upload quota associated with the product.
    monthly: typing.Union[int, float] = Field(alias='monthly')

    # The yearly video upload quota associated with the product.
    yearly: typing.Union[int, float] = Field(alias='yearly')
    class Config:
        arbitrary_types_allowed = True
