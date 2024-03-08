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


class EmbedSettingsButtons(BaseModel):
    # Whether the `embed` button appears in the embeddable player.
    embed: bool = Field(alias='embed')

    # Whether the `fullscreen` button appears in the embeddable player.
    fullscreen: bool = Field(alias='fullscreen')

    # Whether the `HD` button appears in the embeddable player.
    hd: bool = Field(alias='hd')

    # Whether the `like` button appears in the embeddable player.
    like: bool = Field(alias='like')

    # Whether the reaction button appears in the embeddable player.
    reaction: typing.Optional[bool] = Field(alias='reaction')

    # Whether the `scaling` button appears in the embeddable player.
    scaling: bool = Field(alias='scaling')

    # Whether the `share` button appears in the embeddable player.
    share: bool = Field(alias='share')

    # Whether the `watch later` button appears in the embeddable player.
    watchlater: bool = Field(alias='watchlater')
    class Config:
        arbitrary_types_allowed = True
