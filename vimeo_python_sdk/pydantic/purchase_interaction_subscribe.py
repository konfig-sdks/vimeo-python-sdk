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


class PurchaseInteractionSubscribe(BaseModel):
    # Whether the On Demand subscription has DRM.
    drm: typing.Optional[bool] = Field(None, alias='drm')

    # The time in ISO 8601 format when the On Demand video expires.
    expires_time: typing.Optional[typing.Optional[str]] = Field(None, alias='expires_time')

    # The URL to purchase the On Demand subscription on Vimeo.
    link: typing.Optional[typing.Optional[str]] = Field(None, alias='link')

    # The time in ISO 8601 format when the On Demand video was purchased.
    purchase_time: typing.Optional[typing.Optional[str]] = Field(None, alias='purchase_time')

    # The user's streaming access to the On Demand subscription.  Option descriptions:  * `available` - The On Demand subscription is available for streaming.  * `purchased` - The On Demand subscription has been purchased.  * `restricted` - Streaming for the On Demand subscription is restricted.  * `unavailable` - The On Demand subscription is unavailable. 
    stream: typing.Optional[Literal["available", "purchased", "restricted", "unavailable"]] = Field(None, alias='stream')

    # The On Demand subscription's product URI.
    uri: typing.Optional[typing.Optional[str]] = Field(None, alias='uri')
    class Config:
        arbitrary_types_allowed = True
