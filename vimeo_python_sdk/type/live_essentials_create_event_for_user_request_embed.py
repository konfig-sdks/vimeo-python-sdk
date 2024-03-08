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

from vimeo_python_sdk.type.live_essentials_create_event_for_user_request_embed_logos import LiveEssentialsCreateEventForUserRequestEmbedLogos

class RequiredLiveEssentialsCreateEventForUserRequestEmbed(TypedDict):
    pass

class OptionalLiveEssentialsCreateEventForUserRequestEmbed(TypedDict, total=False):
    # Whether playback starts automatically on load.
    autoplay: bool

    # The hexadecimal color code for the main color of the embed player.
    color: str

    logos: LiveEssentialsCreateEventForUserRequestEmbedLogos

    # Whether the playlist should start from the beginning again after reaching the end of the last video.
    loop: bool

    # Whether to show the playlist controls on the embed player.
    playlist: bool

    # Whether to show the event schedule on the embed player.
    schedule: bool

    # Whether to show the latest archived video in the embed player when off-air.
    show_latest_archived_clip: bool

    # Whether the embed player should use (`true`) or ignore (`false`) the **embed.color** value.
    use_color: bool

class LiveEssentialsCreateEventForUserRequestEmbed(RequiredLiveEssentialsCreateEventForUserRequestEmbed, OptionalLiveEssentialsCreateEventForUserRequestEmbed):
    pass
