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


class OnDemandVideoRent(BaseModel):
    # Whether the video can be rented.
    active: bool = Field(alias='active')

    # A map of currency type to price.
    price: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(alias='price')

    # Whether the video has been rented.
    purchased: typing.Optional[bool] = Field(None, alias='purchased')
    class Config:
        arbitrary_types_allowed = True
