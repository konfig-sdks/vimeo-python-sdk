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


class OnDemandRegion(BaseModel):
    # The ISO 3166-1 alpha-2 code for this country.
    country_code: str = Field(alias='country_code')

    # The descriptive name of this country.
    country_name: str = Field(alias='country_name')

    # The region container's relative URI.
    uri: str = Field(alias='uri')
    class Config:
        arbitrary_types_allowed = True
