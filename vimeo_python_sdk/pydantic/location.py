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


class Location(BaseModel):
    # The authenticated user's city.
    city: typing.Optional[str] = Field(alias='city')

    # The authenticated user's country.
    country: typing.Optional[str] = Field(alias='country')

    # The ISO code of the authenticated user's country.
    country_iso_code: str = Field(alias='country_iso_code')

    # The authenticated user's formatted address string.
    formatted_address: str = Field(alias='formatted_address')

    # The authenticated user's latitude.
    latitude: typing.Union[int, float] = Field(alias='latitude')

    # The authenticated user's longitude.
    longitude: typing.Union[int, float] = Field(alias='longitude')

    # The authenticated user's neighborhood.
    neighborhood: typing.Optional[str] = Field(alias='neighborhood')

    # The authenticated user's state.
    state: typing.Optional[str] = Field(alias='state')

    # The ISO code of the authenticated user's state.
    state_iso_code: typing.Optional[str] = Field(alias='state_iso_code')

    # The authenticated user's sub-locality.
    sub_locality: typing.Optional[str] = Field(alias='sub_locality')
    class Config:
        arbitrary_types_allowed = True
