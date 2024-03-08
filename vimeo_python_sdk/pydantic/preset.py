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

from vimeo_python_sdk.pydantic.preset_metadata import PresetMetadata
from vimeo_python_sdk.pydantic.preset_settings import PresetSettings
from vimeo_python_sdk.pydantic.user import User

class Preset(BaseModel):
    metadata: PresetMetadata = Field(alias='metadata')

    # The display name of the preset group.
    name: str = Field(alias='name')

    settings: PresetSettings = Field(alias='settings')

    # The canonical relative URI of the preset object.
    uri: str = Field(alias='uri')

    # The owner of the preset.
    user: User = Field(alias='user')
    class Config:
        arbitrary_types_allowed = True
