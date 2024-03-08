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

from vimeo_python_sdk.type.payment_method_card_billing_address import PaymentMethodCardBillingAddress

class RequiredPaymentMethodCard(TypedDict):
    pass

class OptionalPaymentMethodCard(TypedDict, total=False):
    billing_address: PaymentMethodCardBillingAddress

    # The bank identification number of the card.
    bin: str

    # The brand of the card.
    brand: str

    # The name of the cardholder.
    cardholder_name: str

    # The expiration month of the card.
    expiration_month: typing.Union[int, float]

    # The expiration year of the card.
    expiration_year: typing.Union[int, float]

    # The last four digits of the card.
    last_four_digits: str

class PaymentMethodCard(RequiredPaymentMethodCard, OptionalPaymentMethodCard):
    pass
