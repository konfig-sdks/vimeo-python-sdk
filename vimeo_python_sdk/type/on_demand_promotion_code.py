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


class RequiredOnDemandPromotionCode(TypedDict):
    # The Vimeo promotion code.
    code: str

    # The link to redeem the promotion code.
    link: str

    # The total number of times that this code can be used.
    max_uses: typing.Union[int, float]

    # The current number of times that this code has been used.
    uses: typing.Union[int, float]

class OptionalOnDemandPromotionCode(TypedDict, total=False):
    pass

class OnDemandPromotionCode(RequiredOnDemandPromotionCode, OptionalOnDemandPromotionCode):
    pass
