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


class RequiredSubscriptionPlansPromotionPrice(TypedDict):
    pass

class OptionalSubscriptionPlansPromotionPrice(TypedDict, total=False):
    # The promotional annual price, charged annually.
    annual: typing.Union[int, float]

    # The promotional monthly price, charged annually.
    annual_monthly: typing.Union[int, float]

    # The promotional monthly price, charged monthly.
    monthly: typing.Union[int, float]

class SubscriptionPlansPromotionPrice(RequiredSubscriptionPlansPromotionPrice, OptionalSubscriptionPlansPromotionPrice):
    pass
