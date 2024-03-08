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


class RequiredOnDemandPageSubscription(TypedDict):
    # Whether the On Demand product is active.
    active: bool

    # The link to the On Demand product.
    link: typing.Optional[str]

    # The accepted currencies and respective pricing for the On Demand product.
    price: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class OptionalOnDemandPageSubscription(TypedDict, total=False):
    # The On Demand product's rental period.
    period: str

class OnDemandPageSubscription(RequiredOnDemandPageSubscription, OptionalOnDemandPageSubscription):
    pass
