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


class UploadVideoRequestEmbedButtons(BaseModel):
    # Whether to show the `embed` button on the embeddable player.
    embed: typing.Optional[bool] = Field(None, alias='embed')

    # Whether to show the `fullscreen` button on the embeddable player.
    fullscreen: typing.Optional[bool] = Field(None, alias='fullscreen')

    # Whether to show the `HD` button on the embeddable player.
    hd: typing.Optional[bool] = Field(None, alias='hd')

    # Whether to show the `like` button on the embeddable player.
    like: typing.Optional[bool] = Field(None, alias='like')

    # Whether to show the `scaling` button on the embeddable player in fullscreen mode.
    scaling: typing.Optional[bool] = Field(None, alias='scaling')

    # Whether to show the `share` button on the embeddable player.
    share: typing.Optional[bool] = Field(None, alias='share')

    # Whether to show the `watch later` button on the embeddable player.
    watchlater: typing.Optional[bool] = Field(None, alias='watchlater')
    class Config:
        arbitrary_types_allowed = True
