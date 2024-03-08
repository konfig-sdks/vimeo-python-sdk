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

from vimeo_python_sdk.pydantic.subscription_plans_promotion_price import SubscriptionPlansPromotionPrice
from vimeo_python_sdk.pydantic.subscription_plans_promotion_uri import SubscriptionPlansPromotionUri

class SubscriptionPlansPromotion(BaseModel):
    # The promotion code.
    code: str = Field(alias='code')

    # The promotion discount percentage.
    discount: typing.Union[int, float] = Field(alias='discount')

    price: SubscriptionPlansPromotionPrice = Field(alias='price')

    uri: SubscriptionPlansPromotionUri = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
