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


class RequiredSubscriptionPlansMetadataVideoQuota(TypedDict):
    # The total video upload quota associated with the product.
    lifetime: typing.Optional[typing.Union[int, float]]

    # The monthly video upload quota associated with the product.
    monthly: typing.Union[int, float]

    # The yearly video upload quota associated with the product.
    yearly: typing.Union[int, float]

class OptionalSubscriptionPlansMetadataVideoQuota(TypedDict, total=False):
    pass

class SubscriptionPlansMetadataVideoQuota(RequiredSubscriptionPlansMetadataVideoQuota, OptionalSubscriptionPlansMetadataVideoQuota):
    pass
