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

from vimeo_python_sdk.type.live_essentials_update_event_belonging_to_authenticated_user_request1_embed_logos import LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogos

class RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed(TypedDict):
    pass

class OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed(TypedDict, total=False):
    # Whether playback starts automatically on load.
    autoplay: bool

    # The hexadecimal color code for the main color of the embed player.
    color: str

    logos: LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1EmbedLogos

    # Whether the playlist should start from the beginning again after reaching the end of the last video.
    loop: bool

    # Whether to show the playlist controls on the embed player.
    playlist: bool

    # Whether to show the event schedule on the embed player.
    schedule: bool

    # Whether the embed player should use (`true`) or ignore (`false`) the **embed.color** value.
    use_color: bool

class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed(RequiredLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed, OptionalLiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest1Embed):
    pass
