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

from vimeo_python_sdk.type.subscription_plans_promotion_price import SubscriptionPlansPromotionPrice
from vimeo_python_sdk.type.subscription_plans_promotion_uri import SubscriptionPlansPromotionUri

class RequiredSubscriptionPlansPromotion(TypedDict):
    # The promotion code.
    code: str

    # The promotion discount percentage.
    discount: typing.Union[int, float]

    price: SubscriptionPlansPromotionPrice

    uri: SubscriptionPlansPromotionUri

class OptionalSubscriptionPlansPromotion(TypedDict, total=False):
    pass

class SubscriptionPlansPromotion(RequiredSubscriptionPlansPromotion, OptionalSubscriptionPlansPromotion):
    pass
