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


class RequiredEmbedSettingsBadgesStaffPick(TypedDict):
    # Whether the video is a Vimeo Staff Pick Best of the Month.
    best_of_the_month: bool

    # Whether the video is a Vimeo Staff Pick Best of the Year.
    best_of_the_year: bool

    # Whether the video is a Vimeo Staff Pick.
    normal: bool

    # Whether the video is a Vimeo Staff Pick Premiere.
    premiere: bool

class OptionalEmbedSettingsBadgesStaffPick(TypedDict, total=False):
    pass

class EmbedSettingsBadgesStaffPick(RequiredEmbedSettingsBadgesStaffPick, OptionalEmbedSettingsBadgesStaffPick):
    pass
