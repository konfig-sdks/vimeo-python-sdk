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


class RequiredLiveEventAutomatedClosedCaptionsEditPreferenceForEventRequest1(TypedDict):
    # Whether automated closed captions are enabled for the event.
    auto_cc_enabled: bool

class OptionalLiveEventAutomatedClosedCaptionsEditPreferenceForEventRequest1(TypedDict, total=False):
    # A comma-separated list of keywords that improve the quality of the automated closed captions.
    auto_cc_keywords: str

    # The language in which the automated closed captions appear.  Option descriptions:  * `de-DE` - The language is German.  * `en-US` - The language is English.  * `es-ES` - The language is Spanish.  * `fr-FR` - The language is French.  * `pt-BR` - The language is Portuguese. 
    auto_cc_lang: str

class LiveEventAutomatedClosedCaptionsEditPreferenceForEventRequest1(RequiredLiveEventAutomatedClosedCaptionsEditPreferenceForEventRequest1, OptionalLiveEventAutomatedClosedCaptionsEditPreferenceForEventRequest1):
    pass
