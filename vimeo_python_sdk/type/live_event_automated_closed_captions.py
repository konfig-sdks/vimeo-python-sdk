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


class RequiredLiveEventAutomatedClosedCaptions(TypedDict):
    # Whether automated closed captions can be enabled.
    auto_cc_can_be_enabled: bool

    # Whether the option for automated closed captions is enabled.
    auto_cc_enabled: bool

    # Whether automated closed captions are unlimited for the user.
    auto_cc_is_unlimited: bool

    # A comma-separated list of keywords for enhancing the speech detection of automated closed captions.
    auto_cc_keywords: str

    # The language of the automated closed captions.
    auto_cc_language: typing.Optional[str]

    # The number of minutes remaining for automated closed captions in the user's current period.
    auto_cc_remaining: typing.Union[int, float]

    # The ID of the event.
    event_id: typing.Union[int, float]

class OptionalLiveEventAutomatedClosedCaptions(TypedDict, total=False):
    pass

class LiveEventAutomatedClosedCaptions(RequiredLiveEventAutomatedClosedCaptions, OptionalLiveEventAutomatedClosedCaptions):
    pass
