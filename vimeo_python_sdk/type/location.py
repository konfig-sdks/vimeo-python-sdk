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


class RequiredLocation(TypedDict):
    # The authenticated user's city.
    city: typing.Optional[str]

    # The authenticated user's country.
    country: typing.Optional[str]

    # The ISO code of the authenticated user's country.
    country_iso_code: str

    # The authenticated user's formatted address string.
    formatted_address: str

    # The authenticated user's latitude.
    latitude: typing.Union[int, float]

    # The authenticated user's longitude.
    longitude: typing.Union[int, float]

    # The authenticated user's neighborhood.
    neighborhood: typing.Optional[str]

    # The authenticated user's state.
    state: typing.Optional[str]

    # The ISO code of the authenticated user's state.
    state_iso_code: typing.Optional[str]

    # The authenticated user's sub-locality.
    sub_locality: typing.Optional[str]

class OptionalLocation(TypedDict, total=False):
    pass

class Location(RequiredLocation, OptionalLocation):
    pass
