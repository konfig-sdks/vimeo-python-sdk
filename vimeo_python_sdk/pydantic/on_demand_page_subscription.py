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


class OnDemandPageSubscription(BaseModel):
    # Whether the On Demand product is active.
    active: bool = Field(alias='active')

    # The link to the On Demand product.
    link: typing.Optional[str] = Field(alias='link')

    # The accepted currencies and respective pricing for the On Demand product.
    price: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='price')

    # The On Demand product's rental period.
    period: typing.Optional[str] = Field(None, alias='period')
    class Config:
        arbitrary_types_allowed = True
