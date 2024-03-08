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

from vimeo_python_sdk.type.on_demand_page_metadata_connections import OnDemandPageMetadataConnections
from vimeo_python_sdk.type.purchase_interaction import PurchaseInteraction

class RequiredOnDemandPageMetadata(TypedDict):
    connections: OnDemandPageMetadataConnections

    # The user's available purchase interactions.
    interactions: PurchaseInteraction

class OptionalOnDemandPageMetadata(TypedDict, total=False):
    pass

class OnDemandPageMetadata(RequiredOnDemandPageMetadata, OptionalOnDemandPageMetadata):
    pass
