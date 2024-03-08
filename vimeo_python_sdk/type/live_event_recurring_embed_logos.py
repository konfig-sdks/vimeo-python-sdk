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

from vimeo_python_sdk.type.live_event_recurring_embed_logos_custom import LiveEventRecurringEmbedLogosCustom

class RequiredLiveEventRecurringEmbedLogos(TypedDict):
    custom: LiveEventRecurringEmbedLogosCustom

    # Whether the Vimeo logo appears in the embeddable player for the video.
    vimeo: bool

class OptionalLiveEventRecurringEmbedLogos(TypedDict, total=False):
    pass

class LiveEventRecurringEmbedLogos(RequiredLiveEventRecurringEmbedLogos, OptionalLiveEventRecurringEmbedLogos):
    pass
