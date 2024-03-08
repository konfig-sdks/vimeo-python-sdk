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

from vimeo_python_sdk.type.subscription_plans_metadata_interactions_purchase_uri import SubscriptionPlansMetadataInteractionsPurchaseUri

class RequiredSubscriptionPlansMetadataInteractionsPurchase(TypedDict):
    # The purchase status of the product.  Option descriptions:  * `available` - The product is available for purchase.  * `purchased` - The product is already purchased.  * `unavailable` - The product isn't available for purchase. 
    status: str

    uri: SubscriptionPlansMetadataInteractionsPurchaseUri

class OptionalSubscriptionPlansMetadataInteractionsPurchase(TypedDict, total=False):
    pass

class SubscriptionPlansMetadataInteractionsPurchase(RequiredSubscriptionPlansMetadataInteractionsPurchase, OptionalSubscriptionPlansMetadataInteractionsPurchase):
    pass
