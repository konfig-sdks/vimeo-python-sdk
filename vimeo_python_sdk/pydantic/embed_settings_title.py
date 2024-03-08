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


class EmbedSettingsTitle(BaseModel):
    # How the embeddable player handles the video title.  Option descriptions:  * `hide` - The title is hidden.  * `show` - The title is shown.  * `user` - The title can be toggled to `show` or `hide` by the user. 
    name: Literal["hide", "show", "user"] = Field(alias='name')

    # How the embeddable player handles the video owner's information.  Option descriptions:  * `hide` - The owner's information is hidden.  * `show` - The owner's information is shown.  * `user` - The owner's information can be toggled to `show` or `hide` by the user. 
    owner: Literal["hide", "show", "user"] = Field(alias='owner')

    # How the embeddable player handles the video owner's portrait.  Option descriptions:  * `hide` - The owner's portrait is hidden  * `show` - The owner's portrait is shown.  * `user` - The owner's portrait can be toggled to `show` or `hide` by the user. 
    portrait: Literal["hide", "show", "user"] = Field(alias='portrait')
    class Config:
        arbitrary_types_allowed = True
