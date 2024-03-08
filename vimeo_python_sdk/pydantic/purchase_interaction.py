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

from vimeo_python_sdk.pydantic.purchase_interaction_subscribe import PurchaseInteractionSubscribe

class PurchaseInteraction(BaseModel):
    # Information on purchasing the On Demand video.
    buy: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='buy')

    # Information on renting the On Demand video.
    rent: typing.Optional[typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = Field(None, alias='rent')

    subscribe: typing.Optional[PurchaseInteractionSubscribe] = Field(None, alias='subscribe')
    class Config:
        arbitrary_types_allowed = True
