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

from vimeo_python_sdk.pydantic.create_vod_request_subscription_monthly_price import CreateVodRequestSubscriptionMonthlyPrice

class CreateVodRequestSubscriptionMonthly(BaseModel):
    # Whether a monthly subscription is active. This parameter is required when **rent.active** and **buy.active** are `false`.
    active: typing.Optional[bool] = Field(None, alias='active')

    price: typing.Optional[CreateVodRequestSubscriptionMonthlyPrice] = Field(None, alias='price')
    class Config:
        arbitrary_types_allowed = True