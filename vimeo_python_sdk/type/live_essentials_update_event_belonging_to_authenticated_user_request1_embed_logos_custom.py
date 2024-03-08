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


class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogosCustom(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogosCustom(TypedDict, total=False):
    # Whether to show the custom logo on the embed player.
    active: bool

    # The URL that loads when the user clicks the custom logo.
    link: str

    # Whether to show the custom logo persistently (`true`) or hide it with the rest of the UI (`false`).
    sticky: bool

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogosCustom(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogosCustom, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogosCustom):
    pass
