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


class SubscriptionItemsItem(BaseModel):
    # The ID of the billing plan for the subscription item.
    billing_plan_id: str = Field(alias='billing_plan_id')

    # The time in 8601 format when the subscription item was created.
    created_at: str = Field(alias='created_at')

    # The ID of the subscription item.
    id: str = Field(alias='id')

    # The quantity of the subscription item.
    quantity: typing.Union[int, float] = Field(alias='quantity')

    # The time in 8601 format when the subscription item was synced.
    synced_at: str = Field(alias='synced_at')

    # The time in 8601 format when the subscription item was updated.
    updated_at: str = Field(alias='updated_at')

    # The metadata of the subscription item.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    # The promotional code for the subscription item.
    promo_code: typing.Optional[str] = Field(None, alias='promo_code')

    # The ID of the promotional code for the subscription item.
    promo_code_id: typing.Optional[str] = Field(None, alias='promo_code_id')
    class Config:
        arbitrary_types_allowed = True
