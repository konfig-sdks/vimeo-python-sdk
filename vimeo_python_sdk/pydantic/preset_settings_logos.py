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


class PresetSettingsLogos(BaseModel):
    # Whether the preset includes custom logo settings.
    custom: bool = Field(alias='custom')

    # Whether the present includes sticky custom logo settings.
    sticky_custom: bool = Field(alias='sticky_custom')

    # Whether the preset includes Vimeo logo settings.
    vimeo: bool = Field(alias='vimeo')
    class Config:
        arbitrary_types_allowed = True
