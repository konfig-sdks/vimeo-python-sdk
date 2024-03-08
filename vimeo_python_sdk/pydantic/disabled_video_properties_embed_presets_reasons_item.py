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


class DisabledVideoPropertiesEmbedPresetsReasonsItem(BaseModel):
    # The icon that represents the reason why embed presets are disabled.  Option descriptions:  * `clock` - The reason is represented by a clock icon.  * `create` - The reason is represented by a create icon.  * `image` - The reason is represented by an image icon.  * `theme` - The reason is represented by a theme icon. 
    icon: Literal["clock", "create", "image", "theme"] = Field(alias='icon')

    # A user-deliverable message of why embed presets are disabled.
    message: str = Field(alias='message')
    class Config:
        arbitrary_types_allowed = True
