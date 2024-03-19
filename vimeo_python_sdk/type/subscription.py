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

from vimeo_python_sdk.type.subscription_items import SubscriptionItems

class RequiredSubscription(TypedDict):
    # Whether the subscription is set to auto-renew.
    auto_renew: bool

    # The time in ISO 8601 format when the subscription was created.
    created_at: str

    # The time in ISO 8601 format when the subscription ended.
    end_date: str

    # The ID of the grace period.
    grace_period_id: str

    # The ID of the subscription.
    id: str

    # Whether the subscription is the latest version.
    is_latest: bool

    items: SubscriptionItems

    # The ID of the payment method.
    payment_method_id: str

    # The time in ISO 8601 format when the subscription started.
    start_date: str

    # The status of the subscription.  Option descriptions:  * `0` - The subscription status is unspecified.  * `1` - The subscription is active.  * `2` - The subscription is canceled.  * `3` - The subscription is in a grace period.  * `4` - The subscription is in a trial period.  * `5` - The subscription is past due.  * `6` - The subscription is unpaid. 
    status: str

    # The number of the subscription.
    subscription_number: str

    # The version of the subscription.
    subscription_version: typing.Union[int, float]

    # The time in ISO 8601 format when the subscription was synced.
    synced_at: str

    # The time in ISO 8601 format when the subscription was updated.
    updated_at: str

    # The vendor of the subscription.
    vendor: str

class OptionalSubscription(TypedDict, total=False):
    # The ID of the account.
    account_id: str

    # The time in ISO 8601 format when the subscription was disabled.
    disabled_at: str

class Subscription(RequiredSubscription, OptionalSubscription):
    pass
