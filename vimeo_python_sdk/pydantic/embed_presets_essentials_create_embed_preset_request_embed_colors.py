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


class EmbedPresetsEssentialsCreateEmbedPresetRequestEmbedColors(BaseModel):
    # The hexadecimal color code of the fourth player color, which controls the player background color.
    color_four: typing.Optional[str] = Field(None, alias='color_four')

    # The hexadecimal color code of the first player color, which controls the color of the progress bar, buttons, and more.
    color_one: typing.Optional[str] = Field(None, alias='color_one')

    # The hexadecimal color code of the third player color, which controls the color of text and icons.
    color_three: typing.Optional[str] = Field(None, alias='color_three')

    # The hexadecimal color code of the second player color, which controls the player accent color.
    color_two: typing.Optional[str] = Field(None, alias='color_two')
    class Config:
        arbitrary_types_allowed = True
