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


class UploadVideoRequestEmbedTitle(BaseModel):
    # How to handle the video title in the title bar of the embeddable player.  Option descriptions:  * `hide` - Hide the video title.  * `show` - Show the video title.  * `user` - Enable the user to decide. 
    name: typing.Optional[Literal["hide", "show", "user"]] = Field(None, alias='name')

    # How to handle the owner information in the title bar of the embeddable player.  Option descriptions:  * `hide` - Hide the owner info.  * `show` - Show the owner info.  * `user` - Enable the user to decide. 
    owner: typing.Optional[Literal["hide", "show", "user"]] = Field(None, alias='owner')

    # How to handle the owner portrait in the title bar of the embeddable player.  Option descriptions:  * `hide` - Hide the portrait.  * `show` - Show the portrait.  * `user` - Enable the user to decide. 
    portrait: typing.Optional[Literal["hide", "show", "user"]] = Field(None, alias='portrait')
    class Config:
        arbitrary_types_allowed = True
