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


class RequiredSubscriptionItemsItem(TypedDict):
    # The ID of the billing plan for the subscription item.
    billing_plan_id: str

    # The time in 8601 format when the subscription item was created.
    created_at: str

    # The ID of the subscription item.
    id: str

    # The quantity of the subscription item.
    quantity: typing.Union[int, float]

    # The time in 8601 format when the subscription item was synced.
    synced_at: str

    # The time in 8601 format when the subscription item was updated.
    updated_at: str

class OptionalSubscriptionItemsItem(TypedDict, total=False):
    # The metadata of the subscription item.
    metadata: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The promotional code for the subscription item.
    promo_code: str

    # The ID of the promotional code for the subscription item.
    promo_code_id: str

class SubscriptionItemsItem(RequiredSubscriptionItemsItem, OptionalSubscriptionItemsItem):
    pass
