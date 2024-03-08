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


class RequiredSubscriptionPlansPromotionUri(TypedDict):
    pass

class OptionalSubscriptionPlansPromotionUri(TypedDict, total=False):
    # The URI of the annual promotion.
    annual: str

    # The URI of the monthly promotion.
    monthly: str

class SubscriptionPlansPromotionUri(RequiredSubscriptionPlansPromotionUri, OptionalSubscriptionPlansPromotionUri):
    pass
