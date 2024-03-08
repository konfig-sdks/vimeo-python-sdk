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

from vimeo_python_sdk.type.live_essentials_create_event_for_user_request_embed_logos_custom import LiveEssentialsCreateEventForUserRequestEmbedLogosCustom

class RequiredLiveEssentialsCreateEventForUserRequestEmbedLogos(TypedDict):
    pass

class OptionalLiveEssentialsCreateEventForUserRequestEmbedLogos(TypedDict, total=False):
    custom: LiveEssentialsCreateEventForUserRequestEmbedLogosCustom

    # Whether to show the Vimeo logo on the embed player.
    vimeo: bool

class LiveEssentialsCreateEventForUserRequestEmbedLogos(RequiredLiveEssentialsCreateEventForUserRequestEmbedLogos, OptionalLiveEssentialsCreateEventForUserRequestEmbedLogos):
    pass
