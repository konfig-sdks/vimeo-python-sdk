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

from vimeo_python_sdk.type.live_essentials_create_event_request_embed_logos_custom import LiveEssentialsCreateEventRequestEmbedLogosCustom

class RequiredLiveEssentialsCreateEventRequestEmbedLogos(TypedDict):
    pass

class OptionalLiveEssentialsCreateEventRequestEmbedLogos(TypedDict, total=False):
    custom: LiveEssentialsCreateEventRequestEmbedLogosCustom

    # Whether to show the Vimeo logo on the embed player.
    vimeo: bool

class LiveEssentialsCreateEventRequestEmbedLogos(RequiredLiveEssentialsCreateEventRequestEmbedLogos, OptionalLiveEssentialsCreateEventRequestEmbedLogos):
    pass
