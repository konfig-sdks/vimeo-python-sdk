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


class EmbedSettingsBadgesStaffPick(BaseModel):
    # Whether the video is a Vimeo Staff Pick Best of the Month.
    best_of_the_month: bool = Field(alias='best_of_the_month')

    # Whether the video is a Vimeo Staff Pick Best of the Year.
    best_of_the_year: bool = Field(alias='best_of_the_year')

    # Whether the video is a Vimeo Staff Pick.
    normal: bool = Field(alias='normal')

    # Whether the video is a Vimeo Staff Pick Premiere.
    premiere: bool = Field(alias='premiere')
    class Config:
        arbitrary_types_allowed = True
