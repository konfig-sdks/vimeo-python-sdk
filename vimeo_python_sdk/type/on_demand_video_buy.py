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


class RequiredOnDemandVideoBuy(TypedDict):
    # Whether the video can be purchased.
    active: bool

    # A map of currency type to price.
    price: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalOnDemandVideoBuy(TypedDict, total=False):
    # Whether the video has been purchased.
    purchased: bool

class OnDemandVideoBuy(RequiredOnDemandVideoBuy, OptionalOnDemandVideoBuy):
    pass
