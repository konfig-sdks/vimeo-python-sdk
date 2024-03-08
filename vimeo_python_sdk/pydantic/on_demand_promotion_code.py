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


class OnDemandPromotionCode(BaseModel):
    # The Vimeo promotion code.
    code: str = Field(alias='code')

    # The link to redeem the promotion code.
    link: str = Field(alias='link')

    # The total number of times that this code can be used.
    max_uses: typing.Union[int, float] = Field(alias='max_uses')

    # The current number of times that this code has been used.
    uses: typing.Union[int, float] = Field(alias='uses')
    class Config:
        arbitrary_types_allowed = True
