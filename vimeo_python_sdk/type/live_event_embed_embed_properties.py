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


class RequiredLiveEventEmbedEmbedProperties(TypedDict):
    # The height used to generate the fixed HTML embed code.
    height: str

    # The source URL used to generate the fixed HTML embed code.
    source_url: str

    # The width used to generate the fixed HTML embed code.
    width: str

class OptionalLiveEventEmbedEmbedProperties(TypedDict, total=False):
    pass

class LiveEventEmbedEmbedProperties(RequiredLiveEventEmbedEmbedProperties, OptionalLiveEventEmbedEmbedProperties):
    pass
