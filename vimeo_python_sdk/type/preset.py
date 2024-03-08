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

from vimeo_python_sdk.type.preset_metadata import PresetMetadata
from vimeo_python_sdk.type.preset_settings import PresetSettings
from vimeo_python_sdk.type.user import User

class RequiredPreset(TypedDict):
    metadata: PresetMetadata

    # The display name of the preset group.
    name: str

    settings: PresetSettings

    # The canonical relative URI of the preset object.
    uri: str

    # The owner of the preset.
    user: User

class OptionalPreset(TypedDict, total=False):
    pass

class Preset(RequiredPreset, OptionalPreset):
    pass
