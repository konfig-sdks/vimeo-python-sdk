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


class RequiredPaymentMethodCardBillingAddress(TypedDict):
    pass

class OptionalPaymentMethodCardBillingAddress(TypedDict, total=False):
    # The street address of the billing address.
    address: str

    # The city of the billing address.
    city: str

    # The country of the billing address.
    country: str

    # The postal code of the billing address.
    postal_code: str

    # The state of the billing address.
    state: str

class PaymentMethodCardBillingAddress(RequiredPaymentMethodCardBillingAddress, OptionalPaymentMethodCardBillingAddress):
    pass
