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


class LiveEventEmbedLogosCustom(BaseModel):
    # Whether the custom logo appears in the embeddable player.
    active: bool = Field(alias='active')

    # The URL that loads upon clicking the custom logo.
    link: str = Field(alias='link')

    # Whether the custom logo appears even when the player interface is hidden.
    sticky: bool = Field(alias='sticky')

    # The URL source of the custom player logo.
    url: str = Field(alias='url')

    # Whether the custom logo should use the URL link.
    use_link: bool = Field(alias='use_link')
    class Config:
        arbitrary_types_allowed = True
