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


class PresetSettingsButtons(BaseModel):
    # Whether the preset includes `Embed` button settings.
    embed: bool = Field(alias='embed')

    # Whether the preset includes `Fullscreen` button settings.
    fullscreen: bool = Field(alias='fullscreen')

    # Whether the preset includes `HD` button settings.
    hd: bool = Field(alias='hd')

    # Whether the preset includes `Like` button settings.
    like: bool = Field(alias='like')

    # Whether the preset includes `Reaction` button settings.
    reaction: typing.Optional[bool] = Field(alias='reaction')

    # Whether the present includes `Share` button settings.
    share: bool = Field(alias='share')

    # Whether the preset includes `Vote` button settings.
    vote: bool = Field(alias='vote')

    # Whether the preset includes `Watch Later` button settings.
    watchlater: bool = Field(alias='watchlater')
    class Config:
        arbitrary_types_allowed = True
