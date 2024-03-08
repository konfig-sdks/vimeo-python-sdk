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


class EmbedSettingsCardsItem(BaseModel):
    # The number of seconds for which the card appears.
    display_time: typing.Union[int, float] = Field(alias='display_time')

    # The title of the card.
    headline: str = Field(alias='headline')

    # The UUID of the card.
    id: str = Field(alias='id')

    # The URL of the thumbnail for the card.
    image_url: str = Field(alias='image_url')

    # The description of the card.
    teaser: str = Field(alias='teaser')

    # The playback timestamp, given in seconds, when the card appears.
    timecode: typing.Union[int, float] = Field(alias='timecode')

    # The URL of the card.
    url: str = Field(alias='url')
    class Config:
        arbitrary_types_allowed = True
