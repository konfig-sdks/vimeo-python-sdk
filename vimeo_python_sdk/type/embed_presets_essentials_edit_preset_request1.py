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


class RequiredEmbedPresetsEssentialsEditPresetRequest1(TypedDict):
    pass

class OptionalEmbedPresetsEssentialsEditPresetRequest1(TypedDict, total=False):
    # What to do with the outro.  Option descriptions:  * `nothing` - Disable the outro. 
    outro: str

class EmbedPresetsEssentialsEditPresetRequest1(RequiredEmbedPresetsEssentialsEditPresetRequest1, OptionalEmbedPresetsEssentialsEditPresetRequest1):
    pass
