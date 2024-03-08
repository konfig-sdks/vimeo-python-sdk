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

from vimeo_python_sdk.pydantic.payment_method_card import PaymentMethodCard

class PaymentMethod(BaseModel):
    # The ID of the account.
    account_id: str = Field(alias='account_id')

    # The time when the payment method was created.
    created_at: str = Field(alias='created_at')

    # The time when the payment method was disabled.
    disabled_at: str = Field(alias='disabled_at')

    # The ID of the payment method.
    id: str = Field(alias='id')

    # Whether the payment method is the default payment method for the account.
    is_default: bool = Field(alias='is_default')

    # The type of payment method.  Option descriptions:  * `0` - The payment method type is unspecified.  * `1` - The payment method is a card.  * `2` - The payment method is a PayPal account.  * `3` - The payment method is a bank account.  * `4` - The payment method is Apple Pay.  * `5` - The payment method is Google Pay. 
    type: Literal["0", "1", "2", "3", "4", "5"] = Field(alias='type')

    # The time when the payment method was last updated.
    updated_at: str = Field(alias='updated_at')

    card: typing.Optional[PaymentMethodCard] = Field(None, alias='card')
    class Config:
        arbitrary_types_allowed = True
