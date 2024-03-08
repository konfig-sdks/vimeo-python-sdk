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

from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request_embed_logos_custom import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogosCustom

class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogos(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogos(TypedDict, total=False):
    custom: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogosCustom

    # Whether to show the Vimeo logo on the embed player.
    vimeo: bool

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogos(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogos, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequestEmbedLogos):
    pass
