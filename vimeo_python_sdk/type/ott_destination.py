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


class RequiredOttDestination(TypedDict):
    # The OTT destination's canonical relative URI.
    id: str

    # The ID of the OTT channel.
    ott_channel_id: typing.Union[int, float]

    # The name of the OTT channel.
    ott_channel_name: str

    # The subdomain of the OTT channel.
    ott_channel_subdomain: str

    # The ID of the OTT event.
    ott_event_id: typing.Union[int, float]

    # The ID of the current recurring live event.
    recurring_live_event_id: typing.Union[int, float]

class OptionalOttDestination(TypedDict, total=False):
    pass

class OttDestination(RequiredOttDestination, OptionalOttDestination):
    pass
