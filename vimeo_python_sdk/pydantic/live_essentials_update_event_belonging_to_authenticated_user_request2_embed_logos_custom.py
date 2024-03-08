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


class LiveEssentialsUpdateEventBelongingToAuthenticatedUserRequest2EmbedLogosCustom(BaseModel):
    # Whether to show the custom logo on the embed player.
    active: typing.Optional[bool] = Field(None, alias='active')

    # The URL that loads when the user clicks the custom logo.
    link: typing.Optional[str] = Field(None, alias='link')

    # Whether to show the custom logo persistently (`true`) or hide it with the rest of the UI (`false`).
    sticky: typing.Optional[bool] = Field(None, alias='sticky')
    class Config:
        arbitrary_types_allowed = True
