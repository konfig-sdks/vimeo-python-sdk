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


class LiveEssentialsCreateEventRequestStreamEmbed(BaseModel):
    # The embed permission level for the event.  Option descriptions:  * `private` - Only the user can embed the event.  * `public` - Anyone can embed the event.  * `whitelist` - Only those on the whitelist can embed the event. 
    embed: typing.Optional[Literal["private", "public", "whitelist"]] = Field(None, alias='embed')
    class Config:
        arbitrary_types_allowed = True
