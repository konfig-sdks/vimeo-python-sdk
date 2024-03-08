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


class RequiredPurchaseInteractionSubscribe(TypedDict):
    pass

class OptionalPurchaseInteractionSubscribe(TypedDict, total=False):
    # Whether the On Demand subscription has DRM.
    drm: bool

    # The time in ISO 8601 format when the On Demand video expires.
    expires_time: typing.Optional[str]

    # The URL to purchase the On Demand subscription on Vimeo.
    link: typing.Optional[str]

    # The time in ISO 8601 format when the On Demand video was purchased.
    purchase_time: typing.Optional[str]

    # The user's streaming access to the On Demand subscription.  Option descriptions:  * `available` - The On Demand subscription is available for streaming.  * `purchased` - The On Demand subscription has been purchased.  * `restricted` - Streaming for the On Demand subscription is restricted.  * `unavailable` - The On Demand subscription is unavailable. 
    stream: str

    # The On Demand subscription's product URI.
    uri: typing.Optional[str]

class PurchaseInteractionSubscribe(RequiredPurchaseInteractionSubscribe, OptionalPurchaseInteractionSubscribe):
    pass
