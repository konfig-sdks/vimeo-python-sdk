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


class OttDestination(BaseModel):
    # The OTT destination's canonical relative URI.
    id: str = Field(alias='id')

    # The ID of the OTT channel.
    ott_channel_id: typing.Union[int, float] = Field(alias='ott_channel_id')

    # The name of the OTT channel.
    ott_channel_name: str = Field(alias='ott_channel_name')

    # The subdomain of the OTT channel.
    ott_channel_subdomain: str = Field(alias='ott_channel_subdomain')

    # The ID of the OTT event.
    ott_event_id: typing.Union[int, float] = Field(alias='ott_event_id')

    # The ID of the current recurring live event.
    recurring_live_event_id: typing.Union[int, float] = Field(alias='recurring_live_event_id')
    class Config:
        arbitrary_types_allowed = True
