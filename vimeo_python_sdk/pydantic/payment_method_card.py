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

from vimeo_python_sdk.pydantic.payment_method_card_billing_address import PaymentMethodCardBillingAddress

class PaymentMethodCard(BaseModel):
    billing_address: typing.Optional[PaymentMethodCardBillingAddress] = Field(None, alias='billing_address')

    # The bank identification number of the card.
    bin: typing.Optional[str] = Field(None, alias='bin')

    # The brand of the card.
    brand: typing.Optional[str] = Field(None, alias='brand')

    # The name of the cardholder.
    cardholder_name: typing.Optional[str] = Field(None, alias='cardholder_name')

    # The expiration month of the card.
    expiration_month: typing.Optional[typing.Union[int, float]] = Field(None, alias='expiration_month')

    # The expiration year of the card.
    expiration_year: typing.Optional[typing.Union[int, float]] = Field(None, alias='expiration_year')

    # The last four digits of the card.
    last_four_digits: typing.Optional[str] = Field(None, alias='last_four_digits')
    class Config:
        arbitrary_types_allowed = True
