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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.live_event_recurring_metadata_interactions_activate import LiveEventRecurringMetadataInteractionsActivate
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_interactions_delete import LiveEventRecurringMetadataInteractionsDelete
from vimeo_python_sdk.pydantic.live_event_recurring_metadata_interactions_edit import LiveEventRecurringMetadataInteractionsEdit

class LiveEventRecurringMetadataInteractions(BaseModel):
    activate: LiveEventRecurringMetadataInteractionsActivate = Field(alias='activate')

    delete: LiveEventRecurringMetadataInteractionsDelete = Field(alias='delete')

    edit: LiveEventRecurringMetadataInteractionsEdit = Field(alias='edit')
    class Config:
        arbitrary_types_allowed = True
