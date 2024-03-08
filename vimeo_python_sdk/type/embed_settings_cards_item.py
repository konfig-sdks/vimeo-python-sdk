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


class RequiredEmbedSettingsCardsItem(TypedDict):
    # The number of seconds for which the card appears.
    display_time: typing.Union[int, float]

    # The title of the card.
    headline: str

    # The UUID of the card.
    id: str

    # The URL of the thumbnail for the card.
    image_url: str

    # The description of the card.
    teaser: str

    # The playback timestamp, given in seconds, when the card appears.
    timecode: typing.Union[int, float]

    # The URL of the card.
    url: str

class OptionalEmbedSettingsCardsItem(TypedDict, total=False):
    pass

class EmbedSettingsCardsItem(RequiredEmbedSettingsCardsItem, OptionalEmbedSettingsCardsItem):
    pass
