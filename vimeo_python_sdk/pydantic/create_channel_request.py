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


class CreateChannelRequest(BaseModel):
    # The name of the channel.
    name: str = Field(alias='name')

    # The privacy level of the channel.  Option descriptions:  * `anybody` - Anyone can access the channel.  * `moderators` - Only moderators can access the channel.  * `user` - Only moderators and designated users can access the channel. 
    privacy: Literal["anybody", "moderators", "user"] = Field(alias='privacy')

    # The description of the channel.
    description: typing.Optional[str] = Field(None, alias='description')

    # The link to access the channel. You can use a custom name in the URL in place of a numeric channel ID, as in `/channels/{url_custom}`.
    link: typing.Optional[str] = Field(None, alias='link')
    class Config:
        arbitrary_types_allowed = True
