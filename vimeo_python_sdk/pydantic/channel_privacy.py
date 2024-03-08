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


class ChannelPrivacy(BaseModel):
    # The privacy setting of the channel.  Option descriptions:  * `anybody` - Anyone can access the channel. This privacy setting appears as `Public` on the Vimeo front end.  * `moderators` - Only moderators can access the channel.  * `users` - Only registered users can access the channel. _This field is deprecated._ 
    view: Literal["anybody", "moderators", "users"] = Field(alias='view')
    class Config:
        arbitrary_types_allowed = True
