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

from vimeo_python_sdk.type.payment_method_card import PaymentMethodCard

class RequiredPaymentMethod(TypedDict):
    # The ID of the account.
    account_id: str

    # The time when the payment method was created.
    created_at: str

    # The time when the payment method was disabled.
    disabled_at: str

    # The ID of the payment method.
    id: str

    # Whether the payment method is the default payment method for the account.
    is_default: bool

    # The type of payment method.  Option descriptions:  * `0` - The payment method type is unspecified.  * `1` - The payment method is a card.  * `2` - The payment method is a PayPal account.  * `3` - The payment method is a bank account.  * `4` - The payment method is Apple Pay.  * `5` - The payment method is Google Pay. 
    type: str

    # The time when the payment method was last updated.
    updated_at: str

class OptionalPaymentMethod(TypedDict, total=False):
    card: PaymentMethodCard

class PaymentMethod(RequiredPaymentMethod, OptionalPaymentMethod):
    pass
