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

from vimeo_python_sdk.type.live_event_recurring_metadata_interactions_delete_options import LiveEventRecurringMetadataInteractionsDeleteOptions

class RequiredLiveEventRecurringMetadataInteractionsDelete(TypedDict):
    options: LiveEventRecurringMetadataInteractionsDeleteOptions

    # The API URI that resolves to the connection data.
    uri: str

class OptionalLiveEventRecurringMetadataInteractionsDelete(TypedDict, total=False):
    pass

class LiveEventRecurringMetadataInteractionsDelete(RequiredLiveEventRecurringMetadataInteractionsDelete, OptionalLiveEventRecurringMetadataInteractionsDelete):
    pass
