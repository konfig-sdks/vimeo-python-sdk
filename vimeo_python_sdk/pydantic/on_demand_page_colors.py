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


class OnDemandPageColors(BaseModel):
    # The hexadecimal color code for the On Demand page's first color.
    primary: str = Field(alias='primary')

    # The hexadecimal color code for the On Demand page's second color.
    secondary: str = Field(alias='secondary')
    class Config:
        arbitrary_types_allowed = True
