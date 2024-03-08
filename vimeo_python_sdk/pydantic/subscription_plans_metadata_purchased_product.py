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


class SubscriptionPlansMetadataPurchasedProduct(BaseModel):
    # The display price of the purchased product.
    display_price: typing.Union[int, float] = Field(alias='display_price')

    # Whether the purchased product is billed as a monthly subscription.
    is_monthly: bool = Field(alias='is_monthly')
    class Config:
        arbitrary_types_allowed = True
