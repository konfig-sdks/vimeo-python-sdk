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

from vimeo_python_sdk.type.purchase_interaction_subscribe import PurchaseInteractionSubscribe

class RequiredPurchaseInteraction(TypedDict):
    pass

class OptionalPurchaseInteraction(TypedDict, total=False):
    # Information on purchasing the On Demand video.
    buy: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    # Information on renting the On Demand video.
    rent: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]

    subscribe: PurchaseInteractionSubscribe

class PurchaseInteraction(RequiredPurchaseInteraction, OptionalPurchaseInteraction):
    pass
