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


class EmbedSettingsColors(BaseModel):
    # The fourth player color, which controls the player background color.
    color_four: str = Field(alias='color_four')

    # The first player color, which controls the color of the progress bar, buttons, and more.
    color_one: str = Field(alias='color_one')

    # The third player color, which controls the color of text and icons.
    color_three: str = Field(alias='color_three')

    # The second player color, which controls the player accent color.
    color_two: str = Field(alias='color_two')
    class Config:
        arbitrary_types_allowed = True
