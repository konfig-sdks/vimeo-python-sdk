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

from vimeo_python_sdk.type.subscription_plans_metadata_entitlements import SubscriptionPlansMetadataEntitlements
from vimeo_python_sdk.type.subscription_plans_metadata_interactions import SubscriptionPlansMetadataInteractions
from vimeo_python_sdk.type.subscription_plans_metadata_purchased_product import SubscriptionPlansMetadataPurchasedProduct
from vimeo_python_sdk.type.subscription_plans_metadata_video_quota import SubscriptionPlansMetadataVideoQuota

class RequiredSubscriptionPlansMetadata(TypedDict):
    entitlements: SubscriptionPlansMetadataEntitlements

    interactions: SubscriptionPlansMetadataInteractions

    purchased_product: SubscriptionPlansMetadataPurchasedProduct

    video_quota: SubscriptionPlansMetadataVideoQuota

class OptionalSubscriptionPlansMetadata(TypedDict, total=False):
    pass

class SubscriptionPlansMetadata(RequiredSubscriptionPlansMetadata, OptionalSubscriptionPlansMetadata):
    pass
