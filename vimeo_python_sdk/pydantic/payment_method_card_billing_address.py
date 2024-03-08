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


class PaymentMethodCardBillingAddress(BaseModel):
    # The street address of the billing address.
    address: typing.Optional[str] = Field(None, alias='address')

    # The city of the billing address.
    city: typing.Optional[str] = Field(None, alias='city')

    # The country of the billing address.
    country: typing.Optional[str] = Field(None, alias='country')

    # The postal code of the billing address.
    postal_code: typing.Optional[str] = Field(None, alias='postal_code')

    # The state of the billing address.
    state: typing.Optional[str] = Field(None, alias='state')
    class Config:
        arbitrary_types_allowed = True
