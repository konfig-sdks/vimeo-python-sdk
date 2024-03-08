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


class RequiredOnDemandVideoRent(TypedDict):
    # Whether the video can be rented.
    active: bool

    # A map of currency type to price.
    price: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalOnDemandVideoRent(TypedDict, total=False):
    # Whether the video has been rented.
    purchased: bool

class OnDemandVideoRent(RequiredOnDemandVideoRent, OptionalOnDemandVideoRent):
    pass
