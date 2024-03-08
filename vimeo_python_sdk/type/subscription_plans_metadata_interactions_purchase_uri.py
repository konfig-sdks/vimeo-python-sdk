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


class RequiredSubscriptionPlansMetadataInteractionsPurchaseUri(TypedDict):
    # The redirect URI for the annual plan in the user's cart.
    annual: typing.Optional[str]

    # The redirect URI for the free trial in the user's cart.
    free_trial: typing.Optional[str]

    # The redirect URI for the monthly plan in the user's cart.
    monthly: typing.Optional[str]

class OptionalSubscriptionPlansMetadataInteractionsPurchaseUri(TypedDict, total=False):
    pass

class SubscriptionPlansMetadataInteractionsPurchaseUri(RequiredSubscriptionPlansMetadataInteractionsPurchaseUri, OptionalSubscriptionPlansMetadataInteractionsPurchaseUri):
    pass
