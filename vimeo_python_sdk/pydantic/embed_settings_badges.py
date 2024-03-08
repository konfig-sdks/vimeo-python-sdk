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
from pydantic import BaseModel, Field, RootModel

from vimeo_python_sdk.pydantic.embed_settings_badges_live import EmbedSettingsBadgesLive
from vimeo_python_sdk.pydantic.embed_settings_badges_staff_pick import EmbedSettingsBadgesStaffPick

class EmbedSettingsBadges(BaseModel):
    # Whether the video has an HDR-compatible transcode.
    hdr: bool = Field(alias='hdr')

    live: EmbedSettingsBadgesLive = Field(alias='live')

    staff_pick: EmbedSettingsBadgesStaffPick = Field(alias='staff_pick')

    # Whether the video is a Vimeo On Demand video.
    vod: bool = Field(alias='vod')

    # Whether the video is a Vimeo Weekend Challenge.
    weekend_challenge: bool = Field(alias='weekend_challenge')

    # Whether the video was filmed using Dolby Vision.
    dolby_vision: typing.Optional[bool] = Field(None, alias='dolby_vision')

    # Whether the video was filmed using HDR10.
    hdr_10: typing.Optional[bool] = Field(None, alias='hdr_10')

    # Whether the video was filmed using HDR10 Plus.
    hdr_10_plus: typing.Optional[bool] = Field(None, alias='hdr_10_plus')
    class Config:
        arbitrary_types_allowed = True
