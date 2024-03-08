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


class LiveEventAutomatedClosedCaptions(BaseModel):
    # Whether automated closed captions can be enabled.
    auto_cc_can_be_enabled: bool = Field(alias='auto_cc_can_be_enabled')

    # Whether the option for automated closed captions is enabled.
    auto_cc_enabled: bool = Field(alias='auto_cc_enabled')

    # Whether automated closed captions are unlimited for the user.
    auto_cc_is_unlimited: bool = Field(alias='auto_cc_is_unlimited')

    # A comma-separated list of keywords for enhancing the speech detection of automated closed captions.
    auto_cc_keywords: str = Field(alias='auto_cc_keywords')

    # The language of the automated closed captions.
    auto_cc_language: typing.Optional[str] = Field(alias='auto_cc_language')

    # The number of minutes remaining for automated closed captions in the user's current period.
    auto_cc_remaining: typing.Union[int, float] = Field(alias='auto_cc_remaining')

    # The ID of the event.
    event_id: typing.Union[int, float] = Field(alias='event_id')
    class Config:
        arbitrary_types_allowed = True
