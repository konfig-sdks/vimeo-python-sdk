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


class RequiredOnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice(TypedDict):
    pass

class OptionalOnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice(TypedDict, total=False):
    # The monthly subscription price in United States dollars. This parameter is required when **rent.active** and **buy.active** are `false`.
    USD: typing.Union[int, float]

class OnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice(RequiredOnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice, OptionalOnDemandEssentialsCreatePageRequestSubscriptionMonthlyPrice):
    pass
