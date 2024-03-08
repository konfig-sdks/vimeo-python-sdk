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

from vimeo_python_sdk.type.embed_settings_badges_live import EmbedSettingsBadgesLive
from vimeo_python_sdk.type.embed_settings_badges_staff_pick import EmbedSettingsBadgesStaffPick

class RequiredEmbedSettingsBadges(TypedDict):
    # Whether the video has an HDR-compatible transcode.
    hdr: bool

    live: EmbedSettingsBadgesLive

    staff_pick: EmbedSettingsBadgesStaffPick

    # Whether the video is a Vimeo On Demand video.
    vod: bool

    # Whether the video is a Vimeo Weekend Challenge.
    weekend_challenge: bool

class OptionalEmbedSettingsBadges(TypedDict, total=False):
    # Whether the video was filmed using Dolby Vision.
    dolby_vision: bool

    # Whether the video was filmed using HDR10.
    hdr_10: bool

    # Whether the video was filmed using HDR10 Plus.
    hdr_10_plus: bool

class EmbedSettingsBadges(RequiredEmbedSettingsBadges, OptionalEmbedSettingsBadges):
    pass
