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


class RequiredPaymentsEssentialsListPaymentMethodsRequest(TypedDict):
    pass

class OptionalPaymentsEssentialsListPaymentMethodsRequest(TypedDict, total=False):
    # The type of payment method.  Option descriptions:  * `applepay` - The payment method is Apple Pay.  * `bank_account` - The payment method is a bank account.  * `card` - The payment method is a credit or debit card.  * `googlepay` - The payment method is Google Pay.  * `paypal` - The payment method is a PayPal account. 
    type: str

class PaymentsEssentialsListPaymentMethodsRequest(RequiredPaymentsEssentialsListPaymentMethodsRequest, OptionalPaymentsEssentialsListPaymentMethodsRequest):
    pass
