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

from vimeo_python_sdk.pydantic.subscription_items import SubscriptionItems

class Subscription(BaseModel):
    # Whether the subscription is set to auto-renew.
    auto_renew: bool = Field(alias='auto_renew')

    # The time in ISO 8601 format when the subscription was created.
    created_at: str = Field(alias='created_at')

    # The time in ISO 8601 format when the subscription ended.
    end_date: str = Field(alias='end_date')

    # The ID of the grace period.
    grace_period_id: str = Field(alias='grace_period_id')

    # The ID of the subscription.
    id: str = Field(alias='id')

    # Whether the subscription is the latest version.
    is_latest: bool = Field(alias='is_latest')

    items: SubscriptionItems = Field(alias='items')

    # The ID of the payment method.
    payment_method_id: str = Field(alias='payment_method_id')

    # The time in ISO 8601 format when the subscription started.
    start_date: str = Field(alias='start_date')

    # The status of the subscription.  Option descriptions:  * `0` - The subscription status is unspecified.  * `1` - The subscription is active.  * `2` - The subscription is canceled.  * `3` - The subscription is in a grace period.  * `4` - The subscription is in a trial period.  * `5` - The subscription is past due.  * `6` - The subscription is unpaid. 
    status: Literal["0", "1", "2", "3", "4", "5", "6"] = Field(alias='status')

    # The number of the subscription.
    subscription_number: str = Field(alias='subscription_number')

    # The version of the subscription.
    subscription_version: typing.Union[int, float] = Field(alias='subscription_version')

    # The time in ISO 8601 format when the subscription was synced.
    synced_at: str = Field(alias='synced_at')

    # The time in ISO 8601 format when the subscription was updated.
    updated_at: str = Field(alias='updated_at')

    # The vendor of the subscription.
    vendor: str = Field(alias='vendor')

    # The ID of the account.
    account_id: typing.Optional[str] = Field(None, alias='account_id')

    # The time in ISO 8601 format when the subscription was disabled.
    disabled_at: typing.Optional[str] = Field(None, alias='disabled_at')
    class Config:
        arbitrary_types_allowed = True
