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

from vimeo_python_sdk.type.webinar_event_metadata_interactions_activate import WebinarEventMetadataInteractionsActivate
from vimeo_python_sdk.type.webinar_event_metadata_interactions_delete import WebinarEventMetadataInteractionsDelete
from vimeo_python_sdk.type.webinar_event_metadata_interactions_edit import WebinarEventMetadataInteractionsEdit

class RequiredWebinarEventMetadataInteractions(TypedDict):
    activate: WebinarEventMetadataInteractionsActivate

    delete: WebinarEventMetadataInteractionsDelete

    edit: WebinarEventMetadataInteractionsEdit

class OptionalWebinarEventMetadataInteractions(TypedDict, total=False):
    pass

class WebinarEventMetadataInteractions(RequiredWebinarEventMetadataInteractions, OptionalWebinarEventMetadataInteractions):
    pass
