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


class SubscriptionPlansMetadataInteractionsPurchaseUri(BaseModel):
    # The redirect URI for the annual plan in the user's cart.
    annual: typing.Optional[str] = Field(alias='annual')

    # The redirect URI for the free trial in the user's cart.
    free_trial: typing.Optional[str] = Field(alias='free_trial')

    # The redirect URI for the monthly plan in the user's cart.
    monthly: typing.Optional[str] = Field(alias='monthly')
    class Config:
        arbitrary_types_allowed = True
